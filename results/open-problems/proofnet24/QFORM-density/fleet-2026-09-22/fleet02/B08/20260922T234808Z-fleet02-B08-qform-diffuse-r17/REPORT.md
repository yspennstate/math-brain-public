SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-22T23:48:08Z.
attacking: the delocalized balanced-cut branch in which three units of global curvature leave a principal child through an actual original-coordinate cross block, with no moments and no post-rotation independence.

# fleet02/B08 — full-cross-rank Fourier payment and a delocalized spectral-floor branch

**Run:** `20260922T234808Z-fleet02-B08-qform-diffuse-r17`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control used for prepublication check:** revision `2026-09-22.15`  
**Assignment:** Diffuse eigenvector case / complementary constructions and source-valid counterexamples  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_THEOREM / FULL TARGET OPEN`  
**Execution context:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository retrieval is transport/context, not native learned-memory ingestion under the programme protocol).

## 1. Target and first unpaid implication

The full target remains OPEN: for arbitrary independent real coordinates with probability densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential bound for the density of `X^T A X`, or give a target-valid counterexample. No moments, support bounds, centering, log-concavity, continuity of input densities, or independence after spectral rotation may be inserted.

The preceding B08 run paid a spread-out double-incident determinant bank when the surviving physical cross block has exact rank two. Its remaining tail-stability question cannot be solved by simply deleting a small Hilbert--Schmidt cross tail. Since then the designated partner fleet03/B08 proved a newer structural theorem, `QFORM-DIFFUSE-CURVATURE-TRANSFER-LADDER-v1`, which moves the first structural debt upstream: for a balanced physical cut of three genuine large eigenvectors, failure of principal curvature forces multiple singular directions in the **actual** original-coordinate cross block.

This run closes a precise branch of that newer debt. The new theorem pays an arbitrary full cross block of rank `r>=3` whenever its nonzero singular spectrum has a positive floor. In particular, an actual rank-three cross block with three singular values bounded below is completely paid, including arbitrary same-side quadratic terms and arbitrary outside couplings. The proof is product-preserving and does not condition on spectral coordinates.

The remaining gap is now sharply identified: partner curvature transfer controls the top three cross singular values, while the theorem below pays the full nonzero cross spectrum. Therefore the still-unpaid cross case is exactly the presence of additional arbitrarily small singular directions. This is the genuine truncation/tail-stability interface; no small-coefficient phase perturbation is assumed.

## 2. Source-pinned dependencies actually used

### 2.1 Designated partner fleet03/B08 r24

Canonical proof: `yspennstate/math-open-problems@1bf6f41d81ffddcc6e8ff93b4df165d0ce5bbd05`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B08/20260922T231729Z-fleet03-B08-qform-diffuse-r24/REPORT.md`.

Its theorem states: if `A R=R Lambda`, `R^T R=I_3`, `min_j |lambda_j|>=L`, and a physical cut `I|J` satisfies

`alpha I <= G_I=R_I^T R_I, G_J=I-G_I <=(1-alpha)I`,

then for each `m=1,2,3` and each `0<c<L rho`, with `rho=sqrt(alpha/(1-alpha))`, either `A[I,I]` has at least `m` eigenvalues of modulus at least `c`, or the actual cross block `B=A[I,J]` has at least `4-m` singular values larger than

`alpha(L rho-c)`.

For selected-frame row leverage `mu<=1/48`, the source supplies `alpha=3/8`; with

`c=(L/2)sqrt(3/5)`,

failure of even one principal direction forces

`s_3(B) > beta L`,
`beta=(3/16)sqrt(3/5)=0.145236875482778...`.

This exact inequality is applied in Section 5.

### 2.2 Product-projection density cap

Canonical proof: fleet02/B06 `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`,
`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

If `P` is an `N x r` matrix with orthonormal columns and `W` has independent coordinate densities bounded by one, then `P^T W` has a joint density `g` satisfying

`||g||_infinity <= exp(r/2)`.

The proof is geometric Brascamp--Lieb on original-coordinate affine fibers. It asserts no independence of the projected coordinates.

## 3. New theorem: pay the entire nonzero cross spectrum

Let `I,J` be disjoint sets of ORIGINAL coordinates. Condition only on coordinates outside `I union J`. The surviving conditional form is

`R(U,V)=F(U)+2 U^T B V+G(V)+c`,                                      (3.1)

where `U=X_I`, `V=X_J`, `F,G` are arbitrary real quadratic-affine functions, and the laws of coordinates within `U` and within `V` remain independent products with one-dimensional density caps one. Let

`r=rank(B)>=3`,

and let the nonzero singular values of `B` be

`s_1>=...>=s_r>0`.

### Theorem 3.1 — `QFORM-CROSSBLOCK-SPECTRAL-FLOOR-v1`

The conditional law in (3.1), uniformly in the outside conditioning, has a bounded continuous density and

`boxed(
 ||p_R||_infinity
 <= e * r/(r-2) * (product_{nu=1}^r s_nu)^(-1/r).
)`                                                                    (3.2)

Consequently the unconditional full quadratic form has the same bound. In particular, if every nonzero singular value of `B` is at least `sigma>0`, then

`boxed(
 ||p_R||_infinity <= 3e/sigma.
)`                                                                    (3.3)

The theorem retains arbitrary same-side blocks and affine terms. It uses no moments, support bounds or post-rotation independence.

### Proof

Take a thin singular-value decomposition of the **entire** nonzero cross block,

`B=P D Q^T`,
`P^T P=Q^T Q=I_r`,
`D=diag(s_1,...,s_r)`.                                                (3.4)

Define the spectral projections only as integration variables,

`Y=P^T U`, `Z=Q^T V`.                                                (3.5)

We do **not** claim that the coordinates of `Y` or `Z` are independent. By the completed product-projection theorem in Section 2.2, they possess joint densities `g_Y,g_Z` with

`||g_Y||_infinity, ||g_Z||_infinity <= e^(r/2)`.                     (3.6)

Disintegrate the original product laws over these projections and absorb all same-side phases into conditional amplitudes:

`a_t(y)=g_Y(y) E[ exp(i t F(U)) | Y=y ]`,
`b_t(z)=g_Z(z) E[ exp(i t G(V)) | Z=z ]`.                            (3.7)

Then

`|a_t(y)|<=g_Y(y)`, `|b_t(z)|<=g_Z(z)`,                              (3.8)

and, because `g_Y,g_Z` are probability densities,

`||a_t||_2 <= ||g_Y||_2 <= e^(r/4)`,
`||b_t||_2 <= ||g_Z||_2 <= e^(r/4)`.                                (3.9)

The crucial point is that (3.4) contains the **entire** cross block. Therefore the cross phase depends only on `(Y,Z)`:

`U^T B V=Y^T D Z`.                                                   (3.10)

Hence the conditional characteristic function is

`phi_R(t)=e^(itc) int int a_t(y)b_t(z) exp(2it y^T D z) dy dz`.      (3.11)

Use the Fourier convention `hat f(xi)=int exp(i xi dot y) f(y)dy`. For fixed `z`, the `y` integral is `hat a_t(2tDz)`. Cauchy--Schwarz in `z`, the change of variables `xi=2tDz`, and Plancherel give

`|phi_R(t)|
 <= ||b_t||_2
    [ int |hat a_t(2tDz)|^2 dz ]^(1/2)
 =  pi^(r/2) |t|^(-r/2) (det D)^(-1/2)
    ||a_t||_2 ||b_t||_2`.                                           (3.12)

Insert (3.9):

`|phi_R(t)|
 <= A |t|^(-r/2)`,
`A=(pi e)^(r/2) (product s_nu)^(-1/2)`.                             (3.13)

Together with the trivial `|phi_R(t)|<=1`,

`|phi_R(t)|<=min(1,A|t|^(-r/2))`.                                  (3.14)

Since `r>2`, this envelope is integrable. Put `T=A^(2/r)`. On the positive half-line,

`int_0^infinity min(1,A t^(-r/2))dt
 =T + A int_T^infinity t^(-r/2)dt
 = T * r/(r-2)`.                                                    (3.15)

Thus

`||phi_R||_1
 <=2r/(r-2) A^(2/r)
 =2pi e r/(r-2) (product s_nu)^(-1/r)`.                            (3.16)

Fourier inversion yields a bounded continuous density, vanishing at infinity, with

`||p_R||_infinity
 <=(2pi)^(-1)||phi_R||_1
 <=e r/(r-2)(product s_nu)^(-1/r)`,                                (3.17)

which is (3.2). If every `s_nu>=sigma`, then the geometric mean is at least `sigma`, while `r/(r-2)<=3` for every integer `r>=3`, giving (3.3). The estimate is uniform in the outside ORIGINAL-coordinate conditioning, so averaging those conditional densities gives the same unconditional essential bound. QED.

### Why the full-rank condition matters

The proof does not discard any cross singular directions. If one keeps only the top three singular vectors of a higher-rank block, then the omitted tail still couples the two conditional product fibers and (3.11) acquires a nonfactorized amplitude depending jointly on `y,z`. With arbitrary cap-one laws and no moments, small coefficient norm does not make that amplitude pointwise close to one. Thus Theorem 3.1 closes a genuine spectral-floor boundary but does not smuggle in the still-open tail-stability implication.

## 4. Rank-three corollary

If `rank(B)=3`, then

`boxed(
 ||p_R||_infinity <= 3e (s_1s_2s_3)^(-1/3).
)`                                                                    (4.1)

In particular, `s_3(B)>=sigma` gives

`||p_R||_infinity <=3e/sigma`.                                      (4.2)

This is a direct three-dimensional bilinear analogue of the earlier exact-rank-two `L^3` theorem: rank two gives the borderline `|t|^-1` characteristic-function decay and only an `L^3` density, while rank three gives `|t|^-3/2`, which is integrable and therefore yields `L^infinity` directly. This is another exact manifestation of the three-curvature threshold.

## 5. Actual application of the designated partner result

Apply fleet03/B08 r24 at its clean diffuse threshold. Let three selected eigenvectors satisfy

`max_i ||R_{i,*}||^2 <=1/48`,
`min_j |lambda_j|>=L`.                                               (5.1)

The partner supplies a physical cut `I|J` with `alpha=3/8`. Set

`rho=sqrt(3/5)`,
`c=(L/2)rho`,
`beta=(3/16)rho`.                                                     (5.2)

If the principal child `A[I,I]` has **no** eigenvalue of modulus at least `c`, the partner theorem with `m=1` gives

`s_3(B)>beta L`, `B=A[I,J]`.                                        (5.3)

Therefore, in the source-valid subbranch in which either

1. `rank(B)=3`, or more generally
2. every nonzero singular value of `B` is at least `beta L`,

Theorem 3.1 gives the actual full-form inequality

`boxed(
 ||p_(X^T A X)||_infinity
 <= 3e/(beta L)
 = 16 e sqrt(5/3) / L
 = 56.1485880102... / L.
)`                                                                    (5.4)

The arbitrary complementary spectrum of `A`, arbitrary self blocks on `I,J`, and arbitrary outside original-coordinate couplings are all retained. No exact-rank-three hypothesis on the full matrix is imposed.

Thus the partner's cross-curvature alternative is now completely paid whenever the actual cross block has no tiny nonzero tail. The only part not covered by (5.4) is a higher-rank cross block whose first three singular values are `>=beta L` but which also has additional nonzero singular values below that floor.

## 6. Explicit full-rank delocalized target family

The theorem is not merely an exact-rank-three-matrix statement. Let `m=128` and let `P` be the first three normalized columns of the `128 x128` Sylvester--Hadamard matrix, so `P^T P=I_3` and every row has squared norm `3/m`. Set `delta=1/10` and define on `R^m direct_sum R^m`

`A = [[ delta(I-PP^T),  PP^T ],
     [ PP^T,            delta(I-PP^T) ]]`.                           (6.1)

Then:

* on `span(P) direct_sum span(P)`, the spectrum is `+1` with multiplicity three and `-1` with multiplicity three;
* on the orthogonal complements, the spectrum is `delta` with multiplicity `2m-6`;
* hence `A` is full rank and target-valid, with arbitrarily many additional small nonzero eigenvalues;
* selecting the three `+1` eigenvectors `(Pv,Pv)/sqrt(2)` gives maximum selected-frame leverage
  `3/(2m)=3/256<1/48`;
* for the natural half cut, each principal block is `delta(I-PP^T)`, so it has no eigenvalue of modulus at least
  `c=(1/2)sqrt(3/5)=0.387298...`;
* the actual cross block is `PP^T`, exactly rank three, with all three nonzero singular values equal to one.

Thus the designated partner's `m=1` cross-curvature branch is genuinely active, and Theorem 3.1 gives the much sharper family-specific bound

`boxed(||p_(X^T A X)||_infinity <=3e=8.1548454853... )`             (6.2)

for every independent cap-one product law. This family lies outside any theorem requiring the entire range projection of `A` to be diffuse, because `A` is full rank and that projection is the identity.

## 7. First remaining implication

The first unpaid implication is now

**`QFORM-DIFFUSE-CROSS-SPECTRAL-TRUNCATION-STABILITY-v1` — OPEN.**

In the partner r24 balanced-cut branch, assume only the forced conclusion `s_3(B)>=beta L`; allow arbitrary additional nonzero singular values below `beta L`. Transfer the full-cross Fourier payment above to this situation without conditioning on spectral coordinates, without pointwise deletion of the small singular tail, and without moments. Equivalently, find a product-preserving argument that pays only a three-singular-value floor while retaining the remaining cross phase exactly, or construct a genuine product-source counterexample.

This is strictly narrower than the previous vague tail-stability debt: Theorem 3.1 proves that **all** higher cross directions are harmless if they share the floor, and rank exactly three is completely solved. What remains is only a spectrally small nonzero tail attached to three already-paid cross directions.

## 8. Checks, failure modes, and status

The accompanying checker verifies the Hadamard construction, selected leverage, full spectrum, cross rank, partner constants, and the numerical bounds. It is an arithmetic/finite-dimensional consistency check, not a proof of Theorem 3.1.

Failure modes explicitly avoided:

- no post-rotation independence is asserted; only a joint projection-density cap is used;
- no arbitrary-joint coarea inequality is used;
- no conditional projection-density positive moment is used;
- no pointwise scalar quadratic-phase decay is used;
- no fixed physical minor is selected;
- no small Hilbert--Schmidt cross tail is discarded;
- conditioning is only on original coordinates outside the active physical banks.

**New result:** `QFORM-CROSSBLOCK-SPECTRAL-FLOOR-v1`, proved.  
**Designated partner applied:** fleet03/B08 r24 `QFORM-DIFFUSE-CURVATURE-TRANSFER-LADDER-v1`, yielding (5.4).  
**Explicit target family:** full-rank Hadamard two-bank family, density bound `<=3e`.  
**Full QFORM target:** OPEN / not proved / not disproved.  
**Continuity:** proved in the new spectral-floor branch because the characteristic function is `L^1`.

Privacy/secret review before publication: manual narrow review of this report and the accompanying checker/output found only logical fleet labels, public repository commit identifiers, mathematics and nonsecret constants. No credentials, signed URLs, machine paths, scheduler identifiers, private transcripts or unrelated personal data are included. Repository-native automated privacy tooling was not exposed through the connector, so no broader scan is claimed.
