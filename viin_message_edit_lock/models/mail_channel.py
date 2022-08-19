from odoo import models, fields, _
from odoo.exceptions import UserError


class Channel(models.Model):
    
    _inherit = 'mail.channel'

    message_edit_lock = fields.Boolean(string='Prevent editing and deleting messages',
                                       help="If enabled, avoiding to edit/deleting message in this channel",
                                       default=True)
    
    def _check_can_update_message_content(self, message):
        if message.partner_ids:
            raise UserError(_("You may be able to edit or delete a note only if its content does not mention anyone"))
        if message:
            for r in self:
                if r.channel_type != 'chat' and r.message_edit_lock:
                    raise UserError(_("This channel does not allow message modification / deletion."))
        return super()._check_can_update_message_content(message)
    
    def write(self, vals):
        if 'message_edit_lock' in vals:
            for r in self:
                if not (self.env.user == r.create_uid or self.env.user.has_group('base.group_system')):
                    raise UserError(_("Only the creator of the channel or the users in the groups %s can modify the field %s") % (self.name, self.message_edit_lock))
        return super().write(vals)                                      
