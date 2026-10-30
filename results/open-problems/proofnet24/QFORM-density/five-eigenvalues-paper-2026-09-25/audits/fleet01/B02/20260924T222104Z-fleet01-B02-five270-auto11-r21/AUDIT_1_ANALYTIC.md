# B02 r21 audit part 1 — scope, normalizations, Fourier engine

Source blob: `f3e5fc173cdcee40174c19c955d813d47f32bd91`.
Manifest SHA-256: `359d1e4c5ffe528dcd749f4315b426d6423944d88678544131fa3ffe090c1362`.

I read the complete current five-eigenvalue source and support package independently.

## Lines 49–102 — statements, quantifiers, scaling: PASS

Theorem 1.1 retains arbitrary dimension, arbitrary real symmetric A, arbitrary
remaining spectrum/signature, arbitrary affine b,c, and independent non-iid
coordinates with no hypothesis beyond a density cap K. Theorem 1.2 has the same
scope. Scaling Y=KX and A -> A/s gives exactly K^2/s for density and K/sqrt(s)
for the half-potential.

## Lines 108–153 — Fourier/Gaussian/Riesz: PASS

With hat f(t)=int exp(itx)f(x)dx, Plancherel has factor 2pi and inversion factor
1/(2pi). The Gaussian identity has coefficient 1/(2 sqrt(pi v)). The Gamma
calculation for |x|^{-1/2} gives the coefficient 1/sqrt(2pi). The envelope
integrals used later have the correct exponents and constants.

## Lines 154–199 — conditioning and linear algebra: PASS; spectral Lean coverage incomplete

Conditional density domination conditions only on disjoint original-coordinate
blocks; it does not assert independence between a completed square and its critical
value.

The best-rank approximation characterization proves singular-value Lipschitz,
low-rank shift and compression s_j(U^T T V)<=s_j(T). The Schur count follows
from the lower-right principal block S^{-1} of A^{-1}, interlacing separately on
positive and negative tails, and regularization. Gram/Cauchy–Binet identities are
exact. These three spectral facts are mathematically checked here but remain outside
the saved Lean coverage.

## Lines 200–267 — geometric BL, projection densities, scalar Fourier powers: PASS

The heat-flow identity is
(partial_tau-Delta)F/F=sum c_i v_i^2-|sum c_i v_i u_i|^2>=0
by the Parseval-frame contraction. Compact-support approximation, derivative
domination, the large-time Gaussian limit and small-time Fatou step are valid.

For projection densities, beta_i=1-|U^T e_i|^2 gives the exact complementary
frame. Since 0<=f_i<=1, f_i^(1/beta_i)<=f_i. The resulting e^(d/2) cap is
obtained by deterministic fiber integration, never by declaring rotated coordinates
independent.

The paper's scalar Fourier-power lemma is valid: for m=floor(p/2), the difference
density is cap one, |hat f|^(2m) is the characteristic function of a sum of m
independent differences, Plancherel supplies integrability before inversion at zero,
and the one-dimensional projection theorem gives the displayed bound.

## Lines 268–417 — grouped crossing-volume Fourier compiler: PASS

Cauchy–Schwarz removes the same-bank phase in the zero-hub case. In the hub case,
the phase-weighted image measure is absolutely continuous with total variation
dominated by the ordinary projected law. Plancherel gives exactly (pi/|t|)^k.
Mollification is removed only after an L2 bound; weighted Holder is applied to a
finite measure and does not require normalization.

For a determinant-weighted subset T, the joint map has Gram determinant
Theta(H)*det(C_T C_T^T). The scalar Fourier-power exponent is
p=1/alpha_i>=2 precisely because every unpromoted row has alpha_i<=1/2.
The entropy inequality has the correct sign. Every promoted hub is a literal
original coordinate, so product-law provenance is preserved.

Consequently Theorem 4.1 is valid under the exact rough-law hypotheses. Order three
is a density endpoint, order two is only a full half-potential endpoint, and order
one is only a |t|^{-1/2} characteristic-function endpoint.
