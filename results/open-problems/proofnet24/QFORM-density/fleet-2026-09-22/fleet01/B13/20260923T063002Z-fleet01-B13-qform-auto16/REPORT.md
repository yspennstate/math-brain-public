SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T06:30:02Z.
attacking: extend the scalar-Schur E2 entropic payment from row-marginal cap h<3/4 to the full natural range h<1, then compress every nonpaid E2 survivor from three hubs to two hubs per side.

# fleet01/B13 auto16 — h<1 entropic E2 smoothing and a two-hub Schur obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh owner control before publication: revision `2026-09-22.15`, QFORM-only.  
Execution: `WITHOUT_VERIFIED_BRAIN`.  
Status: **PROVED SUPPORTING TARGET-LEVEL THEOREMS / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

## 1. Scope and source boundary

The target remains: for arbitrary dimension, independent original-coordinate real random variables with probability densities bounded by one, and an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite density bound or construct a valid counterexample. No moments, bounded supports, interval supports, log-concavity, centered laws, post-rotation independence, or fixed-fragment hypotheses are introduced here.

The live corrections are respected. In particular this report does not use law-uniform pointwise quadratic oscillatory decay, arbitrary-joint coarea, conditional projection-density moments, a fixed-good-minor reduction, bounded-diameter continuity, or deletion of small quadratic coefficients on translated supports.

Completed inputs used at their proved scope:

1. Designated partner `fleet02/B13` r23, canonical report commit `892bfe36756e09cbaff3f05070f7a3e20fea0fd1`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T040105Z-fleet02-B13-extremal-r23/REPORT.md`. I use its exact rank-one Schur E2-loss identity in Section 6 below, and its product-law purification as a consistency check on the extremal front end.
2. `fleet03/B13` r23, visible at `math-open-problems@85c3d540cf82ea6a6aca0f22f31811516a8b81aa`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T034405Z-fleet03-B13-qform-r23/REPORT.md`. Its derivation of the entropy-weighted E2 characteristic-function envelope is reused, but I observe that the envelope itself remains valid for every `h<1`; the earlier `h<3/4` restriction enters only when that report fixes the Fourier exponent `3/2` in order to get an `L^3` density.
3. `QFORM-DEPENDENT-SQUARE-LP-v1`, visible at `math-open-problems@85c3d540cf82ea6a6aca0f22f31811516a8b81aa`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260922T141530Z-two-samesign-threeblock/REPORT.md`. It turns any Schur remainder density in `L^p`, `p>2`, into an `L^infinity` density after a genuine original-coordinate scalar square.

## 2. Exact extremal-product reduction used throughout B13

Let

`F={f: 0<=f<=1 a.e., integral_R f=1}`.

For every bounded nonnegative measurable kernel `K:R^n->[0,infinity)`,

`sup_(f_1,...,f_n in F) integral K(x) product_i f_i(x_i) dx`
` = sup_(|E_1|=...=|E_n|=1) integral_(product_i E_i) K(x) dx`.      (2.1)

Proof: with all but one marginal fixed, the functional is `integral g(x)f(x)dx` with `g>=0` bounded. The one-dimensional bathtub principle on nonatomic Lebesgue space says its supremum over `0<=f<=1`, `integral f=1`, equals the supremum of `integral_E g` over measurable `|E|=1`. Apply this coordinate by coordinate. QED.

For `K=1_{Q in J}`, (2.1) is the exact geometric reduction relevant here. It does **not** reduce to a single interval, centered uniform law, bounded diameter, or bounded number of components. The partner's finite-mixture/no-attainment theorem gives a compatible approximating implementation by bounded finite unions, but (2.1) itself is an exact equality of suprema.

## 3. Analytic extension: the E2 characteristic-function envelope works for h<1

Let `R` be a quadratic polynomial in independent cap-one original coordinates. Choose disjoint original-coordinate banks and let `M` be their physical cross block. Let `mu` be a probability law on the nonzero physical `2x2` minors of `M`. Write

`alpha_i=P_mu(i belongs to row pair)`,

and assume

`alpha_i<=h`, with `1/2<=h<1`.                                    (3.1)

Put

`q=2h in [1,2)`,

`K_2(mu)=exp(H(mu)+E_mu log det(M[P,T])^2)`.                      (3.2)

The fleet03/B13 r23 proof through its equation (3.8) uses only `q>=1` and `q/alpha_i>=2`; both remain true under (3.1). The restriction `h<3/4` in that report is used only after (3.8), when integrating the fixed power `|phi|^(3/2)`. Thus for the larger range (3.1) we retain the proved envelope

`|phi_R(t)| <= min{1, A K_2(mu)^(-1/(4q)) |t|^(-1/q)}`,           (3.3)

where

`A=[e(2pi)^2/q]^(1/(2q))`.                                       (3.4)

This simple observation is the door to the two-hub improvement: instead of insisting on an `L^3` remainder, choose a Fourier exponent strictly between `q` and `2`.

## 4. New theorem: scalar pivot plus entropic E2 for every h<1

### Theorem 4.1 — `QFORM-SCALAR-E2-ENTROPIC-LP-LINF-v1`

Let `d=A_kk!=0` be an original-coordinate scalar pivot. Complete the square in the physical coordinate `X_k`:

`Q=d V^2+R`,

`V=X_k+d^(-1)A[k,-k]X_-k`,

`R=X_-k^T S X_-k + (possible affine/constant terms)`,             (4.1)

where `S` is the scalar Schur complement. Let `M=S[I,J]` be a physical cross block on disjoint original-coordinate banks, and let `mu` satisfy (3.1). For every Fourier exponent

`r in (2h,2)`,                                                     (4.2)

put

`beta=1-r/2`,

`D_r=(2/r) beta^(-1/2) [r/(2 beta)]^beta`.                        (4.3)

Then

`boxed:
 ||p_Q||_infinity
 <= C(h,r) |d|^(-1/2) K_2(mu)^(-1/8),
`

where

`C(h,r)=D_r [2 sqrt(e/(2h)) r/(r-2h)]^(1/2)`.                    (4.4)

The theorem retains arbitrary same-bank quadratic curvature, all affine terms created by conditioning, all signs, and arbitrary extra coordinates.

#### Proof

Set `q=2h` and let `T` be the crossover point in (3.3):

`T=A^q K_2(mu)^(-1/4)=2pi sqrt(e/q) K_2(mu)^(-1/4)`.              (4.5)

For `q<r<2`, direct integration of (3.3) gives

`||phi_R||_r^r`
` <=2T + 2 A^r K_2(mu)^(-r/(4q)) integral_T^infinity t^(-r/q)dt`
` =2T [1+q/(r-q)]`
` =2T r/(r-q)`.                                                   (4.6)

Hence

`||phi_R||_r`
` <=[4pi sqrt(e/q) r/(r-q)]^(1/r) K_2(mu)^(-1/(4r)).              (4.7)

Let `p=r/(r-1)>2`. With the Fourier convention of the completed sources, inverse Hausdorff--Young gives

`||p_R||_p`
` <=(2pi)^(-1/r)||phi_R||_r`
` <=[2 sqrt(e/q) r/(r-q)]^(1/r) K_2(mu)^(-1/(4r)).                (4.8)

The completed dependent-square lemma applies to (4.1): conditional on `X_-k`, the translated variable `V` has density at most one because its only fresh randomness is the original independent `X_k`; mixing down to conditioning on `R` preserves that cap. Since the conjugate exponent in that lemma is exactly `r`,

`||p_Q||_infinity <= |d|^(-1/2) D_r ||p_R||_p^(r/2)`.            (4.9)

Insert (4.8). The power `r/2` cancels the `1/r` and changes `K_2^(-1/(4r))` into `K_2^(-1/8)`, giving exactly (4.4). QED.

### Why this extension matters

The old `L^3` implementation needed `2h<3/2`, i.e. `h<3/4`. The present proof only needs some `r` with

`2h<r<2`,

which is possible for **every `h<1`**. Thus the analytic cap reaches the natural endpoint short of a row appearing with probability one. This is not merely a constant improvement: it reduces the finite concentration obstruction from three hubs to two.

## 5. Entropy-or-two-hub corollary

The structural entropy-projection proof in fleet03/B13 r23 also extends without change from `h<3/4` to `h<1`: that proof uses only fractional matching/vertex-cover duality and the cap value `h`. In particular, if the cap-feasible set is empty, a hub set has cardinality `<2/h`; if it is nonempty but every cap-feasible law has KL cost greater than `L`, the dual set `H={i:lambda_i>=hR/2}` has cardinality at most `2/h` and deleting `H` leaves less than `e^(-L)` of the natural E2 mass.

Take the concrete rational values

`h=67/100`, `q=67/50`, `r=87/50`, `L=log 4`.                    (5.1)

Then every failure of the entropic payment produces at most **two** hubs because `2/h=200/67<3`.

Let

`E=e_2(M^T M)=sum_(|P|=|T|=2) det(M[P,T])^2`.                    (5.2)

If a cap-feasible law has `D(mu||w_2)<=log4`, then

`K_2(mu)=E exp[-D(mu||w_2)] >= E/4`.                              (5.3)

For (5.1), formula (4.4) gives the pre-KL constant

`C(67/100,87/50)=14.3678235381...`.                              (5.4)

After (5.3),

`boxed:
 ||p_Q||_infinity
 <=17.086317979 |d|^(-1/2) E^(-1/8).
}`                                                                      (5.5)

If (5.5) fails in the row orientation, there is a row-hub set `H`, `|H|<=2`, touching more than `3E/4` of the squared-minor mass. Apply the same statement to `M^T`. Unless the density is already paid in that orientation, there is a column-hub set `C`, `|C|<=2`, touching more than `3E/4`. By the union bound, more than half the natural E2 mass consists of minors whose row pair meets `H` **and** whose column pair meets `C`:

`boxed:
 sum_(P cap H != empty, T cap C != empty) det(M[P,T])^2 > E/2,
 |H|,|C|<=2.
}`                                                                      (5.6)

This is `QFORM-SCALAR-E2-LINF-OR-TWOHUB-v1`. It strictly sharpens the previous three-row/three-column obstruction.

### Exact hub-pair compression identity

A further deterministic compression costs only a factor four. From (5.6), some `h0 in H`, `c0 in C` obey

`sum_(i!=h0,j!=c0)
 (M[h0,c0] M[i,j]-M[h0,j]M[i,c0])^2 > E/8`.                       (5.7)

Indeed every minor in (5.6) is assigned to at least one of at most four pairs `(h0,c0)`. Writing

`a=M[h0,c0]`, `u=(M[h0,j])_(j!=c0)`, `v=(M[i,c0])_(i!=h0)`,
`N=(M[i,j])_(i!=h0,j!=c0)`,

(5.7) is the exact Frobenius identity

`boxed: ||aN-vu^T||_F^2 > E/8.`                                  (5.8)

No single large minor is selected. The whole aggregate star currency is retained.

## 6. Actual application of designated partner fleet02/B13: Schur survive / two-hub / star

Use fleet02/B13 r23's exact rank-one Schur identity. Suppose a pre-Schur physical cross block `N` and the actual scalar-Schur cross block `S` are related by

`N=S+xy^T`.                                                       (6.1)

Put

`E_0=e_2(N^T N)`, `E=e_2(S^T S)`,

and

`D_*^2=||wedge^2 N-wedge^2 S||_F^2`
`     =||x||^2||y||^2||P_(x^perp) S P_(y^perp)||_F^2`.           (6.2)

The partner's exact exterior identity plus triangle inequality gives

`sqrt(E_0)<=sqrt(E)+D_*`.                                         (6.3)

There are now three possibilities.

**(i) E survives and is diffuse.** If `E>=E_0/4` and one orientation admits the entropy law from Section 5, then (5.5) yields

`boxed:
 ||p_Q||_infinity
 <=20.319170910 |d|^(-1/2) E_0^(-1/8).
}`                                                                      (6.4)

The number is `17.086317979 * 4^(1/8)`.

**(ii) E survives but is concentrated.** If `E>=E_0/4` and neither orientation is paid, then (5.6) produces two row hubs and two column hubs carrying more than `E/2`, hence more than `E_0/8`, of the actual Schur E2 mass. The stronger hub-pair identity (5.8) holds for one of at most four hub pairs.

**(iii) E is destroyed by scalar Schur descent.** If `E<E_0/4`, then (6.3) gives

`D_*>sqrt(E_0)/2`,

so the designated partner's exact transverse-star currency satisfies

`boxed: D_*^2>E_0/4.`                                             (6.5)

Thus the previous partner trichotomy with a three-by-three hub survivor is sharpened to

`QFORM-SCALAR-SCHUR-E2-SURVIVE-OR-TWOHUB-OR-STAR-v1`:

* paid density at the explicit scale (6.4), or
* at most two physical row hubs and two physical column hubs carrying `>E_0/8` of the surviving squared-minor mass, or
* exact transverse-star currency `>E_0/4`.

This is an equation-level use of the designated `fleet02/B13` completed result, not a citation-only reuse.

## 7. Geometric product-set inequality

By the exact extremal reduction (2.1), the diffuse branch (5.5) is equivalently the following slab-volume statement. For arbitrary measurable sets `E_j subset R` with `|E_j|=1` and every interval `J`,

`boxed:
 |{x in product_j E_j : x^T A x in J}|
 <=17.086318 |d|^(-1/2) e_2(M^T M)^(-1/8) |J|,
}`                                                                      (7.1)

whenever `d` is the stated physical scalar pivot and the residual physical E2 minor law has the diffuse alternative of Section 5. Under the pre-Schur survival hypothesis `E>=E_0/4`, (6.4) gives the corresponding bound with `20.319171 E_0^(-1/8)`.

Equation (7.1) is valid for arbitrary unit-measure sets: disconnected, translated, and with arbitrarily many components. There is no interval-extremizer assumption.

## 8. What is still open

The full QFORM theorem is **not** proved. The new argument reaches a natural endpoint for this route: allowing marginal cap `h<1` is exactly what is compatible with an inverse-Hausdorff--Young exponent `r<2`, and it compresses the E2 obstruction to two hubs per side. Pushing the same analytic interpolation to `h=1` would require `r>=2`, at which point the dependent-square lemma loses the `p>2` gain.

The first unpaid implication is therefore

`QFORM-SCALAR-E2-TWOHUB-STAR-CLOSURE-v1`:

> In the no/near-pivot survivor produced by the global synthesis, convert either the two-by-two physical hub packet from (5.6)-(5.8) or the exact transverse-star currency (6.5) into an already-paid grouped-bank / rank-three / mixed-row mechanism, without selecting a dimension-dependent single minor and without perturbatively deleting coefficients on unbounded product supports.

The exact identity (5.8) is the most concrete next object: it retains aggregate squared-minor mass while reducing the combinatorial support to one of four physical hub pairs. Arbitrary additional spectral directions remain retained throughout; no exact-rank-three reduction is asserted.

## 9. Numerical constant check

For `h=67/100`, `q=67/50`, `r=87/50`, `beta=13/100`,

`D_r=(2/r) beta^(-1/2) [r/(2beta)]^beta =4.08163286577...`,

`C(h,r)=14.3678235381...`,

`C(h,r) 4^(1/8)=17.0863179786...`,

`C(h,r) 4^(1/4)=20.3191709093...`.

These decimals are bookkeeping only; the proof is analytic and uses the exact formulas above.
