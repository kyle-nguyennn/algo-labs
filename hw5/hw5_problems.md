## Practice Problems

### [DPV] Problem 3.3 (Topological ordering example)
Given graph the below graph. Perform DFS with pre and post order number. Whenever there's a need to select what vertex to explore, choose in alphabetical order.
A --> C ---> D --> F ---> G
      ^  |         ^  |    
      |  |         |  |    
B -----  --> E -----  --> H
a. Whats the pre and post order number?
b. What are the sources and sinks of the graph?
c. What is the topological ordering found by the algorithm?
d. How many topological ordering are there in this graph?

#### Solution
a. 
A (1,14) --> C (2,13) ---> D (3,10) --> F (4,9) ---> G (5,6)
             ^         |                ^        |    
             |         |                |        |    
B (15,16) ----         --> E (11,12) ----        --> H (7,8)

b. Sources: A, B. Sinks: G, H.

c. Sorted by post-order number decreasing: B, A, C, E, D, F, H, G.

d. 8 valid topological orderings. Since (A,B), (D,E), (G,H) can interchange their internal positions -> 2^3 options.

### [DPV] Problem 3.4 (SCC algorithm example)
[Problem statements]
#### Solution


### [DPV] Problem 3.5 (Reverse of graph)
[Problem statements]
#### Solution


### [DPV] Problem 3.15 (Computopia)
[Problem statements]
#### Solution


## Graded Problem

Let G=(V,E) be a directed graph. A vertex v is well connected if for every vertex w in the graph, there is a path from v to w, or there is a path from w to v (both may exist, but at least one must be present).

Design an algorithm that returns a well connected vertex, if such a vertex exists, and returns no otherwise.

### Solution

a. The algorithm:



b. Justification of Correctness:



c. Runtime analysis:

