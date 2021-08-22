from django.contrib import admin
from .models import *
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('caption','image')
admin.site.register(Imageupload,ImageAdmin)
