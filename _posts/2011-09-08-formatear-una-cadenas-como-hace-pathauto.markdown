---
layout: post
title: "Formatear una cadenas como hace pathauto"
lang: es
date: 2011-09-08 12:00:00
excerpt: "Mini truco Drupal: hay veces en los que debemos transformar las cadenas para que sean seguras para el path (o para cualquier otra situación)."
categories: blog
archived_from: 3oheme.com
---
Mini truco Drupal: hay veces en los que debemos transformar las cadenas para que sean seguras para el path (o para cualquier otra situación).

Para ello, lo mejor es utilizar la mismas funciones que utiliza pathauto, como vemos en el siguiente ejemplo:

```php
module_load_include('inc', 'pathauto');
$output_limpio = pathauto_cleanstring("Mi cadena joía!");
```

PD: Mil gracias a @jacintocapote que me informó del trick

PD2: Luego contaré para qué me ha hecho falta esto :-P

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/formatear-una-cadenas-como-hace-pathauto).*
