import re

from .exceptions import ConfigurationError


class Configuration(object):

    URL_REGEXP = r'\b(?:(?:https?|http):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]'

    def __init__(self, need_access_token=False, **options):
        self.need_access_token = need_access_token
        self.access_token = options.get('access_token')
        if self.access_token is None:
            self.authorization_code = options.get('authorization_code')
            self.refresh_token = options.get('refresh_token')
        self.client_secret = options.get('client_secret')
        self.client_id = options.get('client_id')
        self.redirect_uri = options.get('redirect_uri')
        self.base_url = options['base_url'] if 'base_url' in options else 'https://api.fortnox.se'
        self.timeout = options['timeout'] if 'timeout' in options else 30

    def validate(self):
        if self.need_access_token:
            if self.client_secret is None:
                raise ConfigurationError('No client secret provided. '
                                        'Set your access token during client initialization using: '
                                        '"basecrm.Client(client_secret = <YOUR_APPS_CLIENT_SECRET>)"')

            if self.access_token is None:
                if self.authorization_code or self.refresh_token:
                    return True
                else:
                    raise ConfigurationError('No access token provided. '
                                            'Set your access token during client initialization using: '
                                            '"basecrm.Client(access_token = <YOUR_PERSONAL_ACCESS_TOKEN>)"')

            if re.search(r'\s', self.access_token):
                raise ConfigurationError('Provided access token is invalid '
                                        'as it contains disallowed characters. '
                                        'Please double-check you access token.')
        if not self.base_url or not re.match(self.URL_REGEXP, self.base_url):
            raise ConfigurationError('Provided base url is invalid '
                                    'as it not a valid URI. '
                                    'Please make sure it incldues the schema part, '
                                    'both http and https are accepted, '
                                    'and the hierarchical part')

        return True