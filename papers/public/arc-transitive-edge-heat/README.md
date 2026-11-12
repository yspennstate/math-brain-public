# Heat across an edge of an arc-transitive graph

Yitzchak Shmalo

Paper: [paper/main.pdf](paper/main.pdf) (source `paper/main.tex`).

Aldous and Fill (*Reversible Markov Chains and Random Walks on Graphs*, Open Problem 7.30) ask whether random walk
on an arc-transitive graph has some monotonicity property stronger than their Corollary 7.3,
P_i(X_{2t} = j) <= P_i(X_{2t} = i). The paper proves that on every finite connected 1-walk-regular graph, in
particular on every finite connected arc-transitive graph and every distance-regular graph, the heat-kernel ratio
H_t(x,y)/H_t(x,x) is strictly increasing in t for every edge xy, where H_t = exp(-t(I - A/d)). Its derivative is
the variance of the Laplacian eigenvalue under the exponentially tilted spectral measure of x. The same holds for
the lazy walk in discrete time. On a regular graph that is not 1-walk-regular the ratio across an edge can exceed 1
and decrease, while its average over the neighbours of x is always increasing.

## Contents

- `paper/` - the paper.
- `code/edge_examples.py` - five arc-transitive examples: arc-transitivity, 1-walk-regularity (exact), the variance
  identity and monotonicity (floating point), strict monotonicity of the lazy ratio for k <= 60 (exact rationals).
- `code/regular_counterexample.py` - exact rational certificate that on the 4-regular graph of Regev and Shinkar
  (the cube with a square pyramid on two opposite faces) the ratio across a base-apex edge satisfies r(7) > 1 and
  r'(7) < 0.
- `code/vt_search.py` - floating-point search over small Cayley graphs for a decreasing edge ratio (none found).
- `code/allpairs_scan.py` - floating-point check of all pairs on thirteen arc-transitive graphs (no decrease found).
- `lean/TiltedVariance.lean` - Lean 4 / Mathlib proof of the finite inequality behind Var >= 0.

Each script writes the output kept beside it (`*_output.txt`). They need Python 3 with numpy and networkx.
