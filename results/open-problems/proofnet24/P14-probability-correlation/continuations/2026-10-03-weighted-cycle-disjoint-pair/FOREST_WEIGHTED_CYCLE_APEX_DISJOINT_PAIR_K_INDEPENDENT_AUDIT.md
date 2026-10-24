# Independent audit: arbitrary weighted-cycle apex roots and disjoint pairs

3 October 2026 UTC. **PASS.** Let \(H=C_n\), \(n\geq3\), have arbitrary
finite rim activities \(\lambda_i\geq0\) and arbitrary profile weights
\(\beta_i\geq0\). The one-apex ordinary-forest partition \(D(s)\), with
spoke \(i\) of activity \(s\beta_i\), has only negative real zeros. Its
degree is the number of positive profile entries. The statement also holds
for the two-vertex multigraph \(C_2\) with two labeled parallel rim edges of
arbitrary activities.

Combined with Sections 2--4 of
forest_disjoint_rank_one_attachment_forest_backbone_proof.md, this proves
all-activity negative correlation for the two disjoint marked edges among
four new vertices with spoke rows
\(a\beta,b\beta,c\beta,d\beta\). For positive marked-edge activities, the
inequality is strict exactly when \(abcd>0\) and at least two profile entries
are positive. Under positive-probability coordinate conditioning of rim
edges, strictness instead uses the number of contracted components having
positive profile sum.

I independently reconstructed the two-state transfer, its double-count
correction, the monodromy recurrence, the weighted-Hermitian boundary, all
zero-parameter limits, the \(C_2\) and conditioning cases, and the interface
with the four-core proof. A standalone exact checker imports no proposed or
forest-backbone implementation. I found no mathematical gap or
counterexample. Historical novelty and external peer review are not
certified.

## 1. Literal apex expansion

Index vertices modulo \(n\), and let rim edge \(e_i\), of activity
\(\lambda_i\), join vertex \(i-1\) to vertex \(i\). If \(A\) is a backbone
forest and \(C\) ranges over its components, then the allowed choices of
apex spokes in \(C\) have total weight

\[
1+s\sum_{i\in C}\beta_i.
\]

Hence the actual unrooted-forest partition is

\[
D(s)=\sum_{\substack{A\subseteq E(C_n)\\A\text{ acyclic}}}
       \lambda_A\prod_{C\in\operatorname{comp}(A)}
       \left(1+s\sum_{i\in C}\beta_i\right).
\]

Every coefficient is nonnegative and \(D(0)>0\). If exactly \(r\) profile
entries are positive, the degree is exactly \(r\): no term can select more
than those \(r\) nonzero spokes, while the empty rim forest permits selecting
all of them and contributes their positive product to the leading
coefficient.

For a nonempty selected spoke set \(S\), its vertices split the cycle into
cyclic rim gaps. No two vertices of \(S\) lie in one backbone component
exactly when at least one edge is absent in every gap. The total edge weight
for a gap \(I\) is therefore

\[
g(I)=\prod_{i\in I}(1+\lambda_i)-\prod_{i\in I}\lambda_i.
\]

Thus the coefficient belonging to \(S\) is
\(\beta_S\prod_Ig(I)\). For \(S=\varnothing\), all rim subsets are allowed
except the full cycle, giving

\[
D(0)=\prod_i(1+\lambda_i)-\prod_i\lambda_i.
\]

This literal gap expansion is the reference against which I audited the
transfer.

## 2. The two-state transfer and the \(2\Lambda\) correction

Define

\[
T_i(s)=
\begin{pmatrix}
1+\lambda_i+s\beta_i&s\beta_i\lambda_i\\
1&\lambda_i
\end{pmatrix},
\qquad
\Lambda=\prod_i\lambda_i.
\]

Split

\[
T_i=A_i+s\beta_iB_i,\qquad
A_i=\begin{pmatrix}1+\lambda_i&0\\1&\lambda_i\end{pmatrix},
\qquad
B_i=uv_i^T,
\]

where \(u=(1,0)^T\) and \(v_i=(1,\lambda_i)^T\). Since each \(B_i\) has
rank one, a nonempty selected set in the trace expansion factors into one
scalar for each cyclic gap. Direct multiplication of the lower-triangular
\(A_i\)'s gives

\[
v_b^TA_{b-1}\cdots A_{a+1}u
=\prod_{i\in I}(1+\lambda_i)-\prod_{i\in I}\lambda_i
=g(I),
\]

where \(I\) is the rim gap terminating at \(b\). The one-edge base case is
\(v_b^Tu=1=(1+\lambda_b)-\lambda_b\), and adjoining another
lower-triangular factor proves the displayed identity inductively. Cyclicity
of trace closes the final gap. Therefore every positive-degree coefficient
of

\[
\operatorname{tr}(T_{n-1}\cdots T_0)
\]

is exactly the literal spoke-set coefficient from Section 1.

At \(s=0\), the product of the \(A_i\)'s is lower triangular, so its trace is

\[
\prod_i(1+\lambda_i)+\Lambda.
\]

The correct forest constant is
\(\prod_i(1+\lambda_i)-\Lambda\). Consequently

\[
\boxed{
D(s)=\operatorname{tr}(T_{n-1}(s)\cdots T_0(s))-2\Lambda.
}
\]

Both copies of \(\Lambda\) are necessary. The correction changes only the
constant coefficient, so there is no selected-spoke overcount hidden in
this step.

The derivation also works for \(n=2\). The two matrices correspond to the
two labeled parallel edges; selecting both rim edges is the forbidden
graphic-matroid two-cycle. A one-edge cyclic gap has weight
\((1+\lambda_i)-\lambda_i=1\), exactly as the rank-one transfer gives.

## 3. Determinant and the monodromy eigenvalue

Put

\[
c_i=\lambda_i(1+\lambda_i),\qquad
\delta=\prod_i c_i.
\]

The determinant of each transfer is independent of \(s\):

\[
\det T_i(s)
=\lambda_i(1+\lambda_i+s\beta_i)-s\beta_i\lambda_i
=c_i.
\]

Hence the monodromy

\[
M(s)=T_{n-1}(s)\cdots T_0(s)
\]

has determinant \(\delta\). Initially assume every \(\lambda_i,\beta_i>0\).
If \(D(s)=0\), the transfer identity gives

\[
\operatorname{tr}M(s)=2\Lambda.
\]

Although \(s\) is not yet known to be real, the characteristic polynomial of
\(M(s)\) is therefore

\[
q^2-2\Lambda q+\delta.
\]

Moreover

\[
\delta=\prod_i\lambda_i(1+\lambda_i)
       >\prod_i\lambda_i^2=\Lambda^2.
\]

Thus the two monodromy eigenvalues are the fixed conjugate pair

\[
\rho,\bar\rho
=\Lambda\pm i\sqrt{\delta-\Lambda^2},
\qquad |\rho|^2=\delta.
\]

They are distinct, so a nonzero \(\rho\)-eigenvector exists.

## 4. Recurrence and index audit

Extend the transfer coefficients periodically. Starting from a
\(\rho\)-eigenvector of \(M(s)\), define

\[
\binom{x_{i+1}}{y_{i+1}}
=T_i(s)\binom{x_i}{y_i}.
\]

Then

\[
y_{i+1}=x_i+\lambda_i y_i,
\qquad x_i=y_{i+1}-\lambda_i y_i,
\]

and the first transfer row gives

\[
\begin{aligned}
y_{i+2}
 &=(1+\lambda_i+\lambda_{i+1}+s\beta_i)y_{i+1}
   -\lambda_i(1+\lambda_i)y_i\\
 &=(1+\lambda_i+\lambda_{i+1}+s\beta_i)y_{i+1}
   -c_i y_i.
\end{aligned}
\]

This confirms both neighboring-\(\lambda\) indices and the placement of
\(\beta_i\). Monodromy of the vector implies

\[
y_{i+n}=\rho y_i.
\]

The scalar sequence is nonzero: if every \(y_i\) vanished, the second
transfer equation would force every \(x_i\) to vanish as well.

With \(j=i+1\), the recurrence is the generalized eigenvalue equation

\[
(L_\rho y)_j=s\beta_{j-1}y_j,
\]

where

\[
(L_\rho y)_j
=y_{j+1}+c_{j-1}y_{j-1}
 -(1+\lambda_{j-1}+\lambda_j)y_j
\]

and the boundary is quasi-periodic:
\(y_n=\rho y_0\), \(y_{-1}=\rho^{-1}y_{n-1}\).

## 5. Weighted-Hermitian boundary

Set

\[
m_0=1,\qquad m_{j+1}=\frac{m_j}{c_j},
\]

and use

\[
\langle u,v\rangle_m=\sum_{j=0}^{n-1}m_j\overline{u_j}v_j.
\]

All \(m_j\) are positive. For an interior neighboring pair,

\[
m_j(L_\rho)_{j,j+1}=m_j
=m_{j+1}c_j
=m_{j+1}\overline{(L_\rho)_{j+1,j}},
\]

so the off-diagonal entries are adjoints. For \(n\geq3\), the only delicate
pair is the wraparound:

\[
(L_\rho)_{0,n-1}=\frac{c_{n-1}}{\rho},
\qquad
(L_\rho)_{n-1,0}=\rho.
\]

Since \(m_{n-1}=1/(c_0\cdots c_{n-2})\),

\[
\begin{aligned}
m_0(L_\rho)_{0,n-1}
 &=\frac{c_{n-1}}{\rho},\\
m_{n-1}\overline{(L_\rho)_{n-1,0}}
 &=\frac{\bar\rho}{c_0\cdots c_{n-2}}
  =\frac{c_{n-1}}{\rho},
\end{aligned}
\]

where the last equality is exactly
\(|\rho|^2=\prod_i c_i=\delta\). The diagonal entries are real. Hence
\(L_\rho\) is self-adjoint in this weighted inner product; the modulus
condition is neither missing nor reversed.

For \(n=2\), the forward and backward neighbors coincide, so their
contributions must be added rather than treated as two matrix positions.
The two off-diagonal entries are

\[
(L_\rho)_{0,1}=1+\frac{c_1}{\rho},
\qquad
(L_\rho)_{1,0}=c_0+\rho.
\]

With \(m_0=1,m_1=1/c_0\),

\[
m_0(L_\rho)_{0,1}
=1+\frac{c_1}{\rho}
=1+\frac{\bar\rho}{c_0}
=m_1\overline{(L_\rho)_{1,0}},
\]

again exactly because \(|\rho|^2=c_0c_1\). Thus the parallel-edge case is
genuinely included; it is not inferred from an \(n\geq3\) boundary matrix
whose two off-diagonal positions would be distinct.

Let \(B=\operatorname{diag}(\beta_{j-1})\). Under the present strict
positivity assumption, \(B\) is positive definite. Therefore

\[
s=\frac{\langle y,L_\rho y\rangle_m}
        {\langle y,By\rangle_m}\in\mathbb R.
\]

Every zero of \(D\) is real. Since every coefficient of \(D\) is positive
when all \(\beta_i>0\), while \(D(0)>0\), no zero is nonnegative. All \(n\)
zeros, counted with multiplicity, are strictly negative. The argument does
not assert that arbitrary nonuniform data always give distinct zeros.

## 6. Zero rim activities and zero profiles

The monodromy proof divided by \(c_i\), so zero parameters must be handled
separately.

If one or more \(\lambda_i=0\), the cycle is broken into a weighted forest.
The already audited forest-backbone determinant theorem directly gives
negative real apex roots for arbitrary nonnegative profiles. Alternatively,
replace each zero \(\lambda_i\) by a positive \(\epsilon\). The coefficient
vector of \(D_\epsilon\) converges to that of \(D\); with positive profiles,
the leading coefficient \(\prod_i\beta_i\) is independent of the rim
activities, so the degree does not drop, and the real-rooted limit is
immediate.

If some \(\beta_i=0\), replace it by \(\beta_i+\epsilon\). Real-rooted
polynomials form a closed set under coefficientwise limits, allowing roots
to escape to infinity when the degree drops. More explicitly, a finite
nonreal zero of the limit would, by a small conjugation-symmetric
Rouché contour, force nonreal zeros of all sufficiently close positive
approximants. This is impossible. The limit is nonzero because \(D(0)>0\).
Its finite roots are therefore real; nonnegative coefficients and positive
constant term force all of them to be negative.

If exactly \(r\) profiles are positive, Section 1 showed that the limiting
degree is exactly \(r\). Thus the Stieltjes rank, and later strictness, is
\(r\), not necessarily the number \(n\) of cycle vertices. With zero or one
positive profile the disjoint marked edges are independent; with at least
two, the first Stieltjes bracket is strict when all four row factors are
positive.

These continuity arguments also cover simultaneous zero rim activities and
profiles. If all profiles vanish, \(D\) is the positive constant \(D(0)\)
and has no zeros.

## 7. Coordinate conditioning, including \(C_2\)

Fix any positive-probability coordinate conditioning of rim indicators.
Contract every required-present rim edge, sum the profiles in each
contracted block, and delete every required-absent edge. The fixed product
of required-present activities is a common positive factor.

If at least one rim edge is required absent, the remaining optional
backbone is a forest, so the forest-backbone theorem applies. If no rim edge
is fixed absent and contraction leaves at least three blocks, the optional
edges form another cycle with arbitrary inherited edge activities and
arbitrary profile sums, covered by the theorem audited here. If two blocks
remain, the two remaining edges are parallel and form the weighted \(C_2\)
case already included in the transfer and Hermitian proof.

If contraction leaves one block, every remaining rim edge is a loop and is
forced absent in a forest; the effective backbone has one profile sum and
the marked pair is at equality. Conditioning every rim edge present has
probability zero because it already contains the rim cycle, so it is outside
the conditioning claim.

It follows that coordinate conditioning preserves negative correlation.
Strictness is exactly \(abcd>0\) and at least two contracted blocks with
positive profile sum. Arbitrary-event conditioning is not claimed.

## 8. Four-core consequence

The forest-specific part of
forest_disjoint_rank_one_attachment_forest_backbone_proof.md is Section 1,
where a tree covariance supplies the apex factorization. Sections 2 and 3
are exact algebra for an arbitrary finite weighted backbone: they sum over
its acyclic edge configurations \(A\), contract each actual forest \(A\),
and apply the four-core transfer to the resulting component profile sums.
Edges outside \(A\) are absent and do not require the ambient backbone to
be a forest.

The weighted-cycle theorem supplies exactly the missing Section 1 input.
If \(r\) profiles are positive, then

\[
D(s)=D(0)\prod_{i=1}^r(1+s x_i),
\qquad x_i>0.
\]

Also

\[
\sum_i x_i=\frac{D'(0)}{D(0)}=\sum_j\beta_j,
\]

because a single apex spoke may be added to every backbone forest.
Therefore all logarithmic-derivative identities and the two nonnegative
Stieltjes expansions in Section 4 apply without change. In particular,

\[
UT_0-\Omega=\sum_{i\ne j}\alpha_i\tau_j,
\]

which is positive exactly when \(r\geq2\), and

\[
\frac{EF-AC}{D^2abcd}
=2(UT_0-\Omega)
 +(a+b)(c+d)(\Gamma^2+U^2T_0-2U\Omega)\geq0.
\]

Thus the four-core transfer contains no hidden forest-backbone assumption
after real-rootedness of the actual apex partition is supplied.

## 9. Independent exact checker

The standalone source and report are
forest_weighted_cycle_apex_disjoint_pair_k_independent.py and
forest_weighted_cycle_apex_disjoint_pair_k_independent_results.json.
They import no author helper.

For every apex case, three exact constructions are compared:

1. a literal connectivity-partition DP retaining all rim vertices and the
   apex;
2. direct enumeration of every selected spoke set and its cyclic gap
   factors; and
3. the polynomial \(2\times2\) transfer trace with the
   \(-2\Lambda\) correction.

The checker also verifies exactly that the polynomial determinant of the
monodromy is the constant
\(\delta=\prod_i\lambda_i(1+\lambda_i)\), and uses rational
Sturm sequences plus recursive polynomial gcds to count negative roots with
their full multiplicities.

Twenty-eight prescribed cases cover every \(2\leq n\leq8\) with four
families: all-positive nonuniform activities/profiles, one zero rim
activity, one zero profile, and the edgeless repeated-root boundary.
Another 120 seeded random rational cases cover \(2\leq n\leq8\) with
independent zero and positive parameters. All 148 cases have exactly their
degree many negative roots counting multiplicity, and all three polynomial
constructions agree coefficient by coefficient.

A second literal all-\(n+4\)-vertex DP checks the marked graph. Eight cases
include unequal parallel \(C_2\), nonuniform \(C_3,C_4,C_5\), a broken
cycle, zero profiles of ranks two and one, and a zero row factor. Its four
coefficients \(A,E,F,C\) agree exactly with an independently reconstructed
logarithmic-derivative/four-core formula. Six cases are strict and the two
rank/row boundary cases are exact equalities.

Finally, 106 positive-probability partial rim coordinate conditionings of
nonuniform \(C_3\) and \(C_4\) instances are tested literally. All 88
predicted strict cases and all 18 predicted equalities match exactly. No
counterexample was found.

These finite checks corroborate the proof; the transfer and
weighted-Hermitian argument establish the unbounded theorem.

## 10. Verdict and scope

Every proposed step checks out:

- the transfer trace needs and has the exact \(-2\Lambda\) correction;
- its positive-degree expansion is the literal cyclic-gap forest sum;
- the neighboring indices in the scalar recurrence are correct;
- the interior and wraparound entries are self-adjoint in the proposed
  weighted inner product exactly because \(|\rho|^2=\delta\);
- zero activities and zero profiles are covered by the forest case and
  real-rooted coefficient limits;
- arbitrary unequal parallel-edge \(C_2\) is valid;
- rim cylinder conditioning reduces to a smaller weighted cycle, \(C_2\),
  or a forest; and
- Sections 2--4 of the four-core proof transfer without an unspoken forest
  assumption.

The result remains restricted to a cycle backbone (including the parallel
\(C_2\) convention), a single common profile with four proportional spoke
rows, and exactly the two specified disjoint marked edges. It does not prove
apex real-rootedness for an arbitrary cyclic graph, nonproportional spokes,
negative association of a whole matching, strong Rayleigh, or the general
forest negative-correlation conjecture.
