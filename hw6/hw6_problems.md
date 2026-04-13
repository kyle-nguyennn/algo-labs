## Practice Problems

### [DPV] Problem 4.14 (Shortest path through a given vertex)
[Problem statements]
#### Solution
[TODO]:


### [DPV] Problems 5.1, 5.2 (Practice fundamentals of MST designs)
[Problem statements]
#### Solution


### [DPV] Problem 5.9 (multiple statements about MST. We will provide the answer to a few, you are welcome to try them all)
[Problem statements]
#### Solution

---
<div style="page-break-before: always;"></div>

## Graded Problem

The Georgia Tech Marathon committee is planning a route from the Klaus Advanced Computing Building to the Skiles Test Preparation Building. The campus is modeled as a weighted, undirected graph G=(V,E) where each edge represents a street with a weight w(e) corresponding to its width. To accommodate a large volume of runners, the committee must select a path such that the width of the narrowest street in the path is maximized. Design an algorithm to find the optimal route.
Your input is a weighted graph G=(V,E), with weights w(e)>0. You are also given vertices s and t, representing Klaus and Skiles, respectively. Your algorithm must return the actual path.

### Solution

a. The algorithm:
We first negate all edge weights in G, creating a new weight list w'(e) = -w(e) for every edge. Then we run Kruskal's algorithm on G with the negated weights w'. Since Kruskal's finds the minimum spanning tree, using negated weights gives us a maximum spanning tree T of the original weights.

Now we run DFS on T starting from vertex s. From the DFS output, we use prev[] to trace the path from t back to s: starting at t, we follow prev(t) to its parent, then prev of that parent, and so on until we reach s. We reverse this sequence to get the path from s to t. Return this path.

b. Justification of Correctness:
Negating the weights and running Kruskal's gives us a maximum spanning tree T, because minimizing the sum of negated weights is the same as maximizing the sum of original weights. Since T is a tree, there is exactly one path between any two vertices, including s and t.

We claim the path from s to t in T maximizes the minimum edge weight. Suppose P is the path from s to t in T, and the edge with minimum weight (the bottleneck) in P is e*. Now if we remove e* from T, it splits T into 2 connected components A and B, with s in A and t in B. Assume there exists some other path P' from s to t where every edge has weight strictly greater than edge e*.

This path P' must have an edge f that crosses the cut A,B and w(f) > w(e*) since all edges in P' are strictly greater than e*. Then if we add f to T-{e*}, we form a spanning tree with total weights larger than original T. This leads to a contradiction because we define T to be the maximum spanning tree. So no better path exists, and the path P is optimal.

DFS on the tree T produces prev[], which we use to reconstruct the unique path from s to t.

c. Runtime analysis:
- Negating all edge weights takes O(m) since we go through every edge once. 
- Running Kruskal's on G takes O(m log n). 
- The tree T has n-1 edges, so DFS on T takes O(n + (n-1)) = O(n). 
- Reconstructing the path from prev[] takes at most O(n) since the path can visit at most n vertices.

Overall runtime: O(m log n).