from odoo import http
from odoo.http import request


class Main(http.Controller):
    @http.route('/course', type='http', auth='user', website=True)
    def course(self):
        return request.render(
            'education.course', {
                'courses': request.env['course'].search([])
            }
        )

    @http.route('/course/<model("course"):course>', type='http', auth='user', website=True)
    def course_detail(self, course):
        return request.render(
            'education.course_detail', {
                'courses': course
            }
        )
