from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError
from odoo import fields

class TestPerformance(TransactionCase):
    
    def setUp(self):
        super(TestPerformance, self).setUp()
        # 1. Usuario que representa al empleado (Sin permisos de RRHH)
        self.user_emp = self.env['res.users'].create({
            'name': 'Empleado Test',
            'login': 'emp_test_user',
            'email': 'emp@test.com',
            'groups_id': [(4, self.env.ref('base.group_user').id)],
        })
        
        # 2. Usuario que representa al evaluador (Con permisos de RRHH)
        self.user_hr = self.env['res.users'].create({
            'name': 'Evaluador RRHH',
            'login': 'hr_test_user',
            'email': 'hr_test@test.com',
            'groups_id': [(4, self.env.ref('hr.group_hr_user').id)],
        })

        # 3. Creamos el registro de empleado vinculado a su usuario
        self.employee = self.env['hr.employee'].create({
            'name': 'Test Employee',
            'user_id': self.user_emp.id,
        })

    def test_performance_full_flow(self):
        """Prueba creación exitosa: Empleado es evaluado por alguien de RRHH"""
        review = self.env['hr.performance.review'].create({
            'employee_id': self.employee.id,
            'review_date': fields.Date.today(),
            'score': 8.5,
        })
        self.assertEqual(review.state, 'pending')
        review.action_complete()
        self.assertEqual(review.state, 'completed')

    def test_03_self_evaluation_denied(self):
        """Prueba de Seguridad: El empleado intenta evaluarse a sí mismo (Debe fallar)"""
        with self.assertRaises(ValidationError):
            self.env['hr.performance.review'].create({
                'employee_id': self.employee.id,
                'reviewer_id': self.user_emp.id, 
                'review_date': fields.Date.today(),
                'score': 7.0,
            })

    def test_04_reviewer_permission_check(self):
        """Prueba de Seguridad: Un usuario sin RRHH intenta evaluar (Debe fallar)"""
        #usuario sin permisos
        regular_user = self.env['res.users'].create({
            'name': 'Cualquiera',
            'login': 'regular_guy',
            'groups_id': [(4, self.env.ref('base.group_user').id)],
        })

        with self.assertRaises(ValidationError):
            self.env['hr.performance.review'].create({
                'employee_id': self.employee.id,
                'reviewer_id': regular_user.id,
                'review_date': fields.Date.today(),
                'score': 7.0,
            })