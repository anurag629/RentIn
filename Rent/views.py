from django.shortcuts import render
from django.http import HttpResponse
from . models import Product
from math import ceil

# Create your views here.
def index(request):
    products=Product.objects.all()
    allProds=[]
    catprods=Product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n=len(prod)
        n_slides=n//4 + ceil((n/4) - (n//4))  
        allProds.append([prod , range(1,n_slides),n_slides])

    params={'allProds':allProds }
    return render(request,"Rent/index.html", params)
def about(request):
    return render(request,'Rent/about.html')   

def contact(request):
    return HttpResponse("hello contact")    

def search(request):
    return HttpResponse("hello search")    
def productview(request):
    return HttpResponse("hello productview")    

def checkout(request):
    return HttpResponse("hello checkout")    
