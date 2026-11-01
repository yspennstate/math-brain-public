SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B08, 2026-09-23T00:21:08Z.
attacking: a one-shot Pluecker/third-compound transfer from three diffuse genuine eigenvectors to finite original-coordinate determinant banks, together with an aggregate e3 Fourier receiver that never selects one tiny minor.

# fleet03/B08 r25 — diffuse Pluecker overlap ledger and aggregate third-volume Fourier closure

**Run:** `20260923T002108Z-fleet03-B08-qform-diffuse-r25`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING TARGET-RELEVANT THEOREMS / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The target remains the unrestricted theorem for independent real original coordinates with one-dimensional probability densities bounded by one and arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one. No moment, Gaussian, log-concavity, compact-support, connected-support, iid, diagonal-basis, or independence-after-rotation assumption is introduced. Essential boundedness and continuity are tracked separately.

This run changes mechanism from the preceding recursive balanced-cut curvature ladder. It works directly in the third exterior power of the **actual full matrix** and uses the diffuse three-eigenvector packet only as a Pluecker test vector. In particular it does not discard arbitrary extra spectrum.

The live corrections were reread. In addition to the standing pointwise-decay, arbitrary-joint-coarea, conditional-height and fiber-sup corrections, I consumed the fresh `QFORM-N3-LOCAL-COLLISION-BEFORE-AGGREGATION-FALSE-v1` addendum: localizing to one physical pair before aggregation can lose a positive power of bank size. The theorem below aggregates squared third minors before any reciprocal/minor endpoint, so it goes in the correction-required direction.

## 2. Inputs actually used

1. **Own preceding diffuse theorem.** fleet03/B08 r24,
   `yspennstate/math-open-problems@1bf6f41d81ffddcc6e8ff93b4df165d0ce5bbd05`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T231729Z-fleet03-B08-qform-diffuse-r24/REPORT.md`.
   It supplied the balanced-cut curvature transfer, but its proposed multiscale recursion is *not* used below.

2. **Overlap-aware coordinate banks.** fleet03/B07,
   `yspennstate/math-open-problems@391688138f7f481a2c8688c2d27f9508db7af6af`.
   For the overlap energies
   `E_q(A)=sum_{|I|=|J|=3, |I cap J|=q} det A[I,J]^2`,
   it proves finite disjoint original-coordinate bank extractions with factors
   `1/1296`, `4/3125`, `1/128`, `2/9` for `q=0,1,2,3`, respectively.

3. **Regularized cross-block determinant theorem.** interactive source
   `yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`.
   If `B=A[I,J]` is an original-coordinate cross block and for some `1<=q<2`
   the coordinate diagonal of the projection onto `range(B)` on one side is at most `q/2`, then
   `|phi_Q(t)| <= det(I+2q t^2 BB^T/(pi^2 e^2))^(-1/(4q))`,
   with arbitrary same-side quadratic terms, affine terms, and outside couplings retained.

4. **Compatible completed fleet04 result actually applied.** The designated `fleet04/B08` current-QFORM report/handoff is still absent, so none is fabricated. I apply fleet04/B01,
   `QFORM-GROUPED-SQUARE-INNOVATIONS-v1`,
   `yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`,
   to a genuine diffuse target family in Section 7.

## 3. Pluecker law of the selected three-eigenspace

Let `R` be an `n x 3` matrix with orthonormal columns satisfying

`A R = R Lambda`,                                                   (3.1)

where `Lambda=diag(lambda_1,lambda_2,lambda_3)` and

`min_j |lambda_j| >= L > 0`.                                       (3.2)

Write the row leverages

`ell_i=||R_{i,*}||_2^2`, `mu=max_i ell_i`.                          (3.3)

For each physical three-set `I`, define

`u_I=det R_I`.                                                       (3.4)

Cauchy--Binet gives

`sum_I u_I^2=det(R^T R)=1`.                                        (3.5)

Thus `w_I=u_I^2` is a probability law on physical triples. Its one-coordinate marginals are exactly the leverages:

`sum_{I contains i} u_I^2=ell_i`.                                  (3.6)

For completeness, (3.6) follows by differentiating the Cauchy--Binet identity

`det(R^T D R)=sum_I u_I^2 prod_{j in I} d_j`                       (3.7)

with respect to `d_i` at `D=I`; the matrix derivative is
`tr(R^T e_i e_i^T R)=ell_i`.

Draw `I,J` independently from `w`. Then

`P(I cap J != empty)
 <= E |I cap J|
 = sum_i P(i in I)P(i in J)
 = sum_i ell_i^2
 <= mu sum_i ell_i
 = 3 mu`.                                                          (3.8)

This is the key diffuse statement: two independent Pluecker triples are disjoint with probability at least `1-3mu`, without choosing any physical coordinate.

## 4. Main structural theorem: selected spectral curvature forces actual full-matrix overlap energy

Let `M=C_3(A)=wedge^3 A` be the third compound matrix in the standard physical three-set basis, so

`M_{I,J}=det A[I,J]`.                                               (4.1)

The Pluecker vector `u=(u_I)` is an exact eigenvector of `M`:

`M u=(lambda_1 lambda_2 lambda_3)u`,                               (4.2)

because `r_1 wedge r_2 wedge r_3` is an eigenvector of `wedge^3 A`. Hence, with
`lambda_* = lambda_1 lambda_2 lambda_3`, 

`|u^T M u|=|lambda_*|>=L^3`.                                       (4.3)

Define

`E_q(A)=sum_{|I|=|J|=3, |I cap J|=q} M_{I,J}^2`, `q=0,1,2,3`,       (4.4)

and let `P_q` be the analogous Pluecker-pair probability

`P_q=sum_{|I cap J|=q} u_I^2 u_J^2`.                              (4.5)

By (3.8),

`P_1+P_2+P_3 <=3mu`.                                                (4.6)

Applying Cauchy--Schwarz separately to the disjoint and overlapping parts of (4.3) yields

`L^3
 <= sqrt(E_0 P_0)+sqrt((E_1+E_2+E_3)(P_1+P_2+P_3))
 <= sqrt(E_0)+sqrt(3mu(E_1+E_2+E_3))`.                             (4.7)

### Theorem 4.1 — `QFORM-DIFFUSE-PLUECKER-OVERLAP-LEDGER-v1`

Under (3.1)--(3.3),

`boxed[ sqrt(E_0(A)) + sqrt(3mu(E_1(A)+E_2(A)+E_3(A))) >= L^3 ].`    (4.8)

Consequently, using the clean split `3/4+1/4=1`, either

`E_0(A) >= (9/16)L^6`,                                             (4.9)

or

`E_1(A)+E_2(A)+E_3(A) > L^6/(48mu)`.                              (4.10)

In the latter case some `q in {1,2,3}` satisfies

`E_q(A)>L^6/(144mu)`.                                              (4.11)

No hypothesis is made on any other eigenvalue of `A`; all additional spectrum is already present in the actual minors in (4.4).

## 5. Diffuse physical-bank corollary with explicit constants

Assume now

`mu<=1/48`.                                                         (5.1)

Combining Theorem 4.1 with the completed B07 overlap-coloring theorem gives an exhaustive finite-bank alternative in ORIGINAL coordinates.

* `q=0`: six pairwise-disjoint banks `L1,L2,L3,R1,R2,R3` with
  `P0_bank >= (9/16)L^6/1296 = L^6/2304`.
* `q=1`: five pairwise-disjoint banks `H,R1,R2,C1,C2` with
  `P1_bank > (4/3125)(L^6/3)=4L^6/9375`.
* `q=2`: four pairwise-disjoint banks `H1,H2,R,C` with
  `P2_bank > (L^6/3)/128=L^6/384`.
* `q=3`: three pairwise-disjoint banks `H1,H2,H3` with
  `P3_bank > (2/9)(L^6/3)=2L^6/27`.

Therefore:

### Corollary 5.1 — `QFORM-DIFFUSE-FINITE-BANK-COMPILER-v1`

If three genuine eigenvectors with eigenvalues of modulus at least `L` satisfy
`max_i ||R_{i,*}||^2<=1/48`, then the **actual full matrix** admits one of the four B07 product-preserving overlap-bank packets, and the surviving packet has squared-determinant mass at least

`boxed[ 4 L^6 / 9375 ].`                                          (5.2)

This is dimension-free and one-shot. It replaces the r24 proposed repeated balanced-cut descent by a single exterior-power transfer. It also obeys the fresh collision correction: aggregation occurs before any individual-minor reciprocal is taken.

## 6. New analytic receiver: aggregate third volume, not three individually lower-bounded singular values

The `q=0` bank has a direct Fourier receiver that is stronger than selecting one minor.
Let `B=A[I,J]` be any original-coordinate cross block and set

`Delta_3(B):=e_3(BB^T)
 =sum_{|S|=|T|=3} det B[S,T]^2`.                                  (6.1)

### Theorem 6.1 — `QFORM-CROSS-E3-RIDGE-v1`

Fix `1<=q<3/2`. Assume the coordinate diagonal of the orthogonal projection onto `range(B)` on one physical side is at most `q/2`. If `Delta_3(B)>0`, then `Q=X^TAX` has a continuous `C_0` density and

`boxed[
 ||p_Q||_infinity
 <= { e \/ (6 sqrt(2q)) }
    BETA(1/6, 1/(4q)-1/6)
    Delta_3(B)^(-1/6).
]`                                                                (6.2)

#### Proof

The completed regularized determinant theorem gives

`|phi_Q(t)|
 <=det(I+c_q t^2 BB^T)^(-1/(4q)),
 c_q=2q/(pi^2 e^2)`.                                               (6.3)

Expand the determinant into elementary symmetric functions of the squared singular values. Every coefficient is nonnegative, so

`det(I+c_q t^2 BB^T)
 >=1+c_q^3 Delta_3(B)t^6`.                                         (6.4)

Thus

`|phi_Q(t)|
 <=(1+c_q^3 Delta_3(B)t^6)^(-1/(4q)).`                             (6.5)

The right side is integrable exactly when `q<3/2`. Substituting
`u=c_q^3 Delta_3(B)t^6` gives

`int_R |phi_Q(t)|dt
 <=(1/3)c_q^(-1/2)Delta_3(B)^(-1/6)
   BETA(1/6,1/(4q)-1/6)`.                                          (6.6)

Fourier inversion and `c_q^(-1/2)=pi e/sqrt(2q)` prove (6.2). Since the characteristic function has an `L^1` majorant, the density is continuous and vanishes at infinity. QED.

This theorem is specifically an **aggregate-before-inversion** statement: no lower bound on any individual third singular value or any individual `3x3` minor is needed.

### Explicit diffuse `q=0` bound

In the `q=0` branch of Corollary 5.1, let
`I=L1 union L2 union L3` and `J=R1 union R2 union R3`. The selected packet is a sub-sum of (6.1), so

`Delta_3(A[I,J]) >= L^6/2304`.                                    (6.7)

If the corresponding one-side range leverage is at most `1/2`, take `q=1` in (6.2):

`||p_Q||_infinity
 <= [e/(6sqrt2)] BETA(1/6,1/12) 2304^(1/6) / L
 =20.5544096416.../L
 <21/L`.                                                          (6.8)

The density is continuous. If the range-leverage gate fails, the same actual cross block has a physical coordinate carrying more than half of its range projection, i.e. a quantitative localized-coordinate event rather than an unresolved diffuse Fourier estimate.

More generally any `q<3/2` gives a leverage gate `q/2<3/4`; e.g. `q=4/3` permits leverage up to `2/3` and gives the same branch a finite explicit constant `54.173/L`.

## 7. Completed fleet04 mathematics applied to an actual diffuse target family

The designated fleet04/B08 path is still absent. The compatible completed fleet04 result actually applied is fleet04/B01 `QFORM-GROUPED-SQUARE-INNOVATIONS-v1` at commit
`88003dc06af684cc4bc178a7dfe8e7cbebb0f987`.

For every `m>=48`, split `3m` original coordinates into three disjoint banks `B1,B2,B3` of size `m` and let

`r_j=m^(-1/2) 1_{B_j}`.                                           (7.1)

Then `r_1,r_2,r_3` are orthonormal, their maximum selected-frame row leverage is `mu=1/m<=1/48`, and for any real `lambda_j` with `|lambda_j|>=L`,

`A=sum_{j=1}^3 lambda_j r_j r_j^T`                                (7.2)

is a genuinely diffuse, generally non-diagonal exact-rank-three target matrix. Put
`L_j=r_j^T X_{B_j}`. The banks are disjoint original-coordinate banks, so the `L_j` are genuinely independent. The completed fleet04/B01 theorem applies directly to

`Q=lambda_1 L_1^2+lambda_2 L_2^2+lambda_3 L_3^2`.                 (7.3)

Two of the three coefficients have the same sign. Their coefficient-vector norms are one, so fleet04/B01 gives the actual inequality

`boxed[ ||p_Q||_infinity <= 2pi/L ]`,                              (7.4)

and `p_Q in C_0(R)`, for **every** admissible cap-one product law and every `m>=48`. This is a regression/application of completed fleet04 mathematics, not a claim that arbitrary diffuse eigenvectors have disjoint supports.

## 8. What is now reduced, and what remains

For a selected three-eigenvector frame with `mu<=1/48`, the new result removes the need to recurse balanced physical cuts merely to obtain determinant currency. One shot gives an actual full-matrix finite-bank packet of size at least `4L^6/9375`.

The `q=0` packet is already analytically paid whenever its one-side cross-range leverage is at most `1/2`, with the continuous bound `<21/L`; the tunable theorem pays larger leverage thresholds below `3/4` at larger constants. Failure of that gate is an explicit localized physical row of the cross range.

The remaining branches are therefore concrete and correction-compatible:

1. consume the `q=1,q=2,q=3` **aggregate shared-coordinate packets** using the B07 exact Schur-compound ladder and existing grouped/half-Riesz receivers, without selecting one bad local pair;
2. route the `q=0` high-cross-range-leverage failure into the heavy-coordinate machinery;
3. keep the zero/near-zero physical-pivot cases distinct from nonzero pivots.

This is strictly narrower than r24's open-ended multiscale curvature ledger and is aligned with the newest correction that aggregation must precede local fractional endpoints.

## 9. Status

* `QFORM-DIFFUSE-PLUECKER-OVERLAP-LEDGER-v1`: **PROVED**.
* `QFORM-DIFFUSE-FINITE-BANK-COMPILER-v1`: **PROVED**, explicit packet mass `>=4L^6/9375` for `mu<=1/48`.
* `QFORM-CROSS-E3-RIDGE-v1`: **PROVED**, continuous density under the stated cross-range leverage gate.
* Explicit `q=0`, `mu<=1/48`, leverage `<=1/2` estimate: **PROVED**, `||p_Q||_infinity<21/L`.
* fleet04/B01 grouped-square theorem: **APPLIED** to the genuine diffuse family (7.1)--(7.4), giving `2pi/L` and continuity.
* Full universal QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
* Universal continuity conclusion: **OPEN**.

No public release, scheduler mutation, email/push notification, paid API/Codex call, credential access, or cross-account native action is part of this run.
