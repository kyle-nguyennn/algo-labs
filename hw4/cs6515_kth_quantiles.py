def swap(S, i, j):
    S[i], S[j] = S[j], S[i]

def kth_select(S, k):
    n = len(S)
    if n < 5:
        S = sorted(S)
        return S[(len(S)-1)//2] # left median

    p = n//5
    medians = []
    for i in range(0, n, p):
        chunk =  S[i: min(i+p, len(S))]
        medians.append(kth_select(chunk, len(chunk)//2))
    medians = sorted(medians)
    pivot = medians[2]
    # TODO: to be optimized by swapping
    left = [e for e in S if e<pivot]
    middle = [e for e in S if e==pivot]
    right = [e for e in S if e>pivot]
    if k < len(left): return kth_select(left, k)
    if len(left) <= k < len(left) + len(middle): return pivot
    else: return kth_select(right, k - len(left) - len(middle))

def KthQuantiles(S: list[int], k: int) -> list[int]:
    # −1, 2, 4, 1, 3, 0, 18, −3
    # -3, -1, 0, 1, 2, 3, 4, 18
    # k = 4: -1 1 3
    # S = sorted(S)
    if k==1: return []
    n = len(S)
    p = n//k
    res = []
    pivots = list(range(p-1, n-1, p))
    median = kth_select(S, n//2) # true median, unique number
    # TODO: to be optimized by swapping
    left = [e for e in S if e<=median]
    right = [e for e in S if e>median]
    # find the kth_quantiles covered by left 
    left_quantiles = KthQuantiles(left, k//2)
    right_quantiles = KthQuantiles(right, k//2)

    return left_quantiles + [median] + right_quantiles