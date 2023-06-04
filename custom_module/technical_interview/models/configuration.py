# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Publication(models.Model):
    _name = 'postes.vises'
    _description = 'postes visés'

    name = fields.Char()
    website = fields.Char()
    active = fields.Boolean()


