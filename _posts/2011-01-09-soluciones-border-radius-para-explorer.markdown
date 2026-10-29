---
layout: post
title: "Soluciones border-radius para Explorer"
lang: es
date: 2011-01-09 12:00:00
excerpt: "Después de probar varias soluciones para implementar border-radius en internet xplorer (especialmente IE7 e IE8, porque a IE6 le pueden ir dando ya por c***) os traigo mi veredicto:"
categories: blog
archived_from: 3oheme.com
---
Después de probar varias soluciones para implementar **border-radius** en [internet xplorer](http://msdn.microsoft.com/en-us/library/bb250413%28v=vs.85%29.aspx "Vaya telita con hasefroch...") (especialmente IE7 e IE8, porque a IE6 le pueden ir dando ya por c\*\*\*) os traigo mi veredicto:

## Nada, no hay manera

Básicamente porque:

- [CurvyCorners](http://www.curvycorners.net/ "CurvyCorners") no funciona muy fino: con ejemplos simples no hay problema, pero cuando tiene que enfrentarse a una página de cierto tamaño (y recordemos que Drupal, out-of-the-box, sufre de divitis aguda) parece que recorre mal el DOM, se hace la picha un lío y se deja cosas sin curvar. Y [CSS3PIE](http://css3pie.com/) tres cuartos de lo mismo :-P
- [DD_roundies](http://www.dillerdesign.com/experiment/DD_roundies/ "dd roundies") parecía muy prometedor, pero falla en una feature imprescindible para mí: no tiene soporte para PNG, con lo cual, si nuestro div contiene elementos con un png de imagen de fondo (o el mismo div al que le aplicamos el rounded corners) los PNG o se renderizan sin transparencia o, directamente, no se renderiza.
- Otras técnicas aplican soluciones que añaden un montón de html y solo funcionan con fondos de color uniforme, o directamente renderizan mal el modelo de caja, aparecen bugs raros...

Así que, si vuestra aplicación web necesita verse correctamente en IE7-8 os recomiendo pasar de **-moz-border-radius** y demás (que por otro lado no son ni estándar) y seguir utilizando imágenes de fondo para simular curvas y demás.

Ea, un saludo.

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/soluciones-border-radius-para-explorer).*
