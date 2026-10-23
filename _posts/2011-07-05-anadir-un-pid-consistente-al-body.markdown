---
layout: post
title: "Añadir un PID consistente al body"
lang: es
date: 2011-07-05 12:00:00
excerpt: "Hay veces que resulta útil añadir un identificador único a la página (page id) que estamos viendo, independientemente del idioma en la que la visualicemos."
categories: blog
archived_from: 3oheme.com
---
Hay veces que resulta útil añadir un identificador único a la página (page id) que estamos viendo, independientemente del idioma en la que la visualicemos.

Para conseguir esto no tenemos más que añadir el siguiente código - suponiendo que estamos trabajando en un entorno en el que el idioma principal es el español:

```php
   if ($vars['node']) {
     if ($vars['node']->language == 'es') {
       $vars['body_id'] = 'pid-' . strtolower(preg_replace('/[^a-zA-Z0-9-]+/', '-', drupal_get_path_alias('node/'. $vars['node']->nid)));
     }
     else {
       $node_es = db_result(db_query("SELECT nid FROM {node} WHERE tnid=%d AND language='es'", $vars['node']->tnid));
       $vars['body_id'] = 'pid-' . strtolower(preg_replace('/[^a-zA-Z0-9-]+/', '-', drupal_get_path_alias('node/'. $node_es, 'es')));
     }
   }
```

Y luego utilizar ese $vars['body_id'] donde necesitemos (normalmente será en la etiqueta body).

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/anadir-un-pid-consistente-al-body).*
