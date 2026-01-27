### Problem:
2 workers Claude and Gemma work on a Multi-Conveyer Pipeline to assemble ragdolls.
Each regdoll assembly consists of n steps.
Given:
- C and G are 1-indexed arrays of size n representing amount of time for Claude and Gemma to complete each step respectively.
- Switching between Claude and Gemma take constant time of 1 unit.
- Setup time and packaging time for Claude: Cs, Cp
- Setup time and packaging time for Gemma: Gs, Gp
- The person who performs step 1 must also setup. (as clarified in Ed post #110)
- The person who performs step n must also package. (as clarified in Ed post #110)
Mininize the total time to produce a ragdoll.

### Solution:
#### 1. Definition
Let T(w, i) = the minimum time to complete the first i steps, with the last worker being w.
Range of variables:
    w = 0..1 (0 being Claude, 1 being Gemma)
    i = 1..n

#### 2. Recurrence in terms of smaller subproblems:
Base case:
    T(0, 1) = Cs + C[1]
    T(1, 1) = Gs + G[1]
Recurrence:
    T(0, i) = C[i] + min{T(0, i-1), T(1, i-1) + 1}
    T(1, i) = G[i] + min{T(1, i-1), T(0, i-1) + 1}
    where i=2..n

#### 3. Complexity analysis:
    a. Number of subproblems: O(n)
    b. Runtime for table fill: O(n)
    c. Return extraced as: return min{T(0,n) + Cp, T(1,n) + Gp}
    d. Runtime of return extraction: O(1)
