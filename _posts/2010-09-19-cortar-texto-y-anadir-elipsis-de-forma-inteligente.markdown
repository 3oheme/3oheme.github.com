---
layout: post
title: "Cortar texto y añadir elipsis de forma inteligente"
lang: es
date: 2010-09-19 12:00:00
excerpt: "Primer post pseudo técnico sobre drupal, yuhu! 3oh colabora con la comunidad!"
categories: blog
archived_from: 3oheme.com
---
**Primer post pseudo técnico sobre drupal, yuhu! 3oh colabora con la comunidad!**

En muchas ocasiones nos vemos en la necesidad de recortar texto desde código, bien porque estamos formateando una view, porque estamos imprimiendo a mano campos CCK o por cualquier otra razón, y no queremos que sobrepase de cierto número de caracteres.

En estos casos se suele utilizar la función [substr](http://php.net/manual/es/function.substr.php) de PHP, que nos devuelve los primeros n caracteres de un string. Peeero esta función no tiene en cuenta si estamos cortando un string con código HTML dentro, o si está cortando una palabra por la mitad, ni añade una elipsis (los tres puntos) en el caso de que hayamos recortado.

Solución: utilizar la función [views_trim_text](http://api.lullabot.com/views_trim_text/7 "descripción de la función views_trim_text, gracias a lullabot"); con esta función podremos advertir que trabajamos con texto HTML, añadir elipsis (solo cuando el texto se recorte), no cortar ninguna palabra, etc...

Y ahora un par de ejemplos. Imaginemos que tenemos la siguiente cadena:

`$cadena = 'En un lugar de la <strong>Mancha</strong>, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor.'`

Probando diferentes parámetros, obtenemos las siguientes salidas:

```php
views_trim_text(
  array(
    'max_length' => 20,
    'word_boundary' => true,
    'ellipsis' => true,
    'html' => true),
  $cadena);
// (output) 'En un lugar de la...'
```

Recorta el texto perfectamente. Vamos a ponerle en un aprieto...

```php
views_trim_text(
  array(
    'max_length' => 40,
    'word_boundary' => false,
    'ellipsis' => true,
    'html' => true),
  $cadena);
// (output) 'En un lugar de la <strong>Manc...</strong>'
```

¡Perfecto! Nos respeta el strong y además corta la palabra por la mitad.

*Nota: esta función solamente la podremos utilizar si tenemos instalado en nuestro sistema el módulo views, pero vaya, si en tu instalación Drupal no usas views, mal vamos...*

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/cortar-texto-y-anadir-elipsis-de-forma-inteligente).*
