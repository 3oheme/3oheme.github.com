---
layout: post
title: "Cómo cambiar la altura de un textarea con ckeditor en Drupal"
lang: es
date: 2011-09-16 12:00:00
excerpt: "Los editores WYSIWYG mejoran mucho la usabilidad de las áreas de texto, facilitando al usuario poder insertar código html de forma sencilla."
categories: blog
archived_from: 3oheme.com
---
Los editores [WYSIWYG](https://secure.wikimedia.org/wikipedia/en/wiki/WYSIWYG) mejoran mucho la usabilidad de las áreas de texto, facilitando al usuario poder insertar código html de forma sencilla.

Pero en Drupal esto puede repercutir un poco en el estilo visual de nuestra web, ya que ciertos parámetros (como por ejemplo la altura de estas cajas de texto) están predefinidas (o como se suele decir, **hardcodeadas**) en el módulo, así que siempre tendremos cajas con WYSIWYG del mismo tamaño. Y en el caso concreto del editor [ckeditor](https://drupal.org/project/ckeditor) esta altura es de 420px, enorme en muchos casos.

La solución más limpia para cambiar estos parámetros es añadir un fichero javascript en el theme y cambiar las opciones por defecto que se añaden para el editor ckeditor.

Añadimos el fichero js a nuestro theme con la siguiente línea en el mitheme.info

```php
scripts[] = js/mijavascript.js
```

y luego en el fichero mijavascript.js

```javascript
Drupal.behaviors.MiThemeUserInterface = function(context) {
    Drupal.settings.wysiwyg.configs.ckeditor.format1.height = 100;
    Drupal.settings.wysiwyg.configs.ckeditor.format2.height = 100;
    Drupal.settings.wysiwyg.configs.ckeditor.format3.height = 100;
}
```

Y listo. En este caso hemos reducido la altura de las áreas de texto a 100 píxeles para todos los tipos de formatos de entrada (input formats)

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/como-cambiar-la-altura-de-un-textarea-con-ckeditor-en-drupal).*
