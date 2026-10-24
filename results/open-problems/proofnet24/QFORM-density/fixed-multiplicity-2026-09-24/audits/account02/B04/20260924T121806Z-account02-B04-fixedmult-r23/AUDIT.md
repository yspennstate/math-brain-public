SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-24T12:18:06.155285Z.
attacking: QFORM-FIXED-MULTIPLICITY-AUDIT-20260924; geometric Brascamp--Lieb heat flow and limiting steps, full dependency reread, then a lower-threshold analytic improvement attempt.

# account02/B04 independent audit, run r23

## Source pin and package state

Owner baseline source commit: `7c0d6e60946b19423e6400a12d34b473cf0591e2`.
Recorded source SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.
Exact manuscript git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`.
Fresh `master` advanced during the run from `3fdceee8f151512db356be57565c1786b19b0bc0` to `c86b275521a4acad3df614a0e2a12d24f8cb7909`, but the manuscript blob remained exactly the pinned blob. I reread all 790 source lines from that blob, plus the current `README.md` and `AUDIT.md`.

At fresh master, `SOURCE_MANIFEST.json`, `proof_map.csv`, `verify.py`, and `checks.json` are still absent from the stated root (all explicit fetches returned 404). Therefore the finite-check/reproducibility bundle is **GAP / UNCHECKED** as a repository package. This is not a mathematical gap in the self-contained manuscript.

## Overall mathematical verdict

**PASS.** I found no FALSE mathematical statement and no unresolved mathematical GAP in the written 17-eigenvalue proof. No mathematical source range remains UNCHECKED in this review. The candidate remains only a fixed-multiplicity theorem; the unrestricted three-eigenvalue QFORM conjecture is not proved here.

A later peer report labeled the singular-matrix paragraph of `lem:schur` a repairable GAP. I independently rechecked that point and do **not** sustain the GAP: the moving-threshold argument as written is terse but sufficient. Details are below.

## Complete source-range audit

| Source lines | Status | Independent check |
|---|---|---|
| 1--74 | PASS | Definitions, singular-value convention, theorem quantifiers, affine terms, and `K^2/s` scaling architecture are consistent. The pivot/no-pivot split is exhaustive under the stated definition. |
| 75--129 | PASS | Fourier convention, Gaussian transform, Plancherel via Gaussian regularization, inversion, weak identification of the smoothed law, and the power-envelope constant are correct. |
| 130--169 | PASS | The Gamma representation for `|x|^{-1/2}`, Gaussian inversion, Tonelli order, inner `v` integral, coefficient `1/sqrt(2*pi)`, and the `12 sqrt(u)` weighted envelope are correct. |
| 170--218 | PASS | Singular-value perturbation/rank shift works without symmetry. Schur spectral count is valid in both invertible and singular cases. Strict diagonal dominance is valid for the later nonsymmetric auxiliary block. |
| 219--255 | PASS | Geometric rank-one Brascamp--Lieb heat-flow proof, including differentiation, frame contraction, integration by parts, large-time Gaussian limit, small-time Lebesgue-point limit, zero-mass factors, and monotone truncation. Detailed reconstruction below. |
| 257--309 | PASS | Product-projection density argument uses only a deterministic orthogonal change in an integral, never rotated independence. The `b_i` frame, `f_i^{1/b_i}<=f_i`, entropy estimate, full-dimensional endpoint, and scalar scaling are correct. Scalar Fourier-power exponents and constants are correct. |
| 311--421 | PASS | Two/four-power decoupling uses genuine independent copies and no moments. In the regularized determinant theorem the graph frame, Jacobians, `L^p` exponents, entropy term, choice `alpha=(2*pi*e)^2`, determinant factor, and final `-1/8` exponent all check. Cauchy--Binet and the order-5/order-3 envelopes are correct. |
| 422--519 | PASS | Scalar-square profile and conditional measure domination are correct. Definite pair Jacobian is correct. Hyperbolic pair branches/Jacobian/tails/logarithm are valid with rough densities through nonnegative test functions. Quarter-power concentration and the logarithmic potential bound have correct Gaussian and Gamma powers. |
| 520--679 | PASS | Ordered disjoint volumes, sampled interpolation, bordered determinant, singular-seed inequality, support of `R-P`, global rank `<=3r`, restricted rank `<=r`, and vanishing of `D` on the seed are all correct. Spectral-to-volume counting and the random-cut factor `4^{-k}` close with the displayed constants. |
| 680--790 | PASS | Kernel integrals, scalar/definite/indefinite pivot half-potentials, truncated-versus-full distinction, nine-direction receiver, main case split, Schur spectral survivors, affine terms, and final normalization all check. The limitations correctly avoid a three-eigenvalue or global-continuity claim. |

## B04 lens: heat-flow proof rebuilt

For bounded compactly supported positive-mass `h_i`, let `f_i(t,.)=g_t*h_i`, where the manuscript heat kernel satisfies `partial_t f_i=partial_s^2 f_i`. Put

`F(t,x)=prod_i f_i(t,u_i.x)^{c_i}` and `v_i=partial_s log f_i`.

Direct differentiation gives

`partial_t F-Delta F = F[sum_i c_i v_i^2 - |sum_i c_i u_i v_i|^2]`.

If `W` has columns `sqrt(c_i)u_i`, the frame identity is `WW^T=I`; hence `||W||=1`, and applying it to `(sqrt(c_i)v_i)` proves the bracket is nonnegative.

On every compact time interval `[tau,T] subset (0,infinity)`, compact support of `h_i` gives Gaussian tails for `f_i` and polynomial growth of the logarithmic derivatives. The frame identity turns their product into an integrable Gaussian in `x`; differentiation under the integral and integration by parts therefore have an honest common majorant, so `I(t)=int F(t,x) dx` is nondecreasing.

Taking traces gives `sum_i c_i=d`. With `M_i=int h_i` and `x=sqrt(t)z`,

`sqrt(t) f_i(t,sqrt(t)u_i.z) -> (4*pi)^(-1/2) M_i exp(-(u_i.z)^2/4)`.

The product exponent is `-sum_i c_i(u_i.z)^2/4=-|z|^2/4`. Compact support supplies a uniform `C exp(-|z|^2/8)` bound for `t>=1`, so dominated convergence gives

`lim_{t->infinity} I(t)=prod_i M_i^{c_i}`.

For `t downarrow 0`, the non-Lebesgue-point set of each one-dimensional `h_i` is null, and its inverse image under nonzero `x -> u_i.x` is null by rotation/Fubini. The finite union is null. Thus the heat convolutions converge simultaneously almost everywhere and Fatou gives

`int prod h_i(u_i.x)^{c_i} dx <= liminf_{t downarrow0} I(t) <= lim_{t->infinity} I(t)`.

Zero-mass factors vanish a.e. Finally `h_i^{(m)}=min(h_i,m) 1_{[-m,m]}` increase pointwise to arbitrary nonnegative integrable `h_i`; monotone convergence applies on both sides. I found no hidden nonintegrable boundary term, no reversed limit inequality, and no unjustified exchange.

## Disputed Schur singular-limit paragraph: PASS, not GAP

For singular `A`, the manuscript takes a sequence `epsilon->0` for which `A_epsilon=A+epsilon I` is invertible. The pivot `B+epsilon I` stays invertible for small `epsilon`, and the Schur complement `S_epsilon` tends to `S`. It observes

`N_{A_epsilon}(t-|epsilon|) >= N_A(t)`.

Applying the already-proved invertible case at the positive threshold `t-|epsilon|` gives

`N_{S_epsilon}(t-|epsilon|) >= N_A(t)-k`.

Let `m=N_A(t)-k`; if `m<=0` there is nothing to prove. Otherwise the last count is exactly the statement that the `m`-th ordered eigenvalue modulus (equivalently singular value, since `S_epsilon` is symmetric) satisfies

`s_m(S_epsilon) >= t-|epsilon|`.

Ordered singular values are continuous under matrix convergence, so `S_epsilon->S` and `t-|epsilon|->t` imply

`s_m(S) >= t`.

Therefore `N_S(t)>=m=N_A(t)-k`. No rate comparison between eigenvalue motion and `|epsilon|` is needed. In particular, a concern that an eigenvalue might move with speed `C|epsilon|`, `C>1`, does not invalidate the argument: the displayed lower bound itself holds along the entire chosen sequence, and passing that scalar inequality to the limit is sufficient. A fixed-`delta` proof is also valid, but it is a clarification rather than a necessary repair.

Downstream status: scalar-pivot and indefinite-pair uses of `lem:schur` remain PASS without changing the manuscript or constants.

## Constants and endpoint checks

The determinant theorem normalization is internally exact: fourth-power decoupling, scalar Fourier exponent `2/d_i`, coordinate entropy `e^{theta/2}`, and `sqrt(alpha)=2*pi*e` cancel to leave

`|phi_Z(t)| <= det(I+t^2 M^TM/(pi^2 e^2))^{-1/8}`.

Order five therefore gives exponent `5/4>1` and direct inversion; order three gives `3/4`, which is not directly integrable but is exactly sufficient after the `|t|^{-1/2}` Riesz weight. The manuscript never confuses these two endpoints.

The main normalized branch constants remain below `10^4`; general `K,s` scaling is exact because with `Y=KX`, `tilde Q=(K^2/s)Q` and the quadratic matrix is `A/s`.

## Lower-threshold work this run

I proved a strict extension of my preceding leverage-half lemma: an adaptive fractional-leverage determinant family parameterized by `q in [1,2]`. It yields direct density from an order-`k` crossing whenever `k>2q` and the maximum physical row leverage is at most `q/2`. In particular, order three is directly integrable under the strictly larger condition `max leverage <3/4`, with an explicit constant depending on the leverage gap. The full proof is saved separately in this run's immutable improvement folder.

This still does **not** lower the unconditional theorem from 17. The baseline random-cut argument controls crossing volume but does not give a uniform leverage gap. I also recorded an explicit no-pivot `s_13>=1` construction showing that a target-scale order-four crossing itself may have row leverage exactly one; therefore one cannot finish a 13-direction proof by asserting that volume richness automatically makes the selected physical crossing subcritical for the adaptive determinant theorem. A separate endpoint/high-leverage receiver is still required.

## Status ledger

- 17-eigenvalue mathematical manuscript: **PASS** in this independent account02/B04 reread.
- Geometric Brascamp--Lieb heat-flow and rough limiting steps: **PASS**.
- Singular Schur limit: **PASS**; a reported repairable GAP is a false positive under the ordered-singular-value reading above.
- Root reproducibility files named by README/objective: **GAP / missing**, computational claims therefore **UNCHECKED** in this repository snapshot.
- Unconditional threshold below 17: **NOT PROVED in this run**.
- Unrestricted three-eigenvalue conjecture: **OPEN**.
- New supporting improvement: adaptive fractional-leverage determinant theorem; does not weaken hypotheses of the scoped crossing result, but does not close the structural leverage endpoint.
