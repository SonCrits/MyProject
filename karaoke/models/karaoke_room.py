from odoo import fields, models, api


class KaraokeRoom(models.Model):
    _name = 'karaoke.room'
    _inherit = 'room'
    _description = 'Karaoke Room'
    
    currency_id = fields.Many2one('res.currency', string='Journal Currency')
    price = fields.Monetary(string='Room Price')
    start_time = fields.Datetime(string='Start Time')
    stop_time = fields.Datetime(string='Stop Time')
    room_price = fields.Float(string='Room Price', compute='_compute_price')
    employee_ids = fields.One2many('res.users', 'karaoke_room_id', string='Employee')
    employee_price = fields.Monetary(string='Employee Price')
    employee_sum_price = fields.Monetary(string='Employee Sum price', compute='_compute_sum_employee_price')
    
    @api.depends('price', 'start_time', 'stop_time')
    def _compute_price(self):
        for r in self:
            r.room_price = (r.price + r.employee_price) * (r.stop_time - r.start_time) / 60
        