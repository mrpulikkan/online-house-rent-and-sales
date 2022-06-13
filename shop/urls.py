
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('register/',views.registerPage,name='register'),
    path('login/',views.loginPage, name='login'),
    path('rent/',views.rent,name="rent"),
   # path('rent/<str:pk_test>/',views.customer,name="rent"),
    path('sale/',views.sales,name="sale"),
    path('create_order/',views.createOrder,name="create_order")
]
