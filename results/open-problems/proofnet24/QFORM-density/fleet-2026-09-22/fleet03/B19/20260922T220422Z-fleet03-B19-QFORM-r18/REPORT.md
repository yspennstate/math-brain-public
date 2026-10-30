SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B19, 2026-09-22T22:04:22Z.
attacking: the diffuse aggregate principal-triple bank — pay the fully delocalized rank-one-bank endpoint without selecting any physical triple.

# fleet03/B19 r18 — aggregate determinant payment for three rank-one product banks

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Universal proof assembly  
**Owner control:** revision `2026-09-22.15`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_TARGET-LEVEL BRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`).

## 1. Live proof boundary

The unrestricted target is unchanged: independent original real coordinates, every marginal density bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and one universal bound for the essential density of `X^T A X`.

This run does not use the refuted arbitrary-joint rank-three coarea claim, conditional projection-density moments, post-rotation independence, law-uniform pointwise Fresnel decay, a worst-fiber supremum, one-good-minor selection, or the false assertion that a normalized tri-bank cross core by itself absorbs arbitrary within-bank curvature.

The fresh synthesis input is fleet03/B10 r19, `QFORM-NEARSPAN-TO-O3-AGGREGATE-v1`. In its heavy-null exact-rank-three near-span state it proves that a genuinely diffuse *aggregate* physical principal-triple bank retains a universal amount of determinant mass even when every individual triple can be tiny. The analytic debt is to pay such determinant mass before reciprocal localization.

This run changes mechanism accordingly: instead of selecting one triple, it scalarizes whole disjoint original-coordinate banks whenever their spectral row spans are one-dimensional.

## 2. A deterministic random-split compiler

Suppose an exact-rank-three factorization is

`A=R M R^T`, `R^T R=I_3`,

and let `u_i` denote row `i` of `R`. For disjoint original-coordinate banks `J,K`, define the mixed principal-determinant mass

`mu_21(J,K)=sum_{i<j in J, k in K} |det A_{ {i,j,k},{i,j,k} }|`.

Because

`det A_I = det(M) det(R_I)^2`,                                  (2.1)

every summand has the same sign before taking absolute values.

### Lemma 2.1 — `QFORM-O3-RANDOM-TRIBANK-SPLIT-v1`

There is a partition `J=J_1 disjoint_union J_2` such that

`sum_{i in J_1, j in J_2, k in K} |det A_{ {i,j,k} }|
 >= (1/2) mu_21(J,K)`.                                          (2.2)

The analogous statement holds for a `1J+2K` bank.

**Proof.** Color every coordinate of `J` independently red/blue with probability `1/2`. Each unordered pair `{i,j}` is separated with probability `1/2`. A separated pair contributes its determinant exactly once to the red-blue sum. Taking expectation gives `mu_21/2`, so one coloring attains at least the expectation. No variable is rotated; the resulting banks remain disjoint original-coordinate product banks. QED.

In particular, the B10 near-span lower bound `mu_21>=1/256` (or its `mu_12` analogue) yields a disjoint three-bank determinant packet of mass at least

`mu >= 1/512`.                                                    (2.3)

This split alone is not claimed to solve a general tri-bank packet; the live tri-bank leakage correction forbids that inference.

## 3. New theorem: whole-bank payment at the rank-one endpoint

### Theorem 3.1 — `QFORM-THREE-RANKONE-BANK-AGGREGATE-PAYMENT-v1`

Let `A=RMR^T` have rank exactly three with `R^T R=I_3` and nonsingular symmetric `M`. Partition a set of original coordinates into four disjoint parts

`G_1, G_2, G_3, H`.

Assume that for each `a=1,2,3` the spectral rows in `G_a` are all collinear:

`u_i = c_i^(a) v_a`, `i in G_a`,                                (3.1)

where `v_a` is a unit vector and

`lambda_a = sum_{i in G_a} (c_i^(a))^2 >0`.                      (3.2)

No assumption is made on the rows in `H`. Put

`mu = sum_{i in G_1,j in G_2,k in G_3}
          |det A_{ {i,j,k},{i,j,k} }|`.                          (3.3)

If `mu>0`, then for arbitrary independent cap-one input densities the quadratic form `Q=X^TAX` has an essentially bounded density and

`boxed( ||p_Q||_infinity <= 64 sqrt(10) mu^(-1/3). )`            (3.4)

No moment, support, connectedness, log-concavity, or identical-law assumption is used.

### Proof

Condition on every original coordinate in `H`. This is legitimate product conditioning. The conditioned coordinates generate only an affine perturbation of the active three-bank quadratic form.

For each bank define the normalized original-coordinate linear form

`L_a = lambda_a^(-1/2) sum_{i in G_a} c_i^(a) X_i`.              (3.5)

The three `L_a` are genuinely independent because the banks are disjoint. Their coefficient vectors have Euclidean norm one, so the sharp Rogozin--Ball one-dimensional product-projection estimate gives

`||p_{L_a}||_infinity <= sqrt(2)`.                               (3.6)

Let `V=[v_1 v_2 v_3]` and `D=diag(sqrt(lambda_1),sqrt(lambda_2),sqrt(lambda_3))`. The active spectral projection is

`R^T X_active = V D L`,                                         (3.7)

so, after the conditioning on `H`,

`Q = L^T B L + 2 ell^T L + q_0`,
`B = D V^T M V D`.                                               (3.8)

By (2.1) and (3.1),

`|det B|
 = |det M| lambda_1 lambda_2 lambda_3 det(V)^2
 = mu`.                                                          (3.9)

This equality is the key aggregate step: `mu` may be spread over arbitrarily many vanishing physical triples, but after whole-bank scalarization it becomes the determinant of one three-variable quadratic matrix with no loss.

Set `Y_a=sqrt(2)L_a`. By (3.6), the `Y_a` are independent cap-one variables. In `Y` coordinates the quadratic matrix is `B/2`, hence

`|det(B/2)| = mu/8`.                                             (3.10)

Apply the completed `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1` theorem (fleet03/B14) in its three-independent-variable affine form:

`||p||_infinity <= 32 sqrt(10) |det(B/2)|^(-1/3)`.               (3.11)

Equations (3.10)--(3.11) give

`||p_{Q | X_H}||_infinity
 <=32 sqrt(10) (mu/8)^(-1/3)
 =64 sqrt(10) mu^(-1/3)`.                                       (3.12)

The bound is uniform in the conditioned values. Averaging the conditional densities proves (3.4). QED.

The proof never declares the eigen-coordinates independent. Independence is used only after disjoint *original-coordinate* banks have been compressed into one scalar each.

## 4. Direct application to the new B10 O3 currency

Suppose the B10 near-span compiler lands in the mixed bank with mass at least `1/256`. Lemma 2.1 supplies a disjoint three-bank packet with

`mu >=1/512`.                                                     (4.1)

If those three resource-carrying bank row spans are one-dimensional, Theorem 3.1 gives the completely explicit target bound

`||p_Q||_infinity
 <=64 sqrt(10) (1/512)^(-1/3)
 =512 sqrt(10)
 =1619.086162006210...`.                                         (4.2)

The numerical value is not intended to be sharp. The point is qualitative and dimension-free: a determinant resource distributed over `m^3` physical triples, each of size `O(m^-3)`, is paid without ever inverting one of those atoms.

### Flat diffuse witness

Take three disjoint banks of `m` physical coordinates and rows

`u_i=m^(-1/2)e_a` in bank `a`, `a=1,2,3`,                       (4.3)

with `M=diag(1,1,-1)`. Every cross-bank physical principal triple has determinant magnitude `m^-3`, so no fixed physical triple survives as `m->infinity`, while

`mu = m^3 m^-3 =1`.                                             (4.4)

Theorem 3.1 nevertheless gives the uniform bound

`||p_Q||_infinity <=64 sqrt(10) <202.386`                       (4.5)

for every `m` and every admissible product input law. This is the canonical diffuse principal-determinant phenomenon the aggregate route is designed to retain.

## 5. Required designated-partner application

The designated partner fleet04/B19 proved `QFORM-FINITE-UNION-CORE-v1`: the exact concentration seminorm over arbitrary cap-one product densities equals the supremum over bounded finite-union unit-measure product indicators, with no constant loss.

Apply it to the actual inequality (4.2). On the finite-union product core, Sections 3--4 prove

`P{Q in I} <= 512 sqrt(10) |I|`                                 (5.1)

for every interval `I` in the B10 rank-one-bank endpoint. The partner theorem transfers (5.1), unchanged, to **all** independent one-dimensional probability densities satisfying `0<=f_i<=1`. Thus the finite-union testing reduction and the whole-bank determinant payment splice exactly; no compact-support assumption leaks into the owner quantifiers.

(The direct Rogozin--Ball proof above already works for arbitrary laws; the partner application independently verifies the constant-preserving quantifier transfer required by the assignment.)

## 6. What remains

The full QFORM conjecture is still **OPEN / NOT PROVED / NOT DISPROVED**. A continuous representative is also not established by Theorem 3.1; only an essentially bounded density is claimed.

The B10 near-span structural debt is now narrower. After the random split, a diffuse O3 packet is paid whenever each of the three resource-carrying spectral bank spans has rank one. Consequently the first unpaid interface on this line is

`QFORM-O3-INTERNAL-RANK2-ROUTING-v1`:

> Starting from a disjoint three-bank O3 packet with aggregate determinant mass bounded below (in the B10 branch, at least `1/512`), and with at least one resource-carrying bank having genuine spectral rank at least two, exploit that internal two-dimensional wedge before any reciprocal physical-minor cost; route it to a proved ridge/cross-rank/grouped-square mechanism or prove a direct product-preserving trace bound. The argument must remain uniform as the second bank singular value tends to zero, because Theorem 3.1 pays the exact rank-one boundary but coefficient-small perturbation is invalid under unrestricted supports.

This is a strict narrowing of the diffuse aggregate principal-triple debt and avoids the fresh tri-bank-core-overclaim correction: no assertion is made that the aggregate core alone controls arbitrary within-bank curvature.

## 7. Source pins

- fleet03/B10 near-span aggregate compiler: `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260922T214631Z-fleet03-B10-QFORM-r19/REPORT.md` (current source-pinned copy read this run).
- fleet03/B14 determinant-localization theorem: `QFORM-PRINCIPAL-TRIPLE-DETERMINANT-LOCALIZATION-v1`, canonical source previously pinned by the fleet at `yspennstate/math-open-problems@89e6481f4f7ed7d49a77cfcb989ee93572d5d5cd`.
- fleet04/B18 Rogozin--Ball product-projection transfer: `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.
- designated partner fleet04/B19: `QFORM-FINITE-UNION-CORE-v1`, `yspennstate/math-open-problems@02171dc794a56c0235afb1ca394b3e614162bff4`.

Repository reads/writes are not native learned-memory ingestion; this run remains `WITHOUT_VERIFIED_BRAIN`.
