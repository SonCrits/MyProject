from odoo import  models, _
from odoo.exceptions import UserError


class Message(models.Model):
    _inherit = 'mail.message'

    def check_update_content_message(self):
        for r in self:
            channel = self.env['mail.channel'].browse(r.res_id)
            if r.partner_ids:
                raise UserError(_("You may be able to edit or delete a note only if its content does not mention anyone"))
            if r.model == 'mail.channel' and channel and channel.channel_type != 'chat' and channel.message_edit_lock:
                    raise UserError(_("This channel does not allow message modification / deletion."))
    
    def write(self, vals):
        if 'body' in vals and not self.env.user._is_superuser():
            self.check_update_content_message()  
        return super().write(vals)

    def unlink(self):
        if not self._context.get('delete_mail_thread', False) and not self.env.user._is_superuser():
            self.check_update_content_message()
        return super(Message, self).unlink()
