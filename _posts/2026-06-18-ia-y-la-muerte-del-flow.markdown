---
layout: post
title:  "IA y la muerte del flow"
date:   2026-06-18 17:21:00
excerpt: "Esta semana hemos hecho en Genially un hackathon distinto a todos los que he hecho en mi vida. La premisa era sencilla y ambiciosa a partes iguales: repensar nuestros flujos de trabajo completos poniendo la IA en el centro."
categories: blog
metaimage: /images/hackaton-ia-genially.jpg
---

Esta semana hemos hecho en Genially un hackathon distinto a todos los que he hecho en mi vida. La premisa era sencilla y ambiciosa a partes iguales: repensar nuestros flujos de trabajo completos —los de producto y los de desarrollo— poniendo la IA en el centro. IA first.

Y salí con una sensación rara, contradictoria, que llevo varios días intentando ordenar. Porque, aunque **hayamos generado muchísimo más valor que en cualquier otro hackathon, me he quedado con un sabor agridulce.**

Vamos por partes.

### Lo bueno (que fue mucho)

Empiezo por aquí, porque sería injusto no hacerlo.

**Es increíble el valor que puedes entregar en un lapso de tiempo tan corto.** Y no lo digo como titular vacío, lo digo con ejemplos concretos:

- **Prototipado.** Bien usado, un prototipo facilita una barbaridad la conversación entre actores que normalmente hablan idiomas distintos: desarrollo, stakeholders, QA. En cuestión de minutos tienes algo funcional, en una URL, con cinco o seis pantallas. Eso antes eran días.
- **Historias de usuario.** Las escribe y las refina a la velocidad del rayo, y he de reconocer que comete pocos errores.
- **Implementación de código.** El mayor impacto de todos, evidentemente. No hay que ser un genio para darse cuenta de que, en buenas manos (ojo a este "en buenas manos"), puede hacer que la implementación alcance ese mítico 10x del que tanto se habla en linkedin.
- **Integraciones.** Esto me sorprendió: a día de hoy la interoperabilidad entre sistemas está bastante madura. Puedes pedirle a Claude que lea una conversación de Slack, consulte después unas métricas en Amplitude y genere una historia de usuario en ClickUp siguiendo un formato estandarizado que vive como ficheros markdown en un repo de Github. Todo encadenado. Funciona.

Y un aprendizaje que he podido confirmar: **la conversación con el equipo sigue siendo fundamental**. Si le das espacio a esa conversación (un hackatón presencial es el lugar perfecto para ello) y facilitas las herramientas para recoger feedback – un figjam, lo que sea – en un momento aclaras dudas que la IA por sí sola no te iba a resolver. La IA no sustituye al equipo. Lo acelera.


### Lo que no me gustó

Aquí hay dos cosas, y una me preocupa más de lo que pensaba.

**La IA es terriblemente complaciente.** Por muy específico que seas en el prompt, por mucho que le exijas ser ortodoxo con las mejores prácticas de producto, siempre te entrega un *default*. Una opción recomendada, servida en bandeja, para que te resulte facilísimo darle a continuar al siguiente paso. Gastas más tokens y, sobre todo, no te obliga a parar a pensar. Y parar a pensar es, muchas veces, el trabajo. Aún así, existen herramientas para limitarlo (aquí somos fans de la skill [grill-me](https://github.com/mattpocock/skills/blob/733d312884b3878a9a9cff693c5886943753a741/skills/productivity/grill-me/SKILL.md)) y soy optimista en que se puede mejorar mucho.

Y luego, hablando ya en concreto de Claude, **la interoperabilidad entre sus propias herramientas es deficiente**. Es paradójico que conecte tan bien con sistemas externos y tan mal consigo mismo:

- Tienes Claude conectado a ClickUp, pero luego Claude Design no puede acceder a esa información de ClickUp.
- Generas un prototipo en Claude Design y luego no lo puedes consumir fácilmente en Claude Code.
- Los ficheros de contexto que añades a un proyecto no son visibles desde Claude Code.

Cada herramienta es una isla. Y tú haciendo de barca.



### Ahora hablemos del flow

Esta es la parte que me importa de verdad.

El flow, estar en la zona, esa inmersión total en una tarea en la que el tiempo desaparece y todo encaja. Pues bien, trabajar con un LLM funciona más o menos así:

Primero coges contexto. Entras en la tarea, en el proyecto, en la iniciativa. Entiendes el reto, vas pensando ideas, soluciones, los problemas colaterales que sabes que van a aparecer. Lo que de verdad pasa, vamos, en lugar del irreal double diamond de los esquemas de diseño.

Y entonces empieza el loop con el LLM:

1. **Le pides algo.** Ayuda con un PRD, investigación de competidores, casos de uso, un splitting de tareas.
2. **El LLM se pone a pensar.** Pueden pasar diez segundos, dos minutos o quince. Y como no sabes cuánto va a tardar, te pones a hacer otra cosa.
3. **Aquí aparece el problema.** Hacer otra cosa significa perder el contexto. Respondes un Slack, miras el correo, abres el calendar, empiezas a montar unas slides para mañana…
4. **El LLM vuelve con su respuesta, y te plantea una duda.** Y ahora toca recoger otra vez todo el contexto del principio, esta vez desparramado por el suelo en forma de pequeños trozos: por qué estabas haciendo esto, cómo encaja con lo que ya tiene tu herramienta, a qué user persona iba dirigido, qué métricas movía.

Y vuelta a empezar. El loop se repite hasta que sacas algún outcome.

**El problema no es la espera. El problema es que la espera te expulsa de la zona, y volver cuesta muchísimo más que esperar.**



### Y aun así, hay que ser honestos

Porque este flujo genera valor. Da velocidad, sí, pero hay algo más interesante: si nos centramos únicamente en la fase de producto, un buen prompt genera una conversación que **te obliga a pensar en detalles de producto en los que no habías caído.**

Y no hablo de la técnica del rubberduck de toda la vida. Hablo de que un LLM es capaz de desvelar gaps reales en tu razonamiento, agujeros que ni sabías que tenías, y de obligarte a recorrer entero el framework que habías planteado. No el que dices que recorres. El de verdad.

Eso, reconozcámoslo, es muy valioso.


### Lo bueno que está por venir

¿Y dónde está la esperanza? En que, idealmente, con el tiempo tendremos modelos más pequeños y más eficientes. Ese loop será prácticamente instantáneo. Y cuando la espera desaparezca, desaparecerá también la pérdida de contexto.

Ese día volveremos a estar en la zona. Mientras tanto, toca aprender a bailar con las pausas.

---

**Ojo**: todo esto lo he mirado desde la lente de la productividad. He dejado fuera a propósito variables como el impacto medioambiental o el coste de tokens. Son temas apasionantes, pero no era el scope de este post.

Mil gracias a Genially por montar este hackathon. Creo de verdad que, a la velocidad a la que aparecen nuevas herramientas y flujos de trabajo de IA, es de esas cosas que toda empresa debería repetir cada seis meses.

<p><img class="i-want-to-break-free" src="/images/hackaton-ia-genially.jpg" alt="Hackathon de IA en Genially">
<span class="smaller-text">Por cierto, si vais por Córdoba no os perdáis el fantástico café de <a href="https://c-coffee.es/" alt="website de C Coffee en Córdoba">C Coffee</a>, café de especialidad excelentemente preparado en todas sus variantes. El espresso y el cold brew son para comprarte quince.</span></p>

---

Si quieres contarme tu opinión o seguir la conversación, puedes hacerlo en este post de Bluesky:

<blockquote class="bluesky-embed" data-bluesky-uri="at://did:plc:jpdqvqijzdqgz6m355mlg2nw/app.bsky.feed.post/3morskxfzu224" data-bluesky-cid="bafyreifgw76q62u5js44xqw6jjlmhmyqrzvppax3yylqvu5zw3fwreox7u"><p lang="es">Se habla mucho del 10x de la IA en el código, y se habla poco de que rompe el flow.

El problema no es esperar la respuesta del LLM. Es que mientras esperas, abres Slack, miras el correo... y cuando vuelve, has perdido todo el contexto.

palomoduarte.com/blog/2026/06...</p>&mdash; <a href="https://bsky.app/profile/did:plc:jpdqvqijzdqgz6m355mlg2nw?ref_src=embed">Ignacio Palomo Duarte (@palomoduarte.com)</a> <a href="https://bsky.app/profile/did:plc:jpdqvqijzdqgz6m355mlg2nw/post/3morskxfzu224?ref_src=embed">21 Jun 2026</a></blockquote><script async src="https://embed.bsky.app/static/embed.js" charset="utf-8"></script>
