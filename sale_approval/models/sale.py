# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools import float_is_zero, float_compare, DEFAULT_SERVER_DATETIME_FORMAT

class SaleOrder(models.Model):
    _inherit = "sale.order"
     
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('pendint', 'Pendiente'),
        ('approve', 'Aprobado'),
        ('sent', 'Quotation Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
    approver_id = fields.Many2one('res.users', 'Sale Order Approver', readonly=True, copy=False, track_visibility='onchange', default=lambda self: self.env.user)
    
    #@api.multi
    def action_confirm_2(self):
        user_obj = self.env.user
        for sale_order in self:
            if user_obj.sale_order_can_approve == 'no':
                raise UserError(_('No tiene permisos para confirmar este presupuesto, contacte a su administrador.'))
            #if not sale_order.approver_id == self.env.user: 
             #   user_search = user_obj.search([('sale_order_can_approve', '=', 'no')])
              #  if not user_search:
               #     raise UserError(_('No tiene permisos para confirmar este presupuesto, contacte a su administrador.'))
        return self.write({'state': 'approve'})

    #@api.multi
    def print_quotation(self):
        self.filtered(lambda s: s.state == 'draft').write({'state': 'sent'})

        return self.env.ref('sale.action_report_saleorder')\
            .with_context(discard_logo_check=True).report_action(self)

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        user_obj = self.env.user
        if user_obj.sale_order_can_approve == 'no':
            raise UserError(_('No tiene permisos para confirmar esta factura, contacte a su administrador.'))
        if self.mapped('line_ids.payment_id') and any(post_at == 'bank_rec' for post_at in self.mapped('journal_id.post_at')):
            raise UserError(_("A payment journal entry generated in a journal configured to post entries only when payments are reconciled with a bank statement cannot be manually posted. Those will be posted automatically after performing the bank reconciliation."))
        return self.post()