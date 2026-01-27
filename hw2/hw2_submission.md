## Graded Problem

Let $R[1..n]$ be an array representing the projected total revenue generated through day i from running a digital advertising campaign. Additionally, let $C[1..n]$ be an array representing the projected operating cost of keeping the campaign active on day i.

You are hired to launch one campaign starting on day i and end it on a future day j. The total profit from this campaign period is defined as
$$
profit(i,j) = R[j] - R[i-1] - \sum_{k=i}^{j}{C[k]}
$$

That is, the profit is the difference between the revenue at the end of the campaign and the revenue at the start, minus the operating costs incurred while the campaign was running.

Design a divide and conquer algorithm to find indices i and j that maximize the profit.

## Solution
[TODO]