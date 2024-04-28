import os
from django.db import models
from cyberintelligence.classes.helper import Helper
from cyberintelligence.models import LastLineRead

class Pulsedive(models.Model):
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
        self.MAX_REQUEST_PER_DAY = 50
        self.MAX_REQUEST_PER_MONTH = 500
    
    def query(self, domain):
        url = self.base_url + self.endpoint + "indicator=" + domain + "&" + self.pretty + "&" + "key=" + self.api_key
        return Helper.make_query(url, {})
