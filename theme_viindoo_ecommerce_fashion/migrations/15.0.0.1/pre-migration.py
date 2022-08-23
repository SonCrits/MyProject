from odoo import api, SUPERUSER_ID


def change_menu_name(env):
    shop_menu = env["website.menu"].search([('url', '=', '/shop')])
    shop_menu.write({
        'name': 'Ecommerce'
    })
    
def migarate(cr, installed_version):
    env = api.Environment(cr, SUPERUSER_ID, {})
    change_menu_name(env)
