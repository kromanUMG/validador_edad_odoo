# validador_edad_odoo

## Objetivo del Sprint

Desarrollar un módulo para Odoo 16 que valide automáticamente la fecha de nacimiento de los usuarios al momento del registro. El módulo debe bloquear registros si el usuario tiene menos de 13 años, según las políticas de privacidad.

## Herramientas necesarias

- Odoo 16 CE
- Python 3.10+
- Docker y Docker Compose
- PostgreSQL (contenedor Docker)
- Git, GitHub
- PowerShell
- Visual Studio Code

## Requerimientos técnicos

- Validación en `@api.constrains`
- Base de datos PostgreSQL en contenedor Docker
- Pruebas unitarias con `unittest`
- CI/CD en GitHub Actions
- Ramas Git estructuradas
- Documentación profesional

## Backlog progresivo

| ID | Historia de Usuario / Tarea Técnica                                                         | Rol  | Estado     | Prioridad | Día   |
| -- | ------------------------------------------------------------------------------------------- | ---- | ---------- | --------- | ----- |
| 1  | Crear repositorio en GitHub y rama principal `dev`                                          | PM   | Completado | Alta      | Día 1 |
| 2  | Instalar Python, Git y Docker en máquina local                                              | DEV1 | Completado | Alta      | Día 1 |
| 3  | Crear entorno virtual (`venv`) y activarlo                                                  | DEV1 | Completado | Alta      | Día 1 |
| 4  | Crear estructura inicial del proyecto en carpeta `validador_edad_odoo`                      | DEV1 | Completado | Alta      | Día 1 |
| 5  | Crear módulo base Odoo (`addons/validador_edad_odoo`) con `__init__.py` y `__manifest__.py` | DEV1 | Completado | Alta      | Día 1 |
| 6  | Crear archivo `Dockerfile` para extender imagen Odoo                                        | DEV1 | Completado | Alta      | Día 1 |
| 7  | Crear archivo `docker-compose.yml` con contenedores Odoo y PostgreSQL                       | DEV1 | Completado | Alta      | Día 1 |
| 8  | Confirmar existencia de la carpeta `addons/` y prepararla                                   | DEV1 | Completado | Media     | Día 1 |
| 9  | Levantar contenedores Docker con `docker-compose up -d`                                     | DEV1 | Completado | Alta      | Día 2 |
| 10 | Validar acceso web a Odoo en `http://localhost:8069`                                        | PM   | Completado | Alta      | Día 2 |
| 11 | Crear usuario administrador desde consola Odoo (`odoo shell`)                               | DEV1 | Completado | Alta      | Día 2 |
| 12 | Validar inicio de sesión con `admin@example.com` / `admin123`                               | PM   | Completado | Alta      | Día 2 |



