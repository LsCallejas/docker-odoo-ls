{
    'name': 'Evaluaciones de Desempeño',
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Gestión de evaluaciones periódicas de empleados',
    'description': """
        Módulo de Evaluaciones de Desempeño
        ====================================
        
        Este módulo permite gestionar evaluaciones periódicas de los empleados
        con un flujo de trabajo completo.
        
        Características:
        ----------------
        * Evaluaciones con puntaje, fortalezas y debilidades
        * Vista Kanban para seguimiento por estado
        * Validaciones de seguridad (puntaje 0-10, evaluador RRHH)
        * Reporte PDF con historial por empleado
        * Seguimiento de cambios con chatter
    """,
    'author': 'Luis Callejas',
    'license': 'LGPL-3',
    'depends': ['base', 'hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_performance_views.xml', 
        'reports/ir_actions_report.xml',  
        'reports/performance_report_template.xml', 
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}