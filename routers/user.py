from fastapi import APIRouter , status
from .. import schemas , memory
from typing import List
from uuid import UUID
router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.get('/' , response_model=List[schemas.UserResponse])
def get_all_users():
    return memory.Display_all_users_infps()
    
@router.get('/{user_id}' , response_model=schemas.UserResponse)
def get_user_by_id(user_id:int):
    return memory.Get_user_infos_by_id(user_id)

@router.put('/{user_id}' , response_model=schemas.UserResponse)
def update_user(user_id: UUID , data: schemas.UserUpdate):
    return memory.Update_user( user_id, data)

@router.post('/' , response_model=schemas.User, status_code=status.HTTP_201_CREATED)
def create_user(data:schemas.User):
    return memory.Create_user(data)

@router.delete('/{user_id}')
def delete_user(user_id:UUID ):
    return memory.Delete_user(user_id)