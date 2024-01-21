from django.urls import path
from . import views

urlpatterns = [
    path('',views.packageList,name="packageList"),
    path('حزم الخدمات/',views.packageListAr,name="packageListAr"),
    path('<int:package_id>/<str:title>/',views.packageDetails,name="packageDetails"),
    path('searchPackage/',views.searchPackage,name="searchPackageu"),
    path('searchPackageAr/',views.searchPackageAr,name="searchPackageAr"),
    path('addItem/<int:package_id>/',views.addToCart,name="addPackageToCart"),
    path('ar/<int:package_id>/<str:title>/',views.packageDetailsAr,name="packageDetailsAr"),
    path('packageItemcart/<int:package_id>/<str:title>/',views.packageItemCart,name="packageItemCart"),
    path('packageItemcartAr/<int:package_id>/<str:title>/',views.packageItemCartAr,name="packageItemCartAr"),
]