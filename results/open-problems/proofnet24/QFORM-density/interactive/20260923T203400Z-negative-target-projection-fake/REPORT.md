# Negative-level projection-cap fake at every central target

**Status.** This is a counterexample to a projection-only sufficient lemma. The light triple is dependent and is **not** known to be an orthonormal projection of independent cap-one original coordinates. It is **not** a counterexample to the original product-law QFORM conjecture.

For every fixed \(0<\gamma\le1\), there are an independent cap-one scalar \(H\) and a light triple \(Z_\gamma=(L,V,P)\) with joint probability density \(g_\gamma<1\), obeying every exact numerical 1D, 2D, and 3D orthogonal-projection cap \(2^{d/2}\), while
\[
 Q=2HL+V^2+2LP
\]
has unbounded density in every neighborhood of \(-\gamma\). Its nonzero quadratic singular values are \(\sqrt2,\sqrt2,1\), hence \(s_3(Q)=1\). One can even choose a **single** dependent light law with these projection caps whose output density is essentially unbounded on **every** nonempty open interval inside \((-1,0)\).

## Starting shell construction

Take positive \(a_k<1/4\) with \(\sum_k a_k=1\) and \(\sum_k a_k\log(1/a_k)=\infty\). For example, normalize \(b_k=((k+100)\log^2(k+100))^{-1}\). Choose \(c_k\) by
\[
 c_1\ge100a_1^{-2},\qquad
 c_k\ge100\left(c_{k-1}+\max_{m\le k}a_m^{-2}\right).
\]
Put \(I_k=[c_k-a_k/2,c_k+a_k/2]\) and
\[
 f_H(h)=\sum_k{\bf1}_{I_k}(h).
\]
The intervals are disjoint, so \(f_H\le1\) and \(\int f_H=\sum a_k=1\).

Define
\[
 E_k=\left\{(l,v,p):a_k\le l\le1,\quad0\le v\le1,\quad
 \left|p+c_k+\frac{1+v^2}{2l}\right|\le a_k/2\right\},
 \qquad E=\bigcup_k E_k.
\]
The \(p\)-ranges are disjoint and
\[
 |E_k|=a_k(1-a_k),\qquad S:=|E|=\sum_k a_k(1-a_k)<1.
\]

We use the already audited uniform section lemma for this exact \(E\):
\[
 \sup_{\text{affine lines }\ell}{\cal H}^1(E\cap\ell)\le160,\qquad
 \sup_{\text{affine planes }\Pi}{\cal H}^2(E\cap\Pi)\le160\sqrt2. \tag{1}
\]
For completeness, a single shell has line-section length below \(142\): when the line's \(p\)-direction is at least \(1/2\), use \(t=p+c_k\). The quadratic polynomial \(F(t)=2l(t)t+v(t)^2+1\) satisfies \(F(0)\ge1\), while on the shell \(|F(t)|\le a_kl(t)\). On a dyadic interval \(R\le|t|\le2R\), three separated section points and quadratic interpolation give section \(t\)-measure at most \(\sqrt{216a_kR}\). The geometric dyadic sum is below \(71\), and conversion to arc length costs at most two. If the \(p\)-direction is smaller, the bounded \(l,v\) widths give length below two. When a line hits two separated shells and \(k\) is the largest index, its \(l,v\) slopes relative to \(p\) are at most \(2/c_k\). Each earlier shell is then crossed almost vertically: the derivative of \(p+c_m+(1+v(p)^2)/(2l(p))\) is within \(1/25\) of one, so shell \(m\) contributes at most \(4a_m\) of arc length. Summing gives at most four. A line meeting infinitely many shells must be vertical and contributes at most one. For an affine plane \(\Pi\), choose a horizontal in-plane unit vector \(w\) (so \(w_p=0\)) and a perpendicular in-plane unit vector \(t\). Foliate \(\Pi\) by lines **parallel to \(t\)**, indexed by the transverse coordinate \(x\cdot w\). Each such line meets the whole union \(E\) in length at most \(160\), while \(x\cdot w=w_l l+w_v v\) ranges over an interval of length at most \(|w_l|+|w_v|\le\sqrt2\) on \(0\le l,v\le1\). Fubini therefore gives \({\cal H}^2(E\cap\Pi)\le160\sqrt2\), including nearly vertical planes. The full interpolation and separation bookkeeping is in [the original audited shell report](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T192452Z-independent-hub-all-projections-fake/REPORT.md).

## Contracted shells and exact marginal caps

Fix \(0<\gamma\le1\). Let
\[
 T_\gamma(l,v,p)=(\gamma l,\sqrt\gamma\,v,p),\qquad
 E_\gamma=T_\gamma E,\qquad
 S_\gamma=|E_\gamma|=\gamma^{3/2}S.
\]
Since \(T_\gamma\) is invertible and has operator norm one, its restriction to **every** line or plane is area nonexpanding. For an affine line \(\ell'\) and plane \(\Pi'\),
\[
 {\cal H}^1(E_\gamma\cap\ell')
 ={\cal H}^1(T_\gamma(E\cap T_\gamma^{-1}\ell'))\le160,
\quad
 {\cal H}^2(E_\gamma\cap\Pi')
 ={\cal H}^2(T_\gamma(E\cap T_\gamma^{-1}\Pi'))\le160\sqrt2. \tag{2}
\]
Thus the line X-ray cap \(K=160\) is uniform in \(\gamma\), orientation, offset, and shell index; it applies to the **whole union** \(E_\gamma\), not merely one \(E_{k,\gamma}\).

Let \(\phi_3\) be the standard 3D Gaussian density and set
\[
 g_\gamma(z)=\frac1{512}{\bf1}_{E_\gamma}(z)
      +\left(1-\frac{S_\gamma}{512}\right)\phi_3(z). \tag{3}
\]
It is exactly a probability density, because \(\int{\bf1}_{E_\gamma}=S_\gamma\). Its joint height is at most
\(1/512+(2\pi)^{-3/2}<1\). Orthogonal 2D projection densities are line integrals; orthogonal 1D projection densities are plane integrals. Consequently, by (2),
\[
 \|p_{\pi_2 Z_\gamma}\|_\infty
 \le 160/512+(2\pi)^{-1}<0.472<2,
\]
\[
 \|p_{\pi_1 Z_\gamma}\|_\infty
 \le 160\sqrt2/512+(2\pi)^{-1/2}<0.842<\sqrt2,
\]
and
\[
 \|g_\gamma\|_\infty<1<2\sqrt2. \tag{4}
\]
These are the exact \(2^{d/2}\) numerical LPP caps for all \(d=1,2,3\), with slack. The independent \(H\) still has density cap one.

## Infinite output density at \(-\gamma\)

A point on \(T_\gamma E_k\) has the form
\[
 (L,V,P)=\left(\gamma l,\sqrt\gamma\,v,
       -c_k-\frac{1+v^2}{2l}+r\right),
 \quad a_k\le l\le1,\quad0\le v\le1,\quad |r|\le a_k/2.
\]
For \(h\in I_k\),
\[
 Q=-\gamma+2\gamma l\big((h-c_k)+r\big). \tag{5}
\]
The change of variables \((l,v,r)\mapsto(L,V,P)\) has Jacobian \(\gamma^{3/2}\). Hence the matched \(k\)-shell contribution to the output density is
\[
 p_{k,\gamma}(x)
 =\frac{\sqrt\gamma}{512}\int_{a_k}^1
       \frac{\big(a_k-|x+\gamma|/(2\gamma l)\big)_+}{2l}\,dl. \tag{6}
\]
At the target,
\[
 p_{k,\gamma}(-\gamma)
 =\frac{\sqrt\gamma\,a_k}{1024}\log(1/a_k).
\]
The sum over \(k\) diverges for every fixed \(\gamma>0\). Each finite sum of the nonnegative \(p_{k,\gamma}\) is continuous near \(-\gamma\), so arbitrarily large partial sums remain large on a nonempty interval. Therefore this is failure of the **essential** density cap, independent of the choice of density version. The Gaussian filler contributes a nonnegative density and does not alter the lower bound.

Finally, enumerate the rational numbers in \((0,1)\) as \(\gamma_j\) and choose weights \(w_j>0\) summing to one. The single density \(g_*=\sum_j w_jg_{\gamma_j}\) is normalized. Its projection caps follow by convexity from (4). More explicitly, its shell part has line X-ray at most
\(\sum_jw_j(160/512)=160/512\), and its Gaussian part has line marginal height at most \((2\pi)^{-1}\); the analogous plane bound is \(160\sqrt2/512+(2\pi)^{-1/2}\). Keep the same independent \(H\). The output law is \(\sum_jw_j\operatorname{Law}(Q_{\gamma_j})\), so its density is essentially unbounded in every neighborhood of every \(-\gamma_j\), hence on every nonempty open interval in \((-1,0)\).


## Exact placement in the small-leakage gap

The same construction works for the coefficient range that remains hardest in the genuine-product problem. For every \(\varepsilon\), the quadratic matrix of \(2HL+V^2+2\varepsilon LP\) has nonzero singular values \(\sqrt{1+\varepsilon^2},\sqrt{1+\varepsilon^2},1\), so it meets the exact \(s_3=1\) spectral gate. Fix \(0<\varepsilon\le1\) and \(0<\gamma\le1\), with no restriction on the ratio \(\gamma/\varepsilon\). Put
\[
 T_{\gamma,\varepsilon}(l,v,p)
       =(\gamma l,\sqrt\gamma\,v,p/\varepsilon),
 \qquad E_{\gamma,\varepsilon}=T_{\gamma,\varepsilon}E,
\]
and define
\[
 g_{\gamma,\varepsilon}(z)
   =\frac{\varepsilon}{512}{\bf1}_{E_{\gamma,\varepsilon}}(z)
     +\left(1-\frac{\gamma^{3/2}S}{512}\right)\phi_3(z). \tag{7}
\]
This is exactly normalized:
\(|E_{\gamma,\varepsilon}|=\gamma^{3/2}S/\varepsilon\), so the shell mass is \(\gamma^{3/2}S/512\).

The largest singular value of \(T_{\gamma,\varepsilon}\) is \(1/\varepsilon\); its largest 2D area expansion is \(\sqrt\gamma/\varepsilon\). Applying the original section bounds (1) to preimage lines and planes gives the **whole-union** estimates
\[
 \sup_\ell{\cal H}^1(E_{\gamma,\varepsilon}\cap\ell)
       \le160/\varepsilon,\qquad
 \sup_\Pi{\cal H}^2(E_{\gamma,\varepsilon}\cap\Pi)
       \le160\sqrt{2\gamma}/\varepsilon.
\]
After multiplying by the shell coefficient \(\varepsilon/512\), the 2D projection shell cap is again \(160/512\), the 1D cap is at most \(160\sqrt2/512\), and the 3D shell height is at most \(1/512\). The same Gaussian calculations as (4) give the exact numerical \(2^{d/2}\) caps for every \(d=1,2,3\), uniformly in both parameters.

With the same independent hub, the quadratic
\[
 Q_\varepsilon=2HL+V^2+2\varepsilon LP
\]
equals \(\gamma Q_1\) on the image of each base shell. The Jacobian and shell coefficient cancel the \(1/\varepsilon\) expansion, so the matched density contribution at \(-\gamma\) remains exactly
\[
 p_{k,\gamma,\varepsilon}(-\gamma)
 =\frac{\sqrt\gamma\,a_k}{1024}\log(1/a_k).
\]
Its sum is infinite. Therefore projection-only assumptions fail even in the double-scale regime \(\varepsilon\ll\gamma\ll1\) where the original-product proof is still missing. This section, like the rest of the report, is a **dependent-light surrogate only**.


## The exact dyadic loss behind the fake

For the base shell \(E_k\), take a dyadic \(r\) with \(a_k\le r\le1/2\). At the target \(-1\), the contribution from its matched hub interval and \(r\le L\le2r\) is
\[
 D_{k,r}(-1)=\frac1{512}\int_r^{2r}\frac{a_k}{2l}\,dl
              =\frac{a_k\log2}{1024}. \tag{8}
\]
It is **independent of \(r\)**. There are order \(\log(1/a_k)\) such scales, giving \(a_k\log(1/a_k)\). The 2D \((L,P)\) cap does not charge repeated use of those scales: as \(l\) changes, the shell center moves along
\[
 p=-c_k-\frac{1+v^2}{2l},
\]
to different, increasingly distant \(P\) bands. Its graph can satisfy all line X-ray bounds while saturating (8) at every dyadic \(l\) scale. The independent hub supplies a window of length \(a_k\), and the coarea factor \(1/(2l)\) exactly cancels the dyadic \(l\)-width.

For an actual orthonormal product projection, the light density is a convolution of independent measures supported on the physical row directions. A product-only replacement would need to prevent these independent line contributions from tracking the curved \(P\)-versus-\((L,V)\) graph at every scale. A sufficient dyadic goal is
\[
 D_r(-\gamma)\le C r^\alpha
\]
for some absolute \(\alpha>0\), uniformly in \(\varepsilon,\gamma\), when the light frame admits two full-rank independent banks with uniform density caps. Then the dyadic sum is bounded. The published two-bank Fourier theorem proves a \(\sqrt{r/|\varepsilon|}\) estimate at small \(r\) and a fixed-negative-target logarithmic bound, but it does not establish this uniform dyadic goal for \(r\gg\gamma\gg|\varepsilon|\). This is a proposed intermediate lemma, **not a proved bound**.

**Logical scope.** The correlations in \(g_\gamma\) encode the quadratic shell graph. Passing all one-, two-, and three-dimensional marginal caps, even with a cap-one independent hub, does not give the original product representation. This result isolates a real obstacle to the negative-level proof and says nothing adverse about the original product-law conjecture.