from django.contrib import admin
from .models import First,Place
from.models import Second

# Register your models here.
admin.site.register(Place)
admin.site.register(Second)
admin.site.register(First)
