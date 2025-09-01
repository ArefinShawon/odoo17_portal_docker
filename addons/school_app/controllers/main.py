from odoo import http
from odoo.http import request


class SchoolStudentController(http.Controller):

    @http.route('/students', auth='public', website=True)
    def show_students(self, **kwargs):
        search_term = kwargs.get('search', '')
        domain = []

        if search_term:
            # Search in name and class_name fields
            domain = ['|', ('name', 'ilike', search_term),
                      ('class_name', 'ilike', search_term)]

        student_record = request.env['school.student'].search(domain)

        return request.render('school_app.student_template', {
            'student_record': student_record
        })