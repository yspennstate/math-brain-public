# Regularized determinant estimate and a full-spectrum diffuse-range branch

Programme: QFORM-DENSITY-3EIG-20260922. Interactive run 20260922T131746Z-regularized-determinant, not a scheduled-worker login.

Canonical full proof, successfully committed and read back:
`yspennstate/math-open-problems@a302aab3477c64757b511e80d3907f982e04873a:proofnet24/QFORM-density/interactive/20260922T131746Z-regularized-determinant/REPORT.md`
Report blob: `080253f929411bfa9c7aa3254a2bdaf37be72ebb`.

Status: complete supporting analytic arguments supplied; independent reviews pending. Full arbitrary-matrix conjecture remains OPEN. No literature-wide novelty assertion or native learned-memory-ingestion assertion.

## New general estimate

For every symmetric A, every pair of disjoint ORIGINAL coordinate sets I,J, and B=A[I,J],

`|E exp(it X^TAX)| <= det(I+4t^2 BB^T/(pi^2 e^2))^(-1/8)`.

There are NO restrictions on the two self blocks, outside couplings, signs, input moments, or extra small singular values. Consequently five cross singular values >=sigma give continuous density <=5e/(2sigma). Five cross directions are a supporting branch, NOT the full three-eigenvalue hypothesis.

For 1<=q<2, if the coordinate leverage of the projection onto range(B) in R^I is <=q/2, the stronger estimate is

`|phi(t)| <= det(I+2q t^2 BB^T/(pi^2 e^2))^(-1/(4q))`.

If r>2q cross singular values are >=sigma, this gives

`||p_Q||_infinity <= e r/[sqrt(2q) sigma (r-2q)]`.

In particular q=1 uses three large cross directions and leverage<=1/2. Extra tiny singular values may be discarded from the REGULARIZED determinant without a loss. The full proof combines sharp Young for difference densities, sharp Hausdorff--Young, geometric Brascamp--Lieb on the graph of B, and correctly tracked decoupling. It does not transfer an Lp Fourier bound to an invalid pointwise scalar Fresnel bound.

## Full-spectrum diffuse-range theorem

Let U span the ENTIRE range of A with orthonormal columns. If every row has squared norm <=1/32 and A has at least three eigenvalues of magnitude>=1, then

`||p_Q||_infinity <= 96e/(7sqrt(2)) <27`.

All additional nonzero eigenvalues can be arbitrarily small, of either sign, and arbitrarily numerous. A continuous density vanishing at infinity is obtained. Adding any coordinate-separable measurable phase sum V_i(X_i), finite almost surely, is also allowed.

Proof: MSS Corollary 1.5 partitions the original frame into two blocks with Gram matrices between 7I/32 and 25I/32. The full cross block then has three singular values>=7/32 and range leverage<=1/7, so q=1 applies. The full spectrum is retained through the argument. MSS is prior work and is explicitly cited, not a new claim.

This removes the small-eigenvalue determinant loss in this additional geometric branch. It does NOT remove the range-leverage hypothesis: a full-rank matrix has all range leverages equal to one. A proof for arbitrary matrices must still handle the heavy-coordinate/nonseparable remainder or provide an exhaustive dimension-free reduction.

## Apply and independently review using existing workers

account02/B02: independently check Sections 3--6, especially the sharp Young constant, graph change-of-variable powers, Jensen/decoupling exponent, and orientation of the range projection. Compare to your exact-rank cross-block theorem, without conflating the two exponents.

account03/B04: independently check the graph Brascamp--Lieb normalization and Section 7's MSS partition, singular-value comparison, and arbitrary-small-extra-eigenvalue conclusion. Record an actual pass, gap, or refutation with the exact scope.

B08/B12 workers: use the result to attack the residual heavy/light or nonseparable bridge in your own current assignment; no need to duplicate both reviews. B19/B20 proof-assembly workers must keep the original three-eigenvalue target and identify a concrete sufficient exhaustive reduction rather than relabeling this branch as completion. The archive's isotropic heavy-row leakage obstruction is not resolved here.

Finite checks actually executed: scalar algebra identities, 25 frame/Gaussian graph instances, 22 uniform one-dimensional instances, 128 full Gaussian quadratic instances, nine additional spectral-transfer instances, and exact partition constants. These tests are not universal proof certificates. The full proof and executed check sources/results are provided with the report.

The earlier separable-phase result at commit 773b7fb6f0e6a8142066f0bac08d228dfc164fdb has now received a passing scoped independent review from account02/B08, documented in `handoffs/account02/B08/B08-20260922T124007Z-r11.md`; do not infer that this reviews the new determinant argument.

All existing workers remain exclusively assigned to QFORM. Preserve the existing check-in request, task identities, hourly cadence, quiet delivery and later-stop rules. No new tasks, emails, paid calls, remote workflows or cross-account native authentication are authorized.
