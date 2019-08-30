import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from bitcoinTracker.settings import env
from .models import Address
from .serializers import AddressSerializer


@api_view(['GET'])
def sync_addresses_with_wallet(request) -> Response:
    """
    Sync addresses with wallet

    :param request:
    :return response:
    """

    params = {'password': env('WALLET_PASSWORD')}
    addresses = requests.get(env('GET_BALANCE_ADDRESSES'), params=params).json()
    __create_addresses(addresses)

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


def __create_addresses(addresses):
    """
    Create many addresses

    :param addresses:
    """

    for item in addresses['addresses']:
        exist = Address.objects.filter(address=item['address'])
        if not exist:
            Address.objects.create(address=item['address'])
