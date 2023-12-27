import requests

class VirusTotal():
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url="https://www.virustotal.com/api/v3/"
        self.base_ip_address_endpoint = "ip_addresses/"
        self.header = {
            "x-apikey": self.api_key
        }

    def make_ip_query(self, ip):
        # 500 requests per day and a rate of 4 requests per minute. Free key
        url = self.base_url + self.base_ip_address_endpoint + ip
        print(url)
        response = requests.get(url, headers=self.header)
        print(response.text)
        #return response
    
        