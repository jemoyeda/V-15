import odoo import models, fields

class StockpickingInherit(models.Model):
    _inherit = "stock.picking"

    motivo = fields.Char("Motivo")
    

