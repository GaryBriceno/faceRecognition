from django.contrib import admin
from .models import People

# Register your models here.


class PeopleAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'country_site', 'updated')
    list_filter = ('last_name', 'position', 'country_site')
    search_fields = ('first_name', 'last_name', 'country_site')
    prepopulated_fields = {'slug': ('first_name', 'last_name', )}
    date_hierarchy = 'publish'
    ordering = ['country_site', 'last_name']


admin.site.register(People, PeopleAdmin)

