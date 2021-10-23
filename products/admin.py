from django.contrib import admin
from .models import *



admin.site.register(Brand)
admin.site.register(Quantity)

admin.site.register(Size)


# CategoryAdmin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','image_tag')
admin.site.register(Category,CategoryAdmin)

# Color Admin
class ColorAdmin(admin.ModelAdmin):
    list_display = ('color_name','color_bg')
admin.site.register(Color,ColorAdmin)

# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name','brand_type','price','color_type','size_type','quantity_type','stock','status')
    list_editable = ('status',)
admin.site.register(Product,ProductAdmin)

# ProductImage Admin
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id','product')
admin.site.register(ProductImage,ProductImageAdmin)


