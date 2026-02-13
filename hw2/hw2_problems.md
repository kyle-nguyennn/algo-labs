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
a. T(n) = 2T(n/3) + 1 \
        = O(n^log3(2))      
    Master theorem: d < logb(a) 

b. T(n) = 5T(n/4) + n \
        = O(n^log4(5))      
    Master theorem: d < logb(a)

c. T(n) = 7T(n/7) + n \
        = O(nlogn)    
    Master theorem: d = logb(a)
        
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
- Pair up the elements of A arbitrarily, to get n=2 pairs
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


b. Justifications:

c. Complexity:


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