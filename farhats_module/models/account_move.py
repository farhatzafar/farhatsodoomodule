from odoo import fields, models

class AccountMove(models.Model):

    _inherit = "account.move"

    recipient_id = fields.Many2one("res.partner", string="Recipient")