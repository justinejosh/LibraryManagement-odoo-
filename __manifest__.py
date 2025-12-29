{
    'name': 'Library Management System',
    'category': 'Services',
    'description': """
    Library Management System
    """,
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/library_book_views.xml',
        'views/library_management_menus.xml',
    ],
    'installable': True,
    'application': True,

}