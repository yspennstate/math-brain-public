# Internal learning retained within the authorized directory

Status: proved here, subject to independent mathematical review.

E0082 uses the same Pitman–Tang first-passage family as internal E0081. The source's published version includes Peres's n log n order conjecture as Conjecture 1, equation (30), p. 65. The claimed linear upper bound in the task premise is incorrect.

REPORT.md reconstructs the internal record-range proof of two-sided n log n bounds and supplies a bridge equivalent with an explicit Shepp integral series. For the matrix convention M_ij=sum_l 2^(-l) epsilon_l(A_i,A_j), the correct first-hit vector satisfies M*pi=ET/2^n*1. Thus mean column sums must be weighted by the first-hit word law. Uniform family-word averaging is insufficient. Uniform FP column sums have mean asymptotic (log n)/(2 pi), but this alone does not evaluate the inverse-matrix sum.

Numerical evidence: c_BR(0) approximately 1.544, c_BR(1) approximately 2.414; these are not certified decimals. Exact finite matrices and independent Markov chains agree in all 27 checked parameter rows. No sharp FP n log n coefficient was proved.

This note is a local artifact, not a write to the shared brain. The task explicitly restricted work to this directory, and the sandbox disallowed writes to the global brain and coordination stores.
