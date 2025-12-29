{
    'name': 'Alertas de Stock Crítico',
    'version': '17.0.1.0.0',
    'category': 'Inventory',
    'summary': 'Notificaciones automáticas de productos con stock bajo',
    'description': """
        Módulo de Alertas de Stock Crítico
        ===================================
        
        Este módulo genera alertas automáticas cuando el stock de un producto
        cae por debajo de un umbral configurable.
        
        Características:
        ----------------
        * Campo "Stock Mínimo" en productos
        * Notificaciones automáticas en el chatter del producto
        * Vista de tablero con productos en estado crítico
        * Agrupación por categoría de producto
        * Control de duplicados (una alerta por ciclo)
    """,
    'author': 'Luis Callejas',
    'license': 'LGPL-3',
    'depends': ['stock', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_cron_data.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
