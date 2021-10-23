from django.contrib import admin
from .models import *



# Cart Admin
class CartAdmin(admin.ModelAdmin):
    list_display = ('user','ordered','total_price')
admin.site.register(Cart,CartAdmin)

# CartItems Admin
class CartItemsAdmin(admin.ModelAdmin):
    list_display = ('user','cart','product','price','isOrder','quantity')
admin.site.register(CartItems,CartItemsAdmin)

# Orders Admin
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('user','cart','amount','is_paid','order_id','payment_id','payment_signature')
admin.site.register(Orders,OrdersAdmin)

# OrdersItems Admin
class OrderedItemsAdmin(admin.ModelAdmin):
    list_display = ('user','order')
admin.site.register(OrderedItems,OrderedItemsAdmin)

# ProductReview Admin
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ('user','product','review_text','review_rating')
admin.site.register(ProductReview,ProductReviewAdmin)