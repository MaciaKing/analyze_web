import requests
import json

class VirusTotal():
    # 500 requests per day and a rate of 4 requests per minute. Free key
    
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url="https://www.virustotal.com/api/v3/"
        self.base_ip_address_endpoint = "ip_addresses/"
        self.base_domain_endpoint = "domains/"
        self.header = {
            "x-apikey": self.api_key
        }

    def make_ip_query(self, ip):
        url = self.base_url + self.base_ip_address_endpoint + ip
        response = requests.get(url, headers=self.header)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("An ip was expected")     
        
    def make_domain_query(self, domain):
        url = self.base_url + self.base_domain_endpoint + domain
        response = requests.get(url, headers=self.header)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("A domain was expected")

        