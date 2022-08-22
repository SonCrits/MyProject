from odoo import fields, models, api, _
from odoo.exceptions import UserError


class KaraokeContructor(models.AbstractModel):
    _name = 'karaoke.contructor'
    _inherit = 'service.industry'
    _description = 'karaoke contructor'
    
    rating = fields.Integer(string='Rating')
    service = fields.Boolean(string='Service')
    room_ids = fields.One2many('karaoke.room', 'karaoke_id')
    
    def _compute_total_revenue(self):
        for r in self:
            r.total_revenue = sum(r.room_ids.mapped('price'))

class KaraokeNormal(models.Model):
    _name = 'karaoke.normal'
    _inherit = 'karaoke.contructor'
    _description = 'Karaoke Normal'
    
    @api.depends('room')
    def caculator_money(self):
        for r in self:
            r.price = sum(r.room_ids.mapped('price')) - r.room_ids.employee_sum_price

class KaraokeVip(models.Model):
    _name = 'karaoke.vip'
    _inherit = 'karaoke.contructor'
    _description = 'Karaoke Vip'
    
    tax_money = fields.Float(string='Tax Money', default='0.5', readonly=True)
    
    def check_age_employee(self):
        for r in self:
            if r.room_ids.employee_ids.age > 30:
                raise UserError(_("Employee can't too old"))
    
    def compute_interest_rate(self):
        return super().compute_interest_rate(self, self.tax_money)
