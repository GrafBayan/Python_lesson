from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models import User, Task
from schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])

@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.execute(select(User)).scalars().all()
    return users

@router.get('/{user_id}')
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.execute(select(User).where(User.id == user_id)).scalar()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

@router.post('/create')
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.execute(select(User).where(User.username == user.username)).scalar()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slugify(user.username)  # Генерация slug на основе имени пользователя
    )

    db.execute(insert(User).values(
        username=new_user.username,
        firstname=new_user.firstname,
        lastname=new_user.lastname,
        age=new_user.age
    ))
    db.commit()

    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put('/update/{user_id}')
async def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    existing_user = db.execute(select(User).where(User.id == user_id)).scalar()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(
        update(User).where(User.id == user_id).values(
            username=user.username,
            firstname=user.firstname,
            lastname=user.lastname,
            age=user.age
        )
    )
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}

@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    db.query(Task).filter(Task.user_id == user_id).delete()
    db.delete(db_user)
    db.commit()

    return {'status_code': status.HTTP_200_OK, 'transaction': 'User deleted successfully!'}
