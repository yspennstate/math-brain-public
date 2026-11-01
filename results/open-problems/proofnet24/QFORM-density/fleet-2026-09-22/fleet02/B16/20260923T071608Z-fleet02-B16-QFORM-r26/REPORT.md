SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B16, 2026-09-23T07:16:08Z.
attacking: near-coloop transition — test whether conditioning on the weak leakage projection preserves the planar source cap; retain cube-corner slice mass through the curved null-hub pushforward.

# fleet02/B16 r26 — near-coloop conditional-projection blowup and grouped source repair

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** Projection-product interaction  
**Status:** `NEW SOURCE-VALID MECHANISM OBSTRUCTION + TARGET-VALID FAMILY BOUND / FULL QFORM OPEN`  
**Continuity:** not asserted here; all conclusions below are essential-density statements unless explicitly noted.

## 1. Fresh control and source boundary


Required pinned completed source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, especially

- `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`, Theorem A (localized three-variable density bound) and Theorem C (ruled one-sheet bound using two-dimensional product marginals), and
- the matching `RESULTS.md` / `FOURIER_ROUTE_REPORT.md`, which explicitly forbid replacing original-product structure by an arbitrary projected joint density or by post-rotation independence.

Latest designated partner consumed: fleet03/B16 r26, canonical source `math-open-problems@a398a1c2e6e97683e3fe594fa19476929a882be6`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B16/20260923T045948Z-fleet03-B16-QFORM-r26/REPORT.md`. Its Corollary `QFORM-R23-ONE-COLOOP-REDUCTION-v1` reduces the exact-rank-three residual, after its paid exits, to a genuine near-coloop `c>63/64`; its stated next debt is a uniform near-coloop transition that retains original-product dependence.

## 2. First unpaid implication, attacked immediately

A tempting transition from the exact null-coloop endpoint is:

1. write the dominant spectral coordinate as `sqrt(c) X_0 + sqrt(a) T`, `a=1-c << 1`;
2. condition on the weak leakage projection `T`;
3. invoke the exact-null-coloop theorem on the remaining hub and transverse projected variables, assuming the transverse density cap survives conditioning.

The new result below shows step 3 is false in the strongest possible sense, even in an exact-rank-three target family satisfying `c>63/64` and arbitrarily small physical diagonal/pair pivots. The unconditional two-dimensional product projection has a universal cap, while the corresponding normalized conditional cap is infinite.

## 3. A strict near-coloop target family

Fix even `m>=66` and `0<a<1/64`; put `c=1-a>63/64`. Choose balanced signs `eps_j in {+1,-1}`, `1<=j<=m`, with `m/2` of each sign. Define an `n=(2m+1)` by `3` frame `R` by rows

`r_0=(sqrt(c),0,0)`,

`r_j=(sqrt(a)/sqrt(m), eps_j/sqrt(m),0)`, `1<=j<=m`,

`r_{m+j}=(0,0,1/sqrt(m))`, `1<=j<=m`.

Because the signs balance,

`R^T R=I_3`.

Take

`Lambda = [[0,1,0],[1,0,0],[0,0,1]]`.

Its eigenvalues are exactly `{1,-1,1}`. Hence

`A=R Lambda R^T`

has exact rank three and nonzero spectrum `{1,-1,1}` for every `a,m`; it is always inside the full QFORM target class.

For independent original coordinates write

`T=m^(-1/2) sum_{j=1}^m X_j`,

`U=m^(-1/2) sum_{j=1}^m eps_j X_j`,

`V=m^(-1/2) sum_{j=m+1}^{2m} X_j`.

Then exactly

`Q=X^T A X = 2 (sqrt(c) X_0 + sqrt(a) T) U + V^2`.          (3.1)

No independence between `T` and `U` is asserted. They are an orthogonal two-dimensional projection of the same first leaf product bank. The variable `V` uses a disjoint source bank.

Relative to the dominant row direction `e=(1,0,0)`, every residual transverse leverage is `1/m<1/64`, and the dominant leverage is `c>63/64`, exactly the near-coloop geometry singled out by fleet03/B16 r26.

The family is also arbitrarily deep in the no-pivot regime. Its physical diagonals are

`A_00=0`, `A_jj=2 eps_j sqrt(a)/m` on the first leaf block, and `A_kk=1/m` on the second leaf block.

Its two-coordinate principal determinants are:

- hub/first-leaf: `-c/m`;
- first/first: `0` for equal signs and `-4a/m^2` for opposite signs;
- first/second: `2 eps_j sqrt(a)/m^2`;
- hub/second and second/second: `0`.

Thus every physical diagonal and every physical pair determinant has modulus at most `1/m`. Given any fixed threshold `tau>0`, taking `m>1/tau` puts the whole family below that diagonal/pair threshold while the spectral target remains `{1,-1,1}`.

## 4. New theorem: bounded planar projection, unbounded normalized conditional projection

### Theorem 4.1 — `QFORM-NEAR-COLOOP-CONDITIONAL-PROJECTION-BLOWUP-v1`

For the first `m` leaves take iid `Unif[0,1]`. Then `(T,U)` is an orthogonal two-dimensional projection of a cap-one product law, so the completed two-dimensional product-marginal theorem gives

`||p_(T,U)||_infinity <= 2`.                                     (4.1)

Nevertheless

`ess sup_t ||p_(U | T=t)||_infinity = infinity`.                 (4.2)

More precisely, put `k=m/2` and parameterize the upper cube corner by

`tau = m - sum_{j=1}^m X_j`, `0<tau<1`,

so

`T=sqrt(m)-tau/sqrt(m)`.                                        (4.3)

Then

`p_(U | T)(0 | T=sqrt(m)-tau/sqrt(m))
 = C_m / tau`,                                                   (4.4)

where

`C_m = sqrt(m) 2^(-m+1) / B(k,k)
    = sqrt(m) 2^(-m+1) Gamma(m)/Gamma(m/2)^2 >0`.                (4.5)

#### Proof

Put `Z_j=1-X_j`. On `0<tau=sum Z_j<1`, the cube constraints other than nonnegativity are inactive. Conditional on `sum Z_j=tau`, the normalized vector `Z/tau` is uniform on the standard `(m-1)`-simplex, i.e. Dirichlet `(1,...,1)`.

Let `A_+=sum_{eps_j=+1} Z_j`. Then

`B:=A_+/tau ~ Beta(k,k)`.                                       (4.6)

The balanced contrast is

`U=(tau/sqrt(m))(1-2B)`.                                        (4.7)

The beta density at `1/2` equals `2^(-m+2)/B(k,k)`. The density of `W=1-2B` at zero is therefore `2^(-m+1)/B(k,k)`. Scaling by `tau/sqrt(m)` gives (4.4)-(4.5), proving (4.2). QED.

This is exactly the product-provenance failure relevant to the near-coloop transition. Conditioning on `T=t` preserves independence of the original hub `X_0`, but it does **not** preserve a uniform density cap for the same-bank transverse projection `U`.

If the second bank is also iid uniform, then `V` is independent of `(T,U)`, so

`||p_((U,V) | T=t)||_infinity
 = ||p_(U | T=t)||_infinity ||p_V||_infinity`,                  (4.8)

and the conditional planar cap also diverges. No post-projection independence is being inferred: the only independence in (4.8) comes from disjoint original-coordinate banks.

## 5. The lost weight is explicit and cancels the normalized singularity

The same corner gives the exact density of `tau`:

`p_tau(tau)=tau^(m-1)/(m-1)!`, `0<tau<1`.                       (5.1)

Since `d tau/dT=-sqrt(m)`,

`p_T(sqrt(m)-tau/sqrt(m))
 = sqrt(m) tau^(m-1)/(m-1)!`.                                  (5.2)

Multiplying by the conditional peak in (4.4) gives

`p_T(t) p_(U|T)(0|t)
 = [m 2^(-m+1)/((k-1)!)^2] tau^(m-2)`.                         (5.3)

For every `m>=4` this tends to zero as `tau downarrow 0`. Thus the normalized conditional height loses exactly one power of the physical corner mass: the conditional `tau^(-1)` explosion is compensated by the original-product slice weight `tau^(m-1)`.

Equation (5.3) is the source-valid interface. A proof may keep the **unnormalized** `(T,U)` density or the original product factors; it may not replace them by `sup_t ||p_(U|T=t)||_infinity`.

This is a near-coloop analogue of the earlier B16 scalar-fiber phenomenon, but now the failing object is precisely the two-dimensional product-projection interface that one would naturally use to interpolate from the exact null-coloop theorem.

## 6. The family itself is harmless: grouped original-source repair

The blowup above is an obstruction to a proof mechanism, not a QFORM counterexample. In fact the whole matrix family has a dimension-free density bound for **arbitrary** independent cap-one source laws.

Split the first leaf bank by sign and define the genuinely independent original-source bank projections

`A_+ = m^(-1/2) sum_{eps_j=+1} X_j`,

`A_- = m^(-1/2) sum_{eps_j=-1} X_j`.

Then

`T=A_+ + A_-`, `U=A_+ - A_-`,                                  (6.1)

and `(X_0,A_+,A_-,V)` are independent because they use disjoint original-coordinate banks. The source-valid one-dimensional Rogozin--Ball projection bound gives

`||p_(A_+)||_infinity <=2`,
`||p_(A_-)||_infinity <=2`,
`||p_V||_infinity <=sqrt(2)`.                                  (6.2)

Condition on `A_-`. Put `Y=2A_+` and `W=sqrt(2)V`, whose densities are at most one. Then `(X_0,Y,W)` remain independent cap-one variables, and the conditional quadratic part is

`B_a = [[0, sqrt(c)/2, 0],
        [sqrt(c)/2, sqrt(a)/2, 0],
        [0,0,1/2]]`.                                            (6.3)

The two eigenvalues of the upper `2x2` block are

`lambda_± = (sqrt(a) ± sqrt(4-3a))/4`.                          (6.4)

For `0<a<=1/64`,

`min |lambda_±| >= (sqrt(253)-1)/32
                  =0.4658116787...`,                            (6.5)

while the third eigenvalue is `1/2`. Therefore the completed pinned Theorem A, applied after conditioning `A_-`, yields uniformly in the conditioned value and in all affine terms

`||p_Q||_infinity
 <= 6 sqrt(pi) * 32/(sqrt(253)-1)
 = 22.8305205519... <23`.                                       (6.6)

This is a full essential-density bound for the entire family, all `m`, all `0<a<1/64`, and arbitrary cap-one independent source laws.

The proof order is the point: **group the disjoint original source banks first**, then pay a genuinely nondegenerate three-variable physical block. Conditioning on the weak same-bank projection `T` first destroys the useful density cap.

## 7. Required pinned-source curved inequality

The same family also gives a direct use of the pinned two-dimensional product-marginal curved theorem. Since `Lambda` has signature `(2,1)` and determinant modulus one, Theorem C of `COUNTEREXAMPLE_SEARCH.md@e5f71d79...` gives on the one-sheet side

`p_Q(s) <= pi sqrt(2)`, `s>=0`.                                 (7.1)

The proof of that theorem integrates the three-dimensional spectral projection along ruling lines and identifies each line integral with a two-dimensional marginal density of the **original product measure**. It does not assert independence of the projected coordinates. Thus (7.1) is compatible with the present construction even though `(T,U)` are strongly dependent near the cube corner.

The grouped bound (6.6) pays the remaining side as well.

## 8. Application to the latest partner reduction

Fleet03/B16 r26 proves that, after its Pluecker/duplicated-gate exits, the exact-rank-three residual that still needs a transition theorem is the one-coordinate near-coloop regime `c>63/64`.

The present family has

`c>63/64`, `a=1-c<1/64`, `h_j=1/m<1/64`,                       (8.1)

and can simultaneously make all physical diagonal and pair pivots arbitrarily small. It therefore tests precisely the geometry named by the partner's next obligation.

The conclusion is negative for one natural bridge:

`near-coloop -> condition weak leakage T -> exact-null-coloop endpoint`

cannot be dimension-free if the endpoint is fed a normalized conditional projection cap. The correct transition must either

- retain the unnormalized joint product-projection weight through the curved integral, as (5.3) indicates; or
- regroup disjoint original-coordinate source banks before paying curvature, as (6.1)-(6.6) do.

No small-coefficient deletion, moment/support assumption, arbitrary-joint coarea bound, rotated-coordinate independence, or worst-fiber supremum is used.

## 9. What remains unpaid

`QFORM-NEAR-COLOOP-UNNORMALIZED-OVERLAP-TRANSDUCER-v1`: in the partner-r26 `c>63/64` chamber, prove a uniform transition that keeps the same-bank weak leakage and transverse projection in **unnormalized original-product form** until the null-hub cross curvature is paid, or prove that the coefficient geometry always admits a bounded number of disjoint source-bank regroupings with a uniformly nondegenerate physical three-variable receiver.

The full arbitrary-higher-rank target remains separate and open. This report is not a counterexample to QFORM and does not claim global continuity.

## 10. Telemetry / scope

Model self-report: `GPT-5.6 Sol`. Configured reasoning effort: `UNKNOWN`. Provider reasoning-token and thinking-time telemetry: `null / not exposed`. Any elapsed-work number recorded at finish is wall-clock execution including connector/network and write/readback overhead, not pure thinking.
