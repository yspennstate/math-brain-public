# PROB10-07 idea — fixed-width-eight complete-tripartite transfer

Runtime request: GPT-6 / maximum reasoning. Authenticated runtime model/effort telemetry is unavailable; do not infer the requested setting from this file.

Parent target: Grimmett–Winkler pairwise negative edge correlation for the uniform measure on **all forests** of an arbitrary finite graph. Universal status remains OPEN/PARTIAL. Complete arbitrary-graph order remains 9. This artifact proposes only a complementary structural-family theorem and does not touch P14/HARD10-01 graph-order ownership.

## Continuity and nonoverlap

The immediate PROB10-07 predecessor proves strict p-NC for all complete tripartite `K_{a,b,n}` with the two smallest part sizes summing to at most 7. The natural first new source-valid frontier is therefore fixed terminal width 8:

`K_{1,7,n}, K_{2,6,n}, K_{3,5,n}, K_{4,4,n}`, all `n>=1`.

This is distinct from the current NM13-04/NM13-08 three-terminal layer line, which studies a dominating three-terminal set joined to repeated internal right components such as `P5`. Here the repeated third part is independent and the fixed two-part core has eight terminals; the state space is the Bell lattice on 8 terminals.

## Three materially different attacks considered

1. **Deletion–contraction closed form.** Use `Z_e(G)=Z(G/e)` and `Z_{ef}(G)=Z(G/e/f)` and seek a closed formula for all-forest counts of the contracted complete-tripartite multigraphs. Obstruction: contractions create identified vertices and parallel edge classes, and the readily available matrix-forest determinant is for rooted forests, not the unrooted all-forest partition function required here. No source-safe closed formula was recovered, so this route is not promoted.

2. **Symmetry quotient of the Bell state space.** Quotient the 4140 terminal partitions by `S_a x S_b` to obtain a much smaller transfer. This is attractive for eventually treating arbitrary fixed width, but edge marking breaks part of the symmetry. A proof needs strong lumpability simultaneously for the unmarked transfer and every forced-spoke marked operator used in `Z,Z_e,Z_f,Z_{ef}`. That obligation is not assumed here.

3. **Full Bell transfer with a cached legality table and forced-spoke operators.** This is the chosen route. For `m=8`, the unmarked repeated-vertex transfer is `M=9I+N`; every non-diagonal transition merges at least two terminal blocks, so `N^8=0`. A marked pair touches at most two repeated vertices. Forced-spoke operators initialize those distinguished vertices exactly, then all remaining repeated vertices contribute `M^x`. Therefore every marked count is `9^x` times a rational polynomial of degree at most 7, and every Rayleigh difference is `9^(2x)` times a rational polynomial of degree at most 14. The finite task is to reduce edge pairs by `S_a x S_b x S_2` and prove each resulting polynomial nonnegative on its physical integer domain.

## Falsification plan before claiming a theorem

Construct the width-eight transfer exactly, enumerate every edge-pair orbit for the four families, and inspect every Rayleigh polynomial coefficient in exact rational arithmetic. If ordinary monomial positivity fails, do not hide it: try a Newton/binomial basis or produce the first physical negative value. As an implementation-independent sanity check, directly enumerate all forests of the smallest `K_{1,7,1}` instance and test every actual edge pair.

A successful run moves only the structural complete-tripartite metric from `sum(two smallest parts)<=7` to `<=8`; it does not move the all-graphs order metric and does not resolve the universal conjecture.