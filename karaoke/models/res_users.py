from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    karaoke_room_id = fields.Many2one('karaoke.room', string='Karaoke')
    price = fields.Float(related='karaoke_room_id.employee_sum_price')
