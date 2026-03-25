## Graph black-blox algorithms

### I. Connectivity and reachability
#### 1. DFS
Input: graph in adj list, a starting vertex
Internal (not accessible after run): visited
**Output: ccnum, prev, pre, post**
Runtime: O(n+m)

#### 1. Topological sort
Input: DAG graph in adj list
Output: order - vertices sorted in topological ordering **from source to sink. DFS output**
Runtime: O(n+m)

#### 3. SCC - Kosaraju
Input: graph in adj list
Output: **DAG metagraph with vertices sorted from sink to source (reversed topo), DFS_output**
Runtime: O(n+m)

### II Shortest path
#### 4. BFS:
Input: graph in adj list, starting vertex
Output: dist and prev array
Runtime: O(n+m)

#### 5. Djikstra:
Input: simple graph in adj list, starting vertex, **list of non-negative edge weights**
Output: dist and prev array
Runtime: O((n+m) log n)

#### 6. Bellman-Ford:
Input: simple graph in adj list, starting vertex, list of edge weights
Output: dist and prev array, **iter[][] where iter[i][v] is the shortest-path from starting vertex to v in iteration i**
**Runtime: O(nm)**

#### 7. Floy-Warshall (all-pair shortest path)
Input: simple graph in adj list, list of edge weights
Output: dist[][] - where dist[u][v] is the shortest path between u and v
        **iter[][][] - 3D list where iter[k][u][v] is the shortest path between u and v in iteration k**
**Runtime: O(n^3)**

### III. MST
#### 8. Kruskal:
Input: simple **connected, undirected graph in adj list**; a list of edge weights
Output: edges[] - edge list of the MST
**Runtime: O(m log n)**

#### 9. Prim:
Input: simple **connected, undirected graph in adj list**; a list of edge weights
Output: prev[] to reconstruct the tree
**Runtime: O(m log n)**


### IV. Maxflow - Mincut
#### 10. Ford-Fulkerson
Input: 
    - **simple connected, directed graph in adj list**
    - a list of **positive, integer value** edge capacities
    - **a source vertex s**
    - **a sink vertex t**
    
Output: 
    - flow[] - an array of flow assignment to each edge **that maximize the flow from source to sink**
    - **c - the value of the maximum flow**
Runtime: O(mC)

#### 11. Edmonds-Karp
Input:
    - a simple connected, directed graph in adj list
    - a list of **positive** edge capacities
    - a source vertex s
    - a sink vertex t
Output:
    - flow[] - the flow assignment to each edge to maximize the flow from source to sink
    - c - the value of the maximum flow
Runtime: O(nm^2)

#### 12. 2-SAT
Input: a boolean expression in Conjunctive Normal Form (CNF), **i.e. each clause contains at most 2 literals (A OR B), backed by n variables and m (AND) clause.**
Output: assignments[] - an assignment of T/F for each variable in the expression. **Returns NO if unsatisfiable**
Runtime: **O(n+m)** (Finding SCC and check if any x and its negation are in the same SCC)