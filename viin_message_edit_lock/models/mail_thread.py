from odoo import models, _
from odoo.exceptions import UserError


class MailThread(models.AbstractModel):
     
    _inherit = 'mail.thread'
    
    def _check_can_update_message_content(self, message):
        if message.partner_ids:
            raise UserError(_("You may be able to edit or delete a note only if its content does not mention anyone"))   
        return super()._check_can_update_message_content(message) 
