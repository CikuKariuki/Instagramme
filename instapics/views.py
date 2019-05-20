from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Posts

# @login_required(login_url='/accounts/login/')
def posts(request):
    posts = Posts.objects.all()
    return render(request,'posts.html',{"posts":posts})

def search_results(request):
    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Posts.search_by_tag(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"posts":searched_posts})

    else:
        message = "Invalid input"
        return render(request,'search.html',{"message":message,})

