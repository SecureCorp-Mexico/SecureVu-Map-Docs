# Guía del administrador

[← Volver al inicio](../README.md)

El **administrador** ve todo lo de la [guía del usuario](usuario.md) y además la
sección de **Administración** (⚙ en la barra superior). Aquí se configura de qué
servidores se obtienen las cámaras, sus coordenadas, los usuarios y el asistente.

> La app **descubre las cámaras solas** consultando cada servidor; tú solo
> indicas los servidores y subes las **coordenadas** para ubicarlas en el mapa.

---

## Entrar a Administración

Haz clic en el engrane **⚙** (barra superior). Hay tres pestañas:
**Servidores**, **Coordenadas** y **Usuarios**.

---

## 1. Pestaña «Servidores»

**Configuración general**
- **Título de la app**: el nombre que aparece arriba.
- **Sufijos de stream** (principal / sub): cómo se nombran las dos calidades de
  cada cámara. Si no sabes, deja los valores que ya están.

**Asistente IA (chat)**
- **Proveedor**: `ollama` (un servidor de IA propio) o `anthropic` (nube).
- **URL / Modelo** (para Ollama): la dirección de tu servidor de IA y el modelo.
- **Probar chat**: verifica que responde.

**Servidores SecureVu**
- Agrega la **IP o nombre** de cada servidor y «Guardar configuración».
- **🔄 Descubrir cámaras y reconstruir mapa**: la app consulta cada servidor,
  encuentra todas las cámaras y reconstruye el mapa. Te dice cuántas descubrió,
  cuántas quedaron **con coordenadas** (en el mapa) y cuántas **sin
  coordenadas**.
- **⬇ Descargar plantilla CSV**: un CSV con todas las cámaras descubiertas, listo
  para llenar latitud/longitud.

## 2. Pestaña «Coordenadas»

Aquí pones cada cámara en su lugar del mapa.

1. **Sube** un archivo **CSV o Excel** (arrástralo o elige archivo). ¿No tienes
   uno? Descarga la **plantilla** (botón en la pestaña Servidores) que ya trae
   las cámaras descubiertas.
2. Indica el **mapeo de columnas**:
   - **Columna llave** y **se compara contra**: cómo se identifica cada cámara.
     Si tu archivo trae la **IP** de la cámara, elige la columna de IP y
     «IP de la cámara» (lo más confiable). Si trae el **nombre del stream**,
     elige esa columna y «Nombre del stream».
   - **Latitud** y **Longitud** (obligatorias).
   - **Nombre, Grupo, Tipo** (opcionales). El **Grupo** define cómo se agrupan
     las cámaras en un mismo marcador (normalmente la torre, p. ej.
     `I150200700-558`).
3. **Probar emparejamiento**: muestra cuántas cámaras coincidirían **sin
   publicar** nada. Ajusta el mapeo hasta que el número sea el esperado.
4. **Publicar al mapa**: aplica los cambios para todos.
5. **Cámaras sin coordenadas**: lista las cámaras que no emparejaron, para que
   completes su información en el archivo y vuelvas a subir.

> **Consejo:** si al publicar quedan **0 con coordenadas**, casi siempre la
> «columna llave» elegida no corresponde. Prueba con la columna de **IP** y
> «IP de la cámara».

## 3. Pestaña «Usuarios»

- **Lista** de usuarios con su rol; puedes **cambiar el rol** (visor/admin) o
  **eliminar**.
- **Agregar usuario**: usuario, contraseña (mínimo 6) y rol.

| Rol | Permisos |
|---|---|
| **admin** | Configura servidores, coordenadas y usuarios; ve todos los detalles de cada cámara. |
| **visor** | Solo monitoreo: mapa, video, disponibilidad, alarmas y asistente; en el panel de cámara solo ve **Servidor**. |

> Cambia la contraseña del usuario **admin** inicial en cuanto puedas, y crea
> cuentas **visor** para el personal de monitoreo.

---

## 4. Alarmas SecureTrax (SOS / Tamper)

Las alarmas llegan automáticamente desde el servidor **SecureTrax** (los
microcontroladores de cada sitio) y aparecen en el mapa y en la campana 🔔 (ver
la [guía del usuario](usuario.md#5-alarmas-sos--tamper)). No requieren
configuración en este panel; cualquier usuario puede **reconocer/resolver/anotar**
y queda registrado con su nombre.

En **Administración → Integración SecureTrax** ves el **estado del enlace**:
conectado al broker, tópico MQTT, último mensaje y última alarma recibidos, y los
conteos. Si **Conectado** dice «No» o no llegan alarmas nuevas, pide al equipo
técnico que revise el **reenvío de eventos** en SecureTrax.

## 4b. Auditoría del asistente IA

En **Administración → Asistente IA → «Ver conversaciones (auditoría)»** se lista
el historial de preguntas y respuestas del chat, con **usuario y hora**, para
fines de auditoría.

## 5. Cámaras que no aparecen en el mapa

- Aparece **«con coordenadas: 0»** al publicar → revisa el **mapeo de columnas**
  (usa la IP).
- Una cámara existe pero no se ubica → su IP/nombre no está en el archivo de
  coordenadas; agrégala y vuelve a subir.
- Todo un servidor falta → revisa que esté en la lista de **Servidores** y que la
  app pueda alcanzarlo (botón **Descubrir**).

---

[← Inicio](../README.md) · [Usuario](usuario.md) · [FAQ →](faq.md)
