from fastapi import APIRouter, Depends, HTTPException
from fastapi_jwt_auth import AuthJWT
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session
from starlette import status
from starlette.responses import Response

from app.database import get_db_session
from app.models import Cliente
from app.schemas import ClienteSchema
from app.scores import update_score
from app.utils import allowed_roles

router = APIRouter(prefix='/clientes')


@router.get('')
@allowed_roles(["ADMINISTRADOR"])
def list_all_clientes(session: Session = Depends(get_db_session)):
    stmt = select(ClienteSchema)
    return session.scalars(stmt).all()


@router.get('/{id_cliente}')
@allowed_roles(["ADMINISTRADOR"])
def get_cliente_by_id(id_cliente: int, session: Session = Depends(get_db_session)):
    cliente_in_db = session.get(ClienteSchema, id_cliente)
    if cliente_in_db is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Cliente não encontrado')

    return cliente_in_db


@router.post('')
@allowed_roles(["ADMINISTRADOR"])
def insert_cliente(cliente: Cliente, session: Session = Depends(get_db_session)):
    cliente_in_db = ClienteSchema(**dict(cliente))
    session.add(cliente_in_db)
    session.commit()
    session.refresh(cliente_in_db)
    yield cliente_in_db

    update_score(session, cliente_in_db)


@router.put('/{id_cliente}')
@allowed_roles(["ADMINISTRADOR"])
def update_cliente(id_cliente: int, cliente: Cliente, session: Session = Depends(get_db_session)):
    cliente_in_db = session.get(ClienteSchema, id_cliente)
    if cliente_in_db is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Cliente não encontrado')

    stmt = update(ClienteSchema).where(ClienteSchema.id == id_cliente).values(**dict(cliente))
    session.execute(stmt)
    session.commit()
    session.refresh(cliente_in_db)
    yield cliente_in_db
    
    update_score(session, cliente_in_db)


@router.delete('/{id_cliente}')
@allowed_roles(["ADMINISTRADOR"])
def delete_cliente(id_cliente: int, session: Session = Depends(get_db_session)):
    cliente_in_db = session.get(ClienteSchema, id_cliente)
    if cliente_in_db is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, 'Cliente não encontrado')

    session.delete(cliente_in_db)
    session.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
