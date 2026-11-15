---
name: c0033b_determinantal_entropy_star_and_three_point_rank_two
status: verified
scope: finite Hermitian determinantal kernels; proofs in REPORT.md
---

For Q=[[a,v*],[v,C]], with C fixed, DPP entropy is jointly concave in a and v. Conditional occupancy r_T=a-v*(C-D)^{-1}v decreases with the complement pattern T. Thus h'(r_T) increases, and Loewner stochastic domination implies the matrix sum pi_T h'(r_T)(C-D)^{-1} is positive semidefinite. The conditional entropy Hessian is a negative square plus the negative of this matrix form. See REPORT.md, Theorem 2.1, and verify_certificates.py. This covers indefinite rank-two changes in a whole row and column in any dimension.

For n=3, let ell_ij^0 and ell_ij^1 be the two conditional nonnegative log-odds ratios. Their difference gamma is common to all pairs. Then R=diag(ell_23^0,ell_13^0,ell_12^0)-gamma Q is positive semidefinite, using Q for gamma<=0 and I-Q for gamma>=0. The entropy Hessian is -Fisher+2 tr(adj(A) R). Hence it is nonpositive for every indefinite rank-two A; its full positive index is at most one. See REPORT.md, Section 3 and Proposition 4.1. Full three-point concavity is not established.

Do not generalize the PSD matrix certificate to the second compound matrix in arbitrary dimension. Strict order-five kernels give a negative exterior Rayleigh quotient about -0.02581933223; wedge_interval.py validates its sign and kernel feasibility with outward-rounded intervals. The bivector is not decomposable, so this does not refute rank-two entropy concavity. Orders six and eight give additional high-precision failures. General rank two and arbitrary commuting segments remain open.

The shared brain and checklist stores were read-only in this sandbox. This note preserves the selective mathematical learning locally for later ingestion; no shared index was edited.
