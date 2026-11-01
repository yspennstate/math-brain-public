# Two hubs with arbitrary self-interaction and one transverse square

**Status:** proved dimension-free sufficient theorem. It extends the linear two-hub result to **any** measurable hub self-interaction, including an arbitrary symmetric quadratic block. The three light statistics may be arbitrarily dependent, subject only to a bounded joint density. The unrestricted spectral QFORM conjecture remains **OPEN** because its hypotheses do not automatically yield this physical normal form.

## Main theorem

Let \(H=(H_1,H_2)\in\mathbb R^2\) be independent of \(Z=(Y_1,Y_2,V)\in\mathbb R^3\). Assume \(H\) has a joint probability density \(f_H\le1\), and \(Z\) has a joint probability density \(g\le M\), with \(M<\infty\). No independence among the coordinates *within* either group is needed. Let \(\lambda\ne0\), let \(R:\mathbb R^2\to\mathbb R\) and \(F,G:\mathbb R^2\to\mathbb R\) be arbitrary finite measurable functions, and put

\[
 Q=R(H)+2H\cdot Y+\lambda V^2+2V G(Y)+F(Y).            \tag{1}
\]

Then \(Q\) has a continuous bounded density vanishing at infinity, with

\[
 \boxed{\ \|p_Q\|_\infty
 \le C_*\, M^{2/5}|\lambda|^{-1/5}
 <16\, M^{2/5}|\lambda|^{-1/5}\ },                       \tag{2}
\]
where the explicit analytic constant is
\[
 a_*=\frac{\sqrt{30}\,2^{1/4}}{2(1-2^{-1/4})},
 \qquad C_*=\frac5\pi\left(\frac{\pi a_*}{4}\right)^{4/5}
       =14.6818\ldots .                                 \tag{3}
\]

In particular \(R(H)=H^{\mathsf T}BH+\ell\cdot H+c\) is allowed for **every** symmetric \(2\times2\) matrix \(B\), with constants independent of \(B\), its sign, and its magnitude. Two untouched original cap-one coordinates form a valid \(H\), since their joint density is at most one.

If the light triple is \(Z=TX'\), where \(X'\) has independent cap-one original coordinates and \(T\) is a full-row-rank \(3\times n\) matrix, the product-marginal theorem gives
\[
 M\le \frac{2^{3/2}}{\sqrt{\det(TT^{\mathsf T})}},
 \qquad
 \|p_Q\|_\infty
 <16\left(\frac{8}{|\lambda|\det(TT^{\mathsf T})}\right)^{1/5}. \tag{4}
\]
A nonsingular \(2\times2\) crossing matrix \(C\) in \(2H^{\mathsf T}CY\) can be absorbed into \(\widetilde Y=CY\), replacing \(M\) by \(M/|\det C|\).

## Step 1: reduce the light remainder to a square

The measurable shear
\[
 (y,v)\longmapsto(y,v+G(y)/\lambda)
\]
has Jacobian one on each \(v\)-fiber. It preserves the joint density cap \(M\), the total probability, and independence from \(H\). Completing the square replaces \(F(y)\) by \(F(y)-G(y)^2/\lambda\). Thus it suffices to prove the claim for
\[
 Q=R(H)+2H\cdot Y+\lambda V^2+F(Y),                     \tag{5}
\]
with arbitrary measurable \(R,F\). This works for either sign of \(\lambda\).

Use the Fourier convention \(\widehat a(\xi)=\int e^{i\xi\cdot y}a(y)\,dy\). For \(t\in\mathbb R\), define
\[
 G_t(y)=e^{itF(y)}\int_{\mathbb R}g(y,v)e^{it\lambda v^2}\,dv.
                                                               \tag{6}
\]
Then \(\|G_t\|_1\le1\), and independence of the groups gives
\[
 \varphi_Q(t)=
 \int_{\mathbb R^2} f_H(h)e^{itR(h)}
                   \widehat G_t(2th)\,dh.              \tag{7}
\]
Since \(f_H\le1\) and integrates to one, \(\|f_H\|_2\le1\). For almost every \(t\ne0\) for which \(G_t\in L^2\), Cauchy--Schwarz, two-dimensional Plancherel and the change of variables \(\xi=2th\) give
\[
 |\varphi_Q(t)|
 \le \|f_H\|_2
      \left(\int|\widehat G_t(2th)|^2dh\right)^{1/2}
 = \frac{\pi}{|t|}\,\|G_t\|_2.                           \tag{8}
\]
The factor \(e^{itR(h)}\) has modulus one. This is the reason there is **no** restriction on the hub self-interaction.

## Step 2: a time-averaged square estimate

For almost every \(y\), let \(m_y=\int g(y,v)\,dv\), and push the finite measure \(g(y,v)\,dv\) forward under \(v\mapsto\lambda v^2\); call the resulting measure \(\mu_y\). It has mass \(m_y\). For every interval \(I\) of length \(r>0\),
\[
 \mu_y(I)\le 2M\sqrt{r/|\lambda|}.                       \tag{9}
\]
Indeed, the preimage of any interval of length \(r\) under the positive or negative square map has one-dimensional length at most \(2\sqrt{r/|\lambda|}\). This holds for fragmented and unbounded light laws.

We claim that for every \(T>0\),
\[
 \int_{-T}^{T}\|G_t\|_2^2\,dt
 \le30M\sqrt{T/|\lambda|}.                              \tag{10}
\]
For one fixed \(y\), \(|G_t(y)|=|\widehat\mu_y(t)|\). Since
\(\mathbf1_{\{|t|\le T\}}\le e^{1/4}e^{-t^2/(4T^2)}\), the Gaussian Fourier identity and Tonelli give
\[
 \int_{-T}^{T}|\widehat\mu_y(t)|^2dt
 \le2e^{1/4}\sqrt\pi\,T
   \iint e^{-T^2(s-s')^2}\,\mu_y(ds)\mu_y(ds').           \tag{11}
\]
Fix \(s\) and partition the \(s'\)-axis into consecutive intervals
\([s+k/T,s+(k+1)/T)\), \(k\in\mathbb Z\). Each interval has \(\mu_y\)-mass at most
\(2M/\sqrt{|\lambda|T}\) by (9). The largest Gaussian factor on its interval is at most \(e^{-j^2}\), where \(j=k\) for \(k\ge0\) and \(j=-k-1\) for \(k\le-1\). Since
\[
 2\sum_{j=0}^{\infty}e^{-j^2}<3,\qquad
 2e^{1/4}\sqrt\pi\cdot6<30,
\]
equation (11) is at most \(30M m_y\sqrt{T/|\lambda|}\). Integrate over \(y\) and use \(\int m_y\,dy=1\), proving (10). The phase \(e^{itF(y)}\) does not affect its norm.

This finite integral also shows \(G_t\in L^2\) for almost every \(t\) on each compact frequency interval. Equation (8) is therefore justified almost everywhere; \(\widehat G_t\) is already a bounded continuous function because \(G_t\in L^1\).

## Step 3: dyadic Fourier inversion

For \(T>0\), apply Cauchy--Schwarz to the two-sided shell \(T\le|t|\le2T\). Equations (8) and (10), and \(\int_{T\le|t|\le2T}|t|^{-2}dt=1/T\), give
\[
 \begin{aligned}
 \int_{T\le|t|\le2T}|\varphi_Q(t)|\,dt
 &\le\frac{\pi}{\sqrt T}
       \left(\int_{-2T}^{2T}\|G_t\|_2^2dt\right)^{1/2}\\
 &\le\pi\sqrt{30}\,2^{1/4}
       M^{1/2}|\lambda|^{-1/4}T^{-1/4}.                 \tag{12}
 \end{aligned}
\]
The geometric series of (12) over \(T=2^j T_0\), \(j\ge0\), converges. On \(|t|\le T_0\), use \(|\varphi_Q(t)|\le1\). Hence \(\varphi_Q\in L^1(\mathbb R)\) and inversion gives a continuous \(C_0\) density with
\[
 \|p_Q\|_\infty
 \le\frac{T_0}{\pi}
 +a_* M^{1/2}|\lambda|^{-1/4}T_0^{-1/4}.                \tag{13}
\]
Optimizing at
\(T_0=(\pi a_*M^{1/2}|\lambda|^{-1/4}/4)^{4/5}\)
gives (2)--(3).

## More than two hubs

The same argument works for \(H,Y\in\mathbb R^k\), \(k\ge2\), provided \(H\) is independent of \((Y,V)\), its joint density has cap \(L\), and the joint light density has cap \(M\). An arbitrary measurable \(R(H)\), an arbitrary \(F(Y)\), and \(2VG(Y)\) remain allowed. The \(k\)-dimensional Plancherel step becomes
\[
 |\varphi_Q(t)|\le\pi^{k/2}L^{1/2}|t|^{-k/2}\|G_t\|_2.
\]
The same square energy (10) makes the \(T\)-shell \(O_{k}(\sqrt{LM}\,|\lambda|^{-1/4}T^{3/4-k/2})\), summable for every \(k\ge2\). Optimizing the low-frequency cutoff yields a finite explicit \(C_k\) such that
\[
 \|p_Q\|_\infty
 \le C_k (L M)^{2/(2k+1)}|\lambda|^{-1/(2k+1)}.        \tag{14}
\]
Only the \(k=2\) numerical constant has been optimized above.

## Scope and relation to current work

The recent linear two-hub report, proofnet24/QFORM-density/interactive/20260923T190014Z-two-linear-hubs-square/REPORT.md, uses a pointwise conditional hub-density cap and does not accept \(H^{\mathsf T}BH\). The time-averaged argument (8)--(12) removes that exact obstruction. It does **not** require a pointwise characteristic-function decay estimate uniform over arbitrary fragmented laws: only an integrated dyadic estimate is proved.

To use this theorem in the full QFORM problem one must exhibit two **physical** hub coordinates independent of a light triple of full-rank original-coordinate projections, with a nonzero transverse square and with all remaining light terms fitting \(F(Y)+2VG(Y)\). An arbitrary dense quadratic remainder involving additional light variables is not automatically of that form. Nor does \(s_3(A)\ge1\) alone prove the required quantitative decomposition. Those structural and remainder steps remain open.

**Primary input:** Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), 877--889, Theorem 1.1, for (4). The Fourier/Gaussian energy proof above is self-contained.