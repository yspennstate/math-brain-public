# MOC4 B09 report — residual zero-face Haar lift and quaternion Hessian payment

Run: `20260922T034112Z-fleet02-B09-MOC4-r14`  
Account/slot: `fleet02/B09`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: **ESSENTIAL_STEP_APPLIED**. Parent MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## Scope and source state

Target: for complex normal `4 x 4` pairs, with spectra `a=(a_0,...,a_3)` and `b=(b_0,...,b_3)`, prove

`det(A+B) in conv { prod_i (a_i+b_{sigma(i)}) : sigma in S_4 }`.

As usual diagonalize one normal matrix and write

`D(U)=det(diag(a)+U diag(b) U*)`.

No invertibility, spectral simplicity, or nonzero determinant is assumed below.

Latest complete campaign-lead result actually consumed: fleet03/B07 run `20260922T013930Z-fleet03-B07-MOC4-r11`, shared handoff commit `8a1d8847356dde8c819cbff6fdb294b5b7960b0b`, outcome `CANDIDATE_REFUTED` for the fixed-zero-entry common-permutation-lift shortcut. Its surviving boundary obligation is `MOC4-ZERO-FACE-SUPPORT-v1`.

Named OTHER-account results actually applied:

1. fleet01/B07 `MOC4-CARTAN-HESSIAN-PACKING-v1`, shared handoff commit `dabcb6098e8abcb960ebf4700ae1354d5e3e97a`: the all-zero-endpoints-safe strict interior branch pays a quantitative Hessian trace.
2. fleet03/B08 `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1`, shared handoff commit `afb708e6900d6eb53f12e96226add63f2d16654f`: a genuine `SU(2)` one-cycle slice has an exact ellipse/payment condition. The quadratic-fiber theorem below identifies the higher-dimensional object of which such 2-dimensional slices are sections.
3. fleet04/B08 `MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1`, shared handoff commit `f6de93d3fe3b7a1af69b55e3b45f446f5b2e8770`: support-face gaps strengthen pair curvature payments and motivate keeping the endpoint-support deficit explicit below.

## 1. Exterior-power determinant formula

For subsets `I,J` of `{0,1,2,3}` with `|I|=|J|=k`, write

`a_{I^c}=prod_{i notin I} a_i`, `b_J=prod_{j in J} b_j`.

Cauchy-Binet on exterior powers gives the polynomial identity

`D(U) = sum_{k=0}^4 sum_{|I|=|J|=k} a_{I^c} b_J |det U[I,J]|^2`.        (1)

For a permutation matrix the squared compound minor is the indicator that the permutation sends `J` to `I`; inserting this in (1) gives one of the 24 target vertices (up to inversion of the permutation, which leaves the target set unchanged).

## 2. Exact residual parameterization of a zero face

Relabel rows/columns so a zero-entry unitary satisfies `u_00=0`, and partition

`U = [[0, r*], [c, V]]`,

where `r,c in C^3` are unit vectors. Unitarity is equivalent to

`V r=0`, `V* c=0`, `V*V=I-r r*`, `VV*=I-c c*`.

Choose any isometries `X,Y : C^2 -> C^3` with

`XX*=I-r r*`, `YY*=I-c c*`.

Then every unitary with the same first row and first column is uniquely represented, modulo the harmless choice of complement bases, as

`U(W) = [[0, r*], [c, Y W X*]]`,      `W in U(2)`.                     (2)

Conversely every `W in U(2)` gives a genuine unitary. This is a true-unitary fiber, not a bistochastic relaxation.

Put

`R_j=|r_j|^2`, `C_i=|c_i|^2`,  `i,j in {1,2,3}`.

Thus `sum R_j=sum C_i=1`.

## 3. New theorem: exact Haar common lift after averaging the residual fiber

### Theorem `MOC4-ZERO-FIBER-HAAR-LIFT-v1`

Let `W` be Haar-uniform in `U(2)` in (2). Define a probability law `mu_{r,c}` on permutations of `{0,1,2,3}` as follows.

- Choose `i in {1,2,3}` with probability `C_i`.
- Choose `j in {1,2,3}` independently with probability `R_j`.
- Set `pi(0)=i` and `pi(j)=0`.
- Between the two remaining nonzero columns and two remaining nonzero rows, choose either bijection with probability `1/2`.

Equivalently, every permutation with `pi(0)=i !=0` and `pi^{-1}(0)=j !=0` receives weight

`mu_{r,c}(pi)=C_i R_j/2`,                                                (3)

and the other six permutations receive weight zero.

Then, simultaneously for every pair of equal-cardinality subsets `I,J`,

`E_W |det U(W)[I,J]|^2 = P_{pi~mu_{r,c}}( pi(J)=I )`.                    (4)

Consequently

`E_W D(U(W)) = sum_pi mu_{r,c}(pi) v_pi`,                               (5)

where `v_pi` are the 24 MOC4 target vertices. In particular the entire residual-fiber Haar barycenter belongs to the target convex hull.

This is an **averaged** common lift only. It does not contradict fleet03/B07's exact counterexample to a common lift for an individual zero-entry unitary.

### Proof of (4)

The cases `k=0,4` are immediate.

For `k=1`, set `x_j=X* e_j`, `y_i=Y* e_i`. Then

`||x_j||^2=1-R_j`, `||y_i||^2=1-C_i`,

and

`(Y W X*)_{ij}=y_i* W x_j`.

The `U(2)` Haar identity

`E |y* W x|^2 = ||x||^2 ||y||^2 /2`                                    (6)

gives

- `E|u_00|^2=0`;
- `E|u_0j|^2=R_j`;
- `E|u_i0|^2=C_i`;
- `E|u_ij|^2=(1-C_i)(1-R_j)/2` for `i,j>0`.

The law (3) has exactly these one-point marginals: for `i,j>0`, to have `pi(j)=i` one must choose the distinguished incoming/outgoing indices away from `i,j`, and then one of the two residual bijections succeeds.

For `k=2` there are four incidence patterns.

**(a) `0 in I` and `0 in J`.** Write `I={0,i}`, `J={0,j}`. Then

`det U[I,J] = -conj(r_j)c_i`,

so its squared modulus is `C_i R_j`. Under (3), `pi(J)=I` forces exactly `pi(0)=i` and `pi(j)=0`, again with probability `C_iR_j`.

**(b) `0 notin I` and `0 notin J`.** If `I^c={0,i}`, `J^c={0,j}`, complementary-minor duality for a unitary gives

`|det U[I,J]|^2=|det U[I^c,J^c]|^2=C_iR_j`.

For a permutation, `pi(J)=I` is equivalent to `pi(J^c)=I^c`, so the same probability is obtained.

**(c) `0 in I` and `0 notin J`.** Write `I={0,i}`, `J={j,k}` and let `ell` be the third nonzero column. The minor is

`conj(r_j)(Y W X*)_{ik} - conj(r_k)(Y W X*)_{ij}`

`= y_i* W X*(conj(r_j)e_k-conj(r_k)e_j)`.

The vector in parentheses lies in `r^perp` and has squared norm `R_j+R_k=1-R_ell`. By (6),

`E |det U[I,J]|^2 = (1-C_i)(R_j+R_k)/2`.                                (7)

Under (3), `pi(J)=I` requires the distinguished column sent to zero to lie in `J`, the distinguished image of column zero to lie outside `I`, and then one of the two residual bijections; its probability is exactly the right side of (7).

**(d) `0 notin I` and `0 in J`.** This is the transpose-symmetric calculation and yields the matching law probability

`(C_i+C_k)(1-R_j)/2`

when `I={i,k}` and `J={0,j}`.

Thus (4) holds for `k=2`. For `k=3`, complementary-minor duality reduces to `k=1`, and the permutation event is likewise complemented. This proves (4) for every exterior degree, and (5) follows by substituting (4) into (1). No inverse spectral quantity appears anywhere, so singular and repeated-spectrum cases are included.

## 4. Quaternion polarization of the entire zero-face fiber

The global phase of `W` in (2) multiplies every varying minor homogeneously and disappears after taking squared moduli. Hence the determinant depends only on `PU(2)`. Choose an `SU(2)` representative

`W(q)=[[q0+i q3, q2+i q1],[-q2+i q1,q0-i q3]]`,

with `q=(q0,q1,q2,q3) in S^3`.

Every varying `1 x 1` minor and every mixed `2 x 2` minor is a complex linear form in `q`; lower-right `2 x 2` minors have modulus independent of `q`; `3 x 3` minors reduce to `1 x 1` minors by complementary-minor duality. Therefore, for every fixed real support direction `L(z)=Re(eta z)`, there is a real symmetric `4 x 4` matrix `H_eta` such that

`h_eta(q):=L(D(U(W(q)))) = q^T H_eta q`,       `q in S^3`.               (8)

The residual zero-face support problem is therefore an exact Rayleigh-quotient problem, not merely a local Taylor approximation.

Since Haar measure on `SU(2)` is uniform measure on `S^3`, (5) implies

`tr(H_eta)/4 = E_q h_eta(q) = sum_pi mu_{r,c}(pi) H_pi <= M_eta`,          (9)

where `H_pi=L(v_pi)` and `M_eta=max_pi H_pi`.

## 5. Exact boundary Hessian payment

Suppose a zero-entry true unitary is a support maximizer on its residual fiber and violates the target support by

`gamma = lambda_1(H_eta)-M_eta >0`.

Let the eigenvalues of `H_eta` be `lambda_1>=lambda_2>=lambda_3>=lambda_4`. From (9),

`sum_{m=2}^4 (lambda_1-lambda_m)
 = 4 lambda_1-tr(H_eta)
 = 4[gamma + M_eta-tr(H_eta)/4]
 >= 4 gamma`.                                                           (10)

For the quadratic function (8), the spherical Hessian at a top eigenvector has tangent eigenvalues

`2(lambda_m-lambda_1)`, `m=2,3,4`.

Therefore every hypothetical zero-face support violation pays the exact curvature identity

`-Tr Hess_{S^3} h_eta
 = 8[gamma + Delta_mu] >= 8 gamma`,                                      (11)

where

`Delta_mu := M_eta-sum_pi mu_{r,c}(pi) H_pi >=0`.                        (12)

In particular, a residual fiber that is flat cannot violate MOC4; and at least one orthogonal residual-fiber eigen-direction has support drop at least `4 gamma/3`.

If the target support maximum is unique and its gap to the second endpoint is `delta>0`, then every atom of (3) has mass at most `1/2`. Thus

`Delta_mu >= delta/2`,                                                   (13)

whether or not the maximizing permutation occurs in the support of `mu`. Consequently

`-Tr Hess_{S^3} h_eta >= 8 gamma + 4 delta`.                             (14)

This is a boundary analogue of the strict-interior Hessian payments from fleet01/B07 and fleet04/B08, but it is obtained from an exact positive permutation lift of the **fiber average**, not from an invalid fixed-unitary lift.

## 6. Relation to the OTHER-account one-cycle ellipse

Equation (8) shows that every great-circle section of the residual zero-face fiber is an exact quadratic trigonometric curve. In a two-dimensional plane spanned by unit quaternions `p,q`, the support restriction is governed by the `2 x 2` compression of `H_eta`. Thus the geometric-mean payment test in fleet03/B08 `MOC4-ONE-CYCLE-SU2-ELLIPSE-v1` is the two-dimensional positive-semidefinite test for a particular structured slice of this `4 x 4` Rayleigh problem.

The new point is that the lead's zero-face branch is intrinsically four-real-dimensional after fixing the first row and column, while the Haar lift supplies a global trace/curvature payment across all three tangent directions at once.

## 7. Compact conditional end-to-end route

Assume a support-direction counterexample exists and choose a global true-unitary maximizer.

1. If a proper common reducing block/repeated-spectrum boundary occurs, use the existing lower-dimensional boundary reductions.
2. If the maximizer has a zero entry, relabel it to `(0,0)` and apply `MOC4-ZERO-FIBER-HAAR-LIFT-v1`. The residual fiber has safe target barycenter and any positive gap must satisfy (11), strengthened to (14) under a unique target endpoint.
3. If no zero entry exists, use fleet01/B07's Cartan Hessian packing together with fleet04/B08's pair-specific endpoint roofs and the strict odd-overlap/Spin(6) stationarity constraints.

Thus the remaining proof can be split into two quantitative incompatibility statements, rather than an unconstrained zero-face problem plus an unconstrained interior problem.

## 8. First essential missing implication

`MOC4-ZERO-FIBER-SPECTRAL-PAYMENT-v1`:

On the zero-entry branch, combine

- the rank-one corner factorization already retained by fleet03/B07,
- the exact quadratic representation `h(q)=q^T H_eta q`,
- the positive averaged lift (3)-(5), hence `Delta_mu>=0`,
- the exact boundary curvature payment (11),
- and the structured one-cycle / pair-roof inequalities from the cited peer results,

to rule out `lambda_max(H_eta)>M_eta` for every genuine zero-face source datum; equivalently prove `M_eta I-H_eta` is positive semidefinite from those structured constraints. A failure must be exhibited by an actual zero-entry unitary and actual spectra/support direction, not by an arbitrary symmetric `4 x 4` matrix.

The strict-interior branch separately retains `MOC4-STRICT-INTERIOR-GAP-PAYMENT-v1` from the current peer lineage.

## 9. Status / limitations

- **ESSENTIAL_STEP_APPLIED**: exact positive common lift for the residual-fiber Haar average, exact quaternion Rayleigh reduction, and an exact zero-face Hessian payment.
- This is **not** a full proof of MOC4.
- No arbitrary bistochastic surrogate was used.
- No numerical or external computation is used as evidence in this report; the argument is algebraic/Haar-exact.
- Singular and repeated spectra are covered by the identities above because all determinant identities are polynomial and no division by spectral differences is used.
