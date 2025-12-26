{
    'name': 'Evaluaciones de Desempeño Binaural',
    'version': '17.0.1.0.0',
    'author': 'LsCallejas',
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
    'license': 'LGPL-3',
}