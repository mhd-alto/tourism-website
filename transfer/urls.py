from django.urls import path
from . import views


urlpatterns = [
    path('',views.Cars,name="cars"),
    path('Ar/',views.CarsAr,name="carsAr"),
    path('addToCart/<int:car_id>',views.addToCart,name="addcarToCart"),
    path('carDetails/<int:car_id>',views.carsDetails,name="carDetails"),
    path('carDetailsAr/<int:car_id>/',views.carsDetailsAr,name="carDetailsAr"),

    
]