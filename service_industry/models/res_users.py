from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    service_industry_id = fields.Many2one('service.industry', string='Service Industry')
