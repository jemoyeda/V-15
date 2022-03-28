from odoo import models, fields

class email(models.model):
    _inherit = 'sale.order'

    email = fields.Char(string='Correo electronico')

