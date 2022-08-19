from odoo.tests.common import tagged

from .common import Common


@tagged('post_install', '-at_install')
class TestWriteUnlinkMailMessage(Common):
    
    def test_delete_record_res_partner_with_admin(self):
        self.res_partner.with_user(self.user_admin).unlink()
        
    def test_delete_record_res_partner_with_user(self):
        self.res_partner.with_user(self.user_demo).unlink()
