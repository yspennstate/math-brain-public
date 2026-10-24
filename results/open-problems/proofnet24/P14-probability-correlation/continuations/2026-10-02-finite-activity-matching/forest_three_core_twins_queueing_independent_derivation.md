# Independent finite-activity derivation: arbitrary terminal count over a weighted three-vertex core

2 October 2026. This derivation was obtained independently of the child
researcher's expanded positive certificate and supplies a simpler equivalent
formula. It establishes one marked pair type on an unbounded graph family;
it does not establish the full forest conjecture.

## Statement and exact marked-pair scope

Take three core vertices with respective core edge activities p,q,r>=0.
Attach m>=4 distinct terminals, each joined to each core vertex with the
same spoke activity a>0. Among four of these terminals add two disjoint
matching edges e,f, with arbitrary positive activities z_e,z_f. There are
no other edges between terminals. Missing core edges are allowed by zero
activities; core parallel edges may be aggregated by summing their activities.

The forest Rayleigh difference for **these two added matching edges** is

\[
 \boxed{R_{ef}=4a^4(1+3a)^{2m-8}G,}                   \tag{1}
\]

where, with X=p+q+r and t=pq+pr+qr,

\[
 \begin{aligned}
 G={}&(1+3a)^2\bigl[3+6X+4X^2-6t\bigr]\
 &+6a(1+3a)(1+ma)(3+2X)\
 &+9a^2+30ma^3+18m^2a^4.                            \tag{2}
 \end{aligned}
\]

Since `4X^2-6t=4(p^2+q^2+r^2)+2(pq+pr+qr)`, every term in (2) is
nonnegative and its constant contribution is positive. Thus R_ef>0 for
every stated parameter choice. The two marked indicators have strictly
negative covariance. The expression is independent of z_e,z_f, as required
by multiaffinity of any Rayleigh difference.

This statement does not include a spoke/spoke, spoke/core, core/core, or
matching/spoke pair, nor an arbitrary four-vertex or larger core. Those
extensions require separate proofs.

## 1. Exact deletion/contraction coefficients

Write

\[
 Z=A+(z_e+z_f)B+z_ez_f C.
\]

Terminal permutation symmetry makes the two single-mark coefficients equal.
Contracting one marked edge merges its two terminals. Its two parallel
spokes to each core vertex combine into one activity 2a: selecting both
parallel spokes would create a cycle and is forbidden, so summing their
single-edge alternatives is exact. Contracting both marks produces two
such 2a terminals. Consequently A is the forest partition with m ordinary
terminals, B has one 2a terminal and m-2 ordinary terminals, and C has two
2a terminals and m-4 ordinary terminals. No additional multiplicity or
activity factor occurs in these derivative coefficients.

Direct differentiation cancels every marked activity and gives

\[
 R_{ef}=B^2-AC.                                      \tag{3}
\]

## 2. Five-state core connectivity transfer

The state is a partition of the three core vertices. A new terminal chooses
a subset of the three spokes. It preserves acyclicity exactly when it meets
each existing core block at most once, then merges the met blocks. A terminal
with common spoke activity w therefore has transfer

\[
 T(w)=(1+3w)I+w^2P+w^3Q.                            \tag{4}
\]

Here P chooses and merges two distinct core blocks by a pair of distinct
core vertices; Q merges all three singleton blocks by choosing all three
spokes. In the five-state partition space,

\[
 P^2=6Q,\qquad PQ=QP=Q^2=0.                         \tag{5}
\]

Indeed from the singleton state there are three first pair choices and
two second choices connecting the remaining block, hence six; from a
two-block state two applications of P are impossible. Q already lands in
the one-block state. These identities also show that T(a) and T(2a)
commute; no unsupported commutation assumption is needed.

Let v be the initial row of core forest weights and 1 the all-ones column.
The core triangle's acyclic subsets give

\[
 v1=S:=1+X+t,\qquad vP1=L:=3+2X,\qquad vQ1=1.       \tag{6}
\]

The empty core forest supplies three P choices; each one-edge core forest
supplies two; the core trees supply none. Only the empty core forest
permits Q. Thus

\[
 A=vT(a)^m1,\quad
 B=vT(2a)T(a)^{m-2}1,\quad
 C=vT(2a)^2T(a)^{m-4}1.                             \tag{7}
\]

This transfer is a complete enumeration of all acyclic edge subsets for
every m, rather than a truncation or numerical check.

## 3. Normalized coefficients and the cancellation

Put

\[
 d=1+3a,\quad d_2=1+6a,\quad
 \alpha=a^2/d,\quad\beta=a^3/d,\quad
 \alpha_2=4a^2/d_2,\quad\beta_2=8a^3/d_2.
\]

By (5), for every integer k>=0,

\[
 T(a)^k=d^k\{I+k\alpha P+
            [k\beta+3k(k-1)\alpha^2]Q\}.             \tag{8}
\]

Define normalized coefficients by
`A=d^m Abar`, `B=d_2 d^(m-2) Bbar`,
`C=d_2^2 d^(m-4) Cbar`. Equations (6)--(8) give

\[
 \overline A=S+m\alpha L+m\beta+3m(m-1)\alpha^2,
\]

\[
 \begin{aligned}
 \overline B={}&S+[(m-2)\alpha+\alpha_2]L\
 &+(m-2)\beta+\beta_2
   +3(m-2)(m-3)\alpha^2+6(m-2)\alpha\alpha_2,
 \end{aligned}
\]

\[
 \begin{aligned}
 \overline C={}&S+[(m-4)\alpha+2\alpha_2]L\
 &+(m-4)\beta+2\beta_2+3(m-4)(m-5)\alpha^2\
 &+6\alpha_2^2+12(m-4)\alpha\alpha_2.
 \end{aligned}                                      \tag{9}
\]

The coefficient (m-4)(m-5) is zero at m=4 or5 and nonnegative thereafter;
there is no negative-power transfer at either endpoint.

Set

\[
 \delta=\alpha_2-2\alpha=\frac{2a^2}{dd_2},\qquad
 \kappa=\frac{6a^3(1+2ma)}{d^2d_2}.
\]

Direct cancellation in (9) gives exactly

\[
 \overline B=\overline A+\delta L+\kappa,
 \qquad
 \overline C=\overline A+2\delta L+2\kappa+6\delta^2.
                                                               \tag{10}
\]

Thus the troublesome deletion/contraction cross term is retained and
cancels in a controlled way:

\[
 \overline B^2-\overline A\overline C
 =\delta^2\left[(L+\kappa/\delta)^2-6\overline A\right].         \tag{11}
\]

Here `kappa/delta=3a/d+6m a^2/d`. Expanding the bracket in (11), multiplying
by d^2, and collecting the terms linear and quadratic in m yields

\[
 d^2\left[(L+\kappa/\delta)^2-6\overline A\right]
 =d^2(L^2-6S)+6ad(1+ma)L+9a^2+30ma^3+18m^2a^4.
                                                               \tag{12}
\]

Finally `L^2-6S=3+6X+4X^2-6t`. Restoring the positive normalization
`d_2^2 d^(2m-4)` in (3) proves (1)--(2). Every factor and cancellation
holds at arbitrary finite a,p,q,r, not only in a fugacity expansion.

## 4. Equivalence with the child's positive certificate

Writing n=m-4, the child independently obtained the equivalent expression

\[
 \begin{aligned}
 G={}&d^2[3+6X+4X^2-6t+18a+12aX+9a^2]\
 &+6(n+1)a^2d(3+2X)+(30n+66)a^3\
 &+(18n^2+144n+207)a^4.
 \end{aligned}                                      \tag{13}
\]

To check equivalence explicitly, the additional terms in the first line
are `6ad^2L+9a^2d^2`. Using d-1=3a, their combination with the second
line's L term gives `6adL+6(n+4)a^2dL`. Expanding `9a^2d^2` raises the
remaining cubic coefficient to `30n+120` and the quartic coefficient to
`18n^2+144n+288`, exactly `30ma^3+18m^2a^4` in (2). Hence the two formulas
are identical, not merely equal at sampled parameter choices.

## Status

The complete derivation above proves the stated matching-pair theorem on
this unbounded family. A separate agent is being asked for adversarial
analytic audit before presenting it as a completed campaign result. The
source and novelty boundary remains unresolved: series-parallel and two-sum
I-Rayleigh closure are prior results, and complete K7 SOS was reported in
Erickson's primary 2011 manuscript. Those facts subsume small special cases
but do not, by themselves, establish this entire unbounded weighted-core
family. No historical novelty claim is made here.
