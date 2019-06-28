# -*- coding: utf-8 -*-
from odoo import http

# class RutModule(http.Controller):
#     @http.route('/rut_module/rut_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rut_module/rut_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rut_module.listing', {
#             'root': '/rut_module/rut_module',
#             'objects': http.request.env['rut_module.rut_module'].search([]),
#         })

#     @http.route('/rut_module/rut_module/objects/<model("rut_module.rut_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rut_module.object', {
#             'object': obj
#         })