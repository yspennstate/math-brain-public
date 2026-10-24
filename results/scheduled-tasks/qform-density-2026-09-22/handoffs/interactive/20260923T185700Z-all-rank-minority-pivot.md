# QFORM interactive handoff — all-rank minority-sign Schur pivot

2026-09-23T18:57Z. Full conjecture remains OPEN.

Proved and committed in math repo at commit 2206a8b8cd7f7811cc4564868221158594dce4e6:
https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T185647Z-minority-pivot-all-rank/REPORT.md

Precise theorem: For independent original coordinates with densities <=1, let symmetric A have exactly one negative eigenvalue (zeros allowed), lambda_2(A)>=1, and some ORIGINAL diagonal A_ii<=-delta<0. Then every quadratic-plus-affine form Q has density satisfying
  ||p_Q||_infinity <= [3 sqrt(K2(3+log K2))]/sqrt(delta)
  =674.400889.../sqrt(delta),
where K2=4 sqrt(600)*4 sqrt(128)=4434.050067... comes from the manuscript's PSD second-level concentration proposition. The sign-reversed theorem holds for exactly one positive eigenvalue and two negative eigenvalues >=1 in magnitude when some original diagonal >=delta.

Proof novelty beyond exact-rank-three B11 predecessor: a negative scalar pivot produces PSD Schur complement S at arbitrary rank by inertia. The positive eigenvalue bound survives: for t>0, Schur(A-tI)=D-tI+vv^T/(|a|+t) <= S-tI=D-tI+vv^T/|a|, so lambda_k(S)>=lambda_k(A) for each positive eigenvalue. Thus lambda_2(S)>=1. Conditional scalar-square density gives a half-Riesz profile, and the manuscript's PSD alpha_2 bound plus composition yields the displayed density estimate. Affine terms remain arbitrary; no rotated-coordinate independence or support regularity.

This certificate is CONDITIONAL on the physical minority-sign diagonal size. It does not solve cases with all minority-sign physical diagonals zero/small, e.g. diffuse negative eigenvectors or cancellation from the opposite-sign positive diagonal contributions. Do not upgrade it to the full s3 theorem.

Existing core proof inputs: proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/manuscript/semidefinite.tex (Proposition sd:psd-levels(2), Lemma sd:composition(3)). Exact rank-three predecessor: proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/20260922T231431Z-account01-B11-QFORM-r11/REPORT.md.

Useful next branch: combine this exit with no-minority-physical-pivot structural analysis for one-minority-inertia A, while retaining all dense cross terms. No claim that small diagonals make the remainder ignorable.
