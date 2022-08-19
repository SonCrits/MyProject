from odoo import models, fields, api


class Project(models.Model):   
    _inherit = 'project.project'

    budget_line_ids = fields.One2many('crossovered.budget.line', 'project_id', string='Budget Line')
    budget_count = fields.Float(string='Budget', compute='_compute_budget')
    contract_count = fields.Integer(string='Contract Count', compute='_compute_contract')

    @api.depends('budget_line_ids')
    def _compute_budget(self):
        for r in self:
            r.budget_count = sum(r.budget_line_ids.mapped('planned_amount'))

    @api.depends('analytic_account_id')
    def _compute_contract(self):
        analytic_name = self.analytic_account_id.name
        contract = self.env["hr.contract"].search([('analytic_account_id', '=', analytic_name)])
        for r in self:
            r.contract_count = len(contract) if contract else 0
