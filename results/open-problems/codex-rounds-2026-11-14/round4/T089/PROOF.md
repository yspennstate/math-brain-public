# A smaller target remainder for the GOE spacing certificate

Let Z_s be the number of points of the stationary GOE bulk process of
intensity one in (0,s], and put

\[
b_k(s)=\mathbb E\binom{Z_s}{k},\qquad E(s)=\mathbb P(Z_s=0).
\]

For every integer k>=1 and every R>=0,

\[
\sup_{0\leq s\leq R} b_k(s)
\leq H_k(R):=\frac{R^k}{k!}
\left[k\left(k+\frac{\pi^2}{12}(k-1)\right)\right]^{k/4}.
\tag{1}
\]

In particular,

\[
\sup_{0\leq s\leq2}b_{58}(s)
\leq\frac{913317}{10^{12}}<10^{-6}.
\tag{2}
\]

This is a bound on a random-matrix target moment. No estimate for the
factorial moments of a billiard spectrum is asserted.

## The kernel and two elementary inequalities

The orthogonal sine process has the Pfaffian correlation kernel stated in
Section 1.2, equation (1.8), of Alexander I. Bufetov, Pavel P. Nikitin,
Yanqi Qiu, *On Number Rigidity for Pfaffian Point Processes*,
[arXiv:1810.09223](https://arxiv.org/html/1810.09223).
Set

\[
S(z)=\frac{\sin(\pi z)}{\pi z},\quad S(0)=1,\qquad D(z)=S'(z),
\qquad I(z)=\int_0^zS(u)\,du-\tfrac12\operatorname{sgn}(z),
\]

with I(0)=D(0)=0. For distinct x_1,...,x_k the k-point correlation
density is r_k(x_1,...,x_k)=Pf(A), where

\[
A_{ij}=\begin{pmatrix}
-I(x_i-x_j)&S(x_i-x_j)\\
-S(x_i-x_j)&D(x_i-x_j)
\end{pmatrix}.
\tag{3}
\]

This is the cited matrix kernel multiplied on the right, blockwise, by
J=((0,1),(-1,0)). The diagonal block is J. Evenness of S and oddness
of I,D make A antisymmetric. Thus det A=(Pf A)^2, and r_1=1.
Correlation densities are nonnegative almost everywhere.

First, for every real z,

\[
|I(z)|\leq\tfrac12.
\tag{4}
\]

To prove this without estimating an absolute integral over a long interval,
define

\[
c_n=\int_n^{n+1}|S(u)|\,du
=\int_0^1\frac{\sin(\pi v)}{\pi(n+v)}\,dv,\qquad n\geq0.
\]

The integrand at n=v=0 has its continuous limiting value. The c_n are
nonnegative and nonincreasing, and c_0<=1 since |S|<=1. At each positive
integer N,

\[
\int_0^N S(u)\,du=\sum_{n=0}^{N-1}(-1)^n c_n.
\]

Pairing consecutive terms from the beginning shows each sum is nonnegative.
Pairing the terms after c_0 shows each sum is at most c_0. For example, an
even-length sum is c_0-(c_1-c_2)-...-c_{N-1}; an odd-length sum is
c_0-(c_1-c_2)-...-(c_{N-2}-c_{N-1}). On each intervening lobe the integral
is monotone, so its values stay between its endpoint values. Consequently
0<=integral_0^z S<=c_0<=1 for every z>0. Subtracting 1/2 proves (4) there.
Oddness proves it for z<0, and the stated value at zero proves the last case.

Second, for every real z,

\[
S(z)^2+\frac{3}{\pi^2}D(z)^2\leq1.
\tag{5}
\]

Work in the complex Hilbert space L2([-1,1],dt/2). The functions 1 and
sqrt(3)t are orthonormal. The function f_z(t)=exp(i*pi*z*t) has norm one.
Its inner products with these two real functions are respectively S(z)
and sqrt(3)D(z)/(i*pi), since differentiation under the finite integral gives

\[
S(z)=\frac12\int_{-1}^1 e^{i\pi zt}\,dt,\qquad
D(z)=\frac12\int_{-1}^1 i\pi t e^{i\pi zt}\,dt.
\]

Subtract the two orthogonal projections from f_z. Nonnegativity of the
remaining squared norm gives (5). The same representation also gives
|S(z)|<=1.

## A determinant-one change of scale

Choose alpha>0 with alpha^4=pi^2/3. Let T be the diagonal 2k by 2k matrix
whose entries in each point block are alpha, alpha^{-1}, and put B=TAT.
Since det T=1, det B=det A. Its blocks are

\[
B_{ij}=\begin{pmatrix}
-\alpha^2 I(x_i-x_j)&S(x_i-x_j)\\
-S(x_i-x_j)&\alpha^{-2}D(x_i-x_j)
\end{pmatrix}.
\]

Each second row of a point block has squared Euclidean norm

\[
\sum_{j=1}^k\left(S(x_i-x_j)^2+
\frac3{\pi^2}D(x_i-x_j)^2\right)\leq k
\tag{6}
\]

by (5), including the j=i term, whose value is one. Each first row has
squared norm

\[
\sum_{j=1}^k\left(S(x_i-x_j)^2+
\frac{\pi^2}{3}I(x_i-x_j)^2\right)
\leq k+\frac{\pi^2}{12}(k-1),
\tag{7}
\]

because I(0)=0, S(0)=1, and (4) applies to the other k-1 terms. There
are exactly k rows of each type. Hadamard's determinant inequality yields

\[
|\det B|\leq
\left[k\left(k+\frac{\pi^2}{12}(k-1)\right)\right]^{k/2}.
\]

Taking a square root and using (3) gives

\[
0\leq r_k(x_1,\ldots,x_k)
\leq\left[k\left(k+\frac{\pi^2}{12}(k-1)\right)\right]^{k/4}.
\tag{8}
\]

Diagonals x_i=x_j have Lebesgue measure zero and do not affect the integral.
The factorial correlation identity therefore gives

\[
b_k(s)=\frac1{k!}\int_{(0,s]^k}r_k(x_1,\ldots,x_k)\,dx_1\cdots dx_k.
\]

Using (8) and s<=R proves (1), including s=0. The bound at k=1 is exactly
b_1(s)=s.

## A rational certificate at order 58

The elementary inequality pi<22/7 implies pi^2/12<121/147. One proof of
that inequality, requiring no decimal table, is

\[
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx=\frac{22}{7}-\pi.
\tag{9}
\]

For the equality, divide the numerator by 1+x^2 to obtain
x^6-4x^5+5x^4-4x^2+4-4/(1+x^2), and integrate each term.

Define

\[
Q_k(R)=\frac{R^{2k}}{(k!)^2}
\left[k\left(k+\frac{121}{147}(k-1)\right)\right]^{k/2},
\qquad k\text{ even}.
\tag{10}
\]

Thus H_k(R)^2<=Q_k(R), with Q_k(R) rational when R is rational.
At R=2, exact integer comparisons give

\[
\left(\frac{913316}{10^{12}}\right)^2
<Q_{58}(2)<\left(\frac{913317}{10^{12}}\right)^2
<10^{-12}.
\tag{11}
\]

Equations (1), (10) and (11) prove (2). The script check_remainder.py
verifies (11) by cross multiplication, and recomputes Q_k independently
as a product using k!=product_{j=1}^k j. Every smaller positive even k<58
has Q_k(2)>10^{-12}. This last statement is about the rational upper-bound
formula (10); it is not a lower bound for the actual GOE moments.

For every fixed R, (1) tends to zero as k tends to infinity: since
k+(pi^2/12)(k-1)<(1+pi^2/12)k and k!>=(k/e)^k,

\[
H_k(R)\leq
\left[\frac{R e(1+\pi^2/12)^{1/4}}{\sqrt{k}}\right]^k
\longrightarrow0.
\]

## Insertion into the earlier target-only comparison

For any nonnegative integer-valued count C_s with finite moments through
an even order k, write a_j(s)=E binom(C_s,j), a_0=1. The empirical law may
in particular come from a uniform shift of an interval around a finite circle.
Set V(s)=P(C_s=0), and define

\[
U_a=\sum_{j=0}^k(-1)^j a_j(s),\qquad
L_a=\sum_{j=0}^{k-1}(-1)^j a_j(s),
\]

with U_b,L_b defined for the GOE count. Pascal's identity gives, for n>=1,
sum_{j=0}^r(-1)^j binom(n,j)=(-1)^r binom(n-1,r), with a binomial
coefficient equal to zero when its lower argument exceeds its upper argument.
For n=0 the sum is one. Therefore L_a<=V<=U_a and L_b<=E<=U_b, while
U_b-L_b=b_k(s). Comparing opposite endpoints gives

\[
|V(s)-E(s)|\leq b_k(s)+
\max\{|U_a-U_b|,|L_a-L_b|\}
\leq b_k(s)+\sum_{j=1}^k|a_j(s)-b_j(s)|.
\tag{12}
\]

All sums are finite; no empirical tail estimate is used. Applying (2) at
k=58 gives the concrete certificate

\[
\sup_{0\leq s\leq2}|V(s)-E(s)|
\leq\sum_{j=1}^{58}\sup_{0\leq s\leq2}|a_j(s)-b_j(s)|
+\frac{913317}{10^{12}}.
\tag{13}
\]

For nested interval counts on a circle of circumference W>2, a grid in [0,2]
with largest gap eta and certified target tables with errors tau_{ji}
instead give

\[
\sup_{s\leq2}|V(s)-E(s)|\leq
\max_i\sum_{j=1}^{58}
\bigl(|a_j(t_i)-\widehat b_j(t_i)|+\tau_{ji}\bigr)
+\frac{913317}{10^{12}}+\eta.
\tag{14}
\]

Indeed (12) bounds the errors at grid points, both void functions are
nonincreasing, and E is 1-Lipschitz. The last property follows since the
probability that an added interval of length ell contains a point is at most
its expected count ell. Sandwiching V between adjacent grid values proves
(14).

Consequently the previous spacing reduction applies with Delta equal to
the right side of (14): for density rho=N/W, 0<h<=S, S+h<=2,

\[
\sup_{0\leq s\leq S}|F_N^{\mathrm{int}}(s)-F_{\rm GOE}(s)|
\leq\frac1N+
\frac{2\Delta/h+\omega_{F_{\rm GOE}}(h)+|\rho-1|}{\rho}.
\]

The improvement from order 390 to order 58 concerns the certified
truncation remainder at R=2. Bounds on the 58 empirical moment errors,
or certified tables for their GOE targets, are separate requirements.
