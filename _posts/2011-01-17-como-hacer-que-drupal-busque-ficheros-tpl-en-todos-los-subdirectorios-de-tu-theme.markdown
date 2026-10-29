---
layout: post
title: "Cómo hacer que Drupal busque ficheros tpl en todos los subdirectorios de tu theme"
lang: es
date: 2011-01-17 12:00:00
excerpt: "Resumen rápido : El sistema de theming de Drupal no busca ficheros node-*.tpl.php ni page ni block en subdirectorios de tu theme (mientras que sí busca ficheros del tipo content-field-* o views-view*)"
categories: blog
archived_from: 3oheme.com
---
**Resumen rápido**: El sistema de theming de **Drupal no busca ficheros node-\*.tpl.php ni page ni block en subdirectorios de tu theme** (mientras que sí busca ficheros del tipo content-field-\* o views-view\*). Con este breve fragmento de código puedes **forzar a Drupal a que busque también en cualquier subdirectorio**, y así organizar tus ficheros como te venga mejor.

```php
function themename_theme(&$existing, $type, $theme, $path) {
 
  // get all directories inside theme
  $path = drupal_get_path('theme', 'themename');
  $results = scandir($path);
  foreach ($results as $result) {
    if ($result !== '.' && $result !== '..' && is_dir($path . '/' . $result)) {
      $existing['node']['theme paths'][] = $path . '/' . $result;
      $existing['block']['theme paths'][] = $path . '/' . $result;
      $existing['page']['theme paths'][] = $path . '/' . $result;
    }
  }
  return array();
}
```

En Alquimia estamos desarrollando actualmente un proyecto con otra gran empresa del sector, y la mejor metodología para enfrentarse a un theming a dos bandas es organizarse por directorios:

- En uno de ellos deben estar los css que afecten a toda la web (layout, tipografías, etcétera).
- Y luego diferentes directorios (cada uno con el nombre de una sección o apartado de la web) que contenga los ficheros css y tpl que afecten únicamente a esa zona de la página.

Pero por defecto, Drupal solamente busca por subdirectorios los ficheros de theming relativos a módulos, pero no a core, por lo que buscará por ejemplo los ficheros views-view-field--listado.tpl.php o content-field--hola.php, pero no los ficheros node-historia.tpl.php o block-block-42.tpl.php.

Para arreglar esto primero intenté añadir los nuevos ficheros al hook_preprocess. Este hook recibe un $vars['template_files'] con todas las sugerencias de ficheros, pero no funciona para subdirectorios, así que, mirando luego un poco el hook_theme encontré que se pueden añadir directorios y rutas donde Drupal debe buscar los ficheros .tpl.php.

El hook lo único que hace es buscar las sugerencias de ficheros actuales, escanear los subdirectorios del theme y añadir a las sugerencias nuevas entradas con los directorios encontrados. Fácil y rápido :-)

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/como-hacer-que-drupal-busque-ficheros-tpl-en-todos-los-subdirectorios-de-tu-theme).*
