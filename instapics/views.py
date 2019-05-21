from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm


def posts(request):
    posts = Posts.objects.all()
    return render(request,'posts.html',locals())

def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Posts.search_by_tag(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"posts":searched_posts})

    else:
        message = "Invalid input"
        return render(request,'search.html',{"message":message,})

