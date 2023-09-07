from typing import List

from pydantic import BaseModel, Field

from src.users.router import router


class UserInfo(BaseModel):
    id: int
    username: str = Field(max_length=20)
    phone: str
    age: int


@router.get('', response_model=List[UserInfo])
def users():

    return [
        {
            'id': 1,
            'username': 'sfndckdsnewsl',
            'phone': 'dsnvdsvds',
            'age': 12
        },
        {
            'id': 2,
            'username': 'sfndckdsnewsl',
            'phone': 'dsnvdsvds',
            'age': 12
        }
    ]


@router.get('/{user_id}')
def get_user(user_id):
    print(user_id)
    return {
            'id': 2,
            'username': 'sfndckdsnewsl',
            'phone': 'dsnvdsvds',
            'age': 12
        }


@router.put('/{user_id}')
def get_user(user_id: int, data: UserInfo):
    print(data)
    return 'Success'


@router.delete('/{user_id}')
def get_user(user_id: int):
    print(user_id)
    return 'Success'