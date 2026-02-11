def WootOff(
    W: tuple[int, ...], P: tuple[int, ...], C: tuple[int, ...]
) -> tuple[int, list[int]]:
    max_cap = max(C)
    n = len(W)
    # knapsack on max_cap
    dp = [0] * (max_cap+1) # max profit when cap = i
    for cap in range(max_cap+1):
        for item in range(n):
            if cap >= W[item]:
                dp[cap] = max(dp[cap], dp[cap-W[item]]+P[item])
    # print(dp)
    # extract result for each city
    res = [dp[city_cap] for city_cap in C]
    return sum(res), res
