from .helper import Helper

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
        return Helper.make_query(self.base_url + f"indicators/IPv4/{ip}/general", self.header)
    
    def make_domain_query(self, domain):
        return Helper.make_query(self.base_url + f"indicators/domain/{domain}/general", self.header)