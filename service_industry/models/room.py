from odoo import fields, models


class Room(models.AbstractModel):
    _name = 'room'
    _description = 'Room'
    
    name = fields.Char(string='Name', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
