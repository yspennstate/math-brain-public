# account03/B12 handoff — dependent pivot + aggregate rank-two cross smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`. Full conjecture remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Canonical scientific source:

- repository: `yspennstate/math-open-problems`
- commit: `b3c543b40dfaef13468466fa82625303a7719af8`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`

## New proved mathematics

1. **Dependent square from an L^p remainder.** If `R` has density `g in L^p`, `p>2`, and the conditional density of `V|R=r` is <=1, with no independence assumed, then for `s=p/(p-1) in (1,2)`,

`||p_{R+aV^2}||_infinity <= |a|^(-1/2) D_s ||g||_p^(s/2)`

with explicit `D_s=(2/s)(1-s/2)^(-1/2)[s/(2-s)]^(1-s/2)`.

2. **Pivot + aggregate rank-two cross theorem.** After an original-coordinate scalar Schur pivot `a=A_kk`, let `C` be a residual physical cross block with range leverage <=1/2 and `E_2=e_2(CC^T)>0`. Then

`||p_Q||_infinity <= K_s |a|^(-1/2) E_2^(-1/8)`.

For `s=8/5`, `K_s=8.152027307129858...`, so `8.153` is valid. Extra residual singular directions help monotonically through `E_2`; no independent-convolution assumption is made.

3. For an overlap-one mixed `3x3` minor `M` with two-by-two residual cross block `C`, `det M=a det C`. Hence the local payment is

`||p_Q||_infinity <= 8.153 (|a| |det M|)^(-1/4)`.

This is an explicit analytic payment for the overlap-one channel in `e_3(A^2)`.

4. Exact channel bookkeeping: `M_0+M_1+M_2+M_3=e_3(A^2)>=1`; random coloring realizes expected resources `M_0/64`, `(16/3125)M_1`, `M_2/64`, and `M_3`. Thus a dominant `M_0`/`M_2` channel yields a coloring with resource >=`1/256`; dominant `M_1` yields >=`4/3125`.

5. **One arbitrary added eigen-direction stability.** If a physical `3x3` block has two same-sign eigenvalues of magnitude >=L and arbitrary third eigenvalue, then `||p_Q||_infinity <= C_*/L`, with

`C_*=2*pi+3*sqrt(3)+sqrt((2*pi+3*sqrt(3))^2+3*pi^2)=24.183038289961516...`.

Therefore a physical definite triple with gap L remains uniformly smoothing after adding an arbitrary global rank-one quadratic perturbation `tau(v^T x)^2`, for any sign/magnitude tau, plus arbitrary outside completion/cross coupling.

## Partner use and correction discipline

The assigned `account04/B12` path still had no current QFORM artifact at the fresh source-bound read, so no result was fabricated. The compatible completed account04/B18 dependent-square lemma (`math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`) was actually applied and strengthened to the L^p interface above.

Fresh correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` is respected: nothing here claims the three-large-eigenvalue hypothesis forces one scalar pivot with a rank-two disjoint cross block. The theorem is a payment once that mixed packet is present; aggregation is still needed.

## Remaining implication

Aggregate the overlap-one and overlap-two channel payments **before** inverse pivot/minor powers so diffuse determinant mass cannot incur dimension loss. Then splice the four exact overlap channels into a complete structural/analytic argument. Continuity is not proved by the new mixed theorem; only `L^infinity` is proved there.
