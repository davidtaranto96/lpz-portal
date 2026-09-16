# Portal de Luis López — LPZ Propiedades

> Documento de arranque de sesión. Creado el **2026-09-16**.

## Qué es esto

El sitio público de **Luis López**, que va a publicar sus propiedades como hoy lo hace
`franciscomolins.com` con las de Francisco Molins.

**Es el espejo del portal de Fran, con Luis de principal** (ver la tabla más abajo). Sale de
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

## Cómo es respecto del portal de Fran

**Es su espejo.** Lo pidió David el 16/9: la misma plataforma, con Luis de principal.

| | Portal de Fran | Portal de Luis |
|---|---|---|
| Marca grande, arriba a la izquierda | escudo de Molins + «Francisco Molins» | escudo de LPZ + «Luis López» |
| Logo del socio, a la derecha (barra y pie) | Grupo LPZ, va al WhatsApp de Luis | escudo de Molins (`img/escudo-molins.png`, a color), va al WhatsApp de Fran |
| WhatsApp y teléfono de todo el sitio | 387 415 3669 | 387 503 0113 |
| Pie | Molins · Negocios inmobiliarios | LPZ · Propiedades |
| Oportunidades | Aires y La Torre | **sólo Aires**: Luis no comercializa La Torre |
| Contacto, Preguntas, terrenos, propiedades | — | iguales a los de Fran, por ahora |

### Lo que lo separa del de Fran a simple vista (16/9, segunda vuelta)

David: que se parezcan pero no sean iguales, para que no se confunda la gente ni ellos mismos.

- **Paleta de la marca de Luis**: carbón (`--verde: #2B2825`, `--verde-noche: #1B1917`), naranja de
  la corona (`--naranja: #F07318`) y fondo piedra (`--hueso: #F4F3F0`). **Los nombres de los tokens
  siguen siendo los del portal de Fran** («verde» es el carbón): se cambió el valor, no el nombre,
  para no tocar cientos de reglas. Los `rgba()` verdes escritos a mano se pasaron a carbón.
- **Tipografía**: Besley (títulos, una Clarendon sólida como las letras del logo) y Hanken Grotesk
  (texto). Fran usa Libre Caslon Text y Archivo. Besley es más ancha: «OPORTUNIDADES» en el celular
  toma el cuerpo del ancho disponible.
- **Portada más baja, con una casa en video**: 60svh en escritorio y 52svh en el celular, **para que
  las propiedades asomen apenas se abre la página** (lo pidió Luis). El video es una casa quinta con
  pileta vista desde un dron: los portales grandes venden una casa (Toribio Achával pone un video de
  una propiedad, Compass una casa con las luces prendidas) y los de Salta, un paisaje con el
  buscador (NMS, Zumar, LV y Carina Nuñez usan la misma plantilla). David aceptó que sea genérico
  si es bueno.
  - Fuente: Coverr, «House on a hill in Alentejo, Portugal», licencia de Coverr (uso comercial,
    sin atribución). **Mixkit se descartó**: sus tomas de casas buenas tienen la licencia
    restringida, que no permite uso comercial.
  - Se usan los primeros 3 s (después el dron se va al valle y aparece una persona), desacelerados
    1,5 veces con `minterpolate` y en ida y vuelta, así el loop no salta: 8,9 s.
  - Dos cortes: `video/portada-casa.mp4` (1600×720, 1,6 MB) y `video/portada-casa-movil.mp4`
    (648×720, 0,8 MB), con sus pósters `img/portada-casa*.webp`. Los carga el cargador de videos
    de `app.js` (el mismo de Aires) recién cuando se ven; el del otro ancho está oculto y no se baja.
    Con `prefers-reduced-motion` o ahorro de datos queda el póster.
  - El velo oscurece arriba y al centro y deja los bordes claros: el video es de día.
- **Buscador con pestañas** (16/9, tercera vuelta, «inspirarse en la competencia»): arriba de una
  tarjeta blanca, las pestañas Todas · Comprar · Alquilar · Terrenos con la cantidad de cada una
  (`pestanasBusca` en `app.js`), como Noman, NMS, Carina Nuñez o Compass. Reemplazan el desplegable
  de operación, que queda oculto. Botón «Buscar» rectangular y carbón. Pegado bajo la barra, las
  pestañas se apagan y el `top` resta `--pest-h`: esconderlas cambiando el alto haría saltar la página.
- **Texto de la portada**: «Tu próxima propiedad en Salta» y «Casas, terrenos y alquileres ·
  Corredor matriculado CUCIS 251» (en el celular, en dos líneas sin el punto). Los botones son menos
  redondeados que las píldoras de Fran, y el de la barra dice «Buscar propiedades».
- **Cierre naranja** (16/9): «¿Buscás algo que no está publicado?» en un bloque naranja de la marca
  con texto carbón, botones «Hacer una consulta» (carbón) y «Escribir por WhatsApp» (blanco). En el
  de Fran es una tarjeta oscura con «Escribinos». El pie lleva una línea naranja arriba.
- **Aires es una tarjeta aparte**, con bordes redondeados y margen, y la hoja de contacto ya no la
  tapa al bajar (en el de Fran se apilan).
- Todo eso vive en el bloque «LPZ Propiedades: lo que lo separa del portal de Fran», al final del
  `<style>` del `index.html`.

Lo que se sacó por La Torre: el bloque, la entrada del menú (escritorio y celular), el enlace del
pie, la opción «Edificio La Torre» del formulario, `torres/`, sus videos y renders. En `app.js` la
carga de las unidades sólo corre si existe `.bloque--torre`, y el apilado de los bloques se arma
con los que haya (sin La Torre, la hoja de contacto tapa directo a Aires).

Lo que sigue igual a propósito:

- **La oficina, 20 de Febrero 1705, Of. 7.** En los documentos del proyecto figura como la de
  Grupo LPZ-Molins. Confirmar con Luis.
- **La matrícula**: «Grupo LPZ-Molins · CUCIS 251 · Corredor matriculado Luis López».
- **Las carteras que se publican** (`propia,alquileres`): son las mismas propiedades que en el de Fran.

## Lo que falta

- **Instagram**: se sacó (el que había era la cuenta de Molins). Falta el de Luis.
- **`MOLINS_CLAVE` vacía.** La que venía era la del sitio de Fran: con ella las visitas de acá se
  contaban en su pantalla de Cookies y las consultas caían en su cartera. Sin clave, el formulario
  contesta «No pudimos enviar la consulta» y ofrece WhatsApp. **Nunca ponerle la clave de Fran.**
- **Sin indexar**: `noindex` en el `index.html` y `robots.txt` con `Disallow: /`, hasta que tenga
  dominio propio.

**Lo que se hace en el CRM y no acá** (desde la sesión de `crm-molins/app`): la clave de sitio de
Luis, y el modelo de «un portal por dueño» que planteó David el 16/9. Está en
`crm-molins/docs/plan/portales-de-fran-y-luis.md`.

## La marca

- `extras/marca-original/maqueta-pared-clara.jpg` y `-oscura.jpg`: las dos imágenes que mandó
  (llegaron por WhatsApp el 1/9). **Son maquetas en 3D sobre una pared, no el logo.**
- Los logos planos se armaron a partir de ellas:
  - `img/logo-lpz-propiedades.png`: completo, letras gris cálido, para fondo claro.
  - `img/logo-lpz-propiedades-claro.png`: completo, letras claras, para fondo oscuro.
  - `img/escudo-lpz.png`: cuadrado de 320 px, corona y LPZ sobre carbón. Ocupa el lugar del escudo
    de Molins.
  - `img/escudo-molins.png`: el escudo de Fran recortado de su cuadrado, con fondo transparente,
    para el lugar del socio.
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
