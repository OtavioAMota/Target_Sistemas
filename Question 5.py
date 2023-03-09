# Define a string que será invertida
texto = 'Exemplo de string'

# Converte a string para uma lista de caracteres
lista_caracteres = list(texto)

# Define as posições iniciais e finais da lista de caracteres
posicao_inicial = 0
posicao_final = len(lista_caracteres) - 1

# Percorre a lista de caracteres, trocando as posições dos caracteres
while posicao_inicial < posicao_final:
    # Armazena o valor do caractere na posição inicial em uma variável temporária
    temp = lista_caracteres[posicao_inicial]
    
    # Troca o valor do caractere na posição inicial pelo valor na posição final
    lista_caracteres[posicao_inicial] = lista_caracteres[posicao_final]
    
    # Troca o valor do caractere na posição final pelo valor armazenado na variável temporária
    lista_caracteres[posicao_final] = temp
    
    # Incrementa a posição inicial e decrementa a posição final para continuar a percorrer a lista
    posicao_inicial += 1
    posicao_final -= 1

# Converte a lista de caracteres de volta para uma string
texto_invertido = ''.join(lista_caracteres)

# Imprime o resultado na tela
print(f'Texto original: {texto}')
print(f'Texto invertido: {texto_invertido}')
