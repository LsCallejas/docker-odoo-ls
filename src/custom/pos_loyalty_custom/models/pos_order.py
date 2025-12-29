from odoo import models, fields, api


class PosOrder(models.Model):
    """Extensión de órdenes POS para programa de fidelización."""
    _inherit = 'pos.order'

    points_won = fields.Float(
        string='Puntos Ganados',
        readonly=True,
        help='Puntos de fidelización ganados con esta orden.'
    )

    @api.model
    def create(self, vals):
        """Sobrescribe create para calcular puntos al crear la orden."""
        order = super(PosOrder, self).create(vals)
        self._calculate_loyalty_points(order)
        return order

    def _calculate_loyalty_points(self, order):
        """Calcula y asigna puntos de fidelización al cliente."""
        if not order.partner_id:
            return
        
        config = order.session_id.config_id
        if not config.enable_loyalty:
            return
        
        step_amount = config.loyalty_step_amount
        points_qty = config.loyalty_points_qty

        if step_amount <= 0 or order.amount_total <= 0:
            return

        # División entera para bloques completos
        total_points = (order.amount_total // step_amount) * points_qty

        if total_points > 0:
            order.write({'points_won': total_points})
            new_total = order.partner_id.loyalty_points + total_points
            order.partner_id.write({'loyalty_points': new_total})


class PosSession(models.Model):
    """Extensión de sesiones POS para mostrar resumen de puntos."""
    _inherit = 'pos.session'

    total_loyalty_points = fields.Float(
        string='Total Puntos Entregados',
        compute='_compute_total_loyalty_points',
        store=True,
        help='Total de puntos otorgados en esta sesión.'
    )

    @api.depends('order_ids.points_won')
    def _compute_total_loyalty_points(self):
        for session in self:
            session.total_loyalty_points = sum(session.order_ids.mapped('points_won'))
