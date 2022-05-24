from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def kvp(request):
    return render(request, 'kvp.html')

def product(request):
    return render(request, 'product.html')

def product_ui(request):
    return render(request, 'ui.html')

def product_ia(request):
    return render(request, 'ia.html')

def product_interactions(request):
    return render(request, 'interactions.html')

def business_model(request):
    return render(request, 'business-model.html')