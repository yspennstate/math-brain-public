# C0130 — exact three-cookie stationary balance, cancellation family, and rational difference equation

Target: `C0130`, Kosygina–Zerner Problem 3.12 (escape probability for a transient one-dimensional excited random walk).

Status of this artifact: **PARTIAL**. It gives a complete theorem for the three-cookie backward-chain reduction and exact formulas on a nontrivial cancellation subfamily, but it does not compute the escape probability for every three-cookie law and therefore does not settle the source problem.

## 1. Setup and cumulative dependency

Assume an i.i.d. bounded cookie environment on `Z` in which a site carries the random stack

\[
(p_1,p_2,p_3,1/2,1/2,\ldots), \qquad 0<p_j<1,
\]

and different sites have i.i.d. copies of the triple `(p_1,p_2,p_3)`. Put

\[
\delta=\mathbb E\big[(2p_1-1)+(2p_2-1)+(2p_3-1)\big].
\]

Throughout this artifact we work in the right-transient regime `delta>1`.

For a fresh site, let `F_m` be the number of failures before the `m`-th success in the Bernoulli sequence with success probabilities `p_1,p_2,p_3,1/2,1/2,...`, annealed over the site stack. The standard backward branching chain is

\[
Z_{n+1}=F_{Z_n+1}.
\]

In the right-transient regime this chain has a stationary law `pi=(pi_i)_{i>=0}`. The preceding R7-05 artifact established the exact identity

\[
\boxed{p_{\rm esc}=\mathbb E[p_1]\,\pi_0.}
\]

The present artifact derives new exact information about `pi_0` in the first unsolved finite-depth case `M=3`.

## 2. The exact three-cookie stationary PGF equation

Let

\[
G(s)=\sum_{i\ge0}\pi_i s^i,\qquad 0\le s<1.
\]

Let `Y_j` be the success indicator of the `j`-th cookie toss at a fresh site and put

\[
K=Y_1+Y_2+Y_3,\qquad a_k=\mathbb P(K=k),\quad k=0,1,2,3.
\]

For every `i>=2`, the target number `i+1` of successes is at least three. After the first three trials, if `K=k`, there have been `3-k` failures and `i+1-k` further successes are needed from fair Bernoulli trials. Therefore

\[
\mathbb E[s^{F_{i+1}}]
=
\sum_{k=0}^3 a_k s^{3-k}(2-s)^{-(i+1-k)}.
\]

Define

\[
T(s)=\frac1{2-s},
\qquad
Q(s)=\sum_{k=0}^3 a_k s^{3-k}(2-s)^k,
\qquad
A(s)=Q(s)T(s).
\]

Then for `i>=2`,

\[
\mathbb E[s^{F_{i+1}}]=Q(s)T(s)^{i+1}.
\]

Let

\[
P_0(s)=\mathbb E[s^{F_1}],\qquad P_1(s)=\mathbb E[s^{F_2}].
\]

Stationarity gives the exact functional equation

\[
\boxed{
G(s)=A(s)G(T(s))
+\pi_0\big(P_0(s)-A(s)\big)
+\pi_1\big(P_1(s)-A(s)T(s)\big).
}
\tag{2.1}
\]

This is the first place where depth three differs structurally from depth two: there are two exceptional stationary masses, `pi_0` and `pi_1`.

## 3. A finite-mean-free Abelian lemma

The stationary mean of `Z` need not be finite when `1<delta<=2`, so taking expectation of the linear drift is not justified. The PGF equation avoids that problem.

Write

\[
x=1-s,\qquad t=T(s)=\frac1{1+x}.
\]

Then

\[
t-s=\frac{x^2}{1+x},\qquad 1-t=\frac{x}{1+x}.
\]

For every integer `i>=1`,

\[
0\le t^i-s^i\le i t^{i-1}(t-s).
\]

Also

\[
i t^{i-1}\le 1+t+\cdots+t^{i-1}\le\frac1{1-t}.
\]

Hence

\[
0\le \frac{t^i-s^i}{x}
\le
\frac{t-s}{x(1-t)}=1.
\]

For each fixed `i`, the left side tends to zero as `s\uparrow1`. Dominated convergence under the probability mass function `pi` therefore yields

\[
\boxed{
\frac{G(T(s))-G(s)}{1-s}\longrightarrow0
\quad(s\uparrow1).
}
\tag{3.1}
\]

No moment assumption on `pi` is used.

## 4. Exact stationary drift-balance identity

Let

\[
m_0=\mathbb E[F_1],\qquad m_1=\mathbb E[F_2].
\]

These are finite because after the first three cookies the sequence is fair. Since

\[
P_0(s)=1-m_0(1-s)+o(1-s),
\qquad
P_1(s)=1-m_1(1-s)+o(1-s),
\]

it remains to expand `A`.

With `x=1-s`,

\[
Q(1-x)
=
\mathbb E\big[(1-x)^{3-K}(1+x)^K\big]
=
1+\delta x+O(x^2),
\]

because the coefficient of `x` in the term with `K=k` is `2k-3`. Therefore

\[
A(1-x)=\frac{Q(1-x)}{1+x}
=1+(\delta-1)x+O(x^2).
\]

Consequently

\[
P_0(s)-A(s)
=-(m_0+\delta-1)(1-s)+o(1-s),
\]

and, since `T(s)=1-(1-s)+O((1-s)^2)`,

\[
P_1(s)-A(s)T(s)
=-(m_1+\delta-2)(1-s)+o(1-s).
\]

On the left side of (2.1), using (3.1) and `G(T(s))->1`,

\[
\frac{G(s)-A(s)G(T(s))}{1-s}
\longrightarrow-(\delta-1).
\]

Dividing (2.1) by `1-s` and taking `s\uparrow1` proves the exact identity

\[
\boxed{
\pi_0 c_0+\pi_1 c_1=\delta-1,
}
\tag{4.1}
\]

where

\[
c_0=m_0+\delta-1,
\qquad
c_1=m_1+\delta-2.
\]

This proof is valid throughout the full right-transient range `delta>1`; it does not assume finite stationary mean.

## 5. Closed cookie-level formulas for `c_0,c_1`

Condition on a fixed triple `(p_1,p_2,p_3)` and write `q_j=1-p_j`.

For one required success,

\[
m_0
=
q_1p_2+2q_1q_2p_3+4q_1q_2q_3.
\]

For two required successes,

\[
\begin{aligned}
m_1={}&p_1q_2p_3+q_1p_2p_3\\
&+3\big(p_1q_2q_3+q_1p_2q_3+q_1q_2p_3\big)
+5q_1q_2q_3.
\end{aligned}
\]

Adding the drift terms and simplifying gives the pointwise polynomial identities

\[
\boxed{
c_1=p_1p_2(2p_3-1),
}
\tag{5.1}
\]

and

\[
\boxed{
c_0
=p_1(2p_2-1)
+(2p_3-1)(p_1+p_2-p_1p_2).
}
\tag{5.2}
\]

For a random site stack, take expectations of the right sides. Thus the exact annealed coefficients are

\[
\boxed{
C_1=\mathbb E[p_1p_2(2p_3-1)],
}
\]

\[
\boxed{
C_0=
\mathbb E\!\left[
 p_1(2p_2-1)
 +(2p_3-1)(p_1+p_2-p_1p_2)
\right],
}
\]

and (4.1) reads

\[
\boxed{C_0\pi_0+C_1\pi_1=\delta-1.}
\tag{5.3}
\]

## 6. An exact nontrivial three-cookie cancellation family

If

\[
\boxed{C_1=\mathbb E[p_1p_2(2p_3-1)]=0,}
\tag{6.1}
\]

then (5.3) immediately determines the stationary atom:

\[
\boxed{
\pi_0=\frac{\delta-1}{C_0}.
}
\tag{6.2}
\]

Combining with the already-proved escape identity gives

\[
\boxed{
 p_{\rm esc}
 =
 \mathbb E[p_1]\,
 \frac{\delta-1}{
 \mathbb E[\,p_1(2p_2-1)+(2p_3-1)(p_1+p_2-p_1p_2)\,]
 }.
}
\tag{6.3}
\]

This family is strictly larger than the depth-two case because (6.1) can hold by annealed cancellation even when the third cookie is nonneutral almost surely.

### Exact rational example

Let the site stack be equally likely to be

\[
\left(\frac9{10},\frac9{10},\frac7{10}\right)
\quad\text{or}\quad
\left(\frac9{10},\frac9{10},\frac3{10}\right).
\]

Then

\[
\delta=\frac85,
\qquad
C_1=0,
\qquad
C_0=\frac{18}{25},
\qquad
\mathbb E[p_1]=\frac9{10}.
\]

Hence

\[
\boxed{\pi_0=\frac56,
\qquad
p_{\rm esc}=\frac34.}
\]

The third cookie is genuinely random and is never neutral in either stack type.

## 7. Extremal bounds for nonnegative three-cookie stacks

Assume now that all three cookies are nonnegative in the usual sense:

\[
p_1,p_2,p_3\ge\frac12\quad\text{a.s.}
\]

Then

\[
C_1\ge0.
\]

Moreover, pointwise,

\[
\begin{aligned}
c_0-c_1
&=p_1(2p_2-1)
 +(2p_3-1)(p_1+p_2-2p_1p_2)\\
&=p_1(2p_2-1)
 +(2p_3-1)\big(p_1(1-p_2)+p_2(1-p_1)\big)
\ge0.
\end{aligned}
\]

Thus `C_0>=C_1>=0`. Since `pi_0,pi_1>=0` and `pi_0+pi_1<=1`, (5.3) implies

\[
\boxed{
\pi_0\le\frac{\delta-1}{C_0}.
}
\tag{7.1}
\]

If `C_0>C_1`, it also implies

\[
\boxed{
\pi_0
\ge
\max\left\{0,\frac{\delta-1-C_1}{C_0-C_1}\right\}.
}
\tag{7.2}
\]

Multiplying by `E[p_1]` gives corresponding exact bounds on `p_esc`.

These bounds are extremal with respect to the reduced information `(5.3), pi_0>=0, pi_1>=0, pi_0+pi_1<=1`: every value of `pi_0` in the displayed interval can be paired with

\[
\pi_1=\frac{\delta-1-C_0\pi_0}{C_1}
\]

when `C_1>0`, with the remaining abstract mass placed outside `{0,1}`. This is a statement about the reduced constraint system only, not a claim that every endpoint is realized by an excited-random-walk stationary law.

For the deterministic stack

\[
p_1=p_2=p_3=\frac45,
\]

one has

\[
\delta=\frac95,
\quad C_0=\frac{132}{125},
\quad C_1=\frac{48}{125},
\]

and therefore

\[
\frac{13}{21}\le\pi_0\le\frac{25}{33},
\]

or equivalently

\[
\boxed{
\frac{52}{105}\le p_{\rm esc}\le\frac{20}{33}.
}
\]

## 8. Translation to a rational first-order difference equation

The remaining obstruction can be seen exactly by changing coordinates.

Put

\[
u=\frac1{1-s},
\qquad
s=1-\frac1u,
\qquad
g(u)=G\!\left(1-\frac1u\right).
\]

The Möbius map `T(s)=1/(2-s)` becomes the unit shift

\[
T\!\left(1-\frac1u\right)=1-\frac1{u+1}.
\]

Define the monic cubic

\[
R(u)=\sum_{k=0}^3 a_k (u-1)^{3-k}(u+1)^k.
\]

Then

\[
A\!\left(1-\frac1u\right)
=\frac{R(u)}{u^2(u+1)}.
\]

Hence (2.1) is a first-order rational difference equation

\[
g(u+1)
=
\frac{u^2(u+1)}{R(u)}\,g(u)
+\pi_0 d_0(u)+\pi_1 d_1(u),
\tag{8.1}
\]

where `d_0,d_1` are explicit rational functions obtained from `P_0,P_1`.

The coefficient of `u^2` in `R` is `delta`. If

\[
R(u)=\prod_{j=1}^3(u-r_j),
\]

then

\[
\sum_{j=1}^3r_j=-\delta.
\]

The homogeneous equation corresponding to (8.1),

\[
h(u+1)=\frac{u^2(u+1)}{R(u)}h(u),
\]

has the explicit meromorphic solution

\[
\boxed{
H(u)=
\frac{\Gamma(u)^2\Gamma(u+1)}
{\Gamma(u-r_1)\Gamma(u-r_2)\Gamma(u-r_3)}.
}
\tag{8.2}
\]

Indeed, the gamma recurrence gives

\[
\frac{H(u+1)}{H(u)}
=
\frac{u^2(u+1)}{\prod_j(u-r_j)}.
\]

Stirling's ratio formula and `sum r_j=-delta` give

\[
\boxed{H(u)\asymp u^{1-\delta}.}
\tag{8.3}
\]

Thus in the transient regime `delta>1` this nonzero homogeneous mode decays at infinity. More generally, `H(u)P(u)` is homogeneous for any 1-periodic meromorphic `P`.

This explains the exact gluing failure of the naive depth-three PGF route: the boundary condition

\[
g(u)\longrightarrow1\qquad(u\to\infty)
\]

does not kill the decaying homogeneous mode. At depth two the only exceptional mass is `pi_0`, and the first-order Abelian identity already determines it; at depth three the additional mass `pi_1` couples to a genuine decaying degree of freedom.

This is an obstruction to this particular local/PGF closure route, not an impossibility theorem for an exact three-cookie formula.

## 9. What this does and does not prove

Proved here:

1. the exact three-cookie stationary PGF equation (2.1);
2. the finite-mean-free balance identity `C_0 pi_0 + C_1 pi_1 = delta-1` throughout `delta>1`;
3. explicit cookie-level formulas for `C_0,C_1`;
4. an exact escape-probability formula on the nontrivial cancellation family `C_1=0`, including the rational example with `p_esc=3/4`;
5. exact positive-cookie upper/lower bounds from the first stationary balance;
6. the rational difference-equation translation and its explicit decaying gamma-function homogeneous mode.

Not proved:

- a formula for `pi_0` for every three-cookie law;
- a universal `M=3` closure, so the frozen metric `M_closed` remains 2;
- the broader stationary-ergodic version of the source problem;
- current worldwide novelty or openness;
- any protocol closure or independent audit.

The next useful attack should target the missing relation for `pi_1` without assuming a finite stationary mean. A promising direction is to search for a second bounded tail observable or a renewal identity that annihilates the homogeneous mode, rather than differentiating the first-moment equation and introducing an uncontrolled stationary moment.
