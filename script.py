import pandas as pd
import numpy as np

antiga = pd.read_csv("Planilha Antiga\SLR_PRINCIPAL - SCOPUS_ORIGINAL.csv")
# print(antiga.head())
# print()



atual = pd.read_csv('Planilhas Finais\current_SLR - Scopus.csv',)


count = 0
test = "A generalized, enterprise-level systems development process framework for systems analysis and design education"
for art_novo in atual.iloc[1:, 0]:
    for art_antigo in antiga.iloc[1:, 0]:
        if test == art_antigo:
            l,c = np.where(atual.values == art_antigo)
            print("liha",l[0],"  coluna",c[0])
            # atual.iloc[l[0],c[0]+1] = "ABACAXI"
            print(atual.iloc[l[0],c[0]+1])
            print("Novo: ", art_novo)
            count = count+1

# Antigo:  A generalized, enterprise-level systems development process framework for systems analysis and design education
# Novo:  A generalized, enterprise-level systems development process framework for systems analysis and design education

print(count)
# print(atual.S1.head(35))