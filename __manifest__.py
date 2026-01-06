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
        'views/book_genre.xml',
        'views/book_author.xml',
        'views/library_management_menus.xml',
    ],
    'installable': True,
    'application': True,
    'license':'LGPL-3',
}