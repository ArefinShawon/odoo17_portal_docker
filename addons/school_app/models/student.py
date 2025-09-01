from odoo import fields, models, api


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char()
    class_name = fields.Char()
    admission_date = fields.Date()