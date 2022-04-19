from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def kvp(request):
    return render(request, 'kvp.html')

def product(request):
    return render(request, 'product.html')