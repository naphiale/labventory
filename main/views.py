from django.shortcuts import render, redirect
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    # Data produk dalam bentuk list of dictionaries
    products = Product.objects.all()

    products = [
        {
            'name': 'Microscope X200',
            'price': 2000000,
            'description': 'High-quality microscope suitable for research and education purposes.',
            'rating': 4
        },
        {
            'name': 'Centrifuge 3000 RPM',
            'price': 5000000,
            'description': 'High-speed centrifuge for separating fluids and gases based on density.',
            'rating': 5
        },
        {
            'name': 'Autoclave Sterilizer',
            'price': 7000000,
            'description': 'Compact autoclave for sterilization in laboratories.',
            'rating': 4
        },
    ]
    
    # Context untuk dikirimkan ke template
    context = {
        'npm': '2306224556',
        'name': 'Nafia Levana Aulia',
        'class': 'PBP F',
        'products': products
    }
    
    # Merender template main.html dengan context
    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
