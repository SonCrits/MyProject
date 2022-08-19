from odoo.tests.common import tagged
from odoo.exceptions import UserError

from .common import Common


@tagged('post_install', '-at_install')
class TestWriteUnlinkMailMessage(Common):
    
    #--------------------admin test-----------------------------------------------
    
    def test_channel_disable_delete_message_lock_with_admin(self):
        self.channel.write({
                'message_edit_lock': False
        })      
        self.message_channel_no_tag_by_user.with_user(self.user_admin).unlink()
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin).unlink()

    def test_channel_enable_delete_message_lock_with_admin(self):
        self.channel.write({
            'message_edit_lock': True
        })
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_admin).unlink()
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_admin).unlink()

    def test_delete_log_note_tag_with_admin(self):
        with self.assertRaises(UserError):
            self.message_log_note_tag_by_user.with_user(self.user_admin).unlink()    

    def test_delete_log_note_no_tag_with_admin(self):
        self.message_log_note_no_tag_by_user.with_user(self.user_admin).unlink()
       
    def test_write_message_tag_with_super_admin(self):
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

    #--------------------------Common User Test----------------------------------------
    
    def test_channel_disable_delete_message_lock_with_user(self):
        self.channel.write({
                'message_edit_lock': False
        })      
        self.message_channel_no_tag_by_user.with_user(self.user_demo).unlink()
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo).unlink()

    def test_channel_enable_delete_message_lock_with_user(self):
        self.channel.write({
            'message_edit_lock': True
        })
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_demo).unlink()
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo).unlink()
              
    def test_delete_log_note_tag_with_user(self):
        with self.assertRaises(UserError):
            self.message_log_note_tag_by_user.with_user(self.user_demo).unlink()    

    def test_delete_log_note_no_tag_with_user(self):
        self.message_log_note_no_tag_by_user.with_user(self.user_demo).unlink()   
        
    def test_write_message_tag_with_user(self):
        with self.assertRaises(UserError):
            self.message_channel_no_tag_by_user.with_user(self.user_demo).write({
                "body":'<p>Modify Message Channel no tag</p>',
            })
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo).write({
                "body":'<p>Modify Message Channel tag</p>',
            })
        with self.assertRaises(UserError):
            self.message_channel_tag_by_user.with_user(self.user_demo).unlink()
