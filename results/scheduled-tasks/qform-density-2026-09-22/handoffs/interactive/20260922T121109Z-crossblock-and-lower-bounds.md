# Interactive QFORM handoff: cross-block smoothing and constant lower bounds

Programme QFORM-DENSITY-3EIG-20260922; control revision 2026-09-22.5. This is an interactive mathematical contribution, not a scheduled-worker login or a native-memory receipt. No full solution or independent review is claimed.

## Immutable complete source

Repository: yspennstate/math-open-problems
Commit: 8624982153e5a2154e4ae8922d2fe4dc77080efc
Path: proofnet24/QFORM-density/fleet-2026-09-22/interactive/20260922T121109Z-crossblock-and-lower-bounds/REPORT.md
Blob: d0546b3190cb35a070fabd86162f4b4874975f62
Successful write and content readback observed.

## Results for existing workers to apply

**B08/B09/B10/B16/B19/B20:** For an original-coordinate partition I,J, if the cross block A[I,J] has rank r>2 and product Delta of ALL its nonzero singular values, the report proves ||p_Q||infinity <= (2r/(r-2)) Delta^(-1/r), with a continuous density. Arbitrary within-block quadratic and linear terms are permitted. The proof uses complex phase-weighted marginals, the Livshyts--Paouris--Pivovarov projection-density theorem, and a direct L2 bilinear Fourier bound for phi, avoiding the square-root loss from estimating |phi|^2. Rank exactly three with smallest singular value >=kappa gives 6/kappa. Do not replace the product of all singular values by only the top three without a new argument.

**B08/B10/B16:** For rank-exactly-three A=U Lambda U^T with U^TU=I_3 and |lambda_j|>=1, max_i ||row_i(U)||^2<=1/12 implies ||p_Q||infinity<=24 and a continuous density. A Bernoulli partition/Frobenius-norm existence argument gives two block Gram matrices >=I_3/4. This closes the previously unpaid sufficiently delocalized rank-three branch, including sufficiently large flat Hadamard frames. Mixed-leverage rank-three frames and arbitrary higher-rank spectral remainders are NOT covered.

**B17 and all constant trackers:** The iid-uniform six-variable form ((X1+X2)^2+(X3+X4)^2-(X5+X6)^2)/2 satisfies the full eigenvalue hypothesis and has continuous density p_Q(0)=2pi-7/3>pi. Thus the coordinate-diagonal pi upper bound is NOT a universal upper bound. A normalized block-sum limit proves that every universal constant must satisfy C>=3sqrt(2). The latter proof uses weak convergence and interval domination, not unsupported density convergence. These are lower bounds, not counterexamples to existence of a larger C.

**B07/B15:** The report also supplies qualitative law-uniform boundedness for each FIXED rank>=3 matrix A: select a nonsingular principal block of size 3 or 4 via Schur-complement pivots, then condition outside it. The constants are (2pi+3sqrt(3))/kappa and (pi^2+8)/kappa, respectively. This extends the completed B15 three-dimensional proof. The potentially very small block kappa prevents this from proving the desired universal C. Continuity is not established by that interval argument.

## Corrections and status

Consumed QFORM-CROSSMINOR-ALONE-FALSE: the new direct Fourier theorem requires r>2 and is consistent with the 2x2-cross-block logarithmic counterexample. It does not reinstate the false single-square pointwise Fresnel bound. All input laws remain arbitrary probability densities <=1; no Gaussian or moment hypothesis is used in the upper bounds.

Proofs are supplied and source-pinned, but no independent end-to-end review is yet observed. Full arbitrary-n universal upper bound remains NOT PROVED. Suggested next mathematical use is to combine the new diffuse branch with a valid mixed-leverage or higher-rank mechanism, rather than re-prove the already closed flat-frame case. Preserve all owner scope, quiet-delivery and memory safeguards. Native brain status remains WITHOUT_VERIFIED_BRAIN.
