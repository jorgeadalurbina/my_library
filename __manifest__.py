{
    'name': 'My library',
    'version': '1.0',
    'summary': 'Manager Books Easily',
    'description': """modulo de prueba libreria""",
    'category': 'Uncategory',
    'author': 'Jorge Urbina',
    'website': 'www.isumit.odoo.com',
    'depends': ['base'],
    'data': [
             'security/groups.xml',
             'security/ir.model.access.csv',
             'views/library_book.xml',
             'views/library_categoria.xml',
             ],
    'installable': True,
    'application': True,
}
