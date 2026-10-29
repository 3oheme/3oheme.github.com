---
layout: post
title: "StatSVN bajo Ubuntu [SOLUCIONADO]"
lang: es
date: 2010-06-07 12:00:00
excerpt: "StatSVN es una herramienta genial que nos permite obtener estadísticas de uso, commits, usuarios, etc... de un sistema SVN."
categories: blog
archived_from: 3oheme.com
---
[StatSVN](http://www.statsvn.org/) es una herramienta genial que nos permite obtener estadísticas de uso, commits, usuarios, etc... de un sistema SVN.

Peeeero si seguimos [los pasos que te vienen en su web](http://wiki.statsvn.org/) bajo ubuntu (testeado bajo 9.10 y 10.4) obtendremos un precioso error como el que sigue:

```text
Failed to load Main-Class manifest attribute from /usr/share/java/statsvn
```

Así que los pasos correctos son los siguientes, suponiendo que nuestro proyecto se llama **turmana** y se aloja en **https://forja.rediris.es/svn/turmana**.

Instalamos statsvn

```php
boheme@boheme-laptop:~$ sudo apt-get install statsvn
```

Hacemos checkout de la última versión del repositorio (mejor en un directorio aparte)

```php
boheme@boheme-laptop:~/turmana$ svn co https://forja.rediris.es/svn/turmana
```

Creamos el log que luego servirá de entrada a statsvn

```php
boheme@boheme-laptop:~/turmana$ svn log -v --xml > logfile.log
```

y ejecutamos statsvn (mejor en un directorio aparte) indicándole la ruta al logfile.log y al directorio donde hicimos el checkout

```php
boheme@boheme-laptop:~/turmana-stats$ /usr/bin/statsvn ../turmana/logfile.log \ 
>    ../turmana
```

---

*Publicado originalmente en mi antiguo blog, 3oheme.com, y recuperado de [archive.org](https://web.archive.org/web/2010/http://www.3oheme.com/blog/statsvn-bajo-ubuntu-solucionado).*
