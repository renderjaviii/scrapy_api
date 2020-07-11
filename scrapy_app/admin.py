from django.contrib import admin
from scrapy_app.models import *


class AdminCategory(admin.ModelAdmin):
    search_fields = ("name",)


class AdminProduct(admin.ModelAdmin):
    list_filter = ("name", "created_at")
    date_hierarchy = "created_at"


admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
