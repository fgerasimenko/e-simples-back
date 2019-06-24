# -*- coding: utf-8 -*-
import datetime
import uuid

from logs import get_logger
from storage import base

from models import ProdutoSchema

class ProdutoService:

    def __init__(self):
        self.logger = get_logger()

    def get_all(self):

        lista = [{
            "id": 1,
            "nome": "Essência Hungria Hip Hop",
            "marca": "Zomo",
            "tipo": "Essência",
            "descricao": "Essência mix de varios bagulho",
            "cod_barras": "898726987293",
            "preco_venda": 12.00,
            "preco_compra": 8.00,
            "medida": 1,
            "unidade": "un",
            "tags": ['essencia', 'mix', 'doce', 'especial', 'zomo'],
            "data_cadastro": '24/06/2019',
            "data_alteracao": None,
            "ativo": True 
        },
        {
            "id": 2,
            "nome": "Essência MC Gui",
            "marca": "Zomo",
            "tipo": "Essência",
            "descricao": "Essência mix de varios bagulho",
            "cod_barras": "898726987293",
            "preco_venda": 12.00,
            "preco_compra": 8.00,
            "medida": 1,
            "unidade": "un",
            "tags": ['essencia', 'mix', 'doce', 'especial', 'mc', 'zomo'],
            "data_cadastro": '24/06/2019',
            "data_alteracao": None,
            "ativo": True 
        },
        {
            "id": 3,
            "nome": "Essência No Woman No Cry",
            "marca": "Blue Horse",
            "tipo": "Essência",
            "descricao": "Essência mix de varios bagulho que fica bom",
            "cod_barras": "898726987293",
            "preco_venda": 14.00,
            "preco_compra": 8.00,
            "medida": 1,
            "unidade": "un",
            "tags": ['essencia', 'mix', 'doce', 'especial', 'bob marley', 'blue horse'],
            "data_cadastro": '24/06/2019',
            "data_alteracao": None,
            "ativo": True 
        }]

        schema = ProdutoSchema(many=True).dumps(lista)


        return schema