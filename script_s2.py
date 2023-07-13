import pandas as pd
import numpy as np
import re

acm = pd.read_csv("Resultado S1\current_SLR - ACM Modificado.csv")
iee = pd.read_csv("Resultado S1\current_SLR - IEEE Modificado.csv")
scopus = pd.read_csv("Resultado S1\current_SLR - Scopus Modificado.csv")
springer = pd.read_csv("Resultado S1\current_SLR - Springer Modificado.csv")

atual = acm


count = 0
m=0

for art_scopus in scopus.iloc[1:, 0]:
    for art_atual in atual.iloc[1:, 0]:

        tam = len(art_atual)
        i = int(0.25 * tam)
        f = int(0.8 * tam)
        titulo_menor = art_atual[i:f]

        if (art_scopus == art_atual) or (titulo_menor in art_scopus):
            l,c = np.where(atual.values == art_atual)
            # print("liha",l[0],"  coluna",c[0])
            atual.iloc[l[0],c[0]+2] = "Scopus"  # Mudança
            # print(springer.iloc[l[0],c[0]+1])
            print("SCOPUS: ", art_scopus)
            print("Reduz: ", titulo_menor)
            print("Novo: ", art_atual)
            m = m+1

for art_atual in atual.iloc[1:, 2]:
    if art_atual == "Scopus":
        count = count+1
    
atual.to_csv("Resultado S2/current_SLR - ACM S2.csv", index=False)

print("Total de alterações:",m)
print("Total de artigos repetidos:",count)

