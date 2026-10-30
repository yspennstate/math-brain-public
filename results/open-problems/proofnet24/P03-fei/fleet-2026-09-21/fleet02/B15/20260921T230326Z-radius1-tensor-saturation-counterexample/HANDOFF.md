# Joint FEI Campaign-B handoff — B15

**Status:** `CANDIDATE_REFUTED`; full FEI remains OPEN.

The accessible post-credit candidate

`W(f) <= 3 J(f)/4  OR  T2(f) <= 4 J(f)`

is false for a genuine Boolean function.  Take the four-bit gate `r=1{|x|>=2}` and

`F_m = 1 - 2 prod_{b=1}^m r(x^(b))`.

For `m=12` (`n=48`), the rigorous exact-rational/log-interval checker certifies

- `W(F_12)/J(F_12) > 0.76118423918207877137 > 3/4`,
- `T2(F_12)/J(F_12) > 4.05924537070733980774 > 4`,
- `H(F_12)/J(F_12) = 4.3489407923190538523...`.

So this is not an FEI counterexample; it refutes both branches of the proposed dichotomy.

Two analytic product laws explain the failure:

1. For every non-character Boolean `f`, if `F_t=f^{tensor t}` and `p_*=max_s p_s<1`, then

`0 <= H(F_t)-T2(F_t) <= t^2 p_*^(t-1) H(f)`, hence

`T2(F_t)/J(F_t) -> H(f)/J(f)`.

Therefore

`sup_Boolean T2/J = sup_Boolean H/J`.

2. The real-restriction softmax current is additive:

`W(f tensor g)=W(f)+W(g)`,

so `W/J` is invariant under tensor powers.

**New exact obligation for Campaign B:** any repaired negative-information credit `Gamma_B` in a source-exact residual `T2-Gamma_B` must retain linear tensor-scale mass on hard bases.  If `Gamma_B(f^{tensor t})=o(t)`, then `(T2-Gamma_B)/J -> H(f)/J`, so the refund cannot improve the universal constant on that base.  Do not repair by separately paying a positive global KL: fleet01/B15's one-point family already forbids that.

See `REPORT.md`, `check_radius1_counterexample.py`, and `verification.txt` in this directory.  No priority claim is made.
