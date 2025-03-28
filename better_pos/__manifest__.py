{
    'name': 'Better POS',
    'version': '0.0.1',
    'depends': ['point_of_sale'],
    'data': [
        'views/pos_config_view.xml',
    ],
    'assets': {
        # 'better_pos.assets_common': [
        #     'better_pos/static/src/*',
        #     'better_pos/static/src/**/*',
        # ],
        'point_of_sale._assets_pos': [
            'better_pos/static/src/*',
            'better_pos/static/src/**/*',
        ]
    }
}