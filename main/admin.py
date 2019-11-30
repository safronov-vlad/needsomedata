from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(UserLow)

admin.site.register(Trichcode)

admin.site.register(UserBussines)

admin.site.register(Request)

admin.site.register(Zhilishniki)