from django.contrib import admin
from .models import Address, BalanceHistory
# Register your models here.
admin.site.register(Address)
admin.site.register(BalanceHistory)