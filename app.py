import os

from api import produto_v1

from config import iniciar_logger, iniciar_variaveis_ambiente, \
    definir_ambiente, configurar_healthcheck, iniciar_swagger, init_cors, \
    log_requests

from flask import Flask

def criar_app(usar_var_env=True, testing=False):
    app = Flask(__name__)

    # Configura e formata os logs
    iniciar_logger(app)

    # Configura o ambiente a partir das variáves de ambiente
    if usar_var_env:
        # Cria as variáveis de ambiente contidas no arquivo .env
        iniciar_variaveis_ambiente(app)

        # Configura a aplicação de acordo com as variáveis de ambiente
        definir_ambiente(app)

    iniciar_swagger(app)
    configurar_healthcheck(app)
    init_cors(app)
    log_requests(app)

    if testing:
        app.config["TESTING"] = True
    
    app.logger.info('Registrando blueprint: produto_v1')
    app.register_blueprint(produto_v1)
    
    return app

if __name__ == '__main__':
    app = criar_app(usar_var_env=True)
    app_name = 'e-simples'
    porta = os.getenv('APP_PORTA', 8081)

    try:
        app.run(debug=True, port=int(porta), host='0.0.0.0')
    except Exception as ex:
        app.logger.error(f'''Erro ao levantar a aplicação.
Exception: {str(ex)}''')