from knapsack.solver import knapsack

def test_knapsack():
    items = [(60, 10), (100, 20), (120, 30)]
    capacity = 50
    assert knapsack(items, capacity) == 220

def test_knapsack_zero_capacity():
    items = [(10, 5)]
    assert knapsack(items, 0) == 0
