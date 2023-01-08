# coding=utf-8
from base.base_object import BaseObject

class RealEstateObject(BaseObject):
    mapping_fields = {
        'external_identify': 'ad_id',
        'subject': 'subject',
        'price': 'price',
        'posted_date': 'list_time',
        # 'body': 'body',
        'category': 'category',
        'category_name': 'category_name',
        'rooms': 'rooms',
        'size': 'size',
        'toilets': 'toilets',
        'floors': 'floors',
        'width': 'width',
        'length': 'length',
        'location': 'location',
        'longitude': 'longitude',
        'latitude': 'latitude',
        'owner': 'owner',
        'street_name': 'street_name',
        'ward': 'ward',
        'ward_name': 'ward_name',
        'area_name': 'area_name',
        'area': 'area'
    }
