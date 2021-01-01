from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('programmes', views.programmes, name='programmes'),
    path('facilities', views.facilities, name='facilities'),
    path('placements', views.placements, name='placements'),
]
