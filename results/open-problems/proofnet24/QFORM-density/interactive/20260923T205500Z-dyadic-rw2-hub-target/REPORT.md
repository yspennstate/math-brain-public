# A precise dyadic weak-\(L^2\) target for the remaining canonical QFORM case

**Status:** the restricted weak-\(L^2\) statement below is an **open intermediate lemma**, not a proof. This report proves its equivalence to a conditional-kernel formulation and proves that it would give a dimension-free density cap for the exact one-hub \(a=0\) canonical form. It also proves why strong \(L^2\) is false and why projection caps alone cannot give the lemma.

## The proposed product-source inequality

Let \(H,X_1,\ldots,X_n\) be independent real variables, each with a probability density at most one. Let \(U\in\mathbb R^{3\times n}\) have orthonormal rows and write \((L,V,P)=UX\). For \(\varepsilon,\beta\in\mathbb R\), let
\[
 q(h,L,V,P)=2hL+\beta L^2+V^2+2\varepsilon LP.
\]
The exact \(s_3\ge1\) spectral gate for this canonical matrix is \(|\beta|\le\varepsilon^2\). The proposed inequality is: there is an absolute \(C\) such that, for every \(r\in(0,1/2]\), every finite-measure Borel set \(E\subset\mathbb R\), every interval \(I\subset\mathbb R\), and every \(|\beta|\le\varepsilon^2\),
\[
 \int_E
   \Pr_X\!\left\{r\le|L|\le2r,\ q(h,L,V,P)\in I\right\}\,dh
 \le C\,|I|\,\sqrt{r|E|}. \tag{RW2}
\]
The product origin of \((L,V,P)\) is essential. The same statement with only exact 1D, 2D and 3D projection-density caps is false, as shown below. It is enough to prove (RW2) only for negative intervals \(I\), since the nonnegative targets are already covered by the ruled-line receiver. One may first target \(\beta=0\) and \(|\varepsilon|\ll|s|\ll1\), but that narrower case alone would not finish the canonical spectral gate.

## Why (RW2) proves the canonical density cap

Let \(f_H\le1\) be any probability density, with no support or regularity requirement. For a fixed interval \(I\), put \(E_t=\{h:f_H(h)>t\}\), \(0<t<1\). Layer cake and (RW2) give
\[
 \begin{aligned}
 \Pr\{r\le|L|\le2r,\ q(H,L,V,P)\in I\}
 &=\int_0^1\int_{E_t}
      \Pr_X\{r\le|L|\le2r,\ q(h,L,V,P)\in I\}\,dh\,dt\\
 &\le C|I|\sqrt r\int_0^1\sqrt{|E_t|}\,dt\\
 &\le C|I|\sqrt r.
 \end{aligned}
\]
The last inequality is Cauchy--Schwarz and
\(\int_0^1|E_t|dt=\int f_H=1\). Every \(E_t\) has finite measure for \(t>0\), even if \(H\) has unbounded, fragmented support.

For the dyadic \(r_j=2^{-j-1}\), \(j\ge0\),
\[
 \sum_{j\ge0}\sqrt{r_j}=\frac1{\sqrt2-1}=1+\sqrt2.
\]
On \(|L|\ge1\), integration in \(H\) through derivative \(2L\) gives probability at most \(|I|/2\). Summing the dyadic intervals therefore proves
\[
 \Pr\{q(H,L,V,P)\in I\}
 \le \left(\frac12+(1+\sqrt2)C\right)|I|. \tag{1}
\]
This interval inequality implies an absolutely continuous output law with the same essential density cap. It would settle the complete exact-hub \(a=0\) canonical subclass, uniformly in dimension, leakage, targets, and all source laws. Further structural work is needed to reduce the full arbitrary-matrix conjecture to this subclass.

## Conditional kernel and Lorentz equivalence

Formally, write
\[
 T_{s,r}(h)
   =\int_{r\le|l|\le2r}g(l,v,p)\,
       \delta\!\left(s-2hl-\beta l^2-v^2-2\varepsilon lp\right)
       dl\,dv\,dp,
\]
where \(g\) is the light density. Then \(T_{s,r}(h)\) is the level-\(s\) density for a **fixed** hub value \(h\), restricted to the dyadic \(L\)-strip. The robust definition is the interval inequality (RW2), which avoids choosing conditional density versions.

For almost every \(s\), (RW2) is equivalent up to a factor two in the constant to
\[
 \|T_{s,r}\|_{L^{2,\infty}(dh)}
 :=\sup_{u>0}u\,|\{h:T_{s,r}(h)>u\}|^{1/2}
 \le C\sqrt r. \tag{2}
\]
Indeed, if the restricted estimate \(\int_E T_{s,r}\le C\sqrt r\,|E|^{1/2}\) holds for all finite \(E\), insert \(E=\{T_{s,r}>u\}\) to get (2). Conversely, (2) implies the decreasing rearrangement \(T^*(t)\le C\sqrt{r/t}\), so \(\int_E T\le2C\sqrt{r|E|}\). Lebesgue differentiation in \(s\) on a countable generating algebra of finite-measure \(E\)'s, followed by monotone approximation, passes between this a.e. formulation and (RW2).

The same layer-cake computation proves exactly
\[
 \|f_H\|_{L^{2,1}}
 :=\int_0^\infty t^{-1/2}f_H^*(t)\,dt
 =2\int_0^1|\{h:f_H(h)>u\}|^{1/2}du
 \le2. \tag{3}
\]
This uses only \(0\le f_H\le1\) and \(\int f_H=1\). Thus Lorentz duality gives another route from (2) to the dyadic estimate. The direct layer-cake proof above has the cleaner constant.

## Strong \(L^2\) is false for genuine product inputs

Take \(\varepsilon=\beta=s=0\), \(L=X_1\), \(V=X_2\), \(P=X_3\), with the \(X_i\) independent uniform on \([-1/2,1/2]\). This is an orthonormal product light frame and the canonical quadratic has \(s_3=1\). For \(r\le1/8\) and \(h<0\) sufficiently near zero, both roots of \(2hl+v^2=0\) remain inside the \(V\)-interval, so
\[
 T_{0,r}(h)
 =\int_r^{2r}\frac{dl}{\sqrt{2|h|l}}
 \asymp\frac{\sqrt r}{\sqrt{|h|}}.
\]
This belongs to weak \(L^2(dh)\) at the expected scale but not to strong \(L^2(dh)\), since \(\int_{-\delta}^0 T_{0,r}(h)^2dh=\infty\). A proof relying on a strong-\(L^2\) kernel estimate cannot cover even this elementary admissible case.

## Why all-plane caps fail (RW2)

Use the independently audited dependent-light shell law from the [negative-target projection-cap fake](https://github.com/yspennstate/math-open-problems/blob/master/proofnet24/QFORM-density/interactive/20260923T203400Z-negative-target-projection-fake/REPORT.md). It has an independent cap-one hub, light joint density below one, and all exact numerical product-projection caps, but its light triple is **not** a product projection.

For a base shell \(E_k\) with width \(a_k\), and any dyadic \(r\) with \(a_k\le r\le1/2\), the fixed-hub conditional kernel at \(s=-1\) satisfies
\[
 T_{-1,r}(h)\ge\frac{\log2}{1024}
       \quad\text{for every }h\in I_k.
\]
Indeed, integration in the shell's residual \(P\)-coordinate through the delta constraint contributes \(1/(2l)\), and \(\int_r^{2r}dl/l=\log2\). Set
\(E_r=\bigcup_{k:a_k\le r}I_k\) and \(A(r)=|E_r|=\sum_{a_k\le r}a_k\).
The intervals \(I_k\) are disjoint, so
\[
 \int_{E_r}T_{-1,r}(h)dh
 \ge(\log2/1024)A(r).
\]
For the explicit \(a_k\asymp[k(\log k)^2]^{-1}\), \(A(a_N)\asymp1/\log N\), whereas \(a_N\asymp1/[N(\log N)^2]\). Hence \(A(a_N)/a_N\to\infty\), contradicting the proposed \(C\sqrt{rA(r)}\) bound. The failure is precisely that every dyadic \(L\) scale can use a different faraway \(P\) band and hub center. The same violation persists in the difficult small-leakage regime: for the scaled dependent-light fake with target \(s=-\gamma\), leakage \(\varepsilon\), and physical dyad \(r=\gamma\rho\), every shell with \(a_k\le\rho\) gives \(T_{-\gamma,r}(h)\ge\sqrt\gamma\log2/1024\) on \(I_k\), independently of \(\varepsilon\). Thus \(\|T_{-\gamma,r}\|_{L^{2,\infty}}/\sqrt r\ge(\log2/1024)\sqrt{A(\rho)/\rho}\to\infty\). Any proof of (RW2) must use independent original-coordinate line convolutions or an equivalent product-source property beyond projection caps.

**Open status:** (RW2) is verified for nonnegative targets using the ruled geometry and for several restricted product configurations. Its negative-target, arbitrary-fragmented-support, dimension-free product case remains unproved; no genuine product-source counterexample is known.