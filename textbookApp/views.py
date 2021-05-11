from django.db.models.functions import text
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Post
from textbookApp.models import Post


def home(request):
    texts = Post.objects.all()
    context = {
        'texts': texts
    }
    return render(request, "textbookApp/home.html", context)


def about(request):
    return render(request, "textbookApp/about.html")
