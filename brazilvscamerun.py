import pandas as pd
import networkx as nx

#Leer datos ya filtrados de fase de grupos
df = pd.read_csv("Pases_brasil_grupos.csv")


def crear_grafo(oponente, peso_minimo=3):
    #Filtrar el partido: solo pases completos de ese rival
    partido = df[
        (df["oponente"] == oponente) &
        (df["resultado"] == "Complete")
    ]

    #Contar cuántos pases completados hubo de cada jugador a cada receptor
    pases = (
        partido.groupby(["jugador_nombre", "receptor_nombre"])
        .size()
        .reset_index(name="peso")
    )

    # Crear grafo dirigido
    G = nx.DiGraph()
    for _, fila in pases.iterrows():
        G.add_edge(
            fila["jugador_nombre"],
            fila["receptor_nombre"],
            weight=fila["peso"]
        )

    print("Jugadores:", G.number_of_nodes())
    print("Conexiones:", G.number_of_edges())
    return G


#Grafo para el partido de Brasil vs Camerún
crear_grafo("Cameroon")
