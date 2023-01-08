from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class Property:
    external_identify: str
    subject: str
    price: float
    posted_date: int
    # body: str
    category: str
    category_name: str
    rooms: int
    size: float
    toilets: int
    floors: int
    width: float
    length: float
    location: str
    longitude: str
    latitude: str
    owner: bool
    street_name: str
    ward: int
    ward_name: str
    area: str
    area_name: str
    region: str
    region_name: str

    @property
    def posted_at(self):
        return str(datetime.fromtimestamp(self.posted_date/1000))
    