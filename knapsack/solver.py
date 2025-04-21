def knapsack(items, capacity):
    memo = {}

    def dp(i, remaining_capacity):
        if i == len(items):
            return 0
        if (i, remaining_capacity) in memo:
            return memo[(i, remaining_capacity)]

        value, weight = items[i]
        if weight > remaining_capacity:
            result = dp(i + 1, remaining_capacity)
        else:
            result = max(
                dp(i + 1, remaining_capacity),  # não pega item
                value + dp(i + 1, remaining_capacity - weight)  # pega item
            )

        memo[(i, remaining_capacity)] = result
        return result

    return dp(0, capacity)
