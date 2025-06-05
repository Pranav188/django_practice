from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = "index"),
    path('<int:month>/', views.func_month_number),
    path('<str:month>/', views.func_month, name = 'pranav_website'),
]
