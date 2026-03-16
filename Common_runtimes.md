## Common Course Runtimes #7

When performing runtime analysis for this course, we expect **worst-case** runtime analysis in **fully simplified Big-O** notation.

> For example, O(2n + 3n) is expected to be presented as **O(n)**.

This post presents the runtimes associated with common actions you may describe in your algorithms. When no supporting details are presented for special handling in a submission, the **default action** and associated runtimes will prevail.

For all runtimes below, **n** represents the length or size of the object being used.

---

### List

In this course, lists are treated as standard arrays, indexable by integers starting at 1.

| Operation | Runtime |
|---|---|
| Creating a list (empty) | O(1) |
| Creating a list with initial contents | O(n) |
| Adding an item to a list *(appends to the end)* | O(1) |
| Adding an item to a specific non-tail location | O(n) |
| Remove an item from a list *(swap tail element and pop)* | O(1) |
| Remove an item while maintaining order | O(n) |
| Check the length of a list *(via counting)* | O(n) |
| Check if a list contains an element *(via scanning)* | O(n) |

---

### Hash Table / Hash Set / Map / Set

> While common and practical for software development, these data types have **worst-case performance** that generally makes them undesirable. Unless the problem gives you data in this format (typically as a set), you are unlikely to need this.

| Operation | Runtime |
|---|---|
| Creating a hash table (empty) | O(1) |
| Creating a hash table with initial contents | O(n²) |
| Adding an item to a hash table | O(n) |
| Remove an item from a hash table | O(n) |
| Check the length of a hash table *(via counting)* | O(n) |
| Check if a hash table contains an element *(via scanning)* | O(n) |

---

### Graph

Graphs are always treated as adjacency lists, with an indexable list of vertices each pointing to a linked list of adjacent vertices. Assume you know **n = |V|** (vertices) and **m = |E|** (edges).

| Operation | Runtime | Notes |
|---|---|---|
| Traversing a graph | O(n+m) | Includes reversing, copying, subgraphing, or anything working with all vertices and edges |
| Operating on a single vertex v | O(1) | Includes find, read, removal |
| Operating on all (or a subset of) vertices V | O(n) | Includes find, read, removal |
| Operating on a single edge e=(u,v) | O(n) | Must traverse up to n vertices in u's adjacency list to find v. Includes find, read, removal |
| Operating on all edges \|E\| | O(n+m) | Includes find, read, removal |
| Accessing properties of an edge or vertex | O(1) | Assumes you already have access to the vertex/edge (e.g., weight, color, cost, capacity) |

---

### Simplification Notes

If you **know** something about the connectivity of a graph, some runtimes can be simplified:

| Condition | Simplification |
|---|---|
| Graph is **connected** (m ≥ n−1) | O(n+m) = O(m+m) = O(2m) = **O(m)** |
| Graph is a **clique** (m = n(n−1)/2) | O(n+m) = O(n+n²) = **O(n²)** |