from django.contrib import admin

from washer.models import CarWash, Washer, Car, CarWashToType, Order


class CarWashToTypeInline(admin.TabularInline):
    model = CarWashToType
    extra = 1


@admin.register(CarWash)
class CarWashAdmin(admin.ModelAdmin):
    inlines = (CarWashToTypeInline, )


@admin.register(Washer)
class WasherAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('price',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
