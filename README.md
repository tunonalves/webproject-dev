# webproject-dev

Aplicación Django de gestión administrativa con módulos de clientes, empresas, órdenes de compra, facturación, envíos y pagos. El código incluye modelos relacionados, formularios, vistas de listado/alta/detalle/edición/eliminación y plantillas HTML. La interfaz conserva la identificación **Software CNA MULTIMEDIOS 2022** y el enlace de autor presente en la plantilla base.

> Proyecto de desarrollo: no debe exponerse a Internet ni utilizar datos reales sin revisar autenticación, permisos, dependencias y configuración. Este README documenta el código existente; no certifica su funcionamiento en producción.

## Tecnologías y estado

- Python y Django; `requirements.txt` anota Python 3.10.5 y Django 4.1.3, mientras que la cabecera de la configuración proviene de Django 3.0.14.
- SQLite como base de datos local.
- Plantillas Django, Bootstrap, jQuery y Font Awesome incluidos en `static/`.
- `crispy_forms`, con `CRISPY_TEMPLATE_PACK = 'bootstrap4'`.
- El manifiesto menciona además Pillow y Requests, sin fijar sus versiones.

`requirements.txt` es una lista informativa, **no un archivo instalable directamente con `pip install -r`**: contiene líneas como `python 3.10.5` y nombres/versiones sin sintaxis de requisitos. El paquete que proporciona `crispy_forms` se distribuye como `django-crispy-forms`.

## Preparación local

Se necesita Git y un intérprete Python 3.10 con soporte para entornos virtuales. Esta receta es una propuesta de reproducción del entorno histórico, no un conjunto de dependencias probado ni una recomendación para producción:

```bash
git clone git@github.com:tunonalves/webproject-dev.git
cd webproject-dev
python3.10 -m venv .venv
source .venv/bin/activate
python -m pip install 'Django==4.1.3' 'django-crispy-forms==1.14.0' Pillow requests
python manage.py check
```

La selección de `django-crispy-forms==1.14.0` mantiene las plantillas Bootstrap 4 de la generación 1.x; no es una versión fijada por el repositorio. Antes de actualizar a otra generación, revisar también los paquetes de plantillas y la configuración. No se proporciona un lockfile reproducible.

Solo después de resolver los errores de `check`, crear las tablas en una base local y, opcionalmente, un usuario administrador:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

Abrir <http://127.0.0.1:8000/>. `migrate` modifica la base configurada: confirmar que sea una base de desarrollo antes de ejecutarlo. La configuración incluida usa SQLite y `DEBUG = True`; el servidor de desarrollo no sustituye un despliegue seguro.

## Uso y rutas

| Ruta | Módulo |
| --- | --- |
| `/` | Inicio y navegación |
| `/clientes/` | Clientes |
| `/empresas/` | Empresas |
| `/ordencompra/` | Órdenes de compra |
| `/facturacion/` | Facturas |
| `/envios/` | Registro de envíos |
| `/pagos/` | Registro de pagos |
| `/usuarios/` | Pantalla de usuarios |
| `/usuarios/registro/` | Formulario de registro incompleto |
| `/admin/` | Administración Django |

Para cargar datos relacionados, comenzar por empresas y clientes, continuar con órdenes de compra y facturas, y luego registrar envíos o pagos. Los envíos almacenan información como fechas y dirección de correo; las vistas revisadas no implementan un envío automático de email. Tampoco debe confundirse el registro de facturas/pagos con una integración fiscal o una pasarela de cobro.

## Estructura

- [`manage.py`](manage.py): entrada de los comandos Django.
- [`websiteproject/`](websiteproject/): ajustes, rutas raíz y entradas ASGI/WSGI.
- [`webhome/`](webhome/): inicio y plantilla compartida `templates/base.html`.
- [`cliente/`](cliente/) y [`empresa/`](empresa/): datos de clientes y empresas.
- [`ordencompra/`](ordencompra/) y [`facturacion/`](facturacion/): órdenes y facturas relacionadas.
- [`envios/`](envios/) y [`pagos/`](pagos/): registros asociados a la facturación.
- [`usuarios/`](usuarios/): pantallas de usuarios y registro.
- [`static/`](static/): estilos, imágenes y bibliotecas del frontend.

Las aplicaciones de gestión contienen sus propias migraciones, formularios y plantillas.

## Limitaciones y comprobaciones

- `Vregistro.post()` en `usuarios/views.py` está vacío: mostrar el formulario no implica que se puedan registrar usuarios.
- Las vistas de clientes importan utilidades de autenticación, pero sus clases CRUD no aplican `LoginRequiredMixin`. Revisar permisos en todos los módulos antes de compartir una instancia.
- Preparar una clave secreta propia fuera del control de versiones y revisar `DEBUG`, hosts permitidos, HTTPS y protección de los datos antes de cualquier despliegue. No se documenta un cargador automático de `.env`.
- Las relaciones usan eliminaciones en cascada: trabajar con datos de prueba y mantener copias antes de borrar registros.
- `cliente/tests.py` conserva el esqueleto de pruebas; no constituye cobertura funcional.

Comprobaciones sugeridas en el entorno preparado:

```bash
python manage.py check
python manage.py showmigrations
python manage.py test
```

Para esta revisión documental se inspeccionaron rutas, modelos, formularios, vistas, ajustes no sensibles y plantillas. No se instalaron dependencias ni se ejecutaron migraciones, servidor o pruebas Django; los comandos anteriores quedan pendientes de validación en tiempo de ejecución.

## Créditos

Repositorio de [tunonalves](https://github.com/tunonalves). La plantilla base atribuye la interfaz a Software CNA MULTIMEDIOS 2022 y enlaza a [la página del autor](https://tunonalves.wixsite.com/federico). Las bibliotecas incluidas conservan sus propios avisos y licencias. No se incluye un archivo de licencia general del proyecto.
