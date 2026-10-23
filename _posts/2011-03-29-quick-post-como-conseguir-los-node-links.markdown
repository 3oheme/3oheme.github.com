---
layout: post
title: "Quick post - cómo conseguir los $node->links"
lang: es
date: 2011-03-29 12:00:00
excerpt: "mini quick post de node->links, corre!"
categories: blog
archived_from: 3oheme.com
---
mini quick post de node->links, corre!

**Un post rápido pero muy útil si necesitas los links y no los tienes o la variable que obtienes no tiene los links correctamente generados**: Si necesitas obtener los enlaces relacionados de un nodo (los famosos **$node->links** o **$links** dentro del [node.tpl.php](http://api.drupal.org/api/drupal/modules--node--node.tpl.php/6)) puedes hacerlo desde cualquier sitio con las siguientes dos líneas:

```php
$node->links = module_invoke_all('link', 'node', $node, $teaser);
drupal_alter('link', $node->links, $node);
```

Y si no tienes el $node y quieres el nodo actual, solo tienes que hacer:

```php
$node = menu_get_object();
$node->links = module_invoke_all('link', 'node', $node, $teaser);
drupal_alter('link', $node->links, $node);
```

Mil gracias a [jacintocapote](http://jacintocapote.com "Jacinto Capote, un gran hombre de la cabeza a los pies") por la ayuda :-)

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/quick-post-como-conseguir-los-node-links).*
