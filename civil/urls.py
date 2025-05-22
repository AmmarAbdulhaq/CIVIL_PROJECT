from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('withAdd/',views.withAdd, name='withAdd'),
    path('without/',views.without, name='without'),
]

