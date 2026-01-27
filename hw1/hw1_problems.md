## Practice Problem
### [DPV] Problem 6.4 – Dictionary lookup
You are given a string of n characters s[1...n], which you believe to be a corrupted text document in which all punctuation has vanished...

### [DPV] Problem 6.8 – Longest common substring
Given two strings x = [1...n] and y = [1...m], we wish to find the length of their longest common substrings...

### [DPV] Problem 6.18 – Making change II
Consider the following variation on the change-making problem (Exercise 6.17): you are given denominations , ...

### [DPV] Problem 6.19 – Making change k
Given an unlimited supply of coins of denominations , we wish to make change for a value v using at most k coins...

### [DPV] Problem 6.20 – Optimal Binary Search Tree
Suppose we know the frequency with which keywords occur in programs of a certain language, for instance ...

### [DPV] Problem 6.26 – Alignment
Sequence alignment. When a new gene is discovered, a standard approach to understanding its function is to look through a database of known genes and find close matches

## Graded Problem

Dr. Brito's son Oliver has entered a fundraising contest at school, with the task of providing custom made ragdolls for charity. Whichever students produces the most ragdolls wins A Major AwardLinks to an external site..

To help Oliver win, Dr. Brito enlists the help of his friends Claude and Gemma to establish a Multi-Conveyer Pipeline (MCP), with the goal of assembling as many ragdolls as quickly as they can.

Each ragdoll assembly is composed of n steps, measured in positive minutes. The time it takes Claude to perform each step is provided as C, and for Gemma as G.

After some trial runs, Dr. Brito identifies that this can be further optimized by using a strategic Line Switching Protocol (LSP), even though it takes 1 minute to switch between Claude and Gemma, if the task performance differential is high enough.

Given that Claude is a Milwaukee fan and Gemma is a DeWalt fan, Dr. Brito also noticed that the time to setup their line and package a ragdoll is different for both Claude and Gemma, denoted as positive minutes Cs, Gs, Cp, and Gp.

After getting Claude and Gemma's prompt attention, and giving them all the context they need, they're ready to begin.

Dr. Brito then says "I think we should turn on the light before we get to work", to which both say "You're absolutely right!" in unison.

Let's minimize ragdoll production time to help Oliver win!

Example: For C = [1, 1, 2], G = [1, 1, 1], and assuming Cs, Gs, Cp, and Gp are all 1, the minimum time to make a ragdoll is 5 minutes, as Claude will sit idly by as Gemma does all the work, including setup and packaging.

Example: For C = [1, 2, 3], G = [3, 2, 1], and assuming Cs, Gs, Cp, and Gp are all 1, the minimum time to make a ragdoll is 7 minutes. Claude begins building the ragdoll through step 2, then switches to Gemma to finish off with step 3. If either Claude or Gemma tried to build the ragdoll themselves, it would have taken 8 minutes.

Design a Dynamic Programming Algorithm that takes as input C, G, Cs, Gs, Cp, and Gp, and outputs the minimum time to produce a ragdoll.

Please answer the following parts:
Define the entries of your table in words. E.g. T(i) or T(i, j) is ...
State a recurrence for the entries of your table in terms of smaller subproblems.  Don't forget your base case(s).
Analyze an implementation of this recurrence:
State the number of subproblems in big-O notation.
State the runtime to fill your table using your recurrence from part 2.
State how the return is extracted from your table. 
State the runtime of that return extraction.