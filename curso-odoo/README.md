# Curso Odoo — SecureVu Map

Script idempotente que crea en **Odoo eLearning** (`secure-corp.odoo.com`) el
curso **«SecureVu Map — Operación y Administración»**: secciones de Introducción,
Uso (visor) y Administración como artículos HTML, un **quiz** final de 10
preguntas y una **certificación** (aprobación 70%). En español.

## Publicar

```bash
ODOO_URL=https://secure-corp.odoo.com \
ODOO_DB=secure-corp \
ODOO_USER=tu-correo@securecorp.com \
ODOO_KEY=tu-api-key \
python3 odoo_upload.py
```

La API key se obtiene en Odoo: **Preferencias → Seguridad de la cuenta → Nueva
clave de API**. El curso se crea en **borrador**; revísalo y publícalo desde
eLearning. Volver a ejecutar no duplica (busca-o-crea por nombre).

`--introspect` solo inspecciona los campos disponibles, sin crear nada.
