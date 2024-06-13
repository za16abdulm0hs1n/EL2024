# pip install requests
import requests
url =  requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
bitcoin_data = url.json()

bitcoin_rates_time = {
    'Time': bitcoin_data['time']['updated']
}

bitcoin_rates = {
    'EUR': bitcoin_data['bpi']['EUR']['rate'],
    'GBP': bitcoin_data['bpi']['GBP']['rate'],
    'USD': bitcoin_data['bpi']['USD']['rate']
}

print('Bitcoin Rate on {}'.format(bitcoin_rates_time['Time']))
print('---------------------------------------------')
for currency, rate in bitcoin_rates.items():
    print('{}: {}'.format(currency, rate))