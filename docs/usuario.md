# Guía del usuario (visor)

[← Volver al inicio](../README.md)

Como **visor** puedes monitorear todas las cámaras, ver el video en vivo,
consultar la disponibilidad histórica, atender alarmas y usar el asistente.

---

## 1. El mapa y los marcadores

Cada **marcador** representa un sitio/torre (que normalmente agrupa varias
cámaras: PTZ, bullet, LPR…). El **color** resume el estado del grupo:

| Color | Significado |
|---|---|
| 🟢 Verde | Todas las cámaras del sitio están **en línea** |
| 🔴 Rojo | Todas están **fuera de línea** |
| 🟠 Ámbar | **Mixto**: algunas en línea y otras fuera (¡revisa este sitio!) |
| ⚪ Gris | Sin transmisión configurada |

Cuando un sitio tiene **más de una cámara**, el marcador muestra un **número**
con la cantidad. Así nunca se "esconde" una cámara debajo de otra.

- **Acercar/alejar**: rueda del ratón o los botones `+` / `–`.
- **Pasar el cursor** por un marcador muestra el nombre del sitio y cuántas
  cámaras tiene en línea / fuera.

## 2. Filtrar y buscar

En la barra superior:

- **Servidor**: muestra solo las cámaras de un servidor.
- **Tipo**: filtra por tipo de cámara (PTZ, BULLET, LPR…).
- **Buscar cámara…**: escribe parte del nombre; aparece una lista, y al elegir
  una, el mapa vuela hasta ella y abre su panel.

## 3. Ver una cámara

Haz clic en un marcador. Se abre el **panel derecho** con:

1. **Video en vivo** de la cámara.
   - 🔇/🔊 activar o silenciar audio · ⛶ pantalla completa · ↻ reconectar.
   - Las cámaras **LPR** (lectura de placas) se ven oscuras de noche: es normal,
     usan obturador rápido e infrarrojo para leer placas.
2. **Cámaras del mismo sitio**: si la torre tiene varias, aparecen como
   **fichas** (PTZ, BULLET 1, BULLET 2, LPR…) con un punto de estado; haz clic
   para cambiar de cámara sin salir del panel.
3. **Disponibilidad · 7 días**: una barra tipo "latido" donde cada segmento es
   ~3 horas. **Pasa el cursor** por la barra para ver el rango de horas y el
   porcentaje de disponibilidad de ese tramo. Arriba se muestra el % total de
   los últimos 7 días.
4. **Servidor**: el servidor SecureVu que entrega esa cámara.

> Si eres administrador verás además **Grupo, Tipo, IP y Stream**. Como visor
> solo se muestra **Servidor**.

## 4. Estadísticas de disponibilidad

Haz clic en los **contadores** de la barra superior (los números de "en línea /
fuera"). Se abre un resumen con:

- Totales: en línea, fuera, total y **disponibilidad** del periodo.
- **Selector de periodo**: **7 días**, **Mes** o **Periodo** (fechas a tu
  elección).
- **Por servidor**: disponibilidad de cada servidor.
- **Fuera de línea ahora**: lista de cámaras caídas y desde cuándo.

## 5. Alarmas SOS / Tamper

Los sitios cuentan con botón de **pánico (SOS)** y sensor de **sabotaje
(Tamper)**. Cuando se disparan:

- Aparece un **marcador rojo pulsante** sobre el sitio en el mapa.
- La **campana 🔔** de la barra superior muestra un contador; haz clic para abrir
  el **panel de alarmas**.

En el panel, cada alarma muestra el tipo (SOS/Tamper), el sitio, cuántas veces se
ha repetido, desde cuándo, y su estado:

| Estado | Significado |
|---|---|
| **ACTIVA** | Recién recibida, sin atender |
| **RECONOCIDA** | Alguien ya la vio y la está atendiendo |
| **RESUELTA** | Atendida y cerrada |

**Acciones** (quedan registradas con tu usuario y la hora):

- **Reconocer**: marca que ya la estás atendiendo.
- **Resolver**: ciérrala (puedes escribir una nota de qué pasó).
- **Nota**: agrega una observación sin cambiar el estado.
- **Ver cámaras**: salta a las cámaras de ese sitio para verificar qué ocurre.

Cada alarma conserva su **bitácora**: quién la reconoció/resolvió/anotó y cuándo.

## 6. Asistente IA 💬

El botón **💬** (abajo a la izquierda) abre un asistente al que puedes
preguntarle en español sobre **eventos** (detecciones de las cámaras) y
**alarmas**. Ejemplos:

- «¿cuántas personas se detectaron hoy?»
- «¿qué cámara tuvo más actividad anoche?»
- «¿hubo alguna alarma SOS hoy y en qué torre?»

Responde con datos reales de la base; si no hay resultados, lo dice.

## 7. Cerrar sesión

Botón **Salir** en la barra superior. La sesión también caduca sola tras varias
horas.

---

[← Inicio](../README.md) · [Administrador →](administrador.md) · [FAQ](faq.md)
