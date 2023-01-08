from base.base_service import BaseService
from ..objects import RealEstateObject

class RealEstate(BaseService):
    object_class = RealEstateObject
    item_url = 'ad-listing'
    valid_search_params = ['page', 'limit', 'offset', 'cg', 'o']
    mapping_fields = []
    verbose_name_plural = 'ads'
    verbose_name = 'ad'

    def list(self, params={}, **kwargs):
        adapter = self.get_object_class()
        done = False

        while not done:
            response = self.http_client.get(self.get_url(), params)
            content = response.data
            for item in content[self.verbose_name_plural]:
                yield adapter.to_internal(item)
            total_page = content['total'] // params['limit']
            if params['page'] < total_page:
                params['page'] += 1
                params['o'] += params['limit']
            else:
                done = True
