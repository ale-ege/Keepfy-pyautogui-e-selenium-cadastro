import pandas as pd

#GERAR DATAFRAME COM ITENS A SEREM CADASTRADOS
df = pd.read_excel('man.xlsx')
print(df)


#GERAR DATAFRAME COM ITENS CADASTRADOS
cad = pd.read_excel('data.xlsx')
print(cad)

for i, material in enumerate(df['Material']):
    print(material)
    if (material in (cad['Descriçăo'].values)):
        print("Material cadastrado!")
    else:
        print("NOK")
