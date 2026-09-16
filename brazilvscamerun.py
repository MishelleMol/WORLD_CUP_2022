import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

#Leer datos ya filtrados de fase de grupos
df = pd.read_csv("Pases_brasil_grupos.csv")


def crear_grafo(oponente, peso_minimo=4):
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

    #Crear grafo dirigido
    G = nx.DiGraph()
    for _, fila in pases.iterrows():
        G.add_edge(
            fila["jugador_nombre"],
            fila["receptor_nombre"],
            weight=fila["peso"]
        )

    #Filtrar conexiones con peso_minimo o más EN ESA DIRECCIÓN
    aristas_relevantes = [
        (emisor, receptor) for emisor, receptor, datos in G.edges(data=True)
        if datos["weight"] >= peso_minimo
    ]
    G = G.edge_subgraph(aristas_relevantes).copy()

    
    #Posición de los nodos
    pos = nx.spring_layout(G, seed=42, k=0.8)
 
    plt.figure(figsize=(12, 9))
 
    #Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_size=1800, node_color="#2E8B57")
 
    #Dibujar nombres
    nx.draw_networkx_labels(
        G, pos,
        labels={jugador: jugador.split()[0] for jugador in G.nodes()},
        font_size=9
    )
 
    #Dibujar flechas
    nx.draw_networkx_edges(
        G, pos,
        arrows=True,
        arrowstyle="-|>",
        arrowsize=18,
        connectionstyle="arc3,rad=0.20",
        edge_color="gray"
    )

     #Peso de cada flecha
    pesos = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos, font_size=8, label_pos=0.5)
 
    plt.title(f"Brasil vs {oponente} - Pases completados (3+ pases por dirección)")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
#Grafo de partido de Brasil vs Camerún
crear_grafo("Cameroon")