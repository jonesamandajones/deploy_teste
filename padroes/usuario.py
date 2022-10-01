from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

class Usuario(BaseModel):
    email: EmailStr = Field(unique=True, index=True)
    senha: str
    usuario_ativo: bool = Field(default=True)
    administrador: bool = Field(default=False)
