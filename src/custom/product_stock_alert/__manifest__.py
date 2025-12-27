{
    'name': 'Stock Critical Alerts',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Alertas de stock crítico para productos',
    'author': 'Luis Callejas',
    'license': 'LGPL-3',
    'depends': ['stock', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
