# Local Ward identity needed for the H3 response formula

2 October 2026. Independent derivation by heat_entropy, coinciding with an
independent derivation by k_theory_candidates. This note supplies a local
algebraic identity and the root restriction required when using it. A general
H3 theorem is being assembled and audited separately; this note alone does
not establish any all-orders high-fugacity theorem.

## Local setup

Use the equality geometry of the H2 theorem. Let E be the nonzero support of
the marked e-potential, and let A=N(E) intersect S be its boundary port set.
Assume the grounded vertex r is outside A. Boundary fields on A are thus free
Grassmann variables; no field in A has been fixed to zero.

Let

\[
 M_E(t;\psi_A)=\left\langle\exp(tV_E)\mid\psi_A\right\rangle_E,
 \qquad U_e(t)=\partial_e\log M_E(t)
             =tU_{e,1}+t^2U_{e,2}+\cdots.
\]

The first score is
\(U_{e,1}=\mathrm{constant}+\bar\psi_A B_e\psi_A\), where B_e is the
boundary cycle-flow response matrix, extended with zero rows away from A.
It has zero row sums in the full ungrounded port coordinates.

The claimed identity is

\[
 \boxed{D_{\mathbf1_A}U_{e,2}=-\bar\psi_A B_e\psi_A.}
\]

Here D is the rank-one Gaussian lowering contraction, so
\(D_{\mathbf1}q_i=1\) and
\(D_{\mathbf1}(q_iq_j)=q_i+q_j-\bar\psi_i\psi_j-\bar\psi_j\psi_i\).

## Exact local invariance

For any edge xy define

\[
 F_{xy}(t)=q_x+q_y-\bar\psi_x\psi_y-\bar\psi_y\psi_x-tq_xq_y.
\]

Use left odd Grassmann derivatives and define

\[
 Q_t=\sum_x(1-tq_x)\partial_{\psi_x},\qquad
 \bar Q_t=\sum_x(1-tq_x)\partial_{\bar\psi_x}.
\]

Direct differentiation gives Q_t F_xy=barQ_t F_xy=0. For example
Q_t q_i=-barpsi_i, and the t-dependent variation of the cross bilinears is
cancelled by that of -t q_xq_y.

Consider the unnormalized interior integral

\[
 I_E(t;\psi_A)=\int d\bar\psi_Ed\psi_E
  \prod_{i\in E}(1+tq_i)
  \exp\left[\sum_{g\text{ incident to }E}c_gF_g(t)\right].
\]

Let W=prod_i(1+tq_i). The boundary derivative of this integral equals the
negative of the interior odd derivative of its exponential, since each bond
is invariant under the combined interior and boundary transformation.
Interior integration by parts makes that derivative zero. Explicitly,

\[
 \partial_{\psi_i}(1-tq_i)=t\bar\psi_i,
 \qquad (1-tq_i)\partial_{\psi_i}W
          =-t\bar\psi_i\prod_{j\ne i}(1+tq_j).
\]

These two terms cancel in
partial_psi_i[(1-tq_i)W]. The barred calculation cancels
-t psi_i against +t psi_i. Thus

\[
 Q_{t,A}I_E=\bar Q_{t,A}I_E=0.
\]

This is a finite exterior-algebra integration-by-parts statement; no positive
measure or analytic limit is used.

## Why conditional normalization does not break the marked identity

Completing the interior Gaussian square gives

\[
 I_E=\det L_{EE}\,
     \exp(\bar\psi_A N_E\psi_A)\,M_E,
\]

where N_E is the local Dirichlet Schur complement on A. The marked endpoint
exit rows are equal. Hence changing e leaves the harmonic extension fixed and
changes its Dirichlet energy by
\(\partial_eN_E=(p_a-p_b)^T(p_a-p_b)=0\).
Consequently

\[
 U_e=\partial_e\log I_E-\partial_e\log\det L_{EE}.
\]

The subtracted term is independent of boundary fields. Q_t is independent of
the marked conductance. Since I_E has a nonzero constant term, its formal
logarithm is well defined after extracting that scalar. Thus

\[
 Q_{t,A}U_e=\bar Q_{t,A}U_e=0.
\]

The Dirichlet background is not itself invariant, but its marked derivative
vanishes. This distinction is essential.

## Expansion and the contraction sign

Write Q_t=Q_0-t sum_i q_i partial_psi_i. The first two orders of score
invariance give

\[
 Q_0U_{e,1}=0,
 \qquad Q_0U_{e,2}=\sum_iq_i\partial_{\psi_i}U_{e,1},
\]

and the barred counterparts. Put

\[
 P_e=\sum_{i<j}(B_e)_{ij}q_iq_j.
\]

Direct differentiation of this polynomial produces exactly the right-hand
sides in the second-order equations. Thus U_e2-P_e is invariant under both
ordinary translations Q_0 and barQ_0. The two odd derivatives obey
\(\bar Q_0Q_0=-D_{\mathbf1}\), so the remainder has zero D_1 contraction.
Using the zero row sums of B_e,

\[
 D_{\mathbf1}P_e
 =\sum_{i<j}(B_e)_{ij}q(\psi_i-\psi_j)
 =-\bar\psi_A B_e\psi_A.
\]

This proves the boxed identity, without assuming that higher scores depend
only on the linear range of B_e. They generally do not: the exact two-port
gadget in `local_score_grassmann_heat.py/.json` has a nonzero order-two
quartic score term.

## Root restriction and application at H2=0

The local port transformations above cannot be applied to a port whose
Grassmann field has been grounded. At H2=0 with both response matrices
nonzero, the port sets A and C of the two marked sides satisfy
|A intersect C|<=1: otherwise a common nonzero contrast belongs to both
response ranges and cannot be orthogonal in the positive Green metric.
Choose r in A minus C, and apply the Ward identity only on the f side C.
The f-response potentials then vanish identically on A, so the e-side
second-score covariance is zero without using an e Ward identity. The
e-response potentials are constant on C; their constant-mode contraction
of the f-second score is exactly the identity proved here. This one-sided
choice avoids the grounded-port issue.

If one response matrix is zero, its marked support attaches at a single
port; that is a forest block-independence case and needs no H3 argument.
