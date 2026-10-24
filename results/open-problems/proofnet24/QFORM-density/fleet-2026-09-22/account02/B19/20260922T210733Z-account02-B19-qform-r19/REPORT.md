SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-22T21:07:33.343569Z.
attacking: the heavy exact-null residual-diffuse endpoint — convert the named partner's two independent transverse banks into an exact leakage-span payment and a quantitative rank-three cross-bank certificate off that endpoint.

# account02/B19 r19 — leakage-span boundary theorem for the heavy-null two-bank endpoint

**Run:** `20260922T210733Z-account02-B19-qform-r19`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Universal proof assembly / SYNTHESIS  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The owner target remains the unrestricted product-law statement: independent real coordinates with marginal densities at most one; arbitrary real symmetric `A` with `s_3(A)>=1`; no support, moment, log-concavity, diagonal-basis, or post-rotation-independence assumption.

## 1. Correction boundary and completed inputs

This argument does **not** use law-uniform pointwise Fresnel decay, the false arbitrary-joint coarea inequality, positive conditional projection-density moments, a worst conditional scalar-profile bound, post-rotation independence, a fixed good physical minor, or "bounded conditional density implies independence." It also respects the fresh `QFORM-TRIBANK-CROSS-CORE-LEAKAGE-CLOSURE-FALSE-v1` correction: a nondegenerate three-bank off-diagonal scalar core alone is insufficient under arbitrary within-bank self phases. The rank-three branch below uses the completed exact-cross-bank theorem, whose statement already retains arbitrary self terms; the span endpoint uses the exact null normal form and its nonzero square coefficient rather than an abstract off-diagonal triangle.

The named partner actually applied is **account03/B19 r19**, canonical mathematics

`yspennstate/math-open-problems@63568dad79e5381abb3081ef4685ea126fdd4297`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B19/20260922T203112Z-account03-B19-QFORM/REPORT.md`.

Its theorem `QFORM-DIFFUSE-2D-TWO-BANK-PARTITION-v1` says that for a two-dimensional Parseval frame `v_j` with every `||v_j||^2<=1/2`, there is an **original-coordinate** partition `J,K` such that, for

`S_G=sum_(j in G) v_j v_j^T`, `G=J,K`,

one has

`det(S_J) det(S_K) >= 1/640`,                                      (1.1)

and in particular each `S_G` is positive definite and `det S_G>=1/640`. Thus `J` and `K` are genuinely independent product banks.

The current compatible account02/B10 endpoint, canonical

`yspennstate/math-open-problems@2045e39c5eda8d2a94098d79932223c77f2a4db7`,

combines null-bank compression with the preceding residual-heavy closure. In the near-endpoint hard state it produces one genuine independent cap-one heavy-null coordinate `X_0`, a spectral basis `(r,e,w)`, and

`M = [[0,s,0],[s,d,g],[0,g,f]]`,                                (1.2)

with

`c>=7/9`, `u_0=sqrt(c) r`, `|det M|=s^2 |f|>=1/2`, `f!=0`,       (1.3)

while every remaining transverse row `v_j=(beta_j,gamma_j)` has leverage at most `1/2` and satisfies

`sum_j v_j v_j^T=I_2`.                                          (1.4)

The completed account03/B19 r16 theorem `QFORM-EXACT-CROSS-RANK-L2-v1`, canonical

`yspennstate/math-open-problems@9d55d9ca5a7beaed6f693a57bd32b5fc9949b981`,

will be used in its general rank-three cross-bank form:

`||p_Q||_infinity <= 3 e Pi_3(C)^(-1/3)`                         (1.5)

for an original-coordinate cross block `C` of exact rank three, retaining arbitrary self quadratic terms and outside couplings. Here `Pi_3(C)` is the product of its three nonzero singular values.

Finally, the source-valid two-dimensional product-projection bound used in the account02/B10/account03/B09 chain gives density cap `2` after whitening an orthonormal two-dimensional physical product projection. Consequently the translated transverse packet of bank `G` has joint density at most

`H_G <= 2 det(S_G)^(-1/2) <= 2 sqrt(640)`.                       (1.6)

## 2. Leakage residuals

Write every residual spectral row as

`u_j = alpha_j r + beta_j e + gamma_j w`.                        (2.1)

For `G=J,K`, let `alpha_G,beta_G,gamma_G` be the coefficient vectors restricted to that original-coordinate bank. Define

`q_G = (alpha_G dot beta_G, alpha_G dot gamma_G)^T`,

and define the squared distance of the longitudinal coefficient from the local transverse span by

`rho_G^2 = ||alpha_G||^2 - q_G^T S_G^(-1) q_G`.                  (2.2)

Thus `rho_G=0` exactly when `alpha_G` lies in `span{beta_G,gamma_G}`.

Let `U_G` be the `|G| x 3` row matrix with rows `(alpha_j,beta_j,gamma_j)`. The Gram--Schur identity is

`det(U_G^T U_G) = det(S_G) rho_G^2`.                             (2.3)

If `H_J={0} union K`, let `U_HJ` consist of the heavy row `(sqrt(c),0,0)` and all rows from `K`. Then the same Schur complement gives

`det(U_HJ^T U_HJ) = det(S_K)(c+rho_K^2) >= c det(S_K)`.          (2.4)

The symmetric statement holds with `J,K` interchanged.

## 3. New theorem — exact span or quantitative rank-three cross bank

### Theorem 3.1 — `QFORM-NULLROW-TWOBANK-SPAN-OR-CROSSRANK3-v1`

In the state (1.1)--(1.4), the following hold.

**(a) Nonzero leakage gives an exact physical cross-rank-three certificate.** If `rho_J>0`, then the original-coordinate cross block

`C_J = A[J,{0} union K] = U_J M U_HJ^T`                         (3.1)

has exact rank three and

`Pi_3(C_J)`
` = |det M| sqrt(det(U_J^T U_J) det(U_HJ^T U_HJ))`
` >= |det M| rho_J sqrt(c det(S_J)det(S_K))`
` >= |det M| rho_J sqrt(c/640)`.                               (3.2)

Consequently

`||p_Q||_infinity`
` <= 3e [ |det M| rho_J sqrt(c/640) ]^(-1/3)`.                  (3.3)

The same statement holds with `J,K` swapped. In particular, with

`rho=max(rho_J,rho_K)>0`,

the compressed target state (1.3) satisfies

`||p_Q||_infinity <= 31.452 rho^(-1/3)`.                         (3.4)

Thus every quantitative region `rho>=rho_0>0` is target-level paid.

**(b) The exact local-span endpoint is uniformly paid.** If `rho_J=0` or `rho_K=0`, then

`||p_Q||_infinity < 89.251`.                                    (3.5)

This includes the case `rho_J=rho_K=0`.

### Proof of (a)

For rectangular full-column-rank matrices `L,R` and invertible `3x3` `M`, the three nonzero singular values of `L M R^T` have product

`Pi_3(LMR^T)=|det M| sqrt(det(L^T L)det(R^T R))`.                (3.6)

One proof is to write thin polar/QR factorizations `L=Q_L G_L^(1/2)` and `R=Q_R G_R^(1/2)`; left and right multiplication by the isometries does not change the nonzero singular values, whose product is the absolute determinant of `G_L^(1/2) M G_R^(1/2)`.

If `rho_J>0`, (2.3) and positive definiteness of `S_J` imply that `U_J` has column rank three. Equation (2.4) implies the same for `U_HJ`. Applying (3.6), then (2.3), (2.4), and the partner product bound (1.1), gives (3.2). The exact-cross-rank theorem (1.5) gives (3.3). Under `c>=7/9` and `|det M|>=1/2`, its coefficient is

`3e [sqrt(640/(7/9))/(1/2)]^(1/3)`
` =31.451870276428...`,                                        (3.7)

which is (3.4).

### Proof of (b)

Assume `rho_J=0`; the other case is symmetric. There are real `a,b` with

`alpha_J=a beta_J+b gamma_J`.                                  (3.8)

Condition on every original coordinate in `K`. This preserves independence of `X_0` from the remaining product bank `X_J`. Put

`Y=sum_(j in J) beta_j X_j + y_K`,
`Z=sum_(j in J) gamma_j X_j + z_K`,                            (3.9)

where `y_K,z_K` are now constants. By (1.6), the translated pair `(Y,Z)` has joint density at most `H=2sqrt(640)`. Also

`W=sqrt(c) X_0`                                                 (3.10)

is independent of `(Y,Z)` and has density cap `c^(-1/2)`.

Equation (3.8) expresses the entire `J`-bank longitudinal leakage as `aY+bZ` plus a conditioning-dependent constant. Substitution in the exact null normal form

`Q=2s RY+dY^2+2gYZ+fZ^2`,                                     (3.11)

followed by completing the square in `Z`, gives exactly

`Q=2s W Y + F_K(Y) + f ( Z + theta_K(Y) )^2 + const_K`,         (3.12)

for measurable (indeed affine/quadratic) `F_K,theta_K`. No conditional density surrogate has been introduced: `W` is genuinely independent of the full pair `(Y,Z)` because it uses the separate original coordinate `X_0`.

The completed dependent-pair hyperbolic-square theorem, in its scaled form, therefore gives conditionally on `K`

`||p_(Q|K)||_infinity`
` <= 3*2^(2/3) H^(2/3) c^(-1/3) |s|^(-2/3)|f|^(-1/3)`
` = 3*2^(2/3) H^(2/3) c^(-1/3)|det M|^(-1/3)`.                 (3.13)

The bound is independent of the conditioned values, so averaging preserves it. With `H=2sqrt(640)`, `c>=7/9`, `|det M|>=1/2`, the right side is

`89.250925570717... <89.251`.                                  (3.14)

This proves (3.5). QED.

## 4. What this changes in the conditional proof

The current conditional end-to-end architecture can now be sharpened as follows.

The previously completed ridge/diffuse, physical-pair, nonzero-pivot, exact-cross-rank, zero-self Frobenius, disjoint aggregate-square, and residual-heavy heavy-null branches remain paid in their stated scopes. In the exact-rank-three heavy-null residual-diffuse endpoint, the named partner account03/B19 now supplies two genuine independent transverse banks. The theorem above proves that **the exact leakage-span boundary is not an obstruction at all**, and every state a fixed positive distance from that boundary is paid by an honest rank-three original-coordinate cross bank. The live tri-bank correction does not affect either payment: (3.3) invokes a theorem allowing arbitrary self phases, while (3.12) retains and completes the actual square curvature `fZ^2`.

Therefore the first unpaid exact implication has strictly smaller quantifiers:

`QFORM-NULLROW-TWOBANK-NEARSPAN-UNIFORMITY-v1`.

> There exists a universal finite `C` and a universal `rho_* >0` (or a scale-free substitute with no threshold) such that every compressed heavy-null residual-diffuse state satisfying (1.1)--(1.4) and
>
> `0<rho_J<rho_*`, `0<rho_K<rho_*`
>
> has `||p_Q||_infinity<=C`, uniformly in the input product laws and in the ambient number of original coordinates.

Equivalently, one must bridge the discontinuity between the fixed span payment (3.5) and the reciprocal cross-rank payment (3.4). Coefficient smallness alone may not be treated as small random error because cap-one marginals can have arbitrarily separated/unbounded support. A valid proof has to retain product provenance, for example by a scale-free three-linear-form Brascamp--Lieb/curved trace inequality or by repartitioning so one leakage residual is quantitatively exposed.

This is a genuine narrowing of the partner's `QFORM-NULLROW-TWO-BANK-LEAKAGE-PAYMENT-v1` / account02/B10 `QFORM-NULLROW-TWOBANK-CURVATURE-ABSORPTION-v1`: the exact span case and every quantitatively non-span case are now removed. It does **not** close arbitrary exact rank three, the separate genuinely near-zero nonnull outer-pivot branch, arbitrary additional spectrum, or the full QFORM conjecture.

## 5. Verification

`verify.py` checks on 500 deterministic random rectangular instances the singular-product identity (3.6), on 500 random coefficient banks the Gram--Schur identity (2.3), and the explicit target constants (3.7), (3.14). Its executed output is in `CHECK.txt` and terminates

`QFORM_B19_R19_LEAKAGE_BOUNDARY_CHECK_PASS`.

The numerical checker is regression evidence only; the proof is the exact algebra above.

## 6. Status

`QFORM-NULLROW-TWOBANK-SPAN-OR-CROSSRANK3-v1`: **PROVED SUPPORTING THEOREM / target-level in its stated compressed heavy-null branch**.

`QFORM-NULLROW-TWOBANK-NEARSPAN-UNIFORMITY-v1`: **OPEN**.

Full exact-rank-three QFORM: **OPEN**. Full arbitrary-matrix QFORM: **OPEN**. Continuity is obtained only in the nonzero-leakage cross-rank branch through the source theorem; it is not claimed for the exact-span hyperbolic-square branch or for the full target.
