from django.db import models

# Create your models here.
class Course(models.Model):
    teacher=models.CharField(max_length=150)
    title=models.CharField(max_length=150)
    description=models.TextField()