from datetime import datetime
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator


RequestType = Literal["Talep", "Şikayet", "İhbar", "Sikayet", "Ihbar"]


class TicketCreate(BaseModel):
    citizen_name: str | None = Field(default="Anonim", max_length=120)
    description: str = Field(min_length=10, max_length=2000)
    district: str = Field(min_length=1, max_length=80)
    neighborhood: str = Field(min_length=1, max_length=120)
    address: str | None = Field(default=None, max_length=255)
    request_type: RequestType

    @field_validator("citizen_name", mode="before")
    @classmethod
    def default_citizen_name(cls, value: str | None) -> str:
        if value is None or str(value).strip() == "":
            return "Anonim"
        return str(value).strip()

    @field_validator("description", "district", "neighborhood", mode="before")
    @classmethod
    def strip_required_text(cls, value: str) -> str:
        return str(value).strip()

    @field_validator("address", mode="before")
    @classmethod
    def normalize_optional_text(cls, value: str | None) -> str | None:
        if value is None:
            return None
        value = str(value).strip()
        return value or None


class TicketRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    citizen_name: str
    description: str
    district: str
    neighborhood: str
    address: str | None
    request_type: str
    category: str
    sub_category: str | None
    department: str
    confidence_score: float | None
    priority_level: str
    ai_reason: str | None
    status: str
    created_at: datetime
    updated_at: datetime
