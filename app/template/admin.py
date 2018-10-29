from django.contrib import admin

from .models import Entity

admin.register(Entity)(admin.ModelAdmin)
