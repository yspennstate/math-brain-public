# A finite correlation certificate for the empty-interval criterion

The result below extends the earlier empty-interval reduction by bounding its
missing statistic in terms of finitely many interval-count factorial moments.
It does not bound those moments for a chaotic billiard. The binomial
inequalities and the GOE correlation kernel are standard ingredients.

## 1. Counts and the certificate

Let a circle have circumference W, with N>=2 labelled points
0<=y_1<=...<=y_N<W; coincident points are permitted. For 0<=s<W put

\[
C(t,s)=\#\{j:y_j\in(t,t+s]\pmod W\},\qquad
a_k(s)=\frac1W\int_0^W\binom{C(t,s)}k\,dt,\quad a_0(s)=1.
\tag{1}
\]

Counts include multiplicities. In particular a_1(s)=Ns/W: each labelled
point belongs to the moving interval for a set of starting positions of
length s. Set

\[
V(s)=\frac1W\int_0^W\mathbf1_{\{C(t,s)=0\}}\,dt.
\tag{2}
\]

The target is the stationary, unit-intensity GOE bulk process, also called
the orthogonal sine process. Let Z_s count its points in (0,s], and put

\[
b_k(s)=\mathbb E\binom{Z_s}k,\quad b_0(s)=1,\qquad
E(s)=\mathbb P(Z_s=0).
\tag{3}
\]

For R>0 define

\[
C_R=\max\{2,R+\tfrac12\},\qquad
B_{2m}(R)=\frac{(R C_R)^{2m}(4m)^m}{(2m)!},\quad m\geq1.
\tag{4}
\]

**Finite correlation certificate.** If 0<R<W and

\[
\epsilon_k=\sup_{0\leq s\leq R}|a_k(s)-b_k(s)|,
\]

then, for every integer m>=1,

\[
\boxed{\quad
\sup_{0\leq s\leq R}|V(s)-E(s)|
\leq\sum_{k=1}^{2m}\epsilon_k+B_{2m}(R).
\quad}
\tag{5}
\]

The truncation term involves only the GOE target. There is no empirical
high-count-tail assumption. The bound can exceed one, and is deliberately
conservative. For each fixed R its last term tends to zero as m tends to
infinity.

## 2. Finite binomial inequalities

Use binom(n,k)=0 for k>n. For n>=1 and r>=0, Pascal's identity gives

\[
\begin{aligned}
\sum_{k=0}^{r}(-1)^k\binom nk
&=\sum_{k=0}^{r}(-1)^k\binom{n-1}k
 +\sum_{k=1}^{r}(-1)^k\binom{n-1}{k-1}\\
&=(-1)^r\binom{n-1}r.
\end{aligned}
\tag{6}
\]

For n=0 the sum is one. Consequently, pointwise for every n>=0,

\[
\sum_{k=0}^{2m-1}(-1)^k\binom nk
\leq\mathbf1_{\{n=0\}}
\leq\sum_{k=0}^{2m}(-1)^k\binom nk.
\tag{7}
\]

Integrate this inequality either over t in (1) or over the target process.
All sums are finite. With

\[
L_a=\sum_{k=0}^{2m-1}(-1)^k a_k(s),\quad
U_a=\sum_{k=0}^{2m}(-1)^k a_k(s),
\]

and similarly L_b,U_b, it follows that

\[
L_a\leq V\leq U_a,\quad L_b\leq E\leq U_b,\quad
U_b-L_b=b_{2m}(s).
\tag{8}
\]

In particular

\[
\begin{aligned}
V-E&\leq U_a-L_b=(U_a-U_b)+b_{2m}(s),\\
E-V&\leq U_b-L_a=(L_b-L_a)+b_{2m}(s).
\end{aligned}
\]

Thus the sharper pointwise version is

\[
|V(s)-E(s)|\leq b_{2m}(s)
+\max\{|U_a-U_b|,|L_a-L_b|\}
\leq b_{2m}(s)+\sum_{k=1}^{2m}|a_k(s)-b_k(s)|.
\tag{9}
\]

This comparison uses the two target endpoints, rather than bounding an
empirical inclusion–exclusion remainder. It remains valid for highly
clustered data and for 2m>N.

## 3. An explicit bound on the GOE remainder

The external input is the standard orthogonal sine correlation kernel in
Section 1.2, equations (1.1) and (1.8), of Alexander I. Bufetov, Pavel P.
Nikitin, Yanqi Qiu, *On Number Rigidity for Pfaffian Point Processes*,
[arXiv:1810.09223](https://arxiv.org/html/1810.09223).
In that convention, write

\[
S(z)=\frac{\sin(\pi z)}{\pi z},\quad S(0)=1,\qquad
D(z)=S'(z),\qquad
I(z)=\int_0^z S(u)\,du-\tfrac12\operatorname{sgn}(z),
\]

with I(0)=D(0)=0. For distinct x_1,...,x_k the correlation density is

\[
r_k(x_1,\ldots,x_k)=\operatorname{Pf} A,\qquad
A_{ij}=\begin{pmatrix}-I(x_i-x_j)&S(x_i-x_j)\\
-S(x_i-x_j)&D(x_i-x_j)\end{pmatrix}.
\tag{10}
\]

Here A is a 2k by 2k matrix with two by two blocks. This is the cited
kernel multiplied on the right by J=[[0,1],[-1,0]]. Since S is even and
I,D are odd, A is antisymmetric. On the diagonal its block is J, so
r_1=1. No Wigner-surmise approximation is used.

For |z|<=R, the following elementary bounds hold:

\[
|S(z)|\leq1,\qquad |I(z)|\leq R+\tfrac12,\qquad
|D(z)|\leq\frac\pi2<2.
\tag{11}
\]

For the last bound, use S(z)=integral_0^1 cos(pi z t) dt, differentiate on
this compact integration interval, and bound
pi integral_0^1 t |sin(pi zt)| dt by pi/2. The middle bound follows by
integrating |S|<=1. Every entry of A on [0,R]^k therefore has magnitude
at most C_R. Its diagonal entries vanish and each row has Euclidean norm
at most C_R sqrt(2k). Hadamard's determinant inequality and
det(A)=Pf(A)^2 give

\[
0\leq r_k(x_1,\ldots,x_k)
\leq C_R^k(2k)^{k/2}.
\tag{12}
\]

Indeed, the product of the 2k row norms is at most
(C_R sqrt(2k))^{2k}, and taking a square root gives (12).
Nonnegativity comes from r_k being a correlation density.

By the definition of factorial correlation density, Tonelli's theorem for
the nonnegative sum over distinct ordered points gives

\[
b_k(s)=\frac1{k!}\int_{(0,s]^k}r_k(x_1,\ldots,x_k)
\,dx_1\cdots dx_k
\leq\frac{(R C_R)^k(2k)^{k/2}}{k!},\quad 0\leq s\leq R.
\tag{13}
\]

This proves finiteness of each moment needed in (8). For k=2m it gives
exactly b_{2m}(s)<=B_{2m}(R). Combining (9) and (13) proves (5).

For completeness, put a=R C_R. The factorial estimate k!>=(k/e)^k follows
by summing log(j) and comparing with integral_1^k log(x) dx. Hence

\[
\frac{a^k(2k)^{k/2}}{k!}
\leq\left(\frac{a e\sqrt2}{\sqrt{k}}\right)^k\longrightarrow0.
\tag{14}
\]

There is also an exact rational ratio check along even orders:

\[
\frac{B_{2m+2}(R)}{B_{2m}(R)}
=\frac{2a^2(1+1/m)^m}{2m+1}.
\tag{15}
\]

This tends to zero. Formula (15) independently verifies the truncation
limit and is convenient when R is rational.

## 4. Finite grids and spacings

Suppose only a grid 0=t_0<...<t_q=R is available, of largest gap eta.
Suppose certified target tables satisfy
|hat b_k(t_i)-b_k(t_i)|<=tau_{ki}. Put

\[
\epsilon_{\rm grid}
=\max_{0\leq i\leq q}\sum_{k=1}^{2m}
\bigl(|a_k(t_i)-\widehat b_k(t_i)|+\tau_{ki}\bigr).
\]

Then

\[
\sup_{0\leq s\leq R}|V(s)-E(s)|
\leq\Delta:=\epsilon_{\rm grid}+B_{2m}(R)+\eta.
\tag{16}
\]

To prove this, (9) bounds the discrepancy at every grid point by
epsilon_grid+B_{2m}(R). V and E are nonincreasing. Also E is 1-Lipschitz:
for 0<=u<v, the difference E(u)-E(v) is the probability that (0,u] is
empty but (u,v] is not. It is at most the expected number of points in
(u,v], which is v-u. Sandwiching V(s) between V(t_i) and V(t_{i+1})
therefore adds at most eta. No modulus of continuity of the high-order
moments is needed.

Here is the resulting finite-energy spacing certificate. Define rho=N/W,
cyclic gaps g_j=y_{j+1}-y_j for j<N, g_N=W-y_N+y_1, and the ordinary
internal-gap CDF

\[
F_N^{\rm int}(s)=\frac1{N-1}\sum_{j<N}\mathbf1_{\{g_j\leq s\}}.
\]

Let F be the exact unit-mean GOE bulk right-neighbour spacing CDF, and choose
0<h<=S and S+h<=R<W. Write omega_F(h) for the modulus of F on [0,R]
at distances at most h. Then

\[
\boxed{\quad
\sup_{0\leq s\leq S}|F_N^{\rm int}(s)-F(s)|
\leq\frac1N+
\frac{2\Delta/h+\omega_F(h)+|\rho-1|}{\rho}.
\quad}
\tag{17}
\]

The GOE void function in (3) equals integral_s^infinity (1-F(u)) du.
To see the identity, partition the line into consecutive point gaps. In a
gap of length g, the set of starts whose interval of length s is empty has
length (g-s)_+. Averaging this length over gap beginnings uses their
intensity, which is one, and their Palm gap distribution F. Thus the empty
probability is integral (g-s)_+ dF(g)=integral_s^infinity (1-F(u)) du.
At s=0 the identity also gives mean gap one.

For clarity, (17) uses precisely the earlier reduction, which can be
rechecked as follows. The gap partition gives V(s)=W^{-1} sum_j(g_j-s)_+
and its right derivative is rho(F_N(s)-1), where F_N is the cyclic gap
CDF. At s>=h, convexity traps this derivative between the backward and
forward secants. Replacing each endpoint by E costs at most 2 Delta/h;
each secant of E differs from E'(s)=F(s)-1 by at most omega_F(h).
Since

\[
\rho(F_N-F)
=\rho(F_N-1)-(F-1)+(\rho-1)(1-F),
\]

the cyclic CDF error is at most
(2 Delta/h+omega_F(h)+|rho-1|)/rho. At 0<=s<h the forward secant still
gives the upper bound. The lower bound follows from F_N(s)>=0 and
F(s)<=omega_F(h), using F(0)=0. The displayed bound dominates omega_F(h):
this is immediate for rho<=1; for rho>=1 subtracting omega_F(h) from
(omega_F(h)+rho-1)/rho gives
(rho-1)(1-omega_F(h))/rho>=0. Finally, deleting one cyclic gap and
renormalizing changes the CDF by at most 1/N, proving (17).

No assertion that a chaotic spectrum satisfies small epsilon_grid is made.
Exact or certified eigenvalues, their completeness, and certified GOE
moment tables would all be required for a numerical billiard application.

## 5. A sufficient convergence hypothesis with no empirical tail bound

Suppose W_l tends to infinity and N_l/W_l tends to one. If for every fixed
k>=1 and every rational s>=0,

\[
a_{k,l}(s)\longrightarrow b_k(s),
\tag{18}
\]

then V_l converges locally uniformly to E, and the internal nearest-neighbour
CDFs converge locally uniformly to F.

Fix a rational s and take any fixed m in (9). The finite sum of errors tends
to zero. Thus limsup_l |V_l(s)-E(s)|<=B_{2m}(R) for any fixed R>=s. Let m
tend to infinity using (14). This proves convergence at rational s. On a
fixed compact interval, choose finitely many rational grid points with mesh
at most eta, ending beyond that interval. The monotonicity and Lipschitz
argument of Section 4 bounds the full discrepancy by the largest grid
discrepancy plus eta. First let l tend to infinity and then eta to zero.
This proves local uniform convergence of V_l.

Now fix S and 0<h<=S in the rechecked reduction, with R>=S+h. Take l to
infinity. The limiting upper bound for the spacing discrepancy is
omega_F(h). Continuity of F on the compact interval makes this tend to zero
as h decreases to zero. Since W_l tends to infinity and rho_l tends to one,
N_l also tends to infinity and the artificial-gap term vanishes.

For a specified sector with counting law N_sec(T)=cT+o(T), use the levels
in [Lambda,2Lambda), y_j=c(lambda_j-Lambda), W=c Lambda. Then rho tends to
one. Formula (18), for these explicitly defined averages in that sector,
is a sufficient spectral hypothesis for the spacing part of T089. It is
not proved here for any such sector. The order of limits is essential:
hold m fixed while taking the spectral limit, then increase m. No rate for
moments of order growing with energy has been assumed.

## 6. Why second-order data cannot close the certificate in general

Consider the following two unit-density configurations on a circle of
circumference 4:

\[
A=\{0,1/3,4/3,2\},\qquad
B=\{0,1/3,1,7/3\}.
\tag{19}
\]

Multiply the coordinates by three to work in Z/12Z. The positive ordinary
differences of {0,1,4,6} are 1,2,3,4,5,6. Those of {0,1,3,7} are
1,2,3,4,6,7. Adding the negatives modulo 12 gives, in both cases,
one copy of every nonzero residue other than 6, and two copies of 6.
Thus their complete ordered distinct-pair difference multisets are equal.
In unit-density coordinates these are one copy of r/3 for
r=1,2,3,4,5,7,8,9,10,11 and two copies of 2.

For any bounded measurable f(x,y), integrate
sum_{i!=j} f(y_i-t,y_j-t) over a uniform circular shift t. The contribution
of an ordered pair depends only on its oriented difference: the first
coordinate is uniform on the circle and the second is its translate by
that difference. Equality of the difference multisets therefore proves
equality of the full shifted two-point factorial correlation measures.
In particular a_1(s) and a_2(s) agree for every s<4, as do all interval
count variances and all circular Fourier intensities.

The cyclic gaps, however, are

\[
g(A)=(1/3,1,2/3,2),\qquad
g(B)=(1/3,2/3,4/3,5/3).
\tag{20}
\]

At s=1 their cyclic spacing CDFs are respectively 3/4 and 1/2.
At s=4/3 the gap-hinge formula gives

\[
V_A(4/3)=\frac{2-4/3}{4}=\frac16,\qquad
V_B(4/3)=\frac{5/3-4/3}{4}=\frac1{12}.
\tag{21}
\]

Direct integration of interval counts at this threshold gives

\[
\begin{array}{c|rrrr}
&\mathbb P(C=0)&\mathbb P(C=1)&\mathbb P(C=2)&\mathbb P(C=3)\\\hline
A&1/6&1/3&1/2&0\\
B&1/12&7/12&1/4&1/12
\end{array}
\tag{22}
\]

Both rows have a_1=4/3 and a_2=1/2, whereas a_3 is respectively 0 and
1/12. Hence the first missing moment already separates these spectra.

Repeat either configuration L times, at offsets 0,4,...,4(L-1), on the
circle of circumference 4L. There are 4L levels and the density remains
one. Each ordered base-pair difference is repeated with the same period
offsets; base self-pairs in distinct periods also occur identically.
Their complete two-point measures still agree. The cyclic gap lists are
L copies of (20), and all the discrepancies above persist. For s<4 their
interval-count laws are unchanged by repetition. The internal-gap CDFs
differ from their cyclic CDFs by at most 1/(4L). At s=1 their discrepancy
therefore tends to 1/4. The phenomenon survives increasing window length.

These are artificial periodic spectra. They show that matching general
two-point data cannot determine a spacing law or empty-interval function.
They do not show that GOE two-point data, together with additional billiard
structure, could never suffice. No such billiard implication is established
or refuted here.
