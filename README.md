# Portal LPZ Propiedades

Sitio público de Luis López. **HTML estático, un solo archivo**, sin build.

Arrancó el 16/9/2026 como copia del portal de Francisco Molins (`molins-portal`) con la marca de
Luis. El estado, lo que falta convertir y las reglas están en `CLAUDE.md`.

Las propiedades se leen del CRM (`GET /api/publico/propiedades?cartera=...`) y las consultas entran
por `POST /api/publico/consultas` con la clave del sitio.

## Configuración

Tres valores al principio de `index.html`, en `window.MOLINS_*`:

| Variable | Qué es | Valor |
|---|---|---|
| `MOLINS_API` | URL del CRM | `https://crm.franciscomolins.com` |
| `MOLINS_CARTERA` | carteras que se publican, separadas por coma | `propia,alquileres` (las de Fran, falta cambiar) |
| `MOLINS_CLAVE` | clave del sitio (header `x-sitio-clave`) | vacía hasta que el CRM genere la de Luis |

## Deploy

GitHub Pages desde `main`. `git push` es el deploy.

## Créditos

El video de portada (`video/portada-casa*.mp4`) sale de Coverr, «House on a hill in Alentejo,
Portugal», con la licencia de Coverr: uso comercial libre, sin atribución. Se anota igual.
