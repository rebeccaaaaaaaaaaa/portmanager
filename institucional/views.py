from django.shortcuts import render

def index(request):
    return render(request, 'site/index.html')

def advantages(request):
    return render(request, 'site/advantages.html')

def prices(request):
    return render(request, 'site/prices.html')
    
def faq(request):
    return render(request, 'site/faq.html')

def about(request):
    return render(request, 'site/about.html')

def contact(request):
    return render(request, 'site/contact.html')