## Instructions

NP Reductions are proofs, and as such, we require your reduction to include specific content.   We have an unknown Problem B, and we want to prove that it is NP-complete. To accomplish this, you:

First, demonstrate that problem B is in the class of NP problems. This is, given a candidate solution to an instance of our unknown problem B, we show that you can validate that solution in Polynomial time. (We are not solving the problem; we are checking that the candidate solution is, in fact, a complete and valid solution).

Then demonstrate that problem B is at least as hard as a problem known to be NP-Complete.  This is done via reduction from a known problem A  (A→B). The specific steps are as follows:
Show how an instance of problem A is converted to an instance of problem B in polynomial time
Show how a solution to problem B can be converted to a solution for problem A, again in polynomial time
Show that a solution for B exists if and only if (IFF) a solution to A exists.   You must prove both directions -- if you have a solution to B, you have a solution to A; and if there is no solution for B, then no solution exists for A.
Additional details may be found in Ed Discussions. Please be sure to review that thread and ask any follow-up questions as needed.

[TODO] watch ed discuss for solution format

## Practice Problems

### [DPV] Problem 8.1 (TSP optimization versus search)
TSP:
Input: A matrix of distances between n cities, a budget b.
Output: A tour that passes through all the cities and total length <= n, if such a tour exists, and NO otherwise.

TSP optimization (TSP-OPT):
Input: A matrix of distances between n cities.
Output: The shortest tour that passes through all the cities.

Show that if TSP can be solved in polynomial time, then TSP optimization can also be solved in polynomial time.

#### Solution
If TSP can be solved in polynomial time, we can binary search the budget b to find the shortest tour. This is binary search problem in a order boolean space, which can be solved in O(log n) time. Suppose TSP can be solved in O(f(n)) time, then TSP-OPT can be solved in O(f(n) log n) time, which is polynomial if f(n) is polynomial.


### [DPV] Problem 8.3 (Stingy SAT)
Given a set of clauses and an integer k, find a satisfying assignment in which at most k variables are set to true, if exists. Prove that Stingy SAT is NP-complete. (Hint: reduce from Vertex Cover, which is NP-complete.)

#### Solution
[TODO]:


### [DPV] Problem 8.4 (a), (b), (c) (Clique-3)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 8.8 (Exact 4SAT)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 8.10 (a) (Subgraph isomorphism. You are welcome to try them all)
[Problem statements]
#### Solution
[TODO]:


---
<div style="page-break-before: always;"></div>

## Graded Problem

A bowtie of size N is a graph with exactly 2N vertices such that N vertices form a clique, the other N vertices form a second clique, and there is exactly one edge connecting the two cliques.

Consider the Bowtie Problem:

Input: A graph G=(V,E) and a natural number N>2. 

Output: a set of 2N vertices such that the induced subgraphLinks to an external site. is a bowtie, or report NO if such a set does not exist.

Show that the Bowtie-Search problem is NP-complete.

### Solution
[TODO]