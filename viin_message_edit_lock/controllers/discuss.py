from odoo import http
from odoo.http import request

from odoo.addons.mail.controllers import discuss


class DiscussControllerLock(discuss.DiscussController):

    @http.route('/mail/attachment/delete', methods=['POST'], type='json', auth='public')
    def mail_attachment_delete(self, attachment_id, access_token=None, **kwargs):
        """Override to avoid delete attatchments while there related mail messages 
        
        """
        attachment_sudo = request.env['ir.attachment'].browse(int(attachment_id)).sudo().exists()
        if attachment_sudo and (attachment_sudo.res_model == 'mail.channel' or isinstance(request.env[attachment_sudo.res_model], request.env['mail.thread'].__class__)):
            message_sudo = request.env['mail.message'].sudo().search([
                ('attachment_ids', 'in', attachment_sudo.ids)
                ], limit=1)
            if message_sudo:
                # record_sudo is either mail.channel or an inheritance of mail.thread (e.g. sale.order, res.partner, etc)
                record_sudo = request.env[attachment_sudo.res_model].browse(int(attachment_sudo.res_id)).sudo().exists()
                record_sudo._check_can_update_message_content(message_sudo)
        
        return super(DiscussControllerLock, self).mail_attachment_delete(attachment_id, access_token, **kwargs)
