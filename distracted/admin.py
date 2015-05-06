from django.contrib import admin

# Register your models here.
from .models import Series,Actor,Roles

admin.site.register(Series)
admin.site.register(Actor)
admin.site.register(Roles)