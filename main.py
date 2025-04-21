from knapsack.solver import knapsack

if __name__ == "__main__":
    items = [(60, 10), (100, 20), (120, 30)]  # (valor, peso)
    capacity = 50
    result = knapsack(items, capacity)
    print(f"Valor máximo que pode ser carregado: {result}")
