---
layout: post
title: "Listado de taxonomías $term para un nodo"
lang: es
date: 2011-02-08 12:00:00
excerpt: "Mini snippet sobre cómo conseguir la misma variable $terms (listado de taxonomy) que tenemos en node.tpl.php :"
categories: blog
archived_from: 3oheme.com
---
Mini snippet sobre cómo conseguir la misma variable **$terms** (listado de taxonomy) que tenemos en **node.tpl.php**:

```php
$taxs = taxonomy_link('taxonomy terms', $node);
$terms = theme('links', $taxs, array('class' => 'links inline'));
print $terms;
```

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/listado-de-taxonomias-term-para-un-nodo).*
