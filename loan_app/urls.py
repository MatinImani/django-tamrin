# loan_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('member/<int:member_id>', views.member_books),
    path('bookdetail/<int:book_id>', views.book_detail),
]