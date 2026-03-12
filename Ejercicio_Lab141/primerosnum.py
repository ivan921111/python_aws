with open("Ejercicio_Lab141/results.txt", "w", encoding="utf-8") as f:
    for i in range(1, 251):
        if i > 0:
            f.write(str(i) + "\n")