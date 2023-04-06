# -*- coding: utf-8 -*-
# Copyright 2020-Today TechKhedut.
# Part of TechKhedut. See LICENSE file for full copyright and licensing details.
{
    'name': 'Advanced POS Themes / Responsive POS Theme',
    'description': """
        - 10 Different POS Themes
        - Fully Responsive POS Theme
        - One click installation
        - One click for try different POS Themes
        - Amazing UI/UX POS Update
        - Different types of category in POS
        - POS Themes never like before
        - Modern POS Themes
        - Glassy UI/UX
        - Latest refresh UI
        - Mobile Improved UI
    """,
    'summary': """10 Different amazing POS Theme UI/UX.
    """,
    'category': 'Themes/Point Of Sale',
    'version': '15.0.1.1.1',
    'author': 'TechKhedut Inc.',
    'company': 'TechKhedut Inc.',
    'maintainer': 'TechKhedut Inc.',
    'website': "https://www.techkhedut.com",
    'depends': ['point_of_sale'],
    'images': [
        'static/description/pos-themes-in-odoo-responsive-modern-latest-user-interface-2022.gif',
        'static/description/theme_screenshot.png',
        ],
    'data':[
        'data/data.xml',
        'views/assets.xml',
        'views/theme_view.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'point_of_sale.assets': [
            'tk_pos_themes/static/src/css/theme-1.css',
        ]
    },
    'license': 'OPL-1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'price': 30,
    'currency': 'EUR',
}
