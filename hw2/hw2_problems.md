## Practice Problems

### [DPV] Problem 2.1 (Practice fast multiplication)
[placeholder for problem statement]
#### Solution
[TODO]

### [DPV] Problem 2.5 (Solving recurrence)
[placeholder for problem statement]
#### Solution
[TODO]

### [DPV] Problem 2.16 (infinite array)
[placeholder for problem statement]
#### Solution
[TODO]

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