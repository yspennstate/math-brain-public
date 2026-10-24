# H0024 correction note for the 23:56Z directional-closure artifact

This immutable note corrects two wording issues in `2026-09-17T235600Z__H0024_directional_closure_structure.md` without modifying that prior artifact.

1. In the introductory description of the previous symmetric-radius bound, the intended source inequality is

`P(D^* >= n) <= 2 P(D^-> >= n)`,

not the typographical `P(D^*>=n)<=2P(D^->=n)`.

2. Proposition 3.1's logarithmic closure formula requires the harmless **boundary nondegeneracy** that the fixed-boundary factors do not vanish, for example

`P(L_0=0)>0` and `P(R_0=0)>0`.

Thus the corrected theorem statement is:

> Let `(L_x,R_x)` be iid site marks, symmetric in the sense that `L_0` and `R_0` have the same marginal tail `q_n`, assume `q_n=O(1/n)`, and assume `P(L_0=0)>0`, `P(R_0=0)>0`. Then for `I_n=[0,n]`,
> 
> `log P(I_n is closed) = -2 sum_{k=1}^n q_k + O(1)`.

The proof in the earlier artifact already isolates finitely many boundary factors and explicitly uses their positive limits, so no interior argument changes.

The H0024 frog model satisfies this nondegeneracy. The source has geometric lifetimes supported on `{0,1,...}` with `P(Lifetime=0 | pi)=1-pi>0` because `pi in (0,1)`. Since `E[eta_0]<infinity`, `eta_0<infinity` almost surely. Conditional on any finite number of frogs at a site, there is positive probability that all have lifetime zero; averaging yields positive probability that both site extrema equal zero. Therefore the corrected proposition applies to the admitted source exactly as used.

All other claims in the directional-closure artifact are unchanged by this correction. In particular the H0024 conclusions remain:

- exact directed interval-closure representation;
- stable symmetric-envelope ratio `R_alpha=E[M_alpha]/E[S_alpha]` with `2/alpha <= R_alpha <= 2` and `R_alpha -> 2` as `alpha downarrow1`;
- actual-source closure exponent `P([0,n] closed)=n^{-2c+o(1)}` when the site marginal satisfies `nq_n->c`;
- scale-summed first-moment transition at `c=1`;
- frozen full-source metric `G_crit=2` unchanged.
