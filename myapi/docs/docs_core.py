"""
Arquivo de exemplo de endpoint docs
"""

from flask import Blueprint, render_template
from myapi.utils import utils_core
from myapi.api import api_core
import random
import string

docs = Blueprint('docs', __name__, template_folder='templates/docs')


@docs.route('/getdata', methods=['GET'])
def get_data_docs():
    """
    Exemplo de busca de documentação via método
    :return: docstring em formato html do método get_data.
    """
    return api_core.get_data.__doc__


@docs.route('/gethash', methods=['GET'])
def get_hash_docs():
    """
    Hash docs exemplo
    :return: template com hash criado em utils a partir de 8 letras e numeros aleatorios criados por SystemRandom.
    """
    utils = utils_core.Utilities()
    hash_string = utils.hash_generator(''.join(random
                                               .SystemRandom()
                                               .choice(string.ascii_uppercase + string.digits) for _ in range(8)
                                               ).encode('utf-8'))

    return render_template('api_doc.html', hash_string=hash_string)
