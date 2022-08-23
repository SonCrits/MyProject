from odoo import fields, models


class Table(models.Model):
    _name = 'table'
    _description = 'Restaurant Table'
    
    name = fields.Char(string='name', required=True)
    table_type = fields.Selection(selection=[
        ('4slot', '4 Slot'),
        ('6slot', '6 Slot'),
        ('10slot', '10 Slot'),
    ],string='Table Slot', default='4slot')
    product_template_ids = fields.One2many('product.template', 'table_id')
    
    def _cacul_price(self):
        price = sum(self.product_template_ids.mapped('price') * self.product_template_ids.SL)
        return price
    
    def __get_price(self):
        return self._cacul_price()
