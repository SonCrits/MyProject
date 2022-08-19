from odoo import models


class MailMail(models.Model): 
    _inherit = 'mail.mail'
    
    def unlink(self):
        return super(MailMail, self.with_context(delete_mail_thread=True)).unlink()
