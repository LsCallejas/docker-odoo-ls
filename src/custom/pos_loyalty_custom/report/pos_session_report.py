from odoo import models, api


class ReportSaleDetails(models.AbstractModel):
    """
    Extensión del reporte de detalles de venta para agregar puntos de fidelización.
    """
    _inherit = 'report.point_of_sale.report_saledetails'

    @api.model
    def get_sale_details(self, date_start=False, date_stop=False, config_ids=False, session_ids=False):
        """
        Extiende el método original para agregar información de puntos de fidelización.
        """
        # Obtener datos originales del reporte
        data = super().get_sale_details(date_start, date_stop, config_ids, session_ids)
        
        # Calcular puntos de fidelización
        total_loyalty_points = 0
        total_orders = 0
        
        if session_ids:
            sessions = self.env['pos.session'].browse(session_ids)
            total_loyalty_points = sum(sessions.mapped('total_loyalty_points'))
            total_orders = len(sessions.mapped('order_ids'))
        elif config_ids:
            # Si se filtra por configuración y fechas
            domain = [('config_id', 'in', config_ids)]
            if date_start:
                domain.append(('start_at', '>=', date_start))
            if date_stop:
                domain.append(('stop_at', '<=', date_stop))
            sessions = self.env['pos.session'].search(domain)
            total_loyalty_points = sum(sessions.mapped('total_loyalty_points'))
            total_orders = len(sessions.mapped('order_ids'))
        
        # Agregar puntos al diccionario de datos
        data['loyalty_points'] = total_loyalty_points
        data['total_orders'] = total_orders
        
        return data
