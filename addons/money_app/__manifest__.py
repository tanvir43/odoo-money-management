{
    'name': 'Money App',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Manage your income and expense with ease',
    'description': """
        NA
    """,
    'author': "Tanvir",
    'website': 'https://matacentric.info',
    'license': 'LGPL-3',
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/money_entry_views.xml',
        'views/balance_template.xml',
    ],
    'installation': True,
    'application': True,
    'auto_install': False,
    'maintainers': ['Tanvir'],
}