from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone


class Detection(models.Model):
    OPTIONS = (
        ('Pneumonia', "Pn"),
        ('Diabetic', "Di"),
        ('Hemorrhage', "He")
    )
    first_name = models.CharField(verbose_name='first name', default='User', max_length=500)
    last_name = models.CharField(verbose_name='last name', default='User', max_length=500)
    email = models.EmailField(verbose_name='email')
    subject = MultiSelectField(verbose_name='subject', choices=OPTIONS)
    img_to_detect = models.ImageField(verbose_name='Drop Files', upload_to='images', null=True)
    created = models.DateTimeField(verbose_name='created date', default=timezone.now())


class Results(models.Model):
    email = models.EmailField(verbose_name='email', null=True)
    result = models.CharField(verbose_name='result', max_length=200, null=True)
    created = models.DateTimeField(verbose_name='result created date', default=timezone.now(), null=True)
