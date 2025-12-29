# POS Loyalty Program

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Tests](https://img.shields.io/badge/Tests-9%20passing-brightgreen)

## 📋 Descripción

Módulo de Odoo 17 que implementa un **sistema de puntos de fidelización** para el Punto de Venta (POS). Permite recompensar a los clientes con puntos por cada compra, incentivando la recurrencia.

---

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| Puntos en clientes | Campo `loyalty_points` en contactos |
| Configuración flexible | Monto por punto y cantidad configurable por POS |
| Acumulación automática | Puntos se suman al registrar ventas |
| Resumen por sesión | Total de puntos entregados en cada sesión |
| Historial | Botón para ver historial de puntos del cliente |
| Validaciones | Monto y puntos deben ser mayor a 0 |

---

## 🛠️ Instalación

### Requisitos
- Odoo 17.0
- Módulo `point_of_sale` instalado

### Pasos

1. Copiar la carpeta `pos_loyalty_custom` a `addons/`
2. Actualizar lista de aplicaciones en Odoo
3. Buscar "POS Loyalty" e instalar

---

## ⚙️ Configuración

### Habilitar fidelización

1. Ve a **Punto de Venta** → **Configuración**
2. Selecciona tu POS
3. En **Programa de Fidelización**, configura:

| Campo | Descripción |
|-------|-------------|
| Activar Fidelización | Habilita el programa |
| Monto por Punto | Cuánto debe gastar para ganar puntos (ej: $10) |
| Puntos Otorgados | Cuántos puntos recibe (ej: 1) |

---

## 📖 Uso

### Acumular puntos

1. Abre el POS y selecciona un **cliente**
2. Agrega productos y completa la venta
3. Los puntos se calculan automáticamente

**Fórmula:** `puntos = (total ÷ monto_por_punto) × puntos_otorgados`

### Ver puntos del cliente

1. Ve a **Contactos**
2. Abre un cliente
3. En **Ventas y Compras** → **Puntos de Fidelización**

### Ver historial

1. En el formulario del cliente
2. Clic en **Ver Historial de Puntos**

---

## 🧪 Pruebas

Ejecutar tests:
```bash
docker exec -u odoo proj odoo -d demo_limpia -u pos_loyalty_custom --test-enable --stop-after-init --no-http
```

### Tests incluidos

| Test | Descripción |
|------|-------------|
| test_loyalty_points_calculation | Cálculo correcto de puntos |
| test_different_configuration | Diferentes configuraciones |
| test_no_partner_no_points | Sin cliente no hay puntos |
| test_loyalty_disabled | Programa desactivado no da puntos |
| test_session_total_points | Total por sesión correcto |
| test_step_amount_validation | Monto debe ser > 0 |
| test_points_qty_validation | Puntos deben ser > 0 |

---

## 📁 Estructura

```
pos_loyalty_custom/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── pos_config.py
│   ├── pos_order.py
│   └── res_partner.py
├── views/
│   ├── pos_config_views.xml
│   └── res_partner_views.xml
├── report/
│   └── pos_session_loyalty_report.xml
├── security/
│   └── ir.model.access.csv
└── tests/
    ├── __init__.py
    └── test_loyalty.py
```

---

## 📝 Autor

**Leidy Callejas**

## 📄 Licencia

LGPL-3
