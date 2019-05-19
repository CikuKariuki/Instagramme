from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls,name=admin),
    url(r'',include('instapics.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    
]
