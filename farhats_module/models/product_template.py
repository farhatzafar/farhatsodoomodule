from odoo import fields, models

class ProductTemplate(models.Model):

    _inherit = "product.template"

    committee_id = fields.Many2one("res.partner", string="Committee", domain=[('is_commmittee','=',True)])