import pandas as pd
import numpy as np
import re

acm = pd.read_csv("Resultado S2\current_SLR - ACM S2.csv")
ieee = pd.read_csv("Resultado S2\current_SLR - IEEE S2.csv")
scopus = pd.read_csv("Resultado S1\current_SLR - Scopus Modificado.csv")
springer = pd.read_csv("Resultado S2\current_SLR - Springer S2.csv")

atual = acm


count = 0
m=0

for art_ieee in ieee.iloc[1:, 0]:
    for art_atual in atual.iloc[1:, 0]:

        tam = len(art_atual)
        i = int(0.25 * tam)
        f = int(0.75 * tam)
        titulo_menor = art_atual[i:f]

        if (art_ieee == art_atual) or (titulo_menor in art_ieee):

            linha,colum = np.where(atual.values == art_atual)

            if atual.iloc[linha[0],colum[0]+2] == "Springer":
                l,c = np.where(atual.values == art_atual)
                atual.iloc[l[0],c[0]+2] = "Springer + IEEE"  # Mudança
                print("IEEE: ", art_ieee)
                print("Reduzi: ", titulo_menor)
                print("Atual : ", art_atual)
                print()
                m = m+1
            
            elif atual.iloc[linha[0],colum[0]+2] == "Scopus":
                l,c = np.where(atual.values == art_atual)
                atual.iloc[l[0],c[0]+2] = "Scopus + IEEE"  # Mudança
                print("IEEE: ", art_ieee)
                print("Reduzi: ", titulo_menor)
                print("Atual : ", art_atual)
                print()
                m = m+1

            else:
                l,c = np.where(atual.values == art_atual)
                # print("liha",l[0],"  coluna",c[0])
                atual.iloc[l[0],c[0]+2] = "IEEE"  # Mudança
                # print(springer.iloc[l[0],c[0]+1])
                print("IEEE: ", art_ieee)
                print("Reduzi: ", titulo_menor)
                print("Atual : ", art_atual)
                print()
                m = m+1

for art_atual in atual.iloc[1:, 2]:
    if art_atual == "IEEE" or art_atual == "Scopus + IEEE" or art_atual == "Springer + IEEE":
        count = count+1
    
atual.to_csv("Resultado S2/current_SLR - ACM S2.csv", index=False)

print("Total de alterações:",m)
print("Total de artigos repetidos:",count)

