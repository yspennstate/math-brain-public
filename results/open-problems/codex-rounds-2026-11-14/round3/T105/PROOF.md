# An exact threshold for a scalar moment relaxation of the long-gap argument

## Scope and statement

For a unit-density spectrum, let C_s count the later levels within distance s of a level chosen by index. Poisson pair and triple correlations would give

\[
\mathbb E C_s=s,\qquad \mathbb E[C_s(C_s-1)]=s^2.
\tag{1}
\]

The probability that C_s is positive is the nearest-neighbour gap distribution at s. The constraints below retain (1) separately for each s. They do not require the variables C_s to belong to a common counting process.

For G>0, call F admissible if:

1. F:[0,\infty)\to[0,1] is nondecreasing and 1-Lipschitz, with F(0)=0.
2. F(s)=1 for s\geq G, and \(\int_0^\infty(1-F(s))\,ds=1\).
3. For every s\geq0 there is a nonnegative integer-valued random variable Z_s such that

\[
\mathbb E Z_s=s,\qquad
\mathbb E[Z_s(Z_s-1)]=s^2,\qquad
\mathbb P(Z_s>0)=F(s).
\tag{2}
\]

There is no compatibility requirement between the laws at different s.

**Theorem.** There is an admissible F if and only if G\geq G_*, where G_* is the unique root in \((2,109/54)\) of

\[
35-18G-9G^2+(12G-10)\sqrt{6G-5}=0.
\tag{3}
\]

An explicit admissible distribution at G_* is given in (15) below. Consequently, all scalar consequences of the two moments (1), even together with the full pair-correlation Lipschitz constraint and mean spacing, cannot force a support endpoint greater than G_*.

The constant (3) already occurs in Corollary 3 of Christoph Aistleitner, Valentin Blomer and Maksym Radziwiłł, *Triple correlation and long gaps in the spectrum of flat tori*, [published online-first text](https://ems.press/content/serial-article-files/31432), DOI 10.4171/JEMS/1356. The assertion here is optimality for the explicitly defined relaxation. It supplies no realization by a point process or by a torus spectrum, and makes no claim of priority for the general moment inequalities.

## 1. Why these are spectral constraints

Let x_1<\cdots<x_N, and set

\[
C_i(s)=\#\{j:i<j\leq N,\ x_j-x_i\leq s\}.
\]

The empirical gap distribution, with normalization N, is

\[
F_N(s)=\frac1N\sum_{i=1}^{N}\mathbf1_{C_i(s)>0}.
\]

This identity holds because C_i(s)>0 exactly when i<N and x_{i+1}-x_i\leq s. Directly,

\[
\frac1N\sum_i C_i(s)=T_{2,N}((0,s]),\qquad
\frac1N\sum_i C_i(s)(C_i(s)-1)
=T_{3,N}((0,s],(0,s]),
\tag{4}
\]

where T_3 counts ordered pairs of distinct later indices. In particular, no extra factor 2 belongs in the second identity.

For 0\leq a<b, each consecutive gap in (a,b] is one of the pairs counted by T_{2,N}((a,b]). Thus

\[
0\leq F_N(b)-F_N(a)\leq T_{2,N}((a,b]).
\tag{5}
\]

Poisson pair correlation makes the limiting right side b-a. Any limiting gap distribution therefore has the Lipschitz property used above. If the gaps are eventually bounded by G and their mean tends to 1, the limiting distribution is supported in [0,G] and has mean 1: bounded support permits passage to the limit in the first moment. The normalization N instead of N-1 has no effect on these limits.

Pointwise convergence of the triple statistic in (4) is not known for the flat 2-tori in question. The published averaged triple theorem must not be interpreted as such convergence. Conditions (2) deliberately describe ideal scalar Poisson moments, without making that assertion about any torus. Passing empirical moment limits to a weak limit of the count laws would also require a uniform-integrability argument; no such passage is used here. The exact witnesses in (2) are sufficient for the claimed obstruction to deductions from scalar moments.

## 2. The scalar moment problem

Fix s>0. Let Z be a nonnegative integer-valued variable with the two moments in (2). For every integer m\geq1 define

\[
q_m(n)=\frac{2mn-n(n-1)}{m(m+1)}.
\]

At n=0 both q_m(n) and \(\mathbf1_{n>0}\) are zero. At every positive integer n,

\[
1-q_m(n)=\frac{(n-m)(n-m-1)}{m(m+1)}\geq0,
\tag{6}
\]

because a product of consecutive integers is nonnegative. Taking expectations proves

\[
\mathbb P(Z>0)\geq L_m(s):=\frac{2ms-s^2}{m(m+1)}.
\tag{7}
\]

Choose m so that m-1\leq s\leq m. The following law attains (7):

\[
\begin{aligned}
p_m&=\mathbb P(Z=m)=\frac{s(m-s)}m,\\
p_{m+1}&=\mathbb P(Z=m+1)=\frac{s(s-m+1)}{m+1},\\
p_0&=\mathbb P(Z=0)=1-L_m(s).
\end{aligned}
\tag{8}
\]

The first two probabilities are nonnegative. Their sum is L_m(s), and

\[
p_0=\frac{(m-s)^2+m}{m(m+1)}>0.
\]

The moments can be verified without an inequality:

\[
mp_m+(m+1)p_{m+1}
=s(m-s)+s(s-m+1)=s,
\]

\[
m(m-1)p_m+m(m+1)p_{m+1}
=s\big((m-1)(m-s)+m(s-m+1)\big)=s^2.
\]

Hence the exact minimum is

\[
L(s)=L_{\lfloor s\rfloor+1}(s).
\tag{9}
\]

At an integer s=r\geq1 either adjacent choice of m gives r/(r+1), so (9) is continuous. Set L(0)=0. Because (8) attains the minimum, no quadratic minorant, including one with a constant term, can give a larger lower bound from these moments.

For completeness, the exact range of possible values p=\mathbb P(Z>0) is

\[
\begin{cases}
[L(s),s),&0<s\leq1,\\
[L(s),1],&s>1.
\end{cases}
\tag{10}
\]

To prove the upper assertion when s\leq1, use p\leq\mathbb E Z=s. Equality would force Z\in\{0,1\} almost surely, contradicting the positive second factorial moment. For an integer M\geq2 with M-1\geq s, the law on \{0,1,M\} with probabilities

\[
p_M=\frac{s^2}{M(M-1)},\quad
p_1=s-\frac{s^2}{M-1},\quad
p_0=1-s+\frac{s^2}{M}
\]

has the required moments and positivity probability s-s^2/M, tending to s. Convex mixtures with (8) give every intermediate value below s.

When s>1 there is a law with the required moments and no mass at zero. Here are explicit ingredients. Put k=\lfloor s\rfloor and \theta=s-k. The law A on \{k,k+1\}, with probabilities 1-\theta,\theta, has mean s and second factorial moment

\[
\nu_A=s^2-s+\theta(1-\theta)<s^2.
\]

Choose an integer M>s such that M(s-1)>s^2. The law B on \{1,M\} with probabilities

\[
\mathbb P_B(Z=M)=\frac{s-1}{M-1},\qquad
\mathbb P_B(Z=1)=\frac{M-s}{M-1}
\]

has mean s and second factorial moment \(\nu_B=M(s-1)>s^2\). The mixture with weight

\[
\lambda=\frac{s^2-\nu_A}{\nu_B-\nu_A}\in(0,1)
\]

on B and weight 1-\lambda on A has the desired moments and positivity probability 1. Mixing this law with (8) proves the remaining part of (10). For s=0 the only law is Z=0.

## 3. The lower envelope forced by a support endpoint

Any admissible F satisfies F(s)\geq L(s). From F(G)=1 and the Lipschitz bound it also satisfies

\[
F(s)\geq1-G+s\quad(0\leq s\leq G).
\tag{11}
\]

For now assume \(2\leq G\leq B:=109/54\), and define

\[
c=c(G)=\sqrt{6G-5}-1.
\]

In this range 1<c\leq5/3<2<G+1, and

\[
G=\frac{c^2+2c+6}{6},\qquad
G-c=\frac{(c-2)^2+2}{6}>0.
\tag{12}
\]

On [0,1], L(s)=s-s^2/2 and the line in (11) is nonpositive. On [1,2], L(s)=(4s-s^2)/6, and its difference from that line is

\[
\frac{6G-6-2s-s^2}{6}.
\]

This decreases with s and vanishes exactly at c. On [2,G], formula (9) gives L(s)=(6s-s^2)/12\leq3/4, whereas the line is at least 3-G\geq53/54>3/4. Thus the exact pointwise lower envelope on [0,G] is

\[
H_G(s)=\max\{L(s),1-G+s\}=
\begin{cases}
s-s^2/2,&0\leq s\leq1,\\
(4s-s^2)/6,&1\leq s\leq c,\\
1-G+s,&c\leq s\leq G.
\end{cases}
\tag{13}
\]

This function is itself nondecreasing and 1-Lipschitz. The derivatives on its three open pieces are 1-s, (2-s)/3 and 1, respectively. Its pieces meet continuously, it starts at zero, and it ends at one.

Integrating each polynomial in (13) gives

\[
\begin{aligned}
I(G):=\int_0^G H_G(s)\,ds
&=\frac13+
\left[\frac{s^2}3-\frac{s^3}{18}\right]_1^c+
\left[(1-G)s+\frac{s^2}2\right]_c^G\\
&=G-\frac{G^2}2+\frac1{18}+\frac{c^2}6+\frac{c^3}9.
\end{aligned}
\tag{14}
\]

In the last simplification, substitute G-1=(c^2+2c)/6 from (12). Since mean 1 is equivalent to \(\int_0^G F(s)\,ds=G-1\), a necessary condition for admissibility is D(G):=I(G)-G+1\leq0.

## 4. The threshold and an attaining distribution

Differentiation of (14), using c'(G)=3/(c+1), gives

\[
I'(G)=1-G+c,\qquad D'(G)=c-G<0.
\]

At G=2, direct substitution gives

\[
18D(2)=14\sqrt7-37>0,
\]

since \(14^2\cdot7=1372>1369=37^2\). At G=B=109/54 one has c=5/3 and

\[
D(B)=-\frac{25}{5832}<0.
\]

Continuity and strict decrease therefore give a unique zero G_* in (2,B). Substituting c=\sqrt{6G-5}-1 in 18D gives exactly the left side of (3).

If 2\leq G<G_*, (14) contradicts mean 1. If G<2, admissibility at G would imply admissibility at 2, because the support condition only becomes weaker; this contradicts D(2)>0. Thus no G<G_* is admissible.

Write c_*=c(G_*), and define

\[
F_*(s)=
\begin{cases}
s-s^2/2,&0\leq s\leq1,\\
(4s-s^2)/6,&1\leq s\leq c_*,\\
1-G_*+s,&c_*\leq s\leq G_*,\\
1,&s\geq G_*.
\end{cases}
\tag{15}
\]

Section 3 proves that F_* is nondecreasing, 1-Lipschitz, continuous, and takes values in [0,1]. Equations (14) and D(G_*)=0 prove that its mean is one.

It remains to check every scalar law in (2), rather than only the lower inequalities. For 0<s\leq1, F_*(s)=L(s)<s, so (8) supplies the law. For 1<s\leq c_* the same law applies. For c_*<s<G_*, the envelope calculation gives L(s)\leq F_*(s)<1; the s>1 part of (10), or the explicit mixture proving it, supplies the law. For s\geq G_* one has s>1 and F_*(s)=1, so use the law with no mass at zero constructed above. At s=0 use Z_0=0. All conditions of admissibility hold.

For any G>G_*, the same F_* remains admissible: its support is already contained in [0,G]. This proves both directions of the theorem.

## 5. Independent algebra and first-moment audit

The zero can also be specified without a square root. Substitution of (12) into 72D yields

\[
72D=40-24c-c^2(c-2)^2.
\tag{16}
\]

Thus c_* is a root of

\[
R(c):=c^4-4c^3+4c^2+24c-40=0,
\qquad G_*=(c_*^2+2c_*+6)/6.
\tag{17}
\]

For exact rational sign checks,

\[
R(33/20)=-10639/160000<0,
\qquad R(5/3)=25/81>0.
\]

On [1,2], \(R'(c)=24+4c(c-1)(c-2)\geq16>0\), so there is only one root in that interval. The corresponding bracket is

\[
\frac{1603}{800}<G_*<\frac{109}{54}.
\tag{18}
\]

The published decimal 2.00636193892510 lies in this bracket; additional decimal places are not needed by the proof.

An independent calculation of the mean uses the density, rather than integration of the CDF. There are no atoms because (15) is continuous. Its density is 1-s on (0,1), (2-s)/3 on (1,c_*), 1 on (c_*,G_*), and zero elsewhere. Its total mass is

\[
\frac12+
\left[\frac{2s}3-\frac{s^2}6\right]_1^{c_*}
+G_*-c_*
=G_*-\frac{c_*}3-\frac{c_*^2}6=1,
\]

by (12). Its first moment is

\[
\begin{aligned}
\int_0^1s(1-s)\,ds
+\int_1^{c_*}\frac{s(2-s)}3\,ds
+\int_{c_*}^{G_*}s\,ds
&=\frac{G_*^2}2-\frac{c_*^2}6-\frac{c_*^3}9-\frac1{18}\\
&=1,
\end{aligned}
\]

where the last equality is D(G_*)=0. This checks the normalizations by a second method.

## 6. What the obstruction leaves open

The admissible F_* is not exponential: F_*(1)=1/2, whereas the unit-rate exponential CDF has value 1-e^{-1}>1/2 at 1. The scalar constraints therefore do not determine the spacing law.

The family of moment witnesses constructed above need not couple to counts satisfying Z_a\leq Z_b for a<b, stationary increments, or the consistency relations of neighbouring anchor levels. Neither a point process with these laws nor a torus realizing them has been constructed. The theorem proves an obstruction only after those relations have been discarded. An improvement must use information outside this relaxation, for example joint counts in disjoint intervals or relations between different anchors. It does not follow that pair and triple correlations of an actual point process can do no better.
