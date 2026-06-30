# Manual de usuario — SecureVu Map

**SecureVu Map** es el mapa de monitoreo de cámaras de videovigilancia. Muestra
cada cámara sobre un mapa, su estado en vivo (en línea / fuera de línea), el
video en tiempo real, la disponibilidad histórica y las alarmas de pánico (SOS)
y sabotaje (Tamper) que reportan los sitios.

Este manual está dividido por rol:

- 👤 **[Guía del usuario (visor)](docs/usuario.md)** — ver el mapa, las cámaras,
  el video, las alarmas y el asistente.
- 🛠️ **[Guía del administrador](docs/administrador.md)** — además de todo lo
  anterior: configurar servidores, subir coordenadas, gestionar usuarios y el
  asistente IA.
- ❓ **[Preguntas frecuentes](docs/faq.md)**

---

## Acceso

1. Abre la dirección de la aplicación que te compartió tu administrador (por
   ejemplo `https://mapa.tu-organizacion`). Si el navegador muestra una
   advertencia de certificado en una instalación interna, continúa (es un
   certificado propio de tu red).
2. Inicia sesión con tu **usuario** y **contraseña**.
3. Según tu rol verás más o menos opciones:

| Rol | Puede |
|---|---|
| **Visor** | Ver el mapa, el video de las cámaras, la disponibilidad, las alarmas y el asistente. |
| **Administrador** | Todo lo del visor **más** la sección de Administración (servidores, coordenadas, usuarios, asistente). |

> ¿Olvidaste tu contraseña? Pídele a un administrador que la restablezca desde
> **Administración → Usuarios**.

---

## Un vistazo rápido a la pantalla

- **Barra superior**: título, contadores de cámaras (clic para ver
  **estadísticas de disponibilidad**), filtros (**Servidor** y **Tipo**),
  buscador, 🔔 **alarmas**, ⚙ **administración** (solo admin) y **Salir**.
- **Mapa**: un marcador por sitio/torre. El color indica el estado del grupo de
  cámaras de esa ubicación.
- **Panel derecho**: aparece al hacer clic en un marcador; muestra el video y los
  datos de la cámara.
- **💬 Asistente** (abajo a la izquierda): preguntas en lenguaje natural sobre
  eventos y alarmas.

Continúa con la **[Guía del usuario](docs/usuario.md)**.
