# Boundary reciprocal inertia from the interior Green kernel

Let \(\mathbb D\) be the unit disk, let \(dq=a\,dx\), where \(0\le a\le A<\infty\), and assume
\[
 \int |\psi|^2\,dq\le d\int|\nabla\psi|^2,
 \qquad\psi\in H^1_0(\mathbb D),\qquad 0<d<1.                 \tag{1}
\]
All boundary integrals use arclength on the unit circle. Put \(m=q(\mathbb D)\). Define
\[
 G(x,y)=\frac1{2\pi}\log\left|\frac{1-x\overline y}{x-y}\right|,
 \quad G(x,x)=+\infty,\qquad
 P_s(x)=\frac{1-|x|^2}{2\pi|s-x|^2},\qquad
 N_0(s,t)=\frac1{\pi|s-t|^2}\ (s\ne t).
\]
Write \(T_\rho\) for integration against \(G\) on \(L^2(\rho)\), for any \(0\le\rho\le q\). The bounded-density weak Dirichlet argument gives a self-adjoint operator with \(\|T_\rho\|\le d\): if \(w=T_\rho f\), then
\[
 \|w\|_\rho^2\le d\int|\nabla w|^2
 =d\langle w,f\rangle_\rho\le d\|w\|_\rho\|f\|_\rho.
\]
The source lies in ordinary \(L^2(dx)\), since its squared norm is at most \(A\|f\|_\rho^2\), so this weak solution and its Green representation are legitimate. For \(w=0\) no division is needed. Set \(S_\rho=(I-T_\rho)^{-1}\), so \(\|S_\rho\|\le(1-d)^{-1}\). Every power of \(T_\rho\) preserves nonnegative functions.

Property (P) for a real symmetric finite matrix means at most one positive eigenvalue, counted with multiplicity. Reciprocals of kernels are entrywise.

The previously checked interior result is the following input: for compactly supported \(\rho\le q\), the kernel
\[
 M^\rho(x,y)=G(x,y)+
 \langle G(x,\cdot),S_\rho G(y,\cdot)\rangle_\rho             \tag{2}
\]
has (P) for each finite reciprocal matrix, with reciprocal diagonal zero. Its off-diagonal values and its correction on the diagonal are finite. This note proves the subsequent boundary lemma `lem:bordered` of OpenAI, *Strict hot spots and absence of interior critical points on smooth simply connected planar domains* (September 24, 2026), from this input. It does not establish the full hot-spots theorem.

## 1. Independent recheck of the interior singular-limit estimate

The explicit formula gives
\[
 0<G(x,y)\le\frac1{2\pi}\log\frac2{|x-y|}=:k_x(y).
\]
The superlevel set \(\{k_x>t\}\) is contained in a disk of area \(4\pi e^{-4\pi t}\). Layer integration therefore gives, for positive integers \(j\),
\[
 \int_{\mathbb D}G(x,y)^j\,dy
 \le 4\pi j\int_0^\infty t^{j-1}e^{-4\pi t}\,dt
 =\frac{j!}{(4\pi)^{j-1}}.                                  \tag{3}
\]
Independently, extending the integral of \(k_x^j\) to \(B(x,2)\) and setting \(r=2e^{-t}\) gives
\[
 \frac{2\pi}{(2\pi)^j}\int_0^2 r\log^j(2/r)\,dr
 =\frac{8\pi}{(2\pi)^j}\frac{j!}{2^{j+1}},
\]
the same number. In particular the second and fourth moments are bounded by \(1/(2\pi)\) and \(3/(8\pi^3)\).

For the regularization in the earlier audit, \(1/C_\epsilon=1/G+4\pi\epsilon f\), with \(0\le f\le1/2\) and \(0<C_\epsilon\le G\). Thus, off the diagonal,
\[
 G-C_\epsilon=4\pi\epsilon fGC_\epsilon\le2\pi\epsilon G^2.
\]
The diagonal has zero integration mass. By (3), for any bounded-density \(\rho\le q\),
\[
 \sup_x\|G(x,\cdot)-C_\epsilon(x,\cdot)\|_\rho
 \le\epsilon\sqrt{\frac{3A}{2\pi}},\qquad
 \|T_\rho-T_{\rho,\epsilon}\|
 \le\epsilon\sqrt{\frac{3A\rho(\mathbb D)}{2\pi}}.             \tag{4}
\]
Kernel domination gives \(\|T_{\rho,\epsilon}\|\le d\), and the inverse identity gives convergence of both resolvents in operator norm. Cauchy--Schwarz in the pairings in (2) gives convergence of their finite corrections, including on the diagonal. The direct diagonal \(C_\epsilon(x,x)=1/(2\pi\epsilon)\) diverges and the correction is nonnegative, so the reciprocal diagonal is at most \(2\pi\epsilon\). This rederives the previous singular-limit mechanism and its main constants. The earlier arithmetic script also passes unchanged.

## 2. Full boundary kernels are finite at distinct boundary points

Initially define every iterate applied to \(P_s\) by nonnegative iterated integrals. This does not apply an \(L^2\) operator to \(P_s\).

Since \(1-|y|\le|s-y|\),
\[
 P_s(y)\le\frac1{\pi|s-y|},\qquad
 \int_{\mathbb D}P_s(y)^{3/2}\,dy
 \le\frac{2\pi}{\pi^{3/2}}\int_0^2 r^{-1/2}\,dr
 =4\sqrt{\frac2\pi}.                                       \tag{5}
\]
Equation (3) gives \(\int G(x,y)^3dy\le3/(8\pi^2)\), uniformly in \(x\). Hölder in ordinary area measure now gives
\[
 0\le F_s(x):=\int G(x,y)P_s(y)\,dq(y)\le H,
 \qquad H=\frac{12^{1/3}A}{\pi}.                             \tag{6}
\]
Indeed the cube of the product of the two Hölder constants is
\((3/(8\pi^2))(4\sqrt{2/\pi})^2=12/\pi^3\). In particular \(F_s\in L^2(q)\) and \(\|F_s\|_q\le H\sqrt m\), uniformly in \(s\).

All later iterates are legitimate \(L^2(q)\) expressions. Their nonnegative chain representatives agree with the original iterated integrals by Tonelli. With \(B=\sqrt{A/(2\pi)}\), (3) and contraction give, for \(n\ge2\),
\[
 (T^nP_s)(p)=\langle G(p,\cdot),T^{n-2}F_s\rangle_q
 \le BH\sqrt m\,d^{n-2}.                                   \tag{7}
\]
This identity uses the Green evaluation of an \(L^2(q)\) function; it is finite for every interior \(p\). Define
\[
 K(p,s)=P_s(p)+\sum_{n\ge1}(T^nP_s)(p).
\]
Equations (6)--(7) prove
\[
 0<P_s(p)\le K(p,s)\le P_s(p)+H+\frac{BH\sqrt m}{1-d}.
                                                                    \tag{8}
\]
For fixed \(p\), \(P_s(p)\le(1+|p|)/(2\pi(1-|p|))\), so \(K(p,\cdot)\) is bounded. Its correction is bounded uniformly in both \(p,s\).

For distinct \(s,t\), put \(\delta=|s-t|>0\). At least one of \(|s-y|,|t-y|\) is at least \(\delta/2\); hence at least one of \(P_s(y),P_t(y)\) is at most \(2/(\pi\delta)\). Consequently
\[
 P_sP_t\le\frac2{\pi\delta}(P_s+P_t).
\]
The exact area integral of each Poisson section is
\[
 \int_{\mathbb D}P_s(y)\,dy
 =\int_0^1 r\,dr\int_0^{2\pi}P_s(re^{i\theta})\,d\theta
 =\frac12.                                                  \tag{9}
\]
The angular integral is one, either by its geometric Fourier series or the Poisson formula for constants. Thus
\[
 R_0(s,t):=\int P_sP_t\,dq\le\frac{2A}{\pi\delta},\qquad
 R_1(s,t):=\int P_sF_t\,dq\le\frac{AH}{2}.                  \tag{10}
\]
For \(n\ge2\), reversing the first Green edge in the nonnegative chain and using Tonelli gives
\[
 R_n(s,t):=\int P_sT^nP_t\,dq
 =\langle F_s,T^{n-2}F_t\rangle_q
 \le H^2m\,d^{n-2}.                                        \tag{11}
\]
The right pairing contains two genuine \(L^2(q)\) functions. Equations (10)--(11) prove the finite bound
\[
 0\le R(s,t):=\sum_{n\ge0}R_n(s,t)
 \le\frac{2A}{\pi|s-t|}+\frac{AH}{2}+\frac{H^2m}{1-d}.
                                                                    \tag{12}
\]
Reversing all edges proves symmetry. Set \(N(s,t)=N_0(s,t)+R(s,t)\) for \(s\ne t\), so \(0<N(s,t)<\infty\).

For completeness, nonnegative Tonelli and \(\int_{\partial\mathbb D}P_s(y)\,ds=1\) give
\[
 \iint R(s,t)\,ds\,dt
 =\sum_{n\ge0}\langle1,T^n1\rangle_q
 \le\frac{m}{1-d}.                                         \tag{13}
\]
Values on the boundary diagonal do not affect this identity. No finiteness claim at \(s=t\) is needed in (12).

The same estimates apply to every \(\rho\le q\), with the same \(A,d\) and with its mass at most \(m\).

## 3. Radial Green limits, with normalization checked twice

Fix \(0<R<1\) and \(|x|\le R\). For \(r\) sufficiently close to one, set
\[
 b_r(s,x)=\frac{(1+r)(1-|x|^2)}{|rs-x|^2}.
\]
It is uniformly bounded and continuous in \((r,s,x)\) on this compact set, since \(|rs-x|\ge r-R>0\). The Green identity becomes
\[
 \frac{G(rs,x)}{1-r}
 =\frac1{4\pi}\frac{\log(1+(1-r)b_r(s,x))}{1-r}.
\]
For \(u\ge0\), \(0\le u-\log(1+u)\le u^2/2\), as follows by integrating \(t/(1+t)\le t\). Hence this quotient converges uniformly in \(s,x\) to
\[
 \frac{b_1(s,x)}{4\pi}=P_s(x).                              \tag{14}
\]
An independent check differentiates the original logarithmic ratio. Writing \(z=x\overline s\), direct differentiation at \(r=1\) gives
\[
 -\partial_rG(rs,x)\big|_{r=1}
 =\frac1{2\pi}\mathop{\rm Re}\left(\frac1{1-z}
                              +\frac{\overline z}{1-\overline z}\right)
 =\frac{1-|z|^2}{2\pi|1-z|^2}=P_s(x).
\]
Integrating this radial derivative from \(r\) to one gives the same uniform limit and fixes its sign and factor.

The script's explicit error tolerance also follows from these formulas. With \(\eta=1-R\) and \(r\ge(1+R)/2\), one has \(b_r\le8/\eta^2\) and \(|\partial_r b_r|\le4/\eta^2+32/\eta^3\). Combining the mean value theorem with the logarithm remainder above gives
\[
 \left|\frac{4\pi G(rs,x)}{1-r}-4\pi P_s(x)\right|
 \le(1-r)\left(\frac4{\eta^2}+\frac{32}{\eta^3}
                         +\frac{32}{\eta^4}\right).
\]
For \(R=0.9\) the parenthesis is \(400+32000+320000=352400\), the uniform constant used in the arithmetic fixtures. This bound is deliberately coarse.

For fixed distinct \(s,t\), the explicit formula gives
\[
 G(rs,rt)=\frac1{4\pi}\log\left(1+
                  \frac{(1-r^2)^2}{r^2|s-t|^2}\right),
 \qquad
 \frac{G(rs,rt)}{(1-r)^2}\longrightarrow\frac1{\pi|s-t|^2}.
                                                                    \tag{15}
\]
Here \((1-r^2)^2/(r^2(1-r)^2)=(1+r)^2/r^2\to4\), and the logarithm divided by its argument tends to one. To check the same factor independently, let the two radial variables be independent. Near \((1,1)\) the endpoints stay separated, so \(G(\alpha s,\beta t)\) is smooth, vanishes when either radius is one, and
\[
 \partial_\alpha\partial_\beta G(\alpha s,\beta t)\big|_{(1,1)}
 =-\partial_\beta P_s(\beta t)\big|_{\beta=1}
 =\frac1{\pi|s-t|^2}.
\]
Two integrations of this continuous mixed derivative over \([r,1]^2\) prove (15) again.

## 4. Compact-support resolvent boundary limits

Fix compactly supported \(0\le\rho\le q\), with support in \(\{|x|\le R\}\), and fix \(p\in\mathbb D\). Take \(r>\max(R,|p|)\) tending to one. For \(s\) on the circle let
\[
 v_{r,s}(x)=\frac{G(rs,x)}{1-r},\qquad v_s(x)=P_s(x),
 \quad x\in\operatorname{supp}\rho.
\]
By (14), \(v_{r,s}\to v_s\) uniformly there, hence in \(L^2(\rho)\). In particular the source norms remain bounded. For each fixed pair \(s,t\),
\[
 \begin{aligned}
 &|\langle v_{r,s},S_\rho v_{r,t}\rangle_\rho
       -\langle v_s,S_\rho v_t\rangle_\rho|\\
 &\quad\le\frac{\|v_{r,s}-v_s\|_\rho\|v_{r,t}\|_\rho
                 +\|v_s\|_\rho\|v_{r,t}-v_t\|_\rho}{1-d}
 \longrightarrow0.                                         \tag{16}
 \end{aligned}
\]
Likewise \(G(p,\cdot)\in L^2(\rho)\) by (3), so
\[
 |\langle G(p,\cdot),S_\rho(v_{r,s}-v_s)\rangle_\rho|
 \le\frac{\|G(p,\cdot)\|_\rho\|v_{r,s}-v_s\|_\rho}{1-d}
 \longrightarrow0.                                         \tag{17}
\]
On this compact support, \(P_s\) is bounded and belongs to \(L^2(\rho)\). Expanding the norm-convergent geometric series for \(S_\rho\), and using the nonnegative chain representatives, identifies
\[
 \langle P_s,S_\rho P_t\rangle_\rho=R^\rho(s,t),\qquad
 P_s(p)+\langle G(p,\cdot),S_\rho P_s\rangle_\rho=K^\rho(p,s).
                                                                    \tag{18}
\]
Equations (15)--(18) prove
\[
 \frac{M^\rho(rs,rt)}{(1-r)^2}\longrightarrow N^\rho(s,t)
 \quad(s\ne t),\qquad
 \frac{M^\rho(p,rs)}{1-r}\longrightarrow K^\rho(p,s).          \tag{19}
\]
The zero measure case follows directly from (14)--(15).

## 5. The bordered matrix and removal of the support cutoff

Choose distinct \(s_1,\ldots,s_k\) on the circle. The interior input applies to \(rs_1,\ldots,rs_k,p\), which are distinct because \(r>|p|\). Scale its reciprocal matrix by the positive diagonal matrix
\(\operatorname{diag}(1-r,\ldots,1-r,1)\). Each scaled matrix has (P). By (19), its entrywise limit is
\[
 H^\rho=\begin{pmatrix}B^\rho&\ell^\rho\\(\ell^\rho)^T&0\end{pmatrix},
 \quad
 B^\rho_{ij}=\frac1{N^\rho(s_i,s_j)}\ (i\ne j),\quad
 B^\rho_{ii}=0,\quad
 \ell^\rho_i=\frac1{K^\rho(p,s_i)}.                           \tag{20}
\]
Every denominator in this formula is positive and finite. The diagonals stay zero; no double boundary limit on a coincident pair is required.

Property (P) is closed under entrywise convergence of fixed-size matrices. To see this, if a limiting form were positive definite on a two-dimensional subspace, it would have a positive minimum on the unit circle of that subspace. Entrywise convergence gives uniform convergence of quadratic forms on that circle. The approximating matrices would then also be positive definite on that subspace, contradicting (P). Thus \(H^\rho\) has (P).

Now take \(\rho_j=\mathbf1_{\{|x|\le r_j\}}q\), with \(r_j\uparrow1\). A term \((T_{\rho_j}^nP_s)(p)\), \(n\ge1\), is the integral of
\[
 G(p,x_1)G(x_1,x_2)\cdots G(x_{n-1},x_n)P_s(x_n)
\]
against \(\prod_{h=1}^n\mathbf1_{\{|x_h|\le r_j\}}dq(x_h)\). Its integrand increases to the full chain integrand. The term \(R_n^{\rho_j}(s,t)\) has \(n+1\) integration variables, end factors \(P_s(x_0),P_t(x_n)\), and \(n\) Green factors; the same statement holds. For \(n=0\) this is simply \(\int P_sP_t\,d\rho_j\).

Tonelli and monotone convergence on each product space, then on the counting measure over \(n\), give
\[
 K^{\rho_j}(p,s)\uparrow K(p,s),\qquad
 R^{\rho_j}(s,t)\uparrow R(s,t),\qquad
 N^{\rho_j}(s,t)\uparrow N(s,t)\quad(s\ne t).                 \tag{21}
\]
Logarithmic poles on coincident integration variables have product measure zero because the measures have densities; equivalently the nonnegative integrals can be defined with arbitrary values on those null sets. Bounds (8) and (12) prove that the indicated limits are finite. Direct terms \(P_s(p)\) and \(N_0(s,t)\) prove strict positivity. Hence the reciprocals in (20) converge to those for the full \(q\). A second finite-matrix closure argument proves
\[
 \boxed{\begin{pmatrix}B&\ell\\\ell^T&0\end{pmatrix}
          \text{ has (P)},\qquad
 B_{ij}=1/N(s_i,s_j)\ (i\ne j),\quad B_{ii}=0,\quad
 \ell_i=1/K(p,s_i).}                                        \tag{22}
\]
This is `lem:bordered`. The proof never identifies operators on varying weighted Hilbert spaces by an unsupported norm limit: cutoff removal uses their common nonnegative product integrals.

## 6. Checks on the edge cases

The assumption \(P_s\in L^2(q)\) really can fail under (1). Take \(dq=dx\) on the disk. Zero extension to the square \((-1,1)^2\) gives
\(\int\psi^2\le\int|\partial_x\psi|^2\) and the corresponding inequality in \(y\). For the first inequality, a smooth zero-trace function \(f\) on \((-1,1)\) satisfies
\[
 |f(x)|^2\le\min(x+1,1-x)\int_{-1}^1|f'|^2,
 \qquad\int_{-1}^1\min(x+1,1-x)\,dx=1.
\]
Integrate along horizontal lines and then use density; the vertical inequality is identical. Adding gives (1) with \(d=1/2\), a strict margin.

Nevertheless, the angular Fourier series of the Poisson kernel gives
\[
 \int_0^{2\pi}P_s(re^{i\theta})^2\,d\theta
 =\frac1{2\pi}\left(1+2\sum_{n\ge1}r^{2n}\right)
 =\frac{1+r^2}{2\pi(1-r^2)}.
\]
Consequently, for \(0<R<1\),
\[
 \int_{|x|\le R}P_s(x)^2\,dx
 =\frac{-R^2-2\log(1-R^2)}{4\pi}\longrightarrow+\infty.
                                                                    \tag{23}
\]
The same divergence follows locally by writing \(x=1-u+iv\), taking \(s=1\), \(0<u<1/4\), \(|v|\le u/2\). This region lies in the disk and
\(1-|x|^2=2u-u^2-v^2\ge u\), \(|1-x|^2\le5u^2/4\). Thus \(P_1(x)\ge2/(5\pi u)\); its square integral dominates a positive multiple of \(\int_0^{1/4}du/u\). This is an independent check of the divergence in (23). It explains the need for one Green smoothing and the order of limits used above; it is not a defect in the preprint, which explicitly avoids the invalid assertion.

If \(s=t\), (23) also shows that \(R_0(s,s)\) can be infinite. Accordingly (12), (15), and (19) only assert limits for distinct boundary points. The zero reciprocal diagonal in (22) comes from the interior infinite diagonal, not from an assumption that \(R(s,s)\) is finite. The estimates deteriorate when distinct boundary points approach one another; the assertion concerns each fixed finite distinct family.

If \(q=0\), all corrections vanish, and (22) reduces to the radial limit of the bare Green kernel. Repeated boundary points, if subsequently needed, can be combined at the level of coefficients. If \(d=1\), the series bounds fail, and no assertion at that threshold is made. Singular boundary concentrations or atomic interior measures fall outside the bounded-density hypothesis.

The script `check_boundary_limits.py` independently checks the elementary radial formulas, normalizations, Hölder constants and the zero-potential bordered form. Its arithmetic checks supplement the proof; they are not a PDE discretization or a verification of the full manuscript.

The remaining variational and eigenfunction arguments, including the multiplier construction used after the reciprocal-kernel theorem, are not proved here. This boundary lemma neither removes smoothness from OpenAI's hot-spots theorem nor settles the strict arbitrary-convex-boundary row.
