from django.db import models

# Create your models here.

class place(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

class blog(models.Model):
    date=models.DateField()
    month=models.DateTimeField()
    tittle=models.CharField(max_length=100)
    sub_tittle=models.CharField(max_length=150)
    img=models.ImageField(upload_to='pictures')
    desc=models.TextField()


