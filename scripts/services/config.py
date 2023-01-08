import re

from scripts.services.exceptions import ConfigurationError

class Config:
    URL_REGEX = r'\b(?:(?:https?|http):\/\/|www\.)[-a-z0-9+&@#\/%?=~_|!:,.;]*[-a-z0-9+&@#\/%=~_|]'

    def __init__(self, need_obtain_token=True, **options) -> None:
        self.need_obtain_token = need_obtain_token
        self.access_token = options.get('access_token')
        self.base_url = options.get('base_url')

    def validate(self):
        if not self.base_url or not re.match(self.URL_REGEX, self.base_url):
            raise ConfigurationError('Base URL is invalid')
        if not self.access_token and self.need_obtain_token:
            raise ConfigurationError('Please put access token or ')