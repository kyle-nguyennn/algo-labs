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
Let $T(w, i)$ be the minimum total time to complete steps $1..i$ (inclusive), where the worker who performs step $i$ is $w$.

We use the encoding:
$$
w \in \{0,1\}\quad (0 = \text{Claude},\ 1 = \text{Gemma}),\qquad i \in \{1,2,\dots,n\}.
$$

#### 2. Recurrence in terms of smaller subproblems:
Base case:
$$
T(0,1) = C_s + C[1]\qquad\text{and}\qquad T(1,1) = G_s + G[1].
$$
Recurrence:
$$
T(0,i) = C[i] + \min\{T(0,i-1),\ T(1,i-1) + 1\}
$$
$$
T(1,i) = G[i] + \min\{T(1,i-1),\ T(0,i-1) + 1\}
$$
, where  $i=2..n$:

Finally, add packaging time for the worker who performs step $n$:
$$
\min\{T(0,n) + C_p,\ T(1,n) + G_p\}
$$

#### 3. Complexity analysis:
1. Number of subproblems: $2n = O(n)$.
2. Runtime for table fill: $O(n)$ (each state is computed in $O(1)$).
3. Return extraction: return $\min\{T(0,n)+Cp, T(1,n)+Gp\}$
4. Runtime of return extraction: $O(1)$.
