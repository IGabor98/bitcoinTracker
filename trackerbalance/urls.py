from django.urls import path
from .views import *


urlpatterns = [
    path('sync-addresses-with-wallet/', sync_addresses_with_wallet),
    path('generate-address/', generate_new_address),
    path('get-address-history/<str:address>', get_address_balance_history),
]
