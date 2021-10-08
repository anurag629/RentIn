from django.urls import path ,include
from . import views

urlpatterns = [
    path('', views.index, name='RentHome'),
    path('about', views.about, name='RentHome'),
    path('contact', views.contact, name='contact'),
    path('search', views.search, name='search'),
    path('productview', views.productview, name='productview'),
    path('checkout', views.checkout, name='checkout'),
    
]