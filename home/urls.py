from django.urls import path
from .views import *
from home import views



urlpatterns = [
    path('', views.home, name='home'),
    #path('search', views.search, name='search'),
    path('category-list', views.category_list, name='category-list'),
    path('brand-list', views.brand_list, name='brand-list'),
    #path('product-list', views.product_list, name='product-list'),
    #path('product/<int:id>', views.product_detail, name='product-detail'),
]