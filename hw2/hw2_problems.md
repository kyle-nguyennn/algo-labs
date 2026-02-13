## Practice Problems

### [DPV] Problem 2.1 (Practice fast multiplication)
Use Fast Multiply (Karatsuba) algorithm to perform 1001_1011 * 1011_1010
#### Solution
[TODO]: Let's draw it out

### [DPV] Problem 2.5 (Solving recurrence)
Solving the following recurrence relations: \
a. T(n) = 2T(n/3) + 1 \
b. T(n) = 5T(n/4) + n \
c. T(n) = 7T(n/7) + n \
d. T(n) = 9T(n/3) + n^2 \
e. T(n) = 8T(n/2) + n^3 \
f. T(n) = 49T(n/25) + n^(3/2)logn \
g. T(n) = T(n-1) + 2 \
h. T(n) = T(n-1) + n^c, c >= 1 const \
i. T(n) = T(n-1) + c^n, c > 1 const \
j. T(n) = 2T(n-1) + 1 \
k. T(n) = T(sqrt(n)) + 1
#### Solution

a.  
$T(n) = 2T(n/3) + 1$  
$\phantom{T(n)}\;= O\!\left(n^{\log_{3}(2)}\right)$  
Master theorem: $d < \log_b(a)$

b.  
$T(n) = 5T(n/4) + n$  
$\phantom{T(n)}\;= O\!\left(n^{\log_{4}(5)}\right)$  
Master theorem: $d < \log_b(a)$

c.  
$T(n) = 7T(n/7) + n$  
$\phantom{T(n)}\;= O(n\log n)$  
Master theorem: $d = \log_b(a)$

d.  
$T(n) = 9T(n/3) + n^2$  
$\phantom{T(n)}\;= O(n^2 \log n)$  \# $d = \log_b(a)$

e.  
$T(n) = 8T(n/2) + n^3$  
$\phantom{T(n)}\;= O(n^3 \log n)$  \# $d = \log_b(a)$

f.  
$T(n) = 49T(n/25) + n^{3/2}\log n$  
$\phantom{T(n)}\;= O\!\left(n^{3/2}\log n \right)$  

Explanation:

$\log_b(a) = \log_{25}(49) = \log_{5}{7} \approx 1.218$  
$n^{3/2}\log n > n^{3/2} = n^d$  
$\Rightarrow d = 1.5 > \log_b(a)$  
Hence the term $n^{3/2}\log n$ dominates.
$\Rightarrow T(n) = \Theta\!\left(n^{3/2}\log n\right)$

g.  
$T(n) = T(n-1) + 2$  
$\phantom{T(n)}\;= T(n-k) + 2k$  
$\phantom{T(n)}\;= O(n)$

h.  
$T(n) = T(n-1) + n^c,\;\; c\ge 1$ (constant)  
$\phantom{T(n)}\;= \sum_{k=1}^{n} k^c$  
$\phantom{T(n)}\;= \Theta(n^{c+1})$

i.  
$T(n) = T(n-1) + c^n,\;\; c>1$ (constant)  
$\phantom{T(n)}\;= \sum_{k=1}^{n} c^k$  
$\phantom{T(n)}\;= \Theta(c^n)$

j.  
$T(n) = 2T(n-1) + 1$  
$\phantom{T(n)}\;= 2^k T(n-k) + \sum_{i=0}^{k-1} 2^i$  
$\phantom{T(n)}\;= \Theta(2^n)$

k.  
$T(n) = T(\sqrt{n}) + 1$  
$\phantom{T(n)}\;= T\!\left(n^{1/2^t}\right) + t$  
$\phantom{T(n)}\;= \Theta(\log\log n)$


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
The work done at each iteration is O(1) for comparison, and we do this at most k steps, hence this extension part takes O(logn) work. The final step include finding x in the range n/2 to n using binary search, which also takes O(logn). Hence the total work done is O(logn).

### [DPV] Problem 2.23 (majority element)
An array A[1..n] is said to have a majority element if more than half of its entries are the
same. Given an array, the task is to design an efficient algorithm to tell whether the array has a
majority element, and, if so, to find that element. The elements of the array are not necessarily
from some ordered domain like the integers, and so there can be no comparisons of the form "is
A[i] > A[j]". (Think of the array elements as GIF files, say.) However you can answer questions
of the form: "is A[i] = A[j]?" in constant time.

#### Part A: Show how to solve this problem in O(n log n) time. 
Hint: Split the array A into two arrays
A1 and A2 of half the size. Does knowing the majority elements of A1 and A2 help you figure
out the majority element of A? If so, you can use a divide-and-conquer approach.

#### Part B: Can you give a linear-time algorithm? 
Hint: Here's another divide-and-conquer approach:
- Pair up the elements of A arbitrarily, to get n/2 pairs
- Look at each pair: if the two elements are different, discard both of them; if they are
the same, keep just one of them

Show that after this procedure there are at most n/2 elements left, and that they have a
majority element if and only if A does.

#### Solution
Part A:

a. The algorithm:

We split the original array into 2 halves. For each half, we recursively find the majority element and the count of the majority element. \
The base case is when the array only contain 1 element, we return the element and the count of 1.\
Let m_l, c_l be the majority from the left half, m_r, c_r be the majority from the right half. They are the candidates for the overall majority element of the array. It is possible that 1 or both halves do not have majority element. \
If both half do not have majority element, we return that the current array also does not have majority element and the count as 0. \
If majority element is only found in 1 half, we count the occurence of that majority element in the other half and add to the total count. If the total count > half of the length of the array, we return the majority element and the total count. \
If both halves have majority elements and they are the same, we are sure that is also the majority element of the array and the count is the sum of counts from 2 halves. \
If both halves have majority elements and they are different, we need to count the total occurence of each element in the whole array and compare between them to determine the overall majority. There's also a possiblity that the array does not have a majority element. If we have a winner and the count of the winner > half of the length of the array, we return the winner and its total count.

b. Justifications:

We claim: The overall majority element of the array, if exists, must be the majority element of at least 1 half. \
Proof: Assume the overall majority element of the array is not the majority element of either half. This means c_l <= n/4 and c_r <= n/4 => c_l + c_r <= n/2 => this element cannot be the majority element => contradiction. Hence proves the claim. \

From the result of the 2 subproblems, we have at most 2 candidiates for the overall majority elements. Now we just need to perform the count of each element on the whole array, and determine the overall majority element if its count > half the length of the array => proved by definition.

c. Complexity:

At each step we split the array in half, so we have 2 subproblems of half the size. The combining step takes at most O(n) as we need to iterate through the array to count the occurence of the majority candidate. Hence the recurrence relations is: T(n) = 2T(n/2) + O(n). This is a known recurrence similar to merge-sort, hence is solved to O(nlogn).

Part B:

a. The algorithm:

We split the array into n/2 consecutive pairs and perform the following elimination process:
if they are different, we eliminate both; if they are the same, we add 1 element to the result list. \
Base case: after the round, if the result list is empty, we return no majority element and end the algorithm; if the result list has only 1 element, that element is the best probable candidate for the majority element, we run a linear scan on the array to check if the count is actually > half the array length. \
If the result list has more than 1 element, we repeat the process on the result list until the base case is reach.

b. Justifications:

For simplicity, assume n = 2^k. We will prove 2 claims:\
Claim 1: If an element survive the elimination process, it is not neccessarily the majority element.
Claim 2: If a majority element exists, it must survive the elimination process.

Claim 1 is easy to prove by provide an example: \
Consider the array [1,2,3,4,5,5,5,5] which has no majority element. An arbitrary arrangements as follow: (1,2), (3,4), (5,5), (5,5). This would result in 5 being the survivor after the elimination process but we, by definition, know that 5 is not.

Claim 2 proof: when there's a majority element: \
Consider the weakest majority element c, having the count of n/2+1. The most disadvantageous arrangement for it is to have all other elements conspire against it, i.e, each non-majorirty element pair up with 1 majority element, to eliminate the most of c going through the next round. Since c have n/2+1 instance, there exists 1 pair of c-c, and this ensures at least 1 c going to the next round. Since all other pairs are different, they all get eliminated and c comes out on top as the only winner in this round. \
Why is this the most disadvantageous arrangement for c? Because it ensures the least number of c going through the round. Any deviation from this arrangement improves the number of instances of c in the next round. Take 2 pairs: c-a and c-b. It's obvious that swapping the partners of these 2 pairs only increase the count of c: c-c (1 c survive) and a-b (both eleminated). The other scenario is having 2 pairs: c-d and c-d. Swapping these 2 pairs increases both the count of c and d in the next round by 1, so they tie; but c already have 1 guaranteed member in the next round from the extra c-c pair, so c always 1-up any other element. \
Hence the majority element always survive the elimination process.

From these 2 claims, we are guaranteed that the survivor of the elimination process is the only probable candidate for majority element. We need to do a verification step (linear scan) to check if it's actually the majority element by counting its occurence.

c. Complexity:

From the description of the algorithm, we have the recurrence relation: T(n) = T(n/2) + O(n). Using master theorem this solves to O(n).


### Binary search modified* 
Design an O(log(n)) algorithm to find the smallest missing natural number in a given sorted array of length n. The given array only has distinct natural numbers. For example, the smallest missing natural number from A = [3, 4, 5] is 1, and from A = [1, 3, 4, 6] is 2.

#### Solution
a. The algorithm:

We can modify the binary search algorithm as follow: At each iteration, we compare A[mid] with mid. If A[mid] == mid, we know the missing number must be on the right partition, so we recurse the process from mid+1 to right. If A[mid] != mid, we record mid as the result, and continue to recurse on the left partition (from left to mid-1) to possibly improve on mid (smaller mid). The recursion stops when left > right. The recorded result is the minimum number that is missing from the array.

b. Justifications:

Align the elements on the natural number line, we see that a missing number at index i will shift the right portion of the array to the left, resulting in A[j] > j, for j >= i. If i is the first natural number that is missing, we have A[k] = k, for k < i. Hence we can search for the first element from the left that cause this to happen. The binary search process keep improving the resulting index until there's no further improvement, hence produces the smallest index.

c. Complexity:
Same as binary search, the modification only do 1 comparison per level. Hence the runtime complexity remains O(logn).


<small><b>Note:</b> For the practice problems, your solution (which does not need to be turned in) should be in the D&C format: describe your algorithms in words, justify the correctness of the approach, and analyze the run time.</small>


## Graded Problem

Let $R[1..n]$ be an array representing the projected total revenue generated through day i from running a digital advertising campaign. Additionally, let $C[1..n]$ be an array representing the projected operating cost of keeping the campaign active on day i.

You are hired to launch one campaign starting on day i and end it on a future day j. The total profit from this campaign period is defined as
$$
profit(i,j) = R[j] - R[i-1] - \sum_{k=i}^{j}{C[k]}
$$

That is, the profit is the difference between the revenue at the end of the campaign and the revenue at the start, minus the operating costs incurred while the campaign was running.

Design a divide and conquer algorithm to find indices i and j that maximize the profit.

### Solution

a. The algorithm:

Assume R[0] = 0. \
Let TC be the prefix of the cost, that is the total cost to run the compaign through day i.
$$
    TC[i] = \sum_{k=1}^{i}C[k] 
$$
Define TC[0]=0, we can rewrite the profit formula as
$$
\begin{aligned}
profit(i,j)
    &= (R[j] - R[i-1]) - (TC[j] - TC[i-1]) \\
    &= (R[j] - TC[j]) - (R[i-1] - TC[i-1])
\end{aligned}
$$
Define P as the running profit, that is the difference between the running revenue R and the the running cost TC: $P[i] = R[i] - TC[i]$
The profit again can be rewritten as: 
$$
profit(i,j) = P[j] - P[i-1]
$$

Now define the recursive function max_profit(L, R) that returns the following:

- index i and j that maximize the profit in the closed interval [L,R]
- the max_profit value in the closed interval [L,R]
- the max prefix index, called max_prefix_idx, that maximize profit(L, max_prefix_idx)
- the max prefix profit, called max_prefix, that is the max profit in the closed interval [L, max_prefix_idx]
- the max suffix index, called max_suffix_idx, that maximize profit(max_suffix_idx, R)
- the max suffix profit, called max_suffix, that is the max profit in the closed interval [max_suffix_idx, R]

The function performs these steps:

- Base case: when L=R, the interval only contain 1 element, hence:

    - i = j = max_prefix_idx = max_suffix_idx = L
    - max_prefix = max_suffix = max_profit = P[R] - P[R-1]

- Split the interval to 2 halves: mid = (L+R)/2
- Recursively call the max_profit on [L, mid] to get i_L, j_L, max_profit_L, max_prefix_idx_L, max_prefix_L, max_suffix_idx_L, max_suffix_L
- Recursively call the max_profit on [mid+1, R] to get i_R, j_R, max_profit_R, max_prefix_idx_R, max_prefix_R, max_suffix_idx_R, max_suffix_R
- Calculate the max profit that starts on the left parititon and ends on the right partition, called max_profit_cross. The max_profit_cross must be the max suffix from the left partition combined with the max prefix from the right, i.e., max_profit_cross = max_suffix_L + max_prefix_R.
- The max_profit of the interval [L,R] is the max of the 3 possibilities above, i.e., max(max_profit_L, max_profit_R, max_profit_cross). The index i,j can be extracted according to where the max_profit originates from: if max_profit is max_profit_L, (i,j) = (i_L, j_L); if max_profit is max_profit_R, (i,j) = (i_R, j_R); if max_profit is from max_profit_cross, (i,j) = (max_suffix_idx_L, max_prefix_idx_R).
- We need to also do the maintenance steps to return the extra information regarding the prefix and suffix to the upper recursive level:

    - max_prefix = max(max_prefix_L, (P[mid] - P[L-1]) + max_prefix_R)
    - max_prefix_idx = the max_prefix_idx of the above winner partition
    - max_suffix = max(max_suffix_R, (P[R] - P[mid-1]) + max_suffix_L)
    - max_suffix_idx = the max_suffix_idx of the above winner partition

b. Justifications:

Because profit is additive, meaning $profit(L, R) = profit(L, k) + profit(k+1, R)$, for $L <= k <= R$, we can rely on this property to split the array and calculate the max profit on each smaller half and combine the result. When the true max profit range lies completely on the left or right, is is trivial to conclude the overall max profit must come from the greater of the two. The only non-trivial case is when the true max profit range can cross the mid point, that is $i <= mid < j$. In this case, $[i, mid]$ must be the max suffix of the left partition and $[mid+1, j]$ must be the max prefix of the right parititon. This comes from the distributivity of the max function over addition over 2 sets: $max(A+B) = max(A) + max(B)$, in our case A and B are 2 discrete intervals that intersect at the boundary.


c. Complexity:

The above algorithm gives the recurrence relation: T(n) = 2T(n/2) + O(1), because the work to combine on the top level only takes constant time to update the extra information max_profit, max_prefix, max_suffix. This solves to T(n) = O(n), by master theorem.

