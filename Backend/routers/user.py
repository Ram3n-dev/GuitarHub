from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from Backend.core.session import get_db
from Backend.schemas.user import UserCreate, UserResponse
from Backend.services.user import get_user, create_user, delete_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    return get_user(db, user_id)


@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.delete("/{user_id}")
def remove_user(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return {"status": "deleted"}