# Untwisted independent hub: a diffuse product Fourier corollary

**Status:** proved scoped estimate. The result treats the canonical quadratic \(2HL+V^2\) under a two-frame leverage condition. It does not prove an estimate for the extra coupling \(2\varepsilon LP\) or the unrestricted QFORM density conjecture.

## Statement

Let \(H,X_1,\dots,X_n\) be independent real variables, each with a density bounded by \(1\). Let \(\ell,v\in\mathbb R^n\) be orthonormal, set \(L=\ell\cdot X\), \(V=v\cdot X\), and assume the **full two-frame row leverages**
\[
c_i=\ell_i^2+v_i^2\le\tfrac12\qquad(1\le i\le n).
\]
For arbitrary measurable **separate** source modulations \(\omega_H,\omega_i\) with \(\lvert\omega_H\rvert,\lvert\omega_i\rvert\le1\), write
\[
\Phi_\omega(t)=
\mathbb E\left[\omega_H(H)\prod_{i=1}^n\omega_i(X_i)
  e^{it(2HL+V^2)}\right].
\]
Then, with the convention \(\widehat f(\xi)=\int e^{-i\xi x}f(x)\,dx\),
\[
\boxed{\lvert\Phi_\omega(t)\rvert
\le \min\{1,e\pi^{3/2}\lvert t\rvert^{-3/2}\}
\quad(t\ne0).}                                                   \tag{1}
\]
For the unmodulated real variable \(Q=2HL+V^2\), Fourier inversion gives the continuous density estimate
\[
\boxed{\lVert p_Q\rVert_\infty\le3e^{2/3}<5.85.}             \tag{2}
\]
The estimate applies unchanged after adding any measurable hub-only phase, such as \(aH^2+bH\), and arbitrary original-coordinate affine terms to \(Q\): put their \(t\)-dependent factors into the separate \(\omega\)'s. It also permits an affine light term.

## Proof with constants and regularization

Let \(h=f_H\omega_H\). Its \(L^1\)-norm and essential supremum are at most \(1\). Let \(g(l,v)\) be the complex density of the light projected measure
\[
B\longmapsto\mathbb E\left[\prod_i\omega_i(X_i)
  \mathbf1_{\{(L,V)\in B\}}\right].
\]
Its total variation is at most the law of \((L,V)\), so \(\lVert g\rVert_1\le1\). Its Fourier transform, up to an immaterial sign, is
\[
F(y,z)=\mathbb E\left[\prod_i\omega_i(X_i)e^{i(yL+zV)}\right].
\]
The geometric Brascamp–Lieb and sharp scalar Hausdorff–Young calculation in the companion [diffuse product projection report](REPORT.md), applied to the **two columns** \([\ell\ v]\), proves
\[
\lVert F\rVert_{L^1(\mathbb R^2)}
 \le(2\pi\sqrt e)^2=4e\pi^2.                                  \tag{3}
\]
Hence \(g=(2\pi)^{-2}\int F(y,z)e^{-i(yl+zv)}\,dy\,dz\) almost everywhere, and \(g\) has a bounded continuous representative.

For \(\delta>0\), insert \(e^{-\delta(L^2+V^2)}\) into \(\Phi_\omega(t)\). Fourier inversion of \(g\), Fubini (the Gaussian ensures absolute integrability), and independence of \(H\) express the result as \((2\pi)^{-2}\int F(y,z) B_\delta(t,y) C_\delta(t,z)\,dy\,dz\), where
\[
\begin{aligned}
 B_\delta(t,y)
 &=\int_{\mathbb R}e^{-\delta l^2-i y l}
       \left[\int h(x)e^{i2txl}\,dx\right]dl
  =\int h(x)\sqrt{\frac\pi\delta}\,
       e^{-(2tx-y)^2/(4\delta)}\,dx,\\
 C_\delta(t,z)
 &=\int_{\mathbb R}e^{-\delta v^2+itv^2-izv}\,dv
  =\sqrt{\frac\pi{\delta-it}}\,
       e^{-z^2/[4(\delta-it)]}.
\end{aligned}
\]
The first Gaussian integrates to \(\pi/\lvert t\rvert\) against a function bounded by \(1\). The second has modulus at most \(\sqrt{\pi/\lvert t\rvert}\). Thus (3) gives, uniformly in \(\delta>0\),
\[
\lvert\Phi_{\omega,\delta}(t)\rvert
 \le\frac{4e\pi^2}{(2\pi)^2}
      \frac\pi{\lvert t\rvert}
      \sqrt{\frac\pi{\lvert t\rvert}}
 =e\pi^{3/2}\lvert t\rvert^{-3/2}.
\]
Dominated convergence in the original probability expectation permits \(\delta\downarrow0\). Also \(\lvert\Phi_\omega(t)\rvert\le1\), proving (1). The Fourier \(L^1\)-norm of the real characteristic function is bounded by
\[
2\int_0^\infty\min\{1,e\pi^{3/2}t^{-3/2}\}\,dt
 =6(e\pi^{3/2})^{2/3}.
\]
Multiplication by \((2\pi)^{-1}\) gives (2).

## High-frequency crossover for a genuinely diffuse three-frame

Here is a **conditional proof criterion**, not a proof of its unestablished premise. Suppose additionally \(p\perp\ell,v\), \(\lVert p\rVert=1\), and every full row leverage \(p_i^2+\ell_i^2+v_i^2\le1/2\); put \(P=p\cdot X\). Consider precisely the canonical phase
\[
Q_\varepsilon=aH^2+2HL+V^2+2\varepsilon LP
\]
plus arbitrary original-coordinate affine terms. An extra \(\beta L^2\) is **outside this criterion**, because it prevents the following low-frequency hub/Fresnel reduction without further argument. Define
\[
J(\tau)=\sup_{\lvert\omega_i\rvert\le1}
 \iint_{\mathbb R^2}\left|
 \mathbb E\left[\prod_i\omega_i(X_i)
     e^{i(yL+zV+\tau PL)}\right]\right|\,dy\,dz,
\]
where the supremum is over measurable modulations applied **separately** to the light input coordinates (a stronger premise than merely linear source modulations). The hub density cap and the one-dimensional Fresnel formula yield
\[
\lvert\phi_{Q_\varepsilon}(t)\rvert
 \le \frac{J(2\varepsilon t)}{4\sqrt\pi\,\lvert t\rvert^{3/2}}.
                                                               \tag{4}
\]
Independently, full three-frame diffuse product provenance gives
\(\lVert F_3\rVert_1\le(2\pi\sqrt e)^3\).
For \(\varepsilon\ne0\), Gaussian regularization and Fourier inversion of the signed three-dimensional projected density prove
\[
\lvert\phi_{Q_\varepsilon}(t)\rvert
 \le\frac{e^{3/2}\pi^{3/2}}{\lvert\varepsilon\rvert
                                   \lvert t\rvert^{3/2}}.       \tag{5}
\]
For completeness, the \((p,l)\) Fourier kernel in (5), after Gaussian damping, contains
\[
\int_{\mathbb R} e^{-\delta l^2-iyl}m_t(l)
 \sqrt{\frac\pi\delta}\,
 e^{-(2t\varepsilon l-s)^2/(4\delta)}\,dl,\qquad
m_t(l)=\mathbb E[\omega_H(H)e^{it aH^2+i2tHl}].
\]
Since \(\lvert m_t(l)\rvert\le1\), its absolute value is at most
\(\pi/(\lvert t\varepsilon\rvert)\), uniformly in \(s,y,\delta\).
The \(v\)-Fresnel kernel contributes \(\sqrt{\pi/\lvert t\rvert}\);
the Fourier inverse factor \((2\pi)^{-3}\) and the full-frame
\(L^1\) bound give exactly (5).

**If one proves** \(J(\tau)\le C(1+\lvert\tau\rvert)\) uniformly over all these independent product laws, then (4) on \(1\le\lvert t\rvert\le\lvert\varepsilon\rvert^{-2}\), (5) above that crossover, and \(\lvert\phi\rvert\le1\) below \(1\) show a bound for \(\lVert p_{Q_\varepsilon}\rVert_\infty\) uniform in \(0<\lvert\varepsilon\rvert\le1\). Explicitly,
\[
\lVert p_{Q_\varepsilon}\rVert_\infty
 \le\frac1\pi\left(1+\frac{3C}{2\sqrt\pi}
                         +2e^{3/2}\pi^{3/2}\right).
\]
For \(\lvert\varepsilon\rvert>1\), use (5) above \(t=1\); for
\(\varepsilon=0\), use (2). This statement is restricted to the
canonical displayed light phase; proving the linear \(J\) bound
remains open.

## Sharp scope of the hypothesis

The leverage condition is necessary for this **uniform \(t^{-3/2}\) argument**. Take independent \(H,L,V\sim\mathrm{Unif}[0,1]\), so the two-frame \((L,V)\) has rows of leverage \(1\). Direct integration gives
\[
\mathbb E e^{it(2HL+V^2)}
=\left[\frac1{2it}\int_0^{2t}\frac{e^{iu}-1}{u}\,du\right]
 \left[\int_0^1 e^{itv^2}\,dv\right].
\]
As \(t\to+\infty\), the two brackets have magnitudes asymptotic to \((\log t)/(2t)\) and \(\sqrt\pi/(2\sqrt t)\), respectively. Thus the modulus grows like \((\sqrt\pi/4)t^{-3/2}\log t\), so no fixed universal \(Ct^{-3/2}\) bound holds without a diffuseness assumption.

For the near-coloop leakage model \(2HL+V^2+2\varepsilon LP\), its nonseparable \(LP\) phase destroys the scalar product factorization behind (3). The linear twisted Wiener premise above is genuinely unresolved; (4) and (5) alone do not establish an \(\varepsilon\)-uniform density bound.
