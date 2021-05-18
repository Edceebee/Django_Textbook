from django.shortcuts import render
from django.views.generic import DetailView, ListView

from blog.models import BlogPost


#
# def home(request):
#     details = BlogPost.objects.all()
#     context = {
#         'details': details
#     }
#     return render(request, "blog/home.html", context)
#
class About(ListView):
    model = BlogPost
    template_name = 'blog/about.html'


class Home(ListView):
    model = BlogPost
    template_name = 'blog/home.html'


class Post(ListView):  # new
    model = BlogPost
    template_name = 'blog/post.html'
