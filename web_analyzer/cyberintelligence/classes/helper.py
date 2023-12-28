import requests
import json 

class Helper:

    @staticmethod
    def make_query(url, header):
        response = requests.get(url, headers=header)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception("Bad request for this url", url)