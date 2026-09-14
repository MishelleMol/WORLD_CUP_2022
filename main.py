import pandas as pd 

#3.1 limpieza de datos
df = pd.read_csv("pases_brasil.csv")

df_grupos = df [df["fase"] == "Group Stage"]

print (df_grupos ["oponente"].unique()) #Oponentes en la fase de grupos

df_grupos.to_csv("Pases_brasil_grupos.csv", index = False ) #Datos limpios guardados