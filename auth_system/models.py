from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, verbose_name="Номер телефону:")
    age = models.PositiveIntegerField(blank=True, null=True, verbose_name="Вік:")

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.phone_number}"