from django.db import models
from washer.choices import CarTypeChoices, GenderChoices
from django.utils.translation import gettext_lazy as _


class CarWash(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    location = models.CharField(max_length=250, default='Earth')
    cabins = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('CarWash')
        verbose_name_plural = _('CarWash')


class Cabin(models.Model):
    car_wash = models.ForeignKey('washer.CarWash', on_delete=models.CASCADE, related_name="cabin")

    number = models.PositiveSmallIntegerField()
    is_empty = models.BooleanField(default=True)

    def __str__(self):
        return f'Cabin of {self.car_wash} N.{self.number}'

    class Meta:
        verbose_name = _('Cabin')
        verbose_name_plural = _('Cabins')


class Washer(models.Model):
    car_wash = models.ForeignKey(to='washer.CarWash', on_delete=models.CASCADE, related_name='washers')

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default="")
    phone_number = models.CharField(verbose_name=_('Phone number'), max_length=125, default='')
    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices,
                                              default=GenderChoices.Other)
    percentage = models.FloatField()

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = _('Washer')
        verbose_name_plural = _('Washers')


class Car(models.Model):
    name = models.CharField(max_length=10, default='')
    type = models.PositiveSmallIntegerField(choices=CarTypeChoices.choices,
                                            default=CarTypeChoices.Other)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Car')
        verbose_name_plural = _('Cars')


class Order(models.Model):
    car_wash = models.ForeignKey(to='washer.CarWash', on_delete=models.CASCADE, related_name='order')
    car = models.ForeignKey(to='washer.Car', on_delete=models.CASCADE)
    washer = models.ForeignKey(to='washer.Washer', on_delete=models.CASCADE, related_name='order')

    order_time = models.DateTimeField()
    completion_time = models.DateTimeField()

    def __str__(self):
        return f'Order of: {self.order_time}'

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')


class CarWashToType(models.Model):
    car_washer = models.ForeignKey(to='washer.CarWash', on_delete=models.CASCADE, related_name='carwash_to_car')
    type = models.PositiveSmallIntegerField(choices=CarTypeChoices.choices)

    price = models.IntegerField(default=0)




