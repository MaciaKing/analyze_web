import requests
import json

#https://otx.alienvault.com/api
class AlienVault():

    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://otx.alienvault.com/api/v1/'
        self.header = {
            'X-OTX-API-KEY': self.api_key,
            'Content-Type': 'application/json'
        }
    
    def make_ip_query(self, ip):
        response = requests.post(self.base_url + f"indicators/IPv4/{ip}/general", headers=self.header, data='')
        return json.loads(response.text)
    
    def make_domain_query(self, domain):
        response = requests.get(self.base_url + f"indicators/domain/{domain}/general", headers=self.header, data='')
        return json.loads(response.text)