# Evaluaciones de Desempeño

![Odoo Version](https://img.shields.io/badge/Odoo-17.0-blue)
![License](https://img.shields.io/badge/License-LGPL--3-green)
![Tests](https://img.shields.io/badge/Tests-5%20passing-brightgreen)

## 📋 Descripción

Módulo de Odoo 17 para gestionar **evaluaciones periódicas de empleados**. Permite a Recursos Humanos realizar seguimiento del desempeño con puntajes, fortalezas, debilidades y objetivos.

---

## ✨ Características

| Característica | Descripción |
|----------------|-------------|
| Modelo completo | Campos para empleado, evaluador, puntaje, comentarios, fortalezas, debilidades y objetivos |
| Vista Kanban | Organización por estados: Pendiente y Completada |
| Validaciones | Puntaje 0-10, evaluador debe ser de RRHH, no auto-evaluación |
| Reporte PDF | Historial de evaluaciones por empleado |
| Seguimiento | Integración con chatter para tracking de cambios |

---

## 🛠️ Instalación

### Requisitos
- Odoo 17.0
- Módulos `hr` y `mail` instalados

### Pasos

1. Copiar la carpeta `hr_performance_review` a `addons/`
2. Actualizar lista de aplicaciones en Odoo
3. Buscar "Evaluaciones" e instalar

---

## ⚙️ Uso

### Crear una evaluación

1. Ve a **Desempeño** (menú de aplicaciones)
2. Clic en **Nuevo**
3. Selecciona el empleado a evaluar
4. Completa puntaje (0-10), fortalezas, debilidades
5. Guarda

### Vista Kanban

- Las evaluaciones se organizan en columnas por estado
- Usa el botón "Marcar como Completada" para cambiar estado

### Generar reporte

1. Abre una evaluación
2. Clic en **Imprimir** → **Histórico de Desempeño**

---

## 🧪 Pruebas

Ejecutar tests:
```bash
docker exec -u odoo proj odoo -d demo_limpia -u hr_performance_review --test-enable --stop-after-init --no-http
```

### Tests incluidos

| Test | Descripción |
|------|-------------|
| test_performance_creation | Validar creación correcta de evaluaciones |
| test_self_evaluation_denied | Empleado no puede evaluarse a sí mismo |
| test_score_validation | Puntaje debe estar entre 0 y 10 |
| test_reviewer_permission | Solo usuarios RRHH pueden evaluar |
| test_full_flow | Flujo completo de estados |

---

## 📁 Estructura

```
hr_performance_review/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── hr_performance.py
├── views/
│   └── hr_performance_views.xml
├── reports/
│   ├── ir_actions_report.xml
│   └── performance_report_template.xml
├── security/
│   └── ir.model.access.csv
└── tests/
    ├── __init__.py
    └── test_performance.py
```

---

## 📝 Autor

**Leidy Callejas**

## 📄 Licencia

LGPL-3