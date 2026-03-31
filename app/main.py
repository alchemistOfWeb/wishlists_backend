from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.friends import router as friends_router
from app.api.wishlist import router as wishlist_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(friends_router)
app.include_router(wishlist_router)

@app.get("/")
def root():
    return {"status": "ok"}
