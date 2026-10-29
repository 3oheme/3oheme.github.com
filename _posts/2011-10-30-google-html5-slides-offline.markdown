---
layout: post
title: "Google HTML5 slides offline"
lang: es
date: 2011-10-30 12:00:00
excerpt: "Post rápido (como todos últimamente) — Me encantan las slides con html5 que hizo Google para la presentación del Google I/O 2011 y que luego ha liberado en code.google.com. Son limpias, fáciles de mod"
categories: blog
archived_from: 3oheme.com
---
Post rápido (como todos últimamente) — Me encantan las [slides con html5 que hizo Google](http://code.google.com/p/html5slides/ "Slides en html5 de google") para la presentación del [Google I/O 2011](http://www.google.com/events/io/2011/index-live.html) y que luego ha liberado en code.google.com. Son limpias, fáciles de modificar, suaves, estándares y cualquier otra cosa que se le pueda pedir.

**Pero tienen un problema**, y es que carga por http un javascript que es el que hace funcionar todo el sistema. Y como sabemos, es muy probable que, cuando vayas a realizar tu presentación, aparezca el [amigo Murphy](http://upload.wikimedia.org/wikipedia/commons/0/08/LA_LEY_DE_MURPHY.jpg) y te deje sin conexión a internet. Y sin conexión no hay transparencias, y sin transparencias no hay dinero, y sin dinero terminarás en la calle, tirado por algún sitio y ehmm.. bueno, eso.

Así que nada, decidí que había que bajarlo todo a local, y después de un rato ya lo tengo todo funcionando correctamente:

- Las fuentes se han descargado de [google webfonts](http://www.google.com/webfonts), se han transformado con el [fontsquirrel fontface generator](http://www.fontsquirrel.com/fontface/generator), y se han insertado vía @fontface
- Se han dejado en local todos los javascript y los css
- Y por último se han añadido unas imágenes preciosas por defecto para logo y logo-small :-D

Listo. [Lo dejo por aquí](https://web.archive.org/web/2011/http://www.3oheme.com/sites/www.3oheme.com/files/google-html5slides.zip "¡Vamos, descárgalo, no seas tonto!") para que nadie tenga que rehacer todo el trabajo.

¡Un saludo!

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/google-html5-slides-offline).*
