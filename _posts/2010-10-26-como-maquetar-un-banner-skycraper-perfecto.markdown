---
layout: post
title: "Cómo maquetar un banner skyscraper ferpecto"
lang: es
date: 2010-10-26 12:00:00
excerpt: "¡Hola a todos y bienvenidos a bricoheme ! En el programa de hoy explicaremos cómo maquetar correctamente banners de tipo skyscraper, respetando SEO, accesibilidad y controlando el ancho de la página, "
categories: blog
archived_from: 3oheme.com
---
¡Hola a todos y bienvenidos a **bricoheme**! En el programa de hoy explicaremos cómo maquetar correctamente banners de tipo skyscraper, respetando SEO, accesibilidad y controlando el ancho de la página, para que no aparezca el temido scroll horizontal.

Pero vayamos por partes

## ¿Cómo es un banner skyscraper?

Los banner skyscraper, a menos que me equivoque :-P, son los banners que aparecen en los laterales de la página web **pero por fuera**, es decir, no se colocan dentro del flujo normal de la página, ni en las columnas laterales, sino fuera por completo. Tenemos un ejemplo en la [imagen que acompaña este post](https://web.archive.org/web/2011/http://www.3oheme.com/sites/www.3oheme.com/files/skycraper_marca.jpg "Ejemplo de la web marca.com"). ¿Lo pillas? Pues seguimos.

## Pues yo no veo tan complicado maquetar eso...

Ya, eso es lo que dicen todos :-D colocar ahí los elementos no es complicado. La gracia es que, colocando ahí el banner, la página no gane en anchura. Es decir, si nuestra página tiene una anchura fija de 960px y colocamos dos skyscraper de 200px de ancho, la idea es que un usuario con un monitor de 1024 no vea barras de scroll.

## ¡Ostras, que guapo!

Ya, ya lo sé, es lo que dicen todos. Siguiendo la maquetación que veremos en la demo, podemos colocar banners del tamaño que queramos, ya que es independiente de la anchura. Además los banners irán después del contenido, lo cual es bueno para SEO (el contenido siempre es lo primero) y para accesibilidad (es más rápido y cómodo para navegar con un browser adaptado).

La explicación la haré tomando como ejemplo el banner izquierdo. Para el derecho será igual pero al revés :-D: El truco es colocar el banner en un div con 0px de anchura, y luego flotar la imagen al lado contrario a donde se coloque el banner, en este caso a la derecha, así pegamos el banner al lado que queramos. Luego colocamos el div de 0px con posición absoluta y el atributo right a la anchura de la web más el espacio que queramos dejar entre el content y el banner. Y listo.

El código resumido sería así:

```html4strict
<div id="page">
  <div style="position: relative; width: 900px">
    Contenido principal de la web
  </div>
  <div style="width: 0; top: 0; right: 920px; position: absolute">
    <a style="float: right" href="#">
      <img src="banner.jpg" />
    </a>
  </div>
</div>
```

El código está probado para Firefox, Chrome y Explorer 8. Luego probaré los demás navegadores (especialmente IE6/7, que probablemente necesiten hacks)

Poco más, os dejo con la demo, espero cualquier duda en los comentarios :-D

[ver demo](https://web.archive.org/web/2011/http://www.3oheme.com/sites/www.3oheme.com/files/skyscraper/skyscraper.html "demo de banner skyscraper")

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/como-maquetar-un-banner-skycraper-perfecto).*
