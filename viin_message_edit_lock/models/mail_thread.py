from odoo import models, _
from odoo.exceptions import UserError


class MailThread(models.AbstractModel):
    _inherit = 'mail.thread'
    
    # Situation:
        # has many register has links with mail.thread
        # when these records have a message that cannot be deleted => do not allow these records to be deleted (eg res.partner)
    # Solution:
        # transport context to when delete the write, not blocked by the function '_check_can_update_message_content' anymore
    def unlink(self):
        return super(MailThread, self.with_context(delete_mail_thread=True)).unlink()
    
    def write(self, vals):
        return super(MailThread, self.with_context(delete_mail_thread=True)).write(vals)

    def _check_can_update_message_content(self, message):
        if message.partner_ids:
            raise UserError(_("You may be able to edit or delete a note only if its content does not mention anyone"))
        return super()._check_can_update_message_content(message)
