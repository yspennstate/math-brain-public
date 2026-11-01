# Root corollary — full active covariance for the X019 flags

Status: proved application of a prior theorem to the newly certified X019 family. Root integration, not an additional worker.

Let W,U,Z be any flag in X019's Theorem1, and choose an isometry V onto U. Then

    M -> H(P_(P_W+V M V*))

is concave for every Hermitian 0≤M≤I₂, including arbitrary noncommuting endpoints.

X019 proves an unlabeled projection diamond for every such flag. The prior ROOT_DIAMOND_ACTIVE_MATRIX.md theorem applies to every certified flag with k=min(rank W, codimension(W+U))≤4. Here both quantities equal2. Its exact full active Hessian decomposition controls det A≤0 by log-submodularity of the same measured law, and controls det A>0 by the extreme-count Fisher bound, giving

    −H''(M)[A,A] ≥ (8−2log2−4log3) det A >0

for definite A. The coefficient is positive, e.g. log2<1 and log3<3/2 give a strict positive bound. Integration and entropy continuity give the closed active domain. Impossible measured atoms stay outside the common positive support.

Thus the X019 coupling has the stronger full active-matrix consequence, beyond the opposite-slope fixed-basis deduction stated in its report. X017 gives the sharper invariant criterion and constant once β* of the flag is evaluated. Neither corollary permits the background, active plane, or zero plane to move along the same segment; nor does it prove unrestricted six-site concavity.

Source paths: agents/X019.md in this campaign; ../creative-2026-09-15/ROOT_DIAMOND_ACTIVE_MATRIX.md in the same GitHub track.
