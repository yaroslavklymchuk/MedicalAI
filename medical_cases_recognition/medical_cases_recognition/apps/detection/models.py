from django.db import models
from multiselectfield import MultiSelectField


class DetectionModel(models.Model):
    OPTIONS = (
        ('Pneumonia', "Pn"),
        ('Diabetic', "Di")
    )
    name = models.CharField(name='name', max_length=150)
    email = models.EmailField(name='email')
    subject = MultiSelectField(choices=OPTIONS)
    img_to_detect = models.ImageField(verbose_name='Drop Files', upload_to='images', null=True)

