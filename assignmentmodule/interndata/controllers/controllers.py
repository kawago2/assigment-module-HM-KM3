# -*- coding: utf-8 -*-
# from odoo import http


# class Interndata(http.Controller):
#     @http.route('/interndata/interndata', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/interndata/interndata/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('interndata.listing', {
#             'root': '/interndata/interndata',
#             'objects': http.request.env['interndata.interndata'].search([]),
#         })

#     @http.route('/interndata/interndata/objects/<model("interndata.interndata"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('interndata.object', {
#             'object': obj
#         })
