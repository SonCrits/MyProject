from odoo.tests.common import tagged
from odoo.exceptions import UserError

from .common import Common


@tagged('post_install', '-at_install')
class TestEditLogNote(Common):

    # ---------------admin user test---------------------

    def test_edit_message_channel_tag_with_admin_user(self):
        # default: message_edit_lock = True
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
    
    def test_edit_message_channel_no_tag_with_admin_user(self):
        # default: message_edit_lock = True
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_admin)._update_content(
                    body='<p>123</p>',
                    attachment_ids=[]
                )

    def test_channel_disable_edit_message_lock_with_admin_user(self):
        self.channel.write({
                'message_edit_lock': False
        })
        self.message_channel_no_tag_by_user.with_user(self.user_admin)._update_content(
            body='<p>123</p>',
            attachment_ids=[]
        )
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
            
    def test_edit_log_note_no_tag_with_admin_user(self):
        # default: message_edit_lock = True
        self.message_log_note_no_tag_by_user.with_user(self.user_admin)._update_content(
            body='<p>123</p>',
            attachment_ids=[]
        )
        
    def test_edit_log_note_tag_with_admin_user(self):
        with self.assertRaises(UserError):
            self.message_log_note_tag_by_user.with_user(self.user_admin)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
        
    def test_delete_attachment_message_with_admin_user(self):
        # default: message_edit_lock = True
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin)._update_content(
                    body='<p>Hello Attachment</p>',
                    attachment_ids=[]
            )

    # --------------------common user test-------------------------------
    def test_channel_disable_edit_message_lock_with_user(self):
        self.channel.write({
                'message_edit_lock': False
        })
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo).unlink()
        self.message_channel_no_tag_by_user.with_user(self.user_demo)._update_content(
            body='Modify message no mentions someone',
            attachment_ids=[]
        )
        self.message_channel_no_tag_by_user.with_user(self.user_demo).unlink()

    def test_channel_enable_edit_message_lock_with_user(self):
        self.channel.write({
            'message_edit_lock': True
        })
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo).unlink()
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_demo)._update_content(
                body='Modify message no mentions someone',
                attachment_ids=[]
            )
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_demo).unlink()

    def test_edit_message_channel_tag_with_user(self):
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )

    def test_edit_message_log_note_tag_with_user(self):
        with self.assertRaises(UserError):
            self.message_log_note_tag_by_user.with_user(self.user_demo)._update_content(
                body='modify message log note mentions someone',
                attachment_ids=[]
            )

    def test_delete_message_log_note_tag_with_user(self):
        with self.assertRaises(UserError):
            self.message_log_note_tag_by_user.with_user(self.user_demo).unlink()

    # update content yêu cầu quyền sudo mới có phép đọc <tracking_value_ids>
    def test_edit_message_log_note_no_tag_with_user(self):
        self.message_log_note_no_tag_by_user.with_user(self.user_demo).sudo()._update_content(
            body='modify message log note no mentions someone',
            attachment_ids=[]
        )
