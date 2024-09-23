from django.shortcuts import render, redirect
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


@login_required(login_url="/login")
def show_main(req):
    products = Product.objects.filter(user=req.user)

    context = {
        # User credentials
        'name': req.user.username,
        # Data
        "products": products,
        # Cookies
        'last_login': req.COOKIES['last_login'],
        # My credentials
        "student_name": "Daffa Abhipraya Putra",
        "student_id": "2306245131",
        "student_class": "PBP D",
    }

    return render(req, "main.html", context)


def create_product(req):
    form = ProductForm(req.POST or None)

    if form.is_valid() and req.method == "POST":
        mood_entry = form.save(commit=False)
        mood_entry.user = req.user
        mood_entry.save()
        return redirect('main:show_main')

    context = {"form": form}
    return render(req, "create_product.html", context)


def show_xml(req):
    data = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", data), content_type="application/xml"
    )


def show_json(req):
    data = Product.objects.all()
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
        form = AuthenticationForm(req)
    context = {"form": form}
    return render(req, "login.html", context)


def logout_user(req):
    logout(req)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response