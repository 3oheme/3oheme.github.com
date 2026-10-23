---
layout: post
title: "[html] Usar dos puntos en un ID"
lang: es
date: 2010-06-15 12:00:00
excerpt: "Hoy he aprendido dos cosas en el curro:"
categories: blog
archived_from: 3oheme.com
---
Hoy he aprendido dos cosas en el curro:

- El atributo ID de una etiqueta html puede llevar el carácter "**:**" (dos puntos). Para saber cómo debe estar formado un ID lo mejor es ir [a casa del w3c](http://www.w3.org/TR/html4/types.html#h-6.2).
- Si queremos utilizar ese atributo ID en nuestro CSS debemos escapar el carácter dos puntos de la siguiente forma:  

  ```css
  #elemento\:mola { color: red }
  ```

Nunca te acostarás sin llevarte 15 minutos dándole vueltas a un bug estúpido.

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/html-usar-dos-puntos-en-un-id).*
