from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from datetime import date, timedelta

class TestValidadorEdad(TransactionCase):

    def test_usuario_mayor_13(self):
        usuario = self.env['res.users'].create({
            'name': 'Usuario Mayor',
            'login': 'mayor@example.com',
            'email': 'mayor@example.com',
            'fecha_nacimiento': date.today() - timedelta(days=365*20),
        })
        self.assertTrue(usuario)

    def test_usuario_menor_13(self):
        with self.assertRaises(ValidationError):
            self.env['res.users'].create({
                'name': 'Usuario Menor',
                'login': 'menor@example.com',
                'email': 'menor@example.com',
                'fecha_nacimiento': date.today() - timedelta(days=365*10),
            })
