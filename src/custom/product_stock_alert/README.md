# Stock Critical Alerts

Módulo de Odoo 17 para alertas automáticas de stock crítico.

## Funcionalidades

- Campo "Stock Mínimo" en productos almacenables
- Acción automática (cron) que verifica el stock cada hora
- Notificaciones en el chatter cuando el stock cae por debajo del mínimo
- Tablero de productos críticos agrupados por categoría
- Prevención de alertas duplicadas

## Instalación

1. Copiar a la carpeta de addons
2. Actualizar lista de apps
3. Instalar "Stock Critical Alerts"

## Uso

1. Ir a Inventario → Productos
2. Configurar "Stock Mínimo" en cada producto almacenable
3. Ver productos críticos en: Inventario → Control de Inventario → Stock Crítico
4. Las alertas aparecen automáticamente en el historial del producto

## Ejecutar cron manualmente

```bash
docker exec proj odoo shell -d DB_NAME --no-http << EOF
env['product.template']._cron_check_critical_stock()
EOF
```

## Tests

```bash
docker exec proj odoo -d DB_NAME --test-enable --stop-after-init -i product_stock_alert
```
