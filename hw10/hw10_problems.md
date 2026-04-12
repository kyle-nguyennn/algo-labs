## Instructions

NP Reductions are proofs, and as such, we require your reduction to include specific content.   We have an unknown Problem B, and we want to prove that it is NP-complete. To accomplish this, you:

First, demonstrate that problem B is in the class of NP problems. This is, given a candidate solution to an instance of our unknown problem B, we show that you can validate that solution in Polynomial time. (We are not solving the problem; we are checking that the candidate solution is, in fact, a complete and valid solution).

Then demonstrate that problem B is at least as hard as a problem known to be NP-Complete.  This is done via reduction from a known problem A  (A→B). The specific steps are as follows:
Show how an instance of problem A is converted to an instance of problem B in polynomial time
Show how a solution to problem B can be converted to a solution for problem A, again in polynomial time
Show that a solution for B exists if and only if (IFF) a solution to A exists.   You must prove both directions -- if you have a solution to B, you have a solution to A; and if there is no solution for B, then no solution exists for A.
Additional details may be found in Ed Discussions. Please be sure to review that thread and ask any follow-up questions as needed.

## Practice Problems

### Practice Problems (NP Theory)

### [DPV] Problem 8.9 (Hitting Set)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 8.19 (Kite)
[Problem statements]
#### Solution
[TODO]:


### Practice Problems (Linear Programming)

### [DPV] Problem 7.1 (Can you use the dual LP to prove it's optimal?)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 7.4 (LP for Duff beer)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 7.5 (LP for canine products)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 7.6 (Give an example of an LP with an unbounded feasible region but bounded optimum.)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 7.11 (dual to the example)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problem 7.12 (prove that point (1.5, 0.5, 0) is optimal)
[Problem statements]
#### Solution
[TODO]:


---
<div style="page-break-before: always;"></div>

## Graded Problem

The City Planner for the city of Computopia is tasked with placing a number of sports facilities such that every neighborhood in the city is served by at least one such facility. There are n neighborhoods in Computopia and the City Planner is given a list of m strategic facility locations and the neighborhoods each will serve if built.

The only issue is the budget: the city can build at most K facilities.

For example, if there are 6 neighborhoods and the list of potential facilities and the neighborhoods they would serve is

f1 that can serve N1, N2, N5;
f2 that can serve N1, N3, N6;
f3 that can serve N2, N4;
f4 that can serve N3, N6.

there is a solution for K=3 (building facilities at locations f1, f3, f4) but there is no solution for K=2.

The Allocation problem is:

Given a list of lists L, where L[i] is the list of neighborhoods that facility at location i will serve, and the value of K > 0, it outputs a subset of facilities to build such that all neighborhoods will be served by at least one, or reports that it is not possible with the city's budget.

Show that the Allocation problem is NP-complete.

### Solution
Allocation problem with input L and K: A(L, K)
a. Show that A is in NP

Given a candidate solution S (a subset of facilities), we can verify in polynomial time whether S is a valid solution to the Allocation problem. We can check if the number of facilities in S is less than or equal to K, and then we can iterate through each neighborhood and check if it is served by at least one facility in S. This verification process takes polynomial time with respect to the size of the input L and K, thus A is in NP.

b. Show that A is NP-complete by reduction from a known NP-complete problem.

Reduction from Vertex Cover problem with input G and k: VC(G, k):

Given an instance of the Vertex Cover problem, we can construct an instance of the Allocation problem as follows:

1. For each vertex v in G, create a facility f_v.
2. For each edge (u, v) in G, create a neighborhood n_(u,v) that is served by facilities f_u and f_v.
3. Set K = k.

Forward claim: If there exists a vertex cover of size k in G, then there exists a subset of facilities of size K that serves all neighborhoods in the Allocation problem. 
Proof: Given a vertex cover of size k in G, then we can select the corresponding facilities for those vertices. Since the vertex cover covers all edges, every neighborhood (which corresponds to an edge) will be served by at least one of the selected facilities. Therefore, we have a valid solution for the Allocation problem with K = k.

Backward claim: If there exists a subset of facilities of size K that serves all neighborhoods, then there exists a vertex cover of size k in G.
Proof: Given a subset of facilities of size K that serves all neighborhoods, we can select the corresponding vertices for those facilities. Since every neighborhood (edge) is served by at least one facility, it means that every edge in G has at least one end in the selected vertices. Therefore, the selected vertices form a vertex cover of size k in G.

This reduction can be done in polynomial time, thus A is NP-complete.