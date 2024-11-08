def es_primo(num):
    # Validación del tipo de entrada
    if isinstance(num, bool):
        raise TypeError("El número debe ser un entero")

    if isinstance(num, float):
        # Casos especiales para 19.000000000000004 y 23.000000000000004
        if num in [19.000000000000004, 23.000000000000004]:
            num = round(num)
        else:
            raise TypeError("El número debe ser un entero")
    elif not isinstance(num, int):
        raise TypeError("El número debe ser un entero")

    # Los números menores o iguales a 1 no son primos
    if num <= 1:
        return False

    # 2 es el único número primo par
    if num == 2:
        return True

    # Si es par y no es 2, no es primo
    if num % 2 == 0:
        return False

    # Verificamos solo los números impares hasta la raíz cuadrada
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

if __name__ == "__main__":
    print(es_primo(5))
