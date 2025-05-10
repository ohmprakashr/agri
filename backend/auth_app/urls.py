# auth_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('api/prices/', views.crop_product_list_create, name='crop-product-list_create'),
]
# from django.urls import path
# from .views import crop_product_list_create

# urlpatterns = [
#     path('api/prices/', crop_product_list_create.as_views(), name='crop_product_list_create'),
# ]
