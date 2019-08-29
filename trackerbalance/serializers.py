from rest_framework import serializers
from trackerbalance.models import Address, BalanceHistory


class BalanceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BalanceHistory
        fields = ['id', 'address', 'created_at']


class AddressSerializer(serializers.ModelSerializer):
    history = BalanceHistorySerializer(many=True)

    class Meta:
        model = Address
        fields = ['id', 'address', 'created_at', 'history']
