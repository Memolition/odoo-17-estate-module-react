# -*- coding: utf-8 -*-

{
    'name': 'Estate',
    'author': 'Moh Mejia',
    'version': '0.1',
    'depends': [
        'base',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/react_template.xml',
    ],
    'assets': {
        ####################################################
        ##      Javascript files to build React app       ##
        ####################################################
        #'estate.assets': [
        'web.assets_frontend': [
            'estate/static/src/react/index.js',
            'estate/static/src/react/components/*.js',
            'estate/static/src/react/index.css',
            'estate/static/src/react/components/*.css'
        ]
    },
}
