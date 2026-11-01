# The connectivity window of bilateral preference random graphs

Yitzchak Shmalo

In the bilateral preference random graph LK(n,k) of La and Kabkab, independent uniform scores are placed on the
edges of the complete graph K_n, each vertex prefers its k incident edges of smallest score, and an edge is kept
when both of its endpoints prefer it. Dabirian and Subramanian (J. Appl. Probab. 63 (2026), 552-579) showed that
the graph is connected with high probability above log n + (1/2) log log n sqrt(log n) and disconnected below
log n - (1/2) log log n sqrt(log n), and left the window between the two open.

The paper shows that for every fixed C, uniformly over integers k with |k - log n| <= C, the number of isolated
vertices is asymptotically Poisson with mean n e^{-k} in total variation, and

    P(LK(n,k) is connected) = exp(-n e^{-k}) + o(1).

So LK(n,k) is connected with high probability if and only if k - log n tends to infinity.

## Contents

- `paper/main.pdf`, `paper/main.tex`: the paper.
- `code/checks.py`: the numerical constants of the proofs in exact rational arithmetic, the integral formula of
  Lemma 2.1 against Monte Carlo, and M e^k of Lemma 2.2 for n up to 10^7. Output in `code/checks_out.txt`.
- `code/simulate.py`: the limiting one-vertex integral I_k and a direct simulation of LK(n,k) for n = 1000 and
  n = 3000 (seed 20261029). Output in `code/simulate_out.txt`; the table in Section 6 of the paper is taken from it.

Both programs need Python 3 with numpy and scipy; `simulate.py` also uses scipy.sparse.
