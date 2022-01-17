# -*- coding: utf-8 -*-
from odoo import http


class Specprice(http.Controller):
    @http.route('/specprice/specprice', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/specprice/specprice/objects', auth='public')
    def list(self, **kw):
        return http.request.render('specprice.listing', {
            'root': '/specprice/specprice',
            'objects': http.request.env['specprice.specprice'].search([]),
        })

    @http.route('/specprice/specprice/objects/<model("specprice.specprice"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('specprice.object', {
            'object': obj
        })
