from django.db import models
from multiselectfield import MultiSelectField
from django.utils import timezone


class DetectionModel(models.Model):
    OPTIONS = (
        ('Pneumonia', "Pn"),
        ('Diabetic', "Di"),
        ('Hemorrhage', "He")
    )
    name = models.CharField(name='name', max_length=150)
    email = models.EmailField(name='email')
    subject = MultiSelectField(choices=OPTIONS)
    img_to_detect = models.ImageField(verbose_name='Drop Files', upload_to='images', null=True)
    created = models.DateTimeField('created date', default=timezone.now())


class ResultsModel(models.Model):
    email = models.EmailField(name='email', null=True)
    result = models.CharField(name='result', max_length=200, null=True)
    created = models.DateTimeField('result created date', default=timezone.now(), null=True)
