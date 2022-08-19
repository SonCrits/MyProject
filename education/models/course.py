from odoo import fields, models


class Course(models.Model):
    _name = 'course'
    description = 'Course'
    
    name = fields.Char(string='Name', required=True)
    number_of_lesson = fields.Integer(string='Number Of Lesson', help='Number of lesson in this course')
    level_of_course = fields.Selection(
        selection=[
            ('beginner', 'Beginner'),
            ('intermediate', 'Intermediate'),
            ('professional', 'Professional')
        ],
        string='Level Of Course',
        default='beginner'
    )
    type_of_course = fields.Selection(
        selection=[
            ('course', 'Course'),
            ('career', 'Career')
        ],
        string='Type Of Course',
        default='course'
    )
    image = fields.Binary(string='Image', attachment=True)
    html_description = fields.Html(string='Description')
