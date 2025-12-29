from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestPosLoyalty(TransactionCase):
    """Pruebas unitarias para el módulo de fidelización POS."""

    @classmethod
    def setUpClass(cls):
        """Configuración inicial para las pruebas."""
        super().setUpClass()
        
        # Crear un cliente de prueba
        cls.partner = cls.env['res.partner'].create({
            'name': 'Cliente de Prueba',
            'email': 'test@example.com',
        })
        
        # Obtener la configuración del POS
        cls.pos_config = cls.env['pos.config'].search([], limit=1)
        if not cls.pos_config:
            cls.pos_config = cls.env['pos.config'].create({
                'name': 'POS de Prueba',
            })
        
        # Configurar fidelización: 1 punto por cada $10
        cls.pos_config.write({
            'enable_loyalty': True,
            'loyalty_step_amount': 10.0,
            'loyalty_points_qty': 1.0,
        })
        
        # Crear una sesión del POS
        cls.pos_session = cls.env['pos.session'].create({
            'config_id': cls.pos_config.id,
        })

    def test_01_loyalty_points_calculation(self):
        """
        Prueba: Verificar que los puntos se calculan correctamente.
        $25 gastados con paso de $10 = 2 puntos (25 // 10 = 2)
        """
        # Puntos iniciales del cliente
        initial_points = self.partner.loyalty_points
        
        # Crear una orden de $25
        order = self.env['pos.order'].create({
            'session_id': self.pos_session.id,
            'partner_id': self.partner.id,
            'amount_total': 25.0,
            'amount_tax': 0.0,
            'amount_paid': 25.0,
            'amount_return': 0.0,
        })
        
        # Verificar que la orden tiene 2 puntos (25 // 10 = 2)
        self.assertEqual(order.points_won, 2.0, 
            "La orden debería tener 2 puntos (25 // 10 = 2)")
        
        # Verificar que el cliente acumuló los puntos
        self.assertEqual(self.partner.loyalty_points, initial_points + 2.0,
            "El cliente debería tener 2 puntos más")

    def test_02_different_configuration(self):
        """
        Prueba: Verificar funcionamiento con diferente configuración.
        Configuración: 2 puntos por cada $5
        $15 gastados = 6 puntos (15 // 5 = 3 bloques * 2 puntos)
        """
        # Cambiar configuración: 2 puntos por cada $5
        self.pos_config.write({
            'loyalty_step_amount': 5.0,
            'loyalty_points_qty': 2.0,
        })
        
        initial_points = self.partner.loyalty_points
        
        # Crear una orden de $15
        order = self.env['pos.order'].create({
            'session_id': self.pos_session.id,
            'partner_id': self.partner.id,
            'amount_total': 15.0,
            'amount_tax': 0.0,
            'amount_paid': 15.0,
            'amount_return': 0.0,
        })
        
        # Verificar: (15 // 5) * 2 = 6 puntos
        self.assertEqual(order.points_won, 6.0,
            "La orden debería tener 6 puntos ((15 // 5) * 2)")
        
        self.assertEqual(self.partner.loyalty_points, initial_points + 6.0,
            "El cliente debería tener 6 puntos más")

    def test_03_no_partner_no_points(self):
        """
        Prueba: Sin cliente asignado no se deben otorgar puntos.
        """
        # Restaurar configuración original
        self.pos_config.write({
            'loyalty_step_amount': 10.0,
            'loyalty_points_qty': 1.0,
        })
        
        # Crear orden SIN cliente
        order = self.env['pos.order'].create({
            'session_id': self.pos_session.id,
            'partner_id': False,
            'amount_total': 100.0,
            'amount_tax': 0.0,
            'amount_paid': 100.0,
            'amount_return': 0.0,
        })
        
        # Verificar que no se asignaron puntos
        self.assertEqual(order.points_won, 0.0,
            "Sin cliente, no debería haber puntos")

    def test_04_loyalty_disabled(self):
        """
        Prueba: Con fidelización desactivada no se otorgan puntos.
        """
        # Desactivar fidelización
        self.pos_config.enable_loyalty = False
        
        # Crear un nuevo cliente para esta prueba
        new_partner = self.env['res.partner'].create({
            'name': 'Cliente Sin Puntos',
        })
        initial_points = new_partner.loyalty_points
        
        # Crear orden con cliente
        order = self.env['pos.order'].create({
            'session_id': self.pos_session.id,
            'partner_id': new_partner.id,
            'amount_total': 100.0,
            'amount_tax': 0.0,
            'amount_paid': 100.0,
            'amount_return': 0.0,
        })
        
        # Verificar que no se asignaron puntos
        self.assertEqual(order.points_won, 0.0,
            "Con fidelización desactivada, no debería haber puntos")
        self.assertEqual(new_partner.loyalty_points, initial_points,
            "El cliente no debería tener puntos nuevos")
        
        # Reactivar para otras pruebas
        self.pos_config.enable_loyalty = True
        
    def test_05_session_total_points(self):
            """
            Prueba: Verificar que pos.session suma correctamente los puntos totales.
            CORRECCIÓN: Creamos una config nueva para evitar el error "Session already opened".
            """
            # 1. Crear una CONFIGURACIÓN DE POS NUEVA y EXCLUSIVA para este test
            test_config = self.env['pos.config'].create({
                'name': 'POS Test Session Total',
                'enable_loyalty': True,
                'loyalty_step_amount': 10.0,
                'loyalty_points_qty': 1.0,
            })
            
            # 2. Crear la sesión usando esa NUEVA configuración
            new_session = self.env['pos.session'].create({
                'config_id': test_config.id,
                'user_id': self.env.uid,
            })
            
            new_partner = self.env['res.partner'].create({
                'name': 'Cliente Sesión',
            })
            
            # 3. Crear 3 órdenes de $10 cada una (1 punto cada una)
            for i in range(3):
                self.env['pos.order'].create({
                    'session_id': new_session.id,
                    'partner_id': new_partner.id,
                    'amount_total': 10.0,
                    'amount_tax': 0.0,
                    'amount_paid': 10.0,
                    'amount_return': 0.0,
                })
            
            # 4. Verificar que la sesión muestra 3 puntos totales
            # Forzamos el recomputo si es necesario
            new_session._compute_total_loyalty_points()
            
            self.assertEqual(new_session.total_loyalty_points, 3.0,
                "La sesión debería mostrar 3 puntos totales")

    def test_06_loyalty_step_amount_validation(self):
        """
        Prueba: El monto por punto debe ser mayor a 0 cuando fidelización está activa.
        """
        with self.assertRaises(ValidationError):
            self.env['pos.config'].create({
                'name': 'POS Inválido',
                'enable_loyalty': True,
                'loyalty_step_amount': 0,  # Inválido
                'loyalty_points_qty': 1.0,
            })

    def test_07_loyalty_points_qty_validation(self):
        """
        Prueba: Los puntos otorgados deben ser mayor a 0 cuando fidelización está activa.
        """
        with self.assertRaises(ValidationError):
            self.env['pos.config'].create({
                'name': 'POS Inválido 2',
                'enable_loyalty': True,
                'loyalty_step_amount': 10.0,
                'loyalty_points_qty': 0,  # Inválido
            })