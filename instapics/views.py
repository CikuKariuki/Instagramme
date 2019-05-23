from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import NewPostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm


def posts(request):
    posts = Posts.objects.all()
    return render(request,'posts.html',{"posts":posts})


def search_results(request):
    if 'users' in request.GET and request.GET['users']:
        search_term = request.GET.get("users")
        searched_users = Profile.search_by_users(search_term)
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"users":searched_users})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'search.html',{"message":message,"users":searched_users})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.profile = current_user
            posts.save()
        return redirect('posts')
    else:
        form = NewPostForm()
    return render(request,'new_post.html',{"form":form})


@login_required(login_url='/accounts/login/') 
def profile(request, username):
    profile = User.objects.get(username=username)

    try:
        profile_details = Profile.get_by_id(profile.id)
    
    except:
        profile_details = Profile.filter_by_id(profile.id)
      

    posts = Posts.get_profile_posts(profile.id) 

    context = {
        "profile":profile,
        "profile_details":profile_details,
        "posts":posts,
    }

    return render(request,'profile.html',context)

