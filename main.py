"""
Arquivo de execução principal do Flask.

Este arquivo irá iniciar a execução do servidor de desenvolvimento, lembrando que em produção, o recomendado é usar
um servidor WSGI de produção como, por exemplo, o gunicorn.
"""

import configparser
from flask import Flask, render_template
from myapi.user.user_core import user
from myapi.api.api_core import api
from myapi.docs.docs_core import docs

# Lendo configurações do arquivo config.ini
config = configparser.ConfigParser()
config.read('config/config.ini')
host = config['default']['host_ip']
port = int(config['default']['host_port'])


app = Flask(__name__)

# Secret key para utilização de sessões. Gerada através do comando shell
# $ python -c 'import secrets; secrets.token_hex(16)'
app.secret_key = 'e05527c9d7d0ef8e9fc45c73f07787b5'

# Exemplos de registro de Blueprints.
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(docs, url_prefix='/docs')


@app.route("/")
def home_page():
    """
    Documentação básica de métodos (PEP 8)
    :return: index.html <- página inicial do servidor.
    """
    return render_template('index.html')


# Execução automática do servidor de desenvolvimento com configurações externalizadas via arquivo config.ini.
if __name__ == '__main__':
    app.run(host=host, port=port)