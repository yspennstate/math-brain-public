SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B13, 2026-09-23T17:33:17Z.
attacking: upgrade the physical-cut third-singular-value estimate to a bound on the complete third exterior-volume currency, then feed that aggregate currency into the skeleton identity to force a dimension-free diagonal-plus-rank-eight reduction for every sufficiently concentrated slab.

# account03/B13 r30 — aggregate third-volume control and a diagonal-plus-rank-eight high-concentration reduction

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **NEW CONDITIONAL TARGET-LEVEL IMPLICATIONS / FULL QFORM OPEN / FULL CONTINUITY OPEN**. The only non-reviewed dependency newly inherited from r29 is the source-pinned grouped projected-crossing receiver described below. No post-rotation independence, moment, support, connectedness, interval-extremality, or perturbative deletion assumption is used.

## 1. Fresh sources actually used

### 1.1 Designated partner: exact no-attainment product purification

`yspennstate/math-open-problems@e1a56859520ae79b7a1f049a9eedf41972ddf1e1`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B13/20260922T231352Z-account04-B13-rough-geometric-transfer-r5/REPORT.md`.

For every bounded nonnegative product kernel, the supremum over cap-one mass-one product densities equals the supremum over products of indicators of unit-measure sets, and the latter may be approximated by bounded finite unions of intervals. No optimizer, common diameter, fragment-count bound, single interval, or centered uniform law is asserted.

### 1.2 The physical-third-volume ingredients

Account02/B13:

`yspennstate/math-open-problems@f6ad7b994c1ba509af30fceaf45e8b464db86af8`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B13/20260923T155736Z-account02-B13-rank4star-r30/REPORT.md`.

For an original-coordinate physical cross block `B=A[L,R]`, set

`Z=e_3(B^T B)=sum_{|S|=|T|=3} det(B[S,T])^2`.

If all natural squared-third-minor row marginals are at most `2/3`, its source-pinned `D'` estimate gives

`rho <= C3 Z^(-1/6),      C3=9 sqrt(3e)=25.70102107534928...`,       (1.1)

where `rho=P{Q in J}/|J|`. The same statement applies to `B^T`, hence to column marginals.

My preceding r29 volume cascade:

`yspennstate/math-open-problems@c9a6c9160e063f07856a62fc89a2ba62b857d3cf`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T165827Z-account03-B13-qform-r29/{REPORT.md,POSTREFRESH_ADDENDUM.md}`.

It proves the following extracted implication. If a physical row `i` and physical column `j` have third-minor marginals exceeding `2/3`, let `Z_ij` be the squared-third-minor mass containing both. Then `Z_ij>Z/3`; and, conditional only on the grouped projected-crossing receiver,

`Z_ij^(1/6) > kappa/rho` is impossible,                         (1.2)

where

`kappa=C3/3^(1/6)=3^(7/3) sqrt(e)=21.4008078980155...`.          (1.3)

The proof of (1.2) is the r29 original-coordinate 1-hub/2-cross -> 2-hub/1-cross -> 3-hub cascade. The post-refresh addendum makes the essential conditioning explicit: before the first two receiver applications all original coordinates outside `L union R` are conditioned, so the projected crossing matrices and their volume marginals are exactly those used in the gates.

The still-pending receiver used by that cascade is the complete written supporting theorem at

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

It awaits independent review; therefore every result below that invokes (1.2) retains that condition.

### 1.3 Skeleton identity and localized physical-triple compiler

The deterministic skeleton theorem is in the current Claude continuation

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/structure/REPORT.md`.

With

`V_r(A)=sum det(A[S,T])^2`

over ordered disjoint `r`-sets `S,T`, its Corollary 3.2 states:

if `V_{r+1} <= K V_r`, then

`A=D+R+E`, `rank(R)<=4r`, `E` zero-diagonal, and

`||E||_F <= 3(r+1) sqrt(K)`.                                      (1.4)

The localized original-coordinate triple theorem is my r24 report

`yspennstate/math-open-problems@b097dc81bae17477b60c3af1a56dc6e434f9998f`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260923T103046Z-account03-B13-qform-r24/REPORT.md`.

If a physical `3 x 3` principal block has smallest singular value at least `s>0`, then the full ambient form has

`||p_Q||_infinity <= C0/s`,

`C0=128*2^(1/4)=152.2185107203483...`.                            (1.5)

All outside couplings and affine terms are retained in (1.5).

## 2. First new theorem: the complete third exterior volume is small on every physical cut

### Theorem 2.1 — `QFORM-AGGREGATE-CROSS-E3-SLAB-v1`

Assume the projected-crossing receiver entering (1.2). Let `J` be any interval of positive length, let

`rho=P{X^T A X in J}/|J|`,

and let `B=A[L,R]` be **any** disjoint original-coordinate cross block. Then

`boxed: e_3(B^T B) <= (C3/rho)^6.`                                (2.1)

#### Proof

Put `Z=e_3(B^T B)`. If `Z=0` there is nothing to prove. Suppose for contradiction that

`Z>(C3/rho)^6`.                                                    (2.2)

If every row marginal of the squared-third-minor law were at most `2/3`, (1.1) would imply

`rho<=C3 Z^(-1/6)<rho`,

a contradiction. Hence some row `i` has marginal `>2/3`.

Apply the same argument to `B^T`. Since its `e_3` is the same `Z`, some physical column `j` has marginal `>2/3`. By inclusion-exclusion under the same normalized squared-minor law,

`Z_ij/Z > 1/3`, hence `Z_ij>Z/3`.                                 (2.3)

Using (2.2),

`Z_ij^(1/6) > Z^(1/6)/3^(1/6)
              > C3/(3^(1/6) rho)
              = kappa/rho`.                                      (2.4)

But (2.4) is exactly the impossible anchored-volume threshold (1.2). Contradiction. Thus (2.1) holds. QED.

### Why this is stronger than the preceding `s_3` estimate

The earlier r29 statement gave `s_3(B)<=C3/rho`. Equation (2.1) controls the **sum of every squared physical 3x3 cross minor simultaneously**. It does not select or invert one tiny minor, and it does not lose a dimension factor.

## 3. Global aggregate disjoint-minor currency

For a uniformly random Bernoulli partition of the original coordinate labels into `(L,R)`, every ordered disjoint triple pair `(S,T)` lands with `S subset L`, `T subset R` with probability `4^-3=1/64`. By Cauchy--Binet,

`e_3(A[L,R]^T A[L,R])
 =sum_{S subset L,T subset R, |S|=|T|=3} det A[S,T]^2`.

Taking expectations and using (2.1) for **every** cut gives

`E e_3(A[L,R]^T A[L,R]) = V_3(A)/64
                         <= (C3/rho)^6`.

Hence

`boxed: V_3(A) <= 64 C3^6 rho^(-6).}`                             (3.1)

Numerically `C3^6=2.882055013558859e8`; the proof uses the exact symbolic constant.

This is the first point where the high slab ratio is converted into a dimension-free bound on a **global algebraic currency of A**, rather than only a per-cut singular value.

## 4. Second new theorem: high concentration forces diagonal plus bounded rank plus an O(1/rho) Frobenius twist

Recall

`V_1(A)=sum_{i!=j} a_ij^2 = ||A-diag(A)||_F^2`.                   (4.1)

### Theorem 4.1 — `QFORM-HIGHRATIO-DIAGONAL-RANK8-FROBENIUS-REDUCTION-v1`

Assume A has at least three eigenvalues of absolute value at least one, and assume the projected-crossing receiver entering Theorem 2.1. For any slab with ratio

`rho > C0+2`,                                                     (4.2)

there are a diagonal matrix `D`, a matrix `R` of rank at most eight, and a zero-diagonal residual `E` such that

`boxed: A=D+R+E,     ||E||_F <= K0/rho,}`                          (4.3)

with

`K0=72 C3^3 = 1,222,316.37436014...`.                             (4.4)

More precisely, one of the first two alternatives below occurs:

(A) `V_2(A)>=rho^-4`, in which case `rank R<=8` and (4.3) holds;

(B) `V_2(A)<rho^-4` and `V_1(A)>=rho^-2`, in which case one has the much stronger `rank R<=4` and `||E||_F<6/rho`.

The apparent third alternative `V_1(A)<rho^-2` is impossible under (4.2).

#### Proof

**Case A: `V_2>=rho^-4`.** From (3.1),

`V_3/V_2 <= 64 C3^6 rho^-2`.                                     (4.5)

Apply the skeleton theorem (1.4) with `r=2` and

`K=64 C3^6 rho^-2`.

It gives `rank R<=8` and

`||E||_F
 <=9 sqrt(K)
 <=9*8*C3^3/rho
 =72 C3^3/rho`.                                                    (4.6)

This is (4.3).

**Case B: `V_2<rho^-4` but `V_1>=rho^-2`.** Then

`V_2/V_1 < rho^-2`.                                                (4.7)

Apply (1.4) with `r=1`. We obtain `rank R<=4` and

`||E||_F < 6/rho`.                                                 (4.8)

**Case C: `V_1<rho^-2`.** Put `D_0=diag(A)` and `O=A-D_0`. Then

`||O||_op <= ||O||_F=sqrt(V_1)<1/rho`.                            (4.9)

Since A has at least three eigenvalues with modulus at least one, its third singular value satisfies `s_3(A)>=1`. Singular-value perturbation gives

`s_3(D_0) >= s_3(A)-||O||_op > 1-1/rho`.                          (4.10)

The singular values of the diagonal matrix `D_0` are the absolute diagonal entries. Therefore there are three original indices `I` such that

`|a_ii|>1-1/rho` for all `i in I`.                                (4.11)

On the physical principal block,

`A[I,I]=D_0[I,I]+O[I,I]`,

so another singular-value perturbation gives

`sigma_min(A[I,I]) > 1-2/rho`.                                   (4.12)

By the localized compiler (1.5),

`rho <= ||p_Q||_infinity
     <= C0/sigma_min(A[I,I])
     < C0/(1-2/rho)`.                                             (4.13)

Thus `rho-2<C0`, contradicting (4.2). Hence Case C cannot occur. Cases A and B prove the theorem. QED.

### Scaling and scope check

The powers are dimensionally consistent: under `A -> tA`, `rho -> rho/|t|`, `V_r -> |t|^(2r)V_r`, and the residual bound scales by `|t|`. No support radius is used. The residual is **not** deleted from the quadratic form; (4.3) is a deterministic coefficient-matrix conclusion only.

## 5. Actual use of the designated account04/B13 extremal-product theorem

To make the extremal-product step explicit, first prove Theorem 2.1 for bounded finite-union unit product indicators. Its geometric conclusion is

`|{x in prod_i E_i : x^T A x in J}|/|J| = rho`

` ==> e_3(A[L,R]^T A[L,R]) <= (C3/rho)^6`                         (5.1)

for every physical cut `(L,R)`.

Now suppose an arbitrary admissible product density gave a strict violation of (5.1), with slab ratio `rho_0`. Because the inequality is strict, choose `eta>0` so small that the same matrix still violates

`e_3(B^TB) <= (C3/(rho_0-eta))^6`.                                (5.2)

The account04/B13 no-attainment theorem supplies a bounded finite-union unit-product indicator with the **same A and J** and slab ratio at least `rho_0-eta`. Applying the indicator version of Theorem 2.1 contradicts (5.2). Letting the strict margin tend to zero proves (2.1) for the complete cap-one product class, with zero constant loss.

Equations (3.1) and (4.3) are then deterministic consequences of (2.1), so the same transfer applies to them. This is an application to the actual new aggregate-third-volume inequality. It uses neither interval extremality nor an attained product optimizer.

## 6. What this does and does not close

The full QFORM conjecture is still **OPEN**. Full continuity is also **OPEN**. Theorem 4.1 gives a new dimension-free global reduction:

> any slab witness with ratio `rho>154.219` must have its coefficient matrix within `O(1/rho)` in Frobenius norm of `diagonal + rank <= 8`.

The remaining step is not allowed to simply erase `E`: arbitrary cap-one laws can have unbounded and highly fragmented support. The next B13 obligation is therefore

`QFORM-DIAG-RANK8-SMALL-FROBENIUS-TWIST-GLUE-v1`:

combine (4.3) with the existing exact diagonal/bounded-rank hub mechanisms and the slab-conditioned-core transfer. On a purified finite-union witness the latter rigorously charges `y^T E y` by core geometry; either the exact `D+R` model inherits a high-ratio slab, or a positive fraction of the slab mass is forced onto quantitatively large core spread. The proof must exploit that spread through product geometry rather than assume a uniform support diameter.

A second exact consequence worth retaining is that a hypothetical sequence with slab ratios `rho_m -> infinity` must satisfy simultaneously

`V_3(A_m)=O(rho_m^-6)`

and

`dist_F(A_m, {diagonal + rank<=8})=O(rho_m^-1)`,                  (6.1)

subject to the single pending projected-crossing receiver review stated above.

## 7. Arithmetic diagnostics

`C3 = 9 sqrt(3e) = 25.70102107534928...`

`kappa = C3/3^(1/6) = 21.40080789801550...`

`C0 = 128*2^(1/4) = 152.2185107203483...`

`64 C3^6 = 1.84451520867767e10`.

`K0 = 72 C3^3 = 1.22231637436014e6`.

The exact symbolic forms, not decimal rounding, are used in the proof.

## 8. Source/control integrity


Repository source use does not establish native brain ingestion. This run remains `WITHOUT_VERIFIED_BRAIN`.
