from odoo import models, fields

class Partner(models.Model):

    _inherit = "res.partner"

    certificat = fields.Boolean(string="Certificat ISO9001")

    is_committee = fields.Boolean(string="Is a committee")