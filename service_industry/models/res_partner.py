from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    service_industry_id = fields.Many2one('service.industry', string='Service Industry')
