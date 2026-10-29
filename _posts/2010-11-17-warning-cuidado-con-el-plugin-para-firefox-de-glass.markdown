---
layout: post
title: "Warning! cuidado con el plugin para Firefox de Glass"
lang: es
date: 2010-11-17 12:00:00
excerpt: "Antes que nada la versión corta del post:"
categories: blog
archived_from: 3oheme.com
---
Antes que nada la versión corta del post:

**Si eres webdeveloper, mucho cuidado con el plugin para Firefox de Glass, porque interfiere con el funcionamiento correcto de firebug y añade clases y CSS que provocan errores en la visualización de las páginas.**

[Glass](https://www.writeonglass.com/) es una nueva red social, fundada por antiguos trabajadores de Google, que se mueve en el rollo de poder dejar comentarios a tus colegas en cualquier web (en el [vídeo demostrativo](http://www.youtube.com/watch?v=VBEXqVmiySE) explican el concepto, que por otro lado no es nada nuevo, ver [google sidewiki](http://www.google.com/sidewiki/intl/es/#tbbrand=GZEV), [reframeit](http://reframeit.com/) o [komenti](http://komenti.org/)).

El problema viene en que el plugin de Glass añade marcado html+css a cualquier web que visitemos, y en el último desarrollo que he realizado en [Alquimia](http://al.quimia.net/) he encontrado que ese marcado hace que las imágenes que apliques sobre el body con css den problemas al ajustarlas con **bottom left**. Sí, un issue bien raro, pero que te puede tener 10 minutos peleándote con el código hasta que des con la fuente del error.

Así que ya sabéis, **si sois desarrolladores web al plugin de Glass le pueden ir dando por culo**.

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/warning-cuidado-con-el-plugin-para-firefox-de-glass).*
