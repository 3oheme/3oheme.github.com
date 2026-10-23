---
layout: post
title: "Método rápido y sucio de quitar mensajes generados por Drupal"
lang: es
date: 2010-09-27 12:00:00
excerpt: "Drupal genera e imprime por pantalla mensajes de información para el usuario, que a veces están muy bien pero otras veces solamente incordian."
categories: blog
archived_from: 3oheme.com
---
Drupal genera e imprime por pantalla mensajes de información para el usuario, que a veces están muy bien pero otras veces solamente incordian.

Por defecto en Drupal 6 no hay ningún mecanismo (ni hook ni nada) para poder eliminar selectivamente algunos mensajes concretos, así que, si no quieres [hackear core](http://heyrocker.com/hack_core.jpg "No, nunca se hackea el core, muchacho") aquí te presentamos la manera rápida y sucia de hacerlo.

Solo tienes que copiar la siguiente función al **template.php** del theme que estés usando y cambiar el valor de la variable **$string_to_remove** a lo que quieras.

```php
function phptemplate_status_messages($display = NULL) {
  $output = '';
  $string_to_remove = 'El abuelo fue picador';
  foreach (drupal_get_messages($display) as $type => $messages) {
    $output .= "<div class=\"messages $type\">\n";
    if (count($messages) > 1) {
      $output .= " <ul>\n";
      foreach ($messages as $message) {
        if (strpos($message, $string_to_remove) === false) {
          $output .= '  <li>'. $message ."</li>\n";
        }
      }
      $output .= " </ul>\n";
    }
    else {
      if (strpos($messages[0], $string_to_remove) === false) {
        $output .= $messages[0];
      } else {
        $remove_output = true;
      }
    }
    $output .= "</div>\n";
  }
  return ($remove_output ? '' : $output);
}
```

**Nota 1**: hay un [módulo llamado messages alter](http://drupal.org/project/messages_alter) que facilita un hook para modificar los messages, pero en esencia hace lo mismo, buscar cadenas :-(  
**Nota 2**: esta guarrada no será necesaria en Drupal 7, ya que por fin facilitan un hook para modificar messages :-)

**UPDATE**: gracias a [morgothz](http://twitter.com/morgothz) por encontrar un bug, ya está solucionado :-D

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/metodo-rapido-y-sucio-de-quitar-mensajes-generados-por-drupal).*
