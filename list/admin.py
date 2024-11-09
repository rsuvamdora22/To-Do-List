from django.contrib import admin

from . models import Do,ToDo
# Register your models here.
class All(admin.ModelAdmin):
    list = ['Title','Description','user']
admin.site.register(Do)
admin.site.register(ToDo)