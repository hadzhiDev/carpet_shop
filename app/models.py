from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampAbstractModel(models.Model):
    created_at = models.DateTimeField('дата добавление', auto_now_add=True)
    updated_at = models.DateTimeField('дата изменения', auto_now=True)

    class Meta:
        abstract = True
