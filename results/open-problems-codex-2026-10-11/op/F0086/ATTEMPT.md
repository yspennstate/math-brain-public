# F0086: resolved in published literature, 2026-10-11

## Source and hypotheses
J. Ben Hough, Manjunath Krishnapur, Yuval Peres, Balint Virag,
Determinantal Processes and Independence, Probability Surveys 3 (2006),
206-229; DOI 10.1214/154957806000000078; arXiv:math/0503110.
Conjecture 40, Section 4.5, PDF p.22 / printed p.227, states:
If K is a (real) kernel defining a self-adjoint, non-negative integral
operator on L^2(Lambda) and 0 <= alpha <= 2, then the alpha-determinantal
process with kernel K exists. However, if alpha > 2, then there exists such
a kernel K for which there is no corresponding alpha-determinantal process.
The surrounding setup assumes locally compact Polish spaces, Radon reference
measures and locally trace-class kernels; the conjecture sentence does not
repeat those assumptions. The counterexamples below satisfy them.
The convention is det_alpha(A) = sum_sigma alpha^(n-c(sigma))
product_i A[i,sigma(i)], where c(sigma) is the number of cycles.

## Exact literature resolution
Petter Branden, Solutions to two problems on permanents,
Linear Algebra and its Applications 436 (2012), no.1, 53-58,
DOI 10.1016/j.laa.2011.06.022, arXiv:1104.3531v2 (30 June 2011).
Theorem 2.3, PDF p.4, classifies D_R, the parameters for which every real
symmetric positive semidefinite matrix of every size has nonnegative
alpha-determinant, as
D_R = {0} union {-1/m : integer m >= 1} union {2/m : integer m >= 1}.
Branden writes m+1 with m a nonnegative integer; positive m here avoids
ambiguity in N. His convention det_alpha = alpha^n per_(1/alpha) agrees
term by term with the source because per_beta uses beta^c(sigma).
Hence every positive alpha outside {2/m} admits a negative finite PSD
alpha-determinant. In particular alpha=3/2 disproves the interval assertion,
and every alpha>2 admits a bad kernel, proving the second assertion.

## Complete implication from the literature theorem to nonexistence
Fix alpha>0 outside {2/m}. Theorem 2.3 supplies a finite real symmetric
PSD matrix A of size n with det_alpha(A)<0.
Take Lambda=[0,n) with Lebesgue measure and I_i=[i-1,i), i=1,...,n.
Define K(x,y)=A[i,j] when x belongs to I_i and y belongs to I_j.
The indicators 1_(I_i) are orthonormal. The integral operator T_K acts
as A on their span and as zero on its orthogonal complement.
More explicitly, for f in L^2 let v_i=integral_(I_i) f(x) dx. Then
<f,T_K f>=v* A v >=0. Real symmetry gives self-adjointness.
The operator is bounded, finite rank and trace class, hence locally
trace class. Lambda is locally compact Polish and Lebesgue measure Radon.
For every tuple in I_1 x ... x I_n, all coordinates are distinct and the
matrix [K(x_i,x_j)] is A. The proposed nth joint intensity equals the
strictly negative constant det_alpha(A) on this product set of measure one.
A point process's factorial moment measure is a positive measure, and any
Lebesgue density of it is nonnegative almost everywhere. Contradiction.
Thus this regular real kernel has no alpha-determinantal process.
The construction avoids diagonal, atomic, simplicity and null-set issues.

## Primary-paper proof and referee checks
Read Theorem 2.3 and its complete proof on PDF pp.4-6. Its dependency is
Scott-Sokal's characterization of complete monotonicity of inverse determinant
powers, quoted as Theorem 2.6. For beta=1/alpha not a nonnegative
half-integer, choose d with beta<(d-1)/2. Rank-one PSD matrices spanning
Sym_d give an inverse determinant with a negative signed mixed derivative.
At a positive basepoint y, whitening changes the determinant into a positive
constant times det(I-X U^T U). The generalized MacMahon Master Theorem
(Theorem 2.4) identifies a negative Taylor coefficient with
per_beta((U^T U)[r])/r!, where [r] means row/column replication.
Replication preserves PSD (Remark 2.5). Multiplying by alpha^|r| gives a
negative alpha-determinant. This is a description of the published proof,
not an independent proof of its Scott-Sokal dependency.

Checked: real, not only complex, theorem; universal dimension quantifier;
parameter conversion; positive-measure negative intensity; PSD operator;
trace-class and topological assumptions. At alpha=0, the intensity is the
product of diagonals (Poisson case with locally finite intensity). At alpha=2/m,
the familiar real Gaussian-square Cox constructions / superpositions are
already known, as the source says immediately before Conjecture 40.

## Remaining gap and scope
No remaining gap for F0086's literature status: first assertion false,
second assertion true. No explicit numerical matrix at alpha=3/2 is supplied;
its existence follows from the published classification. No new theorem,
numerical counterexample or Lean verification is claimed. The user's
status-first instruction requires stopping upon a verified literature solution.
The September intake's open-status assertion was stale; speculative immanant
statements in the earlier attempt were not used.

## Continuation referee audit (2026-10-11)
Re-read the saved primary Theorem 2.3 against the recorded classification.
Rechecked the conversion alpha^n (1/alpha)^c = alpha^(n-c),
and the operator quadratic form and positive-measure product rectangle.
All three implications stand. For precision, [0,n) is Polish because it is
a G-delta subspace of the real line, and it is locally compact in its relative
topology. Negative factorial moment density on the rectangle suffices for
nonexistence without additional assumptions on simplicity.
Fixed an encoding defect in the first claim citation (author and page range).
The literature resolution remains decisive; no outstanding research gap
for the stated conjecture and no new explicit matrix claimed.
