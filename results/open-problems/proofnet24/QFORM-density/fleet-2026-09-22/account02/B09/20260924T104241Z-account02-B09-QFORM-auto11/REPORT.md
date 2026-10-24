SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-24T10:42:41Z.
attacking: the latest account03/B09 scalar-pivot rank-two Schur-currency forcing debt, using a dense same-side mixed-hub source family to test whether post-pivot currency can be forced from the three-large-eigenvalue hypothesis.

# account02/B09 auto11 — scalar-pivot currency collapse before a fixed mixed frame

Programme: `QFORM-DENSITY-3EIG-20260922`
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples
Run: `20260924T104241Z-account02-B09-QFORM-auto11`
Status: **ESSENTIAL_STEP_APPLIED; NEW STRUCTURAL OBSTRUCTION PROVED; FULL QFORM OPEN; CONTINUITY SEPARATE**
Execution: `WITHOUT_VERIFIED_BRAIN`.

No moments, bounded support, log-concavity, connected support, iid assumption, diagonal-basis assumption, or post-rotation independence is used. Every random variable below is a literal original coordinate. The family keeps a physically dense same-bank quadratic block. The conclusion is a counterexample to a proposed proof-forcing mechanism, not to the QFORM conjecture.

## 1. First unpaid implication

The first unpaid B09 implication is now

`QFORM-SMALL-SCALARPIVOT-CURRENCY-TO-MIXEDFRAME-OR-CROSSVOLUME-v1`:

> From `s_3(A)>=1`, after already-paid physical-pair and finite-core exits, route the survivor in which every scalar-pivot grouped-rank-two Schur currency is small into a **pre-pivot** literal source-coordinate mixed Fresnel frame, a grouped projected-crossing/volume receiver, or another bounded physical core. The compiler must retain arbitrary same-bank curvature and may not delete a small quadratic coefficient, take a worst conditional projection-density supremum, or infer independence after rotating coordinates.

The new construction below proves that the alternative “force one scalar pivot with universal grouped-rank-two Schur currency” is false. More strongly, even the naive sum of those currencies over all available nonzero scalar pivots can tend to zero.

## 2. Sources actually applied

The required pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` proves Theorem H, the mixed-hub Fresnel–Brascamp–Lieb estimate. In the notation used here, if `H` is a set of literal hubs, the active leaf block is diagonal plus `r` Fresnel directions, the mixed rows combine those Fresnel coefficients with the literal hub-to-leaf coefficients, the mixed Gram is positive, and every leaf leverage is at most `1/2`, then the full characteristic function obeys an explicit power envelope. All hub self terms, outside blocks, and affine terms are retained. This is a no-decoupling estimate: no probability squaring occurs.

The latest compatible completed designated-partner artifact observed before this report is account03/B09 r48,

`math-open-problems@677dba9150479b33025f9f0b948e46eec5dbf9c5`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260924T094653Z-account03-B09-QFORM-r48/REPORT.md`.

Its new supporting theorem, still marked pending independent review by its author, is `QFORM-SCALARPIVOT-GROUPED-RANK2-HALFRIESZ-v1`. For a literal pivot `h` with `a=A_hh!=0`, exact scalar Schur complement `S`, a literal two-row set `I`, disjoint original-coordinate bank `J`, and `C=S[I,J]` of rank two, put

`Delta_2=sigma_1(C)sigma_2(C)`.

The theorem states

`||p_Q||_infinity <= 2^(11/4) |a|^(-1/2) Delta_2^(-1/4)
                    = 2^(11/4) (|a|^2 Delta_2)^(-1/4)`.

It retains arbitrary same-side curvature and converts the rank-two crossing half-potential directly to the linear interval scale. Its own exact next debt was to force `|a|^2 Delta_2>=c` or route every small-currency survivor elsewhere. Its deterministic checker recorded all assertions passed; that finite checker is evidence for algebra/constants, not an independent proof review.

The pinned counterexample search reports no valid counterexample to full QFORM. This run finds none.

## 3. Dense target-valid source family

Let `m=2^k>=8`. Choose three distinct flat orthonormal Sylvester–Walsh vectors

`c,w_1,w_2 in R^m`.

Write

`c_i=tau_i/sqrt(m)`, `w_{1i}=sigma_{1i}/sqrt(m)`, `w_{2i}=sigma_{2i}/sqrt(m)`

with signs in `{+1,-1}`. Let `U,Y_1,...,Y_m` be arbitrary independent real random variables, each with probability density at most one. Define

`Q_m = 2 U <c,Y> + <w_1,Y>^2 + 2 <w_2,Y>^2`.          (3.1)

Thus

`A_m = [[0,c^T],[c,L]]`,
`L = w_1 w_1^T + 2 w_2 w_2^T`.                         (3.2)

The same-side leaf block is physically dense. Indeed

`L_ij=(sigma_{1i}sigma_{1j}+2 sigma_{2i}sigma_{2j})/m`

belongs to `{+-1/m,+-3/m}` and therefore never vanishes.

Because `c,w_1,w_2` are orthonormal, the active operator in the deterministic orthonormal coefficient basis `(U,c,w_1,w_2)` is

`[[0,1],[1,0]] direct_sum [1] direct_sum [2]`.

Hence

`spec_nonzero(A_m)={-1,1,1,2}`.                         (3.3)

Every member therefore satisfies the owner's exact spectral target, in fact with four eigenvalues of modulus at least one.

## 4. Pinned Theorem H pays the full law before any scalar pivot

Apply pinned Theorem H with the literal hub set `H={U}`, leaf bank all `Y_i`, two Fresnel directions `w_1,w_2`, coefficients `lambda_1=1`, `lambda_2=2`, and diagonal remainder `D=0`.

The physical mixed rows are

`rho_i=(w_{1i},w_{2i},c_i) in R^3`.

Their Gram is exactly

`G=sum_i rho_i rho_i^T=I_3`,                            (4.1)

and every physical leaf leverage is

`rho_i^T G^(-1) rho_i = 3/m <= 3/8 < 1/2`.             (4.2)

Theorem H gives

`|phi_{Q_m}(t)|
 <= (2|t|)^(-1) (4pi|t|)^(-1/2) (8pi|t|)^(-1/2) (4pi)^3
 = 4 sqrt(2) pi^2 |t|^(-2)`.                           (4.3)

Thus, with `K=4 sqrt(2) pi^2`,

`int_R min(1,K|t|^(-2)) dt = 4 sqrt(K)`.

Fourier inversion yields

`boxed:
 ||p_{Q_m}||_infinity
 <= (2/pi) sqrt(K)
 = 4*2^(1/4)
 = 4.756828460010884... .`                              (4.4)

Consequently every interval `E` satisfies

`boxed:
 P{Q_m in E} <= 4*2^(1/4) |E|.`                        (4.5)

This branch has a continuous density because the characteristic function is in `L^1`. The dense same-side leaf matrix `L` is retained exactly. There is no Cauchy–Schwarz decoupling, no probability squaring, and hence no square-root small-ball loss.

## 5. Exact scalar-pivot geometry

The literal hub has

`A_UU=0`,

so it is unavailable as the nonzero scalar pivot in the r48 theorem. Every leaf pivot `j` has

`a_j=A_jj=w_{1j}^2+2w_{2j}^2=3/m`.                     (5.1)

Let `u_j=A[-j,j]` and let

`S_j=A[-j,-j]-u_j u_j^T/a_j`                            (5.2)

be its exact scalar Schur complement. We now bound **every** possible grouped rank-two crossing in `S_j`, including pairs that use the physical hub `U` as one of their two rows.

First note that

`L^2=w_1w_1^T+4w_2w_2^T`,

so the full squared norm of a physical leaf column is

`(A_m^2)_{jj}=c_j^2+(L^2)_{jj}=1/m+5/m=6/m`.           (5.3)

After deleting its diagonal entry `a_j=3/m`,

`||u_j||_2^2 = 6/m - 9/m^2`.                           (5.4)

### Leaf rows after the pivot

For a remaining leaf `k!=j`, the row of the Schur complement obeys

`||S_j[k,*]||_2
 <= ||A[k,-j]||_2 + (|A_kj|/a_j)||u_j||_2`.            (5.5)

The full leaf row of `A` has norm `sqrt(6/m)`, and

`|A_kj|=|L_kj|<=3/m=a_j`.

Therefore

`boxed:
 ||S_j[k,*]||_2 <= 2 sqrt(6/m).`                        (5.6)

### Physical hub row after the pivot

The full hub row has norm `||c||_2=1`, while

`|A_Uj|/a_j=(1/sqrt(m))/(3/m)=sqrt(m)/3`.

Using (5.4),

`boxed:
 ||S_j[U,*]||_2
 <= 1 + sqrt(6)/3.`                                     (5.7)

These bounds are independent of which columns will later be retained as the crossing bank.

## 6. Every r48 grouped-rank-two Schur currency vanishes

Fix any literal two-row set `I` in the Schur complement and any disjoint original-coordinate bank `J`. Put

`C=S_j[I,J]`.

For a two-row matrix the product of its two singular values is the Euclidean area of its two row vectors after restriction to `J`, hence

`Delta_2(C)=sigma_1(C)sigma_2(C)
 <= ||row_1(C)||_2 ||row_2(C)||_2`.                     (6.1)

If both rows in `I` are leaves, (5.6) gives

`Delta_2 <= 24/m`.                                      (6.2)

If one row is the hub and one is a leaf, (5.6)-(5.7) give

`Delta_2
 <= (1+sqrt(6)/3) 2 sqrt(6/m)
 = (4+2sqrt(6))/sqrt(m)`.                               (6.3)

For `m>=8`, the latter upper bound dominates `24/m`. Hence **for every possible literal pivot, literal two-row set, and disjoint crossing bank**,

`boxed:
 Delta_2 <= (4+2sqrt(6)) m^(-1/2).`                     (6.4)

Combining (5.1) and (6.4), every r48 scalar-pivot currency satisfies

`boxed:
 |a_j|^2 Delta_2
 <= 9(4+2sqrt(6)) m^(-5/2)
 = 80.0908153700972... m^(-5/2)
 ->0.`                                                  (6.5)

This proves

`QFORM-SCALARPIVOT-RANK2-CURRENCY-FORCING-FALSE-DENSE-MIXEDFRAME-v1`:

> The bare target hypothesis, even with four large eigenvalues and a fully dense physical same-bank block, does not force one literal scalar pivot whose grouped rank-two Schur currency `|A_hh|^2 sigma_1(C)sigma_2(C)` is bounded below by a universal positive constant.

The obstruction is stronger than failure of a best-pivot selector. There are exactly `m` nonzero scalar pivots, all leaves, so even summing the **best possible** grouped-crossing currency for every pivot gives

`boxed:
 sum_j sup_(I,J) |a_j|^2 Delta_2(j;I,J)
 <= 9(4+2sqrt(6)) m^(-3/2)
 ->0.`                                                  (6.6)

Thus a naive `l^1` ledger of the post-pivot currencies cannot repair the forcing implication.

## 7. Actual quantitative obstruction to pair-first/pivot-first payment

The source-reported r48 bound for any admissible rank-two crossing is

`2^(11/4) [|a_j|^2 Delta_2]^(-1/4)`.

By (6.5), every finite certificate produced by that route is at least

`2^(11/4) [9(4+2sqrt(6))]^(-1/4) m^(5/8)
 = 2.248727387848681... m^(5/8)`.                       (7.1)

At the concrete target-valid instance `m=1024`,

`max_(j,I,J) |a_j|^2 Delta_2 <= 2.3868922999530197e-6`,

and

`sum_j sup_(I,J) |a_j|^2 Delta_2 <= 0.002444177715151892`.

Therefore every finite r48 scalar-pivot certificate has numerical right-hand side at least

`boxed: 171.14896699719262...`,                         (7.2)

while the pinned mixed-frame theorem gives the **same full law**

`boxed: ||p_{Q_1024}||_infinity <= 4.756828460010884...`. (7.3)

This does not contradict the partner theorem. It identifies the wrong order of operations. Spreading the two same-bank square directions over `m` literal leaves makes every physical leaf diagonal `3/m`. Paying a scalar pivot first injects the square of that diluted diagonal into the currency, and the remaining two-row crossing area is at most `O(m^(-1/2))`. The pre-pivot mixed frame instead sees the three source directions `c,w_1,w_2` jointly while their Gram is still exactly `I_3`.

## 8. Relation to the previous B09 obstruction

The immediately preceding account02/B09 run on the same dense family showed that every **definite physical-pair polynomial star** is `O(m^(-3/2))` and that the full squared definite-star ledger tends to zero, while the mixed frame stays fixed. The new account03/B09 r48 theorem changes mechanism by allowing one scalar pivot followed by a grouped rank-two Schur crossing. Equations (6.4)-(6.6) show that this stronger post-pivot currency also collapses, even after optimizing the whole disjoint crossing bank and even after naive aggregation over every available nonzero pivot.

Hence the structural lesson is not merely “use a larger bank after choosing a pair.” On diffuse same-bank curvature, the aggregate source directions may have to be recognized **before any physical pivot is paid**.

## 9. What remains

The construction does not refute QFORM: it is uniformly paid by (4.4). It also does not prove that every small-pivot-currency survivor has a good mixed frame. The unresolved full-target compiler must start only from the spectral hypothesis `s_3(A)>=1` and arbitrary same-bank curvature. It must establish a universal alternative of the form

1. a paid physical/core branch is already macroscopic; or
2. a literal source-coordinate mixed frame of sufficient determinant and leverage is available before pivot selection; or
3. a grouped projected-crossing/volume/ridge mechanism pays the survivor; or
4. a genuinely bounded-dimensional physical core remains.

The main difficult point is to produce such a source-coordinate aggregate from a completely general symmetric matrix without interpreting small matrix norm as a small random quadratic perturbation on arbitrary unbounded inputs.

No valid full-target counterexample was found. Full unrestricted essential boundedness remains OPEN, and full-target continuity remains OPEN.
