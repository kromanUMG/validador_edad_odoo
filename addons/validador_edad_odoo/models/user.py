from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date

class ResUsers(models.Model):
    _inherit = 'res.users'

    fecha_nacimiento = fields.Date(string='Fecha de nacimiento')

    @api.constrains('fecha_nacimiento')
    def _check_edad_minima(self):
        for record in self:
            if record.fecha_nacimiento:
                today = date.today()
                edad = today.year - record.fecha_nacimiento.year - (
                    (today.month, today.day) < (record.fecha_nacimiento.month, record.fecha_nacimiento.day)
                )
                if edad < 13:
                    raise ValidationError("No se permite registrar usuarios menores de 13 años.")