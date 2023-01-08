# coding=utf-8
from typing import Dict


class BaseObject:
    mapping_fields = {}

    @classmethod
    def get_valid_search_params(cls):
        return cls.valid_search_params

    @classmethod
    def get_mapping_fields(cls):
        return cls.mapping_fields

    @classmethod
    def add_mapping_fields(cls, internal_key, external_key):
        cls.mapping_fields.update({internal_key: external_key})
        return True

    @classmethod
    def to_internal(cls, external_data: Dict):
        return {
            internal_key: external_data.get(external_key) 
            for internal_key, external_key in cls.get_mapping_fields().items()
            if external_key in external_data
        }

    @classmethod
    def to_external(cls, source_data: Dict) -> Dict:
        return {
            external_key: source_data.get(internal_key)
            for internal_key, external_key in cls.get_mapping_fields().items()
            if internal_key in source_data
        }
