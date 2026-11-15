# An integrated Gibbs bound for a vacant seam

Let \(d\geq2\). Spheres have diameter one, so distinct centers must be at distance at least one. Let

\[
v_d=\frac{\pi^{d/2}}{\Gamma(1+d/2)},\qquad c_d=2^{-d}v_d.
\]

Activity is denoted by \(z>0\). All logarithms are natural. This result bounds the probability of an entirely vacant rectangular region. It does not bound the probability of a general boundary between two crystal orientations.

## 1. Statement

Let \(S=\prod_{i=1}^d(0,L_i)\), with every \(L_i>0\). Let \(\eta\subset S^c\) be any locally finite diameter-one packing. The conditional partition function is

\[
Z_S^\eta(z)=\sum_{n=0}^\infty\frac{z^n}{n!}
 \int_{S^n}\mathbf1\{\eta\cup\{x_1,\ldots,x_n\}
                  \text{ is a packing}\}\,dx_1\cdots dx_n.       \tag{1}
\]

The indicator includes the requirement that the listed inside points are distinct. The zero-particle term is one, and \(Z_S^\eta(z)\leq e^{z|S|}<\infty\). Write

\[
p_S^\eta(z)=\frac1{Z_S^\eta(z)}.                              \tag{2}
\]

This is exactly the empty-region probability under the hard-sphere conditional Gibbs distribution. The unnormalized Poisson factor \(e^{-z|S|}\), if included in both numerator and denominator, cancels.

Choose \(0<a<1/2\), and set

\[
h=1+2a,\qquad b=v_da^d,\qquad
k_i=\max\left\{0,1+\left\lfloor
                   \frac{L_i-2(1+a)}h\right\rfloor\right\},
\qquad m=\prod_{i=1}^d k_i.                                  \tag{3}
\]

Let

\[
V=\prod_i L_i,\qquad
M=\left\lfloor\frac{\prod_i(L_i+1)}{c_d}\right\rfloor.         \tag{4}
\]

Here \(M\geq1\), since the unit ball lies in the cube of side two, so \(c_d\leq1\), and \(\prod_i(L_i+1)>1\). For \(T>0\), put

\[
U(T,M)=
\begin{cases}
T,&T\leq M,\\
M\bigl[1+\log(T/M)\bigr],&T>M.
\end{cases}                                                  \tag{5}
\]

Uniformly over \(\eta\),

\[
\boxed{\quad
m\log(1+zb)\ \leq\ -\log p_S^\eta(z)
\ \leq\ \log\left[\sum_{n=0}^M\frac{(zV)^n}{n!}\right]
\ \leq\ U(zV,M).
\quad}                                                       \tag{6}
\]

The same bounds hold for the probability that \(S\) is vacant in any finite-volume hard-sphere Gibbs law whose sampling region contains \(S\), with any admissible fixed exterior, and in any infinite-volume hard-sphere Gibbs measure. Thus the constants do not depend on the surrounding finite-volume region.

## 2. Independent insertion regions

More generally, suppose disjoint measurable sets \(B_1,\ldots,B_m\subset S\) have volumes \(b_j>0\), every point of each \(B_j\) has distance at least one from every point of \(\eta\), and every point of \(B_i\) has distance at least one from every point of \(B_j\) when \(i\ne j\). No restriction on pair distances within one \(B_j\) is needed, because only zero or one particle will be inserted there. Restrict (1) to configurations with at most one point in each insertion region and no points elsewhere.

For a fixed subset \(J\subset\{1,\ldots,m\}\) with \(|J|=n\), there are exactly \(n!\) ways to assign the labeled integration variables to its distinct regions. All such configurations are admissible. Their term in (1) is consequently

\[
\frac{z^n}{n!}\,n!\prod_{j\in J}b_j
 =\prod_{j\in J}zb_j.
\]

Different assignments are disjoint, and different subsets give disjoint configurations. Summing proves

\[
Z_S^\eta(z)\geq\sum_{J\subset\{1,\ldots,m\}}
                           \prod_{j\in J}zb_j
                 =\prod_{j=1}^m(1+zb_j).                    \tag{7}
\]

Thus (7) integrates all the selected particle displacements; it does not assign positive measure to a fixed packing configuration.

For (3), use open balls of radius \(a\) centered at the Cartesian grid

\[
(1+a+j_1h,\ldots,1+a+j_dh),\qquad 0\leq j_i<k_i.            \tag{8}
\]

If some \(k_i=0\), there are no balls and the lower bound in (6) is just zero. Otherwise the definition of \(k_i\) puts every center coordinate between \(1+a\) and \(L_i-1-a\), inclusive. Every point in its open ball has each coordinate strictly between \(1\) and \(L_i-1\). Such a point has distance greater than one from \(S^c\), so is compatible with every admissible exterior \(\eta\).

Distinct grid centers are separated by at least \(h=1+2a\). Points in their open balls have distance greater than \(h-2a=1\). The balls are therefore disjoint and meet the hypotheses of (7), each with volume \(b\). Equations (2) and (7) give the first inequality in (6).

## 3. Upper bound on the conditional partition function

If \(n\) admissible centers lie in \(S\), their open radius-\(1/2\) balls are pairwise disjoint. All these balls lie inside \(\prod_i(-1/2,L_i+1/2)\). Comparing volumes gives

\[
nc_d\leq\prod_i(L_i+1),\qquad n\leq M.                     \tag{9}
\]

The constraint imposed by \(\eta\) can only reduce the integral in (1). In each sector the integral is at most \(V^n\). Consequently

\[
Z_S^\eta(z)\leq E_M(zV),\qquad
E_M(T):=\sum_{n=0}^M\frac{T^n}{n!}.                         \tag{10}
\]

For completeness, fix \(0<r\leq1\). Since \(r^{-n}\leq r^{-M}\) for \(n\leq M\),

\[
E_M(T)\leq r^{-M}\sum_{n=0}^M\frac{(rT)^n}{n!}
       \leq r^{-M}e^{rT}.                                  \tag{11}
\]

If \(T\leq M\), choose \(r=1\). If \(T>M\), choose \(r=M/T\). Taking logarithms gives (5) and the last inequality of (6). Combining (2), (7), (10), and (11) proves (6).

A possible sharper cap is

\[
M_* = \left\lfloor\rho_*\prod_i(L_i+1)\right\rfloor,        \tag{12}
\]

where \(\rho_*\) is the unrestricted optimal number density of diameter-one packings. To verify (12), take any finite packing in \(S\) and repeat it with periods \(L_i+1\) in coordinate \(i\). In distinct copies a shifted coordinate differs by more than one, so the result is a packing. Its density \(n/\prod_i(L_i+1)\) is at most \(\rho_*\). Equation (12) follows. The earlier report proved that the periodic and unrestricted density suprema coincide, so this is the same \(\rho_*\). The proof of (10)–(11) works with any positive integer packing cap, in particular \(M_*\). The explicit elementary bound (4) does not require knowing \(\rho_*\).

## 4. Conditioning inside a larger region

In a Gibbs distribution on a bounded region \(\Lambda\supset S\), condition further on the configuration in \(\Lambda\setminus S\). This configuration, together with the fixed configuration outside \(\Lambda\), is an admissible exterior for \(S\). The conditional empty probability is (2), by the Gibbs specification. The bounds in (6) do not depend on that exterior. Exponentiating them and averaging therefore gives the same two bounds for the marginal empty probability. Applying minus logarithm preserves the stated bounds in the stated order.

For an infinite-volume Gibbs measure, the DLR equation gives the same conditional kernel in \(S\) almost surely. The identical averaging argument applies. No translation invariance, uniqueness, boundary regularity beyond the chosen rectangle, or monotonicity in activity is used.

## 5. Surface scaling at fixed seam width

Take

\[
S_{L,W}=(0,L)^{d-1}\times(0,W),\qquad A=L^{d-1},
\]

where \(W\geq2(1+a)\) is fixed. Define

\[
k=\max\left\{0,1+\left\lfloor
                   \frac{W-2(1+a)}h\right\rfloor\right\},
\qquad \alpha=\frac{k}{h^{d-1}}>0,\qquad
\kappa=\frac{W+1}{c_d}.                                    \tag{13}
\]

The elementary inequalities \(x\leq1+\lfloor x\rfloor\leq x+1\), for \(x\geq0\), give \(k_i/L\to1/h\) in the first \(d-1\) coordinates. Therefore

\[
\frac mA\longrightarrow\alpha,\qquad
\frac MA\longrightarrow\kappa,\qquad
\frac{zV}A=zW.                                               \tag{14}
\]

For any sequence of admissible exteriors \(\eta_L\), set
\(H_L=-\log p_{S_{L,W}}^{\eta_L}(z)\). The same conclusions below hold for empty probabilities under finite- or infinite-volume Gibbs laws, even if those laws vary with \(L\). The function in (5), expressed per unit area, is continuous across \(T=M\). Hence (6) and (14) imply

\[
\alpha\log(1+zb)
\leq\liminf_{L\to\infty}\frac{H_L}A
\leq\limsup_{L\to\infty}\frac{H_L}A
\leq
\begin{cases}
zW,&zW\leq\kappa,\\
\kappa[1+\log(zW/\kappa)],&zW>\kappa.
\end{cases}                                                  \tag{15}
\]

No existence of a surface limit is asserted. Dividing the two sides by \(\log z\), and then letting \(z\to\infty\), shows that the lower and upper bounding functions have leading coefficients \(\alpha\) and \(\kappa\). Thus for fixed admissible \(a,W,d\), the cost of a vacant seam is of order area times \(\log z\) at large activity, uniformly in exterior configurations and surrounding volumes. For a literal seam the cost is \(\log Z_S^\eta\); this quantity is not an orientational surface tension.

If (12) is used instead, the upper coefficient \(\kappa\) in (13)–(15) can be replaced by \(\rho_*(W+1)\).

## 6. Insertion sites from a periodic packing

Let \(P\) be any periodic diameter-one packing, with intensity \(\rho_P\). Fix an arbitrary orthogonal matrix \(Q\) and again let \(h=1+2a\). The periodic packing \(hQP\) has separation at least \(h\) and intensity \(\rho_P/h^d\). Define

\[
S^{\ominus(1+a)}=\{x\in S:\operatorname{dist}(x,S^c)>1+a\}.
\]

Uniformly translating \(hQP\) over a lattice fundamental domain gives expected number

\[
\frac{\rho_P}{h^d}\,|S^{\ominus(1+a)}|                      \tag{16}
\]

of its centers in this eroded region. Indeed, integrating the periodic point-counting sum over one fundamental domain tiles \(\mathbb R^d\), once for each representative of the periodic packing. Dividing by fundamental volume gives intensity times the volume of the test region. All summands are nonnegative and the count is finite, so summation and integration can be interchanged.

There exists a phase whose number of centers is at least the floor of (16). Otherwise the integer-valued count would be strictly below that floor everywhere except possibly on a null set, contradicting its expectation. Take these centers and put an open radius-\(a\) ball at each one. Its points have distance greater than one from \(S^c\), and different balls have mutual point distances greater than one. Equation (7) applies. Thus in (6) one may replace \(m\) by

\[
m_P=\left\lfloor\frac{\rho_P}{h^d}
                 |S^{\ominus(1+a)}|\right\rfloor,            \tag{17}
\]

or use the larger of \(m\) and \(m_P\). The two constructions are alternatives; their counts cannot be added. This bound holds for every chosen orientation \(Q\). The phase may depend on the region and the orientation, but compatibility holds with every exterior.

For \(S=S_{L,W}\),

\[
|S^{\ominus(1+a)}|
 =(L-2(1+a))_+^{d-1}(W-2(1+a))_+,
\]

where \(x_+=\max\{x,0\}\). Therefore the lower coefficient in (15) can be improved to the larger of \(\alpha\) and

\[
\alpha_P=\frac{\rho_P}{h^d}(W-2(1+a))_+.                    \tag{18}
\]

This version fills part of the empty seam with independently displaced points of a slightly dilated periodic packing, including the displacement-volume factor \(b\). It requires no assumption that the surrounding particles follow that periodic packing.

## 7. A thin seam can be completely blocked

Uniformity over all admissible exteriors cannot be extended to every positive width with a strictly positive lower cost. In dimension two let

\[
S=(0,L)\times(0,W),\qquad 0<W<\sqrt3/2,
\qquad \eta=\{(j,0):j\in\mathbb Z\}.
\]

This exterior is locally finite, lies in \(S^c\), and has minimum separation one. Given \((x,y)\in S\), choose an integer \(j\) with \(|x-j|\leq1/2\). Then

\[
|(x,y)-(j,0)|^2\leq\tfrac14+y^2
                      <\tfrac14+W^2<1.
\]

Every potential inside center violates exclusion with an exterior center. All positive-particle integrals in (1) vanish, so \(Z_S^\eta(z)=1\) and \(p_S^\eta(z)=1\) for every \(z>0\). This is a counterexample for a claim uniform in boundary configurations; it does not assert that this exact exterior has positive probability under a Gibbs measure.

## 8. Consequence and remaining gap

The earlier construction gave high-density mixing packing laws without a Gibbs weight estimate. Equations (6), (15), and (17) supply such an estimate for a specified completely empty seam, uniformly in volume and boundary conditions. A thick vacant guard region is suppressed at high activity because it admits a family of configurations of positive continuum volume.

An interface between differently oriented dense packings need not contain a vacant rectangular seam wide enough for protected insertion balls. Its displacement integrals can couple particles on both sides, and it may accommodate strain or dislocations without a fixed vacant band. The estimates above do not compare those configurations with a healed interface, establish a Peierls bound, prove orientational order, or settle T080.
