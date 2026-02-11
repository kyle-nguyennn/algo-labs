def WootOff(
    W: tuple[int, ...], P: tuple[int, ...], C: tuple[int, ...]
) -> tuple[int, list[int]]:
    max_cap = max(C)
    n = len(W)
    wp = zip(W, P)
    wp = sorted(wp)
    # knapsack on max_cap
    dp = [0] * (max_cap+1) # max profit when cap = i
    for cap in range(max_cap+1):
        for weight, profit in wp:
            if weight > cap:
                break
            dp[cap] = max(dp[cap], dp[cap-weight]+profit)
    # print(dp)
    # extract result for each city
    res = [dp[city_cap] for city_cap in C]
    return sum(res), res
