---
layout: post
title: "Power PNG layers, imágenes de fondo con css realmente grandes"
lang: es
date: 2010-01-06 12:00:00
excerpt: "Hu há! el otro día, visitando la página de los premios grammy (hecha en Drupal , por cierto) me fijé en la imagen de fondo tan chula y atractiva que tiene. En serio, entrad y echadle un vistazo , que "
categories: blog
archived_from: 3oheme.com
---
Hu há! el otro día, visitando la [página de los premios grammy](http://www.grammy.com/) (hecha en [Drupal](http://drupal.org/), por cierto) me fijé en la imagen de fondo tan chula y atractiva que tiene. En serio, [entrad y echadle un vistazo](http://www.grammy.com/), que si no este tutorial no tiene gracia :-D. Observad como cuando vais bajando va cambiando el tono de la imagen con un degradado multicolor super petero.

Bueno, esto no tiene mucha miga. No sería la primera página web con una imagen de fondo enoooooorrrrme (tanto en resolución como en tamaño en disco), y si tuviera tiempo y ganas y me pagárais por ello os buscaría varios ejemplos, pero como no es el caso os fiaréis de mí y seguiremos con los power png layers :-) La gracia de todo este asunto es que la imagen de fondo ocupa simplemente 23KB.

¿Cóoooomo? ¿Una imagen de 1800 por 3000 con esa calidad y esos degradados solo ocupa 23KB? Una imagen normal, de ese tamaño y con esas características simplemente en JPG ocuparía aproximadamente 1MB, lo cual comparativamente sería como meter el volumen de un campo de fútbol en el espacio de un ipod, o comprimir toda la enciclopedia británica en menos de 20 segundos. Tan sorprendente como poco creíble, así es.

Vamos, dímelo ya... ¿cómo lo hace? Pues muy fácil. Jugando con un fondo de 3 divs y 3 imágenes distintas :-D Vaaaaaamos con la explicación.

El html que tenemos es el siguiente:

```html4strict
<div id="a">
  <div id="b">
    <div id="c">
      Contenido principal y tal
    </div>
  </div>
</div>
```

En la capa del fondo (id=a) ponemos una imagen de fondo (por ejemplo, una parecida a [la que utilizan los grammy](http://www.grammy.com/sites/all/themes/grammys_52/images/page_background_tile.jpg)), y hacemos que se repita (tileable que se decía en mi época), consiguiendo el siguiente efecto:  
  
  
  
Feo, tremendamente feo. Además, podemos observar como se nota que se ve que se aprecia que el fondo se repite. En fin, que seguimos, que ahora empieza lo bueno: colocamos en la segunda capa (id=b) el [png con transparencia super tunning marca acme](http://www.grammy.com/sites/all/themes/grammys_52/images/page_background_vertical.png) y hacemos que se repita (tileable que se decía en mi época), quedando así de chachi:  
  
  
  
¡Oleeeee como molaaa! Con esto conseguimos darle una bocanada_de_aire_fresco™ a la imagen de fondo, cuesta mucho más apreciar el patrón que se repite y empezamos a darle ese toque surferillo que tanto les gusta a las mujeres hoy en día. Por último, en la tercera capa (id=c) colocamos el [segundo png super fetén-se-me-acaban-los-adjetivos](http://www.grammy.com/sites/all/themes/grammys_52/images/page_background_horizontal.png), que marcará la zona principal de la web. Esta imagen irá centrada horizontalmente y se repetirá verticalmente  
  
  
  
¡Ayomá que rica! Recordad que podéis hacer los degradados con cualquier software de edición de imagen como GIMP o deluxe paint II, dando cierta transparencia al degradado y guardando como png. El truco se explicaría con el siguiente gráfico:  
  
  
  
Y el CSS correspondiente sería tal que así:

```css
#a { background: url(background_tileable.jpg) }
#b { background: url(background_vertical.jpg) }
#c { background: url(background_horizontal.jpg) repeat-x center center }
```

Fácil, ¿no? Dudas, comentarios o mejoras serán bienvenidas :-D

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/power-png-layers-imagenes-de-fondo-con-css-realmente-grandes).*
