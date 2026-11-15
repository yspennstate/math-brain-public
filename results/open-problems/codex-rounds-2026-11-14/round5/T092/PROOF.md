# A quantitative bound for weighted residue transport

Let T=R/Z with normalized length measure. For an integrable function v on
R write

\[
 (\mathcal Fv)(z)=\sum_{l\in\mathbb Z}v(z+l).
\]

All norms of densities below are L1 norms, without a factor 1/2. The
result concerns the residue-balancing part of a packet passage. Its
coefficient discrepancy is an explicit input; no oscillatory-integral
asymptotic is assumed in the theorem.

## The transport bound

Suppose W(s,a)>=0 is C1 on R x [0,1] and vanishes unless

\[
 s\in[A,B],\qquad |s|\ge s_0>0,
 \qquad A<B.
\]

Choose 0<=psi<=1 in C_c^1((0,1)), L>0, beta in R, and define, with zero
extension in a,

\[
 \begin{split}
 f(s,a)&=W(s,a)\psi(a)^2,\\
 M(s)&=\int_0^1W(s,a)\,da,\qquad
 p=\mathcal F M,\\
 C_{\rm cut}&=\int_{\mathbb R}\int_0^1
                 W(s,a)(1-\psi(a)^2)\,da\,ds,\\
 V(s)&=\int_{\mathbb R}|\partial_a f(s,a)|\,da,\qquad
 H=\int_{\mathbb R}\frac{V(s)}{|s|}\,ds.
 \end{split}                                                    \tag{1}
\]

The integrand defining H is zero near s=0. Define

\[
 K(s,y)=\frac1{|s|L}
       f\left(s,\frac{y/s-\beta}{L}\right)\quad(s\ne0),
 \qquad K(0,y)=0.                                               \tag{2}
\]

This is a compactly supported C1 function on R2. Put d=B-A and

\[
 \begin{split}
 b(y)&=\sup_{s\in\mathbb R}|\partial_sK(s,y)|,\\
 J_1&=\int_{\mathbb R}|y|b(y)\,dy,\\
 J_2&=\int_{\mathbb R}(2y^2+|y|)b(y)\,dy,\\
 D_N&=\frac{dJ_1}{N}+\frac{J_2}{N^2}.
 \end{split}                                                    \tag{3}
\]

Let P,N be any positive integers. Let (q_j)_(j in Z) be nonnegative
integrable functions on R with q_0=0 and sum_j int q_j finite. Their
discrepancy from the sampled coefficient masses is

\[
 E_N=\sum_{j\in\mathbb Z}\int_{\mathbb R}
       \left|q_j(a)-\frac1N f(j/N,a)\right|\,da.                  \tag{4}
\]

For j!=0 push q_j(a) da forward under

\[
       t=\frac jN+\frac{j}{N^2}(La+\beta).                       \tag{5}
\]

Let r_(N,h) be the density on R of the sum of these measures over
j congruent to h modulo P, and let p_(N,h)=F r_(N,h). Then

\[
 \boxed{\quad
 \sum_{h=0}^{P-1}\left\|p_{N,h}-\frac pP\right\|_1
 \le E_N+D_N+\frac{P}{2L}H+C_{\rm cut}.
 \quad}                                                        \tag{6}
\]

The corresponding total density satisfies

\[
 \left\|\sum_h p_{N,h}-p\right\|_1
 \le E_N+D_N+\frac{P}{2L}H+C_{\rm cut}.                          \tag{7}
\]

There is no relation required between N and P. Both signs of s and of
j are allowed. In particular these are finite-N inequalities, including
N=1. The constant 1/2 in the one-dimensional quadrature inequality used
to obtain (6) is optimal.

### Centered quadrature

For g in C_c^1(R), mesh Delta>0, and any offset x_0,

\[
 \left|\Delta\sum_{k\in\mathbb Z}g(x_0+k\Delta)
                    -\int_{\mathbb R}g(x)\,dx\right|
       \le\frac\Delta2\int_{\mathbb R}|g'(x)|\,dx.               \tag{8}
\]

To prove this, put x_k=x_0+k Delta and partition R into the cells
[x_k-Delta/2,x_k+Delta/2]. On the right half-cell the fundamental
theorem of calculus gives

\[
 \int_{x_k}^{x_k+\Delta/2}|g(x_k)-g(x)|\,dx
 \le\int_{x_k}^{x_k+\Delta/2}
          (x_k+\Delta/2-u)|g'(u)|\,du.
\]

The weight on the right is at most Delta/2. On the left half-cell
the same calculation has weight u-(x_k-Delta/2), again at most
Delta/2. Add over all cells to obtain (8).

### Pushforward of the sampled masses

For j!=0, write s=j/N. The derivative of (5) with respect to a is
sL/N. Therefore the density produced by the model coefficient mass
N^(-1)f(s,a) da is exactly

\[
       K(j/N,Nt-j).                                             \tag{9}
\]

Indeed its inverse argument is a=((Nt-j)/s-beta)/L, and the density
Jacobian N/(|s|L) cancels the mass factor 1/N. The model has zero
coefficient at j=0 since f(0,a)=0. Its residue density is

\[
 R_{N,h}(t)=\sum_{j\equiv h\ (P)}K(j/N,Nt-j).                    \tag{10}
\]

Pushforward contracts the total variation norm: for a signed measure
nu and a measurable map F, testing F_*nu against functions bounded by
one gives ||F_*nu||<=||nu||. Applying this separately to every j and
using the triangle inequality gives

\[
       \sum_h\|r_{N,h}-R_{N,h}\|_1\le E_N.                      \tag{11}
\]

All the measures in this display have densities, because (5) is an
invertible affine map for j!=0. Absolute summability of their masses
justifies the countable sums.

### Freezing the slow argument

Define

\[
 Q_{N,h}(t)=\sum_{j\equiv h\ (P)}K(t,Nt-j).
\]

Since residue classes partition Z, the triangle inequality and the
change of variable y=Nt-j give

\[
 \begin{split}
 \sum_h\|R_{N,h}-Q_{N,h}\|_1
 &\le\frac1N\sum_{j\in\mathbb Z}\int_{\mathbb R}
     |K(j/N,y)-K((j+y)/N,y)|\,dy.                               \tag{12}
 \end{split}
\]

For fixed y, the difference inside the integral is bounded by
|y|b(y)/N. It is zero unless the interval with endpoints j/N and
(j+y)/N meets [A,B]. Every such j lies in

\[
       [NA-|y|,NB+|y|].
\]

This interval contains at most Nd+2|y|+1 integers: distinct integers
are separated by at least one. Thus the right side of (12) is at most

\[
 \frac1{N^2}\int |y|(Nd+2|y|+1)b(y)\,dy=D_N.                   \tag{13}
\]

The estimate has no factor P, since (12) sums disjoint sets of indices
before taking the bound. Compact support of K and of its derivative
makes J_1,J_2 finite. To check that support directly, on the support of
f one has |s|<=max(|A|,|B|) and 0<=a<=1, hence
|y|=|s(La+beta)|<=max(|A|,|B|)(L+|beta|).

### Balancing each residue

For fixed t!=0, substitute (2) into Q_(N,h). The a arguments form a
lattice, possibly with reversed orientation, of mesh

\[
                   \Delta=\frac{P}{|t|L}.
\]

Consequently Q_(N,h)(t) is 1/P times the quadrature sum in (8) for
g(a)=f(t,a), at a lattice offset depending on N,t,h,beta. Therefore

\[
 \left|Q_{N,h}(t)-\frac1P\int f(t,a)\,da\right|
             \le\frac{V(t)}{2|t|L}.                            \tag{14}
\]

All terms are zero near t=0, where the expression is set to zero.
Integrate (14) in t and sum over h to obtain PH/(2L).

Write F(t)=int f(t,a) da. Since W>=f, one has

\[
        \sum_h\|F/P-M/P\|_1=\int(M-F)=C_{\rm cut}.              \tag{15}
\]

Combining (11), (13), (14), and (15) proves the real-line version of
(6). Folding contracts L1: Tonelli and the triangle inequality give

\[
 \int_0^1\left|\sum_l v(z+l)\right|\,dz
                  \le\sum_l\int_0^1|v(z+l)|\,dz=\|v\|_1.
\]

Fold every real-line error to prove (6). The triangle inequality
proves (7).

## Relating the discrepancy to a Fourier coefficient array

The next bound specifies how an oscillatory-integral estimate can enter
(6), without presuming it has been proved. Suppose complex coefficient
arrays c_(N,j)(a), ell_(N,j)(a) on [0,1] satisfy

\[
 \begin{split}
 \sum_j\int_0^1|c_{N,j}|^2\,da&=\mathcal M,
             \qquad\mathcal M=\int_{\mathbb R}M(s)\,ds,\\
 |\ell_{N,j}(a)|^2&=\frac1N W(j/N-d_N,a),\\
 \eta_N^2&=\sum_j\int_0^1|c_{N,j}-\ell_{N,j}|^2\,da<\infty.
 \end{split}                                                    \tag{16}
\]

Let cutoffs 0<=chi_(N,j)<=1 equal one on the support of ell_(N,j).
Suppose q_j=psi^2 chi_(N,j)^2 |c_(N,j)|^2 for j!=0 and q_0=0.
Assume W(-d_N,a)=0 for every a, so ell_(N,0)=0 as well. Define

\[
 U=\int_{\mathbb R}|M'(s)|\,ds,\qquad
 \Omega=\int_0^1\psi(a)^2\sup_s|\partial_sW(s,a)|\,da.
\]

Then

\[
 \boxed{\quad
 E_N\le\eta_N\left(\sqrt{\mathcal M}
              +\sqrt{\mathcal M+U/(2N)}\right)
       +|d_N|\left(d+2|d_N|+\frac1N\right)\Omega.
 \quad}                                                        \tag{17}
\]

For j!=0, the cutoff condition implies

\[
 \bigl|q_j-\psi^2|\ell_{N,j}|^2\bigr|
 \le |c_{N,j}-\ell_{N,j}|(|c_{N,j}|+|\ell_{N,j}|).
\]

At j=0 the left side is zero. Cauchy--Schwarz on Z x [0,1] bounds
the summed integral of the right side by

\[
 \eta_N\left(\sqrt{\mathcal M}+\sqrt{B_N}\right),\qquad
 B_N=\frac1N\sum_jM(j/N-d_N).
\]

Apply (8) to M with mesh 1/N and offset -d_N. It gives
|B_N-mathcal M|<=U/(2N). This proves the first term of (17).

For the remaining change of argument, the fundamental theorem of
calculus gives

\[
 \int_0^1\psi(a)^2
    |W(j/N-d_N,a)-W(j/N,a)|\,da\le|d_N|\Omega.
\]

The difference is zero unless j/N is in
[A-|d_N|,B+|d_N|], which contains at most N(d+2|d_N|)+1 lattice
indices j. Multiply by 1/N and sum to obtain the second term of (17).
This proves the bound.

In the passage notation d_N=m Delta_N, with |Delta_N|<=1/N, its
last term is at most

\[
 \frac{|m|}{N}\left(d+\frac{2|m|+1}{N}\right)\Omega.             \tag{18}
\]

For all sufficiently large N, W(-d_N,a)=0 follows from the gap s_0
around zero. Thus eta_N->0 would imply E_N->0. The first equality
in (16) is exact for the Fourier coefficients of
A(u,a)e(mH_N(u)): Parseval in u gives sum_j |c_(N,j)(a)|^2=int |A(u,a)|^2 du;
integration in a and the substitution s=m(c+phi(u)) give mathcal M.
The second equality in (16) specifies the leading array to be checked.
The assertion eta_N->0 is not a consequence of Parseval and is not
proved here.

## Independent checks and scope

There is another proof of the factor 1/2 in (8). Let S(x)=x-x_k-Delta/2
on (x_k,x_(k+1)). It has distributional derivative
1-Delta sum_k delta_(x_k), and |S|<=Delta/2. Integration by parts gives

\[
 \Delta\sum_k g(x_k)-\int g=\int S(x)g'(x)\,dx,
\]

which proves (8) with the same constant.

That constant cannot be decreased even for nonnegative smooth functions.
Take a smooth unimodal bump b supported in (-1,1), with b(0)=1,
increasing on (-1,0), and decreasing on (0,1). For epsilon<Delta/2
put g_epsilon(x)=b(x/epsilon) and take the lattice Delta Z. Its
quadrature sum is Delta, its integral is epsilon int b, and
int |g_epsilon'|=2. Therefore

\[
 \frac{|\Delta\sum_k g_\epsilon(k\Delta)-\int g_\epsilon|}
             {\Delta\int|g_\epsilon'|}
       =\frac12-\frac{\epsilon\int b}{2\Delta}\longrightarrow\frac12.
\]

A second check of the Jacobian in (9) is to integrate it. With
y=Nt-j and then a=(y/s-beta)/L,

\[
 \int K(s,Nt-j)\,dt
      =\frac1N\int K(s,y)\,dy
      =\frac1N\int f(s,a)\,da.
\]

This is exactly the mass of the original sampled coefficient, for both
signs of s. The factor 1/P is also checked by integrating the
periodization sum_(k in Z) K(t,y-h-kP) over a y period of length P:
its integral is int f(t,a) da, so its average is F(t)/P.

The finite bound treats negative indices by absolute Jacobians and
reversal of a lattice; no sign change in the mass occurs. The possible
folding offsets Nl-h have no effect on (14), since (8) is uniform in
its offset. Zero weights give zero model terms. A zero exact array is
allowed, with its missing mass recorded in E_N. If psi is identically
zero, all removed target mass is correctly charged to C_cut. None of
these cases requires normalization of a cutoff subprobability.

For fixed P,W,psi,L,beta, one has D_N->0. Provided E_N->0, the order
of choices is therefore valid: first make C_cut small by choosing psi,
then make PH/(2L) small by choosing L, then take N large. All derivatives
of K may depend on the already chosen L; no bound uniform over future
L or future coordinate charts is claimed. The inequality
(1-psi)^2<=1-psi^2 also bounds the squared coefficient cutoff error by
C_cut under the substitution defining W. A finite packet list is handled
by summing (6) and its nonnegative error terms over that list.

This proves the weighted residue-density estimate, with explicit finite
errors and a sharp local quadrature constant. It does not establish
eta_N->0 for the passage coefficients, simultaneous smooth physical
closeness, the index-signal transmission, or the limiting construction.
No resolution of Banach's finite-measure problem follows from it.
