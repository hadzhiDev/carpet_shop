from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from django_resized import ResizedImageField
from phonenumber_field.modelfields import PhoneNumberField


class TimeStampAbstractModel(models.Model):
    created_date = models.DateTimeField('дата добавление', auto_now_add=True)
    # updated_at = models.DateTimeField('дата изменения', auto_now=True)

    class Meta:
        abstract = True


class Warehouse(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'
        ordering = ('-created_date',)

    name = models.CharField(verbose_name='название', max_length=200)
    owner = models.ForeignKey('accounts.Employer', on_delete=models.CASCADE, related_name='warehouses', verbose_name='Владелец')

    @property
    def goods_quantity(self):
        return sum(product.quantity for product in self.products.all())
    goods_quantity.fget.short_description = 'количество всех товаров'

    def __str__(self):
        return f'{self.name} - {self.goods_quantity}'


class Product(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ('-created_date',)

    name = models.CharField(verbose_name='название', max_length=200)
    quantity = models.PositiveIntegerField(verbose_name='количество товара')
    warehouse = models.ForeignKey('app.Warehouse', on_delete=models.SET_NULL, verbose_name='склад', null=True,
                                  blank=True, related_name='products')
    image = ResizedImageField(size=[300, 400], crop=['middle', 'center'], upload_to='ProductImages/', quality=100,
                              force_format='WEBP', verbose_name='фотография', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='срок годности', null=True, blank=True)
    cost_price = models.DecimalField('себестоимость', max_digits=12, decimal_places=2, default=0.0)
    sell_price = models.DecimalField('цена', max_digits=12, decimal_places=2, default=0.0)
    code = models.CharField(max_length=200, verbose_name='код товара')
    # user_id = models.ForeignKey('')
    amount_type = models.IntegerField()
    cost_currency = models.ForeignKey('app.Currency', related_name='products_cost_currency', on_delete=models.SET_NULL,
                                      null=True, blank=True)
    sell_currency = models.ForeignKey('app.Currency', related_name='products_sell_currency', on_delete=models.SET_NULL,
                                      null=True, blank=True)
    deliver_date = models.DateTimeField(verbose_name='Дата доставки', )

    def __str__(self):
        return f'{self.name} - {self.quantity}'


class History(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'История продажи'
        verbose_name_plural = 'Истории продажи'
        ordering = ('-created_date',)

    user_id = models.ForeignKey('accounts.Employer', on_delete=models.SET_NULL, null=True, blank=True)
    buyer_name = models.CharField(verbose_name='имя покупателя', max_length=300)
    debt_return_date = models.DateField(verbose_name='дата возврата долга')
    debt_currency = models.ForeignKey('app.Currency', on_delete=models.SET_NULL, null=True, blank=True)
    debt_amount = models.DecimalField(verbose_name='сумма долга', max_digits=12, decimal_places=2, default=0.0)

    def __str__(self):
        return self.buyer_name


class HistoryProduct(models.Model):
    class Meta:
        verbose_name = 'History Product'
        verbose_name_plural = 'Histories Products'

    quantity = models.PositiveIntegerField(verbose_name='количество')
    amount_type = models.IntegerField()
    code = models.CharField(max_length=200, verbose_name='код товара')
    product = models.ForeignKey('app.Product', on_delete=models.SET_NULL, null=True, blank=True)
    sold_price = models.DecimalField('цена продажи', max_digits=10, decimal_places=2, default=0.0)
    sold_currency = models.ForeignKey('app.Currency', related_name='products_sold_currency', on_delete=models.SET_NULL,
                                      null=True, blank=True)

    @property
    def name(self):
        return self.product.name


class Currency(TimeStampAbstractModel):
    class Meta:
        verbose_name = 'Валюта'
        verbose_name_plural = 'Валюты'

    name = models.CharField(max_length=200)
    ru_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} - {self.ru_name}'






