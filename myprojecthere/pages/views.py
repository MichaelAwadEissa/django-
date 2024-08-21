from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.



def index (request):
    return render (request,'pages/index.html',{'name':'michael awad eissa zaki','age':'346543568865312'})

def about (request):
    return render (request,'pages/about.html',{'name':'michael awad eissa zaki','age':'346543568865312'})

