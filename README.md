# WORLD_CUP_2022-BRASIL 

Grafo dirigido: Elegimos un grafo dirigido porque en cada pase importa quién manda la pelota y quién la recibe. Por ejemplo, si Vinícius le da un pase a Neymar, se representa como Vinícius → Neymar, ya que esto no significa que Neymar también le haya dado un pase a Vinícius. Así podemos ver mejor cómo circula el balón entre los jugadores.

Grafo con pesos: Elegimos usar pesos porque queremos representar cuántos pases completados hizo un jugador hacia otro. Por ejemplo, si Casemiro completó 15 pases hacia Neymar, esa conexión tendría un peso de 15. Esto nos ayuda a identificar qué jugadores se conectan más entre sí y cuáles son las conexiones más importantes del equipo.

Grafo por partido: Decidimos realizar un grafo por cada partido de la fase de grupos porque así podemos analizar cómo cambió la forma de jugar de Brasil dependiendo del oponente. Esto nos permite comparar las conexiones entre los jugadores en cada partido e identificar diferencias en la circulación del balón.

Pases completos: Decidimos utilizar únicamente los pases completados porque queremos representar las conexiones que realmente ocurrieron entre los jugadores. Un pase incompleto no genera una conexión efectiva entre el emisor y el receptor, por lo que usamos los pases completos para representar de manera más clara cómo circuló el balón.
