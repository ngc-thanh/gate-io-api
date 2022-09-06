
from __future__ import print_function
import gate_api
from gate_api.exceptions import ApiException, GateApiException
# Defining the host is optional and defaults to https://api.gateio.ws/api/v4
# See configuration.py for a list of all supported configuration parameters.
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure APIv4 key authorization

import os
from dotenv import load_dotenv

load_dotenv('.env')

configuration = gate_api.Configuration(
    host = "https://api.gateio.ws/api/v4",
    key = os.getenv('KEY'),
    secret = os.getenv('SECRET')
)

api_client = gate_api.ApiClient(configuration)
# Create an instance of the API class
api_instance = gate_api.WalletApi(api_client)
currency = 'USDT' # str | Currency unit used to calculate the balance amount. BTC, CNY, USD and USDT are allowed. USDT is the default. (optional) (default to 'USDT')

try:
    # Retrieve user's total balances
    api_response = api_instance.get_total_balance(currency=currency)
    print(api_response)
except GateApiException as ex:
    print("Gate api exception, label: %s, message: %s\n" % (ex.label, ex.message))
except ApiException as e:
    print("Exception when calling WalletApi->get_total_balance: %s\n" % e)