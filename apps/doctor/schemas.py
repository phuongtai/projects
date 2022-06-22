
from typing import List, Optional, Union
from pydantic import BaseModel

from apps.core.schemas import OrmBase


class WorkingHourBase(BaseModel):
    day: int = None
    start_at: str = None
    end_at: str = None


class WorkingHourCreate(WorkingHourBase):
    pass

class WorkingHourUpdate(WorkingHourBase):
    pass 

class WorkingHourInDBBase(WorkingHourBase, OrmBase):
    id: int

class RelatedWorkingHour(WorkingHourBase, OrmBase):
    pass


class DoctorBase(BaseModel):
    full_name: str
    consultation_fee: Optional[float] = None
    category: Optional[str] = None
    language: Optional[str] = None
    district: Optional[str] = None

class DoctorCreate(DoctorBase):
    full_name: str
    working_hours: List[WorkingHourBase] = []


# Properties to receive on Doctor update
class DoctorUpdate(DoctorBase):
    pass


# Properties shared by models stored in DB
class DoctorInDBBase(DoctorBase, OrmBase):
    pass


# Properties to return to client
class Doctor(DoctorInDBBase):
    pass


# Properties properties stored in DB
class DoctorInDB(DoctorInDBBase):
    pass

class DockerInDBCreate(DoctorBase, OrmBase):
    pass 


