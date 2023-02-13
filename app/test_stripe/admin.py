from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price']
    list_display_links = ['name',]
    search_fields = ['name',]


admin.site.register(Item, ItemAdmin)
