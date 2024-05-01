import os
import datetime
from django.db import models
from .helper import Helper
from .last_line_read import LastLineRead

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
    # Save to database
    last_day_used = models.DateField() # datetime.datetime.now()
    total_querys_on_month = models.IntegerField(default=0)

    # Api uses
    api_key = os.getenv('PULSEDIVE_API_KEY')
    pretty = "pretty=1"
    endpoint = "/info.php?"
    base_url = "https://pulsedive.com/api"
    MAX_REQUEST_PER_DAY = 50
    MAX_REQUEST_PER_MONTH = 500

    @classmethod
    def create(cls, api_key=os.getenv('PULSEDIVE_API_KEY')):
        return cls(api_key=api_key)

    def query(self, domain):
        url = self.base_url + self.endpoint + "indicator=" + domain + "&" + self.pretty + "&" + "key=" + self.api_key
        return Helper.make_query(url, {})

    def can_make_query(self, actual_number_of_requests):
        # If today is the same month of last query
        if datetime.datetime.now().month == Pulsedive.objects.first().last_day_used.month:
            # Check if the MAX_REQUEST_PER_DAY limit is passed
            if self.MAX_REQUEST_PER_DAY <= actual_number_of_requests:
                return False
            # Check if the total_querys_on_month is passed
            if self.MAX_REQUEST_PER_DAY <= self.total_querys_on_month:
                return False
        # The month is different, so you can make querys
        # or you have not pass the limit and you can make querys.
        return True
    
    def add_one_to_total_querys_on_month(self):
        self.total_querys_on_month = self.total_querys_on_month + 1
        self.save()
