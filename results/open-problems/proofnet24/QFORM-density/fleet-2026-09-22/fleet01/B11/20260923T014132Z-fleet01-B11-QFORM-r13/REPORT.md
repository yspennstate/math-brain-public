SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T01:41:32Z.
attacking: the small-positive-D0 zero-diagonal chamber via Lorentz null-cone angular volume clustering and an exact five-near-ray reduction.

# fleet01/B11 QFORM r13 — Lorentz angular stability of the zero-diagonal indefinite chamber

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: indefinite signatures `(2,1)` and `(1,2)`  
Outcome: **ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. Exact obligation and source-pinned inputs

The full target remains open. This report attacks the exact-rank-three, zero-physical-diagonal indefinite residual left after the existing scalar/pair, diffuse-cross, and exact `D0=0` exits. It does not silently extend to arbitrary additional spectrum.

The designated partner actually used below is fleet02/B11, run `20260922T233948Z-fleet02-B11-QFORM-b35bb6c3`, full report

`yspennstate/math-open-problems@e47740cfec219112c826613bec5785af4b96cf3f`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260922T233948Z-fleet02-B11-QFORM-b35bb6c3/REPORT.md`.

Its theorem says that for exact rank three `A=R M R^T`, `R^T R=I_3`, with `s=min |lambda(M)|` and disjoint Pluecker mass

`D0=sum_{B cap T=empty} det(R_B)^2 det(R_T)^2`,

some ORIGINAL-coordinate cut `S,S^c` has

`σ_3(A[S,S^c]) >= s sqrt(D0)/8`.                                  (1.1)

The newest proof-first continuation is also applied below through the volume-stability theorem

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.

For an ORIGINAL-coordinate cross block `C` with `σ_3(C)>=a` and maximum diagonal of its row-range projection at most `1/2`, the `E=0` case of that theorem gives a continuous density and

`||p_Q||_∞ < 23/a`,                                                (1.2)

while retaining arbitrary self blocks, outside couplings, affine terms, and arbitrary cap-one product input laws.

Binding corrections are respected: no post-rotation independence, arbitrary-joint coarea, conditional-cap-as-independence, fixed-good-minor implication, pointwise law-uniform van der Corput bound, moment/support hypothesis, or perturbative deletion of small matrix coefficients is used.

## 2. Canonical Lorentz-circle representation

Assume first inertia `(2,1)`. Negating `A` handles `(1,2)`, so no sign case is lost. Orthogonally diagonalize the **deterministic spectral matrix only**:

`M=diag(p,q,-r)`, `p,q,r>0`.

Because every physical diagonal vanishes,

`0=tr A=tr M=p+q-r`,

hence

`r=p+q`.                                                          (2.1)

Write the i-th spectral frame row as `r_i=(x_i,y_i,z_i)`. Set

`u_i=(sqrt(p)x_i,sqrt(q)y_i,sqrt(r)z_i)`.

Then the physical null condition is exactly

`u_{i1}^2+u_{i2}^2-u_{i3}^2=0`.                                  (2.2)

For each nonzero row choose its projective representative with positive third coordinate; determinant squares and row outer products are unchanged. Thus

`u_i=rho_i q(theta_i)`,

`q(theta)=(cos theta,sin theta,1)`, `rho_i>0`.                     (2.3)

Parseval gives an exact covariance identity

`sum_i u_i u_i^T = diag(p,q,r)`.                                  (2.4)

In particular

`sum_i rho_i^2=r`.                                                 (2.5)

Define the **Lorentz angular mass**

`mu_i=rho_i^2/r`, so `sum_i mu_i=1`.                              (2.6)

The off-diagonal covariance equations in (2.4) also give

`sum_i mu_i cos theta_i=sum_i mu_i sin theta_i=0`.                 (2.7)

Thus the null frame induces a probability measure on the circle with vanishing first Fourier moment.

### Switching classification

If `epsilon_i` records the original future/past sign of the null row, then

`A_ij=epsilon_i epsilon_j rho_i rho_j (cos(theta_i-theta_j)-1)`.

After diagonal sign switching `D=diag(epsilon_i)`, which corresponds on the random side to replacing each original independent `X_i` by `epsilon_i X_i` and therefore preserves the cap-one class,

`boxed: (DAD)_ij=-2 rho_i rho_j sin^2((theta_i-theta_j)/2), i!=j`, (2.8)

and the diagonal remains zero. Hence every zero-diagonal exact-rank-three `(2,1)` target is product-law equivalent to a weighted squared-chord kernel on the circle. This is an exact classification, not an approximation.

## 3. Exact Pluecker angular formula

For three angles,

`det[q(theta_i),q(theta_j),q(theta_k)]`

`=4 sin((theta_i-theta_j)/2) sin((theta_j-theta_k)/2) sin((theta_k-theta_i)/2)`. (3.1)

Since

`R_B = U_B diag(p^{-1/2},q^{-1/2},r^{-1/2})`,

the Pluecker weight `w_ijk=det(R_{ijk})^2` is exactly

`boxed:
 w_ijk = 16 (r^2/(pq)) mu_i mu_j mu_k
         prod_{pairs a<b in {i,j,k}} sin^2((theta_a-theta_b)/2).` (3.2)

By `r=p+q`, AM-GM gives `r^2/(pq)>=4`, hence

`boxed:
 w_ijk >=64 mu_i mu_j mu_k
         prod_{pairs} sin^2((theta_a-theta_b)/2).`                 (3.3)

This converts the abstract Pluecker weights into an exact angular-volume density on the Lorentz cone.

## 4. Six-separated-bank theorem

### Theorem 4.1 — `QFORM-NULL-D0-SIX-ANGULAR-BANKS-v1`

Let `I_1,...,I_6` be pairwise disjoint Borel subsets of the projective angle circle such that every two distinct sets have circular distance at least `delta>0`. Put

`m_a=sum_{i:theta_i in I_a} mu_i`.

Then

`boxed:
 D0 >=4096 sin(delta/2)^12 prod_{a=1}^6 m_a.`                     (4.1)

#### Proof

Let `W_123` be the total Pluecker weight of triples with one index in each of `I_1,I_2,I_3`. Every pairwise angular gap in such a triple is at least `delta`; therefore (3.3) gives

`W_123 >=64 sin(delta/2)^6 m_1m_2m_3`.                            (4.2)

Likewise

`W_456 >=64 sin(delta/2)^6 m_4m_5m_6`.                            (4.3)

Every triple counted by `W_123` is index-disjoint from every triple counted by `W_456`, so the defining sum for `D0` contains their full product. Hence

`D0>=W_123 W_456`,

which is exactly (4.1). QED.

This result is stronger than a finite-ray-count statement: it permits arbitrarily many original coordinates and controls separated **mass** rather than row count.

## 5. Quantitative five-near-ray concentration from small positive D0

Partition the angle circle into `N>=12` equal half-open bins of length

`ell=2pi/N`.

Fix `epsilon=D0>0` and declare a bin heavy if its `mu`-mass is at least

`eta = epsilon^(1/6)/(2 sin(ell/2)^2)`.                            (5.1)

### Theorem 5.1 — `QFORM-NULL-D0-FIVE-CLUSTER-v1`

The heavy bins have at most five connected components in the cyclic adjacency graph, and at most ten heavy bins in total. Consequently all but mass `N eta` of the Lorentz angular measure lies in a union of at most five arcs, each of length at most `10 ell`.

#### Proof

If the heavy-bin graph had an independent set of six vertices, the corresponding six bins would be pairwise circularly separated by at least `ell`. Theorem 4.1 would yield

`D0 >=4096 sin(ell/2)^12 eta^6 =64 epsilon`,

contradicting `D0=epsilon>0`. Therefore the heavy-bin graph has independence number at most five.

Every connected component contains an independent vertex, so the number of components is at most five. A path component of `L` consecutive heavy bins has independence number `ceil(L/2)`. Summing over components gives at most ten heavy bins total. Every nonheavy bin has mass `<eta`, so their total mass is `<N eta`. Each heavy component occupies at most ten consecutive bins and hence lies in an arc of length at most `10 ell`. QED.

### Explicit asymptotic corollary

When

`epsilon <= (pi/6)^24`,

put `x=epsilon^(1/24)` and choose

`N=ceil(2pi/x)>=12`.

Then `ell<=x` and `ell>=2pi x/(2pi+1)`. Since `sin(ell/2)>=ell/pi`,

`eta <= ((2pi+1)^2/8) x^2 <6.631 x^2`,

and

`N eta <= ((2pi+1)^3/8) x <48.292 x`.

Thus

`boxed:
 mu( union of at most five arcs of length <=10 epsilon^(1/24))
 > 1-48.292 epsilon^(1/24).}`                                     (5.2)

This gives a quantitative stability statement for the projective geometry as `D0->0`. It deliberately does **not** delete the exceptional angular mass: with arbitrary unbounded input supports, small spectral mass is not a small random perturbation.

## 6. Exact near-ray decomposition: the error has special tangent/null structure

The five-cluster statement becomes useful because angular deviation from a null ray has an exact algebraic form, not an arbitrary dense perturbation. Let

`t(theta_0)=(-sin theta_0,cos theta_0,0)`.

Then for every real `tau`,

`boxed:
 q(theta_0+tau)
 = cos^2(tau/2) q(theta_0)
   + sin(tau) t(theta_0)
   + sin^2(tau/2) q(theta_0+pi).}`                                (6.1)

Indeed the radial planar coefficient is `cos tau`, the tangent coefficient is `sin tau`, and the third coordinate equals one. Therefore an original-coordinate bank whose angles lie in an arc around `theta_0` aggregates exactly as

`sum_i rho_i q(theta_i) X_i
 = q(theta_0) Z_0 + t(theta_0) Z_1 + q(theta_0+pi) Z_2`,            (6.2)

where, with `tau_i=theta_i-theta_0`,

`Z_0=sum_i rho_i cos^2(tau_i/2) X_i`,
`Z_1=sum_i rho_i sin(tau_i) X_i`,
`Z_2=sum_i rho_i sin^2(tau_i/2) X_i`.                             (6.3)

Different angular banks remain independent because they use disjoint ORIGINAL coordinates; the three aggregates inside one bank may be dependent and are not treated as independent. The tangent amplitude is first order in `tau`, while the opposite-null amplitude is second order, but neither is discarded.

This exact decomposition identifies the correct next analytic object: a finite number of independent vector-valued near-ray banks with tangent and opposite-null leakage. It avoids the invalid strategy of replacing near rays by exact rays in the random quadratic form.

## 7. Actual application of the designated partner and the newest volume theorem

Apply the designated fleet02/B11 half-cut theorem (1.1). For `D0>0` it gives a product-preserving original-coordinate cut with

`a:=sigma_3(C) >= s sqrt(D0)/8`.                                  (7.1)

If the row-range projection of this **actual** cross block satisfies the newest volume-stability gate

`max_i (P_range(C))_ii <=1/2`,                                    (7.2)

then apply the current volume-stability theorem with `M0=C`, `E=0`. Equation (1.2) gives the actual bound

`boxed:
 ||p_Q||_infinity < 23/a <=184/(s sqrt(D0)).}`                    (7.3)

This branch has a continuous `C_0` density and allows arbitrary self blocks, outside couplings and affine terms.

Combining (4.1) with (7.3), if six separated angular banks have masses at least `eta` and separation `delta`, then whenever (7.2) holds for the partner cut,

`sqrt(D0)>=64 sin(delta/2)^6 eta^3`,

so

`boxed:
 ||p_Q||_infinity < 2.875/[s sin(delta/2)^6 eta^3].}`              (7.4)

This is an explicit application of both the designated partner and the newest proof-first volume result to an actual density inequality. The leverage gate (7.2) is retained; no false claim makes it automatic.

If (7.2) fails, the theorem above instead forces a high-leverage cross-cut survivor together with the five-near-ray geometry (5.2). This is precisely the remaining branch, rather than a hidden dropped case.

## 8. Opposite-sign rank-two logarithmic control and why the third direction appears

For independent `X,Y~Unif[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|)), 0<|t|<1/2`,                            (8.1)

so the opposite-sign rank-two saddle remains genuinely unbounded.

In the present null-cone representation, a pair of distinct null rays only creates the hyperbolic pairing

`q(theta)^T J q(phi)=cos(theta-phi)-1=-2 sin^2((theta-phi)/2)`.    (8.2)

A third separated ray creates a genuine three-volume through (3.1). Six separated positive-mass angular banks force two disjoint rank-three packets and hence positive `D0`, which the partner turns into an actual original-coordinate rank-three cross direction. At `D0=0`, the completed five-ray bank theorem supplies the third independent bank by a different mechanism. For small `D0`, Theorem 5.1 says the only way to approach the logarithmic endpoint is to concentrate almost all Lorentz mass near at most five projective null rays; (6.1) shows exactly how the missing third curvature re-enters as tangent/opposite-null leakage.

Thus the third direction is identified without ever rotating the independent random inputs.

## 9. Remaining implication

The first unpaid B11 implication is now

`QFORM-FIVE-NEAR-RAY-TANGENT-BANK-COMPILER-v1`:

> In the small-positive-`D0` zero-diagonal exact-rank-three chamber, use (5.2) and the exact bank decomposition (6.1)--(6.3) to prove a uniform density/small-ball bound when the partner's cross cut is high-leverage. The proof must retain dependence among `(Z_0,Z_1,Z_2)` within each bank and must not delete the light angular mass. A valid exit may use the existing tangent-ray half-potential, physical-pair, ridge or fractional-volume mechanisms, but only with their actual hypotheses.

This is narrower than the previous generic heavy-cross-overlap residual: the surviving source geometry is now a five-cluster Lorentz configuration with a canonical tangent/opposite-null decomposition.

Arbitrary additional spectrum remains a separate interface to the full theorem.

## 10. Continuity and status

- The new angular theorems are deterministic structural statements and do not themselves prove a density bound in the high-leverage five-near-ray residual.
- In the diffuse partner-cut subbranch (7.2), the applied volume theorem proves a continuous `C_0` density with (7.3).
- Essential boundedness and continuity for the unrestricted target remain OPEN.
- Both indefinite signatures are covered by global sign reversal.

No theorem here assumes Gaussianity, log-concavity, moments, compact support, connected support, identical laws, or spectral-coordinate independence.
