# Proceduralnie
def knapsack_procedural(capacity, items):
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if items[i - 1][1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1][1]] + items[i - 1][2])
            else:
                dp[i][w] = dp[i - 1][w]
    
    w = capacity
    chosen_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(items[i - 1])
            w -= items[i - 1][1]
    
    return dp[n][capacity], chosen_items

# Funkcyjnie
def knapsack_functional(capacity, items, n=None):
    if n is None:
        n = len(items)
    if n == 0 or capacity == 0:
        return 0, []
    
    if items[n - 1][1] > capacity:
        return knapsack_functional(capacity, items, n - 1)
    
    without_item, without_list = knapsack_functional(capacity, items, n - 1)
    with_item, with_list = knapsack_functional(capacity - items[n - 1][1], items, n - 1)
    with_item += items[n - 1][2]
    
    if with_item > without_item:
        return with_item, with_list + [items[n - 1]]
    else:
        return without_item, without_list

# Przykładowe przedmioty (id, waga, wartość)
items = [
    (1, 3, 60),
    (2, 2, 100),
    (3, 4, 120),
    (4, 1, 30)
]
capacity = 5

procedural_result = knapsack_procedural(capacity, items)
functional_result = knapsack_functional(capacity, items)

print("Proceduralnie:", procedural_result)
print("Funkcyjnie:", functional_result)
