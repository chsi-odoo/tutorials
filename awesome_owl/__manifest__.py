# -*- coding: utf-8 -*-
{
    'name': "Awesome Owl",

    'summary': """
        Starting module for "Discover the JS framework, chapter 1: Owl components"
    """,

    'description': """
        Starting module for "Discover the JS framework, chapter 1: Owl components"
    """,

    'author': "Odoo",
    'website': "https://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tutorials/AwesomeOwl',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],
    'application': True,
    'installable': True,
    'data': [
        'views/templates.xml',
    ],
    'assets': {
        'awesome_owl.assets_playground': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            'web/static/lib/bootstrap/scss/_maps.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),
            'web/static/src/libs/fontawesome/css/font-awesome.css',
            'awesome_owl/static/src/**/*',

            # 'web/static/src/scss/import_bootstrap.scss',
            # 'web/static/src/scss/utilities_custom.scss',
            # 'web/static/lib/bootstrap/scss/utilities/_api.scss',
            # 'web/static/src/scss/bootstrap_review.scss',
        ],
        # ????
        # 'awesome_owl._assets_bootstrap': [
        #     'web/static/src/scss/import_bootstrap.scss',
        #     'web/static/src/scss/utilities_custom.scss',
        #     'web/static/lib/bootstrap/scss/utilities/_api.scss',
        #     'web/static/src/scss/bootstrap_review.scss',
        # ],
    },
    'license': 'AGPL-3'
}
