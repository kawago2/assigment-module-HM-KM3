# -*- coding: utf-8 -*-
{
    'name': "interndata",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'wizard/inputmahasiswa_view_wizard.xml',
        'report/report.xml',
        'report/print_sr_mahasiswa.xml',
        'views/program_view.xml',
        'views/mahasiswa_view.xml',
        'views/perusahaan_view.xml',
        'views/karyawan_view.xml',
        'views/universitas_view.xml',


    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
