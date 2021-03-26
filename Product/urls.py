from django.contrib import admin
from django.urls import path
from Product import views

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [

    path('addtocart/',views.OrderList.as_view()),
    path('addtocart/<int:pk>/', views.OrderDetails.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)