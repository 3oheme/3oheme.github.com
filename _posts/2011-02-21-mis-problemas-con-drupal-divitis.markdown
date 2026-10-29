---
layout: post
title: "Mis problemas con Drupal: divitis"
lang: es
date: 2011-02-21 12:00:00
excerpt: "Drupal tiene una enfermedad horrible: divitis."
categories: blog
archived_from: 3oheme.com
---
**Drupal tiene una enfermedad horrible: divitis.**

Solamente pondré un ejemplo:

- Instalación básica de Drupal
- theme [Fusion](http://drupal.org/project/fusion) **(20.750)**
- [Panels](http://drupal.org/project/panels) **(70.657)** con un bloque de [Views](http://drupal.org/project/views) **(280.982)** que simplemente muestra un listado de nodos.

Los numeritos entre paréntesis indican las personas que usan estos módulos/themes, así que como véis esta configuración de Drupal es bastante corriente (para más info tenéis la [lista de módulos/themes más usados](http://drupal.org/project/usage)).

Ahora al lío, mirad el código que genera este monstruo:

[pulsa para ampliar](https://web.archive.org/web/2011/http://www.3oheme.com/sites/www.3oheme.com/files/divitis.png "pulsa para ampliar")

Un poco mal, ¿no? Un mar de divs, una tormenta de clases, una lluvia de tags... y esto no acaba aquí, ahora viene lo peor:

## Es imposible curar la divitis de forma permanente

Todos los módulos de drupal tienen divitis. Views tiene divitis, CCK tiene divitis, Panels también, los themes zen/fusion también. Todo, todo está plagado de divs.

Y alguien dirá: ***Eh, muchacho, ¿por qué no sobreescribes los ficheros tpl.php para que no generen tantas clases y tags?***

Oh, sí, claro que puedes. Por ejemplo [Morten.dk](http://morten.dk/ "el rocker-showman-themer") ya lo hizo en su theme [mothership](http://drupal.org/project/mothership "un theme realmente interesante, en serio, echadle un vistazo"). Un theme enooorme, con un montón de overrides, funciones theme_\* y ficheros .tpl.php. Un theme con un problema peligroso: **todos esos overrides son para versiones específicas de módulos**. Si mañana actualizan CCK o Views y añaden más elementos en los tpl.php, te jodes, o lo que es peor, tu instalación empieza a fallar por algo, aparecen bugs sin saber por qué, tienes que actualizar... no, esta no es la forma de hacer las cosas.

Al final aprendes a convivir con la enfermedad. Te aprovechas de sus beneficios, corriges de forma temporal algunos casos de divitis más exagerados en algunos proyectos... finges ser feliz con ello.

**Hola, soy Ignacio Palomo y sufro la divitis en silencio.**

*Postdata: otro día hablaremos de módulos que añaden CSS mal formado, CSS llenito de !important por todos sitios, pero eso será en otra sesión de themers anónimos.*

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/mis-problemas-con-drupal-divitis).*
