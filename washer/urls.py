from django.urls import path
from washer.views import washer_listing, washer_detail, car_wash_detail, car_wash_listing, car_list_view, test

urlpatterns = [
    path('washers/', washer_listing, name='all-washer-list'),
    path('washer-detail/<int:pk>/', washer_detail, name='washer'),
    path('', car_wash_listing, name='all-car-washes'),
    path('car-wash/<int:pk>/', car_wash_detail, name='car-wash'),
    path('test', test, name="test"),
    path('cars/', car_list_view, name='all-cars'),
]
