import pandas as pd
import numpy as np
import re

bd = pd.read_csv("P1 - Revisão de Duplicados\Duplicados.csv")
count = 0
m=0
bd = bd.applymap(lambda x: x.upper() if isinstance(x, str) else x)

for index, row in bd.iterrows():
    for col in bd.columns:
        artigo = row[col]
        m=m+1

        # Procurando artigo no DataFrame excluindo a linha atual
        temp_bd = bd.drop(index)
        
        if artigo in temp_bd.values: #or titulo_menor in temp_bd.values:
            l, c = np.where(bd.values == artigo)
            count += 1
            #print(f"O artigo '{artigo}' da linha {index + 1} está repetido nas linhas {l + 1}.")

        

if count == 0:
    print("Nenhum artigo repetido encontrado.")


print(temp_bd)
print("Total de alterações:",m)
print("Total de artigos repetidos:",count)

