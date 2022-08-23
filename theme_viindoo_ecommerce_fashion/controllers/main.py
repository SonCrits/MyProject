from odoo import http
from odoo.http import request


class Main(http.Controller):
    
    @http('/home', type='http', auth='user', website=True)
    def home(self):
        