# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    typeprice = fields.Many2one(
        'type.price',
        string="Tipo de precio",
        required=True
    )

    valofert = fields.Many2one(
        'val.ofert',
        string="Validez de la oferta",
        required=True
    )

    ftecnica = fields.Boolean(
        string="Ficha Tecnica",
        required=False
    )

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    ftecnica = fields.Char(
        string="Ficha Tecnica",
        required=False
    )


class TypePrice(models.Model):
    _name = 'type.price'

    name = fields.Char(
        string="Nombre",
        requerid=True
    )

class ValOfert(models.Model):
    _name = 'val.ofert'

    name = fields.Char(
        string="Texto",
        requerid=True
    )