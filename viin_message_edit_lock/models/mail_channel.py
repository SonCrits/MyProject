from odoo import models, fields, _
from odoo.exceptions import UserError


class Channel(models.Model):
    _inherit = 'mail.channel'

    message_edit_lock = fields.Boolean(string='Prevent editing and deleting messages',
                                       help="If enabled, prevent editing/deleting messages in this chat channel",
                                       default=True)

    def _check_can_update_message_content(self, message):
        if message.partner_ids:
            raise UserError(_("You may be able to edit or delete a note only if its content does not mention anyone"))
        if message:
            for r in self:
                if r.message_edit_lock and r.channel_type != 'chat':
                    raise UserError(_("This channel does not allow message modification / deletion."))
        return super()._check_can_update_message_content(message)

    def write(self, vals):
        if 'message_edit_lock' in vals:
            for r in self:
                if not (self.env.user == r.create_uid or self.env.user.has_group('base.group_system')):
                    raise UserError(_("Only the creator of the channel %s or the manager can modify the field 'Prevent editing and deleting messages' ") % (self.display_name))
        return super(Channel, self.with_context(delete_mail_thread=True)).write(vals)
