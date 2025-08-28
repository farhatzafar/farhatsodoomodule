from odoo import fields, models

class SaleOrderLine(models.Model):

    _inherit = "sale.order.line"

    done = fields.Char(string="Done")

    insp = fields.Char(string="Insp.")