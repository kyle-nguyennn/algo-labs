## Dynamic Programming Guidance #10

Solutions for Dynamic Programming (DP) Homework are in a written format with required components. This post is intended to give a general overview of those parts of such a solution.  You will also see quiz and exam questions based on what constitutes a complete solution for DP. 

General Rules
Submissions must be a Dynamic Programming approach to be eligible for points.

No recursion or memoization.

Inputs are always indexed starting from 1, unless stated otherwise (i.e. A[0] is usually invalid).

Inputs may not be modified - they are to be treated as immutable.

Tables may start from anywhere. If you need T[0] or T[-1] for a base case, this is valid as long as it is defined.

Tables may only store primitive values: integers, decimals, characters, or Booleans.

Required Sections
(a) Subproblem Definition

ALWAYS build on a subset of the input (e.g., A[1..i]).

Conceptually, the subproblem should always be defined against "previous" subproblems and not on the entire input.

Is represented using words: "T(i,j) is the ....."

Should use words from the problem statement without redefining their meaning

May or may not require inclusion of the last element: ", including A[i]"

The lectures use the phrase "which includes a[i]" to add the constraint "element a[i] must be used in the subproblem output." The phrases "which includes i" and "ending at a[i]" would also imply this constraint. These are not referring to the range of indices considered for the subproblem, 1,2,...,i, which is assumed inclusive  [1,i].

(b) Recurrence Definition

#11 #11 #11 Read, absorb, and love #11 #11 #11

Expressed using mathematical notation - no programming constructs and not in words

The table gets a single mathematical definition for all entries - there is no logic/flow control structure other than stating a set of conditional definitions.

Defines the value of all table entries recursively to smaller subproblems

Any referenced table entry must also be well-defined

i.e. a reference for T(i-2) for 1 <= i <= n requires a definition for T(-1)

It cannot be defined self-referentially (e.g. T(i) = max(T(i), ...))

When base case(s) are necessary, include them and their applicable bounds

Example: T(i,0) = 0 for 1 <= i <= n

Always provide bounds for any variables used, scoped to where they are used

Focus on table definitions, not a final solution (i.e. no return value)

(c) Implementation Analysis (1,2,3,4)

These parts should be based on the recurrence you use in the previous section.

(1) State the number of subproblems in big-O notation

This scales similar to runtime complexity

A one-dimensional table ranging from indices -1 to n would be O(n).

e.g. O(n), O(n*m)

(2) State the runtime to fill this table

Always, always in this course - worst case Big-O notation.

e.g. O(n^2)

(3) State how/where the final return is extracted from that table

e.g. sum{T(*)}, max{T(*)}, T(n), max(T(n), T(n-1))

(4) State the runtime to extract the final return in big-O notation

Tips and Tricks
You will be tempted to start with code. This is a terrible idea. Starting with code ensures your recurrence will be nearly impossible to craft. Do these sections in order - Dr. Vigoda does the same thing, and you should see how seamlessly the final solution comes together. Define a subproblem, which can then be translated to the mathematical recurrence, and the analysis can be easily derived from that.

The lectures contain multiple approaches (LIS, LCS, Knapsack, CMM, etc.). When solving a new problem, first try to think of which approach makes the most sense to adapt for a solution to the new problem.

Example Solution
Expand the spoiler below for an example of what a complete DP solution looks like:


Expand
Longest Increasing Subsequence (LIS) 
a. Define the entries of your table in words. E.g., T(i) or T(i, j) is ... 

Let T(i) = length of LIS in a[1...i] which includes a[i] 

b. State recurrence for entries of your table in terms of smaller subproblems. 

T(1) = 1

T(i) = 1 + max{T(j) if a[i] > a[j] : where 1 <= j <= i-1} 
     where 2 <= i <= n 
c. Implementation Analysis

(1) State the number of subproblems: O(n)
(2) State the runtime for table fill: O(n^2)
(3) State how the return is extracted: return max{T(*)}
(4) State the runtime of that return extraction: O(n)

Please use this thread to ask any follow-up questions regardin


## DP Recurrence Relations #11
This post is a brief discussion on math notation and the nature of recurrence relations. See post #10 which details the solution format for Dynamic Programming. 

---- Table of Contents -----
Context

What is a Recurrence Relation?

Examples

FAQ

----
1. Context:
Part 2, or the "recurrence relation", in a DP problem solution for this course is providing a mathematical definition of the table entries for the solution. In contrast, Part 1, or the "subproblem definition", is providing a short explanation in English explaining the meaning of each table entry, and Part 3, or the "Implementation Analysis", is an assessment of building and using this table defined in the "recurrence relation" to solve the original problem.

Think of it this way: the recurrence relation is the mathematical specification, and implementation would be the step by step algorithm or code that implements it.

2. What is a Recurrence Relation?
Dynamic Programming uses recurrence relations. Without a recurrence relation, a solution is not a Dynamic Programming solution.

Key characteristics of a recurrence relation:

A recurrence relation is an equation.

The equation provides a general rule for the recurrence.

The rule defines the next term as a function of the previous term(s).

To generate the sequence (or table) using the general rule, your general rule may depend on values being pre-defined for some early elements in this sequence, which are called base cases. Typically, separate equations are used for the base case(s). For example, here is a recurrence relation and base cases for LCS (DP1 lecture 24+):

Base cases:

L(i,0) = 0, 0 <= i <= n
L(0,j) = 0, 1 <= j <= n 

Recurrence: 

L(i,j) = max{L(i-1,j), L(i,j-1) },    if x_i != y_j 
       = 1 + L(i-1, j-1),             if x_i = y_j 

where i,j: 1 <= i <= n, 1 <= j <= n 

Note:

There are multiple base cases, and the bounds for the indices i and j are specified. If no indices are used (such as when there are only one or two individual base case table entries), bounds are not required. For example, T[1] = 1 does not have bounds because no variable is used.

The bounds for the indices in the base cases are different and specified separately from the bounds for recurrence relation. Frequently, the bounds will be slightly different between the base cases and the recurrence relation.

The bounds as provided convey directionality of your table fill. That is, when the range is 0 <= i <= n, we assume a fill order of left to right. If your approach depends on a right to left fill order (common for suffix-based approaches), then your bounds need to reflect this as well, such as n >= i >= 0.

Each unique table entry cannot be contradicted by setting it multiple times. In math, you cannot say "x=5" and "x=3" simultaneously. This should be reflected by comprehensive and mutually-exclusive conditions where otherwise can be used to specify "all other conditions".

Similarly, a table entry defined mathematically can only have one value. For example, in this example definition, L(0,7) is defined under the base cases, and L(1, 5) would be defined by one of the two options in the recurrence relation.

Exception: it is ok for the exact same table entry to be specified more than once in a recurrence relation, as long as it is set equal to the same value across all instances.

Table entries cannot be overwritten. While this would be acceptable in pseudocode where there is a sense of "before", "after", and "iterations", these concepts are not present in a mathematical definition. A table entry is not a temporary variable to store data in this context; it is a clearly, mathematically defined value. This point is similar to the previous bullet.

All table entries that are used to generate the value of any other table entry have a clearly defined value. In other words, there is no scenario where an undefined table entry is used to calculate the value of another table entry.

3. Examples
Example 1:

Example 1: Incorrect version 1 

Base Case: 
T[i] = 0, 0 <= i <= n 

Recurrence:
T[i] = T[i-1]+1, 1 <= i <=n 

What's wrong: Multiple assignments to the same elements. All the entries defined by the recurrence relation are overlapping with the base cases.

Example 1: Incorrect version 2 

Base Case: 
T[0] = 0 

Recurrence:
if i >= 1 T[i] = T[i-1]+1 

What's wrong: Incomplete bounds for i in the recurrence relation (needs to have a ceiling because our tables are finite in size), and use of an if statement construct (which is a pseudocode construct, and not a math construct). 

Example 1: Incorrect Version 3 

Base Case: 
for i = 0->n: T[i] = 0 

Recurrence: 
for i = 1->n: T[i] = T[i-1]+1 

What's wrong: This is completely pseudocode. for loop constructs are used, and the table entries are defined more than once. This is not a mathematical definition for table entries.

Example 1 (corrected):

Base Case: 
T[0] = 0 

Recurrence: 
T[i] = T[i-1]+1, 1 <= i <= n 

-----

Example 2:

Example 2: Incorrect version 

Base Case: 
T[0] = 0 

Recurrence: 
T[i] = max{T[i],T[i-1]+1}, 1 <= i <= n 

What's wrong: T[i] is on both the left and the right sides of the equation. The undefined T[i] is being used to define T[i]. With this incorrect version, it looks like there is an attempt to use pseudocode, but the mathematical definition for a recurrence relation is an equation and not a step-by-step procedure. Each table entry can only be defined once, and there is no such thing as "prior value."

Example 2 (corrected): 

Base Case: 
T[0] = 0 

Recurrence: 

T[i] = max{T[j]+1}, 1 <= i <= n and 0 <= j < i 
You can add helper indices if needed to access a range of previous table entries, as long as the helper indices are clearly defined (bounded). 

Other Notes:

Some ways you can write a range:

T[i] = 0, 0 <= i <= n 
T[i] = 0 where 0 <= i <= n 
T[i] = 0 s.t. 0 <= i <= n 
 

4. FAQ:
1. Q: Should table entries use [] or ()?
A: Either is fine, just be consistent. 

2. Q: Would you define an empty set/list/array as {}?
A: Yes, that's the standard notation. It can also be shown as the greek Phi ϕ, but do not use special symbols in Canvas submissions due to issues with porting format to the grading environment. 

3. Q: Can a base case be a non-discrete value, such as T[i,0] = T[i-1, 0]+1, 1<=i<=n as long as it's not the same as the recurrence function?
A: We are expecting base cases to be a terminating scenario that does not use recursion to produce an answer, such as a hard-coded value for those earlier elements of the table. 

4. Q: Are we allowed to use "or", "and", "||", "&&", logical not (!x), "infinity" in our recurrence definition?
A: Yes. 

5: Q: When is it ok to use "if" and not ok to use "if"?
A: You can use "if" for conditions (frequently on the right side of a multiline equation) to specify which right-hand side to use for an equation when defining a value. You cannot use an if statement (control of flow construct). 

6. Q. If we are using multiple tables, should each table have its own recurrence definition?
A: The recurrence section is made up of base case(s) and a general recurrence. Both tables need to fit into this singular structure. [NOTE: while using multiple tables can be a valid approach, it is almost always more complicated than necessary to solve a problem in our class.]

## Divide and Conquer Guidance #182

Below you will find information on how you should approach solving Divide & Conquer (D&C) problems in this class. In cases where the lecture material differs in format or content, this post supersedes those examples. 

Rules:

Submissions must be a Divide & Conquer approach to be eligible for points.

When asked to describe your solution in words, you may not use code/pseudocode

Each recurrence should be a smaller problem than before.

You must beat the brute force solution

You may leverage known algorithms mentioned as part of your solution, such as Binary Search, Merge Sort, Median of Medians (FastSelect), or FastMultiply. See #183 for further information and runtimes on these known algorithms.

You may also choose to modify a known algorithm (using the pattern and general logic, but adapting it to suit your needs). If you do so, you must (a) account for the run time impact of any modifications (b) justify why your approach, including the modifications, solve the problem.

Required Parts of a D&C Solution
(a) Algorithm. 

Describe "how" to solve the problem in words (narrative/paragraph form)

Bulleted steps are fine, but pseudocode/code is not allowed

"Pseudocode" includes line-by-line restatement of code as words. 

If you find yourself using a lot of nested bullets, you might be erring on the side of line-by-line conversion of code into words, which is not a narrative.

Must include all steps, including the final return

If you modify a known algorithm you must detail the modifications.

(b) Justification of Correctness. 

Describe "why" your algorithm solves the problem, in words (narrative). 

This is not a formal inductive proof; informal justification is ok.

If you modify a known algorithm you must include an explanation of why that modification is correct and effective.

(c) Runtime Analysis. 

Analyze all steps of the algorithm in Big-O notation. 

Always, always in this course - worst case Big-O.

Do not have to analyze O(1) steps

May assert known unmodified black-box runtimes without further justification

If a black box is modified, the runtime impact of those modifications must be justified, even if there is no impact.

Must provide an overall final runtime in (you guessed it) Big-O notation, fully simplified.

You should address each of the three components separately, and keep in mind that you are writing for an audience. The harder it is to find a required component the more likely you will be disappointed with your initial grade. There is no implicit justification of correctness within the algorithm steps; the correctness must be explicitly justified.

Steps to developing a D&C solution:
Figure out your pattern; it may (but does not have to) leverage a known algorithm

Sorted = Binary Search (usually)

Unsorted = Merge Sort or FastSelect (usually)

Polynomials, convolution, multiplication = FFT (usually)

State the modification of the known algorithm if needed. You may also use a known algorithm as is.

Which parts of the algorithm you are changing.

What are your inputs and outputs to the algorithm, if changed.

State the steps of your algorithm in words

Must include base case(s) if needed

Always return what the problem asks for

Prove Correctness

Explain why this algorithm solves the problem.

Not a formal/mathematical proof.

Examples of things you might cover:

Why use this black box? What qualities of the input allow you to take advantage of its use?

Why did you make a black box modification?

Why does the problem space get smaller on each round?

Why does the base case always hold true?

Why do we decide to branch left or right on each round?

Analyze the runtime.

## Usable D&C Algorithms #183
For the divide and conquer section, you may use the algorithms presented in the course materials to help you solve presented problems.

It may also be that the problem does not lend itself directly to one (or a combo) of the course algorithms, so you may choose to:

Leverage divide and conquer techniques directly, avoiding the use of course algorithms; or,

Make modifications to one or more of the course algorithms to make it fit the problem at hand

Any modifications made to the course algorithms must be described and have the impact of the changes accounted for in the runtime analysis.

Modifications listed below under "common modifications" do not need to be described in depth, but the use of a modified algorithm must be explicitly stated and an impact analysis must still be accounted for in the runtime analysis.

Many divide and conquer algorithms exist beyond what is covered in this course; however, only those explicitly mentioned here may be used. The use of extra-curricular algorithms will result in penalties.

Wikipedia entries are provided for supplemental reading, such as history and discovery of these algorithms.

Where differences exist, this post represents the version used in this course.

The following algorithms are available for use during the remainder of the course:

Binary Search (see also: https://en.wikipedia.org/wiki/Binary_search_algorithm)

Input:

A sorted list of comparable elements.

A starting index.

1 is assumed if not provided.

An ending index.

The size of the list (i.e., n) is assumed if the value is known.

The target value.

Output:

The index of the first encountered match if one exists or "NOT FOUND" if no match could be found.

Runtime:

O(log n)

Reference implementation:

binary_search(A, s=1, n, T)
    L = s
    R = n
    while L ≤ R do
        m = floor((L + R) / 2)
        if A[m] < T
            L = m + 1
        else if A[m] > T
            R = m − 1
        else
            return m
    return unsuccessful

Common modifications:

Finding the leftmost matching value.

Finding the rightmost matching value.

Finding the insertion point for a missing matching value.

Merge Sort (see also: https://en.wikipedia.org/wiki/Merge_sort)

Input:

A list of comparable elements.

A starting index.

1 is assumed if not provided.

An ending index.

The size of the list (i.e., n) is assumed if the value is known.

Output:

The original list, sorted in ascending order.

Runtime:

O(n log n)

Reference implementation (based on DPV pp. 50-51):

merge_sort(A, s=1, n)
    if n > 1
        return merge(merge_sort(A[s ... n/2],
                     merge_sort(A[n/2 + 1 ... n])
    else
        return A

merge(L[1 ... i], R[1 ... j])
    if i = 0
        return R
    if j = 0
        return L

    if L[1] ≤ R[1]
        return L[1] + merge(L[2 ... i], R[1 ... j])
    else
        return R[1] + merge(L[1 ... i], R[2 ... j])

Common modifications:

Returning the list in descending order.

Fast Select (see also: https://en.wikipedia.org/wiki/Selection_algorithm)

Input:

A list of comparable elements.

A starting index.

1 is assumed if not provided.

An ending index.

The size of the list (i.e., n) is assumed if the value is known.

An integer k

Output:

The kth smallest element from the original list.

Runtime:

O(n)

Reference implementation (based on DC2.12):

fast_select(A, s=1, n, k)
    if n = 1
        return A[1]

    i = s
    size = 0
    medians = []

    while (i + 4) ≤ n do
        medians += merge_sort(A, i, i+4)[3]
        size += 1
        i += 5

    if i ≤ n
        medians += merge_sort(A, i, n)[ceil((n - i + 1) / 2)]
        size += 1

    pivot = fast_select(medians, size / 2)

    lows = []
    mids = []
    highs = []

    lowSize = 0
    midSize = 0

    for i = s to n
        if A[i] < pivot
            lows += A[i]
            lowSize += 1
        else if A[i] > pivot
            highs += A[i]
        else
            mids += A[i]
            midSize += 1

    if k ≤ lowSize
        return fast_select(lows, k)
    else if k > lowSize + midSize
        return fast_select(highs, k - lowSize - midSize)
    else
        return pivot

Common modifications:

Return the kth largest element.

Fast Multiply (see also: https://en.wikipedia.org/wiki/Karatsuba_algorithm)

Input:

An n-bit integer x such that n = 2^k.

An n-bit integer y such that n = 2^k.

Output:

The product of x and y.

Runtime:

O(n^(log2 3))

Reference implementation (based on DPV p. 47, DC1.10)

fast_multiply(x[1 ... n], y[1 ... n])
    if n = 1
        return x * y

    xl = extract_bits(x, 1, n/2)
    xr = extract_bits(x, n/2 + 1, n)
    yl = extract_bits(y, 1, n/2)
    yr = extract_bits(y, n/2 + 1, n)

    A = fast_multiply(xl, yl)
    B = fast_multiply(xr, yr)
    C = fast_multiply(xl + xr, yl + yr)

    return 2^n * A + 2^(n/2) * (C - A - B) + B

Common modifications:

None.