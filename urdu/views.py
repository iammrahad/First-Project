from django.shortcuts import render, redirect

def Home_Page(request):
    return render (request, "home.html")