# Negative association of all matching indicators over a rank-one weighted three-vertex core

2 October 2026. Complete candidate derivation, pending independent analytic
audit. Historical novelty is unverified. This is a separate proposed
strengthening of the already audited matching-pair theorem. It concerns
only the terminal matching indicators, not every forest edge.

## Theorem claimed by this candidate

Take a core on three vertices with arbitrary nonnegative edge activities.
Attach arbitrarily many terminals with spoke activities `a_j b_i`, where
the three column factors b_i are positive and the terminal row factors a_j
are nonnegative. Add any matching of terminal edges with arbitrary positive
activities. The vector of indicators of those matching edges is negatively
associated under the weighted forest measure: for any increasing real
functions f,g of disjoint sets of matching indicators,

\[
 \mathbb E[fg]\le\mathbb E[f]\mathbb E[g].            \tag{1}
\]

The same is true after conditioning any subset of matching indicators to
specified present/absent values, and under arbitrary positive external
fields on the matching indicators. The latter fields simply change their
activities. This theorem is not asserted for spoke or core indicators, nor
after conditioning arbitrary spoke or core edges.

## 1. A self-contained quadratic forced-subset lemma

Let a random subset Y of a finite index set have support of size at most
two. Give it unnormalized weights

\[
 w(\varnothing)=A>0,\quad
 w(\{i\})=h_i t_i,\quad
 w(\{i,j\})=K t_i t_j\quad(i\ne j),                 \tag{2}
\]

where K>0, t_i>=0 and h_i>0. Suppose

\[
 h_{\min}^2\ge KA,\qquad 2h_{\min}\ge h_{\max}.      \tag{3}
\]

**Lemma.** Y is negatively associated.

First prove negative correlation for the events that Y hits two disjoint
sets E,F. Write C for their complement, and put

\[
 s_H=\sum_{i\in H}t_i,\quad
 q_H=\sum_{\{i,j\}\subset H}t_it_j,\quad
 \beta_H=\frac{\sum_{i\in H}h_it_i}{s_H}
 \quad(H=E,F,C),                                    \tag{4}
\]

with any value for beta_H when s_H=0. If s_E or s_F is zero the joint
event has zero probability and the desired inequality is immediate.
Otherwise the hit-event weights and joint weight are

\[
 W_E=s_E\beta_E+Kq_E+Ks_E(s_F+s_C),\quad
 W_F=s_F\beta_F+Kq_F+Ks_F(s_E+s_C),\quad
 W_{EF}=Ks_Es_F.
\]

Let Z be the total weight in (2). Direct expansion, retaining the internal
pair terms, gives

\[
\begin{aligned}
 W_EW_F-W_{EF}Z={}&s_Es_F\bigl[
   \beta_E\beta_F-KA
   +Ks_C(\beta_E+\beta_F-\beta_C)
   +K^2(s_C^2-q_C)\bigr]\\
 &+Kq_Es_F(\beta_F+Ks_C)
  +Kq_Fs_E(\beta_E+Ks_C)+K^2q_Eq_F.                  \tag{5}
\end{aligned}
\]

Every term is nonnegative. The weighted averages beta_H lie between h_min
and h_max, so (3) handles the first two terms of the bracket; also
`s_C^2-q_C=sum_(i in C)t_i^2+q_C>=0`.

Now consider arbitrary increasing events on disjoint coordinate sets.
An event containing the empty coordinate configuration has probability
one and causes no difficulty. For any other increasing event, let E be
the coordinates whose singleton configurations trigger it. Since Y has
size at most two, a simultaneous occurrence of two nontrivial events on
disjoint coordinates must use one triggering singleton for each event.
Any event that requires a pair inside its own block cannot co-occur with
the other nontrivial event. Thus the joint probability is exactly the
joint hit probability for their two disjoint triggering sets, whereas
each marginal event probability is at least its corresponding hit
probability. Equation (5) therefore implies negative correlation for all
such increasing events. Expressing increasing functions on the finite
cube by their upper level-set indicators proves (1). This proves the lemma.

## 2. Exact matching marginal as forced independent Bernoullis

Use the notation of the separate pairwise theorem:

\[
 B=b_1+b_2+b_3,\quad J=b_1b_2b_3,\quad
 S=1+p+q+r+pq+pr+qr,
\]

\[
 L=b_1b_2+b_1b_3+b_2b_3
   +p\,b_3(b_1+b_2)+q\,b_2(b_1+b_3)+r\,b_1(b_2+b_3).
\]

Define

\[
 d(x)=1+Bx,\quad \alpha(x)=x^2/d(x),\quad
 \gamma(x)=x^3/d(x)^2,
\]

and, with all matching edges absent,

\[
 D_0=\prod_jd(a_j),\quad U_0=\sum_j\alpha(a_j),\quad
 \Gamma_0=\sum_j\gamma(a_j),\quad
 F_0=S+LU_0+J\Gamma_0+BJ U_0^2.                      \tag{6}
\]

The exact terminal transfer has commuting operators P,Q with

\[
 T(x)=d(x)e^{\alpha(x)P+\gamma(x)Q},\quad
 P^2=2BQ,\quad PQ=QP=Q^2=0,
\]

and the initial core row obeys `v1=S,vP1=L,vQ1=J`.
For each matching edge i between row activities a,b, put

\[
 c_i=\frac{d(a+b)}{d(a)d(b)},\quad
 \delta_i=\alpha(a+b)-\alpha(a)-\alpha(b),\quad
 \epsilon_i=\gamma(a+b)-\gamma(a)-\gamma(b).          \tag{7}
\]

Suppose initially that both row activities at every matched endpoint are
positive, so delta_i>0. Zero endpoints are treated at the end.
The ratio of the contracted to split normalized terminal transfer is
`exp(delta_i P+epsilon_i Q)`. If its matching activity is w_i, set

\[
 \theta_i=\frac{c_iw_i}{1+c_iw_i},\qquad
 t_i=\delta_i\theta_i,
\]

\[
 M=L+2BJ U_0,\qquad
 h_i=M+J\epsilon_i/\delta_i+BJ\delta_i,\qquad K=2BJ.
                                                               \tag{8}
\]

Expanding the product of the normalized group factors with the nilpotent
operators, including its second-order cross terms, gives the exact
matching-edge partition polynomial

\[
 Z(\mathbf w)=D_0\prod_i(1+c_iw_i)
 \left[F_0+\sum_i h_it_i+K\sum_{i<j}t_it_j\right].    \tag{9}
\]

In particular this formula sums over every matching edge, rather than
conditioning all but two.

Let independent Bernoulli indicators R_i have success probabilities
theta_i. Independently choose a forced subset Y by (2), with A=F_0 and
the parameters t_i,h_i,K in (8). Then the matching indicator vector has
exactly the law

\[
 X_i=1_{\{i\in Y\}}\vee R_i.                        \tag{10}
\]

To verify (10), let f(S) be the coefficient in the bracket of (9) attached
to the product of theta_i for i in S: f(empty)=F_0,
f({i})=h_i delta_i, f({i,j})=K delta_i delta_j. The forced law gives Y=S
weight `f(S) product_(i in S)theta_i`. Conditional on Y=S, an outcome x
of (10) has probability `P(R=x)1_(S subset x)/product_(i in S)theta_i`.
Multiplication and summation over S therefore give
`P(R=x) sum_(S subset x) f(S)` divided by the bracket's normalization.
The coefficient expansion of the right side of (9) gives exactly the same
matching configuration weight. Thus (10) is an identity of finite measures.

## 3. Verification of the lemma's two bounds

The scalar functions alpha(x)/x and gamma(x)/x are strictly increasing
for x>0, so delta_i,epsilon_i>0. Furthermore

\[
 0<\delta_i<1/B^2,\qquad
 0<\epsilon_i/\delta_i<2/B.                          \tag{11}
\]

For the first bound use

\[
 \delta_i=\frac1{B^2}
   \left[1+\frac1{d(a+b)}-\frac1{d(a)}-\frac1{d(b)}\right]
 <1/B^2.
\]

For the second, the function

\[
 H(x)=(2/B)\alpha(x)-\gamma(x)
\]

satisfies

\[
 H(x)/x=B^{-2}[1-d(x)^{-2}],
\]

strictly increasing for x>0. Its strict superadditivity gives
`(2/B)delta_i-epsilon_i>0`. Hence

\[
 M<h_i<M+3J/B.                                      \tag{12}
\]

The weighted core certificate gives

\[
 L^2-2BJ S>0,
\]

by the positive primitive-variable expansion in the separate pair proof.
Also `B L>=B(b1b2+b1b3+b2b3)>=9J` by AMGM. Since M>=L, (12) implies
`h_max<2M<2h_min`.

For the other condition, gamma(x)<=alpha(x)/B gives Gamma_0<=U_0/B.
Direct expansion yields

\[
\begin{aligned}
 M^2-KF_0
 &=L^2-2BJ S+2BJ L U_0+2B^2J^2U_0^2-2BJ^2\Gamma_0\\
 &\ge L^2-2BJ S+2J(BL-J)U_0+2B^2J^2U_0^2>0.         \tag{13}
\end{aligned}
\]

Thus `h_min^2>M^2>K F_0`. Both hypotheses (3) hold, so the forced subset
Y is negatively associated.

## 4. Passing negative association to the matching indicators

For increasing f,g on disjoint coordinate sets, condition on Y in (10).
The Bernoulli coordinates in the two sets are independent. Thus the
conditional product expectation is `F(Y_E)G(Y_F)`, where F and G are the
Bernoulli-averaged versions of f and g. Coupling the same Bernoullis shows
that F,G are increasing in their respective Y coordinates. Negative
association of Y gives `E[F G]<=E[F]E[G]`, proving (1) for X without any
appeal to an unproved preservation theorem.

If a matching endpoint has zero row activity, its matching edge is a
bridge incident to a vertex with no other edge, or is an isolated
two-vertex component when both endpoints vanish. That indicator is an
independent Bernoulli and can be separated from the remaining forest
measure. The argument above applies to the rest; independence and the
same conditional-expectation argument preserve negative association.

Finally, conditioning matching edges present contracts their disjoint
terminal pairs and sums the two row factors. Conditioning them absent
deletes those edges. The remaining graph retains rank-one spokes, the
same three-vertex core, and a matching among the remaining uncontracted
terminals. The theorem therefore applies again. Arbitrary positive fields
on the matching indicators alter only w_i and were already permitted.

## Status and scope boundary

This derivation requires a separate independent analytic audit before the
negative-association extension is reported as completed. It does not assert
the strong Rayleigh property or a real-stable matching polynomial, and it
does not establish negative association for all forest edges. The full
forest negative-association and all-fugacity pair conjectures on arbitrary
graphs remain unresolved by this argument.
