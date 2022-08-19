from odoo import fields, models, api


class KaraokeContructor(models.AbstractModel):
    _name = 'karaoke.contructor'
    _description = 'karaoke contructor'
    name = fields.Char(string='Name', required=True)
    rating = fields.Integer(string='Rating')
    service = fields.Boolean(string='Service')
    room_ids = fields.One2many('karaoke.room', 'karaoke_id')
    price = fields.Float(string='Price', compute="_compute_price")
    
    @api.depends('room')
    def caculator_money(self):
        pass

class KaraokeCity(models.Model):
    _name = 'karaoke.city'
    _inherit = 'karaoke.contructor'
    _description = 'Karaoke City'
    
    tax_money = fields.Float(string='Tax Money')
    
    @api.depends('room')
    def caculator_money(self):
        for r in self:
            r.price = sum(r.room_ids.mapped('price')) - r.tax_money
