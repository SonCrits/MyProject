from odoo import fields, models


class Restaurant(models.AbstractModel):
    _name = 'restaurant'
    _inherit = "service.industry"
    _description = 'Restaurant AbsModel'
    
    table_ids = fields.One2many('table', 'restaurant_id', string='Table')
    
    #prototed method
    def _cacul_price(self, spending_expenses, employee_salary, tax_money):
        price = sum(self.table_ids.mapped._cacul_price()) - (spending_expenses + employee_salary + tax_money)
        return  price
    
    #gọi tới hàm __get_price và sẽ gây lỗi vì trường này là private
    def _cacul_price_error(self, spending_expenses, employee_salary, tax_money):
        price = sum(self.table_ids.mapped.__get_price()) - (spending_expenses + employee_salary + tax_money)
    

class RestaurantNormal(models.Model):
    _name = 'restaurant.normal'
    _inherit = 'restaurant'
    description = 'Restaurant Normal'
    
    tax_money = fields.Float(string='Tax Money', default=500)
    
    def _cacul_employee_salary(self):
        employee_salary = sum(self.user_ids.mapped('salary'))
        return employee_salary
    
#-------------------------private method can not use another class--------------------------
    def __get_employee_price(self):
        employee_salary = sum(self.user_ids.mapped('salary'))
        return employee_salary
#--------------------------------------------------------------------------------------------
    
    #inherit
    def _cacul_price(self, spending_expenses, employee_salary, tax_money):
        tax_money = self.tax_money
        employee_salary = self._cacul_employee_salary()
        spending_expenses = self.spending_expenses
        return  super().cacul_price(spending_expenses, employee_salary, tax_money)
    
class RestaurantVip(models.Model):
    _name = 'restaurant.vip'
    _inherit = 'restaurant.nomarl'
    description = 'Restaurant Vip'
    
#------------------------------error method---------------------------------------------------
    def action_pay_sip(self):
        employee_salary = self.__get_employee_price()
        #employee_salary = self.super(RestaurantVip, self.__get_employee_price())
        employee_salary.action_pay_sip()
