import json
from decimal import Decimal

import requests

from .exceptions import ResourceError, RateLimitError, RequestError, ServerError
from .config import Configuration

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        super().default(o)

class Response:
    def __init__(self, status_code, headers=None, data=None) -> None:
        self.status_code = status_code
        self.headers = headers
        self.data = data

    def is_success(self):
        return 200 <= self.status_code < 300

class HttpClient(object):

    def __init__(self, config: Configuration):
        self.config = config

    def get(self, url, params=None, **kwargs) -> Response:
        return self.request('get', url, params=params, **kwargs)

    def post(self, url, body=None, **kwargs) -> Response:
        return self.request('post', url, body=body, **kwargs)

    def put(self, url, body=None, **kwargs) -> Response:
        return self.request('put', url, body=body, **kwargs)

    def delete(self, url, params=None, **kwargs) -> Response:
        return self.request('delete', url, params=params, **kwargs)

    def request(self, method, url, params=None, body=None, **kwargs):
        url = "{base_url}{resource}".\
                format(base_url=self.config.base_url, resource=url)
        headers = {
                    'Authorization': "Bearer {access_token}".format(access_token=self.config.access_token)
        } if self.config.need_access_token else {}
    
        user_headers = {}
        if 'headers' in kwargs and isinstance(kwargs['headers'], dict):
            user_headers = kwargs['headers']

        headers.update(user_headers)
        if body:
            body = json.dumps(body, cls=DecimalEncoder)
        resp = requests.request(
            method, url, params=params, data=body, headers=headers, timeout=float(self.config.timeout),
        )
        response_headers = resp.headers
        if response_headers.get('Content-Type', None) and 'json' in response_headers.get('Content-Type', None):
            resp_body = resp.json()
        else:
            resp_body = resp.content
        return Response(resp.status_code, resp.headers, resp_body)

    def handle_error_response(self, resp):
        try:
            errors = resp.json()
        except ValueError:
            errors = {'errors': [], 'meta': {'logref': ''}}
        resp_code = resp.status_code
        if resp_code == 422:
            raise ResourceError(resp_code, errors)
        elif resp_code == 429:
            raise RateLimitError()
        elif 400 <= resp_code < 500:
            raise RequestError(resp_code, errors)
        elif 500 <= resp_code < 600:
            raise ServerError(resp_code, errors)
        else:
            raise Exception('Unknown HTTP error response')
