import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models import Ticket
from app.routes.tickets import router as tickets_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SehirPulse AI API",
    description="Vatandas talep kaydi, AI kategori tahmini ve belediye birimi yonlendirme API'si.",
    version="0.1.0",
)

origins = [origin.strip() for origin in os.getenv("FRONTEND_ORIGINS", "http://localhost:5173,http://localhost:3000").split(",")]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets_router)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok", "service": "sehirpulse-api"}
