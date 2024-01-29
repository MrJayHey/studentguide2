from django.contrib import admin
from .models import Hostel

class HostelAdmin(admin.ModelAdmin):
    
    list_display = ('__str__', 'coworking', 'gym')  # Fields to display in the admin list view
    list_display_links = ('__str__', 'coworking')
    list_filter = ('adress',)  # Fields to use for filtering in the admin list view

admin.site.register(Hostel, HostelAdmin)
