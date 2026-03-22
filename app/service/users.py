from sqlalchemy.orm import Session
from app.repository import users as users_repository
from app.schemas import UserResponse


def create_user(db: Session, login: str):
    user = users_repository.create_user(db, login)
    db.commit()
    return UserResponse.model_validate(user)