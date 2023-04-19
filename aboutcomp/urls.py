from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('managment', views.manag),
    path('purchases', views.purchas),
    path('anti-corruption', views.anti_cor),
    path('disclosures', views.disclosur),
]
