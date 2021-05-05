from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


def home(request):
    # return HttpResponse("Hello world!")
    return render(request, "textbookApp/home.html")


def about(request):
    return render(request, "textbookApp/about.html")
