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
        cls.channel_test_demo_create = cls.env["mail.channel"].with_user(cls.user_demo).create({
            'name': 'channel test',
            'channel_type': 'channel',
            'public': 'groups'
        })
        cls.attachment_id = cls.env['ir.attachment'].with_user(cls.user_demo).create({
            'name': 'viin_message_edit_lock_attachment',
            'res_id': cls.channel.id,
            'res_model': 'mail.channel',
        })
        cls.message_channel_tag_by_user = cls.channel.with_user(cls.user_demo).message_post(
            body='<span><a href="http://localhost:8015/web#model=res.partner&amp;id=7" class="o_mail_redirect" data-oe-id="7" data-oe-model="res.partner" target="_blank">@Marc Demo</a> Hello group channel</span>',
            message_type='comment',
            subtype_id=cls.env.ref('mail.mt_comment').id,
            partner_ids=[7],
            attachment_ids=[cls.attachment_id.id]
        )
        cls.message_channel_no_tag_by_user = cls.channel.with_user(cls.user_demo).message_post(
            body='<p>Hello</p>',
            message_type='comment',
            subtype_id=cls.env.ref('mail.mt_comment').id,
        )
        cls.attachment_res_partner = cls.env['ir.attachment'].with_user(cls.user_demo).create({
            'name': 'viin_message_edit_lock_attachment',
            'res_id': cls.res_partner.id,
            'res_model': 'res.partner',
        })
        cls.message_log_note_tag_by_user = cls.res_partner.with_user(cls.user_demo).message_post(
            body='<span><a href="http://localhost:8015/web#model=res.partner&amp;id=7" class="o_mail_redirect" data-oe-id="7" data-oe-model="res.partner" target="_blank">@Marc Demo</a>Hello Log note</span>',
            message_type='comment',
            subtype_id=cls.env["mail.message.subtype"].search([('name', '=', 'Note')]).id,
            partner_ids=[7],
            attachment_ids=[cls.attachment_res_partner.id]
        )
        cls.message_log_note_no_tag_by_user = cls.res_partner.with_user(cls.user_demo).message_post(
            body='<p>Hello</p>',
            message_type='comment',
            subtype_id=cls.env["mail.message.subtype"].search([('name', '=', 'Note')]).id,
        )
