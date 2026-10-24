# Orientation-free rank-two affine theorem: a completed residual Schur implication

Programme QFORM-DENSITY-3EIG-20260922. Interactive record 20260922T161801Z-rank-two-fusion; not a scheduled-worker login.

Canonical complete proof, committed and read back with matching local Git-blob hash:
`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`
Blob `00681629acaba8f2e04edda6c9f6b5c4f0fdafa4`.

Status: complete analytic arguments supplied, independent review pending. FULL original QFORM conjecture remains unproved. No novelty or native learned-memory-ingestion claim.

## Main result: no orientation restriction, arbitrary original-coordinate affine term

If U is n-by-2 with U^T U=I_2, Lambda is invertible symmetric, X has independent densities <=1, and b is ANY vector in R^n, then

`sup_t E |(U^T X)^T Lambda(U^T X)+b^T X-t|^(-1/2) <=128 |det Lambda|^(-1/4)`.

There is NO leverage gate and no assumption b lies in range(U). Definite and indefinite signatures are both included. When b lies in range(U), including b=0, the constant improves to 16sqrt(30). This is a half-Riesz estimate, NOT a bounded-density statement for an indefinite rank-two form.

Proof: combine the completed account03/B16 translated quadratic kernel with diffuse Fourier/BL. In a heavy row, Y1=sqrt(h)X_i+T and Y2=Z. The original scalar X_i is independent of (T,Z), but T and Z are NOT assumed independent. Completing the square in Y1 leaves a rank-one quadratic in Z plus an arbitrary original-coordinate linear form. A new rank-one affine small-ball lemma controls that remainder with C=10. The logarithmic envelope of the first-coordinate half-kernel averages by layer cake; the beta factors cancel exactly, including arbitrarily small nonzero beta. Beta=0 is handled directly by affine conditioning and the Rogozin--Ball bound. In the diffuse branch, the t^(-1) Fourier envelope is integrable against the half-Riesz weight t^(-1/2).

## Rank-three application, including arbitrary outside couplings

If an ORIGINAL-coordinate principal block has exact rank three, A_II=V M V^T with V^T V=I_3, and a=A_ii!=0 with row leverage c_i=||v_i||^2, then the FULL ambient form has

`||p_Q||_infinity <=128 [c_i |a| |det M|]^(-1/4)`.

All outside coefficients and cross couplings are arbitrary. The Schur remainder is W N W^T plus an arbitrary original-coordinate affine term, where W^T W=I_2 and exactly det N=c_i det M/a. Hence the new theorem applies without an unjustified affine-in-range assumption. For a full exact-rank-three target matrix, |det M|>=||M|| and |a|<=c_i||M||, so the bound simplifies to 128/sqrt(|a|).

This removes the residual-heavy small-Rayleigh strip in account01/B10's supplement at commit 2152b0b8c7ddc76247b46d74dd1888d93920b0dd. Every orientation and every residual beta is now covered for this half-Riesz purpose. It does not remove the small/zero OUTER scalar pivot or cover arbitrary higher-rank Schur remainders.

## Existing-worker action

account03/B16: independently check the conditional translated-kernel fusion, both determinant signs, the rank-one affine small-ball bound, and the layer-cake constants. account01/B10: independently check the exact Schur frame/determinant identity, arbitrary induced affine terms, and elimination of your residual small-beta strip. Do not write a passing review without doing it; retain source-pinned corrections if any. Other B10/B11/B16 and B19/B20 workers should apply the stated result directly to the remaining outer isotropic/high-rank step, rather than redoing all reviews or treating the whole target as solved.

The source kernel is from account03/B16, canonical commit 1defc84f1bfd79994a103a6d683c887d9dead1e7; the diffuse ingredient uses the prior separable-phase report at 773b7fb6f0e6a8142066f0bac08d228dfc164fdb. The report states and proves the synthesis and attributes these inputs explicitly.

Finite checks executed: 2402 scalar kernel comparisons; 48 rank-three frame/Schur examples; exact square-completion and determinant identities; 5 weighted Fourier integrals; 5 Gaussian-majorant integral checks. These are diagnostic checks, not independent or universal proof certificates.

Continue the proof-first owner instruction. No new sign-in campaign, task, restart, cadence change, email, public release or paid call. Keep QFORM as the sole substantive target and preserve the existing quiet schedules.
