# Asynchronous-Programming-and-Parallelism
An Introduction to Asynchronous Programming and Parallelism in Python with examples.

## 1. Multiprocessing
La librería de multiprocesamiento admite procesos dos, tres, cuatro ... diez veces y luego todas las secuencias de comandos se ejecutarán de forma independiente o al mismo tiempo.

## 2. Threading
Un hilo es una línea de ejecución, más o menos como un proceso, pero puede tener varios subprocesos en el contexto de un proceso y todos comparten acceso a recursos comunes.

## 3. Coroutines
Las corutinas son generalizaciones de subrutinas. Se utilizan para la multitarea cooperativa donde un proceso voluntariamente cede (regala) control periódicamente o cuando está inactivo para permitir que se ejecuten múltiples aplicaciones simultáneamente.

## 4. Count Async
Async IO habla con cada una de las llamadas a count () es un bucle de evento único o coordinador. Cuando cada tarea llega a aguardar asyncio.sleep (1), la función grita al bucle de eventos y le devuelve el control, diciendo: "Voy a dormir durante 1 segundo. Continúa y deja que se haga algo más significativo mientras tanto ".

## 5. Rand
Dado una corutina makerandom () que produce enteros aleatorios en el rango [0, 10], hasta que uno de ellos exceda un umbral, desea permitir que múltiples llamadas de esta corutina no necesiten esperar una a la otra para completarse sucesivamente.

## 6. Chained
Una característica clave de las corutinas es que se pueden encadenar juntas. (Recuerde, un objeto de rutina está en espera, por lo que otra puede esperarlo). Esto le permite dividir los programas en pequeñas, manejables y reciclables.

## 7. Función pool.Apply
La función poo.apply () toma un argumento args que acepta los parámetros pasados a la "función a ser paralelizada" como argumento,

## 8. Función pool.Map
La funcion pool.map () solo puede tomar un iterable como argumento. Es realmente más adecuado para operaciones iterables más simples y hace el trabajo más rápido.


## 9. Función pool.Starmap
En la función pool.starmap (), cada elemento en ese iterable también es iterable. Puede proporcionar los argumentos a la "función a ser paralelizada" en el mismo orden en este elemento iterable interno, a su vez se desempaquetará durante la ejecución.

