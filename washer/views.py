from django.shortcuts import render
from washer.models import Washer, CarWash, CarWashToType
from datetime import datetime, date


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
    money_made = []
    return render(request,
                  "Car_Washes/car-wash-detail.html",
                  context={
                      "car_wash": car_wash,
                      "all_salary" : money_made
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
    orders = washer.order.all()
    orders_week = []
    orders_month = []
    orders_year = []
    all_salary = 0
    week_sal = 0
    month_sal = 0
    year_sal = 0

    for ords in orders:

        price = ords.price
        all_salary += price
        current_week = datetime.now().isocalendar()[1]
        completion_week = ords.completion_time.isocalendar()[1]

        if completion_week == current_week:
            orders_week.append(ords)
            week_sal += price
        if ords.completion_time.month == datetime.now().month:
            orders_month.append(ords)
            month_sal += price
        if ords.completion_time.year == datetime.now().year:
            orders_year.append(ords)
            year_sal += price

    return render(request,
                  "washer-detail.html",
                  context={
                      "washer": washer,
                      "orders_week": orders_week,
                      "orders_month": orders_month,
                      "orders_year": orders_year,
                      "all_salary":  all_salary,
                      "month_salary": month_sal,
                      "week_salary": week_sal,
                      "year_salary": year_sal,
                  })
