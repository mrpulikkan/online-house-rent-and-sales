from ast import Return
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

from.models import *
from .forms import CreateUserForm


# Create your views here.
def registerPage(request):
    form=CreateUserForm

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()


    context={'form':form}
    return render(request,'register.html',context)

def loginPage(request):
    context={}
    return render(request,'login.html',context)

def index(request):
    return render(request,'index.html')
   
def rent(request):
    products = product.objects.filter(category="rent")
    
    return render(request,'rent.html',{'products':products})

def sales(request):
    products = product.objects.filter(category="sale") 
    return render(request,'sale.html',{'products':products})

# def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    context={'customer':customer}

    return render(request,'customer.html',context)

def createOrder(request):

    context={}

    return render(request,'create_order.html',context)


    
