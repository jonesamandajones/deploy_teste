from os import environ

from motor.motor_asyncio import AsyncIOMotorClient


class BancoDeDados:
    client: AsyncIOMotorClient = None
    database_uri = environ.get("DATABASE_URI")
    usuarios_colecao = None
    enderecos_colecao = None
    produtos_colecao = None
    carrinhos_colecao = None
    item_carrinho_colecao = None

bd = BancoDeDados()

async def conectar_bd():
    # conexao mongo, com no máximo 10 conexões async
    bd.client = AsyncIOMotorClient(
        bd.database_uri,
        maxPoolSize=10,
        minPoolSize=10,
        tls=True,
        tlsAllowInvalidCertificates=True
    )
    bd.usuarios_colecao = bd.client.magalu_games.users
    bd.enderecos_colecao = bd.client.magalu_games.address
    bd.produtos_colecao = bd.client.magalu_games.produtoss
    bd.carrinhos_colecao = bd.client.magalu_games.carrinhos
    bd.item_carrinho_colecao = bd.client.magalu_games.item_carrinho

async def desconectar_bd():
    bd.client.close()