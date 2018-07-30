from myapi.utils import utils_core
import unittest
import random
import string

class BasicTests(unittest.TestCase):
    """
    Classe de testes básicos.
    """

    def test_util_hash(self):
        """
        Verificar se o tamanho da hash gerada é de tamanho da especificação de criptografia SHA-256.
        :return:
        """
        utils = utils_core.Utilities()
        secret_text = ''.join(random
                              .SystemRandom()
                              .choice(string.ascii_uppercase + string.digits) for _ in range(8)
                              ).encode('utf-8')
        generated_hash = utils.hash_generator(secret_text)
        self.assertTrue(len(generated_hash)==64)

if __name__ == '__main__':
    unittest.main()