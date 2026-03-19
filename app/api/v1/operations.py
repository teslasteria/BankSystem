from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependency import get_db
from app.schemas import OperationRequest
from app.service import operations as operation_service

router = APIRouter()


@router.post('/operations/income')
def add_income(operation: OperationRequest, db: Session = Depends(get_db)):
    return operation_service.add_income(operation)

@router.post('/operations/expense')
def add_expence(operation: OperationRequest, db: Session = Depends(get_db)):
    return operation_service.add_expence(operation)