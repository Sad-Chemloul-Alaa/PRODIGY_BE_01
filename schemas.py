from pydantic import BaseModel, Field, EmailStr
from uuid import UUID
from typing import Optional

class User(BaseModel):
    user_name : str = Field(...,min_length=1 ,max_length=50)
    user_email : EmailStr
    user_age : str = Field(...,ge=0 ,le=120)

class UserResponse(User):
    id : UUID

class UserUpdate(BaseModel):
    user_name: Optional[str]= Field(None, min_length=1, max_length=50)
    user_email : Optional[EmailStr] = None
    user_age : Optional[str] = Field(None,ge=0 ,le=120) 
    