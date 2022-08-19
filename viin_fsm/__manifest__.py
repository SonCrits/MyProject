{
    'name': "Field Service Manager",
    'name_vi_VN': "Dịch vụ hiện trường",

    'summary': """
Field management service support
""",

    'summary_vi_VN': """
Quản lý dịch vụ hỗ trợ hiện trường
""",

    'description': """
What it does
============
Manage field support services, improve customer experience, management, employees

Key Features
============

Editions Supported
==================
1. Community Edition
2. Enterprise Edition
    """,

    'description_vi_VN': """
Ứng dụng này làm gì
===================
Quản lý dịch vụ hỗ trợ hiện trường, cải thiện trải nghiệm khách hàng, quản lý, nhân viên

Tính năng chính
===============

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise
    """,

    'author': "Viindoo",
    'website': "https://viindoo.com",
    'live_test_url': "https://v15demo-int.viindoo.com",
    'live_test_url_vi_VN': "https://v15demo-vn.viindoo.com",
    'support': "apps.support@viindoo.com",

    'category': 'Project/FSM',
    'version': '0.1.1',
    'depends': ['project','to_account_budget', 'hr_contract','to_hr_payroll_account'],
    'data': [
        'security/ir.model.access.csv',
        'views/project_views.xml'
    ],
    'images' : [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'price': 99.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
