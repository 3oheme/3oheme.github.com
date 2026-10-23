---
layout: post
title: "Día 1 - control de estado del proyecto"
lang: es
date: 2010-01-30 12:00:00
excerpt: "¡Vuelta al trabajo! Después de tanto tiempo sin escribir ningún post os tengo que poner un poco al día de cómo va todo el proyecto. ¡Empezamos!"
categories: blog
archived_from: 3oheme.com
---
¡Vuelta al trabajo! Después de tanto tiempo sin escribir ningún post os tengo que poner un poco al día de cómo va todo el proyecto. ¡Empezamos!

### Arquitectura del proyecto

La arquitectura del proyecto sigue bastante fiel a la idea principal que se tuvo (y que explicaré más detalladamente en el siguiente post), pero a grosso modo decir que el sistema está orientado a objetos, y están modularizados y perfectamente separados (sin ningún tipo de acople, al menos por ahora) los siguientes elementos:

- Sistemas de gestión de una partida (dominoes.py), que reparte las fichas, comprueba que los jugadores colocan las fichas que corresponden (es decir, fichas que poseen y que se puedan colocar en el tablero), controla el fin de la mano y de la partida, y todas las acciones normales que pueden necesitarse para controlar una partida de dominó.
- Engine (graphics.py, que cambiará su nombre en breve a engine.py), encargado de los dispositivos de entrada/salida (interacción con del usuario y dibujar la pantalla) Con esto conseguimos que, si en un futuro se quiere prescindir de pygame y adoptar otra librería gráfica el proceso debería ser bastante sencillo y limpio.
- Los jugadores (tanto humano como controlado por una computadora), que heredan de una clase superior player.py y que comparten los métodos básicos de interacción: recibir información de la partida, colocar ficha, etcétera.

### Entorno gráfico

El entorno gráfico está bastante avanzado. Por ahora me he centrado en el desarrollo de una partida (no hay menús, no hay información adicional), las fichas se distribuyen correctamente a los jugadores, se dibujan todas las fichas y la mesa. Las características implementadas son las siguientes:

- Pintado del tablero: se ha desarrollado un algoritmo para pintar las fichas en la posición y orden correcto. Puede parecer un problema trivial, pero resulta bastante laborioso (o yo he estado más torpe de la cuenta, que también puede ser :-P)
- Se ha implementado un sistema de **themes/temas** gráficos, con la idea que desde el menú principal del juego se pueda seleccionar el aspecto gráfico de la aplicación, en concreto: fichas, pantallas de inicio, mesa, etc. En principio únicamente se trabaja con el tema clásico por defecto, más adelante iré añadiendo nuevos temas. Ya os podéis imaginar el juego que da todo esto: entorno *tasca de la España profunda*, diseño inspirado en la película [Tron](http://es.wikipedia.org/wiki/Tron), fichas con símbolos en lugar de números...
- Utilización de fichas en HD, soportando monitores de hasta 1920x1080 ([fullHD](http://es.wikipedia.org/wiki/Full-HD)) sin ningún problema (wow!)
- Diferentes formatos y resoluciones de pantalla: las fichas se reescalan y se configuran según la pantalla del usuario, por lo que da igual que la pantalla tenga proporción 4:3 o 16:9, las fichas tendrán el tamaño correcto para una visualización cómoda de la partida

Poco más. Os dejo aquí una captura de pantalla de la aplicación, y tenéis más en los adjuntos. Prometo escribir como mínimo un post a la semana, e ir informando del estado del proyecto.

Commit!

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/dia-1-control-de-estado-del-proyecto).*
