from odoo.tests.common import tagged, users
from odoo.exceptions import UserError
from odoo.addons.viin_message_edit_lock.controllers.discuss import DiscussControllerLock
from odoo.addons.website.tools import MockRequest

from .common import Common


@tagged('post_install', '-at_install')
class TestUnlinkWriteByRPC(Common):

    @users('admin')
    def test_delete_attachment_message_with_admin_by_rpc(self):
        with self.assertRaises(UserError):
            with MockRequest(self.env):
                DiscussControllerLock.mail_attachment_delete(self, self.attachment_id.id)
         
    @users('demo')
    def test_delete_attachment_message_with_user_by_rpc(self):
        with self.assertRaises(UserError), MockRequest(self.env):
            DiscussControllerLock.mail_attachment_delete(self, self.attachment_id.id)
            
    @users('admin')
    def test_delete_attachment_res_partner_with_admin_by_rpc(self):
        with self.assertRaises(UserError):
            with MockRequest(self.env):
                DiscussControllerLock.mail_attachment_delete(self, self.attachment_res_partner.id)
                
    @users('demo')
    def test_delete_attachment_res_partner_with_user_by_rpc(self):
        with self.assertRaises(UserError):
            with MockRequest(self.env):
                DiscussControllerLock.mail_attachment_delete(self, self.attachment_res_partner.id)
