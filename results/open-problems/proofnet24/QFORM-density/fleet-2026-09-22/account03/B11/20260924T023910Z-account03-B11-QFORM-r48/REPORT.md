SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-24T02:39:10Z.
attacking: the punctured near-coloop third-square interface: test whether the r46 L^3 hyperbolic resource plus the determinant-tied L^(3/2) square can be combined under same-bank dependence using only density caps; preserve a decisive counterexample and identify the missing product-provenance inequality.

# account03/B11 r48 — sharp same-bank L^3 x L^(3/2) interface falsifier at arbitrarily small puncture

Programme: `QFORM-DENSITY-3EIG-20260922`.
Assignment: indefinite signatures `(2,1)` / `(1,2)`.
Status: **NEW REFUTED INTERMEDIATE MECHANISM / EXACT PUNCTURE GEOMETRY MATCH / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN**.
Execution: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted owner conjecture remains OPEN / NOT PROVED / NOT DISPROVED. This report does **not** give a counterexample to QFORM. It gives a sharp counterexample to the dependence-blind interface suggested after r46/account02-B11: finite `L^3` control of the hyperbolic-plus-puncture part and finite `L^(3/2)` control of the third square cannot be combined into `L^infinity` when the two pieces live on the same dependent residual source merely from bounded joint/marginal densities. The missing ingredient must use the fact that the residual triple is an **orthogonal linear projection of an original independent product source**.

No Gaussianity, log-concavity, moments, compact support assumption on the target problem, post-rotation independence, law-uniform pointwise van-der-Corput decay, arbitrary-joint coarea bound, conditional-density cap as independence, or perturbative deletion of the puncture is used.

## 1. Fresh sources and first unpaid implication


Immediate predecessor:

- repository: `yspennstate/math-open-problems`
- commit: `559dcad1a7ad077c7e784bd806602b951926fe28`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260924T011327Z-account03-B11-QFORM-r46/REPORT.md`.

Its theorem `QFORM-PRODUCT-BANK-HYPERBOLIC-LM-v1` says that if `H` is independent of an arbitrary source `Y`, `||p_H||_infinity<=F`, `U=U(Y)` has marginal density cap `G`, `Psi(Y)` is arbitrary, and

`Z=(bU+d)H+Psi(Y)`, `b!=0`,

then for every integer `m>=2`,

`||p_Z||_m^m <= m! (2FG/|b|)^(m-1)`.                       (1.1)

For the exact null-puncture normal form from r45,

`Q = 2 kappa sqrt(q) H W
     + 2 kappa sqrt(1-q) T W
     + c (V')^2 + delta W^2`,                               (1.2)

where `H` is an ORIGINAL independent scalar, `(T,W,V)` is an internally dependent orthonormal projection of the residual ORIGINAL product source, and

`kappa^2 |c| = |det M| >= s^3`,                              (1.3)

r46 gives the full same-bank hyperbolic part finite `L^m` norms, including a uniform `L^3` resource. What was missing was how to spend the third square when `V` belongs to the same residual source.

A concurrent account02/B11 theorem, canonical report at

`yspennstate/math-open-problems@02aedcd3be33ace107851fa74e0b9ac846d0aa25`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B11/B11-20260924T012138Z-auto11/REPORT.md`,

proves that if the third-square scalar is genuinely **source-disjoint**, then the r46 `L^3` bound pairs with the square's uniform `L^(3/2)` bound to give a determinant-homogeneous `L^infinity` estimate. It explicitly leaves the same-bank case open.

The present run tests whether source-disjointness in that final Young/Holder step can be weakened to bounded same-bank joint/marginal densities. The answer is no, sharply, even at an arbitrarily small puncture and even when all the r45 spectral identities hold exactly.

## 2. Counterexample to the dependence-blind `L^3 x L^(3/2)` interface

Fix

`0 < eta <= 1/sqrt(63)`.                                    (2.1)

Let

`H, R, V, W`

be four mutually independent `Uniform[-1/2,1/2]` variables. On the probability-one event `W!=0`, define

`T = R - V^2/(2 eta W)`.                                    (2.2)

Define `T` arbitrarily on `W=0`.

The transformation

`(r,v,w) -> (t,v,w)`,
`r = t + v^2/(2 eta w)`

has Jacobian one in the `r/t` coordinate whenever `w!=0`. Hence `(T,V,W)` has probability density

`g_eta(t,v,w)
 = 1_{|v|<=1/2}
   1_{|w|<=1/2}
   1_{|t + v^2/(2 eta w)|<=1/2}`                            (2.3)

for `w!=0`, with any definition on the null plane `w=0`.

Therefore

`0 <= g_eta <= 1`, `int g_eta = 1`.                         (2.4)

More is true. Every coordinate one- and two-dimensional marginal used by a naive density-cap argument also has cap at most one:

`||p_W||_infinity = ||p_V||_infinity = 1`,                  (2.5)

`||p_T||_infinity <= 1`,                                    (2.6)

`||p_(V,W)||_infinity = 1`,                                 (2.7)

`||p_(T,W)||_infinity <= 1`,
`||p_(T,V)||_infinity <= 1`.                                (2.8)

Indeed (2.7) follows because for fixed `(v,w)` the allowed `t`-interval has length exactly one, and each inequality in (2.8) follows by integrating an indicator over a variable ranging in an interval of length one. Equation (2.6) follows by integrating over the unit `(v,w)` square.

Now form

`Q_eta = 2 H W + 2 eta T W + V^2`.                          (2.9)

Substituting (2.2) gives the exact cancellation

`Q_eta = 2 W (H + eta R)`.                                  (2.10)

Thus the apparently genuine third square is completely neutralized by same-source dependence in the puncture.

### The output density is logarithmically unbounded

Put

`S = H + eta R`.

Since `0<eta<1`, the convolution density of `S` has the exact plateau

`p_S(s)=1` whenever `|s| <= (1-eta)/2`.                     (2.11)

The variable `S` is independent of `W`. From (2.10), for `z!=0`,

`p_(Q_eta)(z)
 = int_{-1/2}^{1/2} p_S(z/(2w)) /(2|w|) dw`.                (2.12)

Whenever

`0 < |z| < (1-eta)/2`,                                      (2.13)

the integrand equals `1/(2|w|)` on the region

`|z|/(1-eta) <= |w| <= 1/2`.

Therefore

`boxed:
 p_(Q_eta)(z)
 >= log((1-eta)/(2|z|)) -> infinity  as z->0.`               (2.14)

So `Q_eta` has no essentially bounded density.

At the rank-two endpoint, the familiar centered-unit-uniform identity is recovered in scale:

`p_(2HW)(z)=log(1/(2|z|)), 0<|z|<1/2`.                      (2.15)

The construction shows that an arbitrarily small but nonzero same-bank puncture can preserve that logarithmic obstruction if one forgets the residual product-projection provenance.

## 3. The coefficient geometry matches the r45 hard chamber exactly

Relative to the coordinates `(H,T,V,W)`, (2.9) has symmetric coefficient matrix

`B_eta = [[0,0,0,1],
          [0,0,0,eta],
          [0,0,1,0],
          [1,eta,0,0]]`.                                    (3.1)

The `V` direction is an eigenvector of eigenvalue `1`. The remaining `(H,T,W)` block has characteristic polynomial

`lambda (lambda^2-(1+eta^2))`.

Hence

`spec(B_eta) = {-sqrt(1+eta^2), 0, 1, +sqrt(1+eta^2)}`.      (3.2)

Thus `B_eta` has exact rank three, signature `(2,1)`, and all three nonzero eigenvalues have absolute value at least one. Negating the matrix gives the `(1,2)` analogue.

The unit kernel vector is

`n_eta = (-eta,1,0,0)/sqrt(1+eta^2)`.                       (3.3)

Consequently the leverage of the physical hub coordinate `H` in the active rank-three range is

`q = 1 - |<e_H,n_eta>|^2
   = 1/(1+eta^2)`.                                           (3.4)

The bound (2.1) is exactly equivalent to

`q >= 63/64`.                                                (3.5)

Moreover, in the r45 notation, set

`kappa = sqrt(1+eta^2)`, `c=1`, `delta=0`.                   (3.6)

Then

`kappa sqrt(q)=1`,
`kappa sqrt(1-q)=eta`,                                      (3.7)

so (1.2) becomes exactly (2.9), and

`kappa^2 |c| = 1+eta^2
             = |product of the three nonzero eigenvalues|`. (3.8)

Therefore this is not a loose caricature: it reproduces the **exact null-pivot, near-coloop, determinant-tied third-square coefficient geometry** of the surviving B11 normal form.

## 4. Even the exact marginal analytic resources are present

Split (2.9) as

`Z_eta = 2 H W + 2 eta T W`,
`S_3 = V^2`,
`Q_eta = Z_eta + S_3`.                                      (4.1)

The r46 theorem (1.1) applies to `Z_eta` with

`F=1`, `U=W`, `G=1`, `b=2`, `Psi=2 eta T W`.

It therefore gives the rigorous bound

`boxed: ||p_(Z_eta)||_3^3 <= 6.`                            (4.2)

Independently, because the **marginal** `V` is exactly `Uniform[-1/2,1/2]`, the square `S_3=V^2` has density

`p_(S_3)(s)=s^(-1/2) 1_{0<s<1/4}`,

and hence

`int p_(S_3)^(3/2) = 2 sqrt(2)`,
`boxed: ||p_(S_3)||_(3/2)=2.`                               (4.3)

Thus both factors of the determinant-homogeneous account02/B11 mechanism exist quantitatively:

- a uniformly finite `L^3` hyperbolic-plus-puncture density;
- a uniformly finite `L^(3/2)` third-square density.

Nevertheless their **dependent sum** has the logarithmically unbounded density (2.14). Hence no inequality of the schematic form

`||p_(Z+S)||_infinity <= C ||p_Z||_3 ||p_S||_(3/2)`          (4.4)

can hold for arbitrary same-source dependence. Ordinary Young/Holder works in the source-disjoint case because it is a convolution; there is no dependence-safe replacement based only on the two marginal norms, even together with (2.3)-(2.8), the tiny-puncture condition, and the rank-three determinant identity.

This is the precise mathematical obstruction the current fleet must avoid.

## 5. Why this is NOT a QFORM counterexample

The target requires the ORIGINAL input coordinates to be independent. The vector `(H,T,V,W)` constructed above is not an independent product vector: `(T,V,W)` is generated from the independent cube `(R,V,W)` by the nonlinear triangular map (2.2).

When (2.9) is pulled back to those actual independent variables, the third square cancels and

`Q_eta(H,R,V,W)=2HW+2 eta RW`,                              (5.1)

whose coefficient matrix on the original product variables has rank only two. Therefore the construction does not satisfy the target hypothesis of three large eigenvalues in the **original independent coordinates**.

Equally, no representation of the residual law (2.3) as the orthogonal **linear** projection of an independent cap-one product source is supplied. The counterexample therefore refutes an intermediate abstraction, not the conjecture.

This distinction is exactly the live correction `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1` in a sharper form adapted to the r45/r46 puncture: bounded joint and conditional/marginal information can coexist with an exact same-source cancellation of the third curvature.

## 6. Designated account04/B11 result applied at an actual inequality

The completed designated partner result consumed from

`yspennstate/math-open-problems@30555c1ca97752e10f5089ccd95f8514c704be5a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T131400Z-account04-B11-extension-mass-r6/REPORT.md`,

gives the pair-area receiver

`||p_Q||_infinity <= 128 sqrt(2)/(s sqrt(g_ij))`.            (6.1)

In the actual B11 near-coloop geometry, for hub `0` and residual transverse leaf `j`,

`g_0j = q ||w_j||^2`.                                       (6.2)

If the large-leaf exit occurs,

`q >= 63/64`, `||w_j||^2 >= 1/36`,                          (6.3)

then

`g_0j >= (63/64)(1/36) = 7/256`.                            (6.4)

Substitution into (6.1) gives

`boxed:
 ||p_Q||_infinity
 <= 2048 sqrt(2/7) / s
 = 1094.7020468732903... / s.`                              (6.5)

Thus the same-bank interface isolated in Sections 2-5 is reached only after this already-paid partner branch has been removed.

## 7. What the third direction must do in the true product problem

The rank-two control remains

`p_(2XY)(t)=log(1/(2|t|))`,                                  (7.1)

for centered unit uniforms. Account02/B11 shows that a genuinely source-disjoint square removes this logarithm at the exact conjugate exponents

`L^3 x L^(3/2) -> L^infinity`.                               (7.2)

The present counterexample shows that the same exponent bookkeeping alone is insufficient in the same-bank punctured state: the square can be hidden inside the puncture by dependence while every naive marginal cap remains benign.

For the **true** r45 state, however, `(T,W,V)` is not an arbitrary joint law. It is an orthonormal linear projection of independent original coordinates. If the residual coefficient vectors are `t=(t_j)`, `w=(w_j)`, `v=(v_j)`, then

`sum_j (t_j,w_j,v_j)^T(t_j,w_j,v_j) = I_3`,                 (7.3)

and the residual joint characteristic function factorizes exactly as

`Phi_(T,W,V)(xi_T,xi_W,xi_V)
 = product_j phi_j(t_j xi_T + w_j xi_W + v_j xi_V)`.         (7.4)

The nonlinear cancellation law (2.3) is not supplied with such a factorization. Therefore the next proof must spend (7.3)-(7.4), or an equivalent original-coordinate bank decomposition, **before** collapsing the residual law to density caps or marginal `L^p` norms.

The next exact B11 target is therefore

`QFORM-R46-ORTHOGONAL-PRODUCT-L3-L32-TRACE-v1`:

> For the true residual orthogonal product projection in (1.2), prove a dependence-safe curved trace / integrated-Fourier inequality at the determinant-homogeneous `L^3 x L^(3/2)` scale, uniformly as `q->1`, retaining `2 kappa sqrt(1-q)TW` and `delta W^2`; or force an already-paid source-disjoint square, pair-area, or rank-three-volume exit. Any proof using only the residual joint-density cap, coordinate marginal caps, or the separate `L^3` and `L^(3/2)` norms is ruled out by Sections 2-4.

This is a stricter and more useful formulation than the previous generic `LM-to-Linfinity` request.

Arbitrary additional nonseparable spectrum remains a separate bridge after the exact-rank-three puncture is paid. Full-target continuity also remains open.

## 8. Verification and scope

`VERIFY.py` and `VERIFY_OUTPUT.txt` in this run directory deterministically check:

1. the spectral/leverage formulas (3.2)-(3.8) for punctures down to `eta=10^(-6)` and at the live endpoint `eta=1/sqrt(63)`;
2. the partner constant in (6.5);
3. the explicit logarithmic lower bound (2.14) at shrinking nonzero `z` values.

No Monte Carlo histogram is used. The checks verify only algebra/numerics; the proof above carries the mathematical claim.

Scope summary:

- `QFORM-SAMEBANK-L3-L32-DEPENDENCE-BARRIER-v1`: **PROVED explicit counterexample to the intermediate interface**.
- exact r45 coefficient geometry: **MATCHED** for every `0<eta<=1/sqrt(63)`.
- r46 `L^3` resource and exact square `L^(3/2)` resource: **BOTH PRESENT** in the counterexample, but their dependent sum is unbounded.
- designated account04/B11 pair-area theorem: **APPLIED** at (6.4)-(6.5).
- full QFORM: **OPEN**.
- full exact-rank-three same-bank puncture: **OPEN**.
- full continuity: **OPEN**.
