# A Vandermonde bound for GOE factorial moments

Let Z_s be the number of points of the stationary GOE bulk process of
intensity one in (0,s], and write

\[
b_k(s)=\mathbb E\binom{Z_s}{k},\qquad E(s)=\mathbb P(Z_s=0).
\]

The following bound concerns this random-matrix target. It supplies no
factorial-moment estimate for a chaotic billiard.

Put p=22/7. For an integer k>=1 define

\[
K=\frac{k(k-1)}2,\qquad F_k=\prod_{n=0}^{k-1}n!,
\qquad a_k=\frac{k-1}4+\sum_{j=1}^k\frac1{j^2},
\]

\[
c_{ki}=\frac{k}{i^2}+p^2\sum_{\substack{1\leq j\leq k\\j\ne i}}
\frac1{(i+j)^2},\qquad
d_k=a_k^k\prod_{i=1}^k c_{ki}.
\]

For R>=0 let

\[
M_k(R)=
\frac{2^{k-1}k^{k/2}R^{k+K}(p/4)^K}{k!F_k}\,d_k^{1/4}.
\tag{1}
\]

Then

\[
\sup_{0\leq s\leq R}b_k(s)\leq M_k(R).
\tag{2}
\]

In particular, exact rational comparisons give

\[
\boxed{\ \sup_{0\leq s\leq2}b_{10}(s)
\leq\frac{517386}{10^{12}}<10^{-6}.\ }
\tag{3}
\]

The order 10 replaces order 58 in the preceding target-only void-probability
certificate. Equation (2) also proves the predecessor's proposed
b_20(2)<=10^-6 target: exact comparisons in (20) give

\[
\sup_{0\leq s\leq2}b_{20}(s)<10^{-89}.
\tag{3a}
\]

## 1. The kernel and its smooth derivatives

The external input is the orthogonal sine correlation kernel in Section 1.2,
equations (1.1) and (1.8), of Alexander I. Bufetov, Pavel P. Nikitin,
Yanqi Qiu, *On Number Rigidity for Pfaffian Point Processes*,
[arXiv:1810.09223](https://arxiv.org/html/1810.09223).
Set

\[
S(z)=\frac{\sin(\pi z)}{\pi z},\quad S(0)=1,\qquad D(z)=S'(z),
\qquad I(z)=\int_0^zS(t)\,dt-\tfrac12\operatorname{sgn}(z),
\]

with I(0)=D(0)=0. In the interleaved ordering
(u_1,v_1,u_2,v_2,...,u_k,v_k), the correlation matrix is

\[
A_{ij}=\begin{pmatrix}-I(x_i-x_j)&S(x_i-x_j)\\
-S(x_i-x_j)&D(x_i-x_j)\end{pmatrix},\qquad
r_k(x_1,\ldots,x_k)=\operatorname{Pf}A.
\tag{4}
\]

Evenness of S and oddness of I,D make A antisymmetric. Its diagonal block
is ((0,1),(-1,0)), hence r_1=1. Correlation densities are nonnegative
almost everywhere, and det A=(Pf A)^2.

For every real z,

\[
|I(z)|\leq\tfrac12.
\tag{5}
\]

Indeed, the unsigned lobe integrals

\[
h_n=\int_n^{n+1}|S(t)|\,dt
=\int_0^1\frac{\sin(\pi v)}{\pi(n+v)}\,dv,\quad n\geq0,
\]

are decreasing, nonnegative, and h_0<=1. The integral of S from zero to
an integer is an alternating partial sum of the h_n. Grouping consecutive
terms shows that every such sum lies in [0,h_0]. On each lobe the integral
is monotone, so the same holds at noninteger endpoints. Therefore
0<=integral_0^z S<=1 for z>0. Subtracting 1/2 proves (5) for z>0;
oddness and the assigned value at zero prove it everywhere.

The Fourier representation

\[
S(z)=\frac12\int_{-1}^1 e^{i\pi zt}\,dt
\]

can be differentiated any finite number of times. For every integer n>=0,

\[
|S^{(n)}(z)|
\leq\frac12\int_{-1}^1\pi^n|t|^n\,dt
=\frac{\pi^n}{n+1}.
\tag{6}
\]

In particular, for n,m>=0,

\[
|\partial_x^n\partial_y^m D(x-y)|
=|S^{(n+m+1)}(x-y)|
\leq\frac{\pi^{n+m+1}}{n+m+2}.
\tag{7}
\]

The discontinuous function I will never be differentiated.

## 2. Divided differences and the congruence determinant

For distinct real nodes t_1,...,t_i, use

\[
f[t_1,\ldots,t_i]
=\sum_{a=1}^i\frac{f(t_a)}{
\prod_{\substack{1\leq b\leq i\\b\ne a}}(t_a-t_b)}.
\tag{8}
\]

The empty denominator product for i=1 is one. This is the coefficient of
t^(i-1) in the interpolation polynomial of degree at most i-1. Subtract
that polynomial from a real C^(i-1) function f. The difference vanishes
at all i nodes; repeated Rolle's theorem gives a point xi in their convex
hull with f^(i-1)(xi)=(i-1)! f[t_1,...,t_i]. Consequently

\[
|f[t_1,\ldots,t_i]|\leq
\frac{\sup|f^{(i-1)}|}{(i-1)!}.
\tag{9}
\]

The i=1 case is the direct supremum bound. Applying (9) successively in
two variables bounds a double divided difference of orders n,m by
sup|partial_x^n partial_y^m f|/(n!m!). To justify the succession,
differentiate the finite sum (8) in the other variable, then apply (9)
to that derivative. Equations (6)--(7) therefore imply

\[
|S(x-\cdot)[x_1,\ldots,x_i]|
\leq\frac{\pi^{i-1}}{i!},
\tag{10}
\]

and the double divided difference of D(x-y), of orders i-1,j-1, has
magnitude at most

\[
\frac{\pi^{i+j-1}}{(i-1)!(j-1)!(i+j)}.
\tag{11}
\]

By symmetry of the point correlation, assume x_1<...<x_k. Permuting
two point blocks in (4) is an even permutation of matrix coordinates, so
this ordering introduces no Pfaffian sign. Define the lower triangular
matrix Q by

\[
Q_{ia}=\begin{cases}
\displaystyle\frac1{\prod_{\substack{1\leq b\leq i\\b\ne a}}
(x_a-x_b)},&a\leq i,\\
0,&a>i.
\end{cases}
\]

Thus the i-th row of Q applied to sampled values is (8). If

\[
\mathcal V(x)=\prod_{1\leq a<b\leq k}(x_b-x_a)>0,
\]

then its diagonal product gives \(\det Q=1/\mathcal V(x)\).
Let gamma_i=(i-1)!/pi^(i-1), and let T act as the identity on the u
coordinates and as diag(gamma_i)Q on the v coordinates. Therefore

\[
\det T=\frac{F_k}{\pi^K\mathcal V(x)}.
\tag{12}
\]

Put B=TAT^T. The Pfaffian congruence identity gives
Pf B=det(T) Pf A. For completeness, associate to A the two-form
sum_(a<b) A_ab e_a wedge e_b. The coefficient of
e_1 wedge ... wedge e_(2k) in its k-th exterior power is k! Pf A.
The linear substitution T multiplies that top-degree coefficient by
det T, proving the identity. Thus

\[
r_k(x)=\frac{\pi^K\mathcal V(x)}{F_k}\,|\operatorname{Pf}B|.
\tag{13}
\]

The absolute value is permitted because r_k>=0 and det T>0.

## 3. The normalized row bounds

The u/u entries of B are unchanged, and (5) bounds their off-diagonal
magnitudes by 1/2; their diagonal is zero. The entry in row u_l and
column v_i is gamma_i times (10), hence has magnitude at most 1/i.
The v_i/v_j entry is gamma_i gamma_j times the double divided difference
in (11), hence has magnitude at most pi/(i+j). Its diagonal is exactly
zero by antisymmetry, even after congruence.

Each u row therefore has squared norm at most

\[
\frac{k-1}4+\sum_{j=1}^k\frac1{j^2}=a_k.
\tag{14}
\]

The v_i row has k mixed entries of magnitude at most 1/i, and its
remaining nonzero entries are bounded as above. Its squared norm is at most

\[
\frac{k}{i^2}+\pi^2\sum_{j\ne i}\frac1{(i+j)^2}\leq c_{ki}.
\tag{15}
\]

Here pi<p=22/7. This rational upper bound follows, for example, from

\[
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx=\frac{22}7-\pi.
\tag{16}
\]

The polynomial division has quotient
x^6-4x^5+5x^4-4x^2+4 and remainder -4. Integrating the quotient gives
22/7, and integrating -4/(1+x^2) gives -pi.

Hadamard's determinant inequality now gives

\[
|\det B|\leq a_k^{k/2}\prod_i c_{ki}^{1/2}=d_k^{1/2}.
\]

Taking a square root, then using (13) and pi<p, proves the pointwise bound

\[
0\leq r_k(x)\leq
\frac{p^K\mathcal V(x)}{F_k}\,d_k^{1/4}.
\tag{17}
\]

Only the smooth v rows and columns have been transformed. In particular,
the jump in I at a coincidence does not enter (10) or (11).

## 4. Bounding the Vandermonde on an interval

For R>0 the Chebyshev polynomial T_n satisfies
T_n(cos theta)=cos(n theta), and so |T_n(t)|<=1 for -1<=t<=1.
The recurrence T_0=1, T_1=t, T_(n+1)=2tT_n-T_(n-1) shows that its
leading coefficient is 2^(n-1) for n>=1. Define monic polynomials

\[
P_0(t)=1,\qquad P_n(t)=2(R/4)^nT_n(2t/R-1),\quad n\geq1.
\]

The stated leading coefficients show that P_n is monic of degree n,
and sup_[0,R]|P_n|<=2(R/4)^n. Replacing the monomial columns of a
Vandermonde matrix by these polynomials is a triangular column operation
with diagonal one, hence

\[
\det(P_{j-1}(x_i))_{i,j=1}^k=\mathcal V(x).
\]

The first column has norm sqrt(k). Column n+1 has norm at most
2 sqrt(k)(R/4)^n for n>=1. Columnwise Hadamard therefore gives

\[
|\mathcal V(x)|\leq
2^{k-1}k^{k/2}(R/4)^K,\qquad x_i\in[0,R].
\tag{18}
\]

This uses a uniform maximum bound, not an evaluation of the Vandermonde
integral. It can be conservative even after retaining repulsion.

## 5. Integration and exact constants

The factorial correlation identity is

\[
b_k(s)=\frac1{k!}\int_{(0,s]^k}r_k(x)\,dx.
\tag{19}
\]

Coincident coordinates form a null set. For the distinct coordinates,
reorder them as above and apply (17)--(18). The resulting bound is uniform
on the cube, whose volume is s^k<=R^k. This proves (1)--(2). For R=0
both sides vanish; for k=1 the bound is exactly b_1(s)<=R.

For rational R, the fourth power of the displayed bound is the rational
number

\[
Q_k(R)=M_k(R)^4
=\frac{2^{4(k-1)}k^{2k}R^{4(k+K)}(p/4)^{4K}}
{(k!F_k)^4}\,a_k^k\prod_{i=1}^k c_{ki}.
\tag{20}
\]

The script check_repulsion.py evaluates (20) independently in two ways:
the displayed formula and an entrywise envelope matrix with the same row
bounds. Exact integer comparisons give

\[
\left(\frac{517385}{10^{12}}\right)^4
<Q_{10}(2)<
\left(\frac{517386}{10^{12}}\right)^4<10^{-24}.
\tag{21}
\]

Taking positive fourth roots proves (3). All smaller positive even k<10
have Q_k(2)>10^-24. This is a threshold of this explicit bound, not a
lower bound on the actual GOE factorial moments.

## 6. Insertion into the target-only comparison

Let C_s be any nonnegative integer-valued count with finite moments through
order 10, a_j(s)=E binom(C_s,j), and V(s)=P(C_s=0). The expectation here
may be the uniform shift average of intervals around a finite spectrum.
For n>=1 Pascal cancellation gives

\[
\sum_{j=0}^m(-1)^j\binom nj=(-1)^m\binom{n-1}m,
\]

with zero binomial coefficients beyond the support. For n=0 the sum is one.
Thus the odd and even partial sums bracket the zero-count indicator.
Writing L_a=sum_(j=0)^9 (-1)^j a_j and
U_a=L_a+a_10, and similarly for b_j, yields

\[
L_a\leq V\leq U_a,\qquad L_b\leq E\leq U_b,\qquad
U_b-L_b=b_{10}.
\]

Comparing V-E with U_a-L_b and E-V with U_b-L_a gives

\[
|V(s)-E(s)|\leq b_{10}(s)+
\max\{|U_a-U_b|,|L_a-L_b|\}
\leq b_{10}(s)+\sum_{j=1}^{10}|a_j(s)-b_j(s)|.
\]

Consequently

\[
\boxed{\ \sup_{s\leq2}|V(s)-E(s)|\leq
\sum_{j=1}^{10}\sup_{s\leq2}|a_j(s)-b_j(s)|+
\frac{517386}{10^{12}}.\ }
\tag{22}
\]

No empirical high-count-tail bound was used. For nested interval counts,
a grid of mesh eta with target-table errors tau_(ji) similarly gives

\[
\sup_{s\leq2}|V(s)-E(s)|\leq
\max_i\sum_{j=1}^{10}
(|a_j(t_i)-\widehat b_j(t_i)|+\tau_{ji})+
\frac{517386}{10^{12}}+\eta.
\tag{23}
\]

Indeed both void functions are nonincreasing, and the GOE void function
is 1-Lipschitz: the probability of finding a point in an added interval
is at most that interval's expected count, its length. Adjacent grid
endpoints therefore sandwich the discrepancy with at most eta extra error.
The preceding empty-interval-to-spacing reduction applies to (23).
Estimating the ten empirical moment errors for a chaotic billiard, or
supplying certified target tables for these ten moments, remains separate.
