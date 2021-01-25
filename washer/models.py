from django.db import models
from washer.choices import EmployeeRoleChoices, GenderChoices
from django.utils.translation import gettext_lazy as _


class Company(models.Model):
    company_id = models.CharField(verbose_name=_('Company_id'), max_length=255, unique=True)
    name = models.CharField(verbose_name=_('Name'), max_length=255)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')


class Washer(models.Model):
    company = models.ForeignKey(to='washer.Company', on_delete=models.CASCADE, related_name='washer')
    name = models.CharField(verbose_name=_('Name'), max_length=255)
    location = models.CharField(max_length=250, default='Earth')

    cabin_number = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        created = not self.pk
        super().save(*args, **kwargs)
        if created:
            if self.cabin_number != 0:
                for num in range(1, self.cabin_number + 1):
                    Cabin.objects.create(washer=self, number=num)

    class Meta:
        verbose_name = _('Washer')
        verbose_name_plural = _('Washers')


class Cabin(models.Model):
    washer = models.ForeignKey(Washer, on_delete=models.CASCADE, related_name="cabin")

    number = models.PositiveSmallIntegerField()
    is_empty = models.BooleanField(default=True)

    def __str__(self):
        return f'Cabin of {self.washer} N.{self.number}'

    class Meta:
        verbose_name = _('Cabin')
        verbose_name_plural = _('Cabins')


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, default="")
    phone_number = models.CharField(verbose_name=_('Phone number'), max_length=125, default='')

    gender = models.PositiveSmallIntegerField(choices=GenderChoices.choices,
                                              default=GenderChoices.Other)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')


class EmployeeToWasher(models.Model):
    washer = models.ForeignKey(to='washer.Washer', on_delete=models.CASCADE, related_name='washer_to_employee')
    employee = models.ForeignKey(to='washer.Employee', on_delete=models.CASCADE, related_name='employee_to_washer')
    role = models.PositiveSmallIntegerField(choices=EmployeeRoleChoices.choices,
                                            default=EmployeeRoleChoices.Washer)
    salary = models.PositiveIntegerField()
