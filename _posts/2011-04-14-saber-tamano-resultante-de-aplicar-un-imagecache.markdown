---
layout: post
title: "Saber tamaño resultante de aplicar un imagecache"
lang: es
date: 2011-04-14 12:00:00
excerpt: "Rápido miniquick_post drupal theming"
categories: blog
archived_from: 3oheme.com
---
**Rápido miniquick_post drupal theming**

A veces necesitamos saber el tamaño de una imagen después de aplicar un preset de [imagecache](http://drupal.org/project/imagecache), sobre todo al aplicar presets que no sean crop, sino scale (esto nos puede resultar útil para maquetar listados en los que no sepamos el tamaño de la imagen)

Para ello simplemente debemos hacer lo siguiente, y tendremos el tamaño en el array $size.

```php
$size = image_get_info(imagecache_create_path($presetname, $path));
print $size['width']; // anchura de la imagen resultante
print $size['height']; // altura de la imagen resultante
```

Fácil y rápido :-)

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/saber-tamano-resultante-de-aplicar-un-imagecache).*
