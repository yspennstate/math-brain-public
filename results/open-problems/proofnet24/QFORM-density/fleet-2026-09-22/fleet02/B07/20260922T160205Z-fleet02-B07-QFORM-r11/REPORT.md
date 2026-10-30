# fleet02/B07 — exterior-power transfer of Pluecker packet mass through arbitrary extra spectrum

**Run:** `20260922T160205Z-fleet02-B07-QFORM-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** Coordinate minor selection / complementary constructions and source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Target, corrections, and first unpaid implication

The full target remains open: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of absolute value at least one, prove a universal essential density bound for `X^T A X`, or produce a valid target-level counterexample.

I use no moment, support, Gaussian, log-concavity, post-rotation independence, pointwise law-uniform Fresnel decay, fiber-supremum, or single-good-minor hypothesis. I retain the live corrections that a fixed local cross minor, a single Schur rank-two extraction, or a good selected-core principal minor need not survive arbitrary complementary spectrum. I also consumed the newer fleet02/B06 correction `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`: same-sign Pluecker support can be disjoint from the support of useful physical pair determinants. The mechanism below does not identify these supports; it transfers the entire determinant energy through `wedge^3 A` before selecting an overlap stratum.

The incoming B07 debt was `QFORM-STRATUM-PACKET-NONSEPARABLE-TRANSFER-v1`: a selected three-large-eigenvalue frame may carry at least constant Pluecker mass in a coordinate packet, but arbitrary orthogonal spectral complement can cancel every corresponding physical principal minor. The exact stress matrix from the previous run was `A=I_4-J_4/3`, with spectrum `{1,1,1,-1/3}`: all selected-core triple weights are `1/4`, yet all physical principal `3x3` determinants vanish.

## 2. Exterior-power packet transfer theorem

Let `A` be real symmetric. Choose orthonormal eigenvectors `U=(u^(1),u^(2),u^(3)) in R^{n x 3}` with eigenvalues `lambda_1,lambda_2,lambda_3` satisfying `|lambda_a|>=1`. Put

`d=lambda_1 lambda_2 lambda_3`,

and for every physical coordinate triple `I` define the signed Pluecker coordinate

`p_I=det(U_I)`, `w_I=p_I^2`.

Cauchy--Binet gives

`sum_{|I|=3} w_I=det(U^T U)=1`.                                      (2.1)

Let `B=wedge^3 A`, indexed by coordinate triples, so

`B_{I,J}=det(A_{I,J})`.                                               (2.2)

Because `A U=U diag(lambda_1,lambda_2,lambda_3)`, functoriality of the exterior power gives the exact eigenvector identity

`sum_J det(A_{I,J}) p_J = d p_I`                                     (2.3)

for every row triple `I`.

### Theorem 2.1 — `QFORM-EXTERIOR-PACKET-ENERGY-TRANSFER-v1`

For every family `R` of coordinate triples,

`sum_{I in R} sum_J det(A_{I,J})^2
   >= d^2 sum_{I in R} w_I
   >= sum_{I in R} w_I`.                                              (2.4)

Equivalently,

`sum_{I in R} det((A^2)_{I,I}) >= d^2 sum_{I in R}w_I`.                (2.5)

If for `q=0,1,2,3` one defines the overlap-stratum energies

`E_q(R)=sum_{I in R} sum_{J:|I cap J|=q} det(A_{I,J})^2`,              (2.6)

then

`max_q E_q(R) >= (d^2/4) sum_{I in R}w_I`.                            (2.7)

Thus any selected-core Pluecker packet of mass `m` forces an **actual full-matrix** determinant-energy packet of size at least `m/4` in one of only four original-coordinate overlap types, regardless of all other eigenvalues and eigenvectors.

### Proof

For fixed `I`, apply Cauchy--Schwarz to (2.3) and use (2.1):

`d^2 p_I^2
 <= (sum_J det(A_{I,J})^2)(sum_J p_J^2)
 = sum_J det(A_{I,J})^2`.                                             (2.8)

Sum over `I in R` to obtain (2.4). The identity in (2.5) is Cauchy--Binet applied to the `3 x n` row submatrix `A[I,:]`:

`det(A[I,:] A[I,:]^T)=sum_J det(A_{I,J})^2`,

and symmetry gives `A[I,:]A[I,:]^T=(A^2)_{I,I}`. Finally the four classes in (2.6) partition all column triples, so one carries at least one fourth of the total in (2.4). QED.

The point of (2.4) is that the complementary spectrum is not treated as noise and is not asked to preserve one principal minor. It may redistribute determinant mass among column triples and among the four overlap classes, but it cannot destroy the total packet energy inherited from the three selected large eigenvalues.

## 3. Immediate application of the preceding B07 packet collar

The previous fleet02/B07 theorem `QFORM-PLUCKER-STRATUM-COLLAR-v1` showed that in the localized exceptional branch there is a family `R` of selected-core triples with

`sum_{I in R}w_I >= 1/8`,                                             (3.1)

with packet type `1+2`, `2+1`, or a literal physical triple.

Theorem 2.1 now gives, for the **full** `A`,

`sum_{I in R}sum_J det(A_{I,J})^2 >= 1/8`,                            (3.2)

and some overlap class obeys

`E_q(R)>=1/32`.                                                        (3.3)

This is the missing cancellation-safe structural transfer. It does not yet pay the quadratic-form density analytically, because (3.3) is an aggregate squared-minor resource rather than one uniformly good minor.

## 4. Direct application of the designated partner fleet03/B07

I consumed fleet03/B07 `QFORM-NESTED-HEAVY-DISJOINT-BANK-COLLAR-v1`, canonical source `yspennstate/math-open-problems@494c999fc67d230fff7e2079b1867216253b35bc`, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260922T154026Z-fleet03-B07-qform-r11/REPORT.md`.

In its nested-heavy rank-three state, the two selected physical rows `i,j` have leverage parameters `c>1/2`, `h>1/2`. Therefore the fixed-pair Pluecker packet

`R_{ij}={ {i,j,k}: k notin {i,j} }`

has total mass

`sum_{k}w_{ijk}=det Gram(u_i,u_j)=c h >1/4`.                          (4.1)

Applying Theorem 2.1 before discarding the complementary spectrum gives the full-matrix certificate

`sum_k sum_J det(A_{ {i,j,k},J})^2 >1/4`,                             (4.2)

so for some `q in {0,1,2,3}`,

`E_q(R_{ij})>1/16`.                                                    (4.3)

In the partner's two-coloop alternative with `eta=1/16`, it proves `c h>3/4`; then the corresponding full-matrix overlap class satisfies

`E_q(R_{ij})>3/16`.                                                    (4.4)

This is an actual use of the completed partner theorem: its quantitative nested-heavy/two-coloop packet is now promoted to a cancellation-safe full-spectrum determinant certificate. The partner's stable disjoint-bank alternative remains analytically relevant, but arbitrary extra spectrum can no longer be said to erase all determinant resource.

## 5. A literal triple: exact self/cross decomposition

If the selected packet is a single physical triple `I` with `w_I>=1/8`, write

`D=A[I,I]`, `C=A[I,I^c]`.

Then

`det(D^2+CC^T)=det((A^2)_{I,I})>=1/8`.                               (5.1)

More precisely, Cauchy--Binet with a scalar weight on outside columns gives the polynomial identity

`det(D^2+t CC^T)=E_3(I)+t E_2(I)+t^2 E_1(I)+t^3 E_0(I)`,              (5.2)

where

`E_q(I)=sum_{J:|I cap J|=q}det(A_{I,J})^2`.                           (5.3)

Hence at least one coefficient is at least `1/32`. The endpoints have familiar meanings:

* `E_3(I)=det(D)^2` (principal triple);
* `E_2(I)=||adj(D) C||_F^2` (two self columns plus one outside column);
* `E_0(I)=det(CC^T)` (three-column disjoint cross volume);
* `E_1(I)` is the aggregate one-self/two-cross mixed discriminant.

So cancellation of the principal triple necessarily moves the selected spectral determinant resource into one of the mixed or cross overlap strata.

## 6. Exact stress test: the old cancellation example is absorbed structurally

Take the previous exact target matrix

`A=I_4-J_4/3`

and select the three `+1` eigenvectors spanning the orthogonal complement of `(1,1,1,1)/2`, using a normalized Hadamard frame. Then `d=1` and every selected-core triple has `w_I=1/4`.

The accompanying exact `Fraction` checker verifies:

* every row-triple full-minor energy is `sum_J det(A_{I,J})^2=1/3`;
* every principal `3x3` determinant vanishes;
* for every row triple, **all** of its `1/3` energy is in overlap class `q=2`;
* for the fixed pair `{0,1}`, its two-triple Pluecker packet has mass `1/2`, total full-minor energy `2/3`, again entirely in `q=2`.

Thus the matrix that refuted selected-core-principal-minor transfer is not an obstruction to Theorem 2.1; it exhibits precisely why the overlap decomposition is necessary.

Exact checker terminal output:

`QFORM_EXTERIOR_PACKET_TRANSFER_CHECK_PASS`

with the rational certificate recorded in `CHECK_OUTPUT.txt`.

## 7. New first unpaid implication

The structural cancellation debt is replaced by the sharper analytic obligation

`QFORM-OVERLAP-STRATUM-ANALYTIC-PAYMENT-v1`:

> Suppose a selected row-triple packet `R` carries one actual full-matrix overlap energy `E_q(R)>=c` with universal `c>0` (in the generic preceding collar, `c=1/32`; in the partner nested-heavy state, `c>1/16`; in its two-coloop subcase, `c>3/16`). Convert this **aggregate squared-minor** resource into a dimension-free small-ball/density bound while preserving the original-coordinate product law and without replacing the aggregate by one tiny minor.

The four cases are geometrically distinct. `q=0` is a disjoint rank-three cross-volume bank; `q=3` is principal-triple energy; `q=1,2` are mixed self/cross resources, and the live stress matrix `I_4-J_4/3` lands purely in `q=2`. Existing single-pivot or fixed-cross-block theorems do not by themselves pay an arbitrary aggregate `q=1` or `q=2` packet, and the recent B06 correction forbids silently identifying Pluecker support with physical pivot support.

This is a strict narrowing: arbitrary extra spectrum can redistribute selected rank-three determinant mass but cannot annihilate it. Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`.

## 8. Source ledger

Fresh brain control during this run remained owner revision `2026-09-22.5` with no later B07 stop observed before publication.

Consumed mathematical sources:

1. fleet02/B07 previous report `yspennstate/math-open-problems@55751ad6d9915a2600d42385d41388c900d29a26`, `.../20260922T143520Z-fleet02-B07-QFORM-r11/REPORT.md`;
2. designated partner fleet03/B07 `QFORM-NESTED-HEAVY-DISJOINT-BANK-COLLAR-v1`, `yspennstate/math-open-problems@494c999fc67d230fff7e2079b1867216253b35bc`;
3. live correction event fleet02/B06 `QFORM-PLUCKER-PIVOT-SUPPORT-DISJOINT-v1`, canonical report `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`.

No scheduler mutation, notification/email action, public release, remote workflow, paid API/model, cross-account authentication, private unrelated data, or benchmark material is used.
