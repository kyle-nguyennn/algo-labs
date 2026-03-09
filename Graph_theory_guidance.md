## Graph Theory Guidance #483

### Context

A graph theory problem is a form of **reduction**. You are given some problem to solve, and the challenge is to solve it by using one of the graph algorithms we study this semester. In other words, you reduce your problem to a graph problem such that a known algorithm can solve it for you.

The known algorithms (#484) are treated as a **black-box** — you are not allowed to change or modify them in any way. You can (and often will) modify the original problem input in some way or create a graph which represents the input — this becomes the input to the black-box. You then use the outputs from the black-box (possibly with modification) to output a solution to the original problem.

### Rules

> **NO PSEUDOCODE — YOU WILL LOSE A LOT OF POINTS**

- You may **only** use known black box algorithms (#484).
- You **must** use one or more black box algorithms (#484) to solve problems.
- You **must not** modify any black box algorithms (#484). Re-creating a black box with modifications counts as a modification.
- All graphs are in adjacency list format (see [Graph Representation](#graph-representation) below).
- You can assume you always have **n** and **m** for runtime analysis, where **n = |V|** (vertices) and **m = |E|** (edges).
- See #7 for common course runtimes, including operations performed on graphs.

### Required Parts of a Graph Theory Solution

Every graph theory solution must include the following three parts:

#### (a) Algorithm

Describe **how** to solve the problem in words (narrative/paragraph form).

- Bulleted steps are fine, but pseudocode/code is **not allowed**.
    - "Pseudocode" includes line-by-line restatement of code as words.
    - If you find yourself using a lot of nested bullets, you're likely writing pseudocode in disguise.
- Describe what modifications are performed to the input, if any.
- Detail the black box algorithm(s) being used:
    - What is passed in as input.
    - What is being used from its output.
- Describe what modifications are performed to the output, if any.
- Repeat as needed for any other black boxes.
- Detail the final return for the problem's solution.

#### (b) Justification of Correctness

Describe **why** your algorithm solves the problem, in words (narrative).

- This is **not** a formal inductive proof; informal justification is fine.
- Explain how your problem is solved by the black boxes used.
- Explain how changing the inputs and/or outputs gets what you want.

#### (c) Runtime Analysis

Analyze all steps of the algorithm in **worst-case Big-O** notation.

- You can assert known black-box runtimes without further justification.
- Must include runtime analysis for any pre/post processing (see #7 for common graph runtimes).
- Provide an overall final runtime in Big-O, **fully simplified**.
- If the problem specifies a target runtime, you must meet it for full credit. Otherwise, faster (and correct) solutions earn more credit.
- Use **tightest-bound** worst-case runtimes:
    - Even though the worst case for an O(n+m) operation occurs when m = n², it is incorrect to state O(n²) unless we know something about the graph (e.g., it is a clique). O(n+m) is the tightest bound.
    - If the graph is a tree, then m = n−1, and O(n+m) collapses to O(n).
- When stating runtimes of black boxes, you are **not required** to simplify, even if the graph's constraints would allow it.

### Graph Representation

Graphs in this class, unless stated otherwise:

- Are **simple graphs** (no multi-edges or self-loops)
- Are always given in **adjacency list format** (see DPV 3.1.1)
    - An array of vertices → linked lists of adjacent vertices, where each list element represents an edge.
    - Vertices are labeled such that they can be found by indexing into the array.
- Can be connected or disconnected, undirected or directed, sparse or dense
    - If unstated by the problem, assume **any** of these could be true.
- Are **connected and undirected** when working with MSTs.
- Are **connected and directed** when working with flow networks.

#### Common Graph Operations

The following actions can be described without going into implementation details. Each is assumed to be an **O(n + m)** operation:

| Operation | Example phrasing |
|---|---|
| Reversing a graph | "Reverse the edges in the graph" |
| Copying a graph | "Create a copy of G and call it G_copy" |
| Creating subgraphs | "Create a copy of G called G_even that only keeps edges with even weights" |
| | "Create a copy of G called G_k that only keeps vertices with degree > k" |
| | "Create a residual graph of G called G_rs using the flows from our run of EK" |

## Usable Black Boxes for Graphs #484

For the graphs section, you must use the algorithms presented in the course materials to help you solve presented problems. Solutions must use one (or a combo) of the black boxes below. Providing full implementation details of a black box with a twist or in-line tracking will be treated as a modification.

> **Important:** Only the algorithms listed here may be used. The use of extra-curricular algorithms will result in penalties, including for variations outside of the lectures, book, and this post. Where differences exist, this post represents the version used in this course.

**Conventions:**
- All runtimes assume **n = |V|** (vertices) and **m = |E|** (edges).
- All outputs are produced as n-sized lists, indexed by vertex in O(1) time, unless otherwise noted.
- Wikipedia entries are provided for supplemental reading.

---

### 1. Depth-First Search (DFS) [Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)

**Input:**
- A simple graph in adjacency list format
- A starting vertex *(optional — if not provided, DFS starts from an arbitrary location via adjacency list ordering)*

**Internal** *(not accessible after run):*
- `visited[]` — Whether the indexed vertex was touched by DFS. All entries will be `true` when DFS completes. Populated by Explore, an internal subroutine.

**Output:**
- `ccnum[]` — Connected component number of the indexed vertex. Vertices reachable from the starting vertex have ccnum = 1.
- `prev[]` — Parent vertex of the indexed vertex (used to construct a path from the start). Unreachable vertices and the start vertex have `nil`.
- `pre[]` — Pre-visit number for the indexed vertex.
- `post[]` — Post-visit number for the indexed vertex.

**Runtime:** O(n + m)

**References:** DPV pp. 83–91 · GR1.3, GR1.6

**Common uses:**
- Finding connected components
- Finding a cycle in a graph
- Producing a path from starting vertex to a reachable vertex

---

### 2. Topological Sort [Wikipedia](https://en.wikipedia.org/wiki/Topological_sorting)

**Input:**
- A simple, **directed, acyclic** graph in adjacency list format

**Output:**
- `order[]` — Vertices sorted in topological ordering from source to sink. *(Indexed numerically, not by vertex.)*
- All outputs from the underlying DFS run are also available.

**Runtime:** O(n + m)

**References:** DPV pp. 89–91 · GR1.10

**Common uses:**
- Finding the topological sorting in a DAG

---

### 3. Strongly Connected Components (SCC) [Wikipedia](https://en.wikipedia.org/wiki/Strongly_connected_component)

**Input:**
- A simple, **directed** graph in adjacency list format

**Output:**
- `G_SCC = (V_SCC, E_SCC)` — The SCC metagraph in adjacency list format. By construction, the metagraph is a DAG with vertices sorted from sink to source (reverse topological ordering).
- All outputs from the final DFS run are also available. This data connects entities in the metagraph to the original graph (e.g., the first vertex in V_SCC represents all vertices with `ccnum[v] = 1`).

**Runtime:** O(n + m)

**References:** DPV pp. 91–95 · GR1.21

**Common uses:**
- Finding strongly connected components
- Finding source and sink SCCs

---

### 4. Breadth-First Search (BFS) [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)

**Input:**
- A simple graph in adjacency list format
- A starting vertex

**Output:**
- `dist[]` — Unweighted distance from the starting vertex to each vertex. Unreachable vertices have distance ∞.
- `prev[]` — Parent vertex of the indexed vertex. Unreachable vertices and the start vertex have `nil`.

**Runtime:** O(n + m)

**References:** DPV pp. 105–106 · GR1.24

**Common uses:**
- Reachability analysis
- Unweighted shortest path determination
- Producing a path from starting vertex to a reachable vertex

---

### 5. Dijkstra's [Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

**Input:**
- A simple graph in adjacency list format
- A starting vertex
- A list of **non-negative** edge weights

**Output:**
- `dist[]` — Weighted distance from the starting vertex to each vertex. Unreachable vertices have distance ∞.
- `prev[]` — Parent vertex of the indexed vertex. Unreachable vertices and the start vertex have `nil`.

**Runtime:** O((n + m) log n)

**References:** DPV pp. 109–115 · GR1.24

**Common uses:**
- Reachability analysis
- Weighted shortest path determination
- Producing a path from starting vertex to a reachable vertex

---

### 6. Bellman-Ford (BF) [Wikipedia](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

**Input:**
- A simple graph in adjacency list format
- A starting vertex
- A list of edge weights

**Output:**
- `dist[]` — Weighted distance from the starting vertex to each vertex (based on the (n−1)th iteration). Unreachable vertices have distance ∞.
- `prev[]` — Parent vertex of the indexed vertex. Unreachable vertices and the start vertex have `nil`.
- `iter[][]` — 2D list where `iter[i][v]` is the shortest-path distance from the start to v at the end of iteration i. Contains iterations 0 through n.

**Runtime:** O(nm)

**References:** DPV pp. 115–119 · DP3.6

**Common uses:**
- Reachability analysis
- Weighted shortest path determination
- Negative cycle detection
- Producing a path from starting vertex to a reachable vertex

---

### 7. Floyd-Warshall (FW) [Wikipedia](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)

**Input:**
- A simple graph in adjacency list format
- A list of edge weights

**Output:**
- `dist[][]` — 2D list where `dist[u][v]` is the shortest-path distance from u to v (based on the nth iteration). Unreachable pairs have distance ∞.
- `iter[][][]` — 3D list where `iter[k][u][v]` is the shortest-path distance from u to v at the end of iteration k. Contains iterations 0 through n.

**Runtime:** O(n³)

**References:** DPV pp. 172–173 · DP3.17

**Common uses:**
- Reachability analysis
- Weighted shortest path determination
- Negative cycle detection

---

### 8. Kruskal's [Wikipedia](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm)

**Input:**
- A simple, **connected, undirected** graph in adjacency list format
- A list of edge weights

**Output:**
- `edges[]` — A list of n−1 edges representing a minimum spanning tree.

**Runtime:** O(m log n)

**References:** DPV pp. 128–137 · GR3.6

**Common uses:**
- Producing a minimum spanning tree

---

### 9. Prim's [Wikipedia](https://en.wikipedia.org/wiki/Prim%27s_algorithm)

**Input:**
- A simple, **connected, undirected** graph in adjacency list format
- A list of edge weights

**Output:**
- `prev[]` — Parent vertex of each vertex, representing the connecting edges of a minimum spanning tree. The starting vertex (chosen arbitrarily) has `nil`.

**Runtime:** O(m log n)

**References:** DPV pp. 137–139 · GR3.15

**Common uses:**
- Producing a minimum spanning tree

---

### 10. Ford-Fulkerson (FF) [Wikipedia](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)

**Input:**
- A simple, **connected, directed** graph in adjacency list format
- A list of **positive, integer** edge capacities
- A starting source vertex
- A terminating sink vertex

**Output:**
- `flow[]` — Capacity used per edge such that flow is maximized from source to sink.
- `C` — The value of the maximum flow.

**Runtime:** O(mC)

**References:** DPV pp. 198–204 · MF1.14

**Common uses:**
- Finding max flows on a graph

---

### 11. Edmonds-Karp (EK) [Wikipedia](https://en.wikipedia.org/wiki/Edmonds%E2%80%93Karp_algorithm)

**Input:**
- A simple, **connected, directed** graph in adjacency list format
- A list of **positive** edge capacities
- A starting source vertex
- A terminating sink vertex

**Output:**
- `flow[]` — Capacity used per edge such that flow is maximized from source to sink.
- `C` — The value of the maximum flow.

**Runtime:** O(nm²)

**References:** DPV pp. 198–204 · MF4.3

**Common uses:**
- Finding max flows on a graph

---

### 12. 2-SAT [Wikipedia](https://en.wikipedia.org/wiki/2-satisfiability)

**Input:**
- A Boolean formula in CNF where each clause contains at most 2 literals, backed by n variables (≤ 2n literals) and m clauses.

**Output:**
- `assignments[]` — Whether each variable is `true` or `false`. Returns `"NO"` if unsatisfiable.
- All outputs from the underlying SCC run are also available.

**Runtime:** O(n + m)

**References:** DPV p. 101 · GR2

**Common uses:**
- Solving problems from non-graph domains via graph reduction
- Converting a graph representation into a Boolean formula to determine satisfiability