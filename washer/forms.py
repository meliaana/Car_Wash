from django import forms
from .models import CarWashToType, CarWash, Car, Washer, Order
from .choices import CarTypeChoices


class CarWashForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    location = forms.CharField(max_length=250)
    cabins = forms.IntegerField()

    class Meta:
        model = CarWash
        fields = ['name', 'location', 'cabins']


class CarWashToTypeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for car_type in CarTypeChoices:
            self.fields[car_type.name] = forms.IntegerField(required=True)

    def save(self, car_wash_pk: int):
        for car_type in CarTypeChoices:
            price = self.cleaned_data[car_type.name]
            a = CarWashToType(type=car_type, price=price, car_washer=CarWash.objects.get(pk=car_wash_pk))
            a.save()


class OrderForm(forms.ModelForm):
    car_wash = forms.ModelChoiceField(queryset=CarWash.objects.all())
    car = forms.ModelChoiceField(queryset=Car.objects.all())
    washer = forms.ModelChoiceField(queryset=Washer.objects.all())
    order_time = forms.DateTimeField()

    class Meta:
        model = Order
        fields = ['car_wash', 'car', 'washer', 'order_time']


class CarForm(forms.ModelForm):
    plate = forms.CharField(max_length=10)
    type = forms.ChoiceField(choices=CarTypeChoices.choices)

    class Meta:
        model = Car
        fields = ['plate', 'type']
