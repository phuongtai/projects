import requests

from scripts.services.config import Config


class HttpClient:
    def __init__(self, config: Config) -> None:
        self.config = config
    
    def get_header(self):
        if self.config.need_obtain_token:
            return {'Authorization': "Bearer {}".format(self.config.access_token)}
        return {}

    def request(self, method, url, params=None, body=None, **kwargs):
        url = '{base_url}/{resource}'.format(base_url=self.config.base_url, resource=url)
        headers = self.get_header()
        return requests.request(method, url=url, data=body, params=params, headers=headers)

    def get(self, url, params={}):
        return self.request('get', url=url, params=params)
    