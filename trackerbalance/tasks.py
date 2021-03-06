from bitcoinTracker.celery_app import app
from bitcoinTracker.settings import env
import requests

from trackerbalance.models import Address, BalanceHistory


@app.task
def tracker_balance_of_addresses():
    """
    Celery task for tracker balance of wallet addresses

    :return:
    """
    for address in Address.objects.all():
        tracker_balance_of_address.delay(address.id)


@app.task
def tracker_balance_of_address(address_id):
    """
    Celery task for tracker balance of specific wallet address
    :param address_id:
    :return:
    """
    address = Address.objects.filter(id=address_id).get()
    params = {
        'password': env('WALLET_PASSWORD'),
        'address': address.address
    }
    response = requests.get(env('GET_BALANCE_ADDRESS'), params=params)

    if response.status_code == 200:
        data = response.json()
        BalanceHistory.objects.create(balance=float(data['balance']), address=address)
