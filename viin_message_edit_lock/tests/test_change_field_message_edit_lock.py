from odoo.tests.common import tagged
from odoo.exceptions import UserError

from .common import Common


@tagged('post_install', '-at_install')
class TestChangeFieldMessageEditLock(Common):
 
    def test_admin_can_change_field_message_edit_lock(self):
        self.channel.with_user(self.user_admin).write({
            'message_edit_lock': False
        })
      
    def test_common_user_cannot_change_field_message_edit_lock(self):
        with self.assertRaises(UserError):
            self.channel.with_user(self.user_demo).write({
                'message_edit_lock': False
            })
      
    def test_create_channel_can_change_field_message_edit_lock(self):
        self.channel_test_demo_create.with_user(self.user_demo).write({
            'message_edit_lock': False
        })
