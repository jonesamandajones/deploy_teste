from typing import List
from pydantic import BaseModel, Field

from .usuario import Usuario


class Endereco(BaseModel):
    logradouro: str
    cep: str
    bairro: str
    cidade: str
    estado: str
    entrega: bool = Field(default=True)


class EnderecosUsuario(BaseModel):
    usuario: Usuario
    enderecos: List[Endereco] = []