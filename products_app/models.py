from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=150)
    img=models.ImageField(upload_to='products_app/image', null=True,blank=True)

    def __str__(self):
        return self.title  
