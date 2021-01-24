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
    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return False
        return super().has_change_permission(request, obj=obj)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


