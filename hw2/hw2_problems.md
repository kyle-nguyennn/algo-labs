## Practice Problems

### [DPV] Problem 2.1 (Practice fast multiplication)
Use Fast Multiply (Karatsuba) algorithm to perform 1001_1011 * 1011_1010
#### Solution
[TODO]: Let's draw it out

### [DPV] Problem 2.5 (Solving recurrence)
Solving the following recurrence relations:
a. T(n) = 2T(n/3) + 1
b. T(n) = 5T(n/4) + n
c. T(n) = 7T(n/7) + n
d. T(n) = 9T(n/3) + n^2
e. T(n) = 8T(n/2) + n^3
f. T(n) = 49T(n/25) + n^(3/2)logn
g. T(n) = T(n-1) + 2
h. T(n) = T(n-1) + n^c, c >= 1 const
i. T(n) = T(n-1) + c^n, c > 1 const
j. T(n) = 2T(n-1) + 1
k. T(n) = T(sqrt(n)) + 1

#### Solution
a. T(n) = 2T(n/3) + 1
        = O(n^log3(2))      # d < logb(a)
b. T(n) = 5T(n/4) + n
        = O(n^log4(5))      # d < logb(a)
c. T(n) = 7T(n/7) + n
        = O(nlogn)          # d = logb(a)
d. T(n) = 9T(n/3) + n^2
        = O(n^2 logn)       # d = logb(a)
e. T(n) = 8T(n/2) + n^3
        = O(n^3 logn)       # d = logb(a)
f. T(n) = 49T(n/25) + n^(3/2)logn
        = O(n^log5(7))
    logb(a) = log25(49) = 2/2 * (log5(7)) = 4.89
    n^(3/2)logn < n^(3/2)n = n^(5/2) => d < 2.5
    => lob(a) > d => Complexity is dominated by subproblem proliferation at each level
g. T(n) = T(n-1) + 2
        = T(n-2) + 2 + 2 = T(n-2) 2*2
        = T(n-k) + 2*k
        = 2*n
        = O(n)
h. T(n) = T(n-1) + n^c, c >= 1 const
        = T(n-2) + n^c + (n-1)^c
        = sum((n-k)^c), k=0..n-1
        = sum(k^c), k=1..n
        = O(n^c)
i. T(n) = T(n-1) + c^n, c > 1 const
        = T(n-2) + c^n + c^(n-1)
        = sum(c^k), k=1..n
        = O(c^n)
j. T(n) = 2T(n-1) + 1
        = 2(2T(n-2) + 1) + 1
        = 2*2T(n-2) + 1*2^0 + 1*2^1
        = 2^kT(n-k) + sum(2^i), i=0..k-1
        = 2^n + sum(2^i), i=0..n-1
        = O(2^n)
k. T(n) = T(sqrt(n)) + 1
        = T(sqrt(sqrt(n))) + 1 + 1
        = log logn          # The number of time to floor sqrt a number n until it reaches 1 is log(log(n))


### [DPV] Problem 2.16 (infinite array)
Given a sorted infinite array A, a number x. Find x in A if it exists, else return NOT FOUND.
#### Solution
a. The algorithm
We modify the binary search algorithm as follow.
Since we don't know the right limit of the array, we start with left=right=1. We keep comparing A[mid] with x until x is found or left > right, which results in NOT FOUND.
For each iteration, we determine where to continue the search based on the comparison between A[mid] and x, where mid is the middle index calculated as (left + right) floordiv 2. If A[mid] == x, we found x and return the index mid.
If A[mid] > x, we know to recursively search on the left partition with a bounded right. This becomes a standard binary search for x in range left to mid-1.
If A[mid] > x, we know to recursively search on the right partition. But this time we expand the right bound by doubling it if A[right] is not already infinite. This also becomes a standard binary search for x in range mid+1 to right.

b. Justifications
Suppose the unknown length of the non-infinite portion is n. The most we need to extend right boundary is log(n) times to get past it. Once we extended the right boundary past n, we are guaranteed to cover every element and can proceed as the standard binary search algorithm.

c. Complexity analysis
The worst case happens when x always fall on the right partition at each iteration. This means the work done at level k is the subproblem of finding x in the range 2^(k/2) to 2^k, i.e, T(2^k/2). We stop extending right at k=log2(n). 
The total work done is T(1) + T(2) + T(4) + ... + T(n)
### [DPV] Problem 2.23 (majority element)
[placeholder for problem statement]
#### Solution
[TODO]

### Binary search modified* 
Design an O(log(n)) algorithm to find the smallest missing natural number in a given sorted array of length n. The given array only has distinct natural numbers. For example, the smallest missing natural number from A = [3, 4, 5] is 1, and from A = [1, 3, 4, 6] is 2.

#### Solution
[TODO]

<small><b>Note:</b> For the practice problems, your solution (which does not need to be turned in) should be in the D&C format: describe your algorithms in words, justify the correctness of the approach, and analyze the run time.</small>


## Graded Problem

Let $R[1..n]$ be an array representing the projected total revenue generated through day i from running a digital advertising campaign. Additionally, let $C[1..n]$ be an array representing the projected operating cost of keeping the campaign active on day i.

You are hired to launch one campaign starting on day i and end it on a future day j. The total profit from this campaign period is defined as
$$
profit(i,j) = R[j] - R[i-1] - \sum_{k=i}^{j}{C[k]}
$$

That is, the profit is the difference between the revenue at the end of the campaign and the revenue at the start, minus the operating costs incurred while the campaign was running.

Design a divide and conquer algorithm to find indices i and j that maximize the profit.