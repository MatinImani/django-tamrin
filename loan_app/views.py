from django.shortcuts import render
from .models import Book,Member

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
