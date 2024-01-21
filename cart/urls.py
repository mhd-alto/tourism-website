from django.urls import path
from . import views

urlpatterns = [
    path('',views.cartList,name='carts'),
    path('ar/',views.cartListAr,name='cartsAr'),
    path('details/<int:cart_id>',views.cartDetails,name='CartDetails'),
    path('detailsAr/<int:cart_id>',views.cartDetailsAr,name='CartDetailsAr'),
    path('deleteItem/<int:item_id>/<int:cart_id>',views.deleteItem,name='deleteItem'),
    path('addItem/<int:item_id>/<int:cart_id>',views.add,name='add'),
    path('minsItem/<int:item_id>/<int:cart_id>',views.mins,name='mins'),
    path('send/<int:cart_id>',views.deactiveCart,name='Send'),

]