from odoo import models, fields


class ResPartner(models.Model):
    """Extensión de contactos para programa de fidelización."""
    _inherit = 'res.partner'

    loyalty_points = fields.Float(
        string='Puntos de Fidelización',
        default=0.0,
        readonly=True,
        help='Total de puntos acumulados por compras en el POS.'
    )

    def action_view_loyalty_history(self):
        """Abre una vista con el historial de puntos del cliente."""
        self.ensure_one()
        return {
            'name': f'Historial de Puntos - {self.name}',
            'type': 'ir.actions.act_window',
            'res_model': 'pos.order',
            'view_mode': 'tree,form',
            'domain': [('partner_id', '=', self.id), ('points_won', '>', 0)],
            'context': {'default_partner_id': self.id},
        }
