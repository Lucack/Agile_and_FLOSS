import pandas as pd
import numpy as np
import re

antiga = pd.read_csv("Planilha Antiga\SLR_PRINCIPAL - Springer.csv")
atual = pd.read_csv("Planilhas Atuais\current_SLR - Springer.csv")

count = 0

for art_novo in atual.iloc[1:, 0]:
    for art_antigo in antiga.iloc[1:, 0]:

        # tam = len(art_novo)
        # i = int(0.05 * tam)
        # f = int(0.95 * tam)
        # titulo_menor = art_novo[i:f]

        if art_novo == art_antigo:
            l,c = np.where(atual.values == art_antigo)
            # print("liha",l[0],"  coluna",c[0])
            atual.iloc[l[0],c[0]+1] = "1"
            # print(atual.iloc[l[0],c[0]+1])
            # print("Novo: ", art_novo)
            count = count+1

atual.to_csv("Resultado/current_SLR - Springer Modificado.csv", index=False)

print("Total de artigos repetidos:",count)

