from django.shortcuts import render, redirect, reverse
from main.forms import ProductForm
from .models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url="/login")
def show_main(req):
    context = {
        # User credentials
        "name": req.user.username,
        # Cookies
        "last_login": req.COOKIES["last_login"],
        # My credentials
        "student_name": "Daffa Abhipraya Putra",
        "student_id": "2306245131",
        "student_class": "PBP D",
        # Page
        # "current_page": "main",
    }

    return render(req, "main.html", context)


def create_product(req):
    form = ProductForm(req.POST or None)

    if form.is_valid() and req.method == "POST":
        product = form.save(commit=False)
        product.user = req.user
        product.save()
        return redirect('main:show_main')

    context = {"form": form}
    return render(req, "create_product.html", context)


def show_xml(req):
    data = Product.objects.filter(user=req.user)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(req):
    data = Product.objects.filter(user=req.user)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def show_xml_by_id(req, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json_by_id(req, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(
        serializers.serialize("json", data), content_type="application/json"
    )


def register(req):
    form = UserCreationForm()

    if req.method == "POST":
        form = UserCreationForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req, "Your account has been successfully created!")
            return redirect("main:login")
    context = {"form": form}
    return render(req, "register.html", context)


def login_user(req):
    if req.method == "POST":
        form = AuthenticationForm(data=req.POST)

        if form.is_valid():
            user = form.get_user()
            login(req, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(req, "Invalid username or password. Please try again.")

    else:
        form = AuthenticationForm(req)
    context = {"form": form}
    return render(req, "login.html", context)


def logout_user(req):
    logout(req)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response


@login_required(login_url="/login")
def edit_product(req, id):
    product = Product.objects.get(pk=id)
    form = ProductForm(req.POST or None, instance=product)

    if form.is_valid() and req.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:show_main"))

    context = {"form": form}
    return render(req, "edit_product.html", context)


@login_required(login_url="/login")
def delete_product(req, id):
    product = Product.objects.get(pk=id)
    product.delete()
    return HttpResponseRedirect(reverse("main:show_main"))


@csrf_exempt
@require_POST
def add_product_ajax(req):
    name = strip_tags(req.POST.get("name"))
    description = strip_tags(req.POST.get("description"))
    price = req.POST.get("price")
    stock = req.POST.get("stock")
    user = req.user

    new_product = Product(
        name=name, description=description, price=price, stock=stock, user=user
    )
    new_product.save()

    return HttpResponse(b"CREATED", status=201)
