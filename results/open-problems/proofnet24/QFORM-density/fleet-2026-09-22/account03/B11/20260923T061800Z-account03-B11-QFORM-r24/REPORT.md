# account03/B11 r24 — balanced defect aggregation and the pure-star mixed-Fresnel receiver

Status: **ESSENTIAL_STEP_APPLIED / PROVED_STRUCTURAL_DICHOTOMY / PROVED_OPPOSITE-SIGN PURE-STAR BRANCH / PARTNER_RESULT_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.

Programme: `QFORM-DENSITY-3EIG-20260922`.  Logical worker: `account03/B11`, indefinite signatures.  The target remains the unrestricted statement for arbitrary independent cap-one real densities and arbitrary symmetric `A` with at least three eigenvalues of absolute value at least one.  Nothing below is claimed to solve that full target.


Required mathematical sources actually used:

1. Claude mixed-Fresnel theorem: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, Theorem MF / equivalent Theorem H formulation in `RESULTS.md`.
2. New volume-stability continuation: `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/` (used to identify the receiver needed after a third cross singular direction is generated; no unsupported converse is used).
3. Designated partner `account04/B11`: `yspennstate/math-open-problems@572f6cd066c9cdef7b5a509917b4dcd79cea2fda:proofnet24/QFORM-density/fleet-2026-09-22/account04/B11/20260923T021512Z-account04-B11-sign-frustrated-triangle-r4/REPORT.md`.
4. Mechanism warning, near-null scalar completion: `yspennstate/math-open-problems@2826d09f8370995686abaf5a51a9a5b38febab9:proofnet24/QFORM-density/fleet-2026-09-22/account02/B16/20260923T043305Z-account02-B16-QFORM-r25/REPORT.md`.

The main new result is a scale-free structural lemma for the sign-balanced pair-PSD chamber, followed by a product-preserving analytic receiver for its pure-star endpoint.

---

## 1. Balanced pair-PSD normalization and the defect matrix

Consider any index set on which

- `A_ii>0`,
- every physical pair is positive semidefinite, hence `|A_ij|<=sqrt(A_ii A_jj)`, and
- the signs are globally balanced: there are fixed `eps_i in {+1,-1}` for which `eps_i eps_j A_ij>=0` for every pair in the set.

Conjugating by the diagonal sign matrix `diag(eps_i)` is only a deterministic sign change of ORIGINAL independent coordinates, so it preserves independence and every density cap.  We may therefore assume

`0 <= A_ij <= sqrt(A_ii A_jj)`.

Put

`u_i=sqrt(A_ii)`,  and  `F=uu^T-A`.

Then

`F_ii=0`, `F_ij>=0`, and `A=uu^T-F`.                                      (1.1)

No lower bound on the physical diagonals is used in the next theorem.

### Theorem 1 — defect-star or disjoint second-volume dichotomy

If `s_3(A)>=s>0`, then at least one of the following holds:

**(STAR)** there is an original coordinate `i` with

`sum_{j != i} F_ij^2 >= s^2/4`;                                           (1.2)

**(CROSS-2VOL)** there is an original-coordinate bipartition `S,T` with

`e_2(F_ST^T F_ST) >= s^4/32`.                                             (1.3)

Here `S,T` are disjoint and `e_2` is the second elementary symmetric polynomial in the squared singular values, equivalently the sum of squares of all `2x2` minors.

### Proof

Because `uu^T` has rank one and `A=uu^T-F`, rank-one singular-value interlacing gives

`s_2(F) >= s_3(A) >= s`.                                                   (1.4)

Write the singular values of `F` as `sigma_1>=sigma_2>=...`, set

`V_2=e_2(F^T F)=sum_{p<q} sigma_p^2 sigma_q^2`,
`q_i=sum_{j != i}F_ij^2`,
`P=sum_{i<j}F_ij^4`.

By Cauchy-Binet, classify each squared `2x2` minor by the size of the intersection of its row and column index sets.  The identical row/column pairs contribute `P`.  If row and column pairs intersect in exactly one index `i`, the determinant is `-F_ij F_ik`; summing these terms gives `sum_i q_i^2-2P`.  Let `W` denote the contribution from disjoint row and column pairs.  Therefore the exact identity is

`V_2 = W + sum_i q_i^2 - P`.                                               (1.5)

In particular `V_2>=sigma_1^2 sigma_2^2>=s^4`.

If `sum_i q_i^2 >= V_2/2`, then since `sum_i q_i=||F||_F^2`,

`max_i q_i >= V_2/(2||F||_F^2)`.                                         (1.6)

We need a dimension-free lower bound for the last ratio.  Put `lambda_j=sigma_j^2` and `S0=sum_j lambda_j=||F||_F^2`.  Since `lambda_1>=lambda_2>=lambda_j`,

`sum_j lambda_j^2 <= lambda_1^2 + lambda_2(S0-lambda_1)`.

Hence

`2V_2=S0^2-sum_j lambda_j^2`
`    >= (S0-lambda_1)(S0+lambda_1-lambda_2)`
`    >= lambda_2 S0`.

Thus `V_2/||F||_F^2 >= sigma_2^2/2`, and (1.6) gives

`max_i q_i >= sigma_2^2/4 >= s^2/4`,

which is (STAR).

Otherwise `sum_i q_i^2<V_2/2`.  From (1.5) and `P>=0`,

`W>V_2/2`.                                                                (1.7)

Choose a random bipartition of all coordinates, independently putting each coordinate into `S` or `T` with probability `1/2`.  Every ordered disjoint `2x2` minor occurring in `W` is captured by `F_ST` exactly when its two row indices fall in `S` and its two column indices fall in `T`, an event of probability `1/16`.  Therefore

`E e_2(F_ST^T F_ST)=W/16>V_2/32>=s^4/32`.

Some deterministic cut realizes at least this value.  This proves (CROSS-2VOL).  QED.

### Meaning

This is a new structural reduction of the previously vague balanced high-leverage survivor.  It does **not** assert one uniformly good physical minor.  It says that, after the fixed-scale sign-frustrated and definite-pair exits are removed, the negative/hidden spectral content of `A=uu^T-F` must appear either as a genuinely large original-coordinate defect star or as collective disjoint `2x2` exterior volume.

---

## 2. Rank-one lift: when collective defect rank two becomes actual third cross volume

The previous theorem produces second exterior volume of the defect cross block, while the existing Fourier receiver wants a third direction of the ACTUAL cross block `A_ST=u_S u_T^T-F_ST`.  The following elementary lemma isolates exactly the missing geometry.

### Lemma 2 — rank-one lift or one-sided alignment

Let `F_0` be an `m x n` matrix of rank two with singular values `s_1>=s_2=c>0`.  Let `u in R^m`, `v in R^n`, and define

`alpha=dist(u,col(F_0))`,
`beta =dist(v,row(F_0))`,
`K=||u|| ||v||+||F_0||_op`.

Then

`s_3(uv^T-F_0) >= alpha beta s_1 s_2/K^2`
`              >= alpha beta c^2/K^2`.                                   (2.1)

More generally, if `F=F_0+E`, then

`s_3(uv^T-F) >= alpha beta c^2/K^2 - ||E||_op`.                           (2.2)

### Proof

Choose left/right singular vectors `l_1,l_2` and `r_1,r_2` for `F_0`.  If `alpha,beta>0`, append normalized perpendicular components `l_3=u_perp/alpha`, `r_3=v_perp/beta`.  Compress `uv^T-F_0` to these three-dimensional subspaces.  In these bases the compression is

`a b^T - diag(s_1,s_2,0)`,

where the third coordinates of `a,b` are `alpha,beta`.  A direct determinant expansion gives exactly

`|det(compression)|=alpha beta s_1 s_2`.                                  (2.3)

The top two singular values of the compression have product at most its operator norm squared, which is at most `K^2`.  Therefore its third singular value is at least the right side of (2.1).  Singular values of a compression do not exceed the corresponding singular values of the full operator, proving (2.1).  Equation (2.2) follows from Weyl's `1`-Lipschitz bound for singular values under operator-norm perturbation.  Cases `alpha beta=0` are immediate.  QED.

Thus a near-rank-two defect block automatically creates the third ACTUAL cross singular direction unless the positive rank-one baseline is almost aligned with the defect row space or column space.  The latter is precisely a grouped-bank/heavy-star geometry rather than an unclassified failure.

This lemma is designed to feed the current volume-stability theorem: once the right-hand side of (2.2) is a fixed scale and the supported leverage gate is verified, the full ambient density is continuous and bounded.  I do not claim that Theorem 1 alone automatically supplies the needed low-rank approximation or leverage gate.

---

## 3. A complete opposite-sign receiver: pure defect stars

The strongest endpoint of (STAR) is when all defect is carried by one physical hub.  In this case the indefinite geometry can be paid directly without completing a small scalar pivot.

Let the original coordinates be split into one hub `h`, a light set `L`, and an arbitrary outside set `J`.  Suppose, after conditioning on `X_J`, the quadratic block on `{h} union L` has

`A_LL = u u^T + D`,                                                       (3.1)

where `D` is arbitrary diagonal, and hub-light column

`A_Lh = u_0 u - b`.                                                       (3.2)

The hub diagonal, all `J` blocks/couplings, and all affine terms are arbitrary.  Put `U=||u||`; when `U>0`, let `s=u/U` and define

`Delta = ||u||^2 ||b||^2-(u dot b)^2`.                                    (3.3)

The augmented rows in Theorem MF are

`w_j=(u_0u_j-b_j, s_j)`.

Their Gram matrix is

`Gamma = [[||u_0u-b||^2, <u_0u-b,s>],
          [<u_0u-b,s>, 1]]`.

Its determinant is exactly

`det Gamma = ||b-P_u b||^2`,

and therefore the rank-one light eigenvalue `lambda=U^2` satisfies

`lambda det Gamma = Delta`.                                               (3.4)

### Theorem 3 — mixed-Fresnel pure-star bound

Assume `Delta>0` and every augmented row obeys the genuine Theorem-MF leverage gate

`w_j^T Gamma^{-1} w_j <= 1/2`.                                            (3.5)

Then the FULL ambient quadratic form, with arbitrary outside blocks/couplings and affine terms as above, has a continuous density and

`||p_Q||_infinity <= 3*2^(4/3) Delta^(-1/3)`.                            (3.6)

### Proof

Theorem MF, applied with one heavy coordinate and the one rank-one light square, gives

`|phi_Q(t)| <= [(4pi)^(3/2)/2] Delta^(-1/2) |t|^(-3/2)`.                 (3.7)

The original-coordinate factors are retained throughout the theorem; no independence of the two projected light variables is asserted.  Combining (3.7) with `|phi_Q|<=1` and

`integral_R min(1,B|t|^(-3/2)) dt = 6 B^(2/3)`

yields by Fourier inversion

`||p_Q||_infinity <= (1/(2pi))*6*([(4pi)^(3/2)/2] Delta^(-1/2))^(2/3)`
`                 = 3*2^(4/3) Delta^(-1/3)`.

The integrable characteristic function also gives a continuous `C_0` density.  QED.

### Exact-rank-three indefinite corollary

If `D=0`, `J` is absent and the entire matrix is the pure-star defect form

`A_0 = w w^T-(e_h b^T+b e_h^T)`,  with  `w=(u_0,u)`,                     (3.8)

then `rank A_0<=3`.  In an orthonormal basis consisting of the hub, `u/||u||`, and the perpendicular component of `b`, a direct determinant computation gives

`pdet(A_0) = -Delta`.                                                      (3.9)

Hence whenever its three nonzero eigenvalues have absolute value at least `s`, necessarily

`Delta>=s^3`.

Under the leverage gate (3.5),

`||p_Q||_infinity <= 3*2^(4/3)/s`
`                  = 7.559526299369239.../s`.                            (3.10)

The determinant is negative and the trace of `A_0` is positive, so the nondegenerate core has signature `(+,+,-)`; negating the form gives `(+,-,-)` with the same bound.

This is a genuinely rotated indefinite branch.  It remains uniform as the physical hub pivot `u_0^2` tends to zero, in contrast with scalar-square completion.

---

## 4. Why the third direction removes the rank-two logarithm here

Keep the mandatory control example: for independent `X,Y~Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|))` for `0<|t|<1/2`,

so an opposite-sign rank-two saddle has a true logarithmic singularity.

In the pure-star geometry, `Delta` is the squared area of the two light coefficient vectors `u,b`.  If `Delta=0`, these vectors are collinear and the active matrix loses the third direction; one falls back toward a rank-two saddle.  If `Delta>0`, the augmented product frame is genuinely two-dimensional.  Together with the hub integration, Theorem MF produces `|t|^-3/2`, which is integrable.  Thus the third direction is not an abstract spectral label: it is exactly the nonzero area `Delta` retained in ORIGINAL-coordinate product provenance.

This also explains why completing a near-null hub is the wrong interface.  The target-valid family in account02/B16 r25 has spectrum `{1+delta,-1,1}` and a uniform true density bound `<7.56`, yet the exact translation-uniform scalar-square/half-Riesz envelope diverges like `log(1/delta)`.  The mixed-Fresnel proof succeeds because it retains the translating original-coordinate factor jointly with the transverse square.

---

## 5. Designated partner applied to the complementary sign-frustrated chamber

The new defect decomposition assumes a global sign gauge.  The designated `account04/B11` theorem pays the fixed-scale sign-frustrated complement at an actual inequality.

Suppose a physical triangle has positive diagonals `a_i>=m>0`, all three physical pairs are PSD, and normalized edges

`rho_ij=A_ij/sqrt(a_i a_j)`

have sign product `-1`.  If some pair defect `1-rho_ij^2>=1/16`, the definite physical-pair theorem gives

`||p_Q||_infinity <= 4pi/m`.                                              (5.1)

Otherwise every defect is `<1/16`.  Set

`eta_0=1-sqrt(15)/4`.

The completed partner theorem gives the smallest singular value of the normalized frustrated triple at least `sqrt(15)/2-1`, hence its target-level density estimate yields

`||p_Q||_infinity`
` <= 6sqrt(pi)/[m(sqrt(15)/2-1)]`
` = 11.355918489042871.../m`
` < 4pi/m`.                                                               (5.2)

Thus at any fixed positive diagonal scale the sign-frustrated branch is completely removed before Theorem 1 is invoked.  This is an equation-level use of the designated partner result, not a copied citation.

---

## 6. What changed and what remains open

The preceding run ended with a qualitative instruction to extract a fixed-scale eight-coordinate balanced packet.  This run replaces part of that request with a dimension-free spectral statement requiring no fixed diagonal lower bound:

`sign-balanced pair-PSD + s3(A)>=s`
` => defect star norm >=s/2 OR disjoint defect cross second-volume >=s^4/32`. (6.1)

The pure-star endpoint of the first alternative is now paid by Theorem 3 whenever its augmented frame is diffuse; exact rank-three target-scale pure stars then satisfy the universal continuous bound `7.56/s`.  Lemma 2 also shows how a rank-two defect cross block generates an actual third cross direction unless the positive rank-one baseline is aligned with it.

The first remaining B11 implication is therefore sharper:

**QFORM-BALANCED-DEFECT-RECEIVER-v1 (OPEN).** Starting from (6.1), prove that either

1. a star contains enough transverse area and a diffuse augmented frame for Theorem 3 / mixed Fresnel;
2. a cross-2-volume block has a quantitative rank-two core whose rank-one baseline is transverse enough for Lemma 2 plus the current volume-stability receiver; or
3. failure of both forces a finite grouped-bank / one-sided-alignment structure already payable by an existing grouped-bank, physical-pair, ridge, or null-hub theorem.

The difficult cases are high augmented leverage and collective `e_2` spread over many small singular directions.  I have **not** proved that (1)-(3) are exhaustive.  Arbitrary additional spectrum is allowed by the analytic receivers once their stated certificates exist, but the bare three-large-eigenvalue hypothesis has not yet been compiled into one of them universally.

Global continuity also remains open.  Theorem 3 and the volume-stability receiver give continuity in their respective branches; the structural Theorem 1 itself is only matrix geometry.

No Gaussianity, moments, compact support, connected support, log-concavity, identical laws, spectral-coordinate independence, arbitrary-joint coarea bound, worst conditional-density supremum, or Monte Carlo extremality is used.
