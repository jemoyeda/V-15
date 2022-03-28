from odoo import models, fields

class email(models.Model):
    _inherit = 'sale.order'

    email = fields.Char(string='Correo electronico')

