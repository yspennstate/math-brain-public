VERDICT: PROVED exponential obstruction to shape-by-shape tree-to-site-animal reweighting using only size and contacts

The dimensional-reduction conjecture in T055 remains unresolved here. The
result below is a limited obstruction to one possible comparison of lattice
models, together with exact finite data. No claim of historical novelty is made.

For a site animal S, let tau(S) count spanning trees of its induced
nearest-neighbor graph, and let k = e − n + 1 be its non-bonded contact count.
Forgetting the bonds of bond trees weights S by tau(S). The following pairs
have the same size and contact count but different multiplicities:

| lattice | first possible size | contacts k | multiplicities |
|---|---|---|---|
| Z² | 7 | 2 | 15 and 16 |
| Z³ | 6 | 1 | 4 and 6 |

`PROOF.md` gives explicit coordinates and proves minimality without relying on
the computation. The cubic minimum also holds in every higher dimension.
Joining r copies by bridges gives planar pairs with n = 8r − 1, k = 2r and
ratio (16/15)^r; cubic pairs have n = 7r − 1, k = r and ratio (3/2)^r.
Consequently no positive weight depending only on (n,k), even with arbitrary
size-dependent normalization, can make the resulting site-animal weights
uniform shape by shape, or uniformly accurate within exp(o(n)).

This does not exclude a relation after summing over shapes. It does not show
that these families are typical and does not disprove universality. Site
animals, bond trees, and induced site trees are distinguished throughout;
size means vertices and rotations/reflections remain distinct.

Exact enumeration covers Z² through eight vertices and Z³ through seven.
There are 2725 site animals and 6986 bond trees at n = 8 in Z², and 23502 site
animals and 42464 bond trees at n = 7 in Z³. Complete shape certificates and
joint (k,tau) histograms are in `data/`; `data/summary.json` gives the totals.

Reproduction commands, from this folder:

```sh
OMP_NUM_THREADS=1 nice -n 15 python3 -B enumerate_animals.py --d2 8 --d3 7 --output data | tee enumeration_output.txt
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit_obstruction.py | tee obstruction_output.txt
```

Both runs end with `ALL_ASSERTIONS_PASSED`. The two animal generators agree
shape by shape on all 31414 animals across the computed sizes. Each
spanning-tree count is checked by an exact determinant and exhaustive edge
subsets. A separate implementation audits the explicit chains by rational
determinants and bridge deletion, and checks the small-graph classification by
exhausting bipartite graphs through six vertices. The runs take seconds and
use less than 100 MB RSS, serially, without numerical libraries. The runner
inherits niceness 20; macOS rejects changing it to 15, and all runs retain that
lower priority. Full output, commands, checks, and limitations are in `LOG.md`.

The literature search took less than ten minutes. No low-dimensional lattice
solution was found. Relevant papers actually opened were:

- David C. Brydges and John Z. Imbrie, *Branched Polymers and Dimensional
  Reduction*, [arXiv:math-ph/0107005](https://arxiv.org/abs/math-ph/0107005),
  Ann. Math. 158 (2003), 1019–1039. The exact relation concerns continuum
  branched polymers and a continuum gas.
- Yucheng Liu and Gordon Slade, *Near-critical and finite-size scaling for
  high-dimensional lattice trees and animals*,
  [arXiv:2412.05491](https://arxiv.org/abs/2412.05491), J. Stat. Phys. 192, 32
  (2025). The correlation-length and finite-size results are for spread-out
  models above dimension eight.
- Robert Fitzner and Remco van der Hofstad, *NoBLE for lattice trees and lattice
  animals*, [arXiv:1905.02785](https://arxiv.org/abs/1905.02785). This gives
  nearest-neighbor mean-field results in high dimensions, not the requested
  d = 2, 3 theorem.
- Gill Barequet, Neal Madras, Johann Peters, *On t-fold Totally-Concave
  Polyominoes*, [CCCG 2025, pp. 92–98](https://cccg-wads-2025.eecs.yorku.ca/cccg-papers/34.pdf).
  Its introduction discusses the lack of rigorous asymptotic geometry in low
  dimensions; its main concavity result does not settle T055.

What failed: a contact-only shape-by-shape bridge between the two counting
measures is ruled out. No exponent bound, exponent value, or lattice-to-continuum
universality theorem was obtained. The search cannot certify the absence of
other literature, and the finite data cannot establish an asymptotic exponent.

The next worker should seek a comparison that controls ensemble averages,
rather than every shape. The exact identity is
`t_d(n)/a_d(n) = E_uniform_site_animal[tau(S)]`.
Conditional on existence of the growth constants and logarithmic exponents,
equality of the two entropic exponents requires
`log E[tau(S)] − n log(lambda_tree/lambda_animal) = o(log n)`.
The obstruction above says nothing about whether such an averaged estimate
holds. A concrete next step is to organize this moment by the graph's
articulation blocks, using the exact multiplicativity of tau, and identify
what probabilistic control of the block distribution would suffice. A
separate argument is still needed to connect either lattice ensemble to the
continuum dimensional-reduction theorem.

Task: “Dimensional reduction for lattice trees and lattice animals” —
2026-11-14, session start 20:47:15 +04:00.
