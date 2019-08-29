from django.test import TestCase
from django.test import Client


# Create your tests here.

class GetBalanceTest(TestCase):

    def test_get_balance_of_addresses_has_not_server_error(self):
        resp = self.client.get('/get-balance-of-addresses/')
        self.assertNotEqual(resp.status_code, 500)

    def test_get_balance_history_of_address_has_not_server_error(self):
        resp = self.client.get('/get-address-history/test')
        self.assertNotEqual(resp.status_code, 500)
