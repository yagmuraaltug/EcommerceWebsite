from re import search
from sys import implementation
from django.contrib import admin
from .models import Category, Order, Product

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "Shoping"
admin.site.index_title = "Manage Website"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'description', 'category')
    search_fields = ('title', )
    actions = ('change_category_to_default',)
   # fields = ('title','price',)
    list_editable = ('price','category',)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)

# Register your models here.
