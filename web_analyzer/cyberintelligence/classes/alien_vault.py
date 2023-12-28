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
        return self.make_query(self.base_url + f"indicators/IPv4/{ip}/general")
    
    def make_domain_query(self, domain):
        return self.make_query(self.base_url + f"indicators/domain/{domain}/general")
    
    def make_query(self, url):
        response = requests.get(url, headers=self.header)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("Bad request for this url", url)