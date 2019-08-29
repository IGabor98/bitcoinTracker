from django.urls import path
from .views import *


urlpatterns = [
    path('generate-address/', get_balance_of_addresses),
    path('get-balance-of-addresses/', get_balance_of_addresses),
    path('get-address-history/<str:address>', get_address_balance_history),
]
