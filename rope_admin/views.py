# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from rope_admin.models import Products

def showLogin(request):
    products = list(Products.objects.filter().values_list('image', flat=True).distinct())
    return render(request, 'index.html', {'products': products})
 
# Create your views here.
def getLogin(request):
    name = request.POST['name']
    pwd = request.POST['pwd']
    if name and pwd:
        user = Register.objects.filter(username= name,password = pwd)
        if user:
            return HttpResponse("Dashboard")
        else:
            return HttpResponse("Please register now")
    else:
        return HttpResponse("Please Enter both Username & Password")

    return HttpResponse("Success")

def user_login(request):
    return HttpResponse("sucess")
