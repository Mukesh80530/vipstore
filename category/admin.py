from django.contrib import admin
from .models import Category, Subcategory, Product


class CategoryAdmin(admin.ModelAdmin):
    pass


# class SubcategoryAdmin(admin.ModelAdmin):
#     pass


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Category, CategoryAdmin)
# admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)

admin.site.site_header = "Shakhu admin"
admin.site.site_title = "Always with us"
admin.site.index_title = "Shakhu Store"
