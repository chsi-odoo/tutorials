{
    'name': "Estate",
    'version': '0.0.1',
    'depends': ['base'],
    'author': "Me",
    'application': True,
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'report/estate_property_templates.xml',
        'report/estate_property_reports.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',
        "views/res_user_views.xml",
        'data/estate.property.type.csv',
        'data/estate.property.csv',
        'data/estate_property_offer.xml',
        'data/estate_property.xml',
    ],
    # # data files containing optionally loaded demonstration data
    'demo': [
    ],
}
