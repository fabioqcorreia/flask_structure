"""
Arquivo de funcionalidades padrão de usuário.
"""

from flask import Blueprint, render_template

# Exemplo de criação de blueprint.
user = Blueprint('user', __name__, template_folder='templates')


@user.route('/')
def user_home():
    """
    Documentação de método básica da homepage de usuário (PEP 8)
    :return: user.html <- página inicial de usuário do exemplo.
    """
    return render_template('user.html')