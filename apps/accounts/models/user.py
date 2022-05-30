from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.accounts.managers.user import CustomUserManager
from apps.utils.mixins import ModelMixin
from apps.utils.validators import phone_regex


class User(ModelMixin, AbstractUser):

    class Role(models.TextChoices):
        STUDENT = 'student'
        TEACHER = 'teacher'
        ADMIN = 'admin'
        SUPERADMIN = 'superadmin'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15,
                                    validators=(phone_regex,))
    second_phone_number = models.CharField(max_length=15, blank=True,
                                           validators=(phone_regex,))
    birthday = models.DateField()
    address = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=50, choices=Role.choices)
    image = models.ImageField(upload_to='photos/%y/%m/%d',
                              null=True, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    bank_account = models.CharField(max_length=16, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []


    def __str__(self):
        return f"{self.role}. {self.first_name} {self.last_name}"
