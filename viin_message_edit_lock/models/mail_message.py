from odoo import models


class Message(models.Model):
    
    _inherit = 'mail.message'
    
    def write(self, vals):
        thread = self.env[self.model].browse(self.res_id)
        thread._check_can_update_message_content(self)
        return super(Message, self).write(vals)
    
    def unlink(self):
        for r in self:
            thread = self.env[self.model].browse(r.res_id)   
            thread._check_can_update_message_content(r)
        return super(Message, self).unlink()
