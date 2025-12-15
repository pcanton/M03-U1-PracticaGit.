import unittest
from security import validar_password

class TestSecurity(unittest.TestCase):

    def test_contrasenya_curta_retorna_fals(self):
        contrasenya_curta = "abcde12"
        self.assertFalse(validar_password(contrasenya_curta))

    # AQUEST NOU TEST HA D'ANAR AQUÍ DINS, AMB LA INDENTACIÓ ADEQUADA
    def test_contrasenya_llarga_retorna_cert(self):
        """
        Prova que una contrasenya de més de 8 caràcters retorna True.
        """
        contrasenya_llarga = "moltsegura123" # 13 caràcters
        self.assertTrue(validar_password(contrasenya_llarga))


if __name__ == '__main__':
    unittest.main()
