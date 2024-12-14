from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, conint
from typing import List

app = FastAPI()

users = []


class User(BaseModel):
    id: int
    username: str
    age: conint(ge=18, le=120)


@app.get('/', response_description="Welcome to the User Management API")
async def read_root():
    return {"message": "Welcome to the User Management API. Use /users to get all users."}


@app.get('/users', response_model=List[User])
async def get_all_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def create_user(
        username: str = Path(..., min_length=5, max_length=20, description='Enter username',
                             examples={'example1': 'UrbanUser'}),
        age: conint(ge=18, le=120) = Path(..., description='Enter age', examples={'example1': 24})
) -> User:
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}', response_model=User)
async def update_user(
        user_id: int = Path(..., ge=1, le=150, description='Enter user_id', examples={'example1': 1}),
        username: str = Path(..., min_length=5, max_length=20, description='Enter username',
                             examples={'example1': 'UrbanUser'}),
        age: conint(ge=18, le=120) = Path(..., description='Enter age', examples={'example1': 24})
) -> User:
    if user_id > len(users) or user_id < 1:
        raise HTTPException(status_code=404, detail="User was not found")

    user = users[user_id - 1]
    user.username = username
    user.age = age
    return user


@app.delete('/user/{user_id}', response_model=User)
async def delete_user(
        user_id: int = Path(..., ge=1, le=150, description='Enter user_id', examples={'example1': 1})) -> User:
    if user_id > len(users) or user_id < 1:
        raise HTTPException(status_code=404, detail="User was not found")

    user = users.pop(user_id - 1)
    return user