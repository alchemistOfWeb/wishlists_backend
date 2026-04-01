from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.users import router as users_router
from app.api.friends import router as friends_router
from app.api.wishlist import router as wishlist_router
from app.api.events import router as events_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(friends_router)
app.include_router(wishlist_router)
app.include_router(events_router)



@app.get("/")
def root():
    return {"status": "ok"}
