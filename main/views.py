from django.shortcuts import render, redirect
from main.forms import ProductForm
from .models import Product
from django.http import HttpResponse
from django.core import serializers


def show_main(req):
    products = Product.objects.all()

    context = {
        # Credentials
        "student_name": "Daffa Abhipraya Putra",
        "student_id": "2306245131",
        "student_class": "PBP D",
        # Data
        "products": products,
    }

    return render(req, "main.html", context)


def create_product(req):
    form = ProductForm(req.POST or None)

    if form.is_valid() and req.method == "POST":
        form.save()
        return redirect("main:show_main")

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
