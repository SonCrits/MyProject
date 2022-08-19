{
    'name': "Internal Message Edit Lock",
	'name_vi_VN': "Khóa chỉnh sửa ghi chú",
    'summary': """
Avoid author and admin to edit/deleting internal note if the note mentions someone""",
    'summary_vi_VN': """
Tránh để tác giả và quản trị viên chỉnh sửa / xóa ghi chú nội bộ nếu ghi chú đề cập đến ai đó
""",

    'description': """
What it does
============
* This module is used to avoid author and admin to edit/deleting his internal note in any documents and his message in channel if the note/message mentions someone
* On channel, providing the option to enable/disable Prevent editing and deleting messages features

Editions Supported
==================
1. Community Edition
2. Enterprise Edition

    """,
    'description_vi_VN': """
Ứng dụng này làm gì
===================
* Mô-đun này được sử dụng để tránh tác giả và quản trị viên chỉnh sửa/xóa ghi chú nội bộ của họ trong bất kỳ tài liệu nào và tin nhắn của họ trong kênh nếu ghi chú/tin nhắn đề cập đến ai đó
* Trên kênh, cung cấp tùy chọn để bật/tắt tính năng Ngăn chặn chỉnh sửa và xóa các tin nhắn

Ấn bản được Hỗ trợ
==================
1. Ấn bản Community
2. Ấn bản Enterprise

    """,

    'author': "Viindoo",
    'website': "https://viindoo.com/apps/app/15.0/viin_message_edit_lock",
    'live_test_url': "https://v15demo-int.erponline.vn",
    'live_test_url_vi_VN': "https://v15demo-vn.erponline.vn",
    'support': "apps.support@viindoo.com",
    'category': 'Mail',
    'version': '0.1.0',
    'depends': ['mail'],

    # always loaded
    'data': [
        'views/mail_channel_views.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'price': 45.9,
    'currency': 'EUR',
    'license': 'OPL-1',
}
