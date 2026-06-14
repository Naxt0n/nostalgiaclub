# Nostalgia Club — Canva Exact App

- La home usa las 4 páginas exportadas de Canva como imágenes completas.
- Las imágenes están pegadas una debajo de otra, sin recortes ni agregados.
- En la tercera página hay zonas clickeables invisibles sobre los looks.
- Cada look abre una página individual con imagen en grande y descripción breve.

## Ejecutar localmente

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abrir:

```text
http://127.0.0.1:5000
```

## Deploy en Render

Build command:

```bash
pip install -r requirements.txt
```

Start command:

```bash
gunicorn app:app
```
