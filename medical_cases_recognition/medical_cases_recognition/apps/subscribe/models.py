from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django_countries.fields import CountryField
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User


class General(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    age = models.IntegerField(verbose_name='age', max_length=200)
    country = CountryField(verbose_name='country', multiple=True)


