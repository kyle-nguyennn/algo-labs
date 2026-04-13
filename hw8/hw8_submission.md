## HW8: T Edge Doubled

**Problem:** You are given a graph G=(V, E) and an MST T of G. The weight of an edge e, which is part of T, is doubled. All other edges keep their original weight. Design an algorithm that outputs an MST for the graph G with the updated weights.

### (a) Algorithm

We are given a connected, undirected graph G=(V, E), an MST T of G under original weights w, an edge e in T, and updated weights w' where w'(e) = 2·w(e) and w'(f) = w(f) for all other edges f.

First, remove edge e from T to obtain T' = T - {e}. Since T is a tree, removing e disconnects T' into exactly two connected components.

Run DFS on T' to obtain the connected component numbers ccnum for each vertex. Let comp_a = ccnum[u] where u is one endpoint of e. This identifies the two components A and B of the cut created by removing e.

Next, scan all edges of G. For each edge (u, v), check whether ccnum[u] ≠ ccnum[v], which indicates the edge crosses the cut between A and B. Among all crossing edges, find the edge f with minimum weight under w'.

Finally, add f to T' to form T'' = T' ∪ {f}. Return T'' as the new MST.

### (b) Justification of Correctness

T was an MST of G under the original weights w. Removing edge e from T splits T into exactly two connected components, creating a cut (A, B). By the Cut Property, any MST of G under the updated weights w' must include the minimum weight crossing edge of the cut (A, B) with respect to w'.

We use DFS on T' to identify the two components via ccnum, which correctly labels each vertex with its component number. Checking ccnum[u] ≠ ccnum[v] correctly identifies edges that cross the cut. We then find the minimum weight crossing edge f under w' by scanning all edges of G.

If f = e (meaning e with its doubled weight is still the cheapest crossing edge), then the original MST T is still optimal, and adding e back produces T again. If f ≠ e, then f has a smaller weight than the doubled e, and T' ∪ {f} replaces e with a cheaper alternative.

T' ∪ {f} is a valid spanning tree: T' has n−2 edges spanning two components, and f reconnects them, giving n−1 edges spanning all n vertices with no cycles. It is an MST because f is the minimum crossing edge of the cut (A, B) under w' (by the Cut Property, f must be in any MST), and the remaining n−2 edges of T' were in the original MST T. None of their weights changed, and for each such edge e', removing e' from T' ∪ {f} creates a cut where e' was already the minimum weight crossing edge under w (since T was an MST). Since w'(e') = w(e') and w'(g) ≥ w(g) for all other edges g (no weight decreased), e' remains the minimum crossing edge under w', confirming T' ∪ {f} is an MST.

### (c) Runtime Analysis

- Removing edge e from T: O(n) (single edge operation on an adjacency list).
- Running DFS on T': O(n), since T' is a forest with n vertices and n−2 edges, giving O(n + (n−2)) = O(n).
- Scanning all edges of G to find the minimum crossing edge f: O(n + m) (traversing the graph). Each crossing check uses ccnum lookups in O(1).
- Adding edge f to T': O(1) (appending to adjacency lists).

**Overall runtime: O(n + m).**
