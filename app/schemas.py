from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class Schema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class UserSchema(Schema):
    id: int
    username: str
    email: EmailStr
    hashed_password: bytes
    scope: int
    created_at: datetime


class UserOutSchema(Schema):
    id: int
    username: str
    email: EmailStr
    scope: int
    created_at: datetime
