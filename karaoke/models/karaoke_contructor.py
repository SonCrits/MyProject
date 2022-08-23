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
    
    def check_age_employee(self):
        pass
    
    #tính tiền nhân viên
    def cacul_employee_salary(self):
        employee = self.env['res.users'].search([('karaoke_room_id', '=!', False)])
        employee_salary = employee.mapped('price')
        return employee_salary

class KaraokeNormal(models.Model):
    _name = 'karaoke.normal'
    _inherit = 'karaoke.contructor'
    _description = 'Karaoke Normal'
    
    
    def check_age_employee(self):
        for r in self:
            if r.room_ids.employee_ids.age > 40:
                raise UserError(_("Employee can't too old"))
    
    
    #chi phí phát sinh thêm. sẽ có khác biệt với karraoke vip
    #đều bao gồm phí phải thanh toán cho nhân viên
    #ở đây ta sẽ gọi lại hàm cacul_employee_salary của model kara contructor
    def compute_interest_rate(self, costs_incurred):
        costs_incurred = self.super().cacul_employee_salary()
        price = sum(self.room_ids.mapped('price')) - costs_incurred
        return price

class KaraokeVip(models.Model):
    _name = 'karaoke.vip'
    _inherit = 'karaoke.contructor'
    _description = 'Karaoke Vip'
    
    #diffirent fields
    tax_money = fields.Float(string='Tax Money', default='0.5', readonly=True)
    
    def check_age_employee(self):
        for r in self:
            if r.room_ids.employee_ids.age > 30:
                raise UserError(_("Employee can't too old"))
    
    ##khác biệt giữa karaoke normal và karaoke vip là tiền thuế
    def compute_interest_rate(self, costs_incurred):
        costs_incurred = self.tax_money + self.super().cacul_employee_salary()
        return super().compute_interest_rate(self, costs_incurred)
