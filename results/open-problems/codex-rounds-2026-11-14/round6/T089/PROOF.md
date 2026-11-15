# Exact integration of the GOE Vandermonde envelope

Let Z_s count the points in (0,s] of the stationary GOE bulk process of
intensity one. Write b_k(s)=E binom(Z_s,k) and E(s)=P(Z_s=0).
For k>=1 put

\[
p=22/7,\qquad K=k(k-1)/2,\qquad F_k=\prod_{n=0}^{k-1}n!,
\]
\[
a_k=\frac{k-1}{4}+\sum_{j=1}^k\frac1{j^2},\qquad
c_{ki}=\frac{k}{i^2}+p^2\sum_{\substack{1\leq j\leq k\\j\ne i}}
\frac1{(i+j)^2},\qquad d_k=a_k^k\prod_{i=1}^k c_{ki}.
\]

For every R>=0 and every integer k>=1,

\[
\boxed{\quad \sup_{0\leq s\leq R}b_k(s)\leq N_k(R):=
\frac{p^K R^{k+K}}{k!\prod_{1\leq i<j\leq k}(i+j)}\,d_k^{1/4}.\quad}
\tag{1}
\]

In particular,

\[
\sup_{s\leq2}b_9(s)<\frac{55771279}{10^{15}}<10^{-6},
\qquad
\sup_{s\leq2}b_{10}(s)<\frac{8253203}{10^{18}}<10^{-11}.
\tag{2}
\]

These are target moment bounds. No estimate on a billiard spectrum is assumed
or obtained. The improvement over the preceding bound comes from integrating
its Vandermonde factor rather than replacing that factor by its maximum.
The determinant integration and Pfaffian identities below are standard
algebraic tools; their needed forms are proved here.

## 1. The pointwise envelope

The external input is the orthogonal sine kernel in Section 1.2,
equations (1.1) and (1.8), of Alexander I. Bufetov, Pavel P. Nikitin,
Yanqi Qiu, *On Number Rigidity for Pfaffian Point Processes*,
[arXiv:1810.09223](https://arxiv.org/html/1810.09223).
Set

\[
S(z)=\sin(\pi z)/(\pi z),\quad S(0)=1,\quad D(z)=S'(z),\quad
I(z)=\int_0^z S(t)\,dt-\tfrac12\operatorname{sgn}(z),
\]

with I(0)=D(0)=0. In coordinates (u_1,v_1,...,u_k,v_k), the correlation
density is r_k(x)=Pf A, where

\[
A_{ij}=\begin{pmatrix}-I(x_i-x_j)&S(x_i-x_j)\\
-S(x_i-x_j)&D(x_i-x_j)\end{pmatrix}.
\tag{3}
\]

The diagonal block is ((0,1),(-1,0)); A is antisymmetric and r_1=1.
Also r_k>=0 almost everywhere and det A=(Pf A)^2.

The unsigned sine-lobe integrals

\[
h_n=\int_0^1\frac{\sin(\pi v)}{\pi(n+v)}\,dv\quad(n\geq0)
\]

decrease with n and satisfy h_0<=1. The integral of S from zero to a
positive integer is an alternating partial sum of these h_n. Pairing terms
shows that every such sum is in [0,h_0]. The integral is monotone on each
intervening lobe, so it remains in that interval at noninteger endpoints.
Oddness then gives |I(z)|<=1/2 for every real z, including the assigned
value at zero.

Differentiating the Fourier integral for S gives

\[
S(z)=\frac12\int_{-1}^1e^{i\pi zt}\,dt,\qquad
|S^{(n)}(z)|\leq\frac{\pi^n}{n+1}\quad(n\geq0).
\tag{4}
\]

For distinct real nodes t_1,...,t_i, the divided difference is

\[
f[t_1,...,t_i]=\sum_{a=1}^i
\frac{f(t_a)}{\prod_{b\ne a}(t_a-t_b)}.
\]

Subtract the degree at most i-1 interpolation polynomial from f. Applying
Rolle's theorem i-1 times shows that the divided difference is
f^(i-1)(xi)/(i-1)! for some xi in the convex hull of the nodes.
Consequently it is bounded by sup|f^(i-1)|/(i-1)!.
For two variables, apply this bound twice. Differentiation in the second
variable commutes with the first finite sum, which justifies the iteration.

Assume x_1<...<x_k and put Delta(x)=product_(a<b)(x_b-x_a).
Let Q take sampled values to the divided differences at the successive
prefixes x_1,...,x_i. Its diagonal entry i is
1/product_(a<i)(x_i-x_a), so det Q=1/Delta(x).
Let T act as the identity on u coordinates and as diag(gamma_i)Q on v
coordinates, where gamma_i=(i-1)!/pi^(i-1). Then

\[
\det T=F_k/(\pi^K\Delta(x)).
\tag{5}
\]

Put B=TAT^t. The u/u entries are unchanged and have magnitude at most 1/2
off the diagonal. By (4), the u_l/v_i entry is bounded by
gamma_i*pi^(i-1)/i!=1/i. A double divided difference of D=S', of orders
i-1,j-1, is bounded by

\[
\frac{\pi^{i+j-1}}{(i-1)!(j-1)!(i+j)}.
\]

Its two normalization factors leave pi/(i+j) in the v_i/v_j entry.
The diagonal entries vanish by antisymmetry. Thus the squared u row norms
are at most a_k and the squared v_i row norm is at most c_ki.
Here pi<p follows from

\[
0<\int_0^1\frac{x^4(1-x)^4}{1+x^2}\,dx=22/7-\pi.
\]

Indeed polynomial division gives quotient
x^6-4x^5+5x^4-4x^2+4 and remainder -4; integration gives the equality.
Hadamard's inequality gives
|Pf B|^4=|det B|^2<=product of squared row norms<=d_k.
Since det B=(det T)^2 det A, (5) implies

\[
0\leq r_k(x)\leq\frac{p^K}{F_k}\,\Delta(x)d_k^{1/4}.
\tag{6}
\]

Only smooth rows and columns were transformed. The discontinuous I block
was not differentiated. Permuting entire point blocks is an even coordinate
permutation, so the correlation is symmetric; (6) holds with |Delta| in
any chamber. Coincident nodes form a null set for integration.

## 2. A determinant integral as a Pfaffian

First let n=2m and take real integrable functions f_1,...,f_n on [0,1],
with all the following products integrable. Define

\[
M_{ij}=\int_{0<x<y<1}
(f_i(x)f_j(y)-f_j(x)f_i(y))\,dx\,dy.
\tag{7}
\]

Equivalently M_ij is the integral over the unit square of
f_i(x)f_j(y) sgn(y-x). For x in the cube put
H_ij(x)=sgn(x_j-x_i), and

\[
J=\int_{[0,1]^n}\prod_{i=1}^n f_i(x_i)\,\operatorname{Pf}H(x)\,dx.
\]

Expanding the Pfaffian as its signed sum over pairings and integrating
each pair separately gives J=Pf M. To fix normalization, the pairing sum
has coefficient 1/(2^m m!) when written as a sum over all permutations;
the same coefficient occurs on both sides.

Expand det[f_i(x_j)] as a sum over column permutations. For a term indexed
by sigma, relabel variables by y_i=x_sigma(i). The Pfaffian of H changes
by sgn(sigma). This cancels the determinant sign, and each of the n! terms
has integral J. Therefore

\[
\int_{[0,1]^n}\det[f_i(x_j)]\operatorname{Pf}H(x)\,dx=n!\operatorname{Pf}M.
\tag{8}
\]

On x_1<...<x_n the matrix H has every entry above the diagonal equal to
one and its Pfaffian is one. This follows by induction: expansion along
the first row gives sum_(j=2)^n (-1)^j=1, with the empty Pfaffian equal
to one. Both factors in the integrand of (8) are alternating in the
variables, so their product is symmetric. All n! chambers contribute
equally. Dividing (8) by n! proves

\[
\int_{0<x_1<...<x_n<1}\det[f_i(x_j)]\,dx=\operatorname{Pf}M.
\tag{9}
\]

For odd k use the ordered measure space [0,1] together with an atom at 2
of mass one. Extend f_1,...,f_k by zero at the atom, and introduce f_(k+1)
equal to zero on [0,1] and one at the atom. Apply the even identity to
these k+1 functions. In the ordered integral the only nonzero determinants
have exactly one atom, in the last position. Their determinants are the
original k-dimensional determinants. Repeated atom coordinates give
identical columns and zero determinant, so they contribute zero even
though they have positive product measure. Thus the same proof of (8)--(9)
applies. The enlarged matrix has original block M and last column

\[
M_{i,k+1}=\int_0^1 f_i(x)\,dx.
\tag{10}
\]

## 3. The Pfaffian product

For an even integer n and positive t_1,...,t_n,

\[
\operatorname{Pf}\left[\frac{t_j-t_i}{t_j+t_i}\right]_{i,j=1}^n
=\prod_{i<j}\frac{t_j-t_i}{t_j+t_i}.
\tag{11}
\]

Here is a polynomial proof. Multiply the Pfaffian by
D_n=product_(i<j)(t_i+t_j), obtaining a homogeneous polynomial P_n of
degree n(n-1)/2. It is alternating because D_n is symmetric. It is
therefore divisible by every t_j-t_i: setting t_i=t_j makes it zero.
These distinct linear factors are relatively prime, so their product
Delta_n divides P_n. Their degrees agree; hence P_n=C_n Delta_n for a
constant C_n.

Set t_(n-1)=a, t_n=-a as a polynomial substitution. In the Pfaffian
expansion multiplied by D_n, every pairing except the one containing
(n-1,n) retains the factor t_(n-1)+t_n and vanishes. That pair has
positive expansion sign. Consequently

\[
P_n\big|_{t_{n-1}=a,t_n=-a}
=(-2a)\prod_{i=1}^{n-2}(t_i^2-a^2)\,P_{n-2}.
\]

Direct substitution into Delta_n gives the same factor times Delta_(n-2),
because (a-t_i)(-a-t_i)=t_i^2-a^2. Thus C_n=C_(n-2).
Starting with C_0=1 proves (11).

Take f_i(x)=x^(i-1), 1<=i<=k. Equation (7) gives

\[
M_{ij}=\frac{1/i-1/j}{i+j}=\frac{j-i}{ij(i+j)}.
\tag{12}
\]

For even k, factor 1/i from row and column i of this Pfaffian and use
(11) with t_i=i. Since the product of the scale factors is 1/k!,
(9) becomes

\[
A_k:=\int_{0<x_1<...<x_k<1}\Delta(x)\,dx
=\frac1{k!}\prod_{1\leq i<j\leq k}\frac{j-i}{i+j}.
\tag{13}
\]

For odd k the extra column (10) is 1/i. After the same scale change it
is a column of ones. Apply (11) with k+1 parameters i=1,...,k and T,
then let T tend to positive infinity. The entries (T-i)/(T+i) tend to
one and all their factors on the right tend to one. The Pfaffian is a
polynomial in its entries, so its limit is the augmented Pfaffian. This
proves (13) for odd k as well, including k=1.

With A_0=1, two useful consequences are

\[
\prod_{i<j}(j-i)=\prod_{j=1}^k(j-1)!=F_k,
\qquad
\frac{A_k}{A_{k-1}}=
\frac1k\prod_{i=1}^{k-1}\frac{k-i}{k+i}
=\frac{((k-1)!)^2}{(2k-1)!}.
\tag{14}
\]

In particular A_1=1, A_2=1/6, A_3=1/180, and

\[
A_9=1/5954093444023153228800000.
\tag{15}
\]

## 4. The integrated bound and exact constants

The factorial correlation identity and symmetry give

\[
b_k(s)=\frac1{k!}\int_{(0,s]^k}r_k(x)\,dx
=\int_{0<x_1<...<x_k<s}r_k(x)\,dx.
\tag{16}
\]

The factor 1/k! has already been absorbed in the passage to the ordered
chamber. Scaling x=s y in (13) gives s^(k+K) A_k. Apply (6), (13),
and the first identity in (14) to (16). The factor F_k cancels, giving
exactly b_k(s)<=N_k(s)<=N_k(R). This proves (1). At R=0 both sides
vanish; at k=1 the bound is b_1(s)<=R, with equality at s=R.

For rational R the fourth power is rational:

\[
N_k(R)^4=
\left[\frac{p^K R^{k+K}}{k!\prod_{i<j}(i+j)}\right]^4
a_k^k\prod_i c_{ki}.
\tag{17}
\]

Exact integer comparisons give

\[
\left(\frac{55771278}{10^{15}}\right)^4<N_9(2)^4
<\left(\frac{55771279}{10^{15}}\right)^4<10^{-24},
\]
\[
\left(\frac{8253202}{10^{18}}\right)^4<N_{10}(2)^4
<\left(\frac{8253203}{10^{18}}\right)^4<10^{-44}.
\tag{18}
\]

The arithmetic expressions in (17)--(18) are evaluated in
check_integration.py with rational arithmetic. An independent integration
formula is available directly from the determinant expansion. For nonnegative
integer exponents e_1,...,e_k and a permutation sigma,

\[
\int_{0<x_1<...<x_k<1}\prod_{j=1}^k x_j^{e_{\sigma(j)}}\,dx
=\prod_{j=1}^k\frac1{\sum_{h=1}^j(e_{\sigma(h)}+1)}.
\tag{19}
\]

This follows by successively integrating x_1,...,x_k. Summing (19) with
the determinant signs gives the integral without a Pfaffian identity.
It can be organized by subsets S of exponent indices: start with D(empty)=1
and use

\[
D(S)=\frac{\sum_{a\in S}(-1)^{\#\{b\in S:b>a\}}D(S\setminus\{a\})}
{\sum_{a\in S}(e_a+1)}.
\tag{20}
\]

The sign counts the inversions created by putting a last. In particular
(20), (13) and (14) separately evaluate the normalization in (15).

Every 1<=k<9 has N_k(2)>10^-6; order 9 is the first successful order of
this bound. The first successful orders at R=1/2 and 1 are 5 and 6.
These statements concern (1), not lower bounds on the actual moments.

## 5. Nine-moment void and spacing certificates

Let C_s be any nonnegative integer-valued count with finite factorial moments
through order k, put a_j(s)=E binom(C_s,j), and V(s)=P(C_s=0).
For n>=1, Pascal cancellation gives

\[
\sum_{j=0}^r(-1)^j\binom nj=(-1)^r\binom{n-1}r.
\]

For n=0 the sum equals one. Thus even partial sums bound the zero-count
indicator above, and odd partial sums bound it below. Define
S_r(a)=sum_(j=0)^r (-1)^j a_j. If k is even, set
U_a=S_k(a), L_a=S_(k-1)(a); if k is odd, set
U_a=S_(k-1)(a), L_a=S_k(a). Define U_b,L_b identically for the GOE count.
Then for either parity,

\[
L_a\leq V\leq U_a,\qquad L_b\leq E\leq U_b,\qquad U_b-L_b=b_k.
\]

The two inequalities V-E<=U_a-L_b and E-V<=U_b-L_a imply

\[
|V-E|\leq b_k+\max(|U_a-U_b|,|L_a-L_b|)
\leq b_k+\sum_{j=1}^k|a_j-b_j|.
\tag{21}
\]

There is no empirical tail term. Taking k=9 in (21) gives

\[
\boxed{\quad
\sup_{0\leq s\leq2}|V(s)-E(s)|\leq
\sum_{j=1}^9\sup_{0\leq s\leq2}|a_j(s)-b_j(s)|
+\frac{55771279}{10^{15}}.\quad}
\tag{22}
\]

For nested interval counts, a grid 0=t_0<...<t_m=2 of maximum step eta,
and approximations b_hat_j(t_i) with certified errors tau_ji, the bound is

\[
\Delta:=\sup_{s\leq2}|V(s)-E(s)|\leq
\max_i\sum_{j=1}^9\bigl(|a_j(t_i)-\widehat b_j(t_i)|+\tau_{ji}\bigr)
+\frac{55771279}{10^{15}}+\eta.
\tag{23}
\]

Indeed V and E are nonincreasing, and E is 1-Lipschitz: adding an interval
of length ell changes the void event with probability at most the expected
number of points in that interval, which is ell. Adjacent grid values
therefore bound the discrepancy at an intermediate point with at most eta
additional error.

For N levels on a circle of length W>2 and density rho=N/W, the preceding
empty-interval reduction now applies with this Delta. If 0<h<=S and
S+h<=2, its internal-spacing conclusion is

\[
\sup_{s\leq S}|F_N^{\rm int}(s)-F_{\rm GOE}(s)|
\leq\frac1N+\frac{2\Delta/h+\omega_{F_{\rm GOE}}(h)+|\rho-1|}{\rho}.
\tag{24}
\]

Here omega is the modulus of continuity on [0,2]. Formula (24) is the
earlier deterministic reduction, with the improved target remainder from
(23). Certified target moment tables and estimates of the empirical moment
errors for a specified billiard symmetry sector remain separate requirements.
