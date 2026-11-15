# Near-optimal density with decaying local correlations

All spheres have diameter one. Write \(v_d=\pi^{d/2}/\Gamma(1+d/2)\) for the volume of the unit ball. Intensity means number of centers per unit volume; the corresponding occupied volume fraction is intensity times \(v_d/2^d\).

The following is a quantitative construction of random packings, not a result about Gibbs measures. The qualitative Euclidean absence of a gap between optimal packing density and Poisson-factor packing density is already stated in Section 1.4 of Lewis Bowen, Marcus Michelen, Will Perkins, *A phase transition for the hard sphere model on the hyperbolic plane*, [arXiv:2607.23873](https://arxiv.org/html/2607.23873v1). Independent marks are used below; no identification with an unmarked Poisson factor is needed or asserted.

## 1. Statement

Let \(d\geq2\), and let \(P\subset\mathbb R^d\) be a periodic packing of centers at mutual distance at least one. Let its intensity be \(\rho_P\). For every \(\lambda>0\) there is a stationary, rotation-invariant random packing \(X\) with intensity

\[
\rho_X=\rho_P q_d(t),\qquad
t=(\lambda v_d)^{1/d},\qquad
q_d(t)=d\int_0^\infty u^{d-1}e^{-(u+t)^d}\,du.                 \tag{1}
\]

Set

\[
C_d=(d-1)\Gamma(1-1/d)=d\Gamma(2-1/d).
\]

Then

\[
q_d(t)\geq 1-C_dt,\qquad
\lim_{t\downarrow0}\frac{1-q_d(t)}t=C_d.                    \tag{2}
\]

Here stationarity and mixing refer to translations. More precisely, suppose \(F\) and \(G\) are complex measurable observables, bounded in absolute value by one, depending only on the packing inside \(B(0,a)\). Let \(G_h(X)=G(X-h)\), so that it depends only on \(B(h,a)\). If \(R=|h|>8a\), then

\[
\left|\mathbb E[F G_h]-\mathbb EF\,\mathbb EG_h\right|
\leq 8(1+m)e^{-m},\qquad
m=\lambda v_d(R/4)^d.                                    \tag{3}
\]

Consequently, for every \(\varepsilon\in(0,1)\), such a mixing law exists with intensity at least \((1-\varepsilon)\rho_*\), where \(\rho_*\) is the supremum of packing intensities. The optimal density is a supremum here; no assertion that a mixing law attains it is made.

## 2. Construction and separation

Write \(P=\bigcup_{j=1}^n(p_j+L)\), where \(L\) is a full-rank lattice and the representatives are distinct modulo \(L\). Choose a bounded half-open fundamental parallelepiped \(D\) for \(L\). Thus \(\rho_P=n/|D|\).

Let \(\mathcal Y\) be a homogeneous Poisson process of intensity \(\lambda\). Independently at each nucleus \(y\), choose an orthogonal matrix \(Q_y\) with Haar probability law on \(O(d)\), and a vector \(U_y\) uniform on \(D\). All these marks are independent of \(\mathcal Y\).

For every nucleus define the open region

\[
A_y=\{x:|x-z|-|x-y|>1\text{ for every }z\in\mathcal Y\setminus\{y\}\}.
\]

Place a rotated and translated copy of \(P\) at each nucleus and retain its points only inside this region:

\[
X=\bigcup_{y\in\mathcal Y}
       \left[\bigl(y+Q_y(P+U_y)\bigr)\cap A_y\right].         \tag{4}
\]

The regions are subsets of the nuclei's Voronoi cells. They are defined by the distance gap, not by an assertion that an entire eroded Voronoi cell has this description.

Points retained from the same nucleus have mutual distance at least one. For points \(x\in A_y\) and \(x'\in A_z\) with \(y\ne z\), put \(f(w)=|w-z|-|w-y|\). Both distance functions are one-Lipschitz, so \(f\) is two-Lipschitz. The definitions give \(f(x)>1\) and \(f(x')<-1\). Therefore

\[
2< f(x)-f(x')\leq2|x-x'|,
\]

and \(|x-x'|>1\). Thus (4) is a packing. In particular it is locally finite: disjoint balls of radius \(1/2\) about points in a bounded set fit in its bounded \(1/2\)-neighborhood. The construction is measurable since the input is countable and each acceptance condition is a countable intersection of measurable inequalities.

Translating the nuclei translates (4), with their marks unchanged. Rotating by \(S\in O(d)\) rotates (4) if each mark \(Q_y\) is replaced by \(SQ_y\). The marked Poisson law is unchanged by either operation. This proves stationarity and rotation invariance, including reflections.

## 3. Exact intensity

For any nonnegative integrable \(g\) and a uniform \(U\in D\),

\[
\begin{aligned}
\mathbb E\sum_{p\in P+U}g(p)
 &=\frac1{|D|}\sum_{j=1}^n\sum_{\ell\in L}
                       \int_D g(p_j+\ell+u)\,du\\
 &=\frac n{|D|}\int_{\mathbb R^d}g(x)\,dx.
\end{aligned}                                             \tag{5}
\]

The second equality follows because, for each \(j\), the sets \(p_j+\ell+D\) tile space up to null boundaries. Rotating and translating does not change (5). Conditional on the nuclei, use (5) for the copy in each \(A_y\), and sum by Tonelli. For a bounded Borel set \(B\),

\[
\mathbb E[\#(X\cap B)\mid\mathcal Y]
       =\rho_P\left|B\cap\bigcup_y A_y\right|.              \tag{6}
\]

At a fixed location, let \(R_1<R_2\) be the distances to the closest and second-closest nuclei. These are distinct almost surely. That location is in \(\bigcup_y A_y\) exactly when \(R_2-R_1>1\). Let the probability of this event be \(q\). Stationarity in (6) gives \(\rho_X=\rho_Pq\).

The nearest distance has density

\[
\lambda d v_dr^{d-1}e^{-\lambda v_dr^d},\qquad r>0.
\]

Conditionally on the nearest distance being \(r\), the rest of the Poisson process outside \(B(0,r)\) is unaffected. The conditional probability of no further nucleus up to distance \(r+1\) is

\[
e^{-\lambda v_d[(r+1)^d-r^d]}.
\]

Multiplying and integrating gives

\[
q=\lambda d v_d\int_0^\infty r^{d-1}
                                      e^{-\lambda v_d(r+1)^d}\,dr.
\]

The substitution \(u=(\lambda v_d)^{1/d}r\) proves (1).

As an independent description of the same probability, radial volumes
\(\lambda v_dR_1^d\) and \(\lambda v_dR_2^d\) are the first two arrival times of a rate-one Poisson process on \((0,\infty)\). Thus if \(E_1,E_2\) are independent exponential random variables with mean one,

\[
q_d(t)=\mathbb P\{(E_1+E_2)^{1/d}-E_1^{1/d}>t\}.            \tag{7}
\]

This follows directly since disjoint radial annuli have independent Poisson counts with means equal to their increments of scaled volume.

## 4. Density loss and low-dimensional formulas

Changing variables to \(v=u+t\) in (1) gives

\[
q_d(t)=d\int_t^\infty(v-t)^{d-1}e^{-v^d}\,dv.              \tag{8}
\]

For \(d\geq2\), the integrand vanishes at the lower endpoint before differentiation. Differentiating, justified by domination by an integrable polynomial times \(e^{-v^d}\), gives

\[
-q_d'(t)=d(d-1)\int_t^\infty(v-t)^{d-2}e^{-v^d}\,dv
\leq d(d-1)\int_0^\infty v^{d-2}e^{-v^d}\,dv
=(d-1)\Gamma(1-1/d)=C_d.                                  \tag{9}
\]

Also \(q_d(0)=1\), by the substitution \(w=v^d\). Integrating (9) proves the inequality in (2). Taking \(t\downarrow0\) in (9) by dominated convergence proves its limit. The equality between the two expressions for \(C_d\) follows from \(\Gamma(s+1)=s\Gamma(s)\).

For \(d=2\), splitting \(v-t\) in (8) yields

\[
q_2(t)=e^{-t^2}-\sqrt\pi\,t\operatorname{erfc}(t),
\qquad C_2=\sqrt\pi.                                     \tag{10}
\]

Here \(\operatorname{erfc}(t)=2\pi^{-1/2}\int_t^\infty e^{-v^2}\,dv\).
For \(d=3\), expand \((v-t)^2\) and use \(w=v^3\). With
\(\Gamma(s,x)=\int_x^\infty w^{s-1}e^{-w}\,dw\), this gives

\[
q_3(t)=e^{-t^3}-2t\Gamma(2/3,t^3)+t^2\Gamma(1/3,t^3),
\qquad C_3=2\Gamma(2/3).                                  \tag{11}
\]

For a direct second derivation of the first-order constant, differentiate (1) at zero instead of (8):

\[
-q_d'(0)=d^2\int_0^\infty u^{2d-2}e^{-u^d}\,du
         =d\Gamma(2-1/d)=C_d.                             \tag{12}
\]

Both integrals and both gamma expressions therefore give the same constant independently of the numerical checks.

## 5. Decay of correlations

Fix a window \(B(c,a)\) and a number \(s>0\). Construct an approximation to its output by using only nuclei and their marks in \(B(c,s+2a)\), and otherwise applying exactly rule (4). If there are fewer than two nuclei in this restricted input, set the approximating output to the empty configuration. This is a measurable function of the restricted marked Poisson process and is itself a packing in the window.

On the event that there are at least two nuclei in \(B(c,s)\), this approximation equals the true output in the window. Indeed, for every \(x\in B(c,a)\), those two nuclei are at distances at most \(s+a\), whereas any nucleus outside \(B(c,s+2a)\) has distance at least \(s+a\). The first two nearest distances, and the mark of the nearest nucleus whenever its distance gap exceeds one, are consequently determined by the restricted input. Equal distances at the cutoff do not affect the distance-gap acceptance rule. Hence

\[
\mathbb P\{\text{approximation differs in }B(c,a)\}
\leq p_s=(1+\lambda v_ds^d)e^{-\lambda v_ds^d}.             \tag{13}
\]

Now put \(s=R/4\). When \(R>8a\), the two input balls of radius \(s+2a\) around \(0\) and \(h\) are disjoint. The two approximations, and therefore the observables \(\widetilde F,\widetilde G_h\) evaluated on them, are independent.

Since the observables have absolute value at most one,

\[
\mathbb E|F-\widetilde F|\leq2p_s,\qquad
\mathbb E|G_h-\widetilde G_h|\leq2p_s.
\]

The difference between the two product expectations is at most \(4p_s\), by adding and subtracting \(\widetilde F G_h\). The difference between the products of their means is also at most \(4p_s\). Independence of the approximations proves (3).

This also implies mixing for arbitrary bounded measurable observables of the entire packing. To see this without assuming locality, approximate each observable in \(L^1\) by its conditional expectation given the packing in \(B(0,a)\). These conditional expectations remain bounded by the same bound and converge in \(L^1\) as \(a\to\infty\), since bounded windows generate the configuration sigma-field. The product and mean errors are bounded by the corresponding \(L^1\) errors, uniformly in the translation of the second observable. First let \(|h|\to\infty\) at fixed \(a\), using (3), and then let \(a\to\infty\). This proves translation mixing. In particular the law is translation ergodic: the correlation identity for a translation-invariant event gives \(p=p^2\).

## 6. Approaching the unrestricted packing optimum

Define \(\rho_*\) initially as the supremum of intensities of periodic diameter-one packings. It is positive, since \(\mathbb Z^d\) is a packing, and finite: disjoint radius-\(1/2\) balls centered in a cube of side \(L\) lie in a cube of side \(L+1\), giving at most \((L+1)^d/(v_d/2^d)\) centers.

For any packing \(Z\), keep its centers in the half-open cube \([0,L)^d\), and repeat this finite set with period \((L+1)\mathbb Z^d\). Centers in distinct copies differ by more than one in at least one coordinate: for a nonzero period-coordinate shift, its absolute difference is at least \(L+1\) minus a number strictly less than \(L\). The repeated set is therefore a periodic packing. If \(N_L\) is the original count in the cube, then

\[
\frac{N_L}{(L+1)^d}\leq\rho_*.
\]

The same bound holds for every translated cube. It follows that the upper limiting center density in growing cubes of every packing is at most \(\rho_*\). Conversely a periodic packing has limiting density equal to its intensity. Thus this definition of \(\rho_*\) equals the usual unrestricted supremum of upper limiting densities.

For a stationary random packing of intensity \(\rho\), taking expectations in the same finite-cube bound gives \(\rho L^d\leq\rho_*(L+1)^d\); hence \(\rho\leq\rho_*\). This verifies that the random construction is compared to the same optimum.

Given \(0<\varepsilon<1\), choose a periodic \(P\) with
\(\rho_P\geq(1-\varepsilon/2)\rho_*\), set

\[
t=\frac{\varepsilon}{2C_d},\qquad
\lambda=\frac1{v_d}\left(\frac{\varepsilon}{2C_d}\right)^d,
\]

and apply (2). Then

\[
\rho_X\geq(1-\varepsilon/2)^2\rho_*
          \geq(1-\varepsilon)\rho_*.
\]

For this choice the parameter in (3) is
\(m=(\varepsilon R/(8C_d))^d\). Thus the construction has an explicit density-versus-correlation estimate, without knowing \(\rho_*\).

The grain scale diverges as \(\varepsilon\downarrow0\). The covariance bound is not uniform in this limit. The proof gives no reason for a limiting optimal-density law to remain mixing.

## 7. Orientational observables and the Gibbs obstruction

For a concrete planar observable, let \(S=X\cap B(x,a)\) and \(N=|S|\). Define

\[
\Psi_6(X;x)=
\frac1{\max\{1,N(N-1)\}}
\sum_{\substack{p,q\in S\\p\ne q}}
               \left(\frac{q-p}{|q-p|}\right)^6,
\]

identifying \(\mathbb R^2\) with \(\mathbb C\). This is a bounded local bond-orientation statistic. Rotation about \(x\) by angle \(\theta\) multiplies it by \(e^{6i\theta}\). Rotation invariance forces its mean to be zero. Applying (3) to \(\Psi_6(X;0)\) and \(\overline{\Psi_6(X;h)}\) proves that their correlation tends to zero. More generally all connected correlations of bounded local statistics decay by (3). This is a statement about these packing laws and about fixed local observables; it is not a Gibbs-phase classification.

There is also a direct obstruction to treating the construction as a finite-activity Gibbs law. Suppose \(P\) contains two centers \(p,p'\) at distance exactly one, as do triangular and FCC packings. Choose \(M\) so large that

\[
1+\sup_{u\in D}\max\{|p+u|,|p'+u|\}<M.
\]

Consider the positive-probability Poisson event that there is exactly one nucleus in \(B(0,1)\) and no other nucleus in \(B(0,2M+3)\). For every \(x\in B(0,M)\), the distance to that nucleus is less than \(M+1\), and the distance to any other nucleus is greater than \(M+3\). Its region \(A_y\) therefore contains \(B(0,M)\). The two marked copies of \(p,p'\) lie in this ball for every orientation and phase. Consequently \(X\cap B(0,M)\) has an exact distance-one pair with positive probability.

At any finite activity \(z>0\), the hard-sphere Gibbs specification in a bounded region, conditional on the outside, has density proportional to

\[
\frac{z^n}{n!}\,
\mathbf1\{\text{all hard-core constraints hold}\}
\,dx_1\cdots dx_n
\]

on each particle-number sector. For each \(n\), the set where an inside pair has distance exactly one has Lebesgue measure zero: fix all but one coordinate of the pair and its remaining coordinate lies on a sphere of Lebesgue measure zero; then apply Fubini and the finite union over pairs. Summing the sectors preserves zero probability. Thus no finite-activity Gibbs measure can have the positive-probability contact event above.

For the near-optimal sequence in Section 6, the periodic packings may also be chosen to contain a contact: a periodic packing has an attained positive minimum separation \(b\geq1\), since only finitely many lattice displacements can have bounded length. Scaling it by \(1/b\) creates a contact and increases its intensity. Hence even the near-optimal mixing examples can be certified non-Gibbs in this way.

The construction disproves the implication “sufficiently high density plus stationarity and isotropy force persistent local orientational correlations” for unrestricted packing laws. It does not disprove, or establish, that implication for hard-sphere Gibbs measures. Any use for T080 must supply an additional estimate from the Gibbs specification.
