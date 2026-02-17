def swap(S, i, j):
    S[i], S[j] = S[j], S[i]

def binary_search(a, e):
    l = 0
    r = len(a)
    # l, r is half open interval [l,r)
    while l < r:
        mid = (l + r)//2
        if a[mid] < e:
            l = mid + 1
        else:
            r = mid
    return l

def KthQuantiles(S: list[int], k: int) -> list[int]:
    # −1, 2, 4, 1, 3, 0, 18, −3
    # -3, -1, 0, 1, 2, 3, 4, 18
    # k = 4: -1 1 3
    # S = sorted(S)
    n = len(S)
    if k==1 or n<k: return []
    p = n//k
    res = []
    pivots = list(range(p-1, n-1, p))
    # estimate median
    if n <= 4:
        S = sorted(S)
        return [S[i] for i in pivots] # left median

    p = n//4
    medians = []
    for i in range(0, n, p):
        chunk =  S[i: min(i+p, len(S))]
        if len(chunk) == 1:
            medians.append(chunk[0])
        else:
            medians.append(KthQuantiles(chunk, 2)[0])
    medians = sorted(medians)
    pivot = medians[1]
    ### estimate median end
    # TODO: to be optimized by swapping
    left = [e for e in S if e<=pivot]
    right = [e for e in S if e>pivot]
    # print(f"pivot: {pivot}")
    # print(f"left: {left}")
    # print(f"right: {right}")
    # find the kth_quantiles covered by left 
    left_quantile_idx = binary_search(pivots, len(left))
    # print(f"pivots: {pivots}")
    # print(f"left_quantile_idx: {left_quantile_idx}")
    middle_quantile = []
    if len(left) < pivots[left_quantile_idx]+1:
        fill = pivots[left_quantile_idx] + 1 - len(left)
        left = left + [float("inf")]*fill
        right =  [float("-inf")]*(p - fill) + right
    elif len(left) == pivots[left_quantile_idx]+1:
        middle_quantile = [pivot]
    # print(f"left: {left}")
    # print(f"right: {right}")
    
    left_quantiles = KthQuantiles(left, left_quantile_idx+1)
    right_quantiles = KthQuantiles(right, k-left_quantile_idx - len(middle_quantile))
    # print(f"left quantiles: {left_quantiles}")
    # print(f"right quantiles: {right_quantiles}")

    return left_quantiles + middle_quantile + right_quantiles

# if __name__=="__main__":
#     quantiles = KthQuantiles([−1, 2, 4, 1, 3, 0, 18, −3],4)
#     assert(quantiles == [-1, 1, 3])