# products_app/urls.py
from django.urls import path
from . import views
# ✅ این خط رو اضافه کن

urlpatterns = [
    path('add/', views.product_add, name='product_add'),
]