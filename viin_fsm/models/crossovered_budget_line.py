from odoo import fields, models


class CrossoveredBudgetLine(models.Model):
    
    _inherit = 'crossovered.budget.line'
    
    project_id = fields.Many2one('project.project', string='Project')
