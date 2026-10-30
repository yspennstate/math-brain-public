SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B11, 2026-09-23T04:27:58Z.
attacking: zero/near-zero indefinite null-arc banks via an exact tangent Vandermonde Gram identity and the new volume-stability cross-block exit.

# fleet01/B11 — null-arc moment-curve compiler and Gram-volume exit

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** indefinite signatures `(2,1)` and `(1,2)`  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING STRUCTURAL THEOREM + CONTINUOUS-DENSITY EXIT / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved only in the volume-exit subbranch below; not proved for the full theorem or full target.

## 1. Exact target and source-valid boundaries

The owner target remains the unrestricted statement: for arbitrary dimension, arbitrary independent real input coordinates with densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal essential bound on the density of `Q=X^TAX`, or give a valid counterexample. The full conjecture remains OPEN.

This run changes mechanism from the preceding half-Riesz/finite-ray endpoint work. It attacks the exact-rank-three zero-diagonal indefinite boundary through the algebraic moment curve hidden in a short Lorentz-null arc, and then splices that identity to the current three-volume Fourier theorem. No random quadratic term is discarded as a small perturbation.

Source-valid inputs actually used:

1. Previous B11 Lorentz angular reduction:
   `yspennstate/math-open-problems@42a6318c46518baa413d08d31a0b18fbda582860`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B11/20260923T014132Z-fleet01-B11-QFORM-r13/REPORT.md`.
   It proves the exact null-circle representation and the tangent/opposite-null identity for the zero-physical-diagonal chamber.

2. Required newest volume-stability theorem:
   `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,
   `proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/REPORT.md`.
   Its `E=0` specialization says: for an ORIGINAL-coordinate cross block `C` with `sigma_3(C)>=a>0` and maximum row-range leverage at most `1/2`, the full quadratic-plus-affine output has a continuous `C_0` density and
   `||p_Q||_infinity < 23/a`, with arbitrary self blocks and outside couplings retained.

3. Designated partner fleet02/B11:
   `yspennstate/math-open-problems@8cf17ad7a60ab0eab6d6c4f8900e62947390db7e`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B11/20260923T025552Z-fleet02-B11-QFORM-db8e3811/REPORT.md`.
   Its minority-sign Schur theorem gives, in exact rank three,
   `||p_Q||_infinity <= 2 sqrt(2 pi)(|a| c_i |det Lambda|)^(-1/4)`
   and hence the leverage-free consequence
   `||p_Q||_infinity <= 2 sqrt(2 pi)|a|^(-1/2)`
   whenever an ORIGINAL physical diagonal `a` carries the minority inertia sign. Its dependent-pair construction also forbids collapsing the near-null product provenance to a mere joint-density cap.

The live corrections consumed in this run include the failures of post-rotation independence, arbitrary-joint rank-three coarea, conditional-cap-as-independence, near-zero half-Riesz interpolation, perturbative coefficient deletion on unbounded inputs, and near-rank-one recoloring stability. None is used below.

## 2. Partner result applied first: fixed minority curvature is already paid

Consider exact rank three of signature `(2,1)`, with spectral magnitudes at least one. If some ORIGINAL physical diagonal satisfies

`A_ii <= -eta <0`,

then the designated fleet02/B11 theorem gives the actual inequality

`boxed: ||p_Q||_infinity <= 2 sqrt(2 pi) eta^(-1/2).`               (2.1)

For the concrete threshold `eta=1/16`,

`||p_Q||_infinity <= 8 sqrt(2 pi) < 20.054`.                         (2.2)

Reflection gives the `(1,2)` statement with a positive minority diagonal. Thus a hypothetical sequence escaping every fixed universal bound cannot retain a fixed-scale minority physical diagonal in the exact-rank-three branch; the minority curvature must approach the null boundary. This is why the zero/near-zero Lorentz geometry below is a genuine boundary problem rather than a convenient special case.

The partner's dependent-pair obstruction is also binding here: the tangent-bank variables below are not replaced by an arbitrary bounded joint pair and no conditional density cap is treated as independence.

## 3. Lorentz-null bank and the exact moment curve

Assume now the exact zero-physical-diagonal `(2,1)` chamber

`A=R M R^T`, `R^T R=I_3`, `A_ii=0 for every i`,                   (3.1)

with

`M=diag(p,q,-r)`, `p,q,r>0`, `s=min(p,q,r)>0`.                     (3.2)

Since `tr A=tr M=0`, necessarily `r=p+q`. Put

`S=diag(sqrt(p),sqrt(q),sqrt(r))`, `u_i=S r_i`.                     (3.3)

Then every transformed row is Lorentz-null:

`u_{i1}^2+u_{i2}^2-u_{i3}^2=0`.                                    (3.4)

After the harmless original-coordinate sign switching already justified in the predecessor report, choose projective representatives

`u_i=rho_i q(theta_i)`,
`q(theta)=(cos theta,sin theta,1)`, `rho_i>0`.                       (3.5)

Fix an ORIGINAL-coordinate bank `B` whose angles lie in an open semicircle centered at `theta_0`, so

`tau_i=theta_i-theta_0 in (-pi,pi)`.                                (3.6)

Define

`z_i=tan(tau_i/2)`,
`a_i=rho_i/(1+z_i^2)=rho_i cos^2(tau_i/2)`.                         (3.7)

Let

`q_0=q(theta_0)`,
`t_0=(-sin theta_0,cos theta_0,0)`,
`q_pi=q(theta_0+pi)`.                                                (3.8)

The exact tangent/opposite-null identity becomes the polynomial parameterization

`boxed:
 u_i=a_i [q_0+2 z_i t_0+z_i^2 q_pi].`                              (3.9)

Moreover

`|det[q_0;t_0;q_pi]|=2`.                                            (3.10)

Thus a short null arc is not an arbitrary three-dimensional perturbation of a ray: after a deterministic basis change it is exactly the quadratic moment curve

`z -> (1,2z,z^2)`.                                                   (3.11)

This observation is the mechanism change of the present run.

## 4. Main new identity: local three-volume equals a quadratic-regression residual

Let

`G_B=sum_{i in B} r_i r_i^T`,                                      (4.1)

and assume `W_B:=sum_{i in B} a_i^2>0`. Give the finite/countable support points `z_i` probability

`P_B(Z=z_i)=a_i^2/W_B`.                                              (4.2)

Set

`v_B=Var_B(Z)`,                                                      (4.3)

and define the least-square quadratic residual

`R_B=min_{alpha,beta in R} E_B[(Z^2-alpha-beta Z)^2].`              (4.4)

### Theorem 4.1 — `QFORM-NULL-ARC-MOMENT-GRAM-v1`

For every such bank,

`boxed:
 |det M| det G_B = 16 W_B^3 v_B R_B.`                              (4.5)

Equivalently,

`boxed:
 |det M| det G_B
 =16 sum_{i<j<k in B} a_i^2 a_j^2 a_k^2
      (z_i-z_j)^2(z_i-z_k)^2(z_j-z_k)^2.`                          (4.6)

In particular,

`det G_B=0  iff  the bank occupies at most two projective null rays.` (4.7)

#### Proof

Let `H_B=sum_{i in B} u_i u_i^T`. By (3.3),

`H_B=S G_B S`, hence

`det H_B=|det M| det G_B`.                                          (4.8)

Let `E` be the `3 x 3` matrix whose rows are `(q_0,t_0,q_pi)`. By (3.9), if

`m(z)=(1,2z,z^2)^T`,                                                (4.9)

then

`H_B=E^T [sum_i a_i^2 m(z_i)m(z_i)^T] E`.                          (4.10)

Using `det(E)^2=4`,

`det H_B
 =4 W_B^3 det E_B[m(Z)m(Z)^T].`                                    (4.11)

Write `D=diag(1,2,1)` and `n(z)=(1,z,z^2)^T`, so `m=Dn`. Therefore

`det E[m m^T]=4 det E[n n^T].`                                      (4.12)

Gram-Schmidt on the ordered functions `1,Z,Z^2` gives

`det E[n n^T]
 = ||1||_2^2 ||Z-EZ||_2^2
   min_{alpha,beta} ||Z^2-alpha-beta Z||_2^2
 =v_B R_B`.                                                         (4.13)

Equations (4.8)-(4.13) prove (4.5).

For (4.6), use Cauchy-Binet in (4.10). For three support points,

`det[m(z_i),m(z_j),m(z_k)]
 =2 (z_j-z_i)(z_k-z_i)(z_k-z_j)`,                                  (4.14)

and multiplication by the basis `E` contributes another factor `det E` of absolute value two. Squaring gives the factor sixteen in (4.6).

If `v_B=0`, all positive-weight `z_i` coincide, so there is one ray. If `v_B>0` and `R_B=0`, the support is contained in the real zero set of one monic quadratic `z^2-beta z-alpha`, hence in at most two points. The converse is immediate from the rank of the moment curve on at most two points. This proves (4.7). QED.

### Interpretation

The first tangent aggregate and the second-order opposite-null aggregate from the previous B11 decomposition are not merely small formal errors. Their genuinely three-dimensional content is exactly `v_B R_B`. The first factor measures failure to be one ray; the second measures failure to be two rays.

## 5. Quantitative two-ray clustering from small local three-volume

The determinant identity has a direct stability consequence that does not delete any row.

Define the dimensionless local volume ratio

`kappa_B := |det M| det G_B /(16 W_B^3)=v_B R_B`.                   (5.1)

### Theorem 5.1 — `QFORM-NULL-ARC-TWO-RAY-STABILITY-v1`

For every `0<rho<=1`, there exist at most two real centers `c_1,c_2` such that

`boxed:
 P_B( dist(Z,{c_1,c_2}) >= rho )
 <= sqrt(kappa_B)/rho^4.`                                          (5.2)

When `kappa_B=0`, the exceptional mass is zero and the bank lies on at most two exact rays.

#### Proof

If `v_B<=sqrt(kappa_B)`, choose the single center `c_1=E_B Z`. Chebyshev gives

`P_B(|Z-c_1|>=rho)<=v_B/rho^2
 <=sqrt(kappa_B)/rho^2
 <=sqrt(kappa_B)/rho^4`,                                            (5.3)

because `rho<=1`.

Assume instead `v_B>sqrt(kappa_B)`. Then

`R_B=kappa_B/v_B<sqrt(kappa_B)`.                                    (5.4)

Let

`q_*(z)=z^2-beta z-alpha`                                           (5.5)

be the monic least-square residual polynomial, so `E q_*(Z)^2=R_B`.

If `q_*` has real roots `c_1,c_2`, then whenever `dist(z,{c_1,c_2})>=rho`,

`|q_*(z)|=|z-c_1||z-c_2|>=rho^2`.                                  (5.6)

Markov therefore gives

`P_B(dist(Z,{c_1,c_2})>=rho)<=R_B/rho^4
 <sqrt(kappa_B)/rho^4`.                                             (5.7)

If the roots are nonreal, write

`q_*(z)=(z-c)^2+h^2`, `h>0`.                                       (5.8)

Then `|z-c|>=rho` implies `q_*(z)>=rho^2`, so the same estimate holds with the single real center `c`. QED.

For the short arcs produced by the predecessor five-cluster theorem, `a_i^2=rho_i^2 cos^4(tau_i/2)` is uniformly comparable with the Lorentz mass `rho_i^2`; hence (5.2) is directly convertible into a two-subray concentration statement for the actual angular mass. The exceptional rows remain in the quadratic form; (5.2) is a structural classification, not permission to erase them.

## 6. Newest volume theorem applied to the same bank: exact Gram-crossblock exit

The identity above becomes analytically useful through an exact relation between a bank Gram matrix and the ORIGINAL-coordinate cross block.

Let `T=B^c`. Parseval gives

`G_T=R_T^T R_T=I_3-G_B`.                                            (6.1)

Put

`d_B=det G_B`,
`gamma_B=1-lambda_max(G_B)=lambda_min(G_T)`.                         (6.2)

Assume `d_B>0` and `gamma_B>0`, so both bank Grams are invertible. Define normalized row leverage inside the bank by

`ell_i^(B)=r_i^T G_B^{-1} r_i`, `i in B`.                            (6.3)

### Theorem 6.1 — `QFORM-NULL-ARC-GRAM-VOLUME-EXIT-v1`

If

`max_{i in B} ell_i^(B) <=1/2`,                                    (6.4)

then the full quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity < 23/[s sqrt(d_B gamma_B)].`                      (6.5)

#### Proof

Let

`U_B=R_B G_B^{-1/2}`, `U_T=R_T G_T^{-1/2}`.                         (6.6)

Both matrices have orthonormal columns. The physical cross block is

`C=A[B,T]
 =U_B [G_B^(1/2) M G_T^(1/2)] U_T^T`.                              (6.7)

Therefore its three nonzero singular values are those of the middle `3 x 3` matrix. Since `sigma_min(M)=s`,

`sigma_3(C)
 >=s sqrt(lambda_min(G_B) lambda_min(G_T)).`                         (6.8)

All eigenvalues of `G_B` lie in `[0,1]`; hence

`lambda_min(G_B)>=det G_B=d_B`.                                     (6.9)

Together with (6.2),

`boxed: sigma_3(C)>=s sqrt(d_B gamma_B).}`                          (6.10)

Because the middle matrix in (6.7) is invertible, `range(C)=range(R_B)`. Its row-range orthogonal projection is

`P_B=R_B G_B^{-1} R_B^T`,                                           (6.11)

whose `i`-th diagonal equals exactly `ell_i^(B)`. Thus (6.4) is precisely the leverage gate of the current volume-stability theorem.

Apply that theorem with `M_0=C`, `E=0`, and

`a=s sqrt(d_B gamma_B)`.                                            (6.12)

It gives a continuous `C_0` density and `||p_Q||infinity<23/a`, which is (6.5). All bank self-interactions and every coefficient outside this cross block remain present; no random perturbation was deleted. QED.

### The local exhaustive alternative

For every null-arc bank `B`, one of the following therefore occurs:

1. `d_B=0`: by Theorem 4.1 the bank lies on at most two exact null rays;
2. `gamma_B=0`: the bank captures a complete spectral direction and the complement loses that direction, a bank-coloop boundary;
3. `d_B,gamma_B>0` but (6.4) fails: there is a normalized high-leverage ORIGINAL row in the bank;
4. otherwise the continuous-density exit (6.5) applies.

Quantitatively, small positive `d_B` is no longer an opaque tangent-leakage regime: Theorem 5.1 converts it into one/two-ray concentration after normalization by the actual bank mass `W_B`, while (6.5) pays any branch in which the local three-volume, complementary spectral mass and leverage stay uniformly nondegenerate.

This is the first concrete bridge in B11 from the five-near-ray angular classification to the required newest three-volume theorem.

## 7. Rank-two logarithmic control and the role of the third direction

The opposite-sign rank-two obstruction remains exact. For independent

`X,Y ~ Uniform[-1/2,1/2]`,

`p_(2XY)(t)=log(1/(2|t|)), 0<|t|<1/2`.                              (7.1)

In the null-circle geometry, support on one or two projective rays is exactly the condition `det G_B=0`; the moment curve has rank at most two and no local third volume exists. A genuinely third angular location creates the Vandermonde factor

`(z_i-z_j)(z_i-z_k)(z_j-z_k)`                                     (7.2)

in (4.6). When that third volume persists on both sides of an ORIGINAL-coordinate cut and the normalized row leverage is diffuse, (6.10) turns it into a genuine third cross singular value and the current Fourier/volume theorem supplies an integrable characteristic-function envelope, hence a continuous bounded density.

Thus the third direction removes the rank-two logarithmic endpoint in a completely product-safe way: either it appears as actual three-volume and is paid by (6.5), or its failure forces algebraic concentration toward at most two null rays. No independence of spectral coordinates is ever asserted.

## 8. What remains unpaid

The full QFORM conjecture remains OPEN. The first B11 implication after this run is

`QFORM-NULL-ARC-HIGH-LEVERAGE-OR-BANK-COLOOP-COMPILER-v1`:

> In the five-near-ray small-`D0` zero-diagonal exact-rank-three chamber, use the new local trichotomy simultaneously across the heavy arcs. Pay the cases where a bank has normalized leverage above `1/2` or where `gamma_B` is small (bank-coloop limit), while retaining all light angular rows. If all local `d_B` are small, combine the quantitative one/two-ray clustering (5.2) with an exact product-preserving finite-spike/ray aggregation rather than deleting the exceptional mass.

The designated partner's theorem has already removed every fixed-scale minority physical pivot. The surviving nonzero near-null one-sign chamber still requires an interpolation/aggregation argument; the live near-zero half-Riesz correction forbids obtaining it by continuity of the exact-null proof alone.

Arbitrary additional spectrum is also a separate interface to the unrestricted theorem.

## 9. Verification notes

A deterministic checker accompanying this report verifies on a nontrivial four-point bank that

- the direct determinant of `H_B=sum u_i u_i^T`,
- the regression formula `16 W_B^3 v_B R_B`, and
- the Cauchy-Binet/Vandermonde sum in (4.6)

agree to floating-point roundoff. The analytic theorems above are proved symbolically; the checker is not an independent proof or review.

No end-to-end independent review of this run is claimed. A full candidate would still need the owner-required two independent complete reviews of all quantifiers.
