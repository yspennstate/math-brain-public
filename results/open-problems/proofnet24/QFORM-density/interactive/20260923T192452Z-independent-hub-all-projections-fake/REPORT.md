# An independent hub and all low-dimensional projection caps still do not prove the leakage endpoint

**Status:** proved counterexample to a proposed *projection-only analytic lemma*. The light triple below is dependent and is **not shown to be a linear image of independent original inputs**. This is **not a counterexample to the original product-law QFORM conjecture**.

## Claim and normalization

There are an independent scalar \(H\) of probability density at most one and a light triple \(Z=(L,V,P)\) with a joint probability density \(g\le1\), such that **every orthogonal 1-, 2-, and 3-dimensional projection of \(Z\)** obeys the exact numerical Livshyts--Paouris--Pivovarov caps
\[
 \|p_{\pi_dZ}\|_\infty<2^{d/2},\qquad d=1,2,3,
 \tag{1}
\]
but
\[
 Q=2HL+V^2+2LP
 \tag{2}
\]
has an unbounded output density. Its quadratic matrix, in the order \((H,L,V,P)\), has eigenvalues \(\sqrt2,-\sqrt2,1,0\), so \(s_3=1\).

Consequently, even the full hierarchy of projection-density inequalities, an independent original-coordinate hub, and a bounded 3D light density are insufficient to establish the proposed leakage receiver. The actual product provenance of \((L,V,P)\) must enter any proof of the full conjecture.

## The hub and the separated light shells

Choose \(a_k\in(0,1/4)\) with
\[
 \sum_{k\ge1}a_k=1,
 \qquad \sum_{k\ge1}a_k\log(1/a_k)=+\infty.
 \tag{3}
\]
One explicit choice is \(a_k=b_k/\sum_{j\ge1}b_j\), where
\(b_k=[(k+100)(\log(k+100))^2]^{-1}\).
The sum of \(b_k\) converges and the entropy sum in (3) diverges. The initial shift by 100 makes \(\max a_k<1/4\).

Choose \(c_k>0\) recursively so rapidly increasing that
\[
 c_1\ge100a_1^{-2},\qquad
 c_k\ge100\left(c_{k-1}+\max_{m\le k}a_m^{-2}\right)
 \quad(k\ge2).                                             \tag{4}
\]
Put \(I_k=[c_k-a_k/2,c_k+a_k/2]\). The disjoint intervals \(I_k\) define the cap-one probability density
\[
 f_H(h)=\sum_{k\ge1}\mathbf1_{I_k}(h).                       \tag{5}
\]

For each \(k\), define
\[
 E_k=\left\{(l,v,p):
 a_k\le l\le1,\quad 0\le v\le1,\quad
 \left|p+c_k+\frac{1+v^2}{2l}\right|\le\frac{a_k}{2}
 \right\}.                                                   \tag{6}
\]
Its volume is \(a_k(1-a_k)\). The \(p\)-ranges of these sets are disjoint by (4), and
\(S=\sum_k|E_k|=\sum_k a_k(1-a_k)<1\).
Let \(\phi_3\) be the standard three-dimensional Gaussian density and set
\[
 g(z)=\frac1{512}\sum_{k\ge1}\mathbf1_{E_k}(z)
       +\left(1-\frac S{512}\right)\phi_3(z).
 \tag{7}
\]
This is a probability density, positive and bounded by
\(1/512+(2\pi)^{-3/2}<1\). Take \(H\) independent of \(Z\).

## Uniform line-section bound

We prove that every affine line meets \(E=\bigcup_kE_k\) in one-dimensional length at most \(160\). Line integrals of \(\mathbf1_E\) therefore have this same cap, uniformly over the position and orientation of the line.

First fix one shell \(E_k\), abbreviating \(a=a_k\) and \(c=c_k\). Parameterize a unit-speed line as
\((l(s),v(s),p(s))\), with direction \(d\). If \(|d_p|<1/2\), one of \(|d_l|,|d_v|\) is at least \(\sqrt{3/8}\). Since every shell lies in \(0\le l,v\le1\), the entire section has length below \(2\).

If \(|d_p|\ge1/2\), use \(t=p+c\) as the line parameter and define the quadratic polynomial
\[
 F(t)=2l(t)t+v(t)^2+1.
\]
At the *extrapolated* point \(t=0\), \(F(0)=1+v(0)^2\ge1\). On \(E_k\), \(|F(t)|\le a\,l(t)\). Its defining relation and \(a\le1/4\) imply
\[
 3/8\le|t|\le2/a,\qquad
 \frac{3}{8|t|}\le l(t)\le\frac{9}{8|t|}.                    \tag{8}
\]
In a dyadic range \(R\le|t|\le2R\), therefore,
\(|F(t)|\le9a/(8R)\). Let \(m_R\) be the measure of the \(t\)-section of this range. If \(m_R>0\), choose three points of that measurable section with pairwise gaps at least \(m_R/4\) (using its first, middle, and last measure quantiles). Each point has modulus at most \(2R\). Lagrange interpolation at zero bounds
\[
 1\le F(0)
 \le 3\cdot\frac{9a}{8R}\cdot\frac{(2R)^2}{(m_R/4)^2}
 =\frac{216aR}{m_R^2}.
\]
Thus \(m_R\le\sqrt{216aR}\). Summing the geometric dyadic series for \(1/4\le R\le2/a\) gives a total \(t\)-section below
\[
 \frac{\sqrt{432}}{1-2^{-1/2}}<71.
\]
Because \(|d_p|\ge1/2\), the actual unit-speed section has length below \(142<160\).

It remains to bound a line that meets *several* shells; merely summing the previous bound would fail. Suppose the largest shell index hit is \(k\), and another hit has index \(j<k\). A point of \(E_m\) has
\[
 -c_m-\frac1{a_m}-\frac{a_m}{2}
 \le p\le -c_m-\frac12+\frac{a_m}{2}.
\]
The separation (4) makes the \(p\)-distance between the chosen points at least \(c_k/2\). Since all their \(l,v\) coordinates lie in \([0,1]\), their common line obeys
\[
 \left|\frac{dl}{dp}\right|,
 \left|\frac{dv}{dp}\right|\le\frac2{c_k}.                  \tag{9}
\]
For any \(m\le k\), consider along this line
\[
 D_m(p)=p+c_m+\frac{1+v(p)^2}{2l(p)}
\]
where \(a_m\le l\le1\) and \(0\le v\le1\). Differentiation and (9) give
\[
 |D_m'(p)-1|
 \le\frac{|v'|}{a_m}+\frac{|l'|}{a_m^2}
 \le\frac4{c_k a_m^2}<\frac1{25}.                           \tag{10}
\]
The feasible set \(a_m\le l(p)\le1,\ 0\le v(p)\le1\) is an interval. Throughout it \(D_m'\ge1/2\), and \(E_m\) also requires \(|D_m|\le a_m/2\). Hence this shell occupies at most \(2a_m\) in \(p\), or \(4a_m\) in unit-speed line length. Summing over \(m\le k\) bounds the complete section by \(4\sum a_m\le4\). If a line meets infinitely many shells, (9) along an unbounded sequence of \(k\) forces \(l'=v'=0\), so it is vertical in \(p\); its full section has length at most \(\sum a_m=1\). Combining these cases proves the uniform constant \(160\).

## Exact projection caps

A 2D orthogonal projection of \(\mathbf1_E\) has density equal to its fiber-line integral, hence at most \(160\). For a plane section, choose a unit vector in the plane with zero \(p\)-component. Foliating the plane by lines perpendicular to that vector, the transverse coordinate is a linear combination of \(l,v\) and spans at most \(\sqrt2\), since \(0\le l,v\le1\). The line-section bound gives plane area at most \(160\sqrt2\). This proves all 1D projection caps of \(\mathbf1_E\) as well.

The Gaussian terms in the 1D and 2D marginals have respective heights at most \((2\pi)^{-1/2}\) and \((2\pi)^{-1}\). Therefore (7) satisfies
\[
 \begin{aligned}
 \|p_{\pi_1 Z}\|_\infty
 &\le160\sqrt2/512+(2\pi)^{-1/2}<0.842<\sqrt2,\\
 \|p_{\pi_2 Z}\|_\infty
 &\le160/512+(2\pi)^{-1}<0.472<2,\\
 \|g\|_\infty
 &\le1/512+(2\pi)^{-3/2}<1<2\sqrt2.
 \end{aligned}                                               \tag{11}
\]
The numeric normalizations in the projection-only proposed lemma are thus met with room to spare.

## Divergent output density

On the \(k\)-th shell write
\[
 p=-c_k-\frac{1+v^2}{2l}+r,\qquad |r|\le a_k/2.
\]
For \(h\in I_k\), equation (2) reduces exactly to
\[
 Q=-1+2l\bigl((h-c_k)+r\bigr).
\]
The \(k\)-th matched contribution to the density at \(-1\) is
\[
 \frac1{512}\int_{a_k}^1dl\int_0^1dv
       \int_{-a_k/2}^{a_k/2}\frac{dr}{2l}
 =\frac{a_k}{1024}\log(1/a_k).                              \tag{12}
\]
Summing (12) diverges by (3).

This is an **essential-supremum** failure, not a choice of density version at one point. For fixed \(k\), the matched contribution at \(x\) near \(-1\) has the explicit continuous triangular-density formula
\[
 p_k(x)=\frac1{512}\int_{a_k}^1
   \frac{\bigl(a_k-|x+1|/(2l)\bigr)_+}{2l}\,dl.
\]
Every finite partial sum of the nonnegative \(p_k\) is continuous and has an arbitrarily large value at \(-1\) as more terms are included. It consequently stays large on a nonempty interval. Thus \(\|p_Q\|_\infty=+\infty\). The independent hub and the Gaussian filler cannot decrease this lower bound.

**Logical boundary:** Equation (7) deliberately correlates \(L,V,P\). Passing all LPP marginal numerical tests does not imply that it is an orthonormal projection of a product law. No such realization is claimed; the unrestricted spectral QFORM conjecture remains open.