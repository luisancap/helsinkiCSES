import time
import random

# Gerando os números aleatórios
array = [random.randint(0, 1000) for _ in range(10**7)]

# Definição das funções antes da medição
def count_even_loop(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_generator(numbers):
    return sum(x % 2 == 0 for x in numbers)

# Teste da implementação 1
start1 = time.perf_counter()
count_even_loop(array)
end1 = time.perf_counter()
running_time1 = end1 - start1

# Teste da implementação 2
start2 = time.perf_counter()
count_even_generator(array)
end2 = time.perf_counter()
running_time2 = end2 - start2

print(running_time1)
print(running_time2)
