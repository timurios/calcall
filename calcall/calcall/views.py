from django.shortcuts import render, HttpResponse, redirect

def calcall(request):
    return render(request,"tmp/index.html")
    