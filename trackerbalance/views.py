import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bitcoinTracker.settings import env
from .models import Address, BalanceHistory
from .serializers import AddressSerializer


@api_view(['GET'])
def get_balance_of_addresses(request) -> Response:
    """
    Return balance of all addresses
    :param request:
    :return response:
    """

    params = {'password': env('WALLET_PASSWORD')}
    addresses = requests.get(env('GET_BALANCE_ADDRESSES'), params=params).json()
    __save_address_balance_in_history(addresses)
    return Response(addresses)


@api_view(['GET'])
def generate_new_address(request) -> Response:
    """
    Generate and return new replenishment address

    :param request:
    :return response:
    """

    params = {'password': env('WALLET_PASSWORD')}
    data = requests.get(env('GENERATING_NEW_ADDRESS'), params=params).json()

    address = Address(address=data['address'])
    address.save()

    return Response(data)


@api_view(['GET'])
def get_address_balance_history(request, address) -> Response:
    """
    Get balance history of specific address

    :param request:
    :param address:
    :return response:
    """
    try:
        address = Address.objects.filter(address=address).get()
        serializer = AddressSerializer(address)

        return Response(serializer.data)
    except Address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def __save_address_balance_in_history(addresses):
    """
    Save address balance in history

    :param addresses:
    """

    for item in addresses['addresses']:
        address = Address.objects.filter(address=item['address'])
        if address:
            BalanceHistory(balance=float(item['balance']), address=address.get()).save()
        else:
            address = __create_address(item['address'])
            BalanceHistory(balance=float(item['balance']), address=address).save()


def __create_address(address) -> Address:
    """
    Create address

    :param string address:
    :return: new address instance
    """
    address = Address(address=address)
    address.save()

    return address
