# PROB10-09 idea-before-code — replace vertical cardinality by vertical spectral norm

Parent target stays the iid **bond** percolation Cayley-graph conjecture `p_c<p_u` for every finitely generated nonamenable group. This note is written before any checker for this iteration.

## Continuity / ownership

R20 predecessor handoff remains `runs/R20/2026-09-19T23-50-00Z_owner_refocus_prob10_handoff_8f2c61.md`; its I0100, KNSV and BMO states/artifacts stay frozen. Source alias remains `D0061 = lyons_nonamenable_2000::conjecture_3.8_(benjamini-schramm_1996)`. The newest neighboring T09 report is `proofnet24/NM13-11/progress-percolation/runs/2026-09-20/2026-09-20T17-25-00+0300__t09-two-seed-arbitrary-four-pairs-gap.md`; that worker owns the Rattaggi/product-fibre/multiseed branching lane. This iteration stays in R20's quotient/extension/two-point-operator lane.

The June attempt history is consumed, not reset: `research/open_status.md`, `research/proof_strategy.md`, and the nonbacktracking/fibre/bridge notes including rounds 011, 018, 040, 042, 053, 054, 055.

## Exact new idea

Previous R20 extension theorem decomposed the adjacency of an extension as `A_X=A_H+A_V`, proved `||A_H||<=r_Q`, but bounded `||A_V||<=m` only by the number `m=|V|` of kernel generators. This throws away all nonamenability internal to the vertical subgroup.

Let `pi:Gamma->Q`, `N=ker pi`, and `V subset N` be finite symmetric. Since right multiplication by `V` preserves every quotient fibre `pi^{-1}(q)=x_q N`, identifying that fibre with `N` by `n -> x_q n` makes the vertical operator on every fibre *exactly* the right Cayley adjacency `A_{N,V}`. Hence

`||A_V|| = r_V := ||A_{N,V}||`,

not merely `<=m`.

Combining with the already-proved Hilbert-fibre horizontal estimate gives

`||A_X|| <= r_Q+r_V`.

Therefore the scalar nonbacktracking transfer should yield

`beta_{D0+m}(r_Q+r_V)<2k-1  =>  p_c<=1/(2k-1)<p_{2->2}<=p_u`

whenever the quotient marking contains a free marked rank-`k` subset.

This should strictly extend the last theorem whenever `V` generates a nonamenable vertical subgroup, since then typically `r_V<m` (and for the explicit free-product kernels below the norm is exact).

## Three genuinely different routes tested conceptually

1. **Vertical spectral-budget refinement (primary):** use exact fibrewise `||A_V||=r_V`; expected to succeed and enlarge the permitted vertical generator budget.
2. **Old vertical-cardinality bound (negation control):** keep `||A_V||<=m`. Freeze a graph with `m` deliberately beyond the previous surface budget `M_g`; this route must fail exactly there, otherwise the example is not new relative to the immediate predecessor.
3. **Quotient-Cheeger route without a free marked subset:** combine `p_c<=1/(1+phi_E(Q))` with the same spectral refinement. On the frozen surface quotient, use the spectral Cheeger lower bound only as a stress test; it is expected to be too weak. Do not relabel a failure as source progress.

A fourth route, multiseed product-fibre branching, is intentionally *not* pursued because the neighboring NM13-11 worker owns that lane.

## Frozen family chosen before code

Take the genus-five surface group `Q=Gamma_5` with its standard 20-direction marking. Let

`N=F_3 x F_3`

with the standard 12-direction product marking `V`. Then

`m=12`, `r_V=4 sqrt(5)`

because each `F_3` factor has adjacency norm `2 sqrt(5)` and product adjacency norms add. For `Q`, Zuk's bound gives `r_Q<=4 sqrt(5)`. Thus the full degree is `D=32` and

`r_Q+r_V <= 8 sqrt(5)`.

Choose a genuinely noncentral semidirect product `Gamma=N semidirect Gamma_5`: let `a_1` act on both `F_3` factors by the Nielsen automorphism `phi(x_1)=x_1 x_2, phi(x_2)=x_1, phi(x_3)=x_3` (and analogously in the second factor), while `b_1,a_2,b_2,...,a_5,b_5` act trivially. The surface relator maps to the identity because every image commutator `[alpha(a_i),alpha(b_i)]` is trivial. Use split horizontal lifts plus `V`.

The old cardinality theorem has genus-five cutoff `M_5=[4*25-25+2-17 sqrt(5)]/4 = (77-17 sqrt(5))/4 ~=9.7467`, so `m=12` lies outside its proved scope. The new spectral criterion predicts

`beta_32(8 sqrt(5)) = 7+4 sqrt(5) < 17`,

hence

`p_c <= 1/17 < 1/(7+4 sqrt(5)) <= p_u`.

The predicted exact gap is

`(68 sqrt(5)-150)/527 ~= 0.0038949`,

which should admit the clean rational certificate `>1/260` if the square check passes.

## Falsification obligations for code

The checker must verify exactly:

- `beta_32(8 sqrt(5)) = 7+4 sqrt(5)` and `<17`;
- the gap exceeds `1/260` by an integer square comparison;
- the previous `+m` theorem fails on the same frozen graph (`m=12 > M_5`, equivalently its beta test fails);
- the quotient-Cheeger stress test does not by itself cross the same uniqueness lower bound;
- the general surface/free-product-kernel algebraic criterion agrees with direct beta evaluation on a broad finite grid.

A successful checker remains a self-check only, not independent validation or source closure.