from cyberintelligence.classes.helper import Helper

class VirusTotal():
    """ This class is to connect my code to virus total api.
    For more information on the total virus api visit
    this link: https://virustotal.readme.io/reference/overview

    If you are using the free token it only allows you to make 
    500 requests per day and a rate of 4 requests per minute.
    """
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url="https://www.virustotal.com/api/v3/"
        self.base_ip_address_endpoint = "ip_addresses/"
        self.base_domain_endpoint = "domains/"
        self.header = {
            "x-apikey": self.api_key
        }

    def make_ip_query(self, ip):
        """ Make an ip query to Virus Total api.
        Params:
            - ip (string). Represents the IP to be analyzed.

        Functionality:
            - Creates a valid request for the total virus endpoint.
        
        Returns:
            - Return a 'dict' (json) object.
        """
        return Helper.make_query(self.base_url + self.base_ip_address_endpoint + ip, self.header)
        
    def make_domain_query(self, domain):
        """ Make a domain query to Virus Total api.
        Params:
            - domain (string). Represents the domain to be analyzed.

        Functionality:
            - Creates a valid request for the total virus endpoint.
        
        Returns:
            - Return a 'dict' (json) object.
        """
        return Helper.make_query(self.base_url + self.base_domain_endpoint + domain, self.header)