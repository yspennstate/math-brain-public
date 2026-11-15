# A finite-window estimate for the conditional law

Fix an integer m >= 2. Let X_n follow the recursion in the question, and write

\[
 p_n(k)=\mathbb P(X_n=k)\quad(k\geq1),\qquad
 q_n=\sum_{k\geq1}p_n(k),\qquad
 g(k)=(m-1)m^{-k}.
\]

The sequence p_n is a subprobability measure on the positive integers. For a
signed sequence v, put ||v||_1 = sum_{k>=1}|v(k)|. Total variation between
probability measures is half their l1 distance. Define the right shift T by
(Tv)(1)=0 and (Tv)(k)=v(k-1) for k>=2, and let delta_1 denote unit mass at 1.

## Theorem 1 (finite-window bound)

For every n with q_n>0 and integer L>=1,

\[
\begin{split}
d_{\rm TV}\bigl(\mathcal L(X_n\mid X_n>0),g\bigr)
\leq\frac1{q_n}\bigg[&
 \sum_{j=1}^{L-1}m^{-j}|q_{n+j}-q_n|
 +m^{-L}\max\{q_{n+L},q_n\}\\
 &+(m-1)\sum_{j=0}^{L-1}m^{-j}q_{n+j}^{\,2}\bigg].                 \tag{1}
\end{split}
\]

In particular, if

\[
 \delta_{n,L}=\max_{0\leq j\leq L}|q_{n+j}/q_n-1|,
\]

then

\[
 d_{\rm TV}\leq
 \frac{\delta_{n,L}}{m-1}
 +(1+\delta_{n,L})m^{-L}
 +m(1+\delta_{n,L})^2q_n.                                  \tag{2}
\]

No criticality or moment assumption is needed for these bounds.

### Proof

Separate the recursion according to the number of positive inputs. For k>=1,
let r_n(k) be the probability that at least two inputs are positive and their
sum is k+1. Independence gives

\[
 p_{n+1}(k)=m(1-q_n)^{m-1}p_n(k+1)+r_n(k).                 \tag{3}
\]

All entries of r_n are nonnegative. Since two positive integer inputs have
sum at least 2, its mass is exactly

\[
 R_n=1-(1-q_n)^m-mq_n(1-q_n)^{m-1}.
\]

A union bound over pairs of inputs yields

\[
 R_n\leq {m\choose2}q_n^2.                                \tag{4}
\]

Put

\[
 b_n(k)=m\{1-(1-q_n)^{m-1}\}p_n(k+1),\qquad e_n=r_n-b_n.
\]

Thus (3) also reads p_{n+1}(k)=mp_n(k+1)+e_n(k). The mass B_n of b_n satisfies

\[
 B_n=m\{1-(1-q_n)^{m-1}\}\{q_n-p_n(1)\}
 \leq m(m-1)q_n^2,                                      \tag{5}
\]

by 1-(1-q)^{m-1} <= (m-1)q. Let s_n=sum_k e_n(k)=R_n-B_n and set

\[
 d_n=\frac{s_n\delta_1-Te_n}{m}.
\]

Then sum_k d_n(k)=0. Because T e_n has zero entry at 1,

\[
\begin{split}
 \frac12\|d_n\|_1
 &=\frac{|R_n-B_n|+\|r_n-b_n\|_1}{2m}\\
 &\leq\frac{|R_n-B_n|+R_n+B_n}{2m}
 =\frac{\max\{R_n,B_n\}}m
 \leq(m-1)q_n^2.                                      \tag{6}
\end{split}
\]

Summing p_{n+1}(k)=mp_n(k+1)+e_n(k) gives
p_n(1)=q_n-q_{n+1}/m+s_n/m. Substituting this at the first coordinate and
using the same identity at every other coordinate proves the exact equality

\[
 p_n=(q_n-q_{n+1}/m)\delta_1+m^{-1}Tp_{n+1}+d_n.          \tag{7}
\]

Iterating it L times gives

\[
 p_n=\sum_{j=0}^{L-1}m^{-j}(q_{n+j}-q_{n+j+1}/m)\delta_{j+1}
      +m^{-L}T^Lp_{n+L}
      +\sum_{j=0}^{L-1}m^{-j}T^jd_{n+j}.                 \tag{8}
\]

Here delta_k is unit mass at k. Independently, the geometric measure satisfies

\[
 q_ng=\sum_{j=0}^{L-1}m^{-j}q_n(1-1/m)\delta_{j+1}
            +m^{-L}T^L(q_ng).                           \tag{9}
\]

Write Delta_j=q_{n+j}-q_n, so Delta_0=0. Subtract (9) from (8). The l1 norm
of the difference of the displayed finite sums is at most

\[
 \sum_{j=0}^{L-1}m^{-j}|\Delta_j-\Delta_{j+1}/m|
 \leq2\sum_{j=1}^{L-1}m^{-j}|\Delta_j|+m^{-L}|\Delta_L|.  \tag{10}
\]

The two boundary measures in (8) and (9) have combined mass
m^{-L}(q_{n+L}+q_n). The last sum in (8) has l1 norm at most
2(m-1)sum_{j=0}^{L-1}m^{-j}q_{n+j}^2 by (6). Divide the resulting bound
by 2q_n and use

\[
 (|q_{n+L}-q_n|+q_{n+L}+q_n)/2=\max\{q_{n+L},q_n\}
\]

to obtain (1). The estimates sum_{j>=1}m^{-j}=1/(m-1) and
sum_{j>=0}m^{-j}=m/(m-1) give (2). This proves the theorem.

## Corollary 2 (a scalar equivalent of conditional geometric convergence)

Suppose q_n>0 eventually and q_n tends to zero. The following are equivalent:

- q_{n+1}/q_n tends to 1;
- the conditional laws converge to g in total variation;
- P(X_n=1 | X_n>0) tends to (m-1)/m.

### Proof

If the ratios tend to 1, then for each fixed L their product shows
delta_{n,L}->0. Taking the limsup as n tends to infinity in (2) gives a
bound m^{-L}. Let L tend to infinity.

Total-variation convergence implies convergence of the mass at 1. Conversely,
the summed version of (3), or the equality before (7), gives

\[
 \frac{q_{n+1}}{q_n}
 =m\left\{1-\mathbb P(X_n=1\mid X_n>0)\right\}+\frac{s_n}{q_n}.
\]

Since |s_n|=|R_n-B_n|<=m(m-1)q_n^2 by (4)-(5), convergence of the mass at 1
to (m-1)/m forces the ratios to tend to 1. This proves all equivalences.

In particular the sufficient ratio condition applies whenever q_n is
asymptotic to A n^{-beta}, with
A>0 and beta>0. It does not deduce ratio convergence from an exponent-only
statement such as q_n=n^{-2+o(1)}.

## Theorem 3 (first-order correction, conditional on local smoothness)

Suppose q_n>0 eventually and, for a constant beta>0,

\[
 q_n=o(n^{-1}),\qquad
 \frac{q_{n+1}}{q_n}=1-\frac{\beta}{n}+o(n^{-1}).          \tag{11}
\]

Define the summable signed sequence

\[
 h_\beta(k)=\beta m^{-k}\{m-(m-1)k\},\qquad k\geq1.
\]

Then

\[
 \sum_{k\geq1}\left|
 n\left\{\mathbb P(X_n=k\mid X_n>0)-g(k)\right\}
             -h_\beta(k)\right|\longrightarrow0.         \tag{12}
\]

Consequently,

\[
 d_{\rm TV}\bigl(\mathcal L(X_n\mid X_n>0),g\bigr)
       \sim\frac{\beta}{mn}.                            \tag{13}
\]

For the exponent beta=2 predicted in the question, (13) is 2/(mn). Hypothesis
(11) is an additional assumption; q_n asymptotic to A n^{-2} alone does not
justify its ratio expansion.

### Proof

Because beta>0, (11) implies that q_n is eventually decreasing. There exist
N and C>0 such that, for every t>=N,

\[
 0\leq1-q_{t+1}/q_t\leq C/t.
\]

Enlarge N so C/N<=1. For n>=N and j>=0, the elementary inequality
1-product_i(1-a_i)<=sum_i a_i for a_i in [0,1] gives

\[
 0\leq1-q_{n+j}/q_n\leq Cj/n.                           \tag{14}
\]

For every fixed j, taking the product of the j expansions in (11) yields

\[
 n(q_{n+j}/q_n-1)\longrightarrow-\beta j.                \tag{15}
\]

For fixed n, let L tend to infinity in (8). Its boundary term has l1 norm
at most m^{-L}, and all sums converge absolutely, since q_t<=1 and (6)
bounds ||d_t||_1. Hence

\[
 p_n=\sum_{j\geq0}m^{-j}(q_{n+j}-q_{n+j+1}/m)\delta_{j+1}+D_n,
 \quad D_n=\sum_{j\geq0}m^{-j}T^jd_{n+j}.                 \tag{16}
\]

Eventual monotonicity and (6) imply

\[
 \|D_n\|_1\leq2(m-1)q_n^2\sum_{j\geq0}m^{-j}
             =2m q_n^2.                                \tag{17}
\]

The sequence in (16) at coordinate k, after division by q_n, is

\[
 v_n(k)=m^{-(k-1)}\left\{\frac{q_{n+k-1}}{q_n}
                          -\frac{q_{n+k}}{mq_n}\right\}.
\]

Equation (15) shows that n(v_n(k)-g(k)) tends to h_beta(k) for every k.
Moreover (14) gives the summable bound

\[
 n|v_n(k)-g(k)|
 \leq C m^{-(k-1)}\{k-1+k/m\}.                          \tag{18}
\]

Dominated convergence for the counting measure, and (17) together with
n q_n->0, prove (12).

Finally, with r=1/m, the identities sum_{k>=1}r^k=r/(1-r) and
sum_{k>=1}kr^k=r/(1-r)^2 give sum_k h_beta(k)=0. Its first entry is beta/m.
For k>=2 it is nonpositive: m-(m-1)k<=2-m<=0. Thus its total positive
mass is beta/m and ||h_beta||_1=2beta/m. Taking norms in (12) proves (13).

## The deterministic exception in the supplied statement

If X_0=c almost surely, with c a nonnegative integer, the critical equality
reduces to (m-1)c=1. Its only solution is m=2, c=1. In that case induction
in the recursion gives X_n=1 almost surely for every n. Thus q_n=1,
E[X_n]=1 and the conditional law is delta_1, contradicting all three
predictions as literally stated. Its distance to g for m=2 is 1/2.

More generally, if a critical initial law has no mass at zero, then
((m-1)X_0-1)m^{X_0} is nonnegative. For m>=3 it is strictly positive,
which is impossible since its expectation is zero. For m=2, it is zero
only at X_0=1, so X_0=1 almost surely. This proves that the displayed
exception is the only critical initial law with no atom at zero.

The nonconstant assumption appears at the start of the original paper and
is omitted in the supplied statement. This observation does not settle
the intended nonconstant critical conjecture.

## Relation to the literature

Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits and Zhan Shi,
*A max-type recursive model: some properties and open questions*,
[arXiv:1705.04787v2](https://arxiv.org/pdf/1705.04787), Section 6, discuss
the qualitative link between survival asymptotics and geometric conditional
limits. The results above give an explicit finite-window total-variation
estimate and a first-order correction under the stated extra hypothesis.
They do not establish the critical survival constant or the local smoothness
in (11). No priority claim for these estimates is made.
