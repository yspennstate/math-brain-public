SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-23T18:53:17Z.
attacking: the Cauchy--Binet overlap decomposition of the third spectral volume; pay disjoint minors by rank-three crossing, one-shared-index minors by a physical square plus critical two-volume smoothing, and two-shared-index minors by an indefinite physical pair plus a new one-volume half-Frostman estimate.

# account01/B03 r31 — overlap-volume compilers for the decoupled-time route

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: `Decoupled time integral`  
Status: **NEW SUPPORTING THEOREMS / THREE OVERLAP SECTORS QUANTITATIVELY ROUTED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` was consumed. The unrestricted target is unchanged: independent real coordinate densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, no moment/support/log-concavity/connected-support/diagonal-basis assumptions. Continuity is tracked separately.

This run changes the structural mechanism. Rather than select one small physical minor and invert it, I decompose the *entire third Cauchy--Binet spectral volume* by the amount of row/column overlap. The disjoint sector feeds the already-proved row-marginal-free rank-three crossing theorem. The one-overlap sector feeds the preceding B03 critical two-volume theorem after one exact scalar Schur completion. The two-overlap sector requires a new row-marginal-free one-volume half-Frostman theorem and then the physical-pair logarithmic transducer. The latter has an exact determinant cancellation, so the determinant of the selected indefinite pair disappears from the final scale.

The full conjecture remains open because the decomposition does not yet force one of the paid normalized resources to be large: zero scalar pivots can carry the one-overlap mass, nearly singular or definite physical pairs can carry the two-overlap mass, and the principal-overlap sector can remain large. Those are now explicit sectors rather than a generic “no good minor” gap.

## 1. Source-valid inputs and corrections retained

### 1.1 Row-marginal-free critical two-volume endpoint

The preceding B03 theorem is

`yspennstate/math-open-problems@588fa418bc29d4b889fcbbee2b61370234ceef37`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T175336Z-account01-B03-QFORM-r30/REPORT.md`.

For a physical cut `I|J`, write

`R=F(X_I)+2 X_I^T B X_J+G(X_J)`,

with arbitrary quadratic-plus-affine internal functions. If

`Z_2=e_2(BB^T)=sum_(i<j)|b_i wedge b_j|^2>0`,

then

`|phi_R(t)| <= min{1, 2*pi*sqrt(2e) Z_2^(-1/4)|t|^(-1)}`,          (1.1)

and

`sup_s E|R-s|^(-1/2) <= 8(2e)^(1/4) Z_2^(-1/8)`.                 (1.2)

The proof retains the whole independent-copy scalar difference and removes the two-volume row-marginal gate by a finite physical-row promotion tree. If one further genuine original coordinate completes as `d(Z+h)^2`, then

`||p_Q||_infinity <= 8(2e)^(1/4)|d|^(-1/2)Z_2^(-1/8)`.           (1.3)

### 1.2 Row-marginal-free rank-three crossing

The preceding B03 rank-three crossing theorem is at

`yspennstate/math-open-problems@2062e0f60e39c2cb88fb72c4908d95f19676d00e`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/20260923T165124Z-account01-B03-QFORM-r29/ADDENDUM_CROSSBLOCK.md`.

For a physical cross block `B=A_{L,R}`, let

`Z_3=e_3(BB^T)=sum_(|S|=3)|wedge_(i in S)b_i|^2`.

Then, with no row-marginal hypothesis,

`||p_Q||_infinity <= C_3 Z_3^(-1/6)`,
`C_3=3*2^(3/2)*sqrt(e)=13.989863889582747...`,                    (1.4)

and this branch has a continuous `C_0` density because its characteristic function is integrable.

### 1.3 Weighted-subset / grouped-crossing source

The independently checked projected-crossing source used below is

`yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`.

Its weighted-subset estimate is used only in the exact `k=0, ell=1` scope in Section 3, and its exact-rank-one crossing theorem is used for the heavy-row promotion. No law-uniform pointwise quadratic-phase decay is used.

### 1.4 Designated partner account02/B03 actually applied

The current completed designated partner result is

`yspennstate/math-open-problems@38920ffa423ec07886112206314249deb7294dd4`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T171205Z-account02-B03-QFORM-auto11/REPORT.md`.

Its `k=1, ell=1` critical grouped-crossing estimate says that a one-dimensional physical hub of density cap `M_H`, hub-to-`J` singular product `S`, projected crossing Frobenius norm `F`, and projected row marginals at most `1/2` obeys

`|phi(t)| <= min{1,2*pi*M_H^(1/2)(S F)^(-1/2)|t|^(-1)}`,          (1.5)

and one further genuine physical square `d(Z+h)^2` yields

`||p_Q||_infinity <=8 M_H^(1/4)(|d|^2 S F)^(-1/4)`.               (1.6)

I apply `(1.6)` to the actual heavy-row subbranch of the one-overlap compiler in Section 5.4.

### 1.5 Physical-pair logarithmic transducer

The source-pinned pair theorem is

`yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.

If a genuine original-coordinate principal pair `B_0` is invertible indefinite, with

`D=|det B_0|`, `kappa=sigma_min(B_0)`,

and after completing it the remainder satisfies

`sup_t P(|R-t|<rho) <= H sqrt(rho)`                                 (1.7)

for all `rho>0`, then

`||p_Q||_infinity <=4 sqrt(2H)(D kappa)^(-1/4)`.                   (1.8)

The pair shifts may depend arbitrarily on the remainder. No conditional cap for one member of a conjugate sum/difference pair is used.

### 1.6 Corrections

The proof below does not use: independence after spectral rotation; the refuted arbitrary-joint three-dimensional coarea cap; a conditional density cap for one of `X+X'` and `X-X'`; law-uniform pointwise van der Corput; a uniformly good single physical minor; a fixed-support/fragment-count reduction; or a moment bound. All Fourier estimates are aggregate product-coordinate estimates or exact crossing/Plancherel bounds in their proved scopes.

## 2. Spectral third volume and the overlap decomposition

Let the eigenvalues of `A` be `lambda_1,...,lambda_n`, ordered by decreasing absolute value, and put

`E^(3)=e_3(A^2)=sum_(i<j<k) lambda_i^2 lambda_j^2 lambda_k^2`.       (2.1)

Cauchy--Binet and symmetry give the exact physical-coordinate identity

`E^(3)=sum_(|S|=|T|=3) det(A_{S,T})^2`.                              (2.2)

Indeed

`e_3(A^2)=sum_(|S|=3) det((A^2)_{S,S})`
`          =sum_(|S|=|T|=3) det(A_{S,T})det(A_{T,S})`,

and `A_{T,S}=A_{S,T}^T`.

Decompose the nonnegative sum by overlap cardinality:

`E^(3)=E_0+E_1+E_2+E_3^pr`,                                        (2.3)

where `E_r` is the sum over ordered triples `(S,T)` with `|S cap T|=r` for `r=0,1,2`, and

`E_3^pr=sum_(|S|=3) det(A_{S,S})^2`.                                (2.4)

If `s=s_3(A)` denotes the third singular value of the symmetric matrix, then

`E^(3)>=s^6`.                                                        (2.5)

This decomposition is the organizing invariant for the present run.

## 3. New analytic lemma: row-marginal-free one-volume half-Frostman smoothing

The two-overlap sector will leave a Schur remainder for which only one aggregate crossing direction is available. The critical one-volume endpoint does not give a bounded density, but it gives exactly a translation-uniform square-root small-ball estimate, enough for the pair-log transducer.

### Theorem 3.1 — `QFORM-ROW-MARGINAL-FREE-1VOLUME-HALFFROSTMAN-v1`

Let `I,J` be disjoint original-coordinate banks and let

`R=F(X_I)+2 X_I^T B X_J+G(X_J)`,                                   (3.1)

where all coordinates are mutually independent with density caps one and `F,G` are arbitrary real quadratic-plus-affine functions on their own banks. Put

`Z_1=||B||_F^2=sum_(i in I)||b_i||^2>0`.                            (3.2)

Then

`boxed:
 |phi_R(t)| <= min{1,K_1 Z_1^(-1/4)|t|^(-1/2)},
 K_1=2^(3/4)*sqrt(pi)=2.98090017885818... .}`                       (3.3)

Consequently, uniformly in `z in R` and `rho>0`,

`boxed:
 P(|R-z|<rho)
 <= H_1 Z_1^(-1/4) sqrt(rho),
 H_1=sqrt(2e)*Gamma(1/4)=8.453631522124514... .}`                   (3.4)

No continuity or bounded-density conclusion for `R` alone is claimed.

### Proof of the Fourier envelope

Define the one-volume row marginals

`alpha_i=||b_i||^2/Z_1`, `sum_i alpha_i=1`.                          (3.5)

There are two cases.

**Diffuse case.** Suppose every `alpha_i<=1/2`. Apply Cauchy--Schwarz in the whole `I` bank before expanding the square. If `X_J'` is an independent copy of `X_J`, `D_J=X_J-X_J'`, and `psi_i` is the characteristic function of the original scalar coordinate `X_i`, then the phase `F(X_I)` cancels inside the absolute square and the phase difference from `G(X_J)-G(X_J')` has modulus one. Therefore

`|phi_R(t)|^2
 <= E_D product_(i in I)|psi_i(2t <b_i,D_J>)|`.                  (3.6)

The coordinates of `D_J` remain independent and each difference density is at most one. Apply the weighted-subset Fourier lemma with `k=0`, `ell=1`. The `ell=1` entropy factor cancels exactly, giving

`|phi_R(t)|^2
 <= min{1, 2*sqrt(2)*pi /(sqrt(Z_1)|t|)}`.                      (3.7)

Taking square roots yields `(3.3)` because

`sqrt(2*sqrt(2)*pi)=2^(3/4)sqrt(pi)=K_1`.                           (3.8)

**Heavy-row case.** Suppose some `alpha_i>1/2`. Promote the genuine physical coordinate `X_i` to a one-dimensional hub and put every other original coordinate in the complementary bank. The full hub-to-complement cross row has Euclidean norm `S` satisfying

`S>=||b_i||=sqrt(alpha_i Z_1)>Z_1^(1/2)/sqrt(2)`.                   (3.9)

The exact-rank-one crossing theorem applies with hub density cap one and one-dimensional product-projection density cap at most `sqrt(2)`. It gives

`|phi_R(t)|
 <= min{1,sqrt(pi)*2^(1/4)S^(-1/2)|t|^(-1/2)}`
` < min{1,sqrt(2*pi) Z_1^(-1/4)|t|^(-1/2)}`.                       (3.10)

Since `sqrt(2*pi)<K_1`, the diffuse envelope `(3.3)` dominates both cases. The promotion keeps all internal curvature on the complementary bank inside the allowed arbitrary internal function. No coordinate rotation of the product law is made.

### Proof of the half-Frostman estimate

Use the elementary Gaussian majorant

`1_(|x|<rho) <= exp(1/2) exp(-x^2/(2rho^2))`.                       (3.11)

Gaussian Fourier inversion and `(3.3)` imply

`P(|R-z|<rho)`
` <= exp(1/2) rho/sqrt(2*pi)
      int exp(-rho^2 t^2/2)|phi_R(t)|dt`
` <= exp(1/2) rho/sqrt(2*pi) K_1 Z_1^(-1/4)
      int exp(-rho^2t^2/2)|t|^(-1/2)dt`.                           (3.12)

After `u=rho t`,

`int_R exp(-u^2/2)|u|^(-1/2)du=2^(1/4)Gamma(1/4)`.                 (3.13)

Substituting `K_1=2^(3/4)sqrt(pi)` gives exactly `(3.4)`.

The independent-copy identity remains available in its safe scalar form

`|phi_R(t)|^2=E exp(it(R-R'))`.                                     (3.14)

I do not condition on one coordinate sum or difference in this proof.

## 4. The disjoint-minor sector `E_0`

Choose a random physical coordinate cut `L|R` by putting each coordinate independently into `L` or `R` with probability `1/2`. For the cross block `A_{L,R}`, Cauchy--Binet gives

`Z_3(A_{L,R})
 =sum_(S subset L,T subset R,|S|=|T|=3) det(A_{S,T})^2`.            (4.1)

Every ordered disjoint pair `(S,T)` is captured with probability `2^-6`. Therefore

`E_cut Z_3(A_{L,R})=E_0/64`,                                        (4.2)

so some physical cut satisfies

`Z_3(A_{L,R})>=E_0/64`.                                             (4.3)

Applying `(1.4)` gives the target-level implication

`boxed:
 ||p_Q||_infinity <= 2 C_3 E_0^(-1/6).}`                            (4.4)

This branch has a continuous `C_0` density. In particular, if

`E_0>=theta_0 s^6`,                                                 (4.5)

then

`||p_Q||_infinity
 <= 2 C_3 theta_0^(-1/6) s^(-1)`.                                  (4.6)

For the illustrative threshold `theta_0=1/4`, the constant is

`2 C_3 4^(1/6)=35.2522479993...`.                                   (4.7)

This is an aggregate-before-inversion certificate: no individual `3x3` cross minor is selected.

## 5. The one-shared-index sector `E_1`: exact scalar Schur compiler

Fix a physical coordinate `h` with

`a=A_hh !=0`.                                                       (5.1)

Write the complement as `Y=X_{-h}`, set `c=A_{-h,h}`, and define the scalar Schur complement

`S^(h)=A_{-h,-h}-a^(-1)c c^T`.                                     (5.2)

Exact completion gives

`Q=a(X_h+a^(-1)c^T Y)^2+Y^T S^(h)Y`.                               (5.3)

Define the overlap-one mass with common index `h`:

`E_1(h)
 =sum_{I,K subset [n]\{h}, |I|=|K|=2, I cap K=empty}
    det(A_{ {h} union I, {h} union K})^2`.                          (5.4)

The sum is over ordered `(I,K)`. Block determinant gives, term by term,

`det(A_{ {h} union I, {h} union K})
 =a det(S^(h)_{I,K})`,                                              (5.5)

hence

`E_1(h)=a^2 sum_(I cap K=empty) det(S^(h)_{I,K})^2`.                (5.6)

Now randomly cut the complement of `h` into `L|R`. Cauchy--Binet gives

`Z_2(S^(h)_{L,R})
 =sum_(I subset L,K subset R,|I|=|K|=2) det(S^(h)_{I,K})^2`.        (5.7)

Every ordered disjoint `(I,K)` is captured with probability `1/16`, so

`E_cut Z_2(S^(h)_{L,R})=E_1(h)/(16a^2)`.                            (5.8)

Choose a cut realizing at least the expectation and apply `(1.3)` to the exact physical square `(5.3)`. This yields

`boxed:
 ||p_Q||_infinity
 <= C_1 [a^2 E_1(h)]^(-1/8),
 C_1=8 sqrt(2)(2e)^(1/4)
    =17.275717919798065... .}`                                     (5.9)

The scaling is correct: `a^2E_1(h)` has coefficient degree eight.

Thus if for some `h`

`a^2E_1(h)>=theta_1 s^8`,                                           (5.10)

then

`||p_Q||_infinity <= C_1 theta_1^(-1/8)s^(-1)`.                    (5.11)

This proves essential boundedness and absolute continuity in this branch. Continuity is not established by the square/half-Riesz compiler for arbitrary fragmented input densities.

### 5.4 Actual use of the designated partner result

The chosen Schur cut in `(5.8)` has cross rows `b_i`. Suppose its pair-volume row marginal

`alpha_i=Z_2^(-1) sum_(j!=i)|b_i wedge b_j|^2`                       (5.12)

is larger than `1/2`, and after promoting this actual row the projected one-volume marginals are all at most `1/2`. The exact exterior identity from the r30 promotion step is

`S^2 F^2=alpha_i Z_2`,                                              (5.13)

where `S` is the hub-to-opposite-bank row norm and `F` is the projected crossing Frobenius norm. The hub is one original coordinate, so `M_H<=1`.

Apply the completed account02/B03 square receiver `(1.6)` to the *same* physical square `(5.3)`:

`||p_Q||_infinity
 <=8 |a|^(-1/2)(alpha_i Z_2)^(-1/8)`.                              (5.14)

Using `alpha_i>1/2` and `(5.8)`,

`boxed:
 ||p_Q||_infinity
 < 8*2^(5/8)[a^2E_1(h)]^(-1/8)
 =12.337686603263526...[a^2E_1(h)]^(-1/8).}`                        (5.15)

This is a concrete application of the designated partner theorem at an actual inequality; it strictly improves the common envelope `(5.9)` on this heavy-row/diffuse-projection subbranch. No conditional sum/difference density cap is introduced.

## 6. The two-shared-index sector `E_2`: indefinite-pair compiler

Fix a physical pair `H={h_1,h_2}` for which the principal block

`B_0=A_{H,H}`                                                       (6.1)

is invertible and indefinite. Put

`D=|det B_0|`, `kappa=sigma_min(B_0)>0`,                            (6.2)

and let the two-coordinate Schur complement on the remaining coordinates be

`S^(H)=A_{H^c,H^c}-A_{H^c,H}B_0^(-1)A_{H,H^c}`.                    (6.3)

Define the overlap-two mass with common pair `H` by

`E_2(H)
 =sum_(i,j in H^c, i!=j)
   det(A_{H union {i}, H union {j}})^2`.                            (6.4)

The ordered pair `(i,j)` matters. The block determinant identity gives

`det(A_{H union {i}, H union {j}})
 =det(B_0) S^(H)_{ij}`,                                             (6.5)

so

`E_2(H)=D^2 sum_(i!=j)(S^(H)_{ij})^2`.                              (6.6)

Randomly cut `H^c=L disjoint_union R`. The cross Frobenius resource of the Schur remainder is

`Z_1(S^(H)_{L,R})
 =sum_(i in L,j in R)(S^(H)_{ij})^2`.                               (6.7)

Each ordered `i!=j` is captured with probability `1/4`; hence

`E_cut Z_1(S^(H)_{L,R})=E_2(H)/(4D^2)`.                             (6.8)

Choose a cut with

`Z_1>=E_2(H)/(4D^2)`.                                               (6.9)

Theorem 3.1 gives the remainder the translation-uniform half-Frostman profile

`sup_z P(|R-z|<rho)
 <= H_1 Z_1^(-1/4) sqrt(rho)`.                                     (6.10)

Now apply the physical-pair logarithmic transducer `(1.8)`. The determinant cancels exactly:

`||p_Q||_infinity
 <=4 sqrt(2 H_1 Z_1^(-1/4))(D kappa)^(-1/4)`
` <=4 sqrt(2 H_1 sqrt(2)D^(1/2)E_2(H)^(-1/4))
       D^(-1/4)kappa^(-1/4)`
` =C_2 kappa^(-1/4)E_2(H)^(-1/8)`,                                 (6.11)

where

`boxed:
 C_2=8 e^(1/4) sqrt(Gamma(1/4))
    =19.55933769831132... .}`                                      (6.12)

Equivalently,

`boxed:
 ||p_Q||_infinity
 <= C_2 [kappa^2 E_2(H)]^(-1/8).}`                                 (6.13)

Thus if some invertible indefinite physical pair satisfies

`kappa^2E_2(H)>=theta_2 s^8`,                                      (6.14)

then

`||p_Q||_infinity<=C_2 theta_2^(-1/8)s^(-1)`.                      (6.15)

This proves essential boundedness and absolute continuity in the stated branch. Continuity is not claimed by the pair-log receiver.

The determinant cancellation in `(6.11)` is important: the compiler does **not** require a lower bound on `D` separately. What remains is the smallest singular value `kappa`, which is unavoidable in the present logarithmic pair theorem.

A definite pair is different. Conditional integration over a whole ellipse gives the elementary cap `pi/sqrt(D)`, but the present argument does not produce an `E_2`-compensated bound when `D` is tiny. Definite near-singular pairs therefore remain in the structural survivor.

## 7. Quantitative structural reduction from `e_3(A^2)`

The exact decomposition can now be written as

`e_3(A^2)
 =E_0+sum_h E_1(h)+sum_(|H|=2)E_2(H)+E_3^pr`.                       (7.1)

Here `E_1(h)` and `E_2(H)` are exactly `(5.4)` and `(6.4)`. The four summands are nonnegative and exhaust all ordered pairs of physical triples by overlap cardinality.

Combining Sections 4--6 gives three product-preserving aggregate certificates:

1. **Disjoint sector**

   `E_0>=theta_0 s^6`
   implies
   `||p_Q||_infinity<=2C_3 theta_0^(-1/6)s^(-1)`,
   with a continuous `C_0` density.

2. **One-overlap scalar-pivot sector**

   some `h` with `A_hh!=0` and
   `A_hh^2 E_1(h)>=theta_1 s^8`
   implies
   `||p_Q||_infinity<=C_1 theta_1^(-1/8)s^(-1)`.

3. **Two-overlap indefinite-pair sector**

   some invertible indefinite `H` with
   `sigma_min(A_HH)^2 E_2(H)>=theta_2 s^8`
   implies
   `||p_Q||_infinity<=C_2 theta_2^(-1/8)s^(-1)`.

All three aggregate before reciprocal local selection. In particular, the estimates remain meaningful when the relevant Cauchy--Binet mass is spread among many individually tiny minors.

The full theorem would follow from a universal structural statement forcing at least one of these paid resources or one of the already-paid diagonal/semidefinite/grouped-hub/ridge branches. I have **not** proved that structural statement.

The precise remaining overlap survivors exposed by `(7.1)` are:

* a large `E_1` sector carried mainly by common indices with zero or extremely small physical diagonals, where scalar Schur completion is unavailable or loses scale;
* a large `E_2` sector carried mainly by definite or nearly singular physical principal pairs, so `kappa^2E_2(H)` can be small pairwise even when the aggregate `E_2` is large;
* a large principal sector `E_3^pr`, potentially distributed among many ill-conditioned physical principal triples;
* mixtures of these three effects.

These are the next targets for an overlap-aware decoupled-time proof. A particularly natural next mechanism is to use the exact whole-copy identity `Q(X)-Q(X')=(X-X')^T A(X+X')` while keeping each conjugate coordinate pair joint, so a shared row/column index can be paid without dividing by a physical diagonal. The live correction `QFORM-UV-CONDITIONAL-CAP-FALSE` means such a step must use the joint pair law, not a conditional marginal cap.

## 8. Dependence-safe time interpretation

The new one-volume theorem is itself obtained from the same product-preserving independent-copy step used throughout B03. Equation `(3.6)` comes from squaring the characteristic function only after grouping an entire original-coordinate bank. In every use of

`|phi(t)|^2=E exp(it(R-R'))`,                                       (8.1)

the scalar difference `R-R'` is kept intact. I never assert that the coordinatewise conjugate sums and differences are independent.

For the critical two-volume residuals inherited from r30, the stronger assignment-specific estimate remains

`int_R |t|^(-1/2)|phi_R(t)|^2dt
 <=20.41360850273567... Z_2^(-1/8)`,                                (8.2)

and the square compiler in Section 5 converts its corresponding one-copy half-Riesz control into a linear small-ball bound. For the overlap-two branch, Theorem 3.1 supplies the square-root remainder small-ball profile required by the pair-log transducer, which again outputs a genuine linear bound

`P(Q in I)<=C_2[kappa^2E_2(H)]^(-1/8)|I|`.                          (8.3)

Thus the present run advances the requested integrated/decoupled route without replacing a collision estimate by an invalid `L^infinity` criterion.

## 9. Finite algebra checks

The current run executed deterministic finite checks on random real symmetric `7x7` matrices. These verify identities and arithmetic only; they are not evidence for the universal theorem.

* For 30 seeded matrices, the scalar-Schur identity `(5.6)` had maximum relative discrepancy `1.34e-15`, and the exact average over all cuts in `(5.8)` had maximum relative discrepancy `9.05e-16`.
* For 10 seeded matrices, the exact all-cut average `(4.2)` had maximum relative discrepancy `3.80e-16`.
* For 20 seeded matrices with nonsingular physical pairs, the pair-Schur identity `(6.6)` had maximum relative discrepancy `8.89e-16`, and the exact average `(6.8)` had maximum relative discrepancy `8.63e-16`.

The constants were also evaluated independently:

`K_1=2.98090017885818...`,
`H_1=8.453631522124514...`,
`C_1=17.275717919798065...`,
`C_2=19.55933769831132...`,
`8*2^(5/8)=12.337686603263526...`.

## 10. Status

**Full QFORM:** OPEN.  
**Universal counterexample:** none produced.  
**Newly proved here:** row-marginal-free one-volume half-Frostman theorem; disjoint/minor-overlap aggregate compilers `E_0`, `E_1(h)` with nonzero scalar pivot, and `E_2(H)` with an invertible indefinite pair; designated-partner improvement on the one-overlap heavy-row subbranch.  
**Essential boundedness:** proved in all three paid branches.  
**Continuity:** proved in the `E_0` rank-three crossing branch; not proved by the `E_1` square compiler or `E_2` pair-log compiler under arbitrary fragmented input densities.  
**Next essential implication:** pay the zero/small-diagonal part of `E_1` and the definite/near-singular part of `E_2` directly from the whole-copy pair law, or prove that their mass forces one of the already-paid structural exits.

No claim of a complete proof, literature novelty, or source-wide priority is made.
