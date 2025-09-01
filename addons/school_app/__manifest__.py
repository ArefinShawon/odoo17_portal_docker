# -*- coding: utf-8 -*-
{
    'name': 'School',
    'version': '1.0',
    'category': 'Uncategorized',
    'summary': 'School Module',
    'description': '''School Module''',
    'author': 'Shawon',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
		'views/student_template.xml',
],
    'installable': True,
    'application': False,
    'auto_install': False,
}
