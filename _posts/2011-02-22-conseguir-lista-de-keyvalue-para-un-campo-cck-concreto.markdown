---
layout: post
title: "Conseguir lista de key|value para un campo CCK concreto"
lang: es
date: 2011-02-22 12:00:00
excerpt: "Muy sencillo: si nuestro campo se llama 'field_categoria' solo tenemos que hacer lo siguiente:"
categories: blog
archived_from: 3oheme.com
---
Muy sencillo: si nuestro campo se llama 'field_categoria' solo tenemos que hacer lo siguiente:

```php
$field = content_fields('field_categoria');
$values = content_allowed_values($field);
```

Y listo. En la variable $values tenemos un array con los diferentes valores que puede coger ese campo CCK (gracias a [Jacinto](http://www.jacintocapote.com/) por la ayuda)

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/conseguir-lista-de-keyvalue-para-un-campo-cck-concreto).*
