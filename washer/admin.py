from django.contrib import admin

from washer.models import CarWash, Cabin, Washer, Car, CarWashToType, Order


class CarWashToTypeInline(admin.TabularInline):
    model = CarWashToType
    extra = 1


@admin.register(CarWash)
class CarWashAdmin(admin.ModelAdmin):
    inlines = (CarWashToTypeInline, )


@admin.register(Cabin)
class CabinAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj is not None:
            return False
        return super().has_change_permission(request, obj=obj)


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
