from django.contrib import admin

# Register your models here.

from basket.models import Basket

class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('exhibits', 'quantity', 'create_timestamp', 'update_timestamp')
    readonly_fields = ('create_timestamp', 'update_timestamp')
    extra = 1