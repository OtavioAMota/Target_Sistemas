def fibonacci_sequence(n):
    """Função que calcula a sequência de Fibonacci até o número n"""
    fibonacci = [0, 1]
    while fibonacci[-1] < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def check_if_fibonacci(n):
    """Função que verifica se o número n pertence à sequência de Fibonacci"""
    fibonacci = fibonacci_sequence(n)
    if n in fibonacci:
        return f'O número {n} pertence à sequência de Fibonacci: {fibonacci}'
    else:
        return f'O número {n} não pertence à sequência de Fibonacci: {fibonacci}'

# Solicita que o usuário informe um número
n = int(input('Informe um número: '))

# Chama a função que verifica se o número pertence à sequência de Fibonacci e imprime o resultado na tela
print(check_if_fibonacci(n))
