from django.db import models
from django.contrib.auth.models import User

class AccountModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    phone_number = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username

class ContactModel(models.Model):
    name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    email = models.EmailField()
    telephone = models.CharField(max_length=20)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.surname