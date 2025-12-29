# Changelog

Todos los cambios notables de este módulo serán documentados en este archivo.

El formato está basado en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/),
y este proyecto adhiere a [Versionado Semántico](https://semver.org/lang/es/).

## [17.0.1.0.0] - 2025-12-28

### Agregado
- **Campo de puntos acumulados** (`loyalty_points`) en el modelo `res.partner`
- **Configuración del programa** en `pos.config`:
  - Activar/desactivar fidelización
  - Monto requerido por puntos
  - Cantidad de puntos a otorgar
- **Acumulación automática** de puntos al crear órdenes en POS
- **Campo `points_won`** en `pos.order` para rastrear puntos por orden
- **Campo computado `total_loyalty_points`** en `pos.session`
- **Botón "Ver Historial de Puntos"** en el formulario de contactos
- **Reporte PDF mejorado** "Detalles de Ventas" con:
  - Diseño moderno y profesional
  - Tarjetas de resumen con colores
  - Sección destacada de puntos de fidelización
  - Compatibilidad total con wkhtmltopdf
- **7 pruebas automatizadas** que cubren:
  - Cálculo básico de puntos
  - Diferentes configuraciones
  - Casos sin cliente
  - Programa desactivado
  - Suma de puntos por sesión
  - Montos menores al paso

### Técnico
- Uso de `@api.model_create_multi` para compatibilidad con creación en lote
- División entera (`//`) para cálculo de bloques de puntos
- Herencia del reporte `report.point_of_sale.report_saledetails`

---

## Historial de Desarrollo

### Fase 1: Modelos Base
- Creación de campos en `res.partner`, `pos.config`, `pos.order`
- Implementación de la lógica de cálculo de puntos

### Fase 2: Vistas
- Formularios de configuración del POS
- Formulario de contactos con puntos y botón de historial
- Vista de historial de órdenes con puntos

### Fase 3: Reportes
- Extensión del reporte de detalles de venta
- Diseño responsive compatible con PDF
- Integración de puntos de fidelización en el reporte

### Fase 4: Pruebas
- Desarrollo de 7 casos de prueba
- Cobertura de diferentes escenarios de configuración
