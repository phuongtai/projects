from .base_object import BaseObject
from .base_http_client import HttpClient
class BaseService(object):
    object_class = BaseObject
    item_url = '/'
    valid_search_params = ['page', 'limit']
    verbose_name = 'result'
    verbose_name_plural = 'results'


    @classmethod
    def get_object_class(cls, **kwargs):
        return cls.object_class(**kwargs)

    def __init__(self, http_client: HttpClient):
        self.__http_client = http_client

    def get_url(self, number=None):
        if number:
            return f"{self.item_url}/{number}"
        return self.item_url

    @property
    def http_client(self):
        return self.__http_client

    def list(self, params={}, **kwargs):
        adapter = self.get_object_class()
        done = False

        # if params:
        #     for key in params.keys():
        #         if key in self.valid_search_params:
        #             search_params[key] = params[key]

        while not done:
            response = self.http_client.get(self.get_url(), params)
            content = response.data
            for item in content[self.verbose_name_plural]:
                yield adapter.to_internal(item)
            total_page = content['total'] // params['limit']
            # total_page = 10
            # print("content['total'] ", content['total'])
            # print("search_params['page']: ", params['page'] )
            # print("total: ", total_page)
            # print("len(content[self.verbose_name_plural]: ", len(content[self.verbose_name_plural]))
            if params['page'] < total_page:
                params['page'] += 1
            else:
                done = True

    # def retrieve_one(self):
    #     resp = self.http_client.get(self.get_url())
    #     if resp.is_success():
    #         return True, self.get_object_class().to_internal(resp.data)
    #     return False, resp.data

    # def retrieve(self, number):
    #     resp = self.http_client.get(self.get_url(number))
    #     if resp.is_success():
    #         return True, self.get_object_class().to_internal(resp.data)
    #     return False, resp.data

    # def create(self, source_data: dict, **kwargs):
    #     if not source_data and not kwargs:
    #         raise Exception('attributes for InvoicePayment are missing')
    #     adapter = self.get_object_class()
    #     data = adapter.to_external(source_data)
    #     response = self.http_client.post(self.get_url(), body={self.verbose_name: data})
    #     if response.is_success():
    #         return True, adapter.to_internal(response.data[self.verbose_name])
    #     return False, response.data


    # def update(self, number, *args, **kwargs):
    #     if not args and not kwargs:
    #         raise Exception('attributes for InvoicePayment are missing')
    #     attributes = args[0] if args else kwargs
    #     attributes = dict((k, v) for k, v in attributes.items())
    #     attributes.update({'service': self.SERVICE})
    #     return self.http_client.put(self.get_url(number), body=attributes)

    # def destroy(self, number):
    #     return self.http_client.delete(self.get_url(number))
