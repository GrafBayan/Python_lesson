from fastapi import FastAPI, HTTPException, Path

app = FastAPI()

users = {'1': 'Имя: Alex, возраст: 24'}

@app.get("/user")
async def users_list():
    return users

@app.post("/user/{username}/{age}")
async def user_add(
    username: str = Path(..., min_length=5, max_length=20, description="Имя пользователя"),
    age: int = Path(..., ge=18, le=120, description="Возраст пользователя")
):
    user_id = str(int(max(users.keys(), key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"User {user_id} is registered"}

@app.put("/user/{user_id}/{username}/{age}")
async def user_update(
    user_id: str = Path(..., description="ID пользователя"),
    username: str = Path(..., min_length=5, max_length=20, description="Имя пользователя"),
    age: int = Path(..., ge=18, le=120, description="Возраст пользователя")
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return {"message": f"The user {user_id} is updated"}

@app.delete("/user/{user_id}")
async def user_delete(
    user_id: str = Path(..., description="ID пользователя")
):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users.pop(user_id)
    return {"message": f"User {user_id} has been deleted!"}