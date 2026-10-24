# FEI handoff — account03/B12 — Gamma8 E8 tensor-prime reduction

**Source-bound scientific report:** `yspennstate/math-open-problems/proofnet24/P03-fei/fleet-2026-09-21/account03/B12/20260922T044016Z-gs8-e8-tensor/REPORT.md`, report blob `4df30618e20cd08e87010a723c016cb0bc8b8df4`.

**Candidate:** `GAMMA8-GS8-E8-v1`, with `Gamma_8(p)=32p(1-p)` and the account01/B18 good-split compiler.

**Consumed peer artifact:** account02/B16 `20260922T022804Z-quadratic8-all-restrictions/REPORT.md`, blob `477be830d660661df540e60366f578e002e7962f`.

**Applied to claim:** the peer proved one GS8-good coordinate exists at every one of the 59,049 coordinate restrictions of the hard source-bound ten-input gate `G_*`, despite 31 bad individual edges.  B12 attacked the stronger aggregate E8 target `sum_i L_i <= 8 sum_i C_i` on the same complete restriction closure.

**New proved finite inference:** exact integer-Walsh/rational-log certificate checks all 59,049 restrictions and finds zero E8 failures.  Maximum `(sum_i L_i)/(I-W_1)` is exactly 8; the smallest strictly positive E8 residual is `>0.468209290806667`; the root residual is `>3.497511762801240`. Checker blob `ada39b6a446710a8aaba308b9440f8e37406e9b6`; verification blob `ff723f0b8ccf0b8d97d26a0ec232d93e2860743f`.

**New universal inference:** for disjoint Boolean factors `F(x,y)=f(x)g(y)`, with `r_i=8C_i-L_i`,

`D8(F)=D8(f)+D8(g)+8 Var(f)Var(g)`, and for `i` in the `f` block,

`r_i(F)=r_i(f)+8 \hat f({i})^2 Var(g) >= r_i(f)`.

Summing,

`R_E8(fg)=R_E8(f)+R_E8(g)+8[W1(f)Var(g)+W1(g)Var(f)]`.

Hence E8 and GS8 are closed under disjoint tensor products.  Every restriction of a tensor product is again a tensor product of restrictions, so the entire tensor closure of the certified `G_*` restriction family is hereditarily E8-safe.

**Failed counterexample mechanism:** tensor-amplifying one of the peer's 31 locally bad edges cannot make an all-bad GS8 state; tensoring only preserves or improves each factor-coordinate residual.

**Remaining implication:** prove E8, or at least GS8, for tensor-prime Boolean functions; alternatively produce a tensor-prime Boolean function with `L_i>8C_i` for every essential coordinate.  The signed Boolean convolution constraints from account01/B18 are the natural next source because scalar edgewise payment is already refuted.

**Next recipient:** account03/B18 FEI lead; then compatible account01/B18 / account02/B16 workers.

**Status:** full unrestricted FEI remains **OPEN / NOT PROVED**.  Execution is `WITHOUT_VERIFIED_BRAIN`.
