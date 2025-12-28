from odoo.tests.common import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestStockAlert(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product = cls.env['product.template'].create({
            'name': 'Test Product',
            'detailed_type': 'product',
            'stock_minimo': 10.0,
        })

    def test_stock_minimo_field(self):
        """El campo stock_minimo debe existir y ser modificable."""
        self.assertEqual(self.product.stock_minimo, 10.0)
        self.product.stock_minimo = 5.0
        self.assertEqual(self.product.stock_minimo, 5.0)

    def test_is_critical_stock_computed(self):
        """El campo is_critical_stock se calcula correctamente."""
        self.product._compute_is_critical_stock()
        # Stock 0 < minimo 10 -> critico
        self.assertTrue(self.product.is_critical_stock)

        self.product.stock_minimo = 0
        self.product._compute_is_critical_stock()
        # Sin minimo configurado -> no critico
        self.assertFalse(self.product.is_critical_stock)

    def test_alert_generation(self):
        """Se genera alerta cuando el stock esta bajo."""
        self.product.alert_sent = False
        messages_before = self.env['mail.message'].search_count([
            ('res_id', '=', self.product.id),
            ('model', '=', 'product.template'),
        ])

        self.env['product.template']._cron_check_critical_stock()

        messages_after = self.env['mail.message'].search_count([
            ('res_id', '=', self.product.id),
            ('model', '=', 'product.template'),
        ])
        self.assertEqual(messages_after - messages_before, 1)
        self.assertTrue(self.product.alert_sent)

    def test_no_duplicate_alerts(self):
        """No se generan alertas duplicadas."""
        self.product.alert_sent = True
        messages_before = self.env['mail.message'].search_count([
            ('res_id', '=', self.product.id),
            ('model', '=', 'product.template'),
        ])

        self.env['product.template']._cron_check_critical_stock()

        messages_after = self.env['mail.message'].search_count([
            ('res_id', '=', self.product.id),
            ('model', '=', 'product.template'),
        ])
        self.assertEqual(messages_after, messages_before)

    def test_alert_reset(self):
        """El flag se resetea cuando el stock vuelve a estar OK."""
        self.product.alert_sent = True
        self.product.stock_minimo = 0  # Ahora stock >= minimo

        self.env['product.template']._cron_check_critical_stock()

        self.assertFalse(self.product.alert_sent)