from django.conf.urls import url
from . import views

urlpatterns=[
    url('^posts/$',views.posts,name='posts')
]