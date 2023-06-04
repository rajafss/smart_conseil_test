# -*- coding: utf-8 -*-
# from odoo import http


# class TechnicalInterview(http.Controller):
#     @http.route('/technical_interview/technical_interview/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/technical_interview/technical_interview/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('technical_interview.listing', {
#             'root': '/technical_interview/technical_interview',
#             'objects': http.request.env['technical_interview.technical_interview'].search([]),
#         })

#     @http.route('/technical_interview/technical_interview/objects/<model("technical_interview.technical_interview"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('technical_interview.object', {
#             'object': obj
#         })
