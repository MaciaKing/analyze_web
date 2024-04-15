import os
import pdb
from cyberintelligence.classes.helper import Helper

class Pulsedive():
    '''
    Rate limits: https://pulsedive.com/about/api
    1 request /second
    50 requests /day
    500 requests /month

    10 Analyze scans /day
    100 Analyze scans /month

    50 Explore results
    '''
    def __init__(self, api_key=os.getenv('PULSEDIVE_API_KEY')):
        self.api_key = api_key
        self.pretty="pretty=1"
        self.endpoint="/info.php?"
        self.base_url="https://pulsedive.com/api"
        self.request_per_day = 50
        self.request_per_month = 500

    
    def query(self, domain):
        url = self.base_url + self.endpoint + "indicator=" + domain + "&" + self.pretty + "&" + "key=" + self.api_key
        return Helper.make_query(url, {})
