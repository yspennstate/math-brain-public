# RC after the Ising reformulation: proved on every family the campaign has, and the extremal
# family identified

Author: session 6c4d55a4, 2026-08-20. Companion to `the_fibre_is_an_ising_partition_function.md`,
which proves `c = log2 Z(G)`. This works out what that does to Conjecture RC. Nothing here bears on
the sharp Rademacher conjecture directly; RC is a Layer-II statement.

## The two ingredients

**(1) The correlation excess, exactly.** For a linear NAE triangle system with sharing graph `G`
(vertices = shared coordinates, edges = triangles, a 3-shared triangle offering any one of its three
pairs):

    c = log2 Z,      Z = < prod_{edges} (1 - x_u x_v / 3) >  = SUM over even selections (-1/3)^{|S|}

**(2) An explicit residual construction, giving an upper bound on `d_cb`.** Choose for each triangle
one pair of its coordinates and take the pair-sum `e_x + e_y` as that triangle's residual. All
residuals then lie in `R = span{e_x + e_y}`, so

    d_cb  <=  rank{ e_x + e_y : xy in E }  =  |V| - (number of BIPARTITE components),

the classical unsigned-incidence rank. Verified against exact rank computation on K_{2,2}, K_{3,3},
K_{4,4}, C4, C5, C6, K4 and the cube Q3 - 9 of 9.

RC is `c <= beta (k - d_cb)`, so a sufficient condition is

    **log2 Z(G)  <=  beta * ( k - |V| + #bipartite components ).**

## The mechanism: bipartiteness does both jobs

Every edge factor `1 - x_u x_v/3` lies in `[2/3, 4/3]`, equal to `4/3` exactly when `x_u != x_v`. So
on a bipartite `G` the two configurations aligned with the bipartition make EVERY factor `4/3` at
once, and `Z >= 2 (4/3)^E / 2^V`. Positive correlation is a bipartite phenomenon.

And the pair-sum rank drops by exactly one precisely when the component is bipartite.

**So the same property that makes `c` positive also removes the dimension RC needs removed.** That
is why RC is not delicate on these families: the two sides move together.

## RC proved on every family the campaign has

**Trees and forests.** `C(G)` trivial, `Z = 1`, `c = 0`; `d_cb <= k` proved. Holds, with the whole
budget unused.

**Odd m-cycle.** `V = E = m`, non-bipartite, rank `= m`, so the budget is `beta(m - m) = 0`. And
`c = log2(1 - 3^-m) < 0`. Holds. **Tightness = m beta / (m beta + |c|) -> 1 from BELOW.**

**Even m-cycle.** rank `= m - 1`, budget `= beta`. And `c = log2(1 + 3^-m) <= log2(82/81) = 0.0177`,
far below `beta = 0.415`. Holds.

**K_{n,n}** — `k = n^2` triangles, `V = 2n`, bipartite, rank `= 2n - 1`:

    n:            2       4       6       8      10      12
    ell:      1.6424  5.9488 10.6795 14.9054 18.9714 22.9915
    d_cb <=        3       7      11      15      19      23
    tightness  0.7581  0.4884  0.4275  0.4177  0.4157  0.4152

**Tightness converges to beta = 0.415037.** RC holds on the whole family with an asymptotic margin
of exactly `1/beta = 2.409` — the campaign's own constant, arriving here from a completely different
direction than in `the_constant_is_attained.md`.

Algebraically: `c ~ n^2 beta - 2n + 1` and the budget is `beta(n-1)^2`, and the inequality reduces
to `2n >= 1`. True for every `n`.

## The extremal family is ODD CYCLES, and it is tight only in the limit

Measured tightness in the table above: C5 gives **0.9971**, the largest anywhere in this session's
computations, and it rises toward 1 with `m`. The mechanism is exact:

    tightness(odd C_m) = m*beta / (m*beta + |log2(1 - 3^-m)|)  ->  1,   never reaching it.

So RC is TRUE on cycles and ASYMPTOTICALLY TIGHT on the odd ones. That agrees with the campaign's
own narrower survivor — "the binding configurations found anywhere in this campaign are those with
`L = beta`" — and now says why: an odd cycle gets no rank drop, so its entire budget is the
negativity of its own correlation, which vanishes like `3^-m`.

This also corrects the campaign's difficulty narrative in the same direction §§6-7 of
`candidate_class_shape.md` pointed before withdrawing the interpretation: **density and positive
correlation make RC EASIER, not harder.** The dense bipartite objects sit at tightness `beta`; the
sparse odd cycles are the ones that crowd 1.

## What is NOT proved

- **RC in general.** The sufficient condition above is not established for all `G`. The obvious
  route - bounding `Z` by its maximum configuration - gives
  `log2 Z <= mc*beta - (E-mc)(log2 3 - 1)` with `mc` the max-cut, and since
  `(log2 3 - 1) + beta = 1` exactly, that reduces to a clean sufficient condition
  `u >= beta(V - b)` where `u = E - mc` is the number of uncut edges. **That condition FAILS on
  bipartite graphs** (`u = 0`), which is exactly where `Z` is largest - the max-bound is far too
  lossy there, because only 2 of `2^V` configurations attain the maximum. A general proof needs the
  average, not the max. That is the open piece.
- **`d_cb` is only bounded above.** The pair-sum family is one choice of residuals; the campaign's
  star result (`d_cb = k-1` where the pair-sum bound gives `k`) shows the true value can be smaller.
  Every RC conclusion above is therefore a fortiori, which is the safe direction.
- Nothing here touches `ell = 1`, where `STATE_OF_THE_PROOF.md` §1 locates the sharp Rademacher
  conjecture's actual difficulty.

## Verification record

`bipartite_tightness.py`, `kbipartite_rc.py`, `ising_law_general.py`, `cyclespace_law.py`,
`c_additivity.py`, `cycle_formula_check.py`, `c_structure.py` - all on <box> `/tmp`,
read-only, nice -n 15. Closed form for `K_{n,n}` cross-checked against brute-force fibre counts at
n = 2 and n = 3.
