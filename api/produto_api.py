# -*- coding: utf-8 -*-
"""Blueprint com endpoints para o Billing
"""
import os
import uuid
import json

from flask import Blueprint, make_response, request
from flasgger import swag_from

from service import ProdutoService

produto_v1 = Blueprint(
    "produto_v1", __name__, url_prefix="/esimples")


bucket = os.getenv("BUCKET")


@swag_from('../../../sensoriamento.yml')
@produto_v1.route("/", methods=['OPTIONS'])
def options():
    response = make_response()

    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")

    return response

@swag_from('../../../sensoriamento.yml')
@produto_v1.route("/produtos", methods=['GET'])
def listar_produtos():
    service = ProdutoService()

    obj = service.get_all()
    
    return obj