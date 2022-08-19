{
    'name': "education website",
    'name_vi_VN': "Trang trình duyệt trường học",

    'summary': """
Learning CMS website developer""",
    'summary_vi_VN': """
Học CMS sáng tạo website""",

    'description': """
Key Features
============
* pass

Supported Editions
==================
1. Community Edition
2. Enterprise Edition

    """,
    'description_vi_VN': """

Tính năng nổi bật
=================
* cho qua

Ấn bản được hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Son-viindoo",
    'live_test_url': "https://v14demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v14demo-vn.viindoo.com",
    'website': "https://viindoo.com/intro/accounting",
    'support': "apps.support@viindoo.com",
    'category': 'Hidden',
    'version' : '0.1.0',
    'depends': ['website'],
    'data': [
           'security/ir.model.access.csv',
           'views/course_template.xml',
           'views/course_views.xml',
           'views/s_course_lessons.xml',
           'views/snippets.xml',
           'views/s_course_carousel.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'education/static/src/css/education_style.css',
            'education/static/src/scss/education_style.scss',
            'education/static/src/js/education.js',
            'education//static/src/js/snippets.js'
        ]
    },
    'installable': True,
    'application': False,
    'auto_install': False, # set this as True after upgrading for Odoo 15,
    'price': 9.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
