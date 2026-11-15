# Translation averaging of a boxed hard-core interaction

## Statement

Fix an integer (d\geq2), a cube side (L>0), a hard-core distance (0<a<L), an attraction strength (j>0), and an inverse temperature (\beta>0). For (\theta\in[0,L)^d), put

\[
b_\theta(x)=\left\lfloor\frac{x-\theta}{L}\right\rfloor\in\mathbb Z^d.
\]

Use half-open cubes. Two cube indices are neighbors when their difference belongs to (\{\pm e_1,\ldots,\pm e_d\}). Define

\[
u_\theta(x,y)=
\begin{cases}
+\infty,&b_\theta(x)=b_\theta(y),\ |x-y|<a,\\
-j,&b_\theta(x)=b_\theta(y),\ |x-y|\geq a,\\
-j,&b_\theta(x),b_\theta(y)\text{ are neighbors},\\
0,&\text{otherwise}.
\end{cases}                                                    \tag{1}
\]

The norm in the hard core is Euclidean. This is a particular boxed interaction of the form (1.13) in Qidong He, Ian Jauslin, Joel Lebowitz, Ron Peled, [*Liquid-vapor transition in a model of a continuum particle system with finite-range modified Kac pair potential*](https://arxiv.org/html/2510.24825v1), with equal same-cube and neighboring-cube attractions. Only its definition is used below; no coexistence theorem is invoked.

For a finite configuration (X), let

\[
H_\theta(X)=\sum_{\{x,y\}\subset X}u_\theta(x,y),\qquad
\overline H(X)=\mathbb E_\theta H_\theta(X),\qquad
W(X)=\mathbb E_\theta e^{-\beta H_\theta(X)},\qquad
F(X)=-\beta^{-1}\log W(X),                                  \tag{2}
\]

where the expectation is normalized Lebesgue measure on ([0,L)^d). Empty and singleton energies are zero.

The following facts hold.

1. The energies (H_\theta) have a stability bound uniform in (\theta). Averaging the energy produces an explicit stable, translation-invariant, finite-range hard-core pair potential.
2. Averaging the Boltzmann weight produces a translation-invariant (W), but (F) is not a pair energy. In fact, (F) is not additive on separated finite sets, however large their separation. Thus it cannot be represented by any finite-range interaction whose energy is additive on sets separated beyond its range.
3. The discrepancy between (F) and (\overline H) can be proportional to the particle number, even for configurations made of mutually distant two-particle groups.

These statements concern the operations in (2). They establish neither existence nor absence of a liquid–vapour transition for the averaged pair potential.

## 1. Uniform stability

Let (m=\lceil2dL/a\rceil) and (K=m^d). Subdivide each cube into (m^d) half-open cubes of side (L/m). Each small cube has diameter

\[
\sqrt d\,L/m\leq a/(2\sqrt d)<a.
\]

If (H_\theta(X)<\infty), no small cube contains two particles. Hence the occupation (n_k) of each original cube is at most (K).

Same-cube pairs number at most ((K-1)N/2), where (N=|X|): every particle has at most (K-1) partners in its cube, and this counts each pair twice. Neighboring-cube pairs number at most (dKN), since every particle has at most (2dK) partners in neighboring cubes and again each pair is counted twice. Consequently

\[
H_\theta(X)\geq-BN,\qquad
B=\frac j2\big((2d+1)K-1\big).                              \tag{3}
\]

If the energy is infinite, the inequality still holds. This proves uniform stability. It also makes the expectations in (2) well-defined: for fixed (N), all energies are bounded below and (0\leq e^{-\beta H_\theta}\leq e^{\beta BN}).

For an independent check of the constant, write the finite energy in terms of cube occupations:

\[
H_\theta=-\frac j2\sum_k(n_k^2-n_k)-j\sum_{\langle k,l\rangle}n_kn_l.
\]

The inequality (2n_kn_l\leq n_k^2+n_l^2), summed over unordered nearest-neighbor edges, gives (\sum_{\langle k,l\rangle}n_kn_l\leq d\sum_k n_k^2). Now (\sum_k n_k^2\leq K\sum_k n_k=KN), giving exactly (3) again.

## 2. The averaged pair potential

Define the tent product

\[
T(z)=\prod_{i=1}^d(1-|z_i|)_+,\qquad t_+=\max\{t,0\}.
\]

For every (k\in\mathbb Z^d) and (r\in\mathbb R^d),

\[
\mathbb P_\theta\big(b_\theta(x+r)-b_\theta(x)=k\big)
=T(r/L-k).                                                   \tag{4}
\]

To see this first in one dimension, let (s=r/L) and write the fractional part of ((x-\theta)/L) as (t\in[0,1)). It is uniform. The index difference is (\lfloor t+s\rfloor). Its probability of equaling (k) is the length of

\[
[0,1)\cap[k-s,k+1-s),
\]

which is ((1-|s-k|)_+). The components of (\theta) are independent, so the probabilities multiply. This proves (4).

If (|r|<a), every coordinate satisfies (|r_i|<L), because (a<L). Therefore (T(r/L)>0). The same-cube hard-core violation has positive probability, so the average of (u_\theta(x,x+r)) is (+\infty). If (|r|\geq a), there is no hard-core violation for any shift. Applying (4) gives

\[
\overline u(r)=
\begin{cases}
+\infty,&|r|<a,\\
-j\left[T(r/L)+\displaystyle\sum_{i=1}^d
\{T(r/L-e_i)+T(r/L+e_i)\}\right],&|r|\geq a.
\end{cases}                                                   \tag{5}
\]

Finite summation commutes with the expectation in (2), including infinite values: subtract the uniform finite lower bound of each summand and use additivity for nonnegative integrals. Thus

\[
\overline H(X)=\sum_{\{x,y\}\subset X}\overline u(y-x).       \tag{6}
\]

The function in (5) is even and depends only on displacement. Its finite part vanishes for (|r|\geq L\sqrt{d+3}): a nonzero unshifted tent has all coordinates of (r/L) of absolute value less than 1, and a nonzero shifted tent has one coordinate of absolute value less than 2 and all others less than 1. These conditions imply (|r|^2<L^2(d+3)). The hard core is contained inside this range. Averaging (3) proves stability of (5), with the same (B).

In particular, this operation does produce a translation-invariant hard-core attractive pair potential. It is anisotropic. No assertion about its phase diagram follows from this calculation.

There is already a difference between the two averages at sub-core separations. If (r=\varepsilon Le_1) with (0<\varepsilon<a/L), then same-cube shifts, of probability (1-\varepsilon), are forbidden, whereas neighboring-cube shifts, of probability (\varepsilon), have energy (-j). Thus (\overline u(r)=+\infty) but (W(\{0,r\})=\varepsilon e^{\beta j}>0). The obstruction below uses only separations greater than (a), so it does not rely on this hard-core difference.

## 3. A four-particle obstruction for averaged weights

The distribution of (H_\theta(X+t)) is the distribution of (H_\theta(X)): replace (\theta) by (\theta-t) modulo (L\mathbb Z^d). Thus (W) and (F) are translation invariant.

Set

\[
A=\{0,\tfrac32Le_1\},\qquad B_M=A+ML e_2,
\qquad M\in\mathbb N,\quad M\geq3.
\]

All these particles have mutual distances greater than (a). Between (A) and (B_M), the second cube indices differ by exactly (M), so no cross pair is in the same or neighboring cubes, for any shift. It follows that

\[
H_\theta(A\cup B_M)=H_\theta(A)+H_\theta(B_M).                \tag{7}
\]

Integer-cube translation also gives (H_\theta(B_M)=H_\theta(A)). Outside the measure-zero set of grid-boundary shifts, the first-coordinate cube difference for (A) equals 2 if (0<\theta_1<L/2), and equals 1 if (L/2<\theta_1<L). The other cube differences are zero. Thus, for an event (I) of probability (1/2),

\[
H_\theta(A)=-j\mathbf1_I,\qquad
H_\theta(A\cup B_M)=-2j\mathbf1_I.
\]

Writing (q=e^{\beta j}>1), this gives exactly

\[
W(A)=W(B_M)=\frac{1+q}{2},\qquad
W(A\cup B_M)=\frac{1+q^2}{2}.                                \tag{8}
\]

Subtracting the product of the two-particle weights gives

\[
W(A\cup B_M)-W(A)W(B_M)=\frac{(q-1)^2}{4}>0.                 \tag{9}
\]

Equivalently, the interaction between the two groups in (F) is

\[
\begin{split}
F(A\cup B_M)-F(A)-F(B_M)
&=-\frac1\beta\log\frac{2(1+q^2)}{(1+q)^2}\\
&=-\frac1\beta\log\left[1+\tanh^2(\beta j/2)\right]<0.
\end{split}                                                   \tag{10}
\]

This value is independent of (M). Since the distance between the two sets is (ML), (10) rules out additivity beyond any finite range.

There is also a direct obstruction to a pair representation of any range. If (F(X)=\sum_{\{x,y\}\subset X}v(y-x)), the values on two-particle configurations force

\[
v(y-x)=F(\{x,y\}).
\]

For every cross pair between (A) and (B_M), its boxed energy vanishes for every shift, so its two-particle (W) equals 1 and its (F) equals zero. Pair additivity would then force the left side of (10) to vanish, contradicting (10). A chemical-potential term cannot help: all singleton energies in (2) are zero and any additive one-particle term cancels in (10).

This is not an obstruction confined to an isolated configuration. In a neighborhood of these four points, all distances stay greater than (a) and all cross interactions stay zero. For any convergent sequence of configurations in that neighborhood, cube memberships converge for almost every shift; the exceptional shifts lie on finitely many coordinate hyperplanes. All Boltzmann factors are bounded there. Dominated convergence therefore gives continuity of the two- and four-particle weights. The strict inequality (9) persists on an open neighborhood. In particular, the contradiction is not removed by allowing equalities only almost everywhere in particle positions.

## 4. Independent check by shifting the second pair

Let

\[
C_M=A+\tfrac12Le_1+ML e_2.
\]

For (0<\theta_1<L/2), the two particles of (C_M) are in neighboring cubes; for (L/2<\theta_1<L), their first cube indices differ by 2. Its attraction event is therefore the complement of the event for (A). There are still no cross interactions. Consequently

\[
H_\theta(A\cup C_M)=-j\quad\text{almost surely},\qquad
W(A\cup C_M)=q.                                             \tag{11}
\]

Each isolated pair has the same weight ((1+q)/2) as before. But

\[
\frac{1+q^2}{2}-q=\frac{(q-1)^2}{2}>0.
\]

Thus the common translation can distinguish two arrangements with identical isolated-group weights, despite the groups being arbitrarily far apart. As a second derivation of (9), if (Z=e^{-\beta H_\theta(A)}), then (Z) equals (1) or (q), each with probability (1/2), and

\[
\mathbb E Z^2-(\mathbb E Z)^2=\operatorname{Var}(Z)
=\tfrac14(q-1)^2.
\]

## 5. An extensive discrepancy

For (n\geq1), take

\[
X_n=\bigcup_{k=0}^{n-1}(A+kML e_2),\qquad M\geq3.
\]

All cross-group boxed energies vanish and every group has the same attraction event. Hence

\[
H_\theta(X_n)=-nj\mathbf1_I,\quad
\overline H(X_n)=-\frac{nj}{2},\quad
W(X_n)=\frac{1+e^{n\beta j}}2.
\]

Using (1+e^t=2e^{t/2}\cosh(t/2)) gives

\[
F(X_n)-\overline H(X_n)=-\frac1\beta\log\cosh(n\beta j/2).
                                                                    \tag{12}
\]

For (t\geq0), (e^t/2\leq\cosh t\leq e^t). Thus

\[
-\frac{nj}{2}\leq F(X_n)-\overline H(X_n)
\leq-\frac{nj}{2}+\frac{\log2}{\beta}.
\]

There are (2n) particles, so

\[
\lim_{n\to\infty}\frac{F(X_n)-\overline H(X_n)}{|X_n|}
=-\frac j4.                                                   \tag{13}
\]

Independently, the exact formula for (W(X_n)) gives

\[
F(X_n)=-nj+\frac{\log2}{\beta}
-\frac1\beta\log(1+e^{-n\beta j}),
\]

which yields the same limit.

## Scope

Energy averaging preserves pair form and yields (5). Common-shift weight averaging yields (8)–(13), so it does not preserve pair form or finite-range additivity. In particular, these two averaging operations cannot be interchanged to transfer a boxed coexistence theorem directly to (5).

The calculation does not analyze mixtures of already normalized infinite-volume Gibbs measures. Their conditional laws include posterior weights for the grid shift; no conclusion about their possible Gibbs representations is asserted here. No novelty claim is made for the general fact that integrating out a common hidden variable creates dependent weights. The contribution is the explicit obstruction and averaged kernel for this boxed continuum interaction.
