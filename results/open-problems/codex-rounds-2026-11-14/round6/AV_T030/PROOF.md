# From the bordered form to Hilbert multipliers

This note checks the final multiplier step in OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026). It proves the bordered-form algebra, `lem:hilbert`, the infinite-coordinate identity `eq:sum-energy`, and its trace consequence. The spectral gap and vector variational principle, including its equality case, are inputs. No assertion that the complete hot-spots proof has been verified is made.

Let S be the unit circle with arclength measure ds. Fix p in the disk. Write K(s)=K(p,s). The kernel input, established in the preceding rounds, is:

1. K is positive, measurable and bounded.
2. For distinct s,t, N(s,t) is finite, symmetric, and N(s,t)>=1/(pi*|s-t|^2)>0.
3. For each finite distinct family, the matrix H=[B,ell;ell^T,0], with B_ii=0, B_ij=1/N(s_i,s_j) and ell_i=1/K(s_i), has at most one positive eigenvalue.

All reciprocals are entrywise. Put D(s,s)=0 and D(s,t)=K(s)K(t)/N(s,t) off the diagonal.

## 1. Independent recheck of the boundary input

Write dq=a dx, 0<=a<=A, m=q(disk), and suppose the Green operator T has norm at most d<1 in L2(q). The disk formulas are

\[
G(x,y)=\frac1{4\pi}\log\left(1+
 \frac{(1-|x|^2)(1-|y|^2)}{|x-y|^2}\right),\qquad
P_s(x)=\frac{1-|x|^2}{2\pi|s-x|^2}.
\]

For delta=1-r, the expression inside the first logarithm at (rs,x) is 1+delta*b_r, where b_r=(1+r)(1-|x|^2)/|rs-x|^2. On a fixed compact interior set b_r converges uniformly to 2(1-|x|^2)/|s-x|^2. The estimate 0<=z-log(1+z)<=z^2/2 gives G(rs,x)/delta -> P_s(x), uniformly there. At distinct boundary points the logarithm argument is 1+delta^2*(1+r)^2/(r^2|s-t|^2). Thus G(rs,rt)/delta^2 -> 1/(pi|s-t|^2). These constants also follow by taking respectively the inward derivative and the mixed inward derivatives of the original Green formula.

The pointwise bounds G(x,y)<=log(2/|x-y|)/(2*pi) and P_s(y)<=1/(pi|s-y|) give

\[
\int G(x,y)^3dy\le\frac3{8\pi^2},\qquad
\int P_s(y)^{3/2}dy\le4\sqrt{2/\pi}.
\]

For the first integral extend to the radius-two disk centered at x, put r=2*exp(-t), and use integral_0^infinity t^3 exp(-2t)dt=3!/2^4. For the second extend to the radius-two disk centered at s and integrate r^(-1/2). Hence Holder gives F_s=TP_s<=H0=12^(1/3)*A/pi uniformly. The cube of the Holder constant is (3/(8*pi^2))*(4*sqrt(2/pi))^2=12/pi^3. In particular F_s is in L2(q), even though P_s need not be.

For n>=2, reversal of the end Green factors and Tonelli give

\[
R_n(s,t)=\int P_s T^nP_t\,dq
=\langle F_s,T^{n-2}F_t\rangle_q
\le H_0^2m d^{n-2}.
\]

The n=0 term is at most 2*A/(pi*|s-t|): at least one of P_s,P_t is <=2/(pi*|s-t|), and each has ordinary area integral 1/2. The n=1 term is <=A*H0/2. Thus N is finite off the diagonal. Similarly, the Green L2 bound integral G^2<=1/(2*pi) makes the tail of K at most sqrt(A/(2*pi))*H0*sqrt(m)/(1-d), besides P_s(p)+H0. This proves boundedness of K(p,.) for fixed p.

On a compactly supported cutoff rho<=q, the radial limits are L2(rho) limits and can be passed through the bounded resolvent. Scaling the reciprocal matrix by diag(delta,...,delta,1) therefore gives the bordered limit with kernels K^rho,N^rho. Every coefficient of their nonnegative chain series increases to the full coefficient under increasing disk cutoffs rho. Tonelli and monotone convergence, with the preceding finite bounds, give K^rho -> K and N^rho -> N. The denominators stay positive. The finite reciprocal matrices converge entrywise, and the condition of at most one positive eigenvalue is closed: a two-dimensional positive subspace of a limiting matrix would remain positive for all sufficiently close matrices. This independently recovers the preceding boundary lemma from the interior-kernel input. It does not assume L2(q) convergence of individual Poisson sections.

## 2. Exact bordered inertia and conditional negativity

Let B be any real symmetric n by n matrix and ell any nonzero real vector. Let U have columns forming a basis of ker(ell^T), and choose y with ell^T y=1. The case n=1 has an empty U. In the coordinates x=Uz+t*y and last coordinate c the bordered quadratic form has matrix

\[
\begin{pmatrix}
C&h&0\\ h^T&e&1\\0&1&0
\end{pmatrix},\qquad
C=U^TBU,\quad h=U^TBy,\quad e=y^TBy.
\tag{1}
\]

This is an invertible change of coordinates because U spans the kernel and y is outside it. Replace c by c'=c+h^T z. The quadratic form becomes

\[
z^TCz+e t^2+2tc'.
\]

The final two-dimensional form has matrix J=[e,1;1,0] and determinant -1, hence one positive and one negative eigenvalue. Therefore the exact inertia is

\[
\operatorname{inertia}\begin{pmatrix}B&\ell\\\ell^T&0\end{pmatrix}
=\operatorname{inertia}(B|_{\ker\ell^T})+(1,1,0).
\tag{2}
\]

In particular the bordered matrix has at most one positive eigenvalue if and only if B is nonpositive on ker(ell^T). The zero bottom-right entry is essential to this argument.

For a second proof of the implication, suppose x lies in ker(ell^T) with x^TBx>0. Choose y with ell^Ty nonzero and replace y by y-(x^TBy)/(x^TBx)*x. This preserves ell^Ty and makes x^TBy=0. In the bordered form, (x,0) is orthogonal to (y,c). Choose the sign and magnitude of c so y^TBy+2c*ell^Ty>0. The two vectors are independent and span a positive plane, a contradiction.

Apply (2) to the kernel input. For real a_i with sum a_i=0, set x_i=K(s_i)*a_i. Then ell^T x=0 and

\[
\sum_{i,j}a_i a_jD(s_i,s_j)=x^TBx\le0.\tag{3}
\]

Repeated points are handled by summing their coefficients. Thus D is conditionally negative semidefinite. It is symmetric, has zero diagonal, is strictly positive off the diagonal, and satisfies

\[
0\le D(s,t)\le L^2|s-t|^2,\qquad
L=\sqrt\pi\,\|K\|_\infty.\tag{4}
\]

## 3. Hilbert realization with no regularity assumption left implicit

Fix s0 on S. Define

\[
\Gamma(s,t)=\tfrac12\{D(s,s_0)+D(t,s_0)-D(s,t)\}.
\]

For any coefficients c_i, put C0=sum c_i and add coefficient -C0 at s0. Expanding (3) for this augmented family gives

\[
\sum_{i,j}c_i c_j\Gamma(s_i,s_j)
=-\tfrac12\sum_{i,j}a_i a_jD(t_i,t_j)\ge0.\tag{5}
\]

Take the vector space of formal finite real sums of symbols e_s with this Gram form. A vector of zero squared norm is orthogonal to every vector: positivity of the quadratic polynomial ||v+t*w||^2 with ||v||^2=0 forces its linear coefficient to vanish. Thus the zero-norm vectors form a subspace that can be quotiented out. Complete the quotient to a real Hilbert space and let b(s) be the image of e_s. Since Gamma(s0,.)=0, b(s0)=0. Direct substitution gives

\[
\|b(s)-b(t)\|^2
=\Gamma(s,s)+\Gamma(t,t)-2\Gamma(s,t)=D(s,t).\tag{6}
\]

Consequently b is injective by strict positivity and Lipschitz by (4). In particular D is continuous, as follows from the realized distance; continuity of K or N was not silently assumed in this construction. Replace the Hilbert space by the closed span of b(S). A countable dense set of points on S maps densely into b(S), and rational finite linear combinations of their images are dense in the span. The resulting space is separable. In a finite or countable orthonormal basis let b_j be the real coordinate functions. Each is Lipschitz with constant at most L and is bounded, since b(s0)=0 and the circle has diameter two.

## 4. Conditional energy identity and pointwise trace consequence

Here are the additional analytic inputs, separated from the kernel statement. They are the vector variational and scalar-extension statements in Sections 3 and 4 of the preprint, not consequences of a general nonnegative potential alone.

Let Omega be the stated smooth bounded simply connected planar domain, Phi its smooth conformal parametrization, mu its first positive Neumann eigenvalue, and V its real eigenspace. Let g=(grad u) composed with Phi on S for a nonzero u in V. Assume:

* g is smooth and tangent, and its scalar Helmholtz extension W_g equals (grad u) composed with Phi.
* On tangent Lipschitz boundary vectors h there is a nonnegative quadratic form E with E(g)=0. Its nullspace is characterized by E(h)=0 if and only if X_h=W_h composed with Phi inverse is grad v for some v in V.
* The boundary form is

\[
E(h,k)=\tfrac12\iint N_0(s,t)(h(s)-h(t))\cdot(k(s)-k(t))\,dsdt
-\iint R(s,t)h(s)\cdot k(t)\,dsdt+\int c(s)h(s)\cdot k(s)\,ds,
\tag{7}
\]

where N=N0+R, R is integrable and symmetric, N0=1/(pi*|s-t|^2), and c is the smooth curvature weight. Also W_h(p)=integral K(s)h(s)ds for Lipschitz h.

For clarity the multiplier identity can be deduced from these inputs. Nonnegativity and E(g)=0 imply E(g,h)=0: the polynomial E(g+t*h)=2tE(g,h)+t^2E(h) is nonnegative for both signs of sufficiently small t. In particular E(g,b^2g)=0 for each real Lipschitz b. Subtract E(g,b^2g) from E(bg,bg) using (7). The curvature term cancels pointwise. At each pair, putting a=b(s), d=b(t), v=g(s), w=g(t), the difference of the N0 numerators is

\[
|av-dw|^2-(v-w)\cdot(a^2v-d^2w)=(a-d)^2v\cdot w.
\]

For the R term the subtraction gives R*(d^2-ad)*v dot w. Symmetry and averaging under s,t interchange replace d^2-ad by (a-d)^2/2. The squared Lipschitz difference cancels the N0 singularity, and all R terms are integrable. Hence

\[
E(bg)=\tfrac12\iint N(s,t)(b(s)-b(t))^2g(s)\cdot g(t)\,dsdt.
\tag{8}
\]

Use the Hilbert coordinates in (8). For m finite put

\[
F_m(s,t)=\tfrac12N(s,t)
 \sum_{j\le m}(b_j(s)-b_j(t))^2g(s)\cdot g(t),\quad s\ne t.
\]

Set F_m=0 on the diagonal. This diagonal has zero product arclength measure. Parseval gives the pointwise convergence of the coordinate sum to D, and

\[
|F_m(s,t)|\le\tfrac12 K(s)K(t)|g(s)||g(t)|.\tag{9}
\]

The right side is integrable: its integral is (integral K*|g|)^2/2, finite because K and g are bounded on a finite-measure circle. Dominated convergence, not monotone convergence of the signed F_m, now gives

\[
\begin{aligned}
\sum_j E(b_jg)
&=\lim_m\int\!\!\int F_m(s,t)\,dsdt\\
&=\tfrac12\iint K(s)K(t)g(s)\cdot g(t)\,dsdt\\
&=\tfrac12\left|\int K(s)g(s)\,ds\right|^2
=\tfrac12|W_g(p)|^2.
\end{aligned}\tag{10}
\]

Fubini in the second line is justified by the same absolute bound (9). If the Hilbert basis is finite, the argument simply terminates. No infinite-dimensional vector PDE or convergence of sum b_j*g in a Sobolev space is used.

If Phi(p) is a critical point of u, W_g(p)=0. Every scalar energy on the left is nonnegative. Thus each equals zero, since any fixed nonnegative term is bounded by every sufficiently long partial sum, whose limit is zero. By the assumed nullspace characterization, for each j there is v_j in V with X_(b_j*g)=grad v_j. The extension has Sobolev trace b_j*g by its definition. Therefore the boundary trace of grad v_j, pulled back by Phi, equals b_j*g almost everywhere. The former is smooth and the latter Lipschitz, so their difference is continuous. A continuous function on the circle that vanishes almost everywhere vanishes everywhere: otherwise continuity supplies a nonempty arc of positive arclength where its norm is positive. Thus the asserted trace equality is pointwise. This proves the trace consequence in the preprint without any exchange of infinitely many nullspace assertions.

For a second justification of the limit, write the nonnegative coordinate tail D-D_m. It decreases to zero and is bounded by D. The absolute error in (10) is at most one half of the integral of N*(D-D_m)*|g(s)||g(t)|. These nonnegative functions decrease to zero and are dominated by the integrable K(s)K(t)|g(s)||g(t)|. Their integrals tend to zero by continuity from above for finite integrals. This gives the same limit and factor 1/2 independently of signs.

## 5. Why nonnegativity is a genuine input

An infinite-coordinate stress example checks the preceding exchange and shows why zero total signed energy alone is insufficient. Let r=1/4 and

\[
b(e^{i\theta})=(2^{-n}\cos n\theta,2^{-n}\sin n\theta)_{n\ge1}
\quad\hbox{in }\ell^2(\mathbb N;\mathbb R^2).
\]

Subtract b(1) if an anchored realization is wanted. The n=1 pair makes this map injective. The geometric-sum inequality |s^n-t^n|<=n|s-t| gives squared Lipschitz constant at most sum n^2*r^n=r*(1+r)/(1-r)^3=20/27. The sum is obtained by differentiating sum r^n=r/(1-r) twice. Independently, two multiplications of (1-r)*sum n^2*r^n reduce it to sum (2n-1)*r^n and give the same value. Orthogonality of distinct trigonometric functions shows the affine span is infinite-dimensional.

Set Delta=theta-phi and z=cos Delta. The squared distance is exactly

\[
D(s,t)=2\sum_{n\ge1}r^n(1-\cos n\Delta)
=\frac{r(1+r)}{1-r}\frac{|s-t|^2}{1-2rz+r^2}.
\tag{11}
\]

This follows by taking the real part of sum r^n exp(i*n*Delta). In particular D>=r*|s-t|^2. Put K=1/(2*pi) and N=K^2/D off the diagonal. These are abstract test kernels, not asserted to arise from a disk potential or satisfy the eigenfunction variational hypotheses.

Use the scalar test g(theta)=cos(ell*theta), ell>=1, as one component of a vector. Its K-weighted mean is zero. The contribution A_n of the nth pair of multiplier coordinates to the right side of (8) equals one quarter of the ell-th Fourier coefficient of

\[
\frac{r^n}{c}(1-2r\cos\Delta+r^2)
 \left|\sum_{k=0}^{n-1}e^{ik\Delta}\right|^2,
\qquad c=\frac{r(1+r)}{1-r}=\frac5{12}.\tag{12}
\]

Indeed averaging cos(ell*theta)*cos(ell*phi) over the common rotation gives cos(ell*Delta)/2, and the extra factor 1/2 is the energy normalization. The Fejer polynomial in (12) has Fourier coefficient F_n(k)=max(n-|k|,0), so

\[
A_n=\frac{r^n}{4c}\{(1+r^2)F_n(\ell)
-r F_n(\ell-1)-r F_n(\ell+1)\}.
\]

It is zero for n<ell, equals -r^(ell+1)/(4*c) at n=ell, and equals r^n*(1-r)^2*(n-ell)/(4*c)>0 for n>ell. The positive tail sums to r^(ell+1)/(4*c), by sum k*r^k=r/(1-r)^2. Therefore sum A_n=0 exactly. At ell=1 the negative term is -3/80 and the positive tail is 3/80. All quantities follow a second time by integrating the total ratio sum_n r^n*|s^n-t^n|^2/D=1: its ell-th Fourier coefficient is zero.

For g=1, the same calculation gives A_n=r^n*((1-r)^2*n+2*r)/(2*c); its sum is 1/2, as required by (10) and integral K*g=1. This also checks the normalization using a nonzero mean.

There is an explicit uniform relative tail bound. After the first M coordinate pairs,

\[
0\le\frac{D-D_M}{D}\le4\sum_{n>M}n^2r^n,
\]

and the latter series equals

\[
4r^{M+1}\left\{\frac{(M+1)^2}{1-r}
+\frac{2(M+1)r}{(1-r)^2}
+\frac{r(1+r)}{(1-r)^3}\right\}\longrightarrow0.\tag{13}
\]

To derive it write n=M+1+k and use the three geometric moment sums for k=0,1,2. Subtracting the finite weighted sum from 20/27 is a separate exact check. Thus even the infinite-coordinate exchange is uniformly controlled in this test. Nevertheless a signed term is negative. This deliberately fails variational nonnegativity; it is not a counterexample to (10), to the preprint, or to hot spots. It proves why positivity of E must be retained when passing from (10) to separate zero energies.

A second discrete hazard is the diagonal. On finitely many nodes with atomic weights w_i, zero diagonal D gives

\[
\frac12\sum_{i\ne j}w_iw_jK_iK_jg_i\cdot g_j
=\frac12\left(\left|\sum_iw_iK_i g_i\right|^2
-\sum_iw_i^2K_i^2|g_i|^2\right).
\]

The omitted diagonal is not negligible for an atomic quadrature. In (10) it is negligible because arclength is nonatomic. The accompanying finite arithmetic checks include this diagonal correction rather than falsely identifying an atomic sum with the continuum integral.

## 6. Scope and next check

Equations (2)--(10) establish the selected final algebra/energy implication under the explicitly stated analytic inputs. They do not derive vector variational positivity or its equality case from the Neumann problem. They also do not independently prove the multiplicity and boundary-uniqueness inputs used for the subsequent contradiction. No defect was found in `lem:hilbert`, `eq:sum-energy`, or the pointwise trace consequence.

The next checkable step is the vector variational principle `prop:vector` and its equality case, including the tangent H1 decomposition and the sign/trace justification in `lem:curvature`. That would address the nonnegativity and nullspace assumptions used in Section 4 above. The full strict result on arbitrary nonsmooth convex domains remains outside the stated preprint theorem.
