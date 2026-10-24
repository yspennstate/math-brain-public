SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B03, 2026-09-22T18:23:38Z.
attacking: bank-level decoupled time integration after the finite-pair TT* fragmentation obstruction; convert a residual original-coordinate cross bank into a fractional collision bound and linear small-ball estimate.

# account03/B03 — three-cross-bank fractional collision splice

Run: `20260922T182338Z-account03-B03-QFORM-r17`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Decoupled time integral`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING THEOREM + SHARP THRESHOLD FOR THIS MECHANISM / FULL TARGET OPEN**.

## 1. Exact target and current corrections

The owner target is the unrestricted statement for every dimension, every independent real input vector whose one-dimensional densities satisfy `0<=f_i<=1`, and every real symmetric matrix having at least three eigenvalues of modulus at least one. The goal is one universal essential-density bound for `Q=X^TAX`, or a target-valid counterexample. Continuity is separate.

This report does not rotate the product law, does not use the refuted law-uniform scalar Fresnel decay, does not condition on `U=X+X'` as if `V=X-X'` retained a density cap, and does not use the refuted arbitrary-joint rank-three coarea or positive conditional-density-moment gates.

A new same-assignment result from account02/B03, canonical source `yspennstate/math-open-problems@e43c2e6afdf2063d5ce3f517d37f066acbda7b12`, proves that *every fixed finite-coordinate* closure obtained by moving absolute values through the exact pair-law `u` integral and then combining one-coordinate Plancherel/L-infinity estimates with time Holder has a certificate diverging on an explicit cap-one scale mixture, even for the solved diagonal form `A=I_3`. Its true collision integral stays bounded. Thus the mechanism below deliberately aggregates a full original-coordinate cross bank first, before paying any fractional collision norm.

The designated partner `account04/B03` still has no completed current-QFORM handoff or canonical report at the fresh source scan. No result is attributed to that slot. A completed compatible account04 Fourier result is applied in Section 6.

## 2. Two completed ingredients actually used

### 2.1 Dependence-safe square / fractional-collision transducer

The preceding account03/B03 theorem, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260922T155848Z-account03-B03-QFORM-r15/REPORT.md`, starts from one ORIGINAL physical coordinate. If

`Q=a(Z+h(W))^2+R(W)`, `a!=0`,

where `Z` is independent of the original-coordinate vector `W` and has density at most one, then

`p_Q(y) <= |a|^(-1/2) E |y-R|^(-1/2)`.                              (2.1)

Let `eta(t)=E exp(itR)` and let `psi(t)=|eta(t)|^2`, the exact characteristic function of `R-R'`. For every `1/2<=alpha<1`, if

`S_alpha=int_R psi(t)^alpha dt=int_R |eta(t)|^(2alpha)dt<infinity`,   (2.2)

then

`||p_Q||_infinity <= [2/sqrt(pi(1-alpha))] |a|^(-1/2) S_alpha^(1/2)`. (2.3)

This step explicitly uses the independent-copy collision quantity while never declaring any within-pair sum/difference variables independent.

### 2.2 Bank-level regularized determinant

The complete regularized-determinant theorem at

`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a`,
`proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`

proves the following unconditional estimate. For any quadratic-affine polynomial in independent original coordinates with cap-one densities, and any bipartition of those ORIGINAL coordinates whose quadratic cross block is `T`,

`|eta(t)| <= det(I+4t^2 T T^T/(pi^2 e^2))^(-1/8)`.                   (2.4)

Arbitrary self-block quadratic terms and affine terms are permitted. Its proof uses independent-copy decoupling plus geometric Brascamp--Lieb before taking the determinant, so it is precisely a bank-level aggregation and does not incur the finite-coordinate fragmentation cost refuted by account02/B03.

## 3. Main theorem — a three-cross-bank fractional collision gate

### Theorem 3.1 (`QFORM-PIVOT-THREECROSS-FRACTIONAL-COLLISION-v1`)

Assume the physical-pivot representation (2.1). Suppose the residual quadratic-affine form `R(W)` admits a bipartition of its ORIGINAL coordinates with cross block `T` having at least three singular values at least `sigma>0`.

Then `Q` has an essentially bounded density and

`||p_Q||_infinity <= C_3 |a|^(-1/2) sigma^(-1/2)`,                    (3.1)

where

`C_3 = 2 sqrt( 3 e sqrt(pi) Gamma(1/8)/Gamma(5/8) )`

and

`C_3 = 17.425422922814978... < 17.426`.                              (3.2)

Thus every interval `I` satisfies the linear small-ball inequality

`P(Q in I) <= 17.426 |a|^(-1/2) sigma^(-1/2) |I|`.                   (3.3)

Only essential boundedness is proved here; continuity is not asserted.

### Proof

From (2.4), discarding determinant factors smaller than one but retaining the three factors belonging to singular values at least `sigma`,

`|eta(t)| <= (1+(2 sigma t/(pi e))^2)^(-3/8)`.                       (3.4)

Choose

`r=5/3`, `alpha=r/2=5/6`.

Then the fractional pair-collision integral is

`S_(5/6)=int |eta(t)|^(5/3) dt`

` <= int (1+(2 sigma t/(pi e))^2)^(-5/8) dt`.                        (3.5)

The standard beta/gamma integral, valid because `5/8>1/2`, gives

`int_R (1+(b t)^2)^(-5/8)dt`
` = b^(-1) sqrt(pi) Gamma(1/8)/Gamma(5/8)`.                          (3.6)

With `b=2 sigma/(pi e)`,

`S_(5/6) <= [pi e/(2 sigma)] sqrt(pi) Gamma(1/8)/Gamma(5/8)`.        (3.7)

Insert (3.7) into (2.3). Since `1-alpha=1/6`,

`||p_Q||_infinity`
` <= 2 sqrt(6/pi) |a|^(-1/2)`
`    * {[pi e/(2 sigma)] sqrt(pi) Gamma(1/8)/Gamma(5/8)}^(1/2)`
` = 2 sqrt(3 e sqrt(pi) Gamma(1/8)/Gamma(5/8))`
`    |a|^(-1/2) sigma^(-1/2)`,

which is (3.1)-(3.2). Equation (3.3) follows by integrating the density over `I`. QED.

## 4. General bank-rank formula and the exact threshold of this splice

The preceding proof has a useful general form. If `T` has `k` singular values at least `sigma` and `1<=r<2`, put `alpha=r/2`. From (2.4),

`int |eta(t)|^r dt`
` <= [pi e/(2 sigma)] sqrt(pi)`
`    Gamma(kr/8-1/2)/Gamma(kr/8)`                                  (4.1)

whenever

`kr>4`.                                                            (4.2)

Combining (4.1) with (2.3) yields an explicit essential-density bound for every `r` satisfying

`max(1,4/k)<r<2`.                                                   (4.3)

This interval exists exactly when `k>=3`. Therefore:

* three bank singular directions are sufficient for this bank-RD + fractional-collision mechanism;
* for `k=2`, the unconditional regularized-determinant envelope alone cannot feed the half-Riesz criterion, because `kr<=4` for every admissible `r<2`; at the endpoint `r=2` the model integral has the logarithmic exponent `1/2` and diverges.

The second statement is a limitation of this particular absolute bank envelope, not a claim that every rank-two residual is bad. Exact-rank-two fractional-trace theorems already show that additional structure can beat this endpoint.

This threshold is target-relevant: a square pivot supplies one physical quadratic smoother, while three genuinely aggregated residual cross directions suffice to turn the independent-copy time integral into linear small-ball scaling. It also explains why merely repeating finitely many coordinatewise pair-Plancherel estimates, as ruled out by account02/B03, is the wrong way to seek those directions.

## 5. Structural consequence for the full proof programme

Theorem 3.1 closes the following full-matrix branch with arbitrary additional spectrum and arbitrary outside couplings:

> there is an original scalar pivot `a!=0` and, after completing that pivot, the Schur residual has an original-coordinate cross cut with `s_3(T)>=sigma>0`.

No rank assumption is placed on the full matrix or on the residual; extra singular directions can be arbitrarily small and are discarded harmlessly from (2.4).

Quantitatively, any structural reduction producing universal constants `|a|>=a_0>0` and `s_3(T)>=sigma_0>0` immediately gives

`||p_Q||_infinity < 17.426 / sqrt(a_0 sigma_0)`.                       (5.1)

Thus a putative counterexample surviving this branch must avoid such a pivot/cut combination. In particular, on a heavy physical pivot branch the remaining obstruction can be formulated as a low-third-cross-singular-value bank geometry rather than as a failure of the time integral itself.

This does **not** finish the owner theorem: the bare hypothesis `s_3(A)>=1` does not presently force a uniformly nonzero physical scalar pivot together with a residual cross block having three uniformly large singular values. Existing singleton-plus-bank and low-cross-rank examples prohibit assuming such an extraction. The difficult branch is still the near-zero/cross-dominated outer pivot and grouped-bank geometry, especially when only two effective residual directions survive after the pivot.

## 6. Compatible account04 result applied to the actual inequality

The designated `account04/B03` has no completed current-QFORM artifact, so no partner result is fabricated. I apply the completed compatible account04 Fourier theorem `QFORM-SIGNED-FEJER-EXACT-INTERFACE-v1`, canonical source

`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

It proves

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`                           (6.1)

for every bounded-density law, where `D_T` is the signed triangular Fejer average, and for an interval of length `ell`,

`mu(I)<= [pi ell/s_0] D_(2/ell)mu(y)`, `s_0=4 sin(1/2)^2`.            (6.2)

Applying (6.1) to Theorem 3.1 gives the concrete signed-time inequality

`sup_(T>0,y) D_T law(Q)(y)`
` <= C_3 |a|^(-1/2) sigma^(-1/2).`                                  (6.3)

Equation (6.2) therefore yields

`P(Q in I) <= (pi/s_0) C_3 |a|^(-1/2) sigma^(-1/2) |I|`.            (6.4)

The direct density estimate (3.3) has the sharper constant, but (6.3)-(6.4) explicitly transfer the bank-level independent-copy estimate into the account04 signed-time interface while retaining cancellation that absolute `L^1` Fourier arguments lose.

## 7. Relation to the fresh finite-pair obstruction

The account02/B03 scale-mixture result is applied, not merely cited: it eliminates the candidate proof step

`exact pair identity -> finitely many coordinatewise L2/Linfinity interpolations -> time Holder -> Tonelli in u`.

Theorem 3.1 replaces exactly that step by

`full original-coordinate cross bank -> regularized determinant -> fractional collision integral -> half-Riesz square smoothing`.

The order matters. The determinant theorem aggregates all bank variables before the absolute-value loss that creates the fragmented Renyi factors in the adversary. Consequently its estimate depends only on the bank singular values and not on support fragmentation, moments, connectedness, or sumset measure.

## 8. Verification, status, and next unpaid implication

Arithmetic checker: `check.py`; saved output: `check_output.txt`. It verifies `alpha=5/6`, time exponent `5/8`, the gamma constant, `C_3<17.426`, and the exact `k>=3` threshold for this splice. Saved output ends `QFORM_B03_R17_CHECK_PASS`.

No Monte Carlo or finite search is used. The changed files contain mathematical text/code only; a manual narrow review found no credentials, scheduler IDs, machine paths, signed URLs, unrelated private material, or public-release action.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** NOT PROVED by this theorem.  
**First unpaid implication for B03:** treat the genuinely low-cross-rank residual left after a useful scalar pivot, especially the two-effective-direction endpoint, without reverting to the refuted fixed-coordinate Tonelli/Holder/Plancherel closure. A plausible next mechanism is signed-Fejer or translation-uniform fractional-trace synthesis on the whole two-direction bank, preserving original-coordinate product provenance.
