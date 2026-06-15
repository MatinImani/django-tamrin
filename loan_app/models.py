from django.db import models

# Create your models here.



class Member(models.Model):
    first_name=models.CharField(max_length=150)
    last_name=models.CharField(max_length=150)
    birth_date=models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    year=models.IntegerField()

    loan_date=models.DateTimeField(auto_now_add=True,verbose_name='تاریخ امانت')
    
    #Memmber اضافه کردن کلید خارجی به مدل
    member =models.ForeignKey(Member,on_delete=models.CASCADE,related_name='books')
    
    def __str__(self):
        return self.title  