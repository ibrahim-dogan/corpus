from django.contrib import admin
from .models import Category, URL

# Register your models here.
admin.site.register(URL)
admin.site.register(Category)
