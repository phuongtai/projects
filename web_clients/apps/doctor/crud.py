from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from apps.core.crud import CRUDBase
from apps.doctor import models
from apps.doctor.schemas import DoctorCreate, DoctorUpdate, WorkingHourCreate, WorkingHourUpdate


class CRUDDoctor(CRUDBase[models.Doctor, DoctorCreate, DoctorUpdate]):
    def get_multi(self, db: Session, *, skip: int = 0, limit: int = 100, filters={}):
        queryset = db.query(self.model)
        if any(filters.values()):
            kw = dict(filter(lambda x:x[1], filters.items()))
            price_from, price_to = kw.pop('price_from', None), kw.pop('price_to', None)
            if price_from and price_to:
                queryset = queryset.filter(and_(
                    self.model.consultation_fee >= price_from, 
                    self.model.consultation_fee <= price_to))
            elif price_from:
                queryset = queryset.filter(self.model.consultation_fee >= price_from)
            elif price_to:
                queryset = queryset.filter(self.model.consultation_fee <= price_to)
            return queryset.filter_by(**kw).offset(skip).limit(limit).all()
        return queryset.offset(skip).limit(limit).all()

    
    def create(self, db: Session, *, obj_in, **kwargs):
        obj_in_data = jsonable_encoder(obj_in)
        working_hours = obj_in_data.pop('working_hours')
        doctor = self.model(**obj_in_data)
        for wh in working_hours:
            doctor.working_hours.append(models.WorkingHour(**wh))
        db.add(doctor)
        db.commit()
        db.refresh(doctor)
        return doctor

    def bulk_create(
        self, db: Session, *, obj_in: List[DoctorCreate]
    ) -> models.Doctor:
        db_objs = [self.model(**jsonable_encoder(obj)) for obj in obj_in]
        db.add_all(db_objs)
        db.commit()
        # db.refresh(*db_objs)
        return db_objs


doctor = CRUDDoctor(models.Doctor)



class CRUDWorkingHour(CRUDBase[models.WorkingHour, WorkingHourCreate, WorkingHourUpdate]):
    pass

workingHour = CRUDWorkingHour(models.WorkingHour)