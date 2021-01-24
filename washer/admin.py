from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin

from washer.models import Washer, Cabin, Employee, EmployeeToWasher


class EmployeeToWasherInline(admin.TabularInline):
    model = EmployeeToWasher
    extra = 1


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    inlines = (EmployeeToWasherInline, )


@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    verbose_name = 'Employee'
    verbose_name_plural = "Employees"


