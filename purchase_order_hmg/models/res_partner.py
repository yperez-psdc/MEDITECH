
from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    p_cod_id = fields.Char(
        string="Codigo",
        required=True
    )
    p_cod_version = fields.Integer(
        string="Version",
        required=True
    )
    p_cod_date = fields.Date(
        string="Fecha",
        required=True
    )

    fac_cod_id = fields.Char(
        string="Codigo",
        required=True
    )
    fac_cod_version = fields.Integer(
        string="Version",
        required=True
    )
    fac_cod_date = fields.Date(
        string="Fecha",
        required=True
    )

    sale_cod_id = fields.Char(
        string="Codigo",
        required=True
    )
    sale_cod_version = fields.Integer(
        string="Version",
        required=True
    )
    sale_cod_date = fields.Date(
        string="Fecha",
        required=True
    )

    de_cod_id = fields.Char(
        string="Codigo",
        required=True
    )
    de_cod_version = fields.Integer(
        string="Version",
        required=True
    )
    de_cod_date = fields.Date(
        string="Fecha",
        required=True
    )
    