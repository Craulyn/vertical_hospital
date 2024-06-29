{
    'name': 'Vertical Hospital',
    'version': '1.0',
    'summary': 'Módulo para la gestión de pacientes y tratamientos en un hospital',
    'description': '',
    'category': 'Healthcare',
    'author': 'Craulyn Feliz',
    'website': '',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient.xml',
        'views/hospital_treatment.xml',
        'reports/patient_report.xml',
        'views/res_config_setting.xml',
        'data/ir_sequence.xml',
        'views/menu.xml'
    ],
    # 'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}