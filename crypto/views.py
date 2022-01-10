from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from django.shortcuts import render
import os

api_key = os.getenv("api_key")

def home(request):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    parameters = {
        'start' : '1',
        'limit' : '5000',
        'convert' : 'USD'
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '64cd695d-26ab-4937-b788-14b86a0db2f8'
    }

    session = Session()
    session.headers.update(headers)

    # try:
    response = session.get(url, params=parameters)
    crypto_data = json.loads(response.text)
    print("Yoooooo")
    print(crypto_data, type(crypto_data))

    # except (ConnectionError, Timeout, TooManyRedirects) as e:
    #     print(e)
    
    context = {
        'crypto_data' : crypto_data
    }
    return render(request, 'home.html', context)