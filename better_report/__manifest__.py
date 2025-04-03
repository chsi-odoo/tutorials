{
    'name': 'Better Reports',
    'version': '0.0.1',
    'depends': ['portal', 'account'],
    'data': [
        'report/portal_reports.xml',
        'report/portal_templates.xml',
        'report/invoice_templates.xml',
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            'better_report/static/src/css/better_report_styles.scss',
        ],
    }
}
