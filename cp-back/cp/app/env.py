import os

from pydantic import BaseModel


class Settings(BaseModel): #serão usados para armazenar chaves secretas para autenticação e criptografia. 
    authjwt_secret_key: str
    bcrypt_salt: bytes


CONFIG = Settings(
    authjwt_secret_key=os.getenv('JWT_SECRET_KEY'), #os.getenv() para obter os valores de variáveis de ambiente chamadas 
    bcrypt_salt=os.getenv('BCRYPT_SALT').encode('utf8')
)
