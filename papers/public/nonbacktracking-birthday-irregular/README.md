# A birthday bound for non-backtracking walks on graphs of bounded degree ratio

Yitzchak Shmalo

Let G be a finite simple graph on n vertices with minimum degree m >= 3 and maximum degree M, and put
Q = M/(m-1). The paper proves that a non-backtracking random walk of length k on G, started along any
directed edge, is vertex-simple with probability at most 256 Q (1+Q) n / k^2.

So the Alon-Peres conjecture stated by Dozier (The birthday paradox for non-backtracking walks on
regular graphs, arXiv:2608.26321, Conjecture 1.5) holds on every class of graphs with bounded ratio of
maximum to minimum degree, with a constant depending only on the probability and the bound for the
ratio. For regular graphs of degree at least three the constant can be taken to be 31/sqrt(epsilon),
for every degree. The expected self-intersection time is at most 32 sqrt(Q(1+Q)n) + 2; for minimum
degree at least three and bounded maximum degree this removes the logarithmic factor from Theorem 1 of
Bencs, Goldberg, Jenssen, Jerrum, Pete, Regts and Yin (arXiv:2608.09729).

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/check_bound.py`: exact computation of the survival probabilities p_k on small random graphs
  (all starting edges) and Monte Carlo estimates of the self-intersection time on graphs with up to
  20,000 vertices, compared with the theorem. Pure Python 3, no dependencies. Run
  `python code/check_bound.py` from the repository root (about 20 seconds).
- `data/bound_checks.json`: the output of that script (seed 20261113).
- `SHA256SUMS`: checksums of the files above.

The checks are not part of the proof.

## License

MIT, see `LICENSE`.
