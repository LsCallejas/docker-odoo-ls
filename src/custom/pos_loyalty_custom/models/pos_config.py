from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PosConfig(models.Model):
    """Configuración del programa de fidelización en POS."""
    _inherit = 'pos.config'

    enable_loyalty = fields.Boolean(
        string='Activar Programa de Fidelización',
        help='Habilita la acumulación de puntos para clientes.'
    )

    loyalty_step_amount = fields.Float(
        string='Monto por Punto',
        default=10.0,
        help='Monto que el cliente debe gastar para ganar puntos.'
    )

    loyalty_points_qty = fields.Float(
        string='Puntos Otorgados',
        default=1.0,
        help='Cantidad de puntos a otorgar por cada monto cumplido.'
    )

    @api.constrains('enable_loyalty', 'loyalty_step_amount', 'loyalty_points_qty')
    def _check_loyalty_config(self):
        for record in self:
            if record.enable_loyalty:
                if record.loyalty_step_amount <= 0:
                    raise ValidationError(
                        "El 'Monto por Punto' debe ser mayor a 0 "
                        "cuando el programa de fidelización está activo."
                    )
                if record.loyalty_points_qty <= 0:
                    raise ValidationError(
                        "Los 'Puntos Otorgados' deben ser mayor a 0 "
                        "cuando el programa de fidelización está activo."
                    )
