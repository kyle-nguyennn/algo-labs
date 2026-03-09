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


## Graded Problem

The Georgia Tech Marathon committee is planning a route from the Klaus Advanced Computing Building to the Skiles Test Preparation Building. The campus is modeled as a weighted, undirected graph G=(V,E) where each edge represents a street with a weight w(e) corresponding to its width. To accommodate a large volume of runners, the committee must select a path such that the width of the narrowest street in the path is maximized. Design an algorithm to find the optimal route.
Your input is a weighted graph G=(V,E), with weights w(e)>0. You are also given vertices s and t, representing Klaus and Skiles, respectively. Your algorithm must return the actual path.

### Solution

a. The algorithm:
We use a modified version of Djikstra algorithm to solve this problem.
Modifications: dist will store the minimum weight of the optimal path from starting index to the indexed vertex, for all vertices of the graph. Initialize dist to be -1 for all vertices, except dist of starting vertex s to be w(s).

Use a max-heap to main the vertex with the largest minimum weight on the path from the starting vertex. 

For a vertex u at the top of the max-heap: we update dist(v) := min(dist(u), w(v)) if dist(v) < min(dist(u), w(v)), for all v that are connected to u. We keep track of prev(v) = u, if the optimality update occurs for v.

We stop the process when t is at the top of the queue or the queue is empty. The output of the problem is dist(t).

b. Justification of Correctness:
The modified version finds the path with maximum distance in the graph. The distance here is calculated as the minimum weight along the path, which is abstracted from the djikstra algorithm, since Djikstra can be used to find the minimum of an arbitrary score calculated along a path, as long as the score are non-negative.

The optimality update happens if it increase the score (dist) of the path. This can't keep increasing the dist forever because of the contraint of the way score is calculated: min(dist(u), w(v)). Even if we add more vertex to the existing path, the score can only stays the same or go down, hence nodes in the same cycle won't be repeated as it does not improve the optimal score.


c. Runtime analysis:
Calculation of the score takes O(1). Operations on max-heap is the same as operations on min-heap. Hence the run time of the modifed version above is the same as the original Djikstra algorithm: O((n+m) log n).