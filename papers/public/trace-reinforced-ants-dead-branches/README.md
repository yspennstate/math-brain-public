# Dead branches in the trace-reinforced ant process

Yitzchak Shmalo

This repository contains a paper on the trace-reinforced ant process of Kious, Mailler and Schapira
(*The trace-reinforced ants process does not find shortest paths*, J. Éc. polytech. Math. 9 (2022), 505-536),
together with the programs and data behind every numerical value in it.

Paper: [dead_branches.pdf](dead_branches.pdf) (source [dead_branches.tex](dead_branches.tex)).

## Summary

Ants walk one at a time from a nest N to a food source F on a finite graph. Each ant performs a random walk weighted
by the current edge weights, and when it reaches F every edge it crossed gains weight 1. Kious, Mailler and Schapira
conjectured that the normalised weights W(n)/n converge almost surely to a deterministic limit, and that every edge
has a positive limit when N and F are at distance at least 2.

* Dead branches (Theorem 2). Let u be a neighbour of F and let H be a set of vertices, not containing N, F or u, that
  is joined to the rest of the graph minus F by a single edge {u, y}. Then W_f(n)/n tends to 0 almost surely for
  every edge f with an endpoint in H. The 4-cycle N, a, F, b with one more vertex joined to a and to F is a
  2-connected example with N and F at distance 2, so the second part of the conjecture fails.
* Shadowed neighbours of F (Theorem 5). Let I be the component of N after F and its neighbours are removed. If some
  neighbour of F has no neighbour in I, the mean-field map has no equilibrium with all coordinates positive, so the
  two parts of the conjecture cannot both hold on that graph. The complete bipartite graph K_{3,3} with N and F on
  the same side, plus one edge from F to the third vertex of that side, is a 3-connected example.
* A corrected form of the second part (Conjecture 9): an explicit set D(G, N, F) of edges that should be exactly the
  edges with limit 0. In the mean-field flow this holds on the 22,828 cases with 3 to 7 vertices (in one of them
  after a longer integration, see `code/rerun_3769.py`).
* Theta graphs (Proposition 10). For k internally disjoint paths of lengths L_1, ..., L_k between N and F, the
  weights alpha_i^j on the j-th edge of path i form an equilibrium, where the alpha_i solve
  sum_i alpha_i^{L_i} = 1 with (1 - alpha_i) / (1 - alpha_i^{L_i}) the same for all i. Equal lengths give
  alpha = k^(-1/L).

## Code

The programs need Python 3 with NumPy and NetworkX. Run them from the `code` directory. Saved outputs are next to
them.

* `ants_core.py`: the crossing probabilities p_e(w) by one linear solve per edge, Newton's method on a given
  support, and the stability data of an equilibrium.
* `ants_fast.py`: the same probabilities from a single Green's matrix; `python3 ants_fast.py test` compares the two.
* `ants_exact.py`: the census. `python3 ants_exact.py 3 6 6 4 out.jsonl` solves every connected graph with 3 to 6
  vertices and every pair (N, F) up to automorphism, from six initial conditions each; `7 7` in place of `3 6` gives
  the 21,090 cases with 7 vertices.
* `dead_set.py`: the edge set of Theorem 2 and the set D(G, N, F) of Conjecture 9.
* `table.py` (output `table_out.txt`): the table of Section 4 from the census files.
* `rerun_3769.py` (output `rerun_3769_out.txt`): the one case of the census in which the six runs were not
  classified alike, with ten and a hundred times the integration time.
* `ex_named.py` (output `ex_named_out.txt`): the examples named in the paper.
* `families.py`: theta graphs, complete and complete bipartite graphs, cycles, grids, hypercubes, the Petersen
  graph, wheels and ladders, thirty initial conditions each; writes `data/fam.jsonl`.
* `check_theta.py` (output `check_theta_out.txt`): Proposition 10 against the flow limits on 39 theta graphs.
* `sim_process.py` (output `sim_process_out.txt`): the process itself, 10^7 ants on four graphs.
* `sim_check.py` (output `sim_check_out.txt`): the crossing indicators of simulated ants against p_e(W(n)).

## Data

* `data/ex5.jsonl`, `data/ex6.jsonl`, `data/ex7.jsonl`: the census for 3 to 5, for 6 and for 7 vertices, one case
  per line (edge list, N, F,
  the limit, its zero set, the largest real part of an eigenvalue on its support).
* `data/fam.jsonl`: the output of `families.py`.
