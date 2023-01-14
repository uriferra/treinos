table = "<table>" # inicializa uma string que representa a tabela
for i in range(1,11):
    row = "<tr>" # inicializa uma string que representa a linha
    for j in range(1,11):
        row += "<td>" + str(i*j) + "</td>" # adiciona uma célula com o resultado da multiplicação
    row += "</tr>"
    table += row # adiciona a linha completa na tabela
table += "</table>"
print(table) # exibe a tabela