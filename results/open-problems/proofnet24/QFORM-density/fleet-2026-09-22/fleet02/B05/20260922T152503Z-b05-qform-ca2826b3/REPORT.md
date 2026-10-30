# fleet02/B05 — bounded-overlap obstruction to pair-Pluecker coarea aggregation

**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Run:** `20260922T152503Z-b05-qform-ca2826b3`  
**Assignment:** Quadratic coarea bound / complementary constructions and source-valid counterexamples  
**Classification:** `CANDIDATE_REFUTED / SUPPORTING_THEOREM_PROVED / PRECISE_MISSING_FACTOR_IDENTIFIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval/write is not native learned-memory receiver use.

## 1. Exact target, corrections, and source pins

The sole target is the full arbitrary-dimension statement: for independent real coordinates with scalar densities bounded by one and any real symmetric matrix with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `X^T A X`, or give a valid target counterexample. No moment, support, diagonal-basis, sign, or post-rotation-independence assumption is used here.

Live corrections consumed include the failure of law-uniform pointwise Fresnel decay, the dimension loss from unrestricted fiber suprema, the failure of conditional density caps to replace genuine independence, the failure of one local cross/minor as a universal structural certificate, and the failure of pre-pivot two-cross survival under Schur completion. In particular, this report never conditions on a transformed spectral coordinate and then treats it as independent.

The assigned partner result actually applied is fleet03/B05 `QFORM-PAIR-SECTIONAL-COAREA-v1`, canonical source `yspennstate/math-open-problems@332f29e335274f2b3f81ccf92d62443b928c66cd`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260922T144946Z-qform-B05-a03-r12/REPORT.md`. Its exact-rank-three heavy-isotropic application gives, for every residual physical pair with

`Delta_jk = y_j z_k - y_k z_j != 0`,

an original-coordinate conditional density bound proportional to `|Delta_jk|^(-2/3)`, while the exact Cauchy-Binet identity is

`sum_{j<k} Delta_jk^2 = 1`.

The first unpaid implication at entry was therefore the partner's `QFORM-PAIR-PLUCKER-AGGREGATION-v1`: aggregate the total pair-Pluecker mass before reciprocal local-minor payment while retaining shared-coordinate product provenance.

For comparison and for source-validity of the stress family below, I also apply fleet03/B07 `QFORM-PLUCKER-COLLAR-TRICHOTOMY-v1`, canonical source `yspennstate/math-open-problems@c3b0a3023962496543da62be43f07bff5ca0865b`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/fleet03-B07-20260922T124045Z-qform-minors-v11/REPORT.md`.

## 2. Conditional end-to-end argument and the exact first missing factor

A natural way to turn the partner's pair theorem into a dimension-free global coarea estimate would be to choose many pair sections but keep coordinate reuse bounded, so that a Finner/Hölder or independent-block argument can still respect the original product law. Abstractly, one would seek nonnegative pair weights `alpha_jk` with bounded vertex load

`sum_{k != j} alpha_jk <= L = O(1)`

and with a constant fraction of the total Pluecker curvature captured:

`sum_{j<k} alpha_jk Delta_jk^2 >= c_0 > 0`.

A slightly more flexible version first partitions or fractionally covers the residual coordinates by bounded-congestion blocks on each of which the leakage coordinate is exactly absorbable into the two transverse coordinates, then applies sectional coarea inside the blocks.

If either bounded-congestion statement were true uniformly, the partner pair estimate could be aggregated without paying for a vanishing single minor. The present run proves that both statements are false in a genuine target family. The exact missing factor is **coordinate overlap of order the ambient residual dimension**: on the stress family, any sectional scheme whose per-coordinate load is bounded independently of `m` captures only `O(1/m)` of the unit Pluecker mass.

Thus the next successful coarea mechanism must be genuinely global/overlap-tolerant. It cannot be a disjoint-pair, matching, bounded-color, or bounded-load exact-sectional reduction in disguise.

## 3. Target-valid Fourier-frame stress family

Fix `c=3/4` and an integer `m>=5`. Put `theta_j=2*pi*j/m`, `0<=j<m`, and define residual coefficient vectors

`y_j = sqrt(2/m) cos(theta_j)`,

`z_j = sqrt(2/m) sin(theta_j)`,

`s_j = sqrt(2(1-c)/m) cos(2 theta_j)`.

Let the spectral frame have one distinguished heavy row and `m` residual rows:

`u_0 = sqrt(c) e`,

`u_j = s_j e + y_j f + z_j g` for `1<=j<=m`,

where `(e,f,g)` is an orthonormal spectral basis. Discrete Fourier orthogonality gives

`||s||_2^2=1-c`, `||y||_2=||z||_2=1`,

`<s,y>=<s,z>=<y,z>=0`.

Hence, for the `(m+1) x 3` row frame `U`,

`U^T U = I_3`.

Choose

`Lambda = [[0,1,0],[1,0,0],[0,0,1]]`.

Its eigenvalues are exactly `{-1,1,1}` and `det Lambda=-1`. Therefore

`A_m = U Lambda U^T`

is a real symmetric rank-three target matrix with three eigenvalues of modulus exactly one. The distinguished physical pivot is exactly isotropic:

`(A_m)_{00}=c e^T Lambda e=0`.

With arbitrary independent cap-one input laws this is a genuine instance of the owner target. For an explicit source-valid law one may take all coordinates uniform on `[-1/2,1/2]`; no property of that special law is used in the structural obstruction.

In the partner's heavy-isotropic notation this family has `B=1`, `tau=1`, and

`Q = 2 (sqrt(c) X_0 + T) Y + Z^2`,

where `T=sum s_j X_j`, `Y=sum y_j X_j`, `Z=sum z_j X_j`.

## 4. Exact Pluecker geometry

For every residual pair,

`Delta_jk = y_j z_k - y_k z_j
          = (2/m) sin(theta_k-theta_j)`.

Consequently

`|Delta_jk| <= 2/m`,

while Cauchy-Binet (or direct Fourier summation) gives the exact total mass

`sum_{j<k} Delta_jk^2 = 1`.

This is the same diffuse regular-polygon obstruction observed by the partner, but the next lemma quantifies how much overlap an aggregation scheme must spend.

### Theorem 4.1 — `QFORM-PAIR-PLUCKER-OVERLAP-OBSTRUCTION-v1`

For the family above:

1. If `alpha_jk>=0` and each residual coordinate has fractional pair load at most `L`,

   `sum_{k != j} alpha_jk <= L` for every `j`,

   then

   `sum_{j<k} alpha_jk Delta_jk^2 <= 2L/m`.

2. Call a coordinate block `K` **exactly absorbable** when the leakage restriction is representable by the two transverse restrictions,

   `s_K in span{y_K,z_K}`.

   Every exactly absorbable block has `|K|<=4`.

3. More generally, for nonnegative block weights `omega_K` supported on exactly absorbable blocks, if the total block load of each residual coordinate is at most `L`,

   `sum_{K containing j} omega_K <= L`,

   then the total internal Pluecker mass counted by those blocks satisfies

   `sum_K omega_K sum_{j<k in K} Delta_jk^2 <= 6L/m`.

Therefore any pair/block exact-sectional scheme that captures a fixed positive fraction `eta` of the unit total Pluecker mass must have coordinate congestion at least `eta*m/6` (and at least `eta*m/2` in the pure pair/fractional-matching case).

#### Proof

For (1), the vertex-load bound implies

`2 sum_{j<k} alpha_jk = sum_j sum_{k != j} alpha_jk <= Lm`.

Since every `Delta_jk^2<=4/m^2`,

`sum alpha_jk Delta_jk^2 <= (4/m^2)(Lm/2)=2L/m`.

For (2), exact absorbability means that there exist constants `A,B` such that for every `j in K`, after cancelling the harmless nonzero scalings,

`cos(2 theta_j) = A cos(theta_j)+B sin(theta_j)`.

The trigonometric polynomial

`F(theta)=cos(2theta)-A cos(theta)-B sin(theta)`

has degree two and is not identically zero. Multiplying its Laurent representation by `z^2` turns it into a nonzero ordinary polynomial of degree at most four. Hence `F` has at most four distinct zeros on the unit circle, so `|K|<=4`.

For (3), use `Delta_jk^2<=4/m^2` and, for `|K|<=4`,

`binom(|K|,2) <= (3/2)|K|`.

Thus

`sum_K omega_K sum_{j<k in K} Delta_jk^2
 <= (4/m^2) sum_K omega_K binom(|K|,2)
 <= (6/m^2) sum_K omega_K |K|
 =  (6/m^2) sum_j sum_{K containing j} omega_K
 <= 6L/m`.

This proves all three claims.

## 5. What this falsifies, and what it does not

The theorem is a source-valid counterexample to the structural implication

> unit total Pluecker mass can always be converted into a constant-curvature family of exact pair/block coarea sections with `O(1)` coordinate congestion.

It also rules out the common refinements “choose a matching”, “use finitely many matchings/colors”, and “use a fractional matching/Finner cover with bounded vertex load” as dimension-free resolutions of the partner's reciprocal-minor tax. To capture constant mass on this family, such a method must reuse some coordinates `Omega(m)` times. Any proof that then invokes Hölder/Finner independently on each reused section must account for that growing overlap instead of silently treating the sections as independent.

This theorem is **not** a counterexample to QFORM and does not disprove an overlap-tolerant multi-pair coarea inequality. It only removes a broad class of bounded-overlap aggregation mechanisms.

## 6. Independent check that the stress family itself is harmless

The stress family is deliberately a mechanism falsifier, not a candidate target counterexample. In fact fleet03/B07's aggregate retained-frame theorem closes it for every `m>=8`.

Condition on the distinguished heavy coordinate `X_0`. The retained residual Gram matrix is

`G = diag(1-c,1,1)`, so `q=det G=1-c=1/4`.

After whitening, residual row `j` has leverage

`ell_j = s_j^2/(1-c)+y_j^2+z_j^2
       = (2/m)(1+cos^2(2 theta_j))
       <= 4/m <= 1/2`.

Therefore B07's diffuse aggregate bound applies uniformly in the conditioned value and gives

`||p_Q||_infinity <= 3e (q |det Lambda|)^(-1/3)
                   = 3e * 4^(1/3)
                   < 12.946`.

So the exact family that destroys bounded-overlap pair extraction is already uniformly controlled by a genuinely global aggregate determinant mechanism. This cleanly identifies the correct lesson: **aggregation must precede local reciprocal determinant payment.**

The newer ridge-window theorem advertised in fresh controls was also checked for scope. Its full-range leverage hypothesis is not met by this family because of the distinguished row of leverage `c=3/4`; no unsupported transfer of that theorem is made here.

## 7. Relation to the preceding B05 theorem

The previous fleet02/B05 result, source `yspennstate/math-open-problems@d88444f6ee8744b72a46448734db26349baabdd7`, proved fractional half-Riesz bounds from controlled post-Schur cross singular values and already showed that one cannot assume two pre-pivot cross directions survive a scalar Schur update.

The present result changes the mechanism: instead of searching for another local cross block, it tests whether the partner's exact `sum Delta^2=1` identity can be harvested through low-overlap sectionalization. The answer is no, quantitatively. The loss is not merely that `max |Delta|` can be `O(1/m)`; even the **entire bounded-congestion collection** carries only `O(1/m)` squared Pluecker mass.

## 8. First unpaid implication after this run

The coarea debt is now

**`QFORM-OVERLAP-TOLERANT-PLUCKER-COAREA-v1` — OPEN.**

Prove a global coarea/small-ball inequality that can exploit

`sum_{j<k} Delta_jk^2=1`

while the useful pair sections overlap each physical coordinate `Omega(m)` times, without paying an `m`-dependent Hölder/Finner/congestion loss; or replace pair sectionalization by a global retained-frame/regularized-determinant mechanism before reciprocal minor inversion. The inequality must preserve original-coordinate product provenance and remain valid with mixed leakage. A source-valid counterexample to such an overlap-tolerant inequality would be equally decisive.

For the full owner target, arbitrary additional spectral components beyond the chosen rank-three core remain a separate interaction debt. The full conjecture and continuity remain OPEN.

## 9. Diagnostic computation

The proof above is analytic. A finite numerical checker was nevertheless run as a sanity check for `5<=m<=200`. It verifies `U^TU=I`, total Pluecker mass one, `max Delta^2<=4/m^2`, and the nonzero spectrum `{-1,1,1}`. It does not prove the theorem.

Checker source in this run directory: `check_overlap_obstruction.py`, blob `9479c2ae29084e388b5974a7f69d85013b7ea739`.

Exact recorded output in `checker_output.txt`, blob `837643092e6431d2d19325989f7dd0e1409296c9`:

```text
m_range=5..200
max_frame_gram_error=3.331e-15
max_plucker_sum_error=4.441e-16
max_delta_sq_minus_4_over_m2=6.939e-18
max_nonzero_spectrum_error=2.442e-15
pair_fractional_matching_bound=2L/m
exact_absorption_block_congestion_bound=6L/m
QFORM_B05_OVERLAP_OBSTRUCTION_PASS
```

## 10. Integrity and status

Changed-file review found only this mathematical report, its checker, and its text output; no credentials, scheduler identifiers, machine paths, private unrelated material, benchmark gold, email/Drive content, or public-release action is present. No task/schedule/permission/notification mutation was performed.

**Result status:** `CANDIDATE_REFUTED / SUPPORTING_THEOREM_PROVED`. The bounded-overlap exact-sectional route to pair-Pluecker aggregation is rigorously false. The exact missing factor is linear coordinate congestion. Full QFORM remains `OPEN / NOT PROVED`.
