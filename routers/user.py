from fastapi import APIRouter , status
from memory import memory_use
from schemas import UserResponse , User ,UserUpdate
from typing import List
from uuid import UUID
router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.get('/' , response_model=List[UserResponse])
def get_all_users():
    return memory_use.Display_all_users_infos()
    
@router.get('/{user_id}' , response_model=UserResponse)
def get_user_by_id(user_id:UUID):
    return memory_use.Get_user_infos_by_id(user_id)

@router.put('/{user_id}' , response_model=UserResponse)
def update_user(user_id: UUID , data: UserUpdate):
    return memory_use.Update_user( user_id, data)

@router.post('/' , response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(data:User):
    return memory_use.Create_user(data)

@router.delete('/{user_id}')
def delete_user(user_id:UUID ):
    return memory_use.Delete_user(user_id)