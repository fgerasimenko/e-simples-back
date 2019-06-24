import os
import logging
import time

from dotenv import load_dotenv
from flasgger import Swagger
from flask import request
from flask_cors import CORS
from healthcheck import HealthCheck, EnvironmentDump


def configurar_healthcheck(app):
    app.logger.info('Iniciando Healthcheck')
    health = HealthCheck(app, "/healthcheck")
    EnvironmentDump(app, "/environment")

    def versao():
        import datetime

        return True, {
            'versao': '1.0.0',
            'gerado_em': str(datetime.datetime.now())
        }

    health.add_check(versao)

def iniciar_variaveis_ambiente(app):
    app.logger.info('Carregando variaveis de ambiente')
    load_dotenv()

def iniciar_logger(app):
    logging.basicConfig(level=logging.INFO)
    app.logger.info('Iniciando Logs')


def definir_ambiente(app, ambiente=None):
    app.logger.info('Verificando ambiente')
    if not ambiente:
        ambiente = os.getenv("AMBIENTE")

    app.config['TESTING'] = ambiente == 'test'
    app.config['DEBUG'] = ambiente == 'development'
    app.config['ENV'] = 'production' if ambiente == 'production' \
        else 'development'
    app.logger.info('Ambiente %s definido' % (app.config['ENV']))


def iniciar_swagger(app):
    app.logger.info('Iniciando Swagger')
    swagger = Swagger(app)

    return swagger


def init_cors(app):
    app.logger.info('Iniciando CORS')
    CORS(app, resources={r"/*": {"origins": "*"}})


def log_requests(app):

    @app.before_request
    def log_request_info():
        timestamp = time.strftime('[%Y-%b-%d %H:%M]')
        app.logger.info(
            'Request: %s %s %s %s %s %s %s',
            timestamp,
            request.remote_addr,
            request.method,
            request.scheme,
            request.full_path,
            request.headers,
            request.get_data())

    @app.after_request
    def after_request(response):
        timestamp = time.strftime('[%Y-%b-%d %H:%M]')
        app.logger.info(
            'Response: %s %s %s %s %s %s %s',
            timestamp,
            request.remote_addr,
            request.method,
            request.scheme,
            request.full_path,
            response.status,
            response.get_data())

        return response
