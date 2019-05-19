from django.contrib import admin
from .models import Profile,tag,Posts

admin.site.register(Profile)
admin.site.register(Posts)
admin.site.register(tag)
