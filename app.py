from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
import os

app = FastAPI(
    title="Santander Dev Week 2023 - Fake API",
    description="API fake para simular a API oficial indisponível",
    version="1.0.0"
)

DATA_FILE = "data.json"

# ---------- MODELOS ----------

class Account(BaseModel):
    number: str
    agency: str
    balance: float
    limit: float

class Card(BaseModel):
    number: str
    limit: float

class User(BaseModel):
    id: int
    name: str
    account: Account
    card: Card

# ---------- HELPERS ----------

def load_users():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)

# ---------- ENDPOINTS ----------

@app.get("/users")
def get_users():
    return load_users()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    users = load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.post("/users")
def create_user(user: User):
    users = load_users()
    if any(u["id"] == user.id for u in users):
        raise HTTPException(status_code=400, detail="Usuário já existe")
    users.append(user.dict())
    save_users(users)
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: dict):
    users = load_users()

    for index, existing_user in enumerate(users):
        if existing_user["id"] == user_id:

            # merge: mantém campos antigos se não vierem no payload
            updated_user = existing_user.copy()
            updated_user.update(user)

            users[index] = updated_user
            save_users(users)
            return updated_user

    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users = load_users()
    for u in users:
        if u["id"] == user_id:
            users.remove(u)
            save_users(users)
            return {"message": "Usuário removido com sucesso"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
