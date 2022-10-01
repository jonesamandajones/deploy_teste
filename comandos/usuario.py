from funcoes.usuario import (
    criar_usuario
)

from mongodb.banco_de_dados import conectar_bd, bd, desconectar_bd


async def crud_usuario():

    await conectar_bd()
    colecao_usuarios = bd.usuarios_colecao
    ...

