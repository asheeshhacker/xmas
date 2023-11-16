from django.contrib import admin
from .models import form1
# Register your models here.
class myform1(admin.ModelAdmin):
    list_display = ['name','wish','address']
    search_fields = ['name']
admin.site.register(form1)