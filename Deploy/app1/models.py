from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class UserImageModel(models.Model):
    image = models.ImageField(upload_to = 'predict/')
    label = models.CharField(max_length=20,default='data')

    def __str__(self):
        return str(self.image)
