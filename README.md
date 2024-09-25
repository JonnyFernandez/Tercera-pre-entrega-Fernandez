# Poryecto BLOG

- 1 Instalar entorno virtual en la carpeta del proyecto

```
- Si operas con pipenv: pipenv install
- Si operas con virtualenv: virtualenv venv
```

- 2 Activar entorno virtual

```
- Si operas con pipenv: pipenv shell
- Si operas con virtualenv: ./venv/scripts/activate
```

- 3 Instalar las dependencias:

```
pip install -r requirements.txt
```

- 4 Levantar el servidor

```
python manage.py runserver
```

## Operaciones en la Blog-Site

- 1

```
Hacer un post de categorias, estas tienen relacion 1 - N con Post
```

- 2

```
Crear Post
```

- 3

```
todos los post apareren en el home
```

- 4

```
buscar por titulo o categoria desde el home
```

- 5

```
las card que aparecen en el home tienen link para detalle del post
```

- 6

```
En el detalle del post se vera la descripcion completa y las reseña de los usuarios
```

- 7

```
Opcion para agregar una reseña
```

## Nota

- Creacion del archivo requirements.txt:

```
pip freeze > requirements.txt
```

- para instalar las dependencias:

```
pip install -r requirements.txt
```
