from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.repository.jobs import create_new_job
from db.session import get_db
from schemas.jobs import JobCreate, ShowJob


router = APIRouter()


@router.post("/create-job/", response_model=ShowJob)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    current_user = 1
    job = create_new_job(job=job, db=db, owner_id=current_user)
    return job
