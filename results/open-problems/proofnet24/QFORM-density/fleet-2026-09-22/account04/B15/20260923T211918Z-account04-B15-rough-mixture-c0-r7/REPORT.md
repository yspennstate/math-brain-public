SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B15, 2026-09-23T21:19:18Z.
attacking: rough conditional-convolution trace and the exact upgrade from an L^p/L^q physical fiber certificate to a C_0 density, without pointwise evaluation of arbitrary density versions.

# account04/B15 — rough conditional-convolution trace and C0 compiler

Programme: `QFORM-DENSITY-3EIG-20260922`
Run: `20260923T211918Z-account04-B15-rough-mixture-c0-r7`
Status: **NEW ROUGH-MIXTURE C0 COMPILER + CONCRETE FINITE-Lp STABILITY APPLICATION / FULL QFORM OPEN**
Continuity is kept separate from the universal essential-height problem.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary

Fresh brain control was read in this run. The full target remains: independent original coordinates with probability densities bounded by one, arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, and one dimension-free essential density bound.

The completed designated-partner result used below is account01/B15 at

`math-open-problems@0bb6eb45c2cb78d3d42ba7911905bf2c7eec3f4a`.

It proves that if two product sources `F,G` are both covered by the same law-uniform output-height certificate `M`, then, for every finite `r`,

\[
 \|p_{F,A}-p_{G,A}\|_r
 \le (2M)^{1-1/r}
 \left(\sum_j\|f_j-g_j\|_1\right)^{1/r}.                 \tag{1.1}
\]

This gives strong finite-\(L^r\) rough-source stability, but deliberately does not assert \(L^\infty\) convergence or continuity of the limit.

The completed account04/B15 pivoted-fiber theorem, corrected at

`math-open-problems@cff8e1368d32302e6d649f776579a5c1951929b1`,

states that independent cap-one \(X,Y\) give

\[
 T=aX^2+2bXY+2uX+2vY+c,\qquad b\ne0,
\]
with
\[
 \|p_T\|_p\le p|b|^{-1+1/p},\qquad 1<p<\infty.          \tag{1.2}
\]

The present report supplies the missing rough-mixture trace needed to use such estimates for continuity without selecting pointwise versions of arbitrary densities.

## 2. Rough conditional-convolution theorem

### Theorem 2.1 — `QFORM-ROUGH-CONDITIONAL-CONVOLUTION-C0-v1`

Let \((\Omega,\mathcal F,\pi)\) be a probability space and let \(1<p<\infty\), \(q=p/(p-1)\). For almost every \(\omega\), let \(\mu_\omega,\nu_\omega\) be probability measures on \(\mathbb R\) having densities represented by equivalence classes

\[
 a_\omega\in L^p(\mathbb R),\qquad b_\omega\in L^q(\mathbb R).
\]

Assume the kernels are measurable in the usual weak sense and

\[
 H(\omega):=\|a_\omega\|_p\|b_\omega\|_q\in L^1(\pi).    \tag{2.1}
\]

Let \(\rho\) be the mixture of the convolutions:

\[
 \rho(E)=\int_\Omega(\mu_\omega*\nu_\omega)(E)\,d\pi(\omega).
                                                               \tag{2.2}
\]

Then \(\rho\) has a canonical density \(h\in C_0(\mathbb R)\) satisfying

\[
 \|h\|_\infty\le\int_\Omega H(\omega)\,d\pi(\omega).     \tag{2.3}
\]

No input density is evaluated at a prescribed point. The statement depends only on \(L^p\) and \(L^q\) equivalence classes.

### Proof

For each \(\omega\), define the convolution as the \(L^p*L^q\) pairing

\[
 h_\omega(t)=\int_{\mathbb R}a_\omega(s)b_\omega(t-s)\,ds.       \tag{2.4}
\]

Changing either factor on a null set changes no value of this integral. Hölder gives

\[
 |h_\omega(t)|\le H(\omega).                                    \tag{2.5}
\]

For a translation \(\tau_zb(x)=b(x+z)\),

\[
 |h_\omega(t+z)-h_\omega(t)|
 \le \|a_\omega\|_p\|\tau_zb_\omega-b_\omega\|_q.        \tag{2.6}
\]

Translations are strongly continuous in \(L^q\); hence \(h_\omega\) is continuous. Standard density of compactly supported bounded functions in \(L^p\) and \(L^q\), followed by Hölder, gives \(h_\omega(t)\to0\) as \(|t|\to\infty\). Thus \(h_\omega\in C_0\).

Define

\[
 h(t)=\int_\Omega h_\omega(t)\,d\pi(\omega).              \tag{2.7}
\]

The integrable majorant (2.5) and dominated convergence applied to (2.6) show that \(h\) is continuous. The same majorant and the pointwise fact \(h_\omega(t)\to0\) show \(h(t)\to0\) at infinity. Thus \(h\in C_0\), and (2.3) follows.

It remains to justify that \(h\) is the density of \(\rho\) without any pointwise-density assertion. For every interval \(I\),

\[
\begin{aligned}
 \rho(I)
 &=\int_\Omega\int_{\mathbb R}\int_{\mathbb R}
     {\bf1}_I(x+y)a_\omega(x)b_\omega(y)\,dx\,dy\,d\pi(\omega)\\
 &=\int_I\int_\Omega h_\omega(t)\,d\pi(\omega)\,dt
 =\int_Ih(t)\,dt,                                               \tag{2.8}
\end{aligned}
\]

by Tonelli and the change of variables \(t=x+y\). Intervals determine the measure, proving the claim. QED.

### Remark 2.2 — why an essential bound alone is insufficient

A measurable mixture of essentially bounded densities need not become continuous merely because every conditional law is absolutely continuous. The continuity conclusion above is paid by the genuine \(L^p*L^q\) structure and the integrable norm product (2.1), not by choosing convenient pointwise representatives.

## 3. Application to the pivoted physical branch

Let the independent original-coordinate variables include \(X,Y,Z\). After conditioning on every other original coordinate \(R\), suppose the remaining quadratic form splits as

\[
 Q=T_R(X,Y)+S_R(Z)+c(R),                                        \tag{3.1}
\]

where

\[
 T_R=aX^2+2bXY+2u(R)X+2v(R)Y,\qquad b\ne0,             \tag{3.2}
\]

and

\[
 S_R=\gamma Z^2+2w(R)Z,\qquad \gamma\ne0.              \tag{3.3}
\]

This is an actual original-coordinate separation; no spectral rotation or post-rotation independence is used.

The completed account04/B15 estimate with \(p=3\) gives uniformly in \(R\)

\[
 \|p_{T_R}\|_3\le3|b|^{-2/3}.                            \tag{3.4}
\]

For a cap-one \(Z\), completing the square and using the standard half-power envelope gives

\[
 \|p_{S_R}\|_{3/2}\le2|\gamma|^{-1/3},                   \tag{3.5}
\]

uniformly in the arbitrary affine shift \(w(R)\). Therefore

\[
 \|p_{T_R}\|_3\|p_{S_R}\|_{3/2}
 \le6|b|^{-2/3}|\gamma|^{-1/3}.                          \tag{3.6}
\]

Theorem 2.1 applies with \(\omega=R\). It yields the interval identity

\[
 \Pr\{Q\in I\}=\int_I p_Q(t)\,dt                         \tag{3.7}
\]

for a representative \(p_Q\in C_0(\mathbb R)\), and the full quantitative bound

\[
 \boxed{\;
 \|p_Q\|_\infty\le6|b|^{-2/3}|\gamma|^{-1/3}.
 \;}                                                       \tag{3.8}
\]

This supplies the rough-product trace and limiting justification: rough, fragmented and unbounded marginal densities enter only through their \(L^p\) classes and interval probabilities.

## 4. Concrete use of account01/B15 finite-Lp stability

For the same physical branch, (3.8) is a law-uniform height certificate with

\[
 M=6|b|^{-2/3}|\gamma|^{-1/3}.                            \tag{4.1}
\]

Applying account01/B15 equation (1.1) gives, for any two admissible product sources \(F=\prod f_j\), \(G=\prod g_j\), and every \(1\le r<\infty\),

\[
 \boxed{\;
 \|p_{F,A}-p_{G,A}\|_r
 \le
 \left(12|b|^{-2/3}|\gamma|^{-1/3}\right)^{1-1/r}
 \left(\sum_j\|f_j-g_j\|_1\right)^{1/r}.
 \;}                                                       \tag{4.2}
\]

In particular,

\[
 \boxed{\;
 \|p_{F,A}-p_{G,A}\|_2
 \le2\sqrt3\,|b|^{-1/3}|\gamma|^{-1/6}
 \left(\sum_j\|f_j-g_j\|_1\right)^{1/2}.
 \;}                                                       \tag{4.3}
\]

Thus cap-preserving smooth approximations converge strongly in every finite output \(L^r\). The endpoint \(r=\infty\) is not claimed. Continuity of the rough limiting output is instead supplied directly by Theorem 2.1.

## 5. Smooth approximation and trace, stated correctly

Let \(f_j^{(m)}\) be smooth cap-one probability densities with
\(\sum_j\|f_j^{(m)}-f_j\|_1\to0\). Let \(p_m\) be the output densities. Then:

1. Equation (4.2) gives \(p_m\to p_Q\) in every finite \(L^r\).
2. Each \(p_m\) is continuous, but finite-\(L^r\) convergence alone does not prove continuity of \(p_Q\).
3. The interval identity (2.8), applied directly to the rough factors, identifies the same limit \(p_Q\).
4. The translation estimate (2.6) and dominated convergence prove \(p_Q\in C_0\).

This avoids the invalid step of evaluating an arbitrary density version at a point and avoids any assertion of a target-uniform modulus of continuity.

## 6. Scope and remaining full-target obstruction

Theorem 2.1 is a regularity compiler. It turns any product-preserving conditional \(L^p*L^q\) certificate with an integrable norm-product budget into a continuous \(C_0\) density and the same essential-height bound. It does not create the missing matrix certificate.

The full conjecture remains open because the bare condition \(s_3(A)\ge1\) does not yet force, in original coordinates and with universal constants, either:

- a separated pivoted pair plus independent receiver as in (3.1);
- a uniformly conditioned physical triple;
- a paid cross-bank, ridge, volume or null-pivot branch.

Dense transverse self-couplings may prevent the split (3.1). They cannot be discarded as a small random error under unbounded inputs. Continuity is therefore solved for every branch that supplies the conjugate-\(L^p\) factorization, while the universal essential-height problem remains the structural endpoint.

No moment, support, smoothness, Gaussianity, interval-extremality, post-rotation independence, arbitrary-joint coarea, or pointwise quadratic Fourier-decay assumption is used.
