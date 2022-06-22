# from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from apps.db.base_class import Base

class WorkingHour(Base):
    id = Column(Integer, primary_key=True, index=True)
    day = Column(Integer, index=True)
    start_at = Column(String, index=True)
    end_at = Column(String, index=True)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))


class Doctor(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    category = Column(String, index=True)
    consultation_fee = Column(Float)
    language = Column(String)
    district = Column(String, index=True)
    working_hours = relationship(WorkingHour)


