---
layout: post
title: "Dominous v0.6 - Personajes + IA"
lang: es
date: 2011-02-20 12:00:00
excerpt: "Bueno, #Dominous avanza :-)"
categories: blog
archived_from: 3oheme.com
---
Bueno, #Dominous avanza :-)

Esta nueva actualización incluye muchas nuevas mejoras; muchas de ellas no son visibles a primera vista, y las iré explicando y desarrollando en posteriores posts, pero en resumen tenemos:

- **Personajes**: por un lado tenemos el nuevo aspecto de los jugadores, contando con una página de selección de compañero y adversarios. Los jugadores se leen dinámicamente de un directorio players, con lo cual podemos añadir nuevos jugadores simplemente añadiendo un nuevo directorio. Cada jugador cuenta con una IA, imagen, y nombre, que se lee de un fichero .INI
- **Sistema básico de IA**: Los jugadores ya piensan (más o menos). He diseñado un sistema de IA (muchísimas gracias a [arld101](http://ragingbit.com/blog/) por la idea original) que se basa en la definición clásica de [sistema experto](https://secure.wikimedia.org/wikipedia/es/wiki/Sistema_experto). Se proporciona una librería o biblioteca de funciones, normas o decisiones, y se van añadiendo estas reglas a la inteligencia artificial de cada jugador, ordenadas según prioridad de ejecución. De este tema ya hablaré en un post más adelante.

Poco más. Os dejo con un vídeo de ejemplo del funcionamiento, a ver qué os parece :-)

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/dominous-v06-personajes-ia).*
