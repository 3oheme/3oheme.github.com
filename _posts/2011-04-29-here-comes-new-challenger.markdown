---
layout: post
title: "Here comes a new challenger!"
lang: es
date: 2011-04-29 12:00:00
excerpt: "Al más puro estilo Street Fighter, hoy os presento a un nuevo contrincante de Dominous... ehmm bueno, todavía no tiene nombre, pero le podéis llamar Lonely player ."
categories: blog
archived_from: 3oheme.com
---
Al más puro estilo Street Fighter, hoy os presento a un nuevo contrincante de Dominous... ehmm bueno, todavía no tiene nombre, pero le podéis llamar **Lonely player**.

Lonely es un gran jugador de dominó, lástima que peque de ser alguien un poco individualista. Bueno, decir que es un poco individualista es mentir más que una perra: juega para él solo, estimando únicamente sus fichas, intentando ganar todas las partidas y sin tener encuenta a su compañero.

Y lo mejor de todo es que no le va mal :-D jugando contra dos jugadores random, se ve que es bastante mejor:

Ahora la explicación de todo esto :-)

- Hace un par de días empecé a darle más caña a la Inteligencia Artificial.
- Empecé con la toma de decisiones al empezar una mano.
- Dependiendo de las fichas que tengas, deberás empezar con una u otra: si tienes muchas fichas de un palo está clara la decisión, pero si tienes el mismo número de fichas... ¿con cuál empezamos?
- Diseñé una matriz de pesos, que tuviera en cuenta cuatro factores:
  - La ficha (no es realmente un factor, pero sirve para diferenciar fichas que tenemos con fichas que no tenemos)
  - Si es doble o no
  - El número de hermanos que tenga (fichas del mismo palo)
  - Tamaño (valorando más o menos desde las blancas hasta el 6)

Y bueno, una vez que me hice las funciones para generar una matriz (y devolver el valor más alto), me dije: ¿Y por qué no creo un personaje que se base únicamente en esta matriz? Dicho y hecho, aquí tenemos al primer personaje medio en condiciones.

Nuestro Lonely player utiliza la matriz con 1000, 100, 10 y 1 puntos para ficha, doble, hermanos y tamaño, respectivamente. Y el siguiente paso será tantear con qué valores obtenemos al mejor Lonely player, así que... ¿Alguna sugerencia de puntos para la matriz? Aquellos que colaboren podrán enviar una foto y serán personajes en la versión definitiva de Dominous... yuhu!

¡Gracias por aguantar el tostón, seguimos!

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/here-comes-new-challenger).*
