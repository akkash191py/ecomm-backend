from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(QuantityVariant)
admin.site.register(ColorVarient)
admin.site.register(SizeVarient)
admin.site.register(ProductImages)
