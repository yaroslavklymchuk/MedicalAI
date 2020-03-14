from django.db import models


class DetectionModel(models.Model):
    name = models.CharField(name='name', max_length=150)
    email = models.EmailField(name='email')
    subject = models.CharField(name='subject', max_length=150)
    img_to_detect = models.ImageField(verbose_name='Drop Files', upload_to='images', null=True)

