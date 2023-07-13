import pandas as pd
import numpy as np
import re

acm = pd.read_csv("Resultado S1\current_SLR - ACM Modificado.csv")
iee = pd.read_csv("Resultado S1\current_SLR - IEEE Modificado.csv")
scopus = pd.read_csv("Resultado S1\current_SLR - Scopus Modificado.csv")
springer = pd.read_csv("Resultado S1\current_SLR - Springer Modificado.csv")


count = 0
m=0

for art_scopus in scopus.iloc[1:, 0]:
    for art_springer in springer.iloc[1:, 0]:

        tam = len(art_springer)
        i = int(0.2 * tam)
        f = int(0.8 * tam)
        titulo_menor = art_springer[i:f]

        if (art_scopus == art_springer) or (titulo_menor in art_scopus):
            l,c = np.where(springer.values == art_springer)
            # print("liha",l[0],"  coluna",c[0])
            springer.iloc[l[0],c[0]+2] = "Scopus"  # Mudança
            # print(springer.iloc[l[0],c[0]+1])
            # print("Novo: ", art_springer)
            m = m+1

for art_springer in springer.iloc[1:, 2]:
    if art_springer == "Scopus":
        count = count+1
    
springer.to_csv("Resultado S2/current_SLR - Springer S2.csv", index=False)

print("Total de alterações:",m)
print("Total de artigos repetidos:",count)

