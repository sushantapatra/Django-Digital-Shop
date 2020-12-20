from django.db import models

class User(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=150, unique=True)
    phone=models.CharField(max_length=13)
    password=models.CharField(max_length=250)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    