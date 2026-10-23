---
layout: post
title: "Testing rápido de código python con pyflakes"
lang: es
date: 2011-05-21 12:00:00
excerpt: "Mini tutorial rápido sobre cómo analizar código python cómodamente en busca de errores mediante parseo del código."
categories: blog
archived_from: 3oheme.com
---
Mini tutorial rápido sobre **cómo analizar código python cómodamente en busca de errores** mediante parseo del código.

Os dejo aquí una pequeña receta para analizar vuestro código python en Ubuntu. Supongamos que (hipotéticamente) soy el usuario **boheme** en el portátil **boheme-laptop** y quiero analizar el código de mi proyecto fin de carrera, [dominous](http://www.3oheme.com/dominous "Gran proyecto!"). Primero instalamos [pyflakes](http://pypi.python.org/pypi/pyflakes):

`-laptop:~/pfc/dominous/trunk$ sudo easy_install pyflakes`

Y luego, a cada fichero python, le pasamos pyflakes:

`-laptop:~/pfc/dominous/trunk$ find . -name '*.py' -exec pyflakes {} \;`

Minitip: si te pasa como a mí, puede ser que te aparezca muchas veces la siguiente línea:

`/dominous.py:8: 'from menu import *' used; unable to detect undefined names`

Esta línea aparece porque, al hacer un import \*, pyflakes no puede saber si utilizas o no todo lo que importas. Puedes filtrar fácilmente estas líneas haciendo

`-laptop:~/pfc/dominous/trunk$ clear; find . -name '*.py' -exec pyflakes {} \; | grep -v "unable to detect undefined names"`

Y listo :-D

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2011/http://www.3oheme.com/blog/testing-rapido-de-codigo-python-con-pyflakes).*
