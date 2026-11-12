# The giant component of bilateral preference graphs with random budgets

Yitzchak Shmalo

Place independent continuous costs on the edges of K_n, give each vertex i an independent budget D_i with law P on
the positive integers, let i prefer its D_i cheapest incident edges, and keep an edge when both endpoints prefer it.
Moharrami, Subramanian, Liu and Sundaresan (Random Structures Algorithms 64 (2024), 537-624) showed that the local
limit of this graph is the Erlang weighted tree, so that the fraction of vertices in the largest component is
asymptotically at most the survival probability rho(P) of that tree, and asked whether the reverse inequality holds.

The paper proves that it does whenever P has a finite mean and P({1}) < 1:

    L_1(G_n) / n -> rho(P)   in probability and in L^1,

and the same holds for deterministic budget arrays whose empirical laws converge weakly to P.

## Contents

- `paper/main.pdf`, `paper/main.tex`: the paper.
- `code/checks.py`: exhaustive checks of the two sensitivity bounds used in the concentration arguments
  (Lemmas 2.2 and 8.1). Over every simple graph on five vertices and every one-edge change, the number of vertices in
  components of size at least k changes by at most 2(k-1); over every cost order and every budget vector on four
  vertices, moving one edge to any other rank changes the graph in at most four edges and that count by at most
  8(k-1). Output in `code/checks_out.txt` and `code/finite_checks.json`.
- `code/simulate.py`: direct simulation of the graph for n = 256, 512, 1024, 2048 (eight graphs each) under three
  budget laws (constant 2, constant 3, and 1 or 5 with probabilities 0.6 and 0.4), with the largest-component fraction
  and the mass in components of size at least 16, 64 and 256, against Monte Carlo estimates of the probability that the
  Erlang weighted tree reaches those sizes (seed 4521012). Output in `code/simulate_out.txt` and
  `code/simulation_results.json`.

Both programs need Python 3 with numpy.
