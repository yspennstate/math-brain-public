# A finite positive cell majorant for the actual simplex operator

Status: analytic comparison lemma, unaudited. No numerical bound is asserted by this document alone.

Write d=1-rho^2, kappa=rho^2/d, and use K_+, J_+ and the additive center ell_rho of Heilman arXiv:2608.00333v1 Appendix A, equations (148)-(151). In Lebesgue L2(0,infinity), the symmetric centered weighted kernel is

A_rho(x,y)=2 exp(-(x^2+y^2)/2) [K_+(x^2,y^2)-ell_rho(x)-ell_rho(y)] / sqrt(Jtilde_+(x) Jtilde_+(y)).

The map from z in L2(J_+ dnu), dnu(t)=exp(-t)dt, to f(x)=sqrt(2x exp(-x^2) J_+(x^2)) z(x^2) is an isometry. Its quadratic form is exactly that of A_rho. For mean-zero z, the additive center drops out, so a bound on the full centered operator bounds the constrained operator used in (152).

Let I_1,...,I_N partition [0,L]. If nonnegative symmetric B satisfies

B_ij >= sqrt(|I_i| |I_j|) sup_{x in I_i,y in I_j,rho in slab} |A_rho(x,y)|,

then ||1_[0,L] A_rho 1_[0,L]|| <= ||B||. Indeed, for any real f put a_i=||f||_{L2(I_i)}. Cauchy-Schwarz on each cell gives the absolute value of the kernel quadratic form <= sum B_ij a_i a_j <= ||B|| sum a_i^2. The same conclusion holds over complex scalars by taking absolute values. Self-adjointness gives the absolute operator norm.

For any exact positive vector v, Collatz-Wielandt gives ||B|| <= max_i (Bv)_i/v_i: B is symmetric and entrywise nonnegative, so its absolute spectral radius is its Perron root. Positive semidefiniteness is not required. A numerically selected binary64 v is an exact dyadic witness; only its directed row-sum check is used.

Let tau uniformly bound integral_{(0,infinity)^2 minus [0,L]^2} |A_rho(x,y)|^2 dx dy. Then the omitted kernel has operator norm at most its Hilbert-Schmidt norm sqrt(tau), including both off-diagonal rectangles. By the triangle inequality,

||A_rho|| <= max_i (Bv)_i/v_i + sqrt(tau).

The certificate computes tau from the source analytic bounds (153)-(154) and the polynomial-center moment tails. Their argument requires rho<1/2, so it remains valid throughout [2/5,43/100]. No sampled tail or assumed eigenfunction decay is used.

The script certify_positive_cells.py reuses the pinned author code's interval enclosure of the integrand in (151), takes its directed square root to obtain B, symmetrizes by entrywise maximum, and checks every row with outward rounding. Arb constructs all transcendental tables; directed binary64 primitives enclose the remaining operations and reductions. A strictly positive vector, finite entries, positive denominator, full slab coverage and total upper bound below 2 are required.

This certificate uses radial cell indicators rather than the Laguerre matrix of Theorem 1.6. That theorem's nonnegative positive-semidefinite matrix is for a different sphere-valued problem, with norm threshold 1. Its tail-trace lemma cannot be applied to the simplex matrix without proving positive semidefiniteness. The cell comparison above proves the needed norm threshold 2 directly, with a Hilbert-Schmidt tail.
