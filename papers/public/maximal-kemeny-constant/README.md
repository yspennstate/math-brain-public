# The maximal Kemeny constant of an n-vertex graph

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem

For simple random walk on a connected simple graph with n vertices, Kemeny's constant is at most n³/54 + (37/8) n^(5/2), and two complete graphs of order ⌊n/3⌋ joined by a path attain the leading term. The maximum of Kemeny's constant over connected n-vertex graphs is therefore asymptotic to n³/54. This proves the Kemeny-constant assertion of Open Problem 6.13 in D. Aldous and J. A. Fill, *Reversible Markov Chains and Random Walks on Graphs*. The relaxation-time assertion of the same problem, proved by Aksoy, Chung, Tait and Tobin (Adv. in Appl. Math. 101 (2018), 1–14), also follows from the bound, because the relaxation time never exceeds Kemeny's constant.

The proof is elementary. It uses the effective-resistance formula for Kemeny's constant, contracts the neighbourhoods of high-degree vertices, and bounds each edge of a spanning tree by a two-mass inequality. The same argument gives the maxima over K_{r+1}-free graphs and over graphs of chromatic number at most r: both are (1 − 1/r) n³/54 + O(n^(5/2)), so the triangle-free and bipartite constants are 1/108.

## Files

- `paper/main.pdf`: the paper
- `paper/main.tex`: LaTeX source

## Citation

Y. Shmalo, *The maximal Kemeny constant of an n-vertex graph*, 2026. https://github.com/yspennstate/maximal-kemeny-constant
