from django.db import models
from django.contrib.auth.models import AbstractUser

from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from app.models import TimeStampAbstractModel


class Employer(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Работодатель'
        verbose_name_plural = 'Работодатели'

    full_name = models.CharField(max_length=200, verbose_name='имя')
    avatar = ResizedImageField(size=[500, 500], crop=['middle', 'center'], upload_to='avatars/',
                               force_format='WEBP', quality=90, verbose_name='аватарка',
                               null=True, blank=True)
    phone = PhoneNumberField(max_length=100, unique=True, verbose_name='номер телефона', blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    paid_date = models.DateField()

    def __int__(self):
        return f'{self.full_name}'


def get_expire_date():
    return timezone.now() + timezone.timedelta(days=1)


class UserResetPassword(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Ключ для логина'
        verbose_name_plural = 'Ключи для логина'
        ordering = ('-created_at', '-updated_at')

    employer = models.OneToOneField('accounts.Employer', on_delete=models.CASCADE, verbose_name='пользователь',
                                    null=True, blank=True)
    if not employer:
        employee = models.OneToOneField('accounts.Employee', on_delete=models.CASCADE, verbose_name='пользователь',
                                    null=True, blank=True)
    key = models.UUIDField('ключ', default=uuid4, editable=False, unique=True)
    expire_date = models.DateTimeField('срок действия', default=get_expire_date)

    def __str__(self):
        return f'{self.user}'

    def is_expired(self):
        return timezone.now() > self.expire_date


class Employee(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ('-created_date',)

    name = models.CharField(max_length=200, verbose_name='имя')
    phone = PhoneNumberField(max_length=100, unique=True, verbose_name='номер телефона', blank=True, null=True)
    avatar = ResizedImageField(size=[500, 500], crop=['middle', 'center'], upload_to='avatars/',
                               force_format='WEBP', quality=90, verbose_name='аватарка',
                               null=True, blank=True)
    employer = models.ForeignKey('accounts.Employer', on_delete=models.CASCADE, related_name='employee',
                                 verbose_name='работодатель')
    # accept = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} - {self.phone}'



