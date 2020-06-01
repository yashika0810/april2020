from django.db import models

# Create your models here.
class Login(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=40, unique=True)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.name




class Session(models.Model):
    session=models.CharField(max_length=30,unique=True)

    def __str__(self):
        return self.session

class Student(models.Model):
    name=models.CharField(max_length=30,unique=False)
    session=models.ForeignKey("Session", on_delete=models.PROTECT)


    def __str__(self):
        return self.name


