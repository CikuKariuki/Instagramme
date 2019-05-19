from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Posts

# @login_required(login_url='/accounts/login/')
def posts(request):
    images = Posts.objects.all()
    return render(request,'posts.html',{"images":images})

