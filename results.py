#!/usr/bin/env python3

numero_inicial = 1
numero_final = 250


def es_primo(numero: int) -> bool:
    """Devuelve True si el número es primo, False en caso contrario."""
    if numero < 2:
        return False

    for divisor in range(2, int(numero ** 0.5) + 1):
        if numero % divisor == 0:
            return False

    return True


def main():
    print(f"Buscando números primos entre {numero_inicial} y {numero_final}...")
    lista_primos = []

    # Calcular números primos en el rango
    for numero in range(numero_inicial, numero_final + 1):
        if es_primo(numero):
            lista_primos.append(numero)

    print(f"Total de números primos encontrados: {len(lista_primos)}\n")
    print("Lista de números primos:\n")

    # Mostrar en pantalla, 10 por línea
    for i, primo in enumerate(lista_primos, start=1):
        print(f"{primo:4}", end="  ")
        if i % 10 == 0:
            print()

    print("\n")

    # Nombre de archivo pedido por el laboratorio
    nombre_archivo = "results.txt"
    print(f"Guardando resultados en '{nombre_archivo}'...")

    # Guardar resultados en results.txt
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write("NÚMEROS PRIMOS ENTRE 1 Y 250\n")
        archivo.write(f"Total de números primos encontrados: {len(lista_primos)}\n\n")
        archivo.write("Lista completa de números primos:\n")

        for i, primo in enumerate(lista_primos, start=1):
            archivo.write(f"{primo:4}  ")
            if i % 10 == 0:
                archivo.write("\n")

    print(f"Archivo generado: {nombre_archivo}")


if __name__ == "__main__":
    main()
