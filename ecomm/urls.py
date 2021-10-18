"""ecomm URL Configuration
"""

from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cart.urls')),
    path('api/', include('products.urls')),
    path('api/accounts/', include('ecomm_auth.urls'))
]
