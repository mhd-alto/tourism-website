from django.urls import path
from .views import visaList,visaListAr,addToCart,visaDetails,visaDetailsAr,searchVisa,searchVisaAr


urlpatterns = [
    path('visaSearch/',searchVisa, name='searchVisau'),
    path('visaSearchAr/',searchVisaAr, name='searchVisaar'),
    path('',visaList,name="visas"),
    path('Ar/',visaListAr,name="visasAr"),
    path('addToCart/<int:visa_id>',addToCart,name="addToCart"),
    path('visaDetails/<int:visa_id>',visaDetails,name="visaDetails"),
    path('visaDetailsAr/<int:visa_id>',visaDetailsAr,name="visaDetailsAr"),
]