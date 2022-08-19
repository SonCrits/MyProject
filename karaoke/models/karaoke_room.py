from odoo import fields, models, api


class KaraokeRoom(models.Model):
    _name = 'karaoke.room'
    _description = 'Karaoke Room'
    
    name = fields.Char(string='Name', required=True)
    currency_id = fields.Many2one('res.currency', string='Currency')
    price = fields.Monetary(string='Price/A Hourse')
    karaoke_id = fields.Many2one('karaoke.contructor')
