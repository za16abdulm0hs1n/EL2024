import requests
import pprint

ip_url =  requests.get("https://api.ipify.org/?format=json")
my_ip = ip_url.json()
info_url = requests.get("https://ipinfo.io/" + my_ip['ip'] + "/geo")
info = info_url.json()
pprint.pprint(info)