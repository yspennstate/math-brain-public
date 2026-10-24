# Session 2026-08-20 (6c4d55a4): the correlation excess has a closed form

Owner's ask: continue the proof in a helpful direction, 20 hours, keep building the brain.

**The sharp Rademacher singularity conjecture is still OPEN.** Everything below is Layer II. The
conjecture's difficulty is at Layer III, `ell = 1`, and nothing here touches it.

## What is new

**1. THEOREM — the fibre is an Ising partition function.** For any linear NAE triangle system, with
the sharing graph `G` (vertices = shared coordinates; each triangle contributes at most one edge -
its shared pair, or any one of its three pairs if all three coordinates are shared):

    |A| / (2^r (3/4)^k)  =  Z  =  SUM over even edge-selections S of (-1/3)^{|S|}
                              =  < prod_{edges} (1 - x_u x_v / 3) >
    c := k*beta - ell  =  log2 Z.

Proof by integrating out private coordinates: a 3-private triangle gives a constant; a 2-private
triangle gives a constant INDEPENDENT of its shared coordinate (this is exactly why trees have
c = 0); a 1-private triangle gives `2 - [x_u = x_v] = (3/2)(1 - x_u x_v/3)`; a 0-private triangle
gives `(3/4)(1 - (uv+vw+uw)/3)`. Expand, and the uniform average kills every non-even selection.
Van der Waerden / high-temperature expansion at coupling `-1/3`.

Written up in `problem/the_fibre_is_an_ising_partition_function.md`.

**Machine-checked**: 1,200 random linear systems across three seeds, exact rational comparison,
**1,200 matches / 0 mismatches**, with coverage of all four triangle types (0/1/2/3 shared
coordinates; 2,781 of the three-shared kind). Plus 12/12 on structured attack shapes (K4, theta
graphs, chorded cycles) and 13/13 on additivity shapes.

**2. RC becomes a graph statement.** With the campaign's proved `d_cb <= k`,

    RC  <=>  Z(G)  <=  (4/3)^{k - d_cb},

and an explicit residual construction (each triangle's pair-sum `e_x + e_y`) gives

    d_cb  <=  rank{e_x+e_y} = |V| - (number of BIPARTITE components)

- the classical unsigned-incidence rank, checked exactly on 9 graphs. So RC follows from

    Z(G) <= (4/3)^{E - V + b}.

**3. The mechanism: bipartiteness does both jobs.** Each factor is `4/3` exactly when the endpoints
differ, so a bipartite `G` has two configurations making every factor `4/3` at once - positive
correlation IS bipartiteness. And the pair-sum rank drops by one exactly when the component is
bipartite. The property that makes `c` positive is the property that pays for it.

**4. RC proved on every family the campaign has**, in `problem/rc_on_the_ising_reformulation.md`:
trees/forests (c = 0), odd cycles, even cycles, and K_{n,n} where `k = n^2` and tightness converges
to **beta = 0.415037** - asymptotic margin exactly `1/beta = 2.409`, the campaign's own constant,
reached from a new direction.

**5. The extremal family is ODD CYCLES**, tight only in the limit:
`tightness(C_m odd) = m*beta/(m*beta + |log2(1 - 3^-m)|) -> 1`, never reaching it. C5 measures
0.9971, the largest anywhere in this work. This reverses the campaign's difficulty narrative in the
direction `candidate_class_shape.md` §§6-7 pointed before withdrawing: **density and positive
correlation make RC EASIER; sparse odd objects are what crowd 1.**

**6. A deletion-contraction recursion**, verified on **27,474 connected graphs, 0 mismatches**:

    F(G) = 2 F(G-e) - F(G/e),      F(G) := SUM_x 2^{cut(x)},   Z = (2/3)^E F / 2^V.

## Where the general proof stops, precisely

The recursion carries a MINUS sign, so bounding `F(G)` above needs an upper bound on `F(G-e)` **and
a lower bound on `F(G/e)`**. A one-sided induction cannot close. (I initially tested
`2B(G-e) - B(G/e) <= B(G)`, which is a consistency property of `B`, not the induction step - that
was my error and it is corrected here.)

Measured: both natural lower bounds are too weak, and they fail at the same first case.

    L = 2^V 2^{E/2}  (Jensen, since <cut> = E/2)        valid on 27,474 graphs, 0 violations
    L = 2^{maxcut} x (#optimal cuts)                    valid on 27,474 graphs, 0 violations
    induction step 2B(G-e) - L(G/e) <= B(G):            FAILS 2,552 of 21,495 for BOTH

First failure is the triangle: `B(C3) = 27`, `B(P3) = 18` (tight, since `F(P3) = 18`), and the
contraction is a doubled edge whose true `F = 10` while both candidate bounds give `8`. With the
exact value the step gives `2(18) - 10 = 26 = F(C3) <= 27` and closes. **So the induction closes if
and only if the lower bound on `F(G/e)` is sharp enough on small dense multigraphs.** That is the
concrete remaining piece, and it is a question about `F` on multigraphs, not about d_cb.

## A defect of mine, caught and fixed

The integer rewrite of the inequality scan had the sign of the edge weight inverted
(`2 if different else 4`, where `3 - x_u x_v` is `4` when different). It reported the triangle as a
violation at `Z = 28/27`. The true value is `26/27`, confirmed independently
(`sum_x prod(3 - x_u x_v) = 2(8) + 6(32) = 208`, and `208/216 = 26/27`). A violation at the smallest
possible case was the tell. Fixed, positive control run (C3 = 26/27, C4 = 82/81), rescanned.

## Files

    problem/the_fibre_is_an_ising_partition_function.md    the theorem and its proof
    problem/rc_on_the_ising_reformulation.md               RC consequences, families, extremal case
    <box> /tmp: c_structure.py, positive_c_hunt.py, cycle_formula_check.py,
      c_additivity.py, cyclespace_law.py, ising_law_general.py, ising_mass_verify.py,
      kbipartite_rc.py, bipartite_tightness.py, rc_graph_inequality.py, deletion_contraction.py,
      two_sided.py   - all read-only, nice -n 15

## Next

1. Sharpen the lower bound on `F` for small dense multigraphs; that closes the induction and with it
   RC on all linear systems (given the pair-sum bound on d_cb).
2. `d_cb` is only bounded ABOVE here, so every RC conclusion is a fortiori - the safe direction. The
   campaign's exact `d_cb` solver is brute-force over `C(|cand|, d)` subspaces and cannot reach the
   sizes needed; a better algorithm is its own piece of work.
3. None of this touches `ell = 1`.
