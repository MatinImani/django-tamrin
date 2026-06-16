"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# from django.urls import path


# from myapp import views
# # مدل جدید از فراخوانی
# from myapp.views import product


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('index/',views.main),
#     path('sum-varible/<int:a>/<int:b>', views.sumAB),
#     path('print/<str:text>/<int:n>', views.print_text_n_times),
#     path('product/<str:a>/<str:b>/<str:c>', product),
#     path('buy/<str:price>/<str:mymoney>', views.buy),
#     path('units/',views.get_unit),
#     path('unitsmodular/',views.get_unit_modular),
#     path('hello/<str:username>', views.hello_user),
#     path('library/<str:member_id>', views.library_member),
   
# ]


from django.urls import path, include # حتما include رو ایمپورت کن





urlpatterns = [
    path('admin/', admin.site.urls),
    
    # هر چیزی که با myapp/ شروع بشه میره توی urls.pyِ اپ myapp
    path('myapp/', include('myapp.urls')), 
    
    # هر چیزی که با loan/ شروع بشه میره توی urls.pyِ اپ loan_app
    path('loan/', include('loan_app.urls')), 


    path('products/', include('products_app.urls')),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
