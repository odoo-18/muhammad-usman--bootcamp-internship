{
    'name': 'FSZ Sale Report Override',
    'version': '1.0',
    'depends': ['sale'],
    'category': 'Sales',
    'description': 'Override Sale Order Report',
    'data': [
        'views/sale_report_template.xml',
        'report/sale_report.xml',
    ],
'assets': {
    'web.report_assets_common': [
        'fsz_sale_report_override/static/src/css/sale_report.css',
    ],
    'web.report_assets_pdf': [
        'fsz_sale_report_override/static/src/css/sale_report.css',
    ],
},
    'installable': True,
    'application': True,
}
