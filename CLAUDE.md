# Portal de Luis López — LPZ Propiedades

> Documento de arranque de sesión. Creado el **2026-09-16**.

## Qué es esto

El sitio público de **Luis López**, que va a publicar sus propiedades como hoy lo hace
`franciscomolins.com` con las de Francisco Molins.

**Por ahora es una copia exacta del portal de Fran con la marca de Luis.** Sale de
`~/Documents/DT-System/crm-molins/portal` (repo `molins-portal`), commit `661a038` del 11/9, sin su
historial. Todo lo que lo vuelva de Luis se hace acá, en sesiones propias, para no cargar las de Fran.

HTML estático, un solo archivo (`index.html`), sin build. Las propiedades no están escritas acá:
se leen del CRM, que **es el mismo sistema de Fran** (`crm.franciscomolins.com`). Luis y Fran
comparten el CRM; lo que separa a uno del otro es la cartera.

## Quién es Luis

- **Luis López**, corredor inmobiliario con cartera propia (López Propiedades) y socio de Francisco
  en Aires de San Lorenzo. No es un empleado de Fran.
- Teléfono y WhatsApp: **387 503 0113** (`wa.me/5493875030113`).
- La comercializadora es **Grupo LPZ-Molins · CUCIS 251**, y el corredor matriculado es Luis. Se
  escribe así, en ese orden: lo corrigió Francisco el 1/9 porque en las webs decía «LPZ Grupo y
  Molins» y «CUCIS MP 251».
- En el CRM es administrador, con las carteras Aires, propia, alquileres y `alquileres-luis` (la
  planilla de sus alquileres). **No tiene La Torre.** Al 15/9 todavía no se le había entregado el
  acceso.

## Lo que ya se cambió respecto del portal de Fran (16/9)

- **Marca**: el escudo de Molins (seis lugares) pasó a `img/escudo-lpz.png`, el ícono de la pestaña
  es una L naranja sobre carbón y la vista previa al compartir es `img/og-lpz.jpg`.
- **No se indexa**: `<meta name="robots" content="noindex, nofollow">` en el `index.html` y
  `robots.txt` con `Disallow: /`. Un duplicado del sitio de Fran en Google le compite a él. Se saca
  el día que el sitio tenga sus textos y su dominio.
- **Sin `CNAME` ni `sitemap.xml`**: eran de `franciscomolins.com`.
- **`MOLINS_CLAVE` vacía.** La que venía era la del sitio de Fran: con ella cada visita de acá se
  contaba en su pantalla de Cookies y cada consulta caía en su bandeja y entraba en la rueda de
  reparto. Sin clave, el formulario contesta «No pudimos enviar la consulta» y ofrece WhatsApp, y no
  se mide nada. **Hasta que exista la clave de Luis no se prueba el formulario con otra clave.**

## Lo que todavía es de Fran

La lista para convertirlo, con cómo encontrar cada cosa:

| Qué | Dónde | Estado |
|---|---|---|
| Nombre «Francisco Molins» y «Real estate · Salta» | `grep -n "Francisco" index.html` (12 líneas) | de Fran |
| WhatsApp y teléfono de Fran, 387 415 3669 | `grep -n "3874153669\|387 415 3669" index.html` (10 lugares) | de Fran |
| Marca «Molins · Negocios inmobiliarios» en el pie | `grep -n "Negocios inmobiliarios" index.html` (2) | de Fran |
| Dirección de la oficina de Fran, 20 de Febrero 1705 | `grep -n "20 de Febrero" index.html` (3) | de Fran; **no inventar la de Luis**, pedirla |
| Instagram `molins.negociosinmobilarios` | `grep -n "instagram.com" index.html` (2) | de Fran |
| `<title>`, `description`, `og:title`, `og:description` | cabecera del `index.html` | de Fran |
| Paleta verde noche (`--verde: #113C3D`) | `src/estilos.css` y el `<style>` del index | de Fran |
| Foto de portada, el estudio de su web actual | `img/portada-estudio.webp` y `-movil.webp` | de Fran |
| Carteras que se publican: `propia,alquileres` | `window.MOLINS_CARTERA` | de Fran |
| Clave del sitio | `window.MOLINS_CLAVE` | vacía, falta la de Luis |
| Logo de Grupo LPZ a la derecha de la barra y en el pie, con enlace al WhatsApp de Luis | `.barra__lpz`, `.pie__lpz` | decidir si queda |
| Oportunidades: Aires y La Torre | bloques de proyectos | Luis no tiene La Torre |
| `torres/` redirige al sitio de La Torre | carpeta `torres/` | decidir |
| Preguntas frecuentes y textos de Contacto | pop-ups `#preguntas` y `#contacto` | escritos para Fran |

Lo que sirve igual y no hace falta tocar: `admin/`, `crm/` y `sistema/` redirigen al CRM, que es
el mismo para los dos. Las cookies se llaman `molins_consent` y `molins_vid` y las variables
`MOLINS_*`; renombrarlas es opcional y, si se hace, va en `src/medicion.js` y en el `index.html` a
la vez.

**Dos cosas que se piden en el CRM y no acá** (se hacen desde la sesión de `crm-molins/app`):

1. La **clave de sitio** de Luis: CRM → Admin → Carteras → Sitios, sobre su cartera.
2. Qué **carteras** publica. Hoy las suyas son `alquileres-luis` y, cuando exista, su cartera
   propia. Una propiedad sale en la web sólo si en el CRM está marcada para la web (`enWeb`).

## La marca

- `extras/marca-original/maqueta-pared-clara.jpg` y `-oscura.jpg`: las dos imágenes que mandó
  (llegaron por WhatsApp el 1/9). **Son maquetas en 3D sobre una pared, no el logo.**
- Los logos planos se armaron a partir de ellas:
  - `img/logo-lpz-propiedades.png`: completo, letras gris cálido, para fondo claro.
  - `img/logo-lpz-propiedades-claro.png`: completo, letras claras, para fondo oscuro.
  - `img/escudo-lpz.png`: cuadrado de 320 px, corona y LPZ sobre carbón. Ocupa el lugar del escudo
    de Molins.
  - `img/og-lpz.jpg`: 1200 × 630, para la vista previa de WhatsApp.
- **Son una reconstrucción.** La corona y las letras LPZ son el mismo dibujo del logo de Grupo LPZ
  (`img/logo-lpz.png`), recoloreado con los colores medidos en la maqueta; «PROPIEDADES» está
  compuesto en Optima Bold, lo más parecido que trae el sistema. **Si Luis tiene el archivo
  original (vector o PNG plano), reemplaza a estos.** Se regeneran con
  `extras/marca-original/armar-logos.py`.
- Colores medidos: naranja `#F37A1F`, carbón `#2E2C28`, gris metal `#8E877F`.

## Deploy

GitHub Pages desde `main`: `git push` es el deploy. Dirección:
`https://davidtaranto96.github.io/lpz-portal/`. Dominio propio: no hay todavía. Si se agrega,
también cambian `og:url`, `canonical` y `og:image`, que hoy apuntan a esa dirección.

Los scripts y la hoja de estilos se versionan por query (`?v=`) al publicar, igual que en el de Fran.

**El git de macOS está caído** («You have not agreed to the Xcode license agreements»): usar
`/Library/Developer/CommandLineTools/usr/bin/git` hasta que David corra
`sudo xcodebuild -license accept`.

## Qué NO tocar desde acá

| Ruta | Por qué |
|---|---|
| `~/Documents/DT-System/crm-molins/portal` | Es el portal de Fran, publicado en `franciscomolins.com`. |
| `~/Documents/DT-System/crm-molins/app` | Es el CRM de los dos, en producción. Lo que Luis necesite del sistema se anota y se hace desde esa sesión. |

## Cómo está hecho por dentro

Lo que el portal de Fran aprendió en diecisiete rondas de correcciones está documentado en el
`CLAUDE.md` de `crm-molins` (sección «Portal de Fran») y en su `README.md`. Tres cosas que muerden:

- Los `data-si` rinden `display:contents`: lo que lleva estilo va envuelto.
- Las listas con `data-clave` reusan la fila cuya clave se repite; sin eso cada repintado recrea las
  fotos y la página parpadea.
- `overflow:hidden` en un ancestro mata el `position:sticky`, y el apilado de los bloques depende de
  eso.
