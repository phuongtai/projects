from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from apps.doctor import crud, schemas
from apps.apis import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Doctor])
def read_doctors(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    district: str = None,
    category: str = None,
    price_from: str = None,
    price_to: str = None,
    language: str = None
) -> Any:
    """
    Retrieve doctors.
    """
    filters = {
        'district': district, 'category': category,
        'price_from': price_from, 'price_to': price_to,
        'language': language
    }
    doctors = crud.doctor.get_multi(db, skip=skip, limit=limit, filters=filters)
    return doctors

@router.post("/", response_model=schemas.Doctor)
def create_doctor(
    *,
    db: Session = Depends(deps.get_db),
    doctor_in: schemas.DoctorCreate,
) -> Any:
    """
    Create new doctor.
    """
    doctor = crud.doctor.create(db=db, obj_in=doctor_in)
    doctor_data = schemas.Doctor.from_orm(doctor).dict()
    if doctor.working_hours:
        doctor_data.update({'working_hours': [
            schemas.WorkingHourInDBBase.from_orm(wh).dict() for wh in doctor.working_hours]
        })
    return JSONResponse(doctor_data)

@router.post("/bulk", response_model=List[schemas.Doctor])
def create_bulk_doctor(
    *,
    db: Session = Depends(deps.get_db),
    doctor_in: List[schemas.DoctorCreate],
) -> Any:
    """
    Create new doctor.
    """
    doctor = crud.doctor.bulk_create(db=db, obj_in=doctor_in)
    
    return doctor

@router.put("/{id}", response_model=schemas.Doctor)
def update_doctor(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
    doctor_in: schemas.DoctorUpdate,
) -> Any:
    """
    Update an doctor.
    """
    doctor = crud.doctor.get(db=db, id=id)
    if not doctor:
        raise HTTPException(status_code=404, detail="doctor not found")
    doctor = crud.doctor.update(db=db, db_obj=doctor, obj_in=doctor_in)
    return doctor


@router.get("/{id}", response_model=schemas.Doctor)
def read_doctor(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Get doctor by ID.
    """
    doctor = crud.doctor.get(db=db, id=id)
    if not doctor:
        raise HTTPException(status_code=404, detail="doctor not found")
    return doctor


@router.delete("/{id}", response_model=schemas.Doctor)
def delete_doctor(
    *,
    db: Session = Depends(deps.get_db),
    id: int,
) -> Any:
    """
    Delete an doctor.
    """
    doctor = crud.doctor.get(db=db, id=id)
    if not doctor:
        raise HTTPException(status_code=404, detail="doctor not found")
    doctor = crud.doctor.remove(db=db, id=id)
    return 