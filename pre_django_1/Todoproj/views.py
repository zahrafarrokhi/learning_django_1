from django.shortcuts import render,HttpResponse

def home(requset):
    return HttpResponse('welcome todo!')