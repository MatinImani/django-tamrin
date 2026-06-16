# products_app/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

def product_add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        img = request.FILES.get('img')
        
        if title and img:
            Product.objects.create(title=title, img=img)
            messages.success(request, '✅ محصول با موفقیت اضافه شد')
            return redirect('product_add')
        else:
            messages.error(request, '❌ لطفاً عنوان و تصویر را وارد کنید')
    
    # نمایش همه محصولات (جدیدترین اول)
    products = Product.objects.all().order_by('-id')
    return render(request, 'products_app/productAdd.html', {'products': products})