faturamento_mensal = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calcula o valor total do faturamento mensal da distribuidora
total_mensal = sum(faturamento_mensal.values())

# Calcula o percentual de representação de cada estado no faturamento mensal da distribuidora
percentuais = {estado: (valor / total_mensal) * 100 for estado, valor in faturamento_mensal.items()}

# Imprime os resultados na tela
for estado, percentual in percentuais.items():
    print(f'O estado {estado} teve uma representação de {percentual:.2f}% no faturamento mensal da distribuidora.')
