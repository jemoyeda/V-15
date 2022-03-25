from odoo import models, fields

class motivo(models.Model):
    _inherit = 'stock.picking'

    motivo = fields.Char("Motivo")
    

