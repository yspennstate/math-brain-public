# Independent review: gluing, qualitative regularity, and Gaussian results

Review completed 23 September 2026. This is an independent mathematical review of the listed manuscript chapters. It certifies the checked arguments at their stated hypotheses, not novelty or a proof of the unrestricted dimension-free conjecture.

## Verdict

**PASS.** The complete gluing and fixed-matrix continuity arguments, the exact smoothing normal forms, and all Gaussian benchmark arguments checked below are valid. The Gaussian component-mixture theorem has the required hypotheses stated and its averaging argument and constants check. No remaining mathematical gap was identified in these chapters.

The qualitative continuity conclusion is substantial and may be stated without a smoothness, compact-support, connected-support, moment, or identical-distribution assumption on the original coordinate laws:

> For every fixed real symmetric matrix of rank at least three, every quadratic polynomial in independent coordinates with bounded densities has a bounded continuous density vanishing at infinity.

The proof gives a matrix-dependent bound. It does **not** bound that height uniformly by the third absolute eigenvalue alone.

## Reviewed file snapshots

| File | Lines | SHA-256 at review checkpoint |
|---|---:|---|
| `fleet_gluing.tex` | 826 | `44ee6282fa2eb7406f7341865b4a9252d4a1559bf492837eb44f575560158203` |
| `gaussian_benchmarks.tex` | 514 | `f707900a1870a794cf41ff502566b14d89582cdcc040f6956ccae4265316dc07` |
| `gaussian_mixture.tex` | 114 | `adb1d52b83f55752285d4d6c4ef281180bfcc5b16b1b34d55351df100929bc2a` |
| `fleet_supplement.tex`, after statement clarifications | 540 | `562a86af35260669235ad1b827597faeda259f70ecde7171add70255b28eb607` |

Later editorial changes may alter a hash; this record identifies the mathematical text inspected. The bibliography then contained 34 entries.

## Gluing proofs

### Product density and two physical hub coordinates

The exact product-density correlation identity is justified by nonnegative Tonelli before finiteness is known. The bounds on `K_f(r)` and `K_g(r)` have the correct behavior both below and above `|r|=1`. Centered uniform densities attain both bounds, so the squared L2 constant `4MN` is indeed sharp. The affine hyperbolic scaling divides the squared L2 norm by `2|c|`.

For `fg:two-hub`, the phase-weighted pushforward density is dominated by the ordinary slope density. Cauchy–Schwarz in the two original hub coordinates gives `pi P/|t|` with the stated Fourier convention. The separate L2 residual is independent, so multiplication of characteristic functions is legitimate. Integrating only the high-frequency tail against `|t|^{-1}` gives the stated optimization and constant `3*2^(-2/3)(P R2)^(2/3)`. The arbitrary measurable bank phase never needs smoothness or separability. The bound proves Fourier L1 and hence C0.

The pair/square estimates also check: Minkowski and the scalar negative moment give the pair Lp estimate; the two-root square formula gives its L^(3/2) estimate. Young with exponents 3 and 3/2 yields the constant six. Conditional C0 averaging is justified by a uniform bound and measurable continuous conditional versions.

## Qualitative C0 for every fixed matrix of rank at least three

### Critical point and far field

The signed-polar calculation in `fg:critical-ball` is valid for each signature in dimensions three and four. The constants `C3=2pi` and `C4=4pi` dominate the definite and indefinite cases. The near-critical density bound tends to zero as the ball radius tends to zero because `d-2>0`.

The far-field argument retains product provenance. Outside radius R, some partial derivative has size at least `2 sigma R/sqrt(d)`. On that set, solving in that original coordinate has at most two branches and costs at most `sqrt(d)/(sigma R)` after its density cap is used. The other factors retain mass one. Summing over the coordinate choices gives the stated `d^(3/2)/(sigma R)` bound.

### The annular exceptional region

If at most one derivative exceeds delta, choose the maximal derivative. Its size remains bounded below on the annulus. All other components of `Bx` are at most delta/2, so the projection onto the remaining original coordinates lies in a tube of radius O(delta) around a bounded line segment. Its dimension is `d-1`, so the tube volume is O(delta^(d-2)); this also covers the case of a projected segment reduced to a point. The inverse-branch integration and density caps therefore establish `fg:tube-bound` uniformly over the input laws.

### The good-region L1 comparison

In a telescoping product difference, a term containing `f_i-g_i` must be integrated in a **different** coordinate. The existence of two large derivatives supplies such a coordinate. Summing over the possible `j != i` and solving in j costs at most `2(d-1)/delta`; the remaining integration retains the L1 norm of `f_i-g_i` and mass one for the other densities. No trace or conditional cap for a rotated law is used.

First making the near, far, and tube contributions small and then making the input L1 error small proves uniform convergence of the output densities. Smooth cap-preserving approximations exist by truncation, disjoint replacement of the missing mass, and convolution. The smooth compactly supported case follows from coordinate charts away from the critical point and the same small critical-ball estimate. Thus the argument establishes C0 for rough laws without an unjustified rough change-of-variables regularity claim.

### General rank and affine terms

Symmetric elimination using invertible pivots of order one or two produces an invertible original principal block of order three or four whenever the full rank is at least three. The union of the pivot indices is a principal block of the original matrix, with determinant equal to the product of the successive pivot determinants.

An affine term in an invertible block is removed by translation of original coordinates, preserving their independence, mass, and density caps. The height bound depends on the fixed block but not the translation. Consequently conditioning outside this block yields measurable C0 densities bounded by the same constant. Dominated convergence makes their average continuous and makes it vanish at infinity. These checks establish `fg:fixed-matrix-continuity` as stated.

## Exact smoothing normal forms

The approximate-identity proof in `fg:kernel-recovery` works for any nonnegative L1 probability kernel, including an unbounded kernel, and for extended density heights. The fixed-kernel scaling identity includes the affine terms and the correct factor `s3(A)`. The restriction on the dilation retains admissibility.

The fixed-window weak-convergence lemma correctly uses continuity of the limiting distribution function and controls possible atoms in the approximating laws through the uniform bound on both right and left distribution functions. It makes no assertion uniform in shrinking window width.

For the countable heat formulation, the bathtub argument handles a threshold with infinite lower superlevel measure or nonattainment by an approximate fill. A bounded measurable set of measure one can be approximated by a rational finite interval union of exactly measure one; the correction of its total length costs at most its original symmetric-difference error. Generic rational symmetric matrices with nonzero entries and principal minors and simple spectrum are dense because the finitely many excluded polynomial zero sets have empty interior. The preliminary spectral dilation preserves a strict third-singular-value margin during rational approximation. The bounded product set justifies uniform polynomial approximation, and the heat bandwidth stays positive while it is approximated by rationals. No finiteness of the unrestricted supremum is assumed or concluded.

## Gaussian benchmarks

The central-square extraction is valid for every scaled noncentral chi-square with scale at least one. Both extra Laplace factors are compound Poisson transforms of nonnegative variables, and independence can be introduced in the distributional construction. Applying this separately to signed selected Gaussian coordinates is legitimate; all affine and kernel terms are absorbed into an independent remainder. The mixed-sign three-square density has the exact maximum `1/(2sqrt(2))`. The covariance congruence bound and rescaling therefore give the sharp Gaussian ceiling at the stated covariance floor.

The Lindeberg proof explicitly assumes finite means and variances, covariance and mean limits, and the vector Lindeberg condition. The scalar characteristic-function expansion yields the multivariate Gaussian limit. The cap-one covariance floor is `I/12`. The common integrable product-law Fourier envelope is the additional step that upgrades weak convergence to uniform density convergence; no such upgrade is inferred from weak convergence alone. The centered-uniform three-bank sequence realizes the sharp limit `3sqrt(2)`.

For the one-heavy family, the conditional polar kernel, its strict monotonicity, and the uniqueness of the centered unit interval optimizer check. The Laplace-ratio calculation and the normalized angular measure give the claimed uniform cone-tip bound. The rational certification of `<4.111374` was checked independently with exact fractions: the stated rational upper bound on sqrt(2) squares to more than two, and the even partial sum through degree 12 gives a total below the stated decimal bound.

The finite product realization has exactly the three claimed nonzero eigenvalues. The three-region estimate for the scalar bank characteristic functions proves L1 convergence and hence uniform convergence of their densities. The conditional angular formula then gives convergence of the cone-tip density for fixed positive a and fixed heavy law. The claim is not uniform as a tends to zero and is not a global output-level ceiling.

The Householder example’s polar formula provides a bounded dominating domain for the continuity argument. For each angle the exceptional boundary radii form a finite set, justifying dominated convergence at zero. The maximal-coordinate sectors and tangent-half-angle integral yield the displayed artanh expression. This value is not asserted to be the global maximum for that example.

## Gaussian component mixtures

All mixture variables are conditioned before the Gaussian rotation. The pairs are independent across coordinates; dependence between a coordinate's random mean and variance is allowed. Positive finite component variances preserve the matrix rank under congruence. The exact Gaussian modulus formula retains kernel linear terms and drops only a nonpositive exponential correction.

The squared-minor expansion includes intersections of the two coordinate subsets; their multiplicity is correctly recorded in `0 <= alpha_i <= 2`. Weighted AM–GM and the inverse-half-variance moment condition give exponents `alpha_i/k <= 2/k < 1`, so concavity applies. Their sum is two, giving the exact `2pi` cancellation against conditional Fourier inversion. The expected conditional Fourier L1 norm is finite, proving unconditional C0 in addition to the height estimate.

For deterministic component centers, monotone convergence toward the center identifies the essential density maximum with the average component peak, including the infinite case. Thus the centered-scale-mixture corollary really follows from the coordinate density cap. The converse is correctly withheld for random component centers. No assertion extends the theorem to all bounded densities by unrestricted Gaussian-mixture approximation.

The chapter provides the determinant and averaging proof and makes no priority claim. Its classical Gaussian citations and the adjacent HMP2025 discussion in the literature chapter are compatible with their actual scopes.

## Statement clarifications applied to the supplement

Following another independent reader's check, the complementary Schur theorem now explicitly requires the columns of Z to form an **orthonormal** basis of the complementary subspace. Its proof and quantitative statement use an orthogonal block basis, so this qualification is necessary. The random-slope proof now explicitly cites the two-sided negative-moment lemma, and the moving-ridge statement explicitly says the triple is independent of the hub X, without asserting independence inside the triple.
