from django.contrib import admin
from .models import member

# Register your models here.

class memberAdmin(admin.ModelAdmin):
	list_display=("Name","Age","Class")
	
admin.site.register(member,memberAdmin)
