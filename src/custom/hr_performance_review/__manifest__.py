{
    'name': 'Evaluaciones de Desempeño Binaural',
    'version': '17.0.1.0.0',
    'author': 'LsCallejas',
    'depends': ['hr', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_performance_views.xml', 
        'reports/ir_actions_report.xml',  
        'reports/performance_report_template.xml', 
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}