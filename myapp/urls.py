# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.main),
    path('sum-varible/<int:a>/<int:b>', views.sumAB),
    path('print/<str:text>/<int:n>', views.print_text_n_times),
    path('product/<str:a>/<str:b>/<str:c>', views.product),
    path('buy/<str:price>/<str:mymoney>', views.buy),
    path('units/', views.get_unit),
    path('unitsmodular/', views.get_unit_modular),
    path('hello/<str:username>', views.hello_user),
]