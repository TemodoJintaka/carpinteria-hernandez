# Carpintería Hernández (madera)

Aplicación web Django para el proyecto **Carpintería Hernández** (paquete Python `madera`), generada con [Cookiecutter Django](https://github.com/cookiecutter/cookiecutter-django/).

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Licencia: MIT

---

## Requisitos

| Herramienta   | Uso |
|---------------|-----|
| **Docker** y **Docker Compose** (plugin v2) | Desarrollo local recomendado (Django, PostgreSQL, Redis, Mailpit). |
| **Python 3.13** y **[uv](https://docs.astral.sh/uv/)** | Gestión de dependencias y comandos fuera del contenedor (por ejemplo linters o tests locales si los configuráis así). Versión indicada en `.python-version`. |

Opcional: [**just**](https://github.com/casey/just) para atajos (`just up`, `just manage`, etc.). El archivo `justfile` ya apunta a `docker-compose.local.yml`.

---

## Inicializar el proyecto (desarrollo local con Docker)

Sigue estos pasos la primera vez (y tras clonar el repositorio en otra máquina).

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd carpinteria-hernandez
```

### 2. Revisar variables de entorno (local)

Los archivos de ejemplo para entorno local están en:

- `.envs/.local/.django` — Django, Redis, Celery/Flower en depuración.
- `.envs/.local/.postgres` — host, puerto, base de datos y credenciales de PostgreSQL.

Ajustad solo lo necesario; los valores por defecto sirven para trabajar en local con Docker.

### 3. Construir e iniciar los contenedores

**Opción A — con Docker Compose directamente:**

```bash
docker compose -f docker-compose.local.yml build
docker compose -f docker-compose.local.yml up
```

**Opción B — con `just` (si lo tenéis instalado):**

```bash
just build
just up
```

Al arrancar, el servicio Django ejecuta las migraciones y levanta la app con **Uvicorn** y recarga en caliente (ver `compose/local/django/start`).

Servicios que quedan levantados:

| Servicio   | Descripción |
|------------|-------------|
| **Django** | API y web en [http://127.0.0.1:8000](http://127.0.0.1:8000) |
| **PostgreSQL** | Base de datos (uso interno en la red de Compose) |
| **Redis** | Caché / broker según configuración |
| **Mailpit** | Captura de correo en desarrollo: [http://127.0.0.1:8025](http://127.0.0.1:8025) |

### 4. Crear un usuario administrador

En otra terminal, con los contenedores en marcha:

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py createsuperuser
```

Con `just`:

```bash
just manage createsuperuser
```

### 5. Parar el entorno

```bash
docker compose -f docker-compose.local.yml down
```

O: `just down`.  
Para borrar también los volúmenes (datos de BD): `just prune` o `docker compose -f docker-compose.local.yml down -v`.

---

## Comandos útiles

### Administración de Django dentro de Docker

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py <comando>
```

Ejemplos: `migrate`, `shell`, `collectstatic` (según entorno).

### Tests (como en CI)

```bash
docker compose -f docker-compose.local.yml run --rm django python manage.py migrate
docker compose -f docker-compose.local.yml run django pytest
```

### Herramientas de calidad (fuera de Docker, con `uv`)

Tras `uv sync --all-groups`:

```bash
uv run ruff check .
uv run mypy madera
uv run pytest
```

Cobertura (resumen similar al README original de Cookiecutter):

```bash
uv run coverage run -m pytest
uv run coverage html
```

### Usuarios y correo en desarrollo

- **Usuario normal:** registro desde la web; el correo de verificación aparece en **Mailpit** ([http://127.0.0.1:8025](http://127.0.0.1:8025)), no en una bandeja real.
- **Superusuario:** ver sección 4 más arriba.

### Configuración avanzada de Django

Documentación oficial de Cookiecutter sobre [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

### Documentación del proyecto (Sphinx)

```bash
docker compose -f docker-compose.docs.yml up
```

---

## Despliegue

Despliegue con Docker: [documentación Cookiecutter Django — Docker](https://cookiecutter-django.readthedocs.io/en/latest/3-deployment/deployment-with-docker.html).

---

## Traducciones (gettext)

Si trabajáis con mensajes traducibles, ver `locale/README.md` para `makemessages` / `compilemessages` con el mismo `docker-compose.local.yml`.
