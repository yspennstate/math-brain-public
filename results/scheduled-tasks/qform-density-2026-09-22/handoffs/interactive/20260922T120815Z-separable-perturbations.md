# Separable-phase extension of the diffuse quadratic-density theorem

Programme QFORM-DENSITY-3EIG-20260922. Claim QFORM-DIFFUSE-SEPARABLE-PHASE-v1. Interactive work, not a scheduled login. Full conjecture remains OPEN. Complete supporting proof supplied; independent reviews PENDING.

Canonical report, successfully committed and read back:
`yspennstate/math-open-problems@773b7fb6f0e6a8142066f0bac08d228dfc164fdb:proofnet24/QFORM-density/interactive/20260922T120815Z-separable-perturbations/REPORT.md`
Blob: `d08d2488c072386e2b8ad818e30b1a6dec79e63a`.

## Exact result

Let U have r>=3 orthonormal columns and row leverage c_i=||u_i||^2<=1/2, and let Lambda be real symmetric invertible. For independent probability densities 0<=f_i<=1 and ANY real measurable coordinate functions V_i, finite almost surely,

`T=(U^T X)^T Lambda(U^T X)+sum_i V_i(X_i)`

has a bounded continuous density vanishing at infinity, with

`||p_T||_infinity <= [r/(r-2)] B(U)^(2/r) |det Lambda|^(-1/r) <= [e r/(r-2)] |det Lambda|^(-1/r)`,

where `B(U)=prod_{c_i>0}(1-c_i)^(-(1-c_i)/2)`. In particular r=3 and |det Lambda|>=1 give 3e.

This extends account02/B08's source-pinned diffuse-rank proof by replacing the original input amplitude with `h_{i,t}=f_i exp(i t V_i)`. The complex amplitudes retain exactly the same L^p norms, so geometric Brascamp-Lieb plus sharp Hausdorff-Young give a phase-uniform L^1 Fourier bound. Gaussian-regularized inversion is justified for the complex projected L^1 measure, with no assertion of independence of the quadratic summands. The report supplies every step and constant.

Consequences: arbitrary DIAGONAL quadratic perturbations and linear terms are allowed. If only one physical principal block has the representation D+U Lambda U^T, every outside coefficient and cross-coupling can also be arbitrary, by original-coordinate conditioning and a uniform conditional characteristic-function estimate. This handles some genuine full-rank indefinite forms with extra small eigenvalues. It does not establish a suitable decomposition for every A in the target.

Example: U=(I_3;I_3)/sqrt(2), Lambda=diag(2,2,-2), D=I_6/10. Full eigenvalues are 2.1,2.1,-1.9,0.1,0.1,0.1 and the sharper bound is 3. Exact symbolic example/prefactor checks passed; these are not universal proof certificates.

## Existing-worker review and use

account02/B08: independently check the extension of your unperturbed proof to complex amplitudes; in particular the t-dependent marginal and domination/Fourier-inversion steps. account04/B12: independently check the separable perturbation and principal-block conditioning corollaries, including all signs and arbitrary additional outside eigenvalues. Publish actual review records, not presumed approvals. Other B08/B12 workers may derive complementary generalizations. B19 and B20 proof-assembly workers should use only the stated supported scope.

First remaining full-target implication: obtain a product-preserving reduction for arbitrary admissible A that provides sufficient diffuse curvature or closes the leverage-heavy/nonseparable branch with one universal constant. Neither the spectral hypothesis nor a bounded projection density alone presently supplies that implication. Do not rename this supporting result as the full theorem.

The all-worker check-in request QFORM-CHECKIN-20260922T120815Z remains active. Mathematical work continues without waiting for the acknowledgement sweep. No new task, email, public release, paid call, cross-account native access, or native-memory-ingestion claim is involved.
