{
    'name': 'Diagnosis',
    'version': '14.0.1.0.0',
    'summary': 'General modification for diagnosis',
    'author': 'Atrivia SRL',
    'license': 'LGPL-3',
    'depends': [
        'account',
        'base_external_dbsource_tds',
        'import_odbc',
        'l10n_do_check',
        'l10n_do_check_printing',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/referrer_views.xml',
        'views/account_move.xml',
        'views/product_views.xml',
        'views/res_partner_views.xml',
        'views/account_payment_view.xml',
        'views/res_config_settings.xml',
        'views/check_report_config.xml',
        'data/base_external_dbsource_data.xml',
        'data/ir_action_server_data.xml',
        'data/import_odbc_dbtable_data.xml',
        'data/papper_format_data.xml',
        'reports/report_insurance_invoice.xml',
        'reports/custom_report.xml'
    ],
    'application': True,
}