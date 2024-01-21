from django.urls import path
from . import views

urlpatterns = [
    path('',views.tourList,name="tourList"),
    path('<int:tour_id>/<str:title>/',views.tourDetails,name="TourDetails"),
    path('addToCart/<int:tour_id>/',views.addToCart,name="addTourToCart"),
    path('رحلات',views.tourListAr,name='tourListAr'),
    path('تفاصيل/<int:tour_id>/<str:title>/',views.tourDetailsAr,name="TourDetailsAr"),
    path('TourCartItem/<int:tour_id>/<str:title>/',views.tourItemCart,name="tourItemCart"),
    path('TourCartItemAr/<int:tour_id>/<str:title>/',views.tourItemCartAr,name="tourItemCartAr"),
    path('searchTour/',views.searchTour,name="searchTouru"),
    path('searchTourAr/',views.searchTourAr,name="searchTourAr"),
]