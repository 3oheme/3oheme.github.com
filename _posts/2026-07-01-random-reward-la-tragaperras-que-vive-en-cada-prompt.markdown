---
layout: post
title:  "Random reward: la tragaperras que vive en cada prompt"
date:   2026-07-01 07:10:41
excerpt: "¿A que no sabes que, gracias a que los chatbots son no deterministas, son también más adictivos? Suena a contradicción. Y sin embargo es justo al revés."
categories: blog
metaimage: /images/decks-tokyo-beach.jpg

---

¿A que no sabes que, gracias a que los chatbots son no deterministas (es decir, fallan más que una escopeta de feria) son también más adictivos?

Suena a contradicción. Lo lógico sería pensar que algo que no te da dos veces la misma respuesta es peor: menos fiable, más frustrante, más difícil de usar. Y sin embargo es justo al revés. Bueno, es peor para nosotros, pero mejor para su beneficio, como decía M. Rajoy. Esa imprevisibilidad, la que en cualquier otra herramienta sería un defecto de manual, aquí es exactamente lo que engancha.

El otro día en Genially soltaron: *"Claude engancha más que Instagram, TikTok y Balatro juntos"*. Lo soltó medio en broma un compañero, pero llevo varios días dándole vueltas y ojo, no le falta razón.

Es verdad. Y lo interesante no es que sea verdad, sino **por qué** lo es.

Vamos por partes.

### Por qué hacemos las cosas

Cuando le pides algo a un LLM hay un montón de motores empujándote a la vez, y conviene separarlos.

Por un lado están los motivadores **extrínsecos**: el resultado útil que necesitas, el ahorro de tiempo, quitarte de encima una tarea aburrida. Son los obvios, los que pondrías en una presentación para justificar el gasto en tokens. Por otro lado están los **intrínsecos**, que son más silenciosos pero más poderosos: la curiosidad de ver qué te va a contestar, la sensación de dominio cuando das con el prompt perfecto, ese placer del trabajo bien hecho cuando la respuesta sale redonda.

Hasta aquí, nada raro. Esto explica perfectamente por qué **usas** un LLM. Lo que no explica es por qué no puedes parar de usarlo. Por qué le sueltas otro prompt "solo para probar una cosa". Para eso hay que hablar de recompensa. Y de un señor con palomas.

### Los tres tipos de recompensa

A mediados del siglo pasado, B. F. Skinner se dedicó a meter ratas y palomas en cajas y a estudiar cómo el tipo de recompensa cambiaba el comportamiento. Lo llamó condicionamiento operante, y de ahí salieron los **esquemas de refuerzo**. Simplificando mucho, hay tres sabores:

* La **recompensa fija o continua**: cada vez que haces X, recibes Y. Aprietas la palanca, cae comida. Siempre. Es predecible, cómoda… y aburre rápido. En cuanto deja de caer comida, el animal abandona casi de inmediato.

* La **recompensa por intervalos**: la recompensa llega cada cierto tiempo, hagas lo que hagas. Es el sueldo a fin de mes. Funciona, pero tampoco engancha demasiado.

* Y luego está la **recompensa variable** o aleatoria (o *random reward* para los modernetes que hemos vivido en UK). En este caso no sabes cuántas veces tendrás que apretar la palanca para que caiga el premio. A veces a la primera, a veces a la décima. Skinner descubrió que este esquema, el de **razón variable**, produce la tasa de respuesta más alta y la mayor resistencia a la extinción de todos los que probó. Traducido: es el que más engancha y del que más cuesta despegarse.

¿Te suena de algo ese patrón de "no sé cuándo va a tocar pero sigo dándole"? Exacto. Es, literalmente, la lógica de una máquina tragaperras. El propio Skinner ya lo dejó escrito en 1953.

### Por qué la aleatoria es la que más dopamina suelta

Aquí entra la dopamina, que es la pieza que lo cierra todo.

Solemos pensar en la dopamina como "la molécula del placer", pero es una descripción mala. La dopamina no es tanto el premio como la **señal de predicción del premio**. Lo demostró Wolfram Schultz con sus famosos experimentos: cuando a un mono le das un zumo que ya esperaba, sus neuronas dopaminérgicas apenas se inmutan. Pero cuando el premio llega **por sorpresa**, sin que lo viera venir, esas neuronas se disparan con fuerza.

Es decir: el cerebro no celebra la recompensa. Celebra la **sorpresa** de la recompensa. Cuanto más impredecible es el premio, mayor es el chispazo. Y cuando algo es perfectamente predecible, el chispazo desaparece.

Junta las dos piezas —el esquema de razón variable de Skinner y la dopamina como señal de sorpresa de Schultz— y tienes la receta exacta del enganche. La tragaperras no te engancha a pesar de ser impredecible. Te engancha **precisamente porque** lo es. Cada tirada es una pequeña apuesta sobre si esta vez tocará, y tu circuito dopaminérgico no puede evitar emocionarse con la duda.

### Y entonces llega el LLM

Aquí es donde quería llegar.

Un LLM como Claude es **no determinista**. Le mandas el mismo prompt dos veces y recibes dos respuestas distintas. No sabes si esta vez te va a dar la solución elegante, el insight que no habías visto, o se ha equivocado contando [cuántas erres hay en la palabra 'strawberry'](https://www.reddit.com/r/singularity/comments/1enqk04/how_many_rs_in_strawberry_why_is_this_a_very/). No lo sabes hasta que le das a enviar.

¿Y eso qué es, exactamente? Pues una tirada. Cada prompt es **una palanca de la tragaperras**.

**La no-determinación convierte cada interacción en una recompensa variable.** Esperas los n segundos que tarda en pensar (para valores de n entre 3 y 600 segundos, como conté en [el post sobre el flow](https://palomoduarte.com/blog/2026/06/18/ia-y-la-muerte-del-flow.html)) y entonces aparece el resultado. A veces es oro. A veces es regular. Y como no sabes cuál de las dos va a tocar, vuelves a tirar. Y otra vez. Y otra.

No es metáfora. Es el mismo mecanismo que la paloma de Skinner apretando la palanca, el mismo que el jugador delante de la tragaperras, el mismo chispazo de dopamina. Solo que en lugar de comida o monedas, lo que cae es texto, código o una historia de usuario.

Por eso un compañero, sin haber leído un solo paper sobre condicionamiento operante, dio en el clavo: Claude engancha más que Instagram, TikTok y Balatro juntos. Porque las tres están construidas sobre exactamente el mismo principio. Solo que esta vez la tragaperras viene disfrazada de herramienta de trabajo.

### Lo que jamás le perdonaríamos a una tostadora

Es que me encanta. Porque esa misma no-determinación que en un LLM nos parece fascinante, en cualquier otro cacharro nos sacaría de quicio.

Imagínate por un momento que el resto de tus herramientas funcionara así:

- Le das al **interruptor de la luz** y unas veces se enciende la bombilla, otras suena la radio y otras no pasa absolutamente nada. Tú, encantado, volviendo a pulsar a ver qué toca.
- Metes el pan en la **tostadora**, bajas la palanca, y a veces sale tostado, a veces sale congelado y una de cada diez te suena la Macarena (que es exactamente lo que me pasa con la [última tostadora que me compré](https://amzn.eu/d/00cqNJKw), en lugar de pillarme una [Dualit](https://www.dualit.com/collections/toasters)).
- Pulsas el **6 en el ascensor** y te deja, con suerte, cerca de la sexta planta. O en el garaje. O en la azotea, con vistas.
- Tu **calculadora** te dice que 2+2 son 4… casi siempre.

Nos parecería de locos. De hecho, en mi post sobre [Apple y el camino hasta el delight](https://palomoduarte.com/blog/2021/11/01/apple-y-el-camino-desde-el-reliable-hasta-el-delight.html) defendía justo lo contrario: que lo que de verdad valoramos de un producto es que **funcione siempre. Siempre.** Esa palabra era la clave.

Y aquí estamos, pagando con gusto por una herramienta que, por diseño, no se comporta igual dos veces seguidas. La diferencia, claro, es que a la tostadora le pides una tostada y punto, mientras que al LLM le pides algo cuyo abanico de respuestas válidas es enorme. Pero el mecanismo psicológico por debajo es exactamente el de la tragaperras: si supieras de antemano qué va a salir, no habría sorpresa. Y sin sorpresa, ya lo hemos visto, no hay chispazo.

### Y aun así, seamos honestos

No escribo esto para demonizar nada. Yo soy el primero que tira de la palanca veinte veces al día, y la gran mayoría de esas veces saco valor real. Que el mecanismo del enganche sea el de una tragaperras no convierte el resultado en humo: la diferencia es que aquí, cuando "toca", muchas veces toca de verdad.

Pero creo que merece la pena ser conscientes de qué nos está pasando por dentro cuando trabajamos así. Saber que parte de las ganas de mandar "un prompt más" no viene de la tarea, sino de un circuito que llevamos cableado desde mucho antes de que existieran los LLMs. Reconocer la tragaperras no hace que deje de funcionar, pero al menos te deja decidir cuándo estás trabajando y cuándo simplemente estás tirando de la palanca a ver qué cae.

<p><img class="i-want-to-break-free" src="/images/decks-tokyo-beach.jpg" alt="Decks Tokyo Beach"></p>

---

Notas al pie de blog post para dármelas de guay:
- **Fuentes:** los esquemas de refuerzo y la razón variable vienen del trabajo de B. F. Skinner sobre condicionamiento operante ([Science and Human Behavior](https://www.bfskinner.org/behavioral-science/science-human-behavior/), 1953). Lo de la dopamina como señal de predicción de recompensa es de los experimentos de Wolfram Schultz con primates: las neuronas dopaminérgicas se disparan más ante recompensas inesperadas que ante las predecibles. Si os pica la curiosidad, hay literatura de sobra sobre el *reward prediction error*.
- Sabiendo un poco motivación intrínseca / extrínseca, tipos de recompensa, sistema 1 y 2 de Daniel Kahneman y em modelo de BJFog ya tienes el master en psicología.