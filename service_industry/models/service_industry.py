from odoo import fields, models


class ServiceIndustry(models.AbstractModel):
    _name = 'service.industry'
    _description = 'Service Industry'
    
    name = fields.Char(string='Name')
    user_ids = fields.One2many('res.users', 'service_industry_id', string='User')
    partner_ids = fields.One2many('res.partner', 'service_industry_id', string='Partner')
    currency_id = fields.Many2one('res.currency', string='Journal Currency')
    spending_expenses = fields.Float(string='Spending Expenses', default='2000')
    total_revenue = fields.Float(string='Total Revenue', compute='_compute_total_revenue')
    
    #hàm thuần ảo, có thể tính dk nhiều kiểu tiền dịch vụ
    def compute_interest_rate(self, costs_incurred):
        interest_rate = self.total_revenue - self.spending_expenses - costs_incurred      
        return  interest_rate
    
    def _compute_total_revenue(self):
        pass
