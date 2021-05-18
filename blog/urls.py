from django.urls import path

from blog.views import Home, About, Post

urlpatterns = [

    path('', Home.as_view(), name='home'),
    path('about/', About.as_view(), name='about'),
    path('post/', Post.as_view(), name='post')

]
