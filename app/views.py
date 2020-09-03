from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    template = 'app/index.html'
    context = {

    }
    return render(request, template, context)

def product(request):
    template = 'app/product.html'
    context = {

    }
    return render(request, template, context)

def category(request):
    template = 'app/category.html'
    context = {

    }
    return render(request, template, context)