#!/usr/bin/env python3
"""
Crea en Odoo eLearning el curso "SecureVu Map" (operación y administración),
con contenidos como artículos HTML, un quiz final y una certificación.
Idempotente: busca-o-crea por nombre. No escribe secretos en disco.

  ODOO_URL   p.ej. https://secure-corp.odoo.com
  ODOO_DB    p.ej. secure-corp
  ODOO_USER  tu login (email)
  ODOO_KEY   API key (Preferencias > Seguridad de la cuenta) o contraseña

Ejecutar:  ODOO_URL=... ODOO_DB=... ODOO_USER=... ODOO_KEY=... python3 odoo_upload.py
Introspección (no crea): añade --introspect
"""
import os, sys, ssl, xmlrpc.client

URL = os.environ.get("ODOO_URL", "https://secure-corp.odoo.com").rstrip("/")
DB  = os.environ.get("ODOO_DB", "secure-corp")
USER = os.environ.get("ODOO_USER", "")
KEY = os.environ.get("ODOO_KEY", "")
INTROSPECT = "--introspect" in sys.argv

CHANNEL = "SecureVu Map — Operación y Administración"
CHANNEL_DESC = ("Curso del mapa de monitoreo SecureVu Map: cómo operarlo (rol visor) "
                "y cómo administrarlo (rol admin). En español, sin requisitos técnicos "
                "para la parte de operación.")
CERT_TITLE = "Certificación: SecureVu Map"
PASS = 70.0

def H(title, body):
    return f"<h2>{title}</h2>\n{body}"

# (sección, título, html)
SLIDES = [
  ("Introducción", "¿Qué es SecureVu Map?", H("¿Qué es SecureVu Map?",
    "<p>SecureVu Map es el <b>mapa de monitoreo</b> de las cámaras de "
    "videovigilancia. Sobre un mapa muestra cada cámara, su <b>estado en vivo</b> "
    "(en línea / fuera de línea), el <b>video en tiempo real</b>, la "
    "<b>disponibilidad histórica</b> y las <b>alarmas SOS y Tamper</b> de cada "
    "sitio.</p><ul><li><b>Visor</b>: monitorea (mapa, video, disponibilidad, "
    "alarmas, asistente).</li><li><b>Administrador</b>: además configura "
    "servidores, coordenadas y usuarios.</li></ul>")),
  ("Introducción", "Acceso y roles", H("Acceso y roles",
    "<p>Abre la dirección que te dio tu administrador e inicia sesión con tu "
    "usuario y contraseña. En instalaciones internas, si aparece una advertencia "
    "de certificado, continúa (es un certificado propio de la red).</p>"
    "<table border='1' cellpadding='6'><tr><th>Rol</th><th>Puede</th></tr>"
    "<tr><td>Visor</td><td>Mapa, video, disponibilidad, alarmas y asistente.</td></tr>"
    "<tr><td>Administrador</td><td>Todo lo anterior + Administración.</td></tr></table>"
    "<p>¿Olvidaste tu contraseña? Un administrador la restablece en "
    "<i>Administración → Usuarios</i>.</p>")),

  ("Uso (Visor)", "El mapa y los marcadores", H("El mapa y los marcadores",
    "<p>Cada marcador es un sitio/torre que agrupa varias cámaras. El color "
    "resume el estado del grupo:</p><ul>"
    "<li>🟢 <b>Verde</b>: todas en línea.</li>"
    "<li>🔴 <b>Rojo</b>: todas fuera.</li>"
    "<li>🟠 <b>Ámbar</b>: <b>mixto</b> (algunas fuera; revísalo).</li>"
    "<li>⚪ <b>Gris</b>: sin transmisión.</li></ul>"
    "<p>Si el sitio tiene varias cámaras, el marcador muestra un <b>número</b>. "
    "Al pasar el cursor verás cuántas están en línea / fuera.</p>")),
  ("Uso (Visor)", "Filtrar, buscar y ver una cámara", H("Filtrar, buscar y ver una cámara",
    "<p>En la barra superior: <b>Servidor</b> y <b>Tipo</b> filtran; el "
    "<b>buscador</b> te lleva a una cámara por nombre.</p>"
    "<p>Al hacer clic en un marcador se abre el panel derecho con el "
    "<b>video en vivo</b> (silenciar, pantalla completa, reconectar), las "
    "<b>cámaras del mismo sitio</b> como fichas para cambiar entre ellas, y la "
    "<b>barra de disponibilidad de 7 días</b> (pasa el cursor para ver el rango de "
    "horas y el porcentaje). Las cámaras <b>LPR</b> se ven oscuras de noche: es "
    "normal.</p><p>Como <b>visor</b> solo se muestra el dato <b>Servidor</b>; el "
    "resto (Grupo, Tipo, IP, Stream) es para administradores.</p>")),
  ("Uso (Visor)", "Estadísticas de disponibilidad", H("Estadísticas de disponibilidad",
    "<p>Haz clic en los <b>contadores</b> de la barra superior. Verás totales, la "
    "<b>disponibilidad</b> del periodo y un selector <b>7 días / Mes / Periodo</b> "
    "(fechas a tu elección), además de la disponibilidad por servidor y la lista de "
    "cámaras fuera de línea en este momento.</p>")),
  ("Uso (Visor)", "Alarmas SOS / Tamper", H("Alarmas SOS / Tamper",
    "<p>Cuando un sitio dispara <b>SOS</b> (pánico) o <b>Tamper</b> (sabotaje), "
    "aparece un <b>marcador rojo pulsante</b> en el mapa y la <b>campana 🔔</b> "
    "muestra un contador. En el panel de alarmas cada una tiene estado "
    "<b>ACTIVA → RECONOCIDA → RESUELTA</b> y acciones:</p><ul>"
    "<li><b>Reconocer</b>: indicas que la estás atendiendo.</li>"
    "<li><b>Resolver</b>: la cierras (con nota opcional).</li>"
    "<li><b>Nota</b>: agregas una observación.</li>"
    "<li><b>Ver cámaras</b>: saltas a las cámaras de ese sitio.</li></ul>"
    "<p>Cada acción queda en la <b>bitácora</b> con tu usuario y la hora.</p>")),
  ("Uso (Visor)", "Asistente IA", H("Asistente IA",
    "<p>El botón <b>💬</b> abre un asistente al que preguntas en español sobre "
    "eventos y alarmas, por ejemplo: «¿cuántas personas se detectaron hoy?» o "
    "«¿hubo alguna alarma SOS y en qué torre?». Responde con datos reales.</p>")),

  ("Administración", "Servidores y descubrimiento", H("Servidores y descubrimiento",
    "<p>En <b>⚙ Administración → Servidores</b> agregas la IP/nombre de cada "
    "servidor SecureVu y guardas. Con <b>«Descubrir cámaras y reconstruir mapa»</b> "
    "la app consulta los servidores, encuentra todas las cámaras y te dice cuántas "
    "quedaron con/sin coordenadas. Aquí también configuras el <b>Asistente IA</b> "
    "(proveedor Ollama o Anthropic) y descargas la <b>plantilla CSV</b>.</p>")),
  ("Administración", "Coordenadas (ubicar cámaras)", H("Coordenadas (ubicar cámaras)",
    "<p>En <b>Coordenadas</b> subes un CSV/Excel y eliges el <b>mapeo de "
    "columnas</b>: la <b>columna llave</b> (lo más confiable es la <b>IP</b> de la "
    "cámara), <b>latitud/longitud</b> y opcionalmente nombre, grupo y tipo. El "
    "<b>Grupo</b> (la torre) define cómo se agrupan en un marcador.</p>"
    "<p>Usa <b>«Probar emparejamiento»</b> para ver cuántas coinciden antes de "
    "<b>«Publicar al mapa»</b>. Si quedan <b>0 con coordenadas</b>, casi siempre la "
    "columna llave no corresponde: prueba con la IP.</p>")),
  ("Administración", "Usuarios y roles", H("Usuarios y roles",
    "<p>En <b>Usuarios</b> creas cuentas, cambias el rol (visor/admin) o eliminas. "
    "Crea cuentas <b>visor</b> para el personal de monitoreo y cambia la contraseña "
    "del admin inicial. El <b>visor</b> solo monitorea y, en el panel de cámara, "
    "solo ve <b>Servidor</b>; el <b>admin</b> ve todos los detalles y la "
    "configuración.</p>")),
  ("Administración", "Alarmas y solución de problemas", H("Alarmas y solución de problemas",
    "<p>Las alarmas llegan solas desde <b>SecureTrax</b> (los microcontroladores de "
    "cada sitio); no requieren configuración aquí. Si no llegan, el equipo técnico "
    "debe verificar el <b>reenvío de eventos</b> de SecureTrax.</p>"
    "<p>Cámaras que no aparecen: revisa el mapeo de coordenadas (usa la IP), que la "
    "cámara esté en el archivo, y que el servidor esté en la lista y sea "
    "alcanzable.</p>")),
]

# Quiz / certificación: (pregunta, tipo, [(opción, correcta)])
QUIZ = [
  ("¿Qué significa un marcador ámbar en el mapa?", "single",
   [("Todas las cámaras del sitio están en línea", False),
    ("Estado mixto: algunas en línea y otras fuera", True),
    ("El sitio no tiene cámaras", False),
    ("Hay una alarma SOS", False)]),
  ("Como rol visor, ¿qué dato de la cámara se muestra en el panel?", "single",
   [("Grupo, Tipo, IP y Stream", False), ("Solo el Servidor", True),
    ("Ninguno", False), ("La contraseña RTSP", False)]),
  ("¿Para qué sirve pasar el cursor por la barra de disponibilidad?", "single",
   [("Reconectar el video", False),
    ("Ver el rango de horas y el porcentaje de ese tramo", True),
    ("Cambiar de cámara", False), ("Borrar el historial", False)]),
  ("¿Qué estados puede tener una alarma?", "single",
   [("Nueva / Vieja", False), ("Activa / Reconocida / Resuelta", True),
    ("Abierta / Cerrada / Pendiente de pago", False), ("Verde / Rojo / Gris", False)]),
  ("Al atender una alarma, ¿qué queda registrado?", "single",
   [("Nada", False), ("Solo la hora", False),
    ("El usuario que actuó, la acción y la hora", True), ("Solo si se resolvió", False)]),
  ("¿Qué hace el botón «Ver cámaras» de una alarma?", "single",
   [("Apaga la cámara", False), ("Salta a las cámaras de ese sitio", True),
    ("Exporta un reporte", False), ("Reinicia el servidor", False)]),
  ("En el selector de disponibilidad, ¿qué periodos hay?", "single",
   [("Solo 24 horas", False), ("7 días, Mes y Periodo personalizado", True),
    ("Solo el mes actual", False), ("Año completo", False)]),
  ("¿Cómo descubre la app las cámaras de un servidor? (admin)", "single",
   [("Hay que capturarlas a mano", False),
    ("Consulta el servidor y las encuentra solas al «Descubrir»", True),
    ("Las lee de un PDF", False), ("No puede, requiere reinstalar", False)]),
  ("Si al publicar coordenadas quedan «0 con coordenadas», ¿qué revisar primero? (admin)", "single",
   [("Reiniciar el navegador", False), ("La columna llave del mapeo (probar con la IP)", True),
    ("Cambiar de servidor de IA", False), ("Borrar todos los usuarios", False)]),
  ("¿Qué puede hacer un rol visor?", "single",
   [("Configurar servidores y usuarios", False),
    ("Monitorear: mapa, video, disponibilidad, alarmas y asistente", True),
    ("Subir coordenadas", False), ("Eliminar cámaras", False)]),
]


def connect():
    common = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/common", context=ssl._create_unverified_context())
    uid = common.authenticate(DB, USER, KEY, {})
    if not uid:
        sys.exit("ERROR: autenticación fallida. Revisa ODOO_DB/USER/KEY.")
    models = xmlrpc.client.ServerProxy(f"{URL}/xmlrpc/2/object", context=ssl._create_unverified_context())
    return uid, models


def main():
    if not (USER and KEY):
        sys.exit("Define ODOO_URL, ODOO_DB, ODOO_USER, ODOO_KEY en el entorno.")
    uid, models = connect()
    def ex(model, method, *a, **k):
        return models.execute_kw(DB, uid, KEY, model, method, list(a), k)

    sfields = ex("slide.slide", "fields_get", [], {"attributes": ["string"]})
    cat = "slide_category" if "slide_category" in sfields else "slide_type"
    html_field = "html_content" if "html_content" in sfields else ("content" if "content" in sfields else None)
    art_cat = "article" if cat == "slide_category" else "infographic"
    print(f"campo categoría={cat}, campo html={html_field}, categoría artículo={art_cat}")
    if INTROSPECT:
        print("slide.slide fields:", sorted(sfields)); return

    def foc(model, domain, vals, label):
        ids = ex(model, "search", domain, limit=1)
        if ids:
            print(f"= {label} (id {ids[0]})"); return ids[0]
        rid = ex(model, "create", vals)
        print(f"+ {label} (id {rid})"); return rid

    ch = foc("slide.channel", [["name", "=", CHANNEL]],
             {"name": CHANNEL, "description": CHANNEL_DESC, "is_published": False},
             "curso")
    seq = 1
    # secciones en orden de aparición
    sections, order = {}, []
    for sec, _, _ in SLIDES:
        if sec not in sections:
            order.append(sec); sections[sec] = None
    for sec in order:
        sid = foc("slide.slide",
                  [["channel_id", "=", ch], ["name", "=", sec], ["is_category", "=", True]],
                  {"name": sec, "channel_id": ch, "is_category": True, "sequence": seq},
                  f"sección {sec}")
        sections[sec] = sid; seq += 1
        for s_sec, title, html in SLIDES:
            if s_sec != sec: continue
            vals = {"name": title, "channel_id": ch, "category_id": sid,
                    "sequence": seq, cat: art_cat, "is_published": False}
            if html_field: vals[html_field] = html
            foc("slide.slide",
                [["channel_id", "=", ch], ["category_id", "=", sid], ["name", "=", title],
                 ["is_category", "=", False]], vals, f"artículo «{title}»")
            seq += 1

    # Evaluación + quiz
    eval_sec = foc("slide.slide",
                   [["channel_id", "=", ch], ["name", "=", "Evaluación final"], ["is_category", "=", True]],
                   {"name": "Evaluación final", "channel_id": ch, "is_category": True, "sequence": seq},
                   "sección Evaluación"); seq += 1
    quiz = foc("slide.slide", [["channel_id", "=", ch], ["name", "=", "Quiz — SecureVu Map"]],
               {"name": "Quiz — SecureVu Map", "channel_id": ch, "category_id": eval_sec,
                "sequence": seq, cat: "quiz", "is_published": False}, "quiz"); seq += 1
    if not ex("slide.question", "search_count", [["slide_id", "=", quiz]]):
        for qi, (qt, _, opts) in enumerate(QUIZ, 1):
            qid = ex("slide.question", "create", {"question": qt, "slide_id": quiz, "sequence": qi})
            for ot, ok in opts:
                ex("slide.answer", "create", {"question_id": qid, "text_value": ot, "is_correct": ok})
        print(f"+ quiz poblado ({len(QUIZ)} preguntas)")

    # Certificación
    svf = ex("survey.survey", "fields_get", [], {"attributes": []})
    sv_vals = {"title": CERT_TITLE, "certification": True, "scoring_type": "scoring_with_answers"}
    for f, v in (("scoring_success_min", PASS), ("is_attempts_limited", True),
                 ("attempts_limit", 3), ("questions_layout", "page_per_question")):
        if f in svf: sv_vals[f] = v
    sv = foc("survey.survey", [["title", "=", CERT_TITLE]], sv_vals, "certificación")
    if not ex("survey.question", "search_count", [["survey_id", "=", sv], ["is_page", "=", False]]):
        for qi, (qt, _, opts) in enumerate(QUIZ, 1):
            ans = [(0, 0, {"value": ot, "is_correct": ok, "answer_score": 1.0 if ok else 0.0}) for ot, ok in opts]
            ex("survey.question", "create",
               {"survey_id": sv, "title": qt, "sequence": qi, "question_type": "simple_choice",
                "is_scored_question": True, "constr_mandatory": True, "suggested_answer_ids": ans})
        print(f"+ certificación poblada ({len(QUIZ)} preguntas)")
    if "survey_id" in sfields:
        foc("slide.slide", [["channel_id", "=", ch], [cat, "=", "certification"], ["survey_id", "=", sv]],
            {"name": CERT_TITLE, "channel_id": ch, "sequence": seq + 5, cat: "certification",
             "survey_id": sv, "is_published": False}, "contenido de certificación")

    print(f"\nLISTO → {URL}/odoo/elearning  (curso en borrador, revísalo y publícalo)")

if __name__ == "__main__":
    main()
