from django.urls import path
from . import views

urlpatterns= [
    path('',views.cart_summary, name='cart_summary'),
    path('cart/add/',views.cart_add,name='cart_add'),
    path('cart/update/',views.cart_update,name='cart_update'),
    path('cart/delete/',views.cart_delete,name='cart_delete'),
    path('cart/buy',views.cart_buy, name='cart_buy'),

]