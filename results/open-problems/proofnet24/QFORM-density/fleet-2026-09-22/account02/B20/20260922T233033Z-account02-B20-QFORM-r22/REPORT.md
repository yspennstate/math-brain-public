# account02/B20 QFORM r22 — physical deshearing of the O0 double-anchor packet

Run: `20260922T233033Z-account02-B20-QFORM-r22`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: proof closure and keeper / SYNTHESIS  
Classification: **ESSENTIAL_STEP_APPLIED / O0-PHYSICAL-DESHEARING / D5-HIGH-VOLUME-BRANCH-PAID / FULL_TARGET_OPEN**  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and correction discipline

The target remains: for every finite `n`, every independent real `X_i` with probability densities `0<=f_i<=1`, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove that `Q=X^TAX` has a density with one universal finite essential-supremum bound, or give a valid counterexample. Continuity is separate.

No moments, Gaussianity, log-concavity, compact/connected support, identical laws, diagonal-basis assumption, or post-rotation independence is used below. In particular this report does not use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, worst fiber supremum, positive conditional projection-density moment/supremum, or a direct spectral-to-single-minor selection claim.

Fresh brain control used OWNER CONTROL revision `2026-09-22.15`. The newest owner continuation `QFORM-CLAUDE-LATEST-20260922T225732Z` requires equation-level use of a completed result from `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, directory `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`. The result actually used below is the proved fifth-volume theorem D5 from `FOURIER_ROUTE_REPORT.md`:

`||p_Q||_infinity <= 5 sqrt(2e) E_5(M)^(-1/10)`                            (1.1)

for every actual physical cross block `M=A[I,J]`, with no volume-marginal restriction; arbitrary same-side blocks, outside coordinates/couplings and affine terms are retained.

## 2. Newest designated partner result actually consumed

The newest completed account03/B20 result available at the source refresh is run `20260922T224748Z-account03-B20-QFORM-r19`, canonical mathematics

`yspennstate/math-open-problems@21c78fcc8e4bd9f5c7a872ae3c034b03ca0f88bf`,

report

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260922T224748Z-account03-B20-QFORM-r19/REPORT.md`.

Inside the current O0 third-compound branch, account01/B20 r21 plus account03/B20 r19 give an actual physical cross block, after physical row/column permutations,

`B = [[b, r^T], [c, D]]`,                                               (2.1)

with a row anchor `i`, column anchor `a`, and anchored third-minor mass

`Z_ia := sum_{|J|=|K|=2} det B[{i} union J,{a} union K]^2 > 1/768`.       (2.2)

The partner then introduced the rectangular Schur bank `S=D-cr^T/b` when `b!=0`, obtaining `b^2 E_2(S)>1/768`. That identity is correct but `S` is not a new independent source bank. The purpose of the present run is to eliminate `S` from the first unpaid interface entirely.

For any real matrix `M`, write

`E_k(M)=sum_{|I|=|J|=k} det(M[I,J])^2`.

## 3. New theorem: exact physical deshearing inequality

### Theorem `QFORM-O0-PHYSICAL-DESHEARING-v1`

Let `B` be any real rectangular matrix written as in (2.1). Define the anchored third-minor matrix `T`, indexed by residual row pairs `J={j,k}` and residual column pairs `K={p,q}`, by

`T_{J,K}=det B[{i} union J,{a} union K]`.                              (3.1)

Then

`boxed( sqrt(Z_ia) <= |b| sqrt(E_2(D)) + ||c||_2 ||r||_2 ||D||_F. )`  (3.2)

Consequently, if (2.2) holds, then at least one of the two *physical-coordinate* alternatives holds:

`boxed( |b| sqrt(E_2(D)) > 1/(32 sqrt(3)) )`                           (3.3)

or

`boxed( ||c||_2 ||r||_2 ||D||_F > 1/(32 sqrt(3)). )`                  (3.4)

No Schur-complement variable, shear, or rotated source occurs in (3.2)-(3.4).

### Proof

Let `V` be the residual column space and `W` the residual row space, with their coordinate Euclidean structures. Regard `D:V->W`. Let

`C_2(D): Lambda^2 V -> Lambda^2 W`

be its second compound. Let `iota_r:Lambda^2 V->V` be contraction by the physical vector `r`, and let

`L_c:W->Lambda^2 W`, `L_c(w)=c wedge w`.

For basis pairs `J={j,k}`, `K={p,q}`, expansion of the physical `3x3` determinant gives

`T_{jk,pq}`
` = b(D_jp D_kq-D_jq D_kp)`
`   - r_p(c_jD_kq-c_kD_jq)`
`   + r_q(c_jD_kp-c_kD_jp)`.                                         (3.5)

With the standard contraction sign convention this is exactly

`T = b C_2(D) - L_c D iota_r`.                                       (3.6)

The Hilbert--Schmidt norm of the second compound is

`||C_2(D)||_HS = sqrt(E_2(D))`.                                      (3.7)

Moreover

`||L_c||_op=||c||_2`, `||iota_r||_op=||r||_2`,                       (3.8)

so the Hilbert--Schmidt ideal inequality gives

`||L_c D iota_r||_HS <= ||c||_2 ||D||_F ||r||_2`.                    (3.9)

Taking the Hilbert--Schmidt norm in (3.6), using the triangle inequality, and observing `||T||_HS^2=Z_ia`, proves (3.2).

By (2.2),

`sqrt(Z_ia)>1/sqrt(768)=1/(16 sqrt(3))`.                              (3.10)

If both terms on the right side of (3.2) were at most `1/(32 sqrt(3))`, their sum would be at most `1/(16 sqrt(3))`, contradicting (3.10). Hence (3.3) or (3.4). QED.

### Checks at the two endpoints

If `b=0`, (3.2) reduces exactly to the partner's zero-anchor estimate

`Z_ia <= ||c||_2^2 ||r||_2^2 ||D||_F^2`.

If `c=0` or `r=0`, it becomes

`Z_ia = b^2 E_2(D)`,

as it should. Thus (3.2) continuously interpolates the partner's two separate anchor cases without ever declaring the Schur bank `S` to be probabilistically realizable.

## 4. A source-realizable three-way packet

Apply the threshold `|b|=1/8` to (3.3). Every state satisfying (2.2) therefore obeys at least one of:

1. **heavy physical anchor edge**

   `boxed( |b|>1/8; )`                                               (4.1)

2. **residual physical second-compound packet**

   `boxed( E_2(D)>1/48; )`                                           (4.2)

3. **two-star times residual-bank packet**

   `boxed( ||c||_2 ||r||_2 ||D||_F>1/(32 sqrt(3)). )`                 (4.3)

Indeed, if (3.3) holds and `|b|<=1/8`, then

`sqrt(E_2(D)) > 8/(32 sqrt(3)) = 1/(4 sqrt(3))`,

which is (4.2). Alternative (3.4) is (4.3).

All quantities in (4.1)-(4.3) are coefficients or aggregate norms of actual original-coordinate banks of `A`; no source transformation is involved.

## 5. Exact application of the newest Claude D5 theorem

The block `D` in (2.1) is itself the actual physical cross block

`D=A[L\{i},R\{a}]`.                                                  (5.1)

Therefore theorem D5, equation (1.1), applies directly to the *full ambient quadratic form* whenever `E_5(D)>0`.

Choose the fixed threshold

`E_5(D) >= 1/1024`.                                                   (5.2)

Then (1.1) gives

`||p_Q||_infinity`
` <= 5 sqrt(2e) (1/1024)^(-1/10)`
` = 10 sqrt(2e)`
` < 23.317`.                                                         (5.3)

This is a complete payment of that branch, not merely a structural certificate. It retains arbitrary `A[L,L]`, `A[R,R]`, outside coordinates and couplings, and affine terms exactly as in theorem D5.

Combining (4.1)-(4.3) with (5.3), every still-unpaid O0 double-anchor state is forced into one of the following *physical* packets:

`H:` `|b|>1/8`;                                                      (5.4)

`P:` `||c||_2 ||r||_2 ||D||_F>1/(32 sqrt(3))`;                      (5.5)

`R:` `E_2(D)>1/48` **and** `E_5(D)<1/1024`.                          (5.6)

The previous Schur-shear branch `b^2E_2(S)>1/768` is therefore not the first probabilistic interface anymore: it can be replaced, before any probabilistic use, by (5.4)-(5.6), plus the D5-paid branch (5.3).

## 6. Relation to the full target

The strongest current conditional proof graph is:

- already-paid classes remain paid under their exact source scopes;
- the O0 third-compound survivor has `E_3(B)>=1/256`;
- fractional volume-sampling pays O0 if either third-volume orientation is sufficiently diffuse;
- otherwise the newest account03/B20 result supplies anchors with (2.2);
- the present theorem removes the Schur-coordinate interface and reduces that anchored survivor to the physical packets (5.4)-(5.6), with high fifth exterior volume in `D` already paid by (5.3).

This does **not** assert that the upstream structural exhaustion into O0/other paid classes has itself been fully closed. It also does not pay (5.4)-(5.6) in complete generality. Thus the full conjecture remains open.

### First unpaid universal implication after this run

`QFORM-O0-PHYSICAL-PACKET-PAYMENT-v1`:

Under the original product-source hypotheses and arbitrary same-side/outside couplings, prove one universal linear small-ball/density bound for each still-unpaid physical packet (5.4)-(5.6), or source-preservingly reduce it to an already-paid physical-pair, physical-triple, ridge/grouped-square, mixed-hub, or volume-sampling class.

A useful next split is now source-valid and low-dimensional in exterior degree: the residual-bank alternative has substantial `E_2` but sub-threshold `E_5`. One may next apply the newest D' theorem to any substantial `E_3(D)` diffuse subbranch; if its third-volume marginals concentrate, recurse on actual physical anchors of `D`, not on sheared coordinates. If `E_3(D)` is small, the obstruction is genuinely rank-two/four-volume dominated and should be attacked by the pair-log/fractional-potential machinery. The heavy-edge packet (5.4) must not be called a uniformly conditioned physical pair without controlling its two diagonal entries; that shortcut is false in general.

## 7. Status

Classification: `ESSENTIAL_STEP_APPLIED / O0-PHYSICAL-DESHEARING / D5-HIGH-VOLUME-BRANCH-PAID / FULL_TARGET_OPEN`.

No new full-target continuity statement is made. The D5-paid subbranch has the continuity supplied by its integrable characteristic-function proof; the structural alternatives alone do not.
