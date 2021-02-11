from decimal import Decimal
from .forms import CarWashForm, CarWashToTypeForm, OrderForm
from .choices import CarTypeChoices

from django.http import HttpResponse
from django.shortcuts import render
from washer.models import Washer, CarWash, CarWashToType, Order
from datetime import datetime, date
from django.db.models import Sum, ExpressionWrapper, DecimalField, F, Q


def test(request):
    car_wash_form = CarWashForm()
    price_form = CarWashToTypeForm()
    cars_lists = list(zip(*CarTypeChoices.choices))[1]  # @TODO: change

    if request.method == 'POST':
        car_wash_form = CarWashForm(request.POST)
        price_form = CarWashToTypeForm(request.POST)

        if car_wash_form.is_valid() and price_form.is_valid():
            new_car_wash = car_wash_form.save()
            car_wash_pk = new_car_wash.pk
            print(price_form)

    context = {"car_wash_form": car_wash_form,
               "price_form": price_form,
               "car_types": cars_lists}
    return render(request, "test.html", context=context)


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
    order_form = OrderForm()
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

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_form.save()

    return render(request,
                  "washer-detail.html",
                  context={
                      "form": order_form,
                      "washer": washer,
                      **money_made
                  })

