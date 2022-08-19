from odoo.tests.common import tagged, users
from odoo.exceptions import UserError
from odoo.addons.viin_message_edit_lock.controllers.discuss import DiscussControllerLock
from odoo.addons.website.tools import MockRequest

from .common import Common


@tagged('post_install', '-at_install')
class TestEditLogNote(Common):

    # ---------------super user test---------------------

    def test_edit_message_channel_tag_with_super_user(self):
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
    
    def test_edit_message_channel_no_tag_with_super_user(self):
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_admin)._update_content(
                    body='<p>123</p>',
                    attachment_ids=[]
                )

    def test_channel_disable_edit_message_lock_with_super_user(self):
        self.channel.with_user(self.user_admin).write({
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
    
    def test_channel_enable_edit_message_lock_with_super_user(self):
        self.channel.with_user(self.user_admin).write({
                'message_edit_lock': True
        })
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_admin)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )
    
    def test_edit_log_note_no_tag_with_super_user(self):
        self.message_log_note_no_tag_by_user.with_user(self.user_admin)._update_content(
            body='<p>123</p>',
            attachment_ids=[]
        )

    def test_edit_log_note_tag_with_super_user(self):
        with self.assertRaises(UserError):
            self.message_log_note_tag_by_user.with_user(self.user_admin)._update_content(
                body='<p>123</p>',
                attachment_ids=[]
            )

    # -----rpc------
    def test_channel_disable_delete_message_lock_with_super_user(self):
        self.channel.with_user(self.user_admin).write({
                'message_edit_lock': False
        })
        self.message_channel_no_tag_by_user.with_user(self.user_admin).unlink()
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin).unlink()
    
    def test_channel_enable_delete_message_lock_with_super_user(self):
        self.channel.with_user(self.user_admin.id).write({
            'message_edit_lock': True
        })
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_admin).unlink()
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin).unlink()
    
    def test_delete_log_note_tag_with_super_user(self):
        with self.assertRaises(UserError):
            self.message_log_note_tag_by_user.with_user(self.user_admin).unlink()    
    
    def test_delete_log_note_no_tag_with_super_user(self):
        self.message_log_note_no_tag_by_user.with_user(self.user_admin).unlink()
    
    def test_write_message_tag_with_super_user(self):
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_admin).write({
                "body":'<p>Modify Message Channel no tag</p>',
            })
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin).write({
                "body":'<p>Modify Message Channel tag</p>',
            })
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin).unlink()
    
    @users('admin')
    def test_delete_attachment_message_with_super_user_by_rpc(self):
        with self.assertRaises(UserError):
            with MockRequest(self.env):
                DiscussControllerLock.mail_attachment_delete(self, self.message_attachment_tag.attachment_ids.id)

    # --------------------common user test-------------------------------
    # def test_channel_disable_edit_message_lock_with_user(self):
    #     self.channel.write({
    #             'message_edit_lock': False
    #     })
    #     with self.assertRaises(UserError):
    #         self.message_channel_tag_by_user.with_user(self.user_demo)._update_content(
    #             body='<p>123</p>',
    #             attachment_ids=[]
    #         )
    #     with self.assertRaises(UserError):
    #         self.message_channel_tag_by_user.with_user(self.user_demo).unlink()
    #     self.message_channel_no_tag_by_user.with_user(self.user_demo)._update_content(
    #         body='Modify message no mentions someone',
    #         attachment_ids=[]
    #     )
    #     self.message_channel_no_tag_by_user.with_user(self.user_demo).unlink()
    #
    # def test_channel_enable_edit_message_lock_with_user(self):
    #     self.channel.write({
    #         'message_edit_lock': True
    #     })
    #     with self.assertRaises(UserError):
    #         self.message_channel_tag_by_user.with_user(self.user_demo)._update_content(
    #             body='<p>123</p>',
    #             attachment_ids=[]
    #         )
    #     with self.assertRaises(UserError):
    #         self.message_channel_tag_by_user.with_user(self.user_demo).unlink()
    #     with self.assertRaises(UserError):
    #         self.message_channel_no_tag_by_user.with_user(self.user_demo)._update_content(
    #             body='Modify message no mentions someone',
    #             attachment_ids=[]
    #         )
    #     with self.assertRaises(UserError):
    #         self.message_channel_no_tag_by_user.with_user(self.user_demo).unlink()
    #
    # def test_edit_message_channel_tag_with_user(self):
    #     with self.assertRaises(UserError):
    #         self.message_channel_tag_by_user.with_user(self.user_demo)._update_content(
    #             body='<p>123</p>',
    #             attachment_ids=[]
    #         )

    # def test_delete_message_channel_tag_with_user(self):
    #     with self.assertRaises(UserError):
    #         self.message_channel_tag_by_user.with_user(self.user_demo).unlink()

    # def test_edit_message_channel_no_tag_with_user(self):
    #     with self.assertRaises(UserError):
    #         self.message_channel_no_tag_by_user.with_user(self.user_demo)._update_content(
    #             body='modify message channel no mentions someone',
    #             attachment_ids=[]
    #         )
    #
    # def test_delete_message_channel_no_tag_with_user(self):
    #     with self.assertRaises(UserError):
    #         self.message_channel_no_tag_by_user.with_user(self.user_demo).unlink()
    #
    # def test_edit_message_log_note_tag_with_user(self):
    #     with self.assertRaises(UserError):
    #         self.message_log_note_tag_by_user.with_user(self.user_demo)._update_content(
    #             body='modify message log note mentions someone',
    #             attachment_ids=[]
    #         )
