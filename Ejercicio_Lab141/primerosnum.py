def es_primo(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True      
    if n % 2 == 0:
        return False     
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

count = 0
with open("Ejercicio_Lab141/results.txt", "w", encoding="utf-8") as f:
    for i in range(1, 251):
        if es_primo(i):
            print(i)
            f.write(f"{i}\n")
            count += 1

print(f"Total de primos encontrados: {count}") 