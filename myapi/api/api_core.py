"""
Arquivo exemplo de funcionalidade de API para criação de endpoints.
"""

from flask import Blueprint, render_template, make_response
from myapi.constants.constants_core import api_return_data
import json

api = Blueprint('api', __name__)


@api.route('/')
def user_home():
    return render_template('api.html', api_data=api_return_data)


@api.route('/getdata', methods=['GET'])
def get_data():
    """
    <html>
    <head>
    </head>
    <body>
        <div>
            <p style="color: red; font-size: 1.2em;">
            Método de pega dado do arquivo constants e retorna em JSON
            com cabeçalho na requisição de Content-Type: application/json.
            </p>
        </div>
        <div>
            <p style="color: green; font-size: 1.2em;">:return: json</p>
        </div>
    </body>
    </html>
    """
    # Transformando dict em retorno do tipo JSON.
    json_return = json.dumps(api_return_data)

    # Escrita de conteúdo de retorno.
    response = make_response(json_return)

    # Escrita de cabeçalho de retorno.
    response.headers['Content-Type'] = 'application/json'

    return response
