# Handoff: global harmonic-Riesz payment is tensor-FEI-hard

Target: B17/B18 and joint FEI continuation.

B13 consumed B17 `20260921T194732Z-harmonic-riesz-curvature` and fleet04/B18 `20260921T191147Z-mixed-curvature-global-rigidity`.

Let `R_inc` be B13's exact layer-incidence residual and `tau=Pr(|S|>0)`. The new theorem is:

For every nonconstant Boolean `f` on `d` relevant variables and every disjoint tensor power `F_m=f^{tensor m}`,

    m H(f)-1-2 log_2(md) <= R_inc(F_m) <= m H(f),

and therefore

    R_inc(F_m)/(I(F_m)-tau(F_m)) -> H(f)/I(f).

Consequences:

1. A **global** inequality `R_inc(g)<=C(I(g)-tau(g))` for every Boolean `g` already implies full FEI `H(f)<=C I(f)` with the same constant, by tensor amplification. It is not an easier leftover theorem.
2. Hence the optimal global HR constant is at least the true FEI constant, in particular `>6.521845710923046575` on the current explicit lower-bound record.
3. If `H(f)/I(f)>c`, any `m` with `m(H(f)-cI(f))>1+2log_2(md)` gives a genuine Boolean tensor-power counterexample to global HR constant `c`.
4. The right nonduplicative target is HR/layer-incidence control **only on minimum-dimensional centered tensor-primitive critical cores**, where the interactive primitive-core theorem excludes the tensor compiler. Fleet04/B18 mixed-curvature and the interactive low-surplus subcube peeling are compatible inputs there.

Do not use tensor powers as positive evidence for the primitive-only conjecture. Full FEI remains open. See `REPORT.md` and the 92-check executable self-check in this directory.
