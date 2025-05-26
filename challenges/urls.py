from django.urls import path
from . import views
urlpatterns = [
    path('jan', views.index,name='index'),
    path('feb', views.func_feb)
]