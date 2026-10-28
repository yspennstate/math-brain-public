SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T06:18:05Z.
attacking: exterior-power/Pluecker stability of fifth cross-volume under arbitrary signed rank-one spectral additions; seed an actual five-mode carrier with the completed account02/B12 numerical-range theorem and transport it through further resonant eigenmodes without any convolution argument.

# account01/B12 — exterior-power stability for added eigenvalues

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: additional eigenvalue control  
Run: `20260924T061805Z-account01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain state: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and first unpaid implication

The target is unchanged: independent ORIGINAL coordinates with densities bounded by one, arbitrary real symmetric `A`, and only the hypothesis that at least three eigenvalues of `A` have modulus at least one. No moment, compact-support, connected-support, iid, log-concavity, Gaussian, diagonal-basis or post-rotation-independence assumption is used below.

The present run changes mechanism from the preceding relative-inertia/operator-carrier approach. The new invariant is the actual fifth exterior volume of an ORIGINAL-coordinate cross block. A single spectral eigenmode changes every fifth minor only affinely in its amplitude. This yields an exact resonance formula and a magnitude-free stability factor. The result handles both signs and arbitrarily large amplitudes; a separate one-shot Weyl payment handles arbitrarily many small eigenvalues.

The first unpaid implication remains structural: bare `s_3(A)>=1` has not been shown to force a fifth-volume physical cross certificate, nor does common spectral independence imply such a certificate (the live `QFORM-BIINDEPENDENT-SPECTRAL-MODES-NOT-CROSS-VOLUME-v1` correction forbids that shortcut). The theorem below transports a certificate once it exists; it does not manufacture one from `s_3(A)>=1`.


The density receiver used at the end is the completed fifth-volume theorem in `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, path `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`: for any actual disjoint ORIGINAL-coordinate cross block `B=A[I,J]`,

`||p_(X^T A X)||_infinity <= 5 sqrt(2e) e_5(B^T B)^(-1/10)`,

with no row-marginal condition; the branch has a continuous `C_0(R)` density. Same-bank terms, outside curvature, outside couplings and affine terms are retained by that theorem.

## 2. General Pluecker affine-line identity

Let `B in R^{p x q}`, `p,q>=k`, and assume

`Z_k(B):=e_k(B^T B)>0`.

Equivalently, `rank(B)>=k`. Let `D_k(B)` be the Euclidean vector of all `k x k` minors

`D_{R,C}(B)=det(B[R,C])`, `|R|=|C|=k`.

By Cauchy-Binet,

`||D_k(B)||_2^2 = e_k(B^T B)=Z_k(B)`.                     (2.1)

For `a in R^p`, `b in R^q`, define the derivative Pluecker vector

`C_k(B;a,b) = d/dtheta|_{theta=0} D_k(B+theta a b^T)`.      (2.2)

For every pair `(R,C)`, the rank-one determinant identity gives exactly

`det(B[R,C]+theta a_R b_C^T)
 = det(B[R,C]) + theta b_C^T adj(B[R,C]) a_R`.              (2.3)

There are no powers `theta^2` in any individual minor.

### Theorem 2.1 — `QFORM-PLUECKER-RANKONE-SPECTRAL-STABILITY-v1`

Put `D=D_k(B)` and `C=C_k(B;a,b)`. Then for every real `theta`,

`boxed:
 Z_k(B+theta a b^T)
 = ||D+theta C||_2^2
 = Z_k(B)+2 theta <D,C>+theta^2 ||C||_2^2.`                 (2.4)

If `C=0`, then `Z_k(B+theta a b^T)=Z_k(B)` for every `theta`.

If `C!=0`, define

`rho = <D,C>/(||D|| ||C||)`,
`eta = sqrt(1-rho^2) in [0,1]`.                              (2.5)

Then

`boxed:
 inf_{theta in R} Z_k(B+theta a b^T)
 = eta^2 Z_k(B),`                                           (2.6)

and the minimizing amplitude is

`theta_* = -<D,C>/||C||^2`.                                 (2.7)

Consequently, if `eta>0`, no positive or negative amplitude, however large, can drive the cross-block rank below `k`. Exact rank loss at some amplitude can occur only in the Pluecker-collinear case `eta=0`.

### Proof

Equation (2.3) proves `D_k(B+theta ab^T)=D+theta C` coordinate by coordinate. Squaring and summing gives (2.4). If `C!=0`, completing the square gives

`||D+theta C||^2
 = ||C||^2 (theta+<D,C>/||C||^2)^2
   + ||D||^2 - <D,C>^2/||C||^2`,

which is (2.6). Since `Z_k=0` exactly when every `k x k` minor vanishes, `eta>0` forbids rank below `k`. QED.

This theorem is coefficient algebra only. It does not rotate the random vector and does not treat the added quadratic term as independent noise.

## 3. Exact two-sided formula when the baseline has rank exactly k

The abstract angle in Theorem 2.1 has an explicit physical formula in the rank-exactly-`k` case.

Let

`B=U Sigma V^T`,

where `U in R^{p x k}`, `V in R^{q x k}` have orthonormal columns and `Sigma=diag(sigma_1,...,sigma_k)>0`. Decompose

`alpha=U^T a`, `beta=V^T b`,
`a_perp=(I-UU^T)a`, `b_perp=(I-VV^T)b`,                    (3.1)

and define

`tau = beta^T Sigma^{-1} alpha`,                             (3.2)

`R = tau^2
   + ||a_perp||^2 ||Sigma^{-1} beta||^2
   + ||b_perp||^2 ||Sigma^{-1} alpha||^2
   + ||a_perp||^2 ||b_perp||^2 tr(Sigma^{-2}).`             (3.3)

### Theorem 3.1 — `QFORM-TWOSIDED-RANKk-RESONANCE-FORMULA-v1`

For every real `theta`,

`boxed:
 e_k((B+theta ab^T)^T(B+theta ab^T))
 = (det Sigma)^2 [1+2 theta tau+theta^2 R].`                 (3.4)

If `R>0`, the uniform magnitude-free reserve is

`boxed:
 e_k((B+theta ab^T)^T(B+theta ab^T))
 >= (det Sigma)^2 (1-tau^2/R)`                              (3.5)

for every `theta`. The quantity `R-tau^2` is the exact transverse repair energy:

`R-tau^2
 = ||a_perp||^2 ||Sigma^{-1} beta||^2
 + ||b_perp||^2 ||Sigma^{-1} alpha||^2
 + ||a_perp||^2 ||b_perp||^2 tr(Sigma^{-2}) >=0.`           (3.6)

Hence exact destructive resonance requires the transverse repair to vanish. In particular, if either side of the spectral mode has a quantitative component outside the corresponding active singular subspace while the opposite active component is nonzero, the `k`-volume cannot collapse for any sign or magnitude of `theta`.

### Proof

Both sides of (3.4) are invariant under orthogonal changes of coordinates on the row and column spaces, so reduce to

`B = [[Sigma,0],[0,0]]`.

Every `k x k` minor of `B+theta ab^T` is affine in `theta`. The only minor with nonzero constant term is the active-active minor; its derivative is `(det Sigma) tau`.

The remaining derivative minors fall into three mutually orthogonal classes in the Euclidean minor vector:

1. replace one active row by an outside row, keeping active columns. Squared derivative mass:
   `(det Sigma)^2 ||a_perp||^2 ||Sigma^{-1} beta||^2`;
2. replace one active column by an outside column, keeping active rows. Squared derivative mass:
   `(det Sigma)^2 ||b_perp||^2 ||Sigma^{-1} alpha||^2`;
3. replace the same active row/column index by one outside row and one outside column. Squared derivative mass:
   `(det Sigma)^2 ||a_perp||^2 ||b_perp||^2 tr(Sigma^{-2})`.

If different active row and column indices were missing in class 3, the baseline minor would have rank at most `k-2`, and a rank-one update could not make its determinant nonzero; thus only the matched-index terms contribute. Summing the square of the active derivative and the three orthogonal classes gives exactly `(det Sigma)^2 R`. Equation (3.4) follows from Theorem 2.1, and (3.5)-(3.6) follow by minimizing the quadratic. QED.

The preceding formula extends the full-column determinant-resonance calculation to the genuinely two-sided rectangular rank-`k` situation: both left and right null-space components can repair a longitudinal resonance.

## 4. Arbitrary high spectral packets: adaptive corollary

Let `I,J` be disjoint ORIGINAL-coordinate banks and let a symmetric spectral packet be written

`S_hi = sum_{r=1}^N theta_r v_r v_r^T`,                       (4.1)

with arbitrary real `theta_r` (positive or negative, no size bound). Put

`a_r=P_I v_r`, `b_r=P_J v_r`,
`B_r=B_{r-1}+theta_r a_r b_r^T`, `B_0=A_0[I,J]`.             (4.2)

Assume `Z_k(B_0)>0`, and at step `r` let `eta_r` be the Pluecker angle from Theorem 2.1 for `(B_{r-1},a_r,b_r)`, with `eta_r=1` when the derivative vector vanishes. Then

`boxed:
 Z_k(B_N) >= Z_k(B_0) prod_{r=1}^N eta_r^2.`                 (4.3)

No amplitude `theta_r` appears in the right side. The modes may have either sign and arbitrary magnitude. The angles are geometric and are evaluated on the actual current physical cross block; this is intentionally stronger than pretending spectral coordinates remain independent.

For `k=5`, the completed D5 receiver therefore gives, whenever all factors are positive,

`boxed:
 ||p_(X^T A X)||_infinity
 <= 5 sqrt(2e) Z_5(B_0)^(-1/10)
    prod_{r=1}^N eta_r^(-1/5).`                              (4.4)

The density in this branch has a continuous `C_0` representative.

This is a true added-eigenvalue stability theorem: it prices each arbitrary large signed mode by its exterior geometric alignment, not by its eigenvalue magnitude.

## 5. One-shot control of arbitrarily many small eigenvalues

Let `E_lo=E_lo^T` have all eigenvalues in `[-h,h]`. Its rank, signs, multiplicities and eigenvectors are unrestricted, and

`||E_lo||op <= h`.                                            (5.1)

Therefore every physical cross compression satisfies

`||E_lo[I,J]||op <= h`.                                       (5.2)

If a high-spectrum construction produces an actual cross block `B_hi` with

`s_5(B_hi)>=g`,                                               (5.3)

and a further arbitrary symmetric remainder `T` satisfies only

`||T[I,J]||op <= delta`,                                      (5.4)

then singular-value Weyl gives

`boxed:
 s_5(A[I,J]) >= g-h-delta.`                                  (5.5)

Thus, whenever `g>h+delta`,

`boxed:
 ||p_(X^T A X)||_infinity
 <= 5 sqrt(2e)/(g-h-delta).`                                 (5.6)

The outside-outside and same-bank blocks of `T` are unrestricted. No claim is made that `X^T E_lo X` or `X^T T X` is small as a random variable.

## 6. Applying the completed account02/B12 theorem to an actual inequality

I now use the designated partner's newest completed theorem at an equation, not merely as a citation.

Take disjoint ORIGINAL-coordinate banks

`H={h_1,...,h_9}`, `J={j_1,...,j_9}`,

and on `H union J` let

`A_0 = [[0,2 I_9],[2 I_9,0]].`                               (6.1)

Let

`R_2=[[0,1],[-1,0]]`, `J_4=diag(R_2,R_2)`,
`K_c=diag(-I_4,c J_4,0)`, `c>=2`,                            (6.2)

and add

`S_c=[[0,2K_c^T],[2K_c,0]].`                                 (6.3)

For the partner's carrier `P_H`, the baseline scale is `g=2` and its whitened relative action is exactly `K_c`; the fifth eigenvalue of `Sym(K_c)=diag(-I_4,0_4,0)` is zero. The account02/B12 theorem therefore gives

`boxed:
 s_5((A_0+S_c)P_H) >= 2.`                                    (6.4)

Since the `H x H` block is zero at this stage, this is the actual cross-block inequality

`boxed:
 s_5(B_c) >= 2,
 B_c=(A_0+S_c)[H,J]=2(I_9+K_c^T).`                           (6.5)

The partner report further computes equality `s_5(B_c)=2`. Importantly, `S_c` is not small: it contains signed eigenvalues of magnitude `2c`, so (6.5) already survives an unbounded positive/negative spectral packet.

This is the promised application of a completed account02/B12 result.

## 7. New transport beyond the partner carrier: four arbitrary signed eigenmodes

The first four rows of `B_c` vanish because the first block of `I_9+K_c^T` is zero. Hence

`span(e_{h_1},...,e_{h_4}) subset ker(B_c^T)`.                (7.1)

For `r=1,...,4`, define the mutually orthonormal ambient vectors

`v_r=(e_{h_r}+e_{j_{4+r}})/sqrt(2)`                           (7.2)

and add the spectral packet

`L_lambda=sum_{r=1}^4 lambda_r v_r v_r^T`,                   (7.3)

where **every `lambda_r` is an arbitrary real number**, independently positive or negative and with no magnitude bound. Since the `v_r` are orthonormal, `L_lambda` itself has nonzero eigenvalues exactly `lambda_1,...,lambda_4`.

Its physical cross block is

`E_lambda=L_lambda[H,J]
 = (1/2) sum_{r=1}^4 lambda_r e_{h_r} e_{j_{4+r}}^T`.         (7.4)

By (7.1),

`B_c^T E_lambda=0`.                                           (7.5)

Therefore the exact Gram identity is

`boxed:
 (B_c+E_lambda)^T(B_c+E_lambda)
 = B_c^T B_c + E_lambda^T E_lambda
 >= B_c^T B_c.`                                               (7.6)

Consequently

`boxed:
 s_5(B_c+E_lambda) >= 2`                                      (7.7)

for **all** four signed amplitudes, even at infinity. This is the `eta=1` chamber of the Pluecker theorem: the added modes are exterior-transverse, so their fifth-volume contribution is orthogonal to the old Pluecker line.

Notice that these modes are not spectators. They couple the two smoothing banks and simultaneously create arbitrary same-bank quadratic terms through the diagonal pieces of `v_rv_r^T`; the D5 receiver retains those pieces automatically.

## 8. Arbitrarily many small eigenvalues, dense local tail, and exact target verification

Append any arbitrary-dimensional symmetric spectator block `Theta`; its signs, multiplicities, magnitudes and internal mixing are unrestricted. It does not change the chosen `H x J` cross block.

Now add an arbitrary symmetric low spectral packet `E_lo` with

`||E_lo||op <= 1/64`,                                        (8.1)

so it may contain arbitrarily many small positive and negative eigenvalues, and add a further arbitrary symmetric `T` satisfying only

`||T[H,J]||op <= 1/64`.                                      (8.2)

All same-bank and outside-outside parts of `T` may be arbitrarily large. From (7.7) and Weyl,

`boxed:
 s_5(A[H,J]) >= 2-1/64-1/64 = 63/32.`                        (8.3)

Hence

`e_5(A[H,J]^T A[H,J]) >= (63/32)^10`.                        (8.4)

The D5 theorem gives the actual final-law estimate

`boxed:
 ||p_(X^T A X)||_infinity
 <= 5 sqrt(2e)/(63/32)
 = 5.921635508818094... < 5.922.`                             (8.5)

This branch has a continuous `C_0` density.

Finally, compression is contractive for singular values:

`s_5(A[H,J]) <= s_5(A)`.                                      (8.6)

Because `A` is symmetric, its singular values are the ordered absolute values of its eigenvalues. Therefore

`boxed:
 s_5(A) >= 63/32 >1`,                                        (8.7)

so every matrix in this explicit family genuinely lies inside the owner's exact target class (indeed it has at least five eigenvalues of modulus greater than one).

## 9. What this pays and what remains

Paid here:

- one arbitrary signed spectral mode admits an exact quadratic fifth-volume formula in its amplitude;
- a mode with positive Pluecker angle cannot destroy a `k`-volume at any amplitude;
- sequential arbitrary large signed spectral modes are charged by geometric Pluecker angles, not by their eigenvalue sizes;
- for rank exactly `k`, the angle has the explicit two-sided repair formula (3.3)-(3.6);
- arbitrarily many small eigenvalues of either sign are paid in one operator threshold;
- the designated account02/B12 theorem is applied to seed an actual `s_5>=2` cross carrier;
- four further mutually orthogonal spectral modes with completely arbitrary signed eigenvalues preserve that carrier exactly;
- the final target-class family has the continuous density bound `<5.922`.

Still unpaid:

The bare global assumption `s_3(A)>=1` does not force any particular physical fifth-volume `Z_5(A[I,J])` to be positive at a universal scale. The existing correction that bi-independent spectral modes can cancel in aggregate cross volume shows why a purely spectral-independence argument cannot supply this. A full proof still needs a cancellation-aware structural dichotomy: either some original-coordinate cross block has a quantitative fifth exterior volume (then D5 plus the transport theorem above pays arbitrary added spectrum), or the failure of all such volumes must force one of the already-paid grouped-bank/hub, physical-pair, Schur, ridge, half-Riesz, common-plane or related exits.

Therefore **the unrestricted conjecture remains OPEN**. Essential boundedness and continuity are proved only in the stated D5 branch.

## 10. Finite sanity check

`CHECK.py` verifies the rank-exact formula on 2,000 random rank-five rectangular matrices at three amplitudes each and checks the explicit partner-family transverse packet. It reported

`max_relative_formula_error = 1.427189e-13`,
`partner_family_baseline_s5 = 2.000000000000`,
`partner_family_min_s5_over_test_lambdas = 2.000000000000`,
`density_bound_h_delta_1over64 = 5.921635508818`.

These computations are sanity checks only. The proof is the exact determinant/minor algebra above.

## 11. Source/correction ledger

Fresh control source: `yspennstate/math-research-brain@ff61378f690209c9d98542dbb67ab6cff48d981c`.

Consumed live corrections include: pointwise quadratic-phase decay false; no independence after spectral rotation; fiber-sup dimension loss; arbitrary-joint rank-three coarea false; positive conditional projection-density moments false; and `QFORM-BIINDEPENDENT-SPECTRAL-MODES-NOT-CROSS-VOLUME-v1`. None is used as a positive premise.

Partner applied: `yspennstate/math-open-problems@572fa1f2bc3b1ab29018a426f414d21dce2b5504`, account02/B12 `QFORM-RELATIVE-NUMERICAL-RANGE-MODE-SHIELD-v1`, equations (2.1)-(2.3) and explicit family (5.1)-(5.7).

Receiver applied: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `FOURIER_ROUTE_REPORT.md`, theorem D5.

No scheduler state, email, notification, task identity, permission, repository visibility, paid model/API, remote workflow or cross-account authentication was changed.
