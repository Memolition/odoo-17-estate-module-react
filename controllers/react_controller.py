# -*- coding: utf-8 -*-
from odoo import http

class ReactController(http.Controller):
    @http.route('/estate/todo', auth='public')
    def index(self, **kw):
        print('>>>>==============================')
        return http.request.render('estate.index')
