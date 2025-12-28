# Módulo: Evaluación de Desempeño (Ejercicio 1)

Este módulo ha sido desarrollado como parte de la prueba técnica de Binaural. Implementa un flujo completo para la gestión de evaluaciones de empleados en Odoo 17.

## 🚀 Funcionalidades Principales
- **Gestión de Evaluaciones**: Modelo `hr.performance.review` con seguimiento de metas, fortalezas y debilidades.
- **Flujo de Estados**: Kanban organizado por estados `Pendiente` y `Completada`.
- **Seguridad y Validación**:
  - **Filtro de RRHH**: Solo usuarios del grupo `Human Resources / Officer` o `Manager` pueden ser evaluadores.
  - **Integridad**: Validación que impide que un empleado se evalúe a sí mismo (User ID validation).
  - **Rango de Puntaje**: Restricción de 0 a 10 puntos.
- **Reportes**: Generación de PDF con el historial de evaluaciones por empleado.

## 🛠️ Instalación en el Workspace
1. Colocar la carpeta `hr_performance_review` en `src/custom/`.
2. El entorno detectará automáticamente el módulo gracias a la configuración de `addons_path` en el workspace.

## 🧪 Pruebas Unitarias (Testing)
Para validar la lógica de negocio y las restricciones de seguridad, ejecute el siguiente comando (adaptado al estándar de Binaural Workspace):

```bash
docker exec -u odoo -it proj odoo -d binaural_db -i hr_performance_review --test-enable --without-demo=true --stop-after-init --addons-path=/usr/lib/python3/dist-packages/odoo/addons,/home/odoo/src/custom --http-port 8072