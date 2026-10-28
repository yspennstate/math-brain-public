SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-22T23:51:00Z.
attacking: an unnormalized sum/difference slice identity for the independent-copy collision integral; use it to close the physical 2-by-2 cross endpoint at the half-Riesz level and test the newest account02/B03 Walsh obstruction.

# account01/B03 r19 — unnormalized slice Plancherel and the physical two-by-two endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.

The full owner target is still open. The theorem below is a dependence-safe supporting result. It does not assume moments, compact support, connected support, log-concavity, identical laws, diagonal-basis independence, or any pointwise one-dimensional quadratic-phase decay. Continuity is stated separately from essential boundedness.

## 1. Sources and corrections actually used

The current brain state says the unrestricted conjecture is open and records the failures of law-uniform pointwise Fresnel decay, conditional density caps for `X+X'` given `X-X'`, arbitrary-joint rank-three coarea, positive conditional projection-density moments, universal single-Schur extraction, and universal local triple / cross-rank-three extraction. None of those refuted statements is used here.

The designated partner is **account02/B03**, run `20260922T231550Z-account02-B03-QFORM-r13`, canonical mathematics

`yspennstate/math-open-problems@e9edee72f4272f7bc84c7a914f3a087f614f9c60`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T231550Z-account02-B03-QFORM-r13/REPORT.md`.

I apply two completed pieces from that report below: its overlap-one `k=3` transducer, and its exact Walsh-projection target family `A_t=tI_8+(1-t)P` with the formula for the collapsing fourth-order overlap-one bank. This is an actual quantitative application, not a citation-only dependency.

For comparison, account01/B03 r10 proved a leverage-free rectangular-cross theorem using projected two-copy packets and the LPP marginal-density theorem. At rank two it gave

`H_{1/2}(R) <= 8 Delta_2(B)^(-1/4)`.

The present proof changes mechanism: it never projects the one-copy law. It keeps each dependent sum/difference pair as one **unnormalized two-dimensional slice**, obtains an exact global `L^2` norm for that slice, and then performs only a physical-coordinate change of variables. At a physical `2 x 2` cross minor it improves the constant `8` to `4 sqrt(2)`.

## 2. Exact unnormalized sum/difference slice

Let `X` have density `f` with `0<=f<=1`, let `X'` be an independent copy, and put

`U=X-X'`, `V=X+X'`.

The joint density of `(U,V)` is

`F(u,v)=(1/2) f((v+u)/2) f((v-u)/2)`.                         (2.1)

This is the point at which the known conditional-cap trap must be avoided. The normalized conditional law of `V` given `U=u` can have arbitrarily large density. We never normalize (2.1). Instead define the unnormalized slice transform

`K(u,s) = | int_R exp(i s v) F(u,v) dv |`.                     (2.2)

Because `0<=F<=1/2` and `int int F=1`,

`int int F(u,v)^2 du dv <= 1/2`.                               (2.3)

Plancherel in `v` therefore gives the exact law-uniform estimate

`boxed:  ||K||_{L^2(R^2)}^2 <= pi.`                            (2.4)

No density statement for `V|U` occurs anywhere. The dependence between sum and difference is retained in the same function `F(u,v)` until after the Fourier transform.

## 3. Collision identity for a physical quadratic block

Let `W=(W_1,...,W_N)` have independent cap-one coordinates and let

`R(W)=W^T B W + ell^T W + c`,                                  (3.1)

where `B` is real symmetric and `ell,c` are arbitrary. For an independent copy `W'`, define componentwise

`u=W-W'`, `v=W+W'`.

Symmetry of `B` gives the exact identity

`R(W)-R(W') = u^T B v + ell^T u`.                              (3.2)

If `F_j,K_j` are the slice objects (2.1)-(2.2) for coordinate `j`, then Fubini in the `v_j` variables gives

`|phi_R(t)|^2`
` = | int exp(i t ell.u) prod_j [int exp(i t (Bu)_j v_j) F_j(u_j,v_j) dv_j] du |`
` <= int prod_j K_j(u_j,t(Bu)_j) du.`                          (3.3)

Equation (3.3) is the basic dependence-safe decoupled-time identity of this run.

## 4. Main theorem: square physical cross block

### Theorem `QFORM-UNNORMALIZED-SLICE-CROSS-v1`

Condition on every original coordinate outside two disjoint physical banks

`I={1,...,m}`, `J={m+1,...,2m}`,

and let `C=B[I,J]` be the resulting physical `m x m` cross block. Assume `det C !=0`. Same-side quadratic terms and all affine terms are arbitrary. Then

`boxed:
 |phi_R(t)|^2 <= min(1, pi^m |t|^(-m) |det C|^(-1)),
}`                                                              (4.1)

hence

`boxed:
 |phi_R(t)| <= min(1, pi^(m/2) |t|^(-m/2) |det C|^(-1/2)).
}`                                                              (4.2)

#### Proof

Write

`L_j^t(u)=(u_j,t(Bu)_j) in R^2`.                               (4.3)

Split the integrand in (3.3) into the first and second physical banks and use Cauchy--Schwarz:

`I_t := int prod_{j=1}^{2m} K_j(L_j^t u) du`
` <= [int prod_{j in I} K_j(L_j^t u)^2 du]^(1/2)`
`    [int prod_{j in J} K_j(L_j^t u)^2 du]^(1/2).`              (4.4)

The combined map

`T_I^t:u -> (L_j^t(u))_{j in I}`                               (4.5)

is a linear map from `R^(2m)` to `R^(2m)`. After permuting output rows, its matrix has the block form

`[ I_m   0 ]`
`[  *   t C ]`,                                                (4.6)

so

`|det T_I^t|=|t|^m |det C|`.                                   (4.7)

Likewise the `J`-bank map has determinant `|t|^m |det C^T|`. Therefore the two changes of variables in (4.4), followed by (2.4), give

`int prod_{j in I} K_j(L_j^t u)^2 du`
` <= |t|^(-m)|det C|^(-1) pi^m`,                              (4.8)

and the identical bound for `J`. Inserting these into (4.4) proves

`|phi_R(t)|^2 <= pi^m |t|^(-m)|det C|^(-1)`.                   (4.9)

Together with `|phi_R(t)|<=1`, this is (4.1)-(4.2). QED.

This proof is entirely in physical coordinates. The arbitrary same-bank quadratic terms are already contained in the rows `(Bu)_j`; no rotation of the input product law is made.

## 5. Exact fractional-time integral

Put

`T=pi |det C|^(-1/m)`.                                         (5.1)

For `0<alpha<m/2`, (4.2) gives

`int_R |t|^(alpha-1)|phi_R(t)| dt`
` <= 2 T^alpha [ 1/alpha + 1/(m/2-alpha) ].`                   (5.2)

The classical Riesz identity

`|x|^(-alpha)`
` = [2 Gamma(alpha) cos(pi alpha/2)]^(-1)`
`   int_R exp(i t x)|t|^(alpha-1) dt`                          (5.3)

(with standard Gaussian regularization if desired) therefore yields

`boxed:
 H_alpha(R):=sup_z E|z-R|^(-alpha)
 <= [ T^alpha /(Gamma(alpha) cos(pi alpha/2)) ]
    [1/alpha + 1/(m/2-alpha)].
}`                                                              (5.4)

This is the requested integrated estimate. It comes from the exact independent-copy identity while retaining the full dependence inside every `(X_j-X_j',X_j+X_j')` pair.

For `m>=3`, taking the unweighted Fourier integral in (4.2) also recovers the sharp physical-cross density constant

`||p_R||_infinity <= [m/(m-2)] |det C|^(-1/m),`                 (5.5)

and this branch has a bounded continuous density because `phi_R in L^1`.

For `m=2`, the direct density integral is exactly critical, but the half-Riesz integral closes. Setting `alpha=1/2` in (5.4) gives

`boxed:
 H_{1/2}(R) <= 4 sqrt(2) |det C|^(-1/4).
}`                                                              (5.6)

This improves the earlier account01/B03 physical rank-two constant `8` to `4 sqrt(2)` and removes the LPP projection theorem from this physical-square endpoint.

The same envelope also gives an `L^2` density for `R`:

`int_R |phi_R(t)|^2 dt <= 4 pi |det C|^(-1/2),`

hence

`boxed: ||p_R||_2^2 <= 2 |det C|^(-1/2).}`                      (5.7)

Consequently, for an independent copy `R'`,

`P(|R-R'|<=epsilon) <= 4 epsilon |det C|^(-1/2).`              (5.8)

Equations (5.6)-(5.8) are genuine decoupled-time/collision estimates, not Monte Carlo statements.

## 6. Linear small-ball scaling after one genuine physical square

Let `Z` be an original coordinate, independent of the remaining original coordinates, and suppose after conditioning only on outside original coordinates and completing the `Z` square one has

`Q=d(Z+h(W))^2+R(W)`, `d!=0`.                                  (6.1)

Assume four residual physical coordinates split into two pairs whose `2 x 2` cross block `C` in the Schur residual is invertible. Conditioning all other residual original coordinates changes only affine terms in this four-coordinate form, so (5.6) applies uniformly.

For fixed `W`, the cap-one density of `Z` gives

`p_{d(Z+h)^2}(y) <= |d|^(-1/2)|y|^(-1/2)`.                     (6.2)

Therefore

`p_Q(x) <= |d|^(-1/2) E|x-R|^(-1/2)`,                         (6.3)

and (5.6) yields

`boxed:
 ||p_Q||_infinity <= 4 sqrt(2) |d|^(-1/2)|det C|^(-1/4).
}`                                                              (6.4)

Equivalently every interval `L` obeys the exact linear scaling

`P(Q in L) <= 4 sqrt(2)|d|^(-1/2)|det C|^(-1/4)|L|.`           (6.5)

This branch proves absolute continuity and essential boundedness. It does **not** prove continuity.

### Original-matrix overlap-one form

Let the pivot index be `i`, and let `I,J` be disjoint two-element sets not containing `i`. The block determinant identity gives

`det A[{i} union I,{i} union J] = d det S[I,J]`,                (6.6)

where `S` is the physical Schur complement. Thus (6.4) can be written directly in terms of a third-order overlap-one original minor `D_{i;I,J}`:

`boxed:
 ||p_Q||_infinity
 <=4 sqrt(2) |A_ii|^(-1/4)
   |det A[{i} union I,{i} union J]|^(-1/4).
}`                                                              (6.7)

This is homogeneous of degree `-1` in `A`. It aligns the half-Riesz payment with the **natural third compound** of `A`, rather than the fourth-order overlap-one minors required by the partner's `k=3` residual-bank theorem.

## 7. Designated partner account02/B03 applied: the Walsh obstruction is uniformly paid here

The partner r13 report constructs

`A_t=t I_8+(1-t)P`, `0<t<=1/2`,                                (7.1)

where `P=RR^T` and `R` consists of the first three normalized columns of the Sylvester `8 x 8` Walsh matrix. It proves

`spectrum(A_t)={1,1,1,t,t,t,t,t}`,                             (7.2)

and every diagonal pivot equals

`d_t=(3+5t)/8`.                                                 (7.3)

It also proves its new fourth-order overlap-one bank collapses:

`M_{i,3}(A_t)=7 t^2(1-t)^6/128`,                               (7.4)

so the partner transducer gives the actual inequality

`||p_Q||_infinity`
` <=13.9167889868 d_t^(-1/3)`
`   [7 t^2(1-t)^6/128]^(-1/12),`                               (7.5)

which diverges like `t^(-1/6)` as `t downarrow0`. This is exactly the completed partner result applied to an inequality.

Now apply the new theorem to the **same** target family. Use one-based physical coordinates, pivot coordinate `1`, residual left pair

`I={2,3}`

and residual right pair

`J={4,6}`.

Exact symbolic Schur computation gives

`det S_t[I,J]`
` = -(1-t)^2(1+t) / [4(5t+3)].`                                (7.6)

Therefore

`Delta_t:=|det S_t[I,J]|`
` =(1-t)^2(1+t)/[4(5t+3)] >0`.                                 (7.7)

Insert (7.3),(7.7) into (6.4):

`||p_{X^T A_t X}||_infinity`
` <=4 sqrt(2) d_t^(-1/2) Delta_t^(-1/4).`                      (7.8)

On `0<t<=1/2`, the right side has its maximum at an endpoint; its value at `t=1/2` is larger and equals

`boxed:
 ||p_{X^T A_t X}||_infinity
 <= 32 sqrt(2) / 33^(1/4)
 <18.882.
}`                                                              (7.9)

Thus the partner's exact pivot-`E_3` obstruction is **not** an obstruction to the lower-order physical-pair endpoint. The same family for which every fourth-order overlap-one bank collapses has a third-order overlap-one minor that stays at universal scale. This is useful structural information for the remaining compiler.

Indeed (6.6) and (7.6) simplify to

`|det A_t[{1,2,3},{1,4,6}]|=(1-t)^2(1+t)/32`,                  (7.10)

which stays at least `3/256` on `0<t<=1/2`. The small parameter `t` cancels before any reciprocal payment.

## 8. Third-compound alignment and the remaining structural problem

The spectral hypothesis `s_3(A)>=1` implies the exact Cauchy--Binet identity

`sum_{|R|=|C|=3} det A[R,C]^2 = e_3(A^2) >=1`.                 (8.1)

Partition this mass by the intersection size

`q=|R cap C| in {0,1,2,3}`.                                    (8.2)

The new transducer (6.7) is exactly the local analytic payment for the `q=1` atoms of this **third-order** mass. The `q=0` atoms are disjoint physical `3 x 3` cross minors, for which the physical cross theorem (5.5) gives a bounded continuous density. The `q=2` and `q=3` atoms correspond respectively to two-pivot / one-transverse-coordinate geometry and physical principal triples, for which other fleet branches exist in stated quantitative regimes.

What is still missing is not a new local oscillatory estimate. It is an **aggregate-before-inversion theorem**: one must convert a dimension-free share of the total third-compound mass (8.1), in whichever overlap class carries it, into a paid product-preserving branch without selecting one determinant atom and losing dimension. The partner r13 counterexample shows that moving up to the fourth-order overlap-one bank does not solve this by itself. The present theorem puts the decoupled-time endpoint at the same third-compound order as the spectral hypothesis.

## 9. A failed three-coordinate shortcut, recorded to avoid repetition

One might try to apply (2.4) directly to three physical coordinates using the three maps

`L_i(u)=(u_i,(Bu)_i)`, `i=1,2,3`,                              (9.1)

and a symmetric Brascamp--Lieb `L^2` argument. This simple closure is structurally singular for every symmetric `3 x 3` matrix. The one-dimensional kernels are generated by

`k_1=(0,-b_13,b_12)`,
`k_2=(b_23,0,-b_12)`,
`k_3=(-b_23,b_13,0)`,                                          (9.2)

and satisfy the exact identity

`k_1+k_2+k_3=0`.                                                (9.3)

Hence all three kernels lie in one two-dimensional subspace; the equal-weight `L^2` BL dimension condition fails there. This refutes only this naive three-map closure, not the QFORM conjecture or other three-coordinate arguments. The successful four-coordinate proof works because each two-map bank becomes a square invertible map controlled by a physical `2 x 2` cross determinant.

## 10. Status

**New proved supporting theorem:** `QFORM-UNNORMALIZED-SLICE-CROSS-v1`, including the exact fractional-time estimate (5.4), physical `2 x 2` half-Riesz constant `4sqrt(2)`, `L^2` collision estimate (5.8), and linear-small-ball transducer (6.4)/(6.7).

**Partner application:** account02/B03 r13's exact Walsh target family and overlap-one `k=3` bound were applied quantitatively; the new third-order endpoint gives the uniform target-family bound `<18.882` while the partner fourth-order bank bound diverges.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.

**Continuity:** proved in the direct `m>=3` physical-cross branch by `L^1` Fourier inversion; not proved by the `m=2` plus outer-square branch.

**Next B03 implication:** build an aggregate compiler for the `q=1` third-compound mass, or show that failure of such a compiler quantitatively transfers mass into one of the already-paid `q=0,2,3`, diffuse-Fresnel, grouped-bank, or ridge branches. Do not return to a single-good-minor selection.
