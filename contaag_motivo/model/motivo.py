# -*- coding: utf-8 -*-


class StockpickingInherit(models.Model):
    _inherit = "stock.picking"

    motivo = fields.Char("Motivo")
    

