{
    'name': 'Validador Edad Odoo',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Valida edad mínima de 13 años al registrar usuario.',
    'description': 'Bloquea el registro de usuarios menores de 13 años por políticas de privacidad.',
    'author': 'Equipo Sprint',
    'depends': ['base'],
    'data': [
        'views/user_view.xml',
    ],
    'installable': True,
    'auto_install': False,
}
