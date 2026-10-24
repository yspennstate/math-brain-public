SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B11, 2026-09-23T21:16:33Z.
attacking: the same-bank punctured-collar interpolation; first force an exact ORIGINAL-coordinate cocircuit exit before paying any vanishing third-crossing singular value.

# account01/B11 — conditionable cocircuit compiler for the indefinite near-coloop collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control consumed:** revision `2026-09-22.15`, latest continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREM / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new cocircuit branch proves essential boundedness. The partner fixed-puncture branch used below proves continuity in its own scope. No global continuity claim is made.

The unrestricted owner target remains **OPEN**. No Gaussianity, log-concavity, moments, compact support, connected support, post-rotation independence, pointwise van-der-Corput decay, conditional-cap-as-independence, or small-random-perturbation step is used.

## 1. Fresh source state and exact gap

The live B11 punctured-collar state comes from account03/B11 r40--r41 and account02/B11's completed fixed-puncture theorem.

Write the exact-rank-three form

`A = R M R^T`, `R^T R = I_3`, `s := min_j |lambda_j(M)| >= 1`,

and in the true near-coloop chamber choose the ORIGINAL hub row

`r_0 = sqrt(c) e`, `c > 63/64`.

For every residual original coordinate write

`r_i = s_i e + w_i`, `w_i in e^perp`.

After the already-paid large-leaf exit, r40 works in the chamber

`||w_i||^2 < 1/36` for every residual row,                                  (1.1)

and gives a literal original-coordinate partition `S sqcup T` with

`lambda_min(G_S), lambda_min(G_T) > g_0 := 17/288`,                         (1.2)

where `G_B = sum_(i in B) w_i w_i^T`.

For each bank `B`, put

`h_B = sum_(i in B) s_i w_i`, `a_B = G_B^(-1) h_B`,

and define the exact regression residual coefficients

`q_i^(B) := s_i - a_B^T w_i`, `i in B`.                                     (1.3)

Then

`rho_B = sum_(i in B) (q_i^(B))^2`

is the graph-defect variance. The exact-graph endpoint is `q^(B)=0`; the punctured collar has `rho_S,rho_T>0`, possibly arbitrarily small.

The completed account02/B11 theorem at `math-open-problems@25c25e15fa0f570e7b0b1a2a9fab0811eda07113`, with its r41 addendum at `c6063d311ba25c0f98dbc4add4090b51607062bb`, proves for a nonzero 3D physical crossing matrix `C_cross`

`||p_Q||_infinity <= 6 |det C_cross|^(-1/3)`,                              (1.4)

with a continuous density. Together with r40's

`sigma_1 sigma_2 > kappa_* s^2`,
`kappa_* := (34/111)(17/288)^2 = 0.0010672564926037...`,                    (1.5)

this pays every fixed puncture but deteriorates as the third crossing singular value `sigma_3 -> 0`.

The goal of this run is not to treat a small graph defect as a small random error. Instead, I prove that whenever the defect is carried by a cheap ORIGINAL-coordinate cocircuit, one may condition those coordinates away **exactly**, retain a quantitatively nondegenerate transverse two-plane, and pay the resulting exact graph for every value of the physical hub pivot.

Two previously proved account01/B11 analytic receivers are used as immutable inputs:

1. `QFORM-SUBCRITICAL-HUB-PLANAR-CORE-v1`, `math-open-problems@cedc867395f462e31df64232907480cea07db3d5`, which for an independent cap-one scalar and an independent planar vector of joint density cap `M` gives `||p_Q||_infinity <= B(r,M)/sigma` when the 3D Hessian has `sigma_min >= sigma` and normalized scalar pivot at most `r<1`.
2. `QFORM-ROUGH-HUB-FULL3-DISCRIMINANT-v1`, canonical in the preceding account01/B11 run `math-open-problems@5aa9163cd7259b345e1ec802e27dbadaed68cbba`, which in the scalar-plus-two-product-forms geometry gives

`||p_Q||_infinity <= 128 (|a det H| G)^(-1/4)`                              (1.6)

for scalar density cap one, where `a` is the scalar pivot and `G` is the two-form Gram determinant. Arbitrary deterministic affine terms are allowed.

## 2. New theorem: all-pivot exact cocircuit compiler

### Theorem `QFORM-NEARCOLOOP-CONDITIONABLE-COCIRCUIT-ALLPIVOT-v1`

Retain the exact-rank-three near-coloop state above with `c>63/64`. Let `K` be **any** set of residual ORIGINAL coordinates that will be conditioned on, and let `R=K^c` be the residual coordinates retained together with the hub. Assume there is a vector `a in e^perp` such that

`s_i = a^T w_i` for every `i in R`,                                         (2.1)

and assume the retained transverse Gram matrix

`G_R := sum_(i in R) w_i w_i^T`

satisfies

`lambda_min(G_R) >= g`, with `0<g<=1/2`.                                   (2.2)

Then, for arbitrary independent cap-one input densities and for **every** physical hub pivot `A_00=c e^T M e`, the conditional and unconditional laws of `Q=X^TAX` have an essentially bounded density satisfying

`boxed:
 ||p_Q||_infinity < 170/(g s).`                                             (2.3)

The estimate is invariant under `M -> -M`, hence covers both signatures `(+,+,-)` and `(+,-,-)`.

The theorem permits conditioning any other ORIGINAL coordinates as well; those variables only create deterministic affine and constant terms.

### Proof

Condition on every original coordinate in `K`. Put

`Y = G_R^(-1/2) sum_(i in R) w_i X_i in R^2`.                              (2.4)

The two coefficient columns producing `Y` are orthonormal in the ORIGINAL retained source space, so the product-projection theorem gives

`||p_Y||_infinity <= 2`.                                                    (2.5)

Moreover `Y` is genuinely independent of the untouched ORIGINAL hub scalar `X_0`.

By the exact graph relation (2.1), after conditioning the spectral vector is an affine translate of

`sqrt(c) e X_0 + e a^T G_R^(1/2)Y + G_R^(1/2)Y`.                           (2.6)

In the deterministic spectral splitting `span(e) direct_sum e^perp`, write

`L = [[sqrt(c), r^T],[0,G_R^(1/2)]],  r=G_R^(1/2)a`.                       (2.7)

The conditional three-variable Hessian is

`H = L^T M L`.                                                             (2.8)

Because the total residual longitudinal Parseval energy is `1-c`, (2.1) gives

`||r||^2 = a^T G_R a = sum_(i in R) s_i^2 <= 1-c`.                         (2.9)

Factor

`L = diag(sqrt(c),G_R^(1/2)) S`,
`S=[[1,u^T],[0,I_2]]`, `u=r/sqrt(c)`.                                      (2.10)

Since `c>63/64`,

`||u||^2 <= (1-c)/c < 1/63`.                                               (2.11)

Also `g<=1/2<c`, so

`sigma_min(diag(sqrt(c),G_R^(1/2))) >= sqrt(g)`.                           (2.12)

The inverse shear satisfies `||S^(-1)||_op <= 1+||u||`; hence

`sigma_min(L)^2
 >= g/(1+1/sqrt(63))^2
 =: rho(g).`                                                               (2.13)

Therefore

`sigma_min(H) >= rho(g) s`,                                                (2.14)

and consequently

`|det H| >= [rho(g)s]^3`.                                                   (2.15)

The first physical coordinate of the conditional 3D form is exactly the original hub variable, so its scalar pivot is

`h := H_11 = c e^T M e = A_00`.                                           (2.16)

Fix the numerical split `r_* = 0.85`.

**Case 1: `|h| <= r_* rho(g)s`.** Apply the completed subcritical scalar-planar theorem with planar cap `M=2`, singular scale `rho(g)s`, and ratio `r_*`. Its explicit constant is

`B(0.85,2)=133.7856144314...`,                                             (2.17)

so

`||p_Q||_infinity <=133.786/[rho(g)s]`.                                   (2.18)

**Case 2: `|h| > r_* rho(g)s`.** Apply `QFORM-ROUGH-HUB-FULL3-DISCRIMINANT-v1` to the genuine original scalar `X_0` and the two normalized product forms in (2.4). Here the two-form Gram determinant is one. By (2.15),

`|h det H| > r_* [rho(g)s]^4`,                                             (2.19)

hence

`||p_Q||_infinity
 <=128 r_*^(-1/4)/[rho(g)s]
 =133.3077008448.../[rho(g)s].`                                            (2.20)

Thus both cases are bounded by `133.786/[rho(g)s]`. Since

`rho(g)=g/(1+1/sqrt(63))^2`

and

`133.786 (1+1/sqrt(63))^2 =169.62049...<170`,                              (2.21)

we obtain (2.3), uniformly in all conditioned values. Averaging the interval inequality over the conditioned original coordinates preserves the same essential density cap. QED.

### Why this is not a perturbative theorem

No coefficient in the conditioned set `K` is assumed small. Those random variables are removed by genuine ORIGINAL-coordinate conditioning, and (2.1) is then an exact source-span identity on what remains. The estimate never replaces a nonzero defect by zero, never conditions on a dependent projection, and never rotates the input product law into independent spectral coordinates.

## 3. Punctured-collar corollary: a defect supported on at most two leaves is paid

Return to the r40 partition `S sqcup T`, with (1.1)--(1.2). Fix one bank `B` and let

`E_B := { i in B : q_i^(B) !=0 }`                                         (3.1)

be the exact ORIGINAL-coordinate support of its regression defect from (1.3). Put `R=B\E_B`. Then by definition

`s_i = a_B^T w_i` for every `i in R`;                                     (3.2)

the retained bank is an exact graph after conditioning `E_B` and the entire opposite bank.

Also

`G_R = G_B - sum_(i in E_B) w_i w_i^T`.                                  (3.3)

Thus

`lambda_min(G_R)
 >=17/288 - ||sum_(i in E_B) w_iw_i^T||_op`.                              (3.4)

### Corollary 3.1 — transverse-cost cocircuit exit

If

`||sum_(i in E_B) w_iw_i^T||_op <= 1/18 =16/288`,                         (3.5)

then `lambda_min(G_R)>1/288`, and Theorem 2 gives

`boxed:
 ||p_Q||_infinity < 170*288/s =48960/s.`                                  (3.6)

Using the unrounded constant from (2.21) improves this to

`||p_Q||_infinity <48851/s`.                                               (3.7)

This is a genuine nonzero-defect branch: `rho_B` may be positive and the defect values `q_i^(B)` may be arbitrarily large relative to their eventual small-collar scale. Only their exact ORIGINAL-coordinate carrier is conditioned away.

### Corollary 3.2 — at most two defect coordinates

In the already-paid-large-leaf complement (1.1), if `|E_B|<=2`, then

`||sum_(i in E_B) w_iw_i^T||_op
 <=sum_(i in E_B)||w_i||^2 <2/36=1/18`.                                   (3.8)

Therefore every punctured bank whose exact graph defect is carried by at most two original coordinates satisfies (3.6)--(3.7).

If `|E_B|<=1`, then

`lambda_min(G_R)>17/288-1/36=1/32`,                                      (3.9)

and the same theorem gives the sharper rounded estimate

`||p_Q||_infinity <5440/s`                                                (3.10)

(the unrounded value is `<5428/s`).

Hence a genuinely unpaid punctured double-graph sequence in the r40 hard chamber must have **at least three defect-carrying original coordinates in each bank**, and more invariantly the exact defect carrier of each bank must cost more than `1/18` in transverse operator mass. This is a new exact source-provenance narrowing; it does not follow from `rho_B>0` alone.

## 4. Designated account02/B11 theorem applied to an actual collar inequality

Apply the completed account02/B11 fixed-puncture theorem (1.4) to the actual r40 crossing singular values. From (1.5), if

`sigma_3 >= s/288`,                                                        (4.1)

then

`|det C_cross| = sigma_1 sigma_2 sigma_3
 > (kappa_*/288) s^3`.                                                     (4.2)

Therefore

`boxed:
 ||p_Q||_infinity
 <6 (288/kappa_*)^(1/3) s^(-1)
 =387.7267913375.../s <388/s.`                                             (4.3)

The partner theorem also gives a continuous density on this branch. Thus, after this actual partner application and the new cocircuit compiler, a still-unpaid r40/r41 sequence must simultaneously satisfy

`0<sigma_3<s/288`,                                                         (4.4)

and neither bank may have an exact graph-defect carrier of transverse operator cost `<=1/18` (in particular neither defect can be supported on only one or two leaves).

This isolates the genuinely diffuse same-bank interpolation problem rather than merely saying `sigma_3` is small.

## 5. The opposite-sign logarithmic endpoint and the third direction

The required rank-two control example remains exact. For independent centered unit uniforms,

`p_(2XY)(t)=log(1/(2|t|)),  0<|t|<1/2`.                                  (5.1)

So the opposite-sign rank-two saddle itself is unbounded.

The new branch identifies a precise way the third direction survives after source-safe deletion. Once a cheap defect cocircuit is conditioned away, the untouched hub plus the retained transverse bank form a genuine three-variable scalar-plus-planar core whose least singular value is at least `rho(g)s`. If the hub pivot is subcritical, all three curvatures enter the three-dimensional coarea receiver. If the hub pivot is large, the discriminant identity behind the rough-hub theorem produces a nondegenerate rank-two half-Riesz receiver with determinant currency `|h det H|`. In neither case is the third direction replaced by a bounded-density projection slogan; it appears as an actual nonzero 3D Hessian scale.

On the complementary partner branch, a nonzero third cross singular value upgrades the rank-two `|t|^-1` Fourier endpoint to the integrable `|t|^-3/2` regime. These are distinct legitimate mechanisms.

## 6. Verification and constants

The companion `VERIFY.py` checks the constants used above and stress-tests the deterministic singular-value estimate (2.13) on exact graph frames. The intended terminal marker is

`QFORM_B11_COCIRCUIT_ALLPIVOT_CHECK_PASS`.

The proof itself is analytic; the checker is diagnostic only.

## 7. Remaining implication

The first unpaid B11 collar is now sharpened to

`QFORM-DIFFUSE-DEFECT-SAMEBANK-INTERPOLATION-v1`:

> In the r40/r41 true-near-coloop state, assume `0<sigma_3<s/288`, the two dominant crossing singular values satisfy `sigma_1 sigma_2>kappa_*s^2`, and the internal curvature satisfies the r41 persistent-curvature lower bound. In addition, assume neither bank admits an exact graph-defect carrier of transverse operator cost `<=1/18`. Prove a universal density bound by exploiting the genuinely diffuse ORIGINAL-coordinate defect, or force another already-paid product-preserving exit.

This is strictly narrower than the previous `same-bank shear` debt: finite one- and two-coordinate defect carriers are now removed exactly, with no perturbative step. Arbitrary additional nonseparable spectrum remains a separate bridge beyond exact rank three.

## Immutable sources consumed

- fresh controls/corrections: `yspennstate/math-research-brain`, main, OWNER CONTROL revision `2026-09-22.15`.
- account03/B11 r40 punctured-collar geometry: `yspennstate/math-open-problems@2db0a7f81437b6e67efe800f129abebae0e10b4c`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T191401Z-account03-B11-QFORM-r40/REPORT.md`.
- account03/B11 r41 persistent curvature: brain handoff commit `9a2824966c565fbadaf2e537f6fa20955c404fb6`, canonical math source recorded there.
- account02/B11 fixed-puncture crossing theorem: `yspennstate/math-open-problems@25c25e15fa0f570e7b0b1a2a9fab0811eda07113`; r41 addendum terminal worker-math commit `c6063d311ba25c0f98dbc4add4090b51607062bb`.
- account01/B11 subcritical scalar-planar receiver: `yspennstate/math-open-problems@cedc867395f462e31df64232907480cea07db3d5`.
- account01/B11 arbitrary invertible-core rough-hub discriminant receiver: canonical preceding-run math `yspennstate/math-open-problems@5aa9163cd7259b345e1ec802e27dbadaed68cbba`.

No scheduler/task state, cadence, email, push notification, public release, workflow, paid model/API/Codex call, credential, permission, cross-account authentication, or installation setting was changed.
