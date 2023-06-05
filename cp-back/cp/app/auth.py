import bcrypt
from fastapi import APIRouter, HTTPException, Depends
from fastapi_jwt_auth import AuthJWT
from sqlalchemy import select
from sqlalchemy.orm import Session
from starlette import status

from app.database import get_db_session
from app.env import CONFIG
from app.models import Usuario, LoginData
from app.schemas import UsuarioSchema

router = APIRouter(prefix='/auth')


@router.post('/login')
def login(login_data: LoginData, session: Session = Depends(get_db_session), authorize: AuthJWT = Depends()):
    stmt = select(UsuarioSchema).where(UsuarioSchema.login == login_data.login)
    user = session.scalar(stmt)

    if user is None:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Usuário ou senha incorretos')

    if not bcrypt.checkpw(login_data.password.encode('utf8'), user.password.encode('utf8')):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, 'Usuário ou senha incorretos')

    user_claims = {'role': user.role}
    access_token = authorize.create_access_token(subject=user.id, user_claims=user_claims)
    return {'access_token': access_token}


@router.post('/register')
def register(usuario: Usuario, session: Session = Depends(get_db_session)):
    hashed_password = bcrypt.hashpw(usuario.password.encode('utf8'), CONFIG.bcrypt_salt)
    final_user_data = {**dict(usuario), 'password': hashed_password.decode('utf8')}

    user_in_db = UsuarioSchema(**final_user_data)
    session.add(user_in_db)
    session.commit()
    session.refresh(user_in_db)
    return usuario


@router.get('/me')
def get_current_user(session: Session = Depends(get_db_session), authorize: AuthJWT = Depends()):
    authorize.jwt_required()

    user_id = authorize.get_jwt_subject()
    user_in_db = session.get(UsuarioSchema, user_id)
    return user_in_db
