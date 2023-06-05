from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db_session
from app.schemas import ScoresSchema, ClienteSchema
from app.utils import allowed_roles

router = APIRouter(prefix='/scores')


@router.get('/{id_cliente}')
@allowed_roles(["ADMINISTRADOR", "CLIENTE"])
def get_all_scores(id_cliente: int, session: Session = Depends(get_db_session)):
    stmt = select(ScoresSchema).where(ScoresSchema.id_cliente == id_cliente)
    return session.scalars(stmt).all()


def update_score(session: Session, cliente: ClienteSchema):
    desempenho, risco = _calculate_score(cliente.salario, cliente.dividas)
    score = ScoresSchema(id_cliente=cliente.id, desempenho=desempenho, risco=risco)
    session.add(score)
    session.commit()
    session.refresh(score)


def _calculate_score(salario: float, dividas: str):
    desempenho = _calculate_desempenho(salario)
    risco = _calculate_risco(desempenho, dividas)
    return desempenho, risco


def _calculate_desempenho(salario: float):
    if salario >= 3960:  # 3x salario minimo
        return 'ÓTIMO'
    elif salario >= 2640:  # 2x salario minimo
        return 'BOM'
    elif salario >= 1320:  # 1x salario minimo
        return 'REGULAR'
    elif salario >= 660:  # 1/2 salario minimo
        return 'RUIM'
    else:
        return 'PÉSSIMO'


def _calculate_risco(desempenho: str, dividas: str):
    if dividas == 'SIM':
        if desempenho in ('REGULAR', 'BOM', 'ÓTIMO'):
            return 'MÉDIO'
        else:
            return 'ALTO'
    elif dividas == 'NÃO':
        if desempenho in ('REGULAR', 'BOM', 'ÓTIMO'):
            return 'BAIXO'
        else:
            return 'MÉDIO'
