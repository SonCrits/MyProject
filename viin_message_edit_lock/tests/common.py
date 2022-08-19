from odoo.tests.common import TransactionCase


class Common(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super(Common, cls).setUpClass()        
        cls.channel = cls.env.ref('mail.channel_all_employees')     
        cls.user_admin = cls.env.ref("base.user_admin")
        cls.user_demo = cls.env.ref("base.user_demo")
        cls.res_partner = cls.env["res.partner"].create({
            'name': 'partner test'
        })
        cls.message_attachment_record_set_tag = cls.env['mail.message'].search([('attachment_ids','!=', False), ('partner_ids', '!=', False), ('model', '!=', 'mail.channel')])
        cls.message_attachment_tag = cls.env["mail.message"].browse(cls.message_attachment_record_set_tag.ids[0])
        

        cls.message_channel_tag_by_user = cls.channel.with_user(cls.user_demo).message_post(
            body='<span><a href="http://localhost:8015/web#model=res.partner&amp;id=7" class="o_mail_redirect" data-oe-id="7" data-oe-model="res.partner" target="_blank">@Marc Demo</a> Hello group channel</span>',
            message_type='comment',
            subtype_id=cls.env.ref('mail.mt_comment').id,
            partner_ids=[7]
        )
        cls.message_channel_no_tag_by_user = cls.channel.with_user(cls.user_demo).message_post(
            body='<p>Hello</p>',
            message_type='comment',
            subtype_id=cls.env.ref('mail.mt_comment').id,
        )
        cls.message_log_note_tag_by_user = cls.res_partner.with_user(cls.user_demo).message_post(
            body='<span><a href="http://localhost:8015/web#model=res.partner&amp;id=7" class="o_mail_redirect" data-oe-id="7" data-oe-model="res.partner" target="_blank">@Marc Demo</a>Hello Log note</span>',
            message_type='comment',
            subtype_id=cls.env["mail.message.subtype"].search([('name', '=', 'Note')]).id,
            partner_ids=[7]
        )
        cls.message_log_note_no_tag_by_user = cls.res_partner.with_user(cls.user_demo).message_post(
            body='<p>Hello</p>',
            message_type='comment',
            subtype_id=cls.env["mail.message.subtype"].search([('name', '=', 'Note')]).id,
        )
