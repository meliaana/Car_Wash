from decimal import Decimal

from django.shortcuts import render
from washer.models import Washer, CarWash, CarWashToType, Order
from datetime import datetime, date
from django.db.models import Sum, ExpressionWrapper, DecimalField, F, Q


def car_wash_listing(request):
    car_washes = CarWash.objects.all()
    return render(
        request,
        "Car_Washes/car-washes.html",
        context={
            "car_washes": car_washes,
        }
    )


def car_wash_detail(request, pk):
    car_wash = CarWash.objects.get(pk=pk)
    money_made = Order.objects.filter(car_wash=pk).aggregate(money=Sum('price'))
    return render(request,
                  "Car_Washes/car-wash-detail.html",
                  context={
                      "car_wash": car_wash,
                      "money_made": money_made['money']
                  })


def washer_listing(request):
    washers = Washer.objects.all()
    return render(
        request,
        "washers_listing.html",
        context={
            "washers": washers,
        }
    )


def washer_detail(request, pk):
    washer = Washer.objects.get(pk=pk)

    washer_salary = washer.base_salary
    current_week = datetime.now().isocalendar()[1]

    month = datetime.now().month
    week = current_week
    year = datetime.now().year

    done_orders = washer.order.filter(completion_time__isnull=False)
    money_made = done_orders.aggregate(all_money=washer.percentage * Sum('price'),
                                       monthly_money=washer.percentage * Sum('price',
                                                                             filter=Q(completion_time__month=month,
                                                                                      completion_time__year=year)),
                                       yearly_money=washer.percentage * Sum('price',
                                                                            filter=Q(completion_time__year=year)),
                                       )
    return render(request,
                  "washer-detail.html",
                  context={
                      "washer": washer,
                      **money_made
                  })
