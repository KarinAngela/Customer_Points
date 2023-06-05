from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

 #Schema é referente as tabelas do banco
class Base(DeclarativeBase):
    pass


class UsuarioSchema(Base):
    __tablename__ = 'usuarios'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    login: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(2048))
    role: Mapped[ENUM] = mapped_column(ENUM('CLIENTE', 'ADMINISTRADOR'))


class ClienteSchema(Base):
    __tablename__ = 'clientes'

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(256))
    cpf: Mapped[str] = mapped_column(String(14))
    cnpj: Mapped[str] = mapped_column(String(18), nullable=True)
    salario: Mapped[float] = mapped_column()
    dividas: Mapped[ENUM] = mapped_column(ENUM('SIM', 'NÃO'), default='NÃO')


class ScoresSchema(Base):
    __tablename__ = 'scores'

    id: Mapped[int] = mapped_column(primary_key=True)
    id_cliente: Mapped[int] = mapped_column(ForeignKey("clientes.id"))
    timestamp: Mapped[datetime] = mapped_column(default=datetime.now())
    desempenho: Mapped[ENUM] = mapped_column(ENUM('PÉSSIMO', 'RUIM', 'REGULAR', 'BOM', 'ÓTIMO'))
    risco: Mapped[ENUM] = mapped_column(ENUM('BAIXO', 'MÉDIO', 'ALTO'))
