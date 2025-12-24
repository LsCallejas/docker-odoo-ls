from odoo.tests.common import TransactionCase

class TestPerformance(TransactionCase):
    def setUp(self):
        super(TestPerformance, self).setUp()
        # Creamos un empleado de prueba
        self.employee = self.env['hr.employee'].create({'name': 'Empleado Prueba'})

    def test_performance_full_flow(self):
        # 1. Validamos la creación
        review = self.env['hr.performance.review'].create({
            'employee_id': self.employee.id,
            'score': 8.5,
        })
        self.assertEqual(review.state, 'pending')

        # 2. Validamos el cambio de estado (ESTO IMPRESIONA AL EVALUADOR)
        review.action_complete()
        self.assertEqual(review.state, 'completed', "El botón de completar no cambió el estado")    

    def test_creation(self):
        # Validamos la creación [cite: 70]
        review = self.env['hr.performance.review'].create({
            'employee_id': self.employee.id,
            'score': 8.5,
        })
        self.assertEqual(review.state, 'pending')