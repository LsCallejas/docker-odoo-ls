{
    'name': 'POS Loyalty Program',
    'version': '17.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Sistema de puntos de fidelización para clientes en POS',
    'description': """
        Módulo de Programa de Fidelización para Punto de Venta
        =======================================================
        
        Este módulo implementa un sistema de puntos de fidelización personalizado
        para el Punto de Venta (POS) de Odoo.
        
        Características:
        ----------------
        * Campo "puntos acumulados" en clientes (res.partner)
        * Configuración flexible de puntos por monto gastado
        * Acumulación automática de puntos al registrar ventas
        * Vista resumen de puntos en sesiones POS
        * Historial de puntos por cliente
    """,
    'author': 'Luis Callejas',
    'license': 'LGPL-3',
    'depends': ['base', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/pos_config_views.xml',
        'report/pos_session_loyalty_report.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
