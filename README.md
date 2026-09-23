# DRF Project — API de Productos

API REST desarrollada con **Django REST Framework** para la gestión de artículos y categorías de un catálogo de productos (proyecto práctico orientado a un futuro sistema de e-commerce).

## 🛠️ Tecnologías

- Python 3.12
- Django >= 6.1
- Django REST Framework >= 3.18
- SQLite (base de datos por defecto)
- [uv](https://docs.astral.sh/uv/) como gestor de entornos y dependencias

## 📁 Estructura del proyecto

```
drf-project/
├── src/
│   ├── manage.py
│   ├── settings/          # Configuración del proyecto (settings, urls, wsgi, asgi)
│   └── productos/         # App principal
│       ├── models.py      # Modelos Categoria y Articulo
│       ├── serializers.py # Serializers de DRF
│       ├── views.py       # Vistas basadas en generics
│       ├── urls.py        # Rutas de la API
│       └── admin.py
├── Drf2_entrega/           # Colección de requests (Bruno/Postman) para probar la API
├── pyproject.toml
└── uv.lock
```

## 📦 Modelos

**Categoria**
| Campo | Tipo |
|---|---|
| nombre | CharField(100) |
| descripcion | TextField (opcional) |

**Articulo**
| Campo | Tipo |
|---|---|
| nombre | CharField(150) |
| precio | IntegerField |
| stock | IntegerField |
| timestamp | DateTimeField (auto) |
| categoria | ForeignKey → Categoria (opcional, SET_NULL) |

## 🔌 Endpoints

Todas las rutas están montadas bajo el prefijo `/api/`.

| Método | Endpoint | Descripción |
|---|---|---|
| GET, POST | `/api/categorias/` | Listar / crear categorías |
| GET, PUT, PATCH, DELETE | `/api/categorias/<id>/` | Detalle / editar / eliminar categoría |
| GET, POST | `/api/articulos/` | Listar / crear artículos |
| GET, PUT, PATCH, DELETE | `/api/articulos/<id>/` | Detalle / editar / eliminar artículo |

El serializer de `Articulo` expone la `categoria` completa (anidada, solo lectura) y acepta `categoria_id` para asignarla al crear/editar.

## 🚀 Instalación y uso

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/SantiiCapee/drf-project.git
   cd drf-project
   ```

2. Instalar dependencias con uv:
   ```bash
   uv sync
   ```

3. Aplicar migraciones:
   ```bash
   cd src
   uv run manage.py migrate
   ```

4. Levantar el servidor de desarrollo:
   ```bash
   uv run manage.py runserver
   ```

5. La API quedará disponible en `http://127.0.0.1:8000/api/`

## 🧪 Probar la API

En la carpeta `Drf2_entrega/` hay una colección de requests (formato Bruno/Postman) con ejemplos para listar, crear, editar y borrar artículos y categorías.

## 👥 Integrantes

- Facundo Bellandi
- Santiago Capellino
- Alejandro Quiroga

## 📌 Estado del proyecto

Proyecto práctico de la materia DRF, con CRUD funcional para artículos y categorías. Pensado como base para evolucionar hacia una app de e-commerce más completa.
