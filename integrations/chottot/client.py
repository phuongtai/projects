from base.config import Configuration
from .http_client import ChoTotHTTPClient

from . import services

class Client(object):
    def __init__(self, **options):
        self.config = Configuration(**options)
        self.config.validate()
        self.http_client = ChoTotHTTPClient(self.config)

    @property
    def realEstate(self):
        return services.RealEstate(self.http_client)
