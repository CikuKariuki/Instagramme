from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/accounts/login/')
def posts(request):
    posts.objects.all()
    return render(request,'posts.html')

