# account03/B19 — universal proof assembly: zero-diagonal remainder sharpens the low-offdiagonal barrier to 1/2

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Run:** `20260922T170047Z-account03-B19-QFORM-r15`  
**Owner control at prepublication refresh:** revision `2026-09-22.8`  
**Status:** `ESSENTIAL_STEP_APPLIED / TARGET_LEVEL_BRANCH_PROVED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and scope

Let `X=(X_1,...,X_n)` have independent real coordinates, each with a probability density `0<=f_i<=1`, and let `A` be real symmetric with at least three eigenvalues of modulus at least one. The target asks for one dimension-, law-, sign-, and matrix-independent finite bound on the essential supremum of the density of

`Q=X^T A X`.

Continuity is a separate desired conclusion. The theorem proved below gives essential boundedness on a new target-level branch; it does not prove continuity there and does not prove the unrestricted conjecture.

No rotation of the product law, no pointwise law-uniform van-der-Corput bound, no conditional-density-cap surrogate, no support/moment/log-concavity assumption, and no fixed-good-minor assertion is used.

## 2. Completed inputs used

### 2.1 Fresh universal-assembly input from account01/B19

Source: `yspennstate/math-open-problems@46d99d0364a9bf15376b5c8875cdd321373ba75c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B19/20260922T165145Z-b19-qform-r11/REPORT.md`.

That report proves two local payments needed below.

1. **Opposite physical diagonals.** If two original coordinates satisfy, after possibly replacing `A` by `-A`,

   `A_ii=a>=m`, `A_jj=-b<=-m`, `m>0`,

   then

   `||p_Q||_infinity <= 50 m^(-3/4)`.                         (2.1)

   The proof uses the exact physical two-coordinate indefinite pivot, the B19 quarter-kernel, rank-two Schur inheritance `s_1(S)>=s_3(A)`, and the account03/B11 one-eigenvalue quarter-Riesz theorem. It permits all outside couplings and arbitrary cap-one product laws.

2. **Definite physical pair.** If two physical diagonal entries have the same sign, magnitudes at least `m`, and `|A_ij|<=r<m`, then

   `||p_Q||_infinity <= pi/sqrt(m^2-r^2)`.                    (2.2)

The fresh report used the crude bound `|A_ij|<=2 tau` when `s_2(A-diag A)<=tau`, which imposed a `tau<1/3` barrier. The main point of the present run is that zero diagonal actually gives the sharp bound `|A_ij|<=tau`.

### 2.2 Designated partner account04/B19 applied

Source: `yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B19/20260922T122030Z-account04-B19-QFORM-r1/REPORT.md`.

Partner theorem `QFORM-FINITE-UNION-CORE-v1` says that, for every measurable map `Phi`, the supremum of interval concentration over all independent cap-one densities equals the supremum over product indicators `1_{E_i}` with each `E_i` a bounded finite union of intervals of measure one. Constants are unchanged.

In Section 5 I apply this theorem to the actual same-sign interval inequality obtained from the new sharp offdiagonal estimate. Thus no compact-support or finite-fragment assumption is added to the final statement.

## 3. New sharp zero-diagonal entry lemma

Let

`D=diag(A)`, `H=A-D`.

Then `H` is symmetric and has zero diagonal.

### Lemma 3.1 — `QFORM-ZERODIAG-TOPMODE-ENTRY-v1`

Let `H` be any real symmetric matrix with zero diagonal. Choose a top-modulus eigenpair `(lambda,v)`, `||v||_2=1`, `|lambda|=s_1(H)`, and write

`H=lambda v v^T+R`,

so `||R||_op=s_2(H)`. If `s_2(H)<=tau`, then for every `i!=j`,

`|H_ij|<=tau`.                                             (3.1)

This improves the triangle-inequality estimate `2 tau` by a factor two.

#### Proof

The case `lambda=0` is trivial. Put `sigma=sign(lambda)` and

`u_i=|lambda| v_i^2`.

Since `H_ii=0`,

`R_ii=-lambda v_i^2`,

hence `0<=u_i<=tau` because `|R_ii|<=||R||<=tau`.

All eigenvalues of `sigma R` lie in `[-tau,tau]`, so

`M=tau I+sigma R`

is positive semidefinite. Its `i`th diagonal entry is

`M_ii=tau-u_i`.

Therefore positivity of the `{i,j}` principal `2 x 2` minor gives

`|R_ij|^2 <= (tau-u_i)(tau-u_j)`.                         (3.2)

On the other hand,

`|lambda v_i v_j|=sqrt(u_i u_j)`.

Consequently

`|H_ij|`
` <= sqrt(u_i u_j)+sqrt((tau-u_i)(tau-u_j))`
` <= tau`,                                                  (3.3)

where the last step is Cauchy--Schwarz applied to the two vectors

`(sqrt(u_i),sqrt(tau-u_i))` and `(sqrt(u_j),sqrt(tau-u_j))`, each of Euclidean norm `sqrt(tau)`. QED.

### Sharpness of the lemma

For any `tau>0`, the two-coordinate matrix

`H=[[0,tau],[tau,0]]`

has `s_1(H)=s_2(H)=tau`. Choosing the `+tau` eigenvector `(1,1)/sqrt(2)` gives

`R=[[-tau/2,tau/2],[tau/2,-tau/2]]`,

and equality holds in (3.1). Thus no improvement below `tau` follows from only zero diagonal and `s_2(H)<=tau`.

## 4. Two heavy physical diagonals still follow

Let `0<=tau<1`, assume the exact owner target and

`s_2(H)<=tau`.                                               (4.1)

With the decomposition of Lemma 3.1 set

`A_0=D+lambda vv^T=A-R`.

Since `s_3(A)>=1`, Weyl's singular-value inequality gives

`s_3(A_0)>=1-tau=:m`.                                        (4.2)

A rank-one perturbation can increase singular-value counting by at most one, hence

`s_3(D+lambda vv^T)<=s_2(D)`.                                (4.3)

Therefore

`s_2(D)>=m`,                                                  (4.4)

so there exist two original coordinates `i,j` such that

`|A_ii|>=m`, `|A_jj|>=m`.                                    (4.5)

This is exactly the physical-coordinate resource required for the sign split below.

## 5. New target-level theorem: fixed thresholds below one half

### Theorem 5.1 — `QFORM-LOW-OFFDIAG-ONE-HALF-BARRIER-v1`

Fix `0<=tau<1/2`. Under the exact full target hypotheses, if

`s_2(A-diag A)<=tau`,                                        (5.1)

then `Q=X^TAX` has an essentially bounded density and

`||p_Q||_infinity <= max{
    50(1-tau)^(-3/4),
    pi/sqrt(1-2 tau)
}`.                                                           (5.2)

No continuity conclusion is asserted.

#### Proof

Let `m=1-tau` and choose the two coordinates from (4.5).

**Opposite signs.** If the two heavy diagonal entries have opposite signs, apply the completed account01/B19 opposite-diagonal payment (2.1):

`||p_Q||_infinity <=50m^(-3/4)`.                             (5.3)

**Same sign.** Suppose their signs agree. Lemma 3.1 gives

`|A_ij|=|H_ij|<=tau`.                                        (5.4)

Because `tau<1/2`,

`m=1-tau>tau`.

After a global sign change if necessary, the physical `2 x 2` pivot has both diagonal entries at least `m` and determinant at least

`m^2-tau^2=(1-tau)^2-tau^2=1-2tau>0`.                       (5.5)

For a product indicator law from the finite-union core, condition on every outside original coordinate. Those values create only an affine term in the two selected variables. Completing the square translates the positive definite quadratic. For every interval `I`, its inverse image in the selected physical plane has area at most

`pi |I|/sqrt(det B) <= pi |I|/sqrt(1-2tau)`.                 (5.6)

The conditioned two-variable product indicator density is at most one, so the same inequality bounds the conditional interval probability. Averaging gives (5.6) for every finite-union product indicator law.

Now apply the designated partner account04/B19 theorem `QFORM-FINITE-UNION-CORE-v1` with `Phi(x)=x^TAx`. It transfers the interval inequality (5.6), with **no constant loss**, to every independent cap-one product density allowed by the target. Therefore

`||p_Q||_infinity <= pi/sqrt(1-2tau)`.                       (5.7)

The two sign cases exhaust all possibilities, proving (5.2). QED.

## 6. Clean universal branch and exact arithmetic

Take the fixed target-level threshold

`tau_*=499/1000`, `m_*=501/1000`.

Then

`m_*^2-tau_*^2=1/500`.                                       (6.1)

The opposite-sign bound is

`50(1000/501)^(3/4)=83.96372739446834...`,                   (6.2)

while the same-sign bound is

`pi sqrt(500)=70.24814731040726...`.                          (6.3)

Moreover the first inequality is certified without floating-point dependence by

`(84/50)^4-(1000/501)^3`
`=675442655696/49121680078125>0`.                             (6.4)

Hence

`boxed: s_2(A-diag A)<=499/1000  ==>  ||p_Q||_infinity<84.`   (6.5)

This strictly improves the fresh account01/B19 threshold `3/10` and the preceding account03/B19 threshold `3/20`.

## 7. The one-half barrier is the actual obstruction of this mechanism

At `tau=1/2`, the information produced by Sections 3--4 permits the same-sign physical pivot data

`A_ii=A_jj=1/2`, `|A_ij|=1/2`,

for which the `2 x 2` determinant lower bound in (5.5) is zero. Thus the present two-heavy-diagonal mechanism cannot yield a uniform endpoint bound at `tau=1/2` without additional information.

This is a limitation of this proof mechanism, **not** a QFORM counterexample. The correct next step must use the third-compound / overlap structure or another aggregate resource precisely in this nearly singular same-sign geometry.

## 8. Updated compact conditional proof tree

Combining completed compatible branches gives the following compact universal assembly.

1. If the `|lambda(A)|>=1/64` spectral window is diffuse at the completed ridge threshold, the full form has a bounded continuous density (source ridge theorem; the strongest completed branch constants are <64 or <194 depending on the conditioning formulation).
2. Otherwise the existing spectral-window localization/physical-resource reductions apply.
3. If `s_2(A-diag A)<=499/1000`, Theorem 5.1 closes the exact target with `||p_Q||_infinity<84` for all arbitrary cap-one product laws.
4. Therefore every still-unpaid form must have

   `s_2(A-diag A)>499/1000`,                                 (8.1)

   while simultaneously lying in the localized/high-window residual and in one of the third-compound overlap classes O0-heavy/O1/O2/O3 supplied by the completed full-matrix overlap reduction.
5. The missing item is to turn that high-offdiagonal aggregate resource into one already-paid product-coordinate smoothing packet without selecting a reciprocal tiny minor.

No step above treats a rotated eigen-coordinate law as independent.

## 9. First essential missing implication

The first unpaid implication is now

`QFORM-HALF-OFFDIAGONAL-OVERLAP-PAYMENT-v1`:

> For target matrices satisfying `s_2(A-diag A)>499/1000`, together with the surviving spectral-window localization/physical-resource condition and the full third-compound O0-heavy/O1/O2/O3 alternative, prove a universal product-preserving smoothing bound. In the near-endpoint same-sign branch, the two heavy physical diagonals form an almost rank-one positive/negative plane; use the third-compound mass to force either a transverse grouped coordinate, a paid ridge bank, or overlap transfer before any reciprocal local-minor payment.

The immediate O0-heavy subproblem is especially concrete: the calibrated ridge/DPP reduction already supplies an original-coordinate row carrying more than half of the regularized determinant weight. Combine that row with the nearly singular heavy physical pair. If the resources are transverse, extract a grouped rank-two-plus-square or ridge packet; if they coincide, condition the shared physical coordinate and transfer a fixed amount of third-compound mass into O1/O2/O3. The live corrections rule out demanding one fixed good minor and rule out replacing the residual product law by a conditional density cap.

## 10. Corrections respected and status

Respected live corrections include: no law-uniform pointwise Fresnel decay; no conditional-cap-as-independence step; no fixed good cross minor/triple; no unrestricted fiber supremum; no same-sign Pluecker/full-pivot identification; no bare 3D `L^infinity` coarea surrogate; and no one-pair normalized TT* integration over fragmented supports.

**Proved here:** Lemma 3.1 and Theorem 5.1, in their full stated quantifier scope, plus the fixed branch (6.5).  
**Continuity:** not proved on this new branch.  
**Full QFORM:** `OPEN / NOT PROVED / NOT DISPROVED`.  
**Native brain ingestion:** not verified; repository retrieval/write does not change `WITHOUT_VERIFIED_BRAIN`.
