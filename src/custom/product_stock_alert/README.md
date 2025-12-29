# Alertas de Stock Crítico

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Tests](https://img.shields.io/badge/Tests-8%20passing-brightgreen)

## 📋 Descripción

Módulo de Odoo 17 para **generar alertas automáticas** cuando el stock de un producto cae por debajo de un umbral configurable. Ayuda a evitar quiebres de stock y mejorar la gestión de inventario.

---

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| Campo Stock Mínimo | Umbral configurable por producto |
| Alertas automáticas | Notificaciones en el chatter del producto |
| Tablero de críticos | Vista con productos en estado crítico |
| Agrupación | Productos agrupados por categoría |
| Sin duplicados | Control para evitar alertas repetidas |
| Validación | Stock mínimo no puede ser negativo |

---

## 🛠️ Instalación

### Requisitos
- Odoo 17.0
- Módulos `stock` y `mail` instalados

### Pasos

1. Copiar la carpeta `product_stock_alert` a `addons/`
2. Actualizar lista de aplicaciones en Odoo
3. Buscar "Stock Critical" e instalar

---

## ⚙️ Uso

### Configurar stock mínimo

1. Ve a **Inventario** → **Productos**
2. Abre un producto (tipo Almacenable)
3. Configura el campo **Stock Mínimo**
4. Guarda

### Ver productos críticos

1. Ve a **Inventario** → **Control de Inventario** → **Stock Crítico**
2. Los productos se muestran agrupados por categoría

### Cómo funcionan las alertas

- Un cron se ejecuta periódicamente
- Si stock < stock_minimo → se genera alerta en el chatter
- Cuando el stock normaliza → se marca como resuelto

---

## 🧪 Pruebas

Ejecutar tests:
```bash
docker exec -u odoo proj odoo -d demo_limpia -u product_stock_alert --test-enable --stop-after-init --no-http
```

### Tests incluidos

| Test | Descripción |
|------|-------------|
| test_stock_minimo_field | Campo existe y es modificable |
| test_is_critical_stock_computed | Cálculo correcto de estado crítico |
| test_alert_generation | Se genera alerta cuando stock está bajo |
| test_no_duplicate_alerts | No se duplican alertas |
| test_alert_reset | Flag se resetea cuando stock normaliza |
| test_stock_minimo_negative | Stock mínimo no puede ser negativo |

---

## 📁 Estructura

```
product_stock_alert/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── product_template.py
├── views/
│   └── product_template_views.xml
├── data/
│   └── ir_cron_data.xml
├── security/
│   └── ir.model.access.csv
└── tests/
    ├── __init__.py
    └── test_stock_alert.py
```

---

## 📝 Autor

**Leidy Callejas**

## 📄 Licencia

LGPL-3
