from django.contrib import admin

# Register your models here.
from mainapp.models import ExhibitsCategories, Exhibits

admin.site.register(ExhibitsCategories)

@admin.register(Exhibits)
class Product(admin.ModelAdmin):

    list_display = ('name', 'category')
    fields = ('name', 'image', 'descriptions', 'category')
    ordering = ('name',)
    search_fields = ('name',)