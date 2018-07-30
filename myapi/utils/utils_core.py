"""
Arquivo com métodos utilitários centralizados.
"""

import hashlib


class Utilities:
    """
    Classe de métodos utilitários
    """

    def hash_generator(self, value):
        """
        Gerador de hash sha256.
        :param value: string (texto a ser encriptado)
        :return: string
        """
        hash_string = hashlib.sha256(bytes(value))
        return hash_string.hexdigest()
