from .models import Entry, Profile
from django.contrib import admin

myModels = [Entry, Profile]
admin.site.register(myModels)

# Register your models here.
