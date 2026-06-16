from django.shortcuts import render
from .models import Book,Member
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def member_books(request,member_id):
    member=Member.objects.filter(id=member_id).first()
    if member==None:
        return render(request,'loan_app/memberNotExists.html')
    else:
        return render(request,'loan_app/memberBooks.html', context={'member':member})


# {'book':book} این خط یعنی آبجکت بوکی که دارم از این به بعد توی تمپلیت با اسم بوک خونده میشه
def book_detail(request,book_id):
    book=Book.objects.filter(id=book_id).first()
    if book==None:
        return render(request,'loan_app/bookNotExists.html')
    else:
        return render(request,'loan_app/bookDetail.html', context={'book':book})




# http://127.0.0.1:8000/loan/bookadd/

# def book_add(request):
#     title=request.GET.get('title')
#     author=request.GET.get('author')
#     year=request.GET.get('year')

#     if title !=None and author !=None and year !=None:
#         Book.objects.create(title=title, author=author, year=year)
#         # messges.success(request,'کتاب با موفقیت اضافه شد')
#         return HttpResponse('کتاب با موفقیت اضافه شد')

#     return render(request,'loan_app/bookAdd.html')

def book_add(request):
    if request.method == 'GET':  # ✅ POST به جای GET
        title = request.GET.get('title')
        author = request.GET.get('author')
        year = request.GET.get('year')

        if title and author and year:
            Book.objects.create(title=title, author=author, year=year)
            messages.success(request, 'کتاب با موفقیت اضافه شد')
            # return redirect('book_list') 

    return render(request, 'loan_app/bookAdd.html')




