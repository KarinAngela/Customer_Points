from typing import Optional

from pydantic import BaseModel

#O models seria o DTO-são objetos utilizados para transportar dados entre componentes do sistema, 
# proporcionando uma forma padronizada e eficiente de comunicação.

class Usuario(BaseModel):
    id_cliente: Optional[int]
    login: str
    password: str
    role: str


class Cliente(BaseModel):
    nome: str
    cpf: str
    cnpj: Optional[str]
    salario: float
    dividas: str


class LoginData(BaseModel):
    login: str
    password: str

