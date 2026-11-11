# An upper bound to second order for the longest minimum-weight path in a complete graph

Yitzchak Shmalo, November 2026.

Give the edges of the complete graph K_n independent exponential weights of mean one. Between any two vertices
there is a unique path of minimum weight; its number of edges is the hopcount of the pair, and M_n is the largest
hopcount over all pairs. Addario-Berry, Broutin and Lugosi (2010) proved that M_n / log n converges in probability
to alpha = 3.5911..., the root of alpha log alpha - alpha = 1, with
alpha log n - L log log n <= M_n <= alpha log n + omega(n) with high probability.

Write b_n = alpha log n - (log log n) / (2 log alpha). The paper proves that

- P(M_n >= b_n + x) <= C alpha^(-x) for all n >= 3 and x >= 0, so M_n - alpha log n tends to minus infinity in
  probability and E M_n <= b_n + O(1);
- the expected number of pairs at hopcount at least k_n equals (C_* + o(1)) alpha^(-(k_n - b_n)) when
  k_n - alpha log n = O(log log n), with C_* = 0.01104...;
- at k_n = ceil(b_n) the second moment of that number is at least c n^(5 - alpha log 4) times a power of log n, and
  so tends to infinity although the mean stays bounded;
- P(M_n = n - 1) = n / (2 (n-1)!) for every n >= 2.

This concerns Open Problem 3.1 in van der Hofstad's Saint-Flour lecture notes "Stochastic processes on random
graphs" (2017), which asks for the fluctuations of M_n - alpha log n. The upper side is improved to the scale
log log n; a matching lower bound is not obtained, and the question stays open on that side.

## Files

- `longest_geodesic.pdf`, `longest_geodesic.tex`, `sec_*.tex`, `tail.tex`, `bib_*.tex`: the paper.
- `code/first_moment.py`: exact expected number of pairs at hopcount at least k, the ratios quoted after Theorem 2
  and the levels used in Tables 1 and 2 (`python first_moment.py data/first_moment.json`).
- `code/check_small.py`: enumeration of recursive trees with at most 8 vertices and Monte Carlo on K_3,...,K_6
  (`python check_small.py 100000 20261111 data/check_small.json`).
- `code/sim_mn.c`: simulation of M_n by Dijkstra's algorithm from every vertex
  (`cc -O3 -o sim_mn sim_mn.c -lm; ./sim_mn n graphs seed out_prefix`).
- `code/summarize_sim.py`: summary of the simulation output against the exact first moment
  (`python summarize_sim.py data/sim data/sim_summary.json`).
- `code/check_rep.c`: regenerates one graph of a simulation run and recomputes its longest minimum-weight path by
  the Bellman-Ford recursion with a bounded number of edges
  (`cc -O2 -o check_rep check_rep.c -lm; ./check_rep 250 3210 101`).
- `code/root_tail.py`: exact law of the height of a random recursive tree by a recursion over the size of the
  subtree of the second vertex, compared with the expected number of deep vertices
  (`python root_tail.py 32000 law > data/root_tail.log`).
- `data/`: outputs of the programs above; `data/sim/` holds, for each run, the values of M_n and of the largest
  hopcount from vertex 1 for every sampled graph, and the histogram of hopcounts over all pairs.

The paper is part of the Math Brain project: https://github.com/yspennstate/math-brain-public
