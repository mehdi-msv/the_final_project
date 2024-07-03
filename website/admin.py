from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','subject','created_date')
    search_fields = ('email','subject','message')
    list_filter = ['email']
admin.site.register(Newsletter)