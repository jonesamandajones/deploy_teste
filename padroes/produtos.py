from pydantic import BaseModel, Field
from decimal import Decimal

class Produto(BaseModel):
    nome: str = Field(max_length=100)
    descricao: str
    plataforma: str
    preco: Decimal = Field(max_digits=10, decimal_places=2)
    qantidade_em_estoque: int
    codigo: int
