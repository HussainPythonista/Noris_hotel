from django.contrib import admin
from django.contrib.admin.sites import site
from .models import AdminStuff,Room
# Register your models here.
admin.site.register(AdminStuff)
admin.site.register(Room)
