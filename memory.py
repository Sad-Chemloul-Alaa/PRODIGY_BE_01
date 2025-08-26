from typing import Dict
from uuid import UUID , uuid4
from .schemas import User , UserUpdate
from fastapi import HTTPException , status
class User_Memory():
    def __init__(self):
        self.users = Dict[UUID,User] = {}

    def Display_all_users_infps(self):
        return list(self.users.values())
    
    def Get_user_infos_by_id(self , id : UUID):
        return self.users.get(id)
    def Create_user(self, data: User):
        user = User(
            id=uuid4(), 
            user_name=data.user_name,
            user_email=data.user_email,
            user_age= data.user_age
        )
        self.users[user.id] = user
        return user
    
    def Update_user(self, user_id: UUID, data:UserUpdate):
        to_update_user = self.users.get(user_id)
        if not to_update_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        updated_user = to_update_user.model_copy(update=data.model_dump(exclude_unset=True))
        self.users[user_id] = updated_user
        return updated_user

    def Delete_user(self , user_id: UUID):
        if not user_id in self.users:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        del self.users[user_id]
        return True