from django.urls import path
from . import views

urlpatterns = [
    path('',views.Insurances,name="insurances"),
    path('addToCart/<int:insurance_id>',views.addToCart,name='addinsuranceToCart'),
    path('Ar/',views.InsurancesAr,name="insurancesAr"),
    path('cartItem/<int:insurance_id>',views.insuranceDetails,name="insuranceDetails"),
    path('cartItemAr/<int:insurance_id>',views.insuranceDetailsAr,name="insuranceDetailsAr"),

]