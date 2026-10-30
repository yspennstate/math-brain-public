# B03 QFORM report: critical decoupled-collision hierarchy for cross blocks

Run: `20260922T140943Z-fleet03-B03-QFORM-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
Control snapshot read at brain commit `c930e7c7079b307fbe1783b30bf3c76c408cfd98`.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Status and scope

The full owner conjecture remains OPEN. This report proves a new all-order decoupled time-integral lemma for a physical original-coordinate cross block and quantifies a sharp endpoint defect of the current absolute-value decoupling mechanism.

The only external mathematical premise used is the completed regularized cross-block determinant theorem from the interactive QFORM handoff, canonical math-open-problems commit `a302aab3477c64757b511e80d3907f982e04873a`: for disjoint original-coordinate sets I,J, B=A[I,J], and independent coordinate densities bounded by one,

\[
 |\mathbf E e^{itX^TAX}|\le
 \det\!\left(I+\frac{4t^2}{\pi^2e^2}BB^T\right)^{-1/8}.
\tag{RD}
\]

Its stated scope permits arbitrary self blocks, outside couplings, signs, and additional small singular values. This report applies (RD) only within that scope. The assigned partner `fleet04/B03` had no completed current-QFORM handoff in the fresh brain scan; its visible recent B03 artifacts remained historical FOREST work, so no partner result is fabricated or inherited.

All arguments below preserve independence only in the original coordinates. No rotation of X is made. No conditional density cap for U=X+X' or V=X-X' is used; the correction `QFORM-UV-CONDITIONAL-CAP-FALSE` is respected. No pointwise scalar van-der-Corput claim is used.

## 2. Exact multi-copy identity

Let \(\mu\) be the law of \(Y=Q(X)=X^TAX\), with characteristic function \(\phi(t)\). For \(\varepsilon>0\), let
\[
 p_\varepsilon=\mu*\gamma_\varepsilon,
 \qquad
 \widehat p_\varepsilon(t)=\phi(t)e^{-\varepsilon^2t^2/2}.
\]
For every integer \(m\ge2\), Fourier expansion and Fubini for the Gaussian mollification give
\[
 \int_{\mathbb R}p_\varepsilon(y)^m\,dy
 =\frac1{(2\pi)^{m-1}}
 \int_{\mathbb R^{m-1}}
 \prod_{a=1}^{m}\phi(\alpha_a)
 \exp\!\left(-\frac{\varepsilon^2}{2}\sum_{a=1}^m\alpha_a^2\right)
 dt,
\tag{2.1}
\]
where
\[
 \alpha_a=t_a\quad(1\le a\le m-1),
 \qquad
 \alpha_m=-\sum_{a=1}^{m-1}t_a.
\]
The product of characteristic functions is itself a single quadratic characteristic function:
\[
 \prod_{a=1}^{m}\phi(\alpha_a)
 =\mathbf E\exp\!\left(i\sum_{a=1}^m\alpha_a Q(X^{(a)})\right),
\tag{2.2}
\]
for independent copies \(X^{(1)},\dots,X^{(m)}\). On the stacked original coordinates the quadratic matrix is
\[
 \mathcal A_\alpha=\operatorname{diag}(\alpha_1A,\dots,\alpha_mA).
\]
Thus, for physical disjoint coordinate sets I,J, its corresponding cross block is exactly
\[
 \mathcal B_\alpha=\operatorname{diag}(\alpha_1B,\dots,\alpha_mB).
\tag{2.3}
\]
This is the key decoupled-time construction: dependence inside each sum/difference pair is never discarded; instead one keeps genuinely independent original-coordinate copies.

## 3. Collision majorant from r cross singular directions

Assume B has at least r singular values at least \(\sigma>0\). Put
\[
 a:=\frac{2\sigma}{\pi e},
 \qquad
 f_r(s):=(1+s^2)^{-r/8}.
\]
Applying (RD) to the stacked form (2.2)-(2.3) yields
\[
 \left|\prod_{a=1}^m\phi(\alpha_a)\right|
 \le \prod_{a=1}^m f_r(a\alpha_a).
\tag{3.1}
\]
Therefore
\[
 \|p_\varepsilon\|_m^m
 \le (2\pi a)^{-(m-1)} I_{m,r},
\tag{3.2}
\]
where
\[
 I_{m,r}:=
 \int_{\mathbb R^{m-1}}
 \prod_{a=1}^{m} f_r(s_a)\,ds_1\cdots ds_{m-1},
 \qquad s_m=-\sum_{a=1}^{m-1}s_a.
\tag{3.3}
\]
This is an exact quantitative bridge from a one-time determinant estimate to the complete collision hierarchy. If \(I_{m,r}\le C_0^{m-1}\) uniformly in m, then the mollified densities have \(\|p_\varepsilon\|_m\le C_0/(2\pi a)\) asymptotically uniformly in m, and the standard \(m\to\infty\) argument gives a linear small-ball bound and an \(L^\infty\) density bound.

The endpoint r=4 is the important new case below.

## 4. Exact endpoint r=4: all finite L^m, but factorial collision growth

For r=4,
\[
 f_4(s)=\frac1{\sqrt{1+s^2}}=:f(s),
 \qquad I_{m,4}=f^{*m}(0).
\]
In the Fourier convention \(\widehat f(\xi)=\int e^{-i\xi x}f(x)dx\),
\[
 \widehat f(\xi)=2K_0(|\xi|),
\]
where \(K_0\) is the modified Bessel function. Since \(K_0^m\in L^1(\mathbb R)\) for every \(m\ge2\), approximation by truncations of f gives rigorously
\[
 I_{m,4}
 =\frac1{2\pi}\int_{\mathbb R}(2K_0(|\xi|))^m\,d\xi
 =\frac{2^m}{\pi}\int_0^\infty K_0(x)^m\,dx.
\tag{4.1}
\]
We now prove explicit factorial two-sided bounds.

The integral representation
\[
 K_0(x)=\int_0^\infty e^{-x\cosh u}\,du
\tag{4.2}
\]
implies, for \(0<x\le1\), using \(\cosh u\ge e^u/2\),
\[
 K_0(x)
 \le \int_0^\infty e^{-xe^u/2}du
 =E_1(x/2)
 \le \log(2/x)+e^{-1}.
\tag{4.3}
\]
Writing \(c_0=\log2+e^{-1}\),
\[
 \int_0^1K_0(x)^m dx
 \le\int_0^\infty (u+c_0)^m e^{-u}du
 \le e^{c_0}m!.
\tag{4.4}
\]
For \(x\ge1\), \(\cosh u\ge1+u^2/2\), hence
\[
 K_0(x)\le e^{-x}\sqrt{\frac{\pi}{2x}},
\]
and therefore
\[
 \int_1^\infty K_0(x)^m dx
 \le \left(\sqrt{\pi/2}\right)^m\frac{e^{-m}}m.
\tag{4.5}
\]
For every \(m\ge2\), (4.4)-(4.5) give the convenient bound
\[
 I_{m,4}\le 2^{m+1}m!.
\tag{4.6}
\]

For the reverse estimate, if \(0<x\le1\) and \(0\le u\le\log(1/x)\), then \(x\cosh u\le xe^u\le1\). Thus
\[
 K_0(x)\ge e^{-1}\log(1/x),
\]
so
\[
 \int_0^1K_0(x)^m dx\ge e^{-m}m!,
\]
and hence
\[
 I_{m,4}\ge \frac1\pi\left(\frac2e\right)^m m!.
\tag{4.7}
\]
Thus the absolute decoupled collision majorant has genuinely factorial, not merely exponential, growth at the four-cross-direction endpoint.

Combining (3.2) and (4.6) yields, uniformly in \(\varepsilon>0\),
\[
 \|p_\varepsilon\|_m
 \le 4m\left(\frac{e}{4\sigma}\right)^{1-1/m},
 \qquad m\ge2.
\tag{4.8}
\]
Uniform \(L^m\) weak compactness for each fixed \(m>1\), together with weak convergence \(\mu*\gamma_\varepsilon\Rightarrow\mu\), shows that \(\mu\) has a density p and
\[
 \boxed{
 \|p\|_m
 \le 4m\left(\frac{e}{4\sigma}\right)^{1-1/m}
 \quad\text{for every finite }m\ge2.}
\tag{4.9}
\]
No continuity conclusion follows from (4.9) alone.

## 5. Near-linear small-ball bound with an unavoidable logarithm in this majorant

For an interval E of length h, Holder and (4.9) give
\[
 \mathbf P\{Q\in E\}
 \le4m\left(\frac{eh}{4\sigma}\right)^{1-1/m}.
\tag{5.1}
\]
When \(\delta:=eh/(4\sigma)\le e^{-2}\), choose
\[
 m=\lceil\log(1/\delta)\rceil.
\]
Then \(\delta^{-1/m}\le e\), and
\[
 \boxed{
 \mathbf P\{Q\in E\}
 \le e^2\frac h\sigma
 \left\lceil\log\frac{4\sigma}{eh}\right\rceil.}
\tag{5.2}
\]
Thus four original-coordinate cross singular directions already give an explicit \(h\log(1/h)\) bound using only the decoupled integrated-time method. This is strictly closer to linear scaling than any fixed finite-m Holder estimate.

However, the lower bound (4.7) proves that the *absolute determinant majorant itself* cannot supply the uniform exponential collision bound needed to remove the logarithm: its m-copy collision constants grow like m! up to exponential factors. This is a limitation of this proof mechanism, not a counterexample to QFORM and not a lower bound on the actual density of Q.

## 6. Why this locates the three-direction obstruction

The same hierarchy explains the cross-direction threshold.

* With five cross singular directions, \(f_5(s)=(1+s^2)^{-5/8}\in L^1(\mathbb R)\). Hence
  \[
  I_{m,5}=f_5^{*m}(0)\le \|f_5\|_1^{m-1}\|f_5\|_\infty
  =\|f_5\|_1^{m-1},
  \]
  which is exactly the exponential all-order control that recovers a linear small-ball/density bound. This is consistent with the completed regularized-determinant five-cross-direction branch.

* With four cross directions, every finite collision order is controlled, but only with factorial constants, yielding the logarithmic loss above.

* With three cross directions, the absolute four-copy majorant already diverges. Indeed \(f_3(s)\asymp |s|^{-3/4}\). In (3.3) with m=4, restrict to \(R\le s_1,s_2,s_3\le2R\). Then \(|s_4|\asymp R\), the integrand is \(\asymp R^{-3}\), the box has volume \(\asymp R^3\), and disjoint dyadic R-boxes contribute a fixed positive amount. Hence
  \[
  I_{4,3}=\infty.
  \tag{6.1}
  \]
  In contrast, the three-copy integral is finite: for \(f=f_3\), Young plus Holder gives
  \[
  I_{3,3}=(f*f*f)(0)\le \|f\|_{3/2}^3<\infty,
  \tag{6.2}
  \]
  because \(f^{3/2}=(1+s^2)^{-9/16}\in L^1\). Thus the basic absolute-value determinant route reaches \(L^3\) but stops before the all-order hierarchy needed for linear scaling.

This is a quantitative mechanism diagnosis directly relevant to the owner target: three spectral directions must be converted into more effective integrated smoothing than the unconditional exponent 1/8 supplies, or the proof must retain additional signed/time cancellation rather than taking the absolute determinant majorant copy-by-copy.

## 7. Relation to the q=1 leverage-improved theorem

The same completed regularized-determinant handoff gives, under its q=1 range-leverage hypothesis,
\[
 |\phi(t)|\le \det\!\left(I+\frac{2t^2}{\pi^2e^2}BB^T\right)^{-1/4}.
\]
With three cross singular values this is already \(O(|t|^{-3/2})\), so \(\phi\in L^1\) and the full collision hierarchy has exponential constants. Therefore the new endpoint calculation pinpoints exactly what the leverage improvement accomplishes: it doubles the determinant exponent and jumps from a three-direction four-copy divergence to direct linear small-ball scaling.

The unpaid implication for the unrestricted owner theorem is correspondingly sharp: obtain an equivalent exponent gain/aggregate cancellation from the mere existence of three large eigenvalues in arbitrary orientation, including the heavy-coordinate/nonseparable regime, without assuming a favorable cross block or leverage condition.

## 8. Corrections and nonclaims

Consumed live corrections include `QFORM-CROSSMINOR-ALONE-FALSE`, `QFORM-UV-CONDITIONAL-CAP-FALSE`, `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`, `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE`, `QFORM-FIBERWISE-TRACE-MASS-BOUND-FALSE-v1`, and `QFORM-PHASE-WIENER-AVERAGED-UNIVERSAL-FALSE-v1`. None is bypassed here.

This report does **not** claim that the target hypothesis forces four cross singular values. It does **not** claim that the logarithmic loss is intrinsic to QFORM. It does **not** prove the full three-large-eigenvalue theorem. It supplies a rigorous decoupled-time phase diagram and a new quantitative near-linear branch that exposes the first missing all-order implication.

Continuity of the full target density remains separate and OPEN here.
