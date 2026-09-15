import pandas as pd

#Leer datos ya filtrados de fase de grupos
df = pd.read_csv("Pases_brasil_grupos.csv")


def crear_grafo(oponente, peso_minimo=3):
    # Filtrar el partido: solo pases completos
    partido = df[
        (df["oponente"] == oponente) &
        (df["resultado"] == "Complete")
    ]

    # Contar cuántos pases completados hubo de cada jugador a cada receptor
    pases = (
        partido.groupby(["jugador_nombre", "receptor_nombre"])
        .size()
        .reset_index(name="peso")
    )

    print(pases.head())


# Grafo camerun
crear_grafo("Cameroon")