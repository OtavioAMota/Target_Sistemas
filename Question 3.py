import json

# Carrega os dados de faturamento a partir de um arquivo JSON
with open('dados_faturamento.json', 'r') as file:
    dados_faturamento = json.load(file)

# Remove os valores de faturamento para os dias sem dados (finais de semana e feriados)
dias_validos = [dia for dia in dados_faturamento if dados_faturamento[dia] is not None]
valores_faturamento = [dados_faturamento[dia] for dia in dias_validos]

# Calcula o menor e o maior valor de faturamento
menor_faturamento = min(valores_faturamento)
maior_faturamento = max(valores_faturamento)

# Calcula a média mensal de faturamento
media_mensal = sum(valores_faturamento) / len(valores_faturamento)

# Calcula o número de dias em que o faturamento diário foi superior à média mensal
dias_acima_da_media = sum([1 for valor in valores_faturamento if valor > media_mensal])

# Imprime os resultados na tela
print(f'O menor valor de faturamento ocorrido em um dia do mês foi R${menor_faturamento:.2f}.')
print(f'O maior valor de faturamento ocorrido em um dia do mês foi R${maior_faturamento:.2f}.')
print(f'O número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi {dias_acima_da_media}.')
