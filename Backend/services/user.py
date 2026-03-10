from sqlalchemy.orm import Session
from Backend.models.models import User


class UserRepository:

    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def create_user(self, db: Session, user_data):
        user = User(**user_data)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()