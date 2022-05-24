from openpyxl import load_workbook
caminho = '.\data.xlsx'
arquivo_excel = load_workbook(caminho)
planilha1 = arquivo_excel.active

valores = [
    ("Categoria", "Valor"),
    ("Restaurante", 45.99),
    ("Transporte", 208.45),
    ("Viagem", 558.54)
]
for linha in valores:
    planilha1.append(linha)

arquivo_excel.save("data.xlsx")