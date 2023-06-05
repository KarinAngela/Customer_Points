from functools import wraps
from typing import List

from fastapi import Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from fastapi_wraps import fastapi_wraps
from starlette import status

#é refeerente  pra verifica se o usuario possui conta ou n 
def allowed_roles(roles: List[str]):
    def decorator(function):
        @fastapi_wraps(function)
        def wrapper(authorize: AuthJWT = Depends(), *args, **kwargs):
            authorize.jwt_required()
            user_role = authorize.get_raw_jwt()['role']
            if user_role in roles:
                return function(*args, **kwargs)
            raise HTTPException(status.HTTP_403_FORBIDDEN)
        return wrapper
    return decorator
