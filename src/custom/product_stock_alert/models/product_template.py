from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    stock_minimo = fields.Float("Stock Mínimo", default=0.0)
    alert_sent = fields.Boolean("Alerta Enviada", default=False, copy=False)
    is_critical_stock = fields.Boolean(
        "Stock Crítico",
        compute="_compute_is_critical_stock",
        store=True,
    )

    @api.depends('qty_available', 'stock_minimo')
    def _compute_is_critical_stock(self):
        for rec in self:
            rec.is_critical_stock = (
                rec.detailed_type == 'product'
                and rec.stock_minimo > 0
                and rec.qty_available < rec.stock_minimo
            )

    @api.model
    def _cron_check_critical_stock(self):
        """Verifica productos con stock bajo y envía alertas."""
        products = self.search([
            ('detailed_type', '=', 'product'),
            ('stock_minimo', '>', 0),
            ('alert_sent', '=', False),
        ])
        for prod in products:
            if prod.qty_available < prod.stock_minimo:
                prod.message_post(
                    body=f"⚠️ <b>STOCK CRÍTICO:</b> El producto '{prod.name}' "
                         f"tiene {prod.qty_available} unidades (Mínimo: {prod.stock_minimo}).",
                    message_type='notification',
                    subtype_xmlid='mail.mt_note',
                )
                prod.alert_sent = True

        # Reset cuando el stock vuelve a niveles normales
        for prod in self.search([('alert_sent', '=', True)]):
            if prod.qty_available >= prod.stock_minimo:
                prod.alert_sent = False