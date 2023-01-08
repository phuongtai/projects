from os import environ
from scripts.services.config import Config
from scripts.services.http_client import HttpClient

# base_url = 'https://gateway.chotot.com/v1/public/'



# def save_to_json(page, data):
#     with open('{}.json'.format(page), '+w') as json_file:
#         json_file.write(data)
#     json_file.close()

# def get_ad_list(page, limit=50):
#     path = 'https://gateway.chotot.com/v1/public/ad-listing?cg=1000&o=20&page={}&st=s,k&limit={}&key_param_included=true'.format(page, limit)
#     resp = requests.get(path)
#     save_to_json(page, resp.content.decode('utf-8'))

class ChoTotClient(HttpClient):
    fields = ('ad_id', 'list_id', 'list_time', 'room',)
    def get_real_estate(self, params={}):
        return self.get(url='ad-listing', params=params)
    def reduce_fields(self, item):
        pass

chotot_config = Config(need_obtain_token=False)
chotot_config.base_url = environ.get('base_url')
 




        
    
