import datetime
from decimal import Decimal
from typing import List, Optional
from pydantic import BaseModel, Field

from enderecos import Endereco
from usuario import Usuario
from produtos import Produto


class Carrinho(BaseModel):
    usuario: Usuario
    preco: Decimal = Field(max_digits=10, decimal_places=2)
    paid: bool = Field(default=False)
    data_de_criacao: datetime.datetime = Field(default=datetime.datetime.now())
    endereco: Endereco

class item_carrinho(BaseModel):
    carrinho: Carrinho
    produtos: List[Produto] = []