# QFORM B17: rotational penalties for exact three-bank witnesses

Run: `20260923T073715Z-account01-B17-QFORM-r17`  
Status: `SUPPORTING_SHARP-WITNESS_THEOREMS`; full QFORM remains OPEN / NOT PROVED. Full-target continuity remains separate. Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact source-valid architecture

Let

\[
J=\operatorname{diag}(1,1,-1),\qquad O\in O(3),\qquad v_j=Oe_j.
\]

For positive integers \(m_1,m_2,m_3\), repeat the physical row \(v_j/\sqrt{m_j}\) exactly \(m_j\) times. If \(R\) is the resulting matrix, then

\[
R^TR=\sum_{j=1}^3v_jv_j^T=I_3,
\]

so

\[
A=RJR^T
\]

has nonzero spectrum **exactly** \(\{1,1,-1\}\) for every finite choice of the bank sizes. With independent physical inputs \(X_{jk}\),

\[
Y_j=m_j^{-1/2}\sum_{k=1}^{m_j}X_{jk},\qquad Q=Y^TB Y,\quad B=O^TJO.
\]

All calculations below therefore preserve original-coordinate product provenance. No independence after spectral rotation is used.

The main inputs are the weighted one-dimensional local Edgeworth expansion proved in the exact rotated-witness report

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f:proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`

and the completed account02/B17 finite-bank theorem

`yspennstate/math-open-problems@596288dcf1a153d7ba008dc6fc7d3097d340f37c:proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T045156Z-account02-B17-QFORM-auto11/REPORT.md`.

## 2. Theorem A: arbitrary anisotropic diffuse banks have a positive first-order deficit

Assume every physical input in the three banks is \(\mathrm{Unif}[-1/2,1/2]\), and put \(m_*=\min_jm_j\). Let \(m_*\to\infty\), with no requirement that the three bank sizes have the same rate. Set

\[
u_j=O_{3j}^2,\qquad u_j\ge0,\qquad \sum_j u_j=1.
\]

Then uniformly in \(O\in O(3)\),

\[
\boxed{
 p_Q(0)=3\sqrt2\left[1-D_O(m_1,m_2,m_3)+O(m_*^{-2})\right],
}
\]

where

\[
\boxed{
D_O(m_1,m_2,m_3)=\frac3{640}\sum_{j=1}^3
\frac{19+2u_j-13u_j^2}{m_j}.
}
\tag{2.1}
\]

In particular

\[
\boxed{
D_O\ge \frac3{640}\left(19\sum_j\frac1{m_j}-11\max_j\frac1{m_j}\right)
\ge \frac{3}{80m_*}>0.
}
\tag{2.2}
\]

Hence there is an absolute \(M\) such that whenever all three bank sizes are at least \(M\), every rotation in this exact source-valid family satisfies

\[
p_Q(0)<3\sqrt2.
\]

Thus a finite central-density overshoot cannot be produced asymptotically by arbitrary rotation plus arbitrary anisotropic rates of **three diffuse interval banks**.

### Proof

Write \(\sigma^2=1/12\). The source weighted local Edgeworth lemma gives, with an integrable polynomially weighted remainder,

\[
g_m(y)=\gamma_\sigma(y)
\left[1-\frac1{20m}H_4(y/\sigma)\right]
+O(m^{-2})(1+|y|)^{-8}.
\tag{2.3}
\]

Diagonalize only for the geometric cone calculation. On \(z^TJz=0\), write

\[
z=r(\cos\theta,\sin\theta,\varepsilon),
\quad r>0,\quad \varepsilon\in\{\pm1\},
\]

and put

\[
a_j=(O^T(\cos\theta,\sin\theta,\varepsilon))_j.
\]

The cone coarea measure is \(\tfrac12dr\,d\theta\) on each nappe, and \(\sum_ja_j^2=2\). Under the normalized Gaussian cone measure, \(q=r/\sigma\) satisfies

\[
\mathbb E q^2=\frac12,\qquad \mathbb E q^4=\frac34.
\]

For a fixed column \(j\), averaging over \(\theta,\varepsilon\) gives

\[
\mathbb E a_j^2=\frac{1+u_j}{2},
\]

and

\[
\mathbb E a_j^4
=\frac38(1-u_j)^2+3u_j(1-u_j)+u_j^2
=\frac{3+18u_j-13u_j^2}{8}.
\]

Therefore

\[
\begin{aligned}
\mathbb E H_4(qa_j)
&=\frac34\mathbb E a_j^4
-6\left(\frac12\right)\mathbb E a_j^2+3\\
&=\frac{3}{32}(19+2u_j-13u_j^2).
\end{aligned}
\]

Multiplying the three expansions (2.3), all cross terms and one-dimensional remainder terms are \(O(m_*^{-2})\). Orthogonality makes the leading Gaussian decay \(e^{-12r^2}\), so the weighted cone remainder is uniformly integrable in \(O\). This proves (2.1).

The function \(19+2u-13u^2\) is positive on \([0,1]\). More sharply, if \(w_j=1/m_j\), then \(D_O\) is concave in \(u\) on the simplex, so its minimum occurs at a vertex. At vertex \(k\),

\[
D_k=\frac3{640}\left(19\sum_jw_j-11w_k\right).
\]

The minimum chooses the largest \(w_k\), yielding the first inequality in (2.2); since \(\sum_jw_j\ge\max_jw_j=1/m_*\), the second follows.

### Equal-bank rotation penalty

When \(m_1=m_2=m_3=m\),

\[
\boxed{
D_O=\frac{177-39\sum_ju_j^2}{640m}
=\frac{69}{320m}+\frac{39}{640m}\left(1-\sum_ju_j^2\right).
}
\tag{2.4}
\]

Thus the aligned orientation minimizes the first-order loss. Every genuine mixing of the minority-sign eigendirection creates an explicit extra deficit. For the previously published exact rotation with

\[
\sum_ju_j^2=\frac{199}{343},
\]

(2.4) gives

\[
D_O=\frac{5295}{21952m},
\]

exactly reproducing the independently derived coefficient in the source report. This is a consistency check and a strict extension from equal banks to arbitrary anisotropic bank sizes.

## 3. Theorem B: one arbitrary cap-one heavy law plus two Gaussianized banks cannot hit the central obstruction, for any rotation

Let \(X\) be an arbitrary real random variable with density \(0\le f\le1\), let \(G_2,G_3\) be independent \(N(0,1/12)\), independent of \(X\), and define

\[
Y=(X,G_2,G_3),\qquad Q_O=Y^TO^TJOY.
\]

Then

\[
\boxed{p_{Q_O}(0)<3\sqrt2\qquad\text{for every }O\in O(3).}
\tag{3.1}
\]

Moreover, among all cap-one heavy laws, the central value is maximized by the centered interval law \(X\sim\mathrm{Unif}[-1/2,1/2]\).

This theorem is about the Gaussian-completion limit. It has an exact source-valid finite realization: take one physical row \(v_1\), and \(m\) copies each of \(v_2/\sqrt m\) and \(v_3/\sqrt m\), with the two banks consisting of independent centered unit intervals. The finite matrices again have exact nonzero spectrum \(\{1,1,-1\}\). The source weighted local CLT inserted in the same cone formula gives, for every fixed \(O\) and fixed cap-one heavy law,

\[
p_{Q_{m,O}}(0)\longrightarrow p_{Q_O}(0)<3\sqrt2.
\tag{3.2}
\]

Thus **arbitrary rotation of a one-heavy/two-diffuse exact product construction cannot asymptotically attain the central \(3\sqrt2\) obstruction.**

### Proof of the cap-one reduction

Put \(c_0=\sqrt{6/\pi}\), the density of \(N(0,1/12)\) at zero. In the cone parametrization above, let

\[
a_j=(O^Tw)_j,\qquad w=(\cos\theta,\sin\theta,\varepsilon),
\]

so \(a_1^2+a_2^2+a_3^2=2\). Pair each cone ray \(w\) with its antipode \(-w\). For \(a=|a_1|>0\), the paired radial contribution from the heavy coordinate equals, up to the common Gaussian and coarea prefactors,

\[
\int_0^\infty [f(ar)+f(-ar)]e^{-6(2-a^2)r^2}\,dr
=\frac1a\int_{\mathbb R}f(x)e^{-6(2-a^2)x^2/a^2}\,dx.
\]

The kernel in \(x\) is even and decreasing in \(|x|\). The bathtub principle under \(0\le f\le1\) and \(\int f=1\) therefore puts the mass on \([-1/2,1/2]\). The same centered interval simultaneously maximizes every antipodal ray pair. The exceptional directions \(a=0\) are null in the angular integral and follow by continuity. Hence it is enough to take the centered unit interval.

### Raywise comparison with the fully Gaussian extremal surrogate

For centered uniform \(X\), define

\[
I(a)=\int_0^{1/(2a)}e^{-6(2-a^2)r^2}\,dr,
\qquad 0<a<\sqrt2.
\]

The corresponding third-Gaussian ray integral is

\[
c_0\int_0^\infty e^{-12r^2}\,dr=\frac1{2\sqrt2}.
\]

I claim

\[
\boxed{I(a)\le\frac1{2\sqrt2},\qquad 0\le a\le\sqrt2.}
\tag{3.3}
\]

For \(0<a<\sqrt2\), put

\[
x=\frac{\sqrt{6(2-a^2)}}{2a}.
\]

Then (3.3) is equivalent to

\[
\operatorname{erf}(x)
\le
\frac{2x/\sqrt\pi}{\sqrt{1+2x^2/3}}.
\tag{3.4}
\]

Both sides vanish at zero. The derivative of the right side minus the left side is

\[
\frac2{\sqrt\pi}
\left[(1+2x^2/3)^{-3/2}-e^{-x^2}\right]\ge0,
\]

because

\[
\frac32\log(1+2x^2/3)\le x^2
\]

is exactly \(\log(1+y)\le y\). This proves (3.4), hence (3.3); the endpoints follow by continuity.

The fully Gaussian three-coordinate cone integral is exactly \(3\sqrt2\). Inequality (3.3) compares the uniform-heavy radial integral to the third-Gaussian radial integral **ray by ray**, so it proves \(p_{Q_O}(0)\le3\sqrt2\). Equality in (3.4) for finite \(a\) is strict unless \(x=0\), i.e. \(a=\sqrt2\). A fixed orthogonal column can satisfy \(|a_1|=\sqrt2\) on at most a null set of cone directions. Therefore the angular integral is strictly smaller, proving (3.1).

As a useful exact stress control, when the heavy interval is aligned with the minority-sign spectral direction,

\[
Q=G_1^2+G_2^2-U^2,
\]

and

\[
\boxed{
p_Q(0)=\sqrt{6\pi}\,\operatorname{erf}(\sqrt{3/2})
=3.9801056750420085\ldots<3\sqrt2.
}
\tag{3.5}
\]

This is substantially closer to the obstruction than the diagonal \(\pi\) control, but still leaves a gap of about \(0.262535\).

## 4. Required account02/B17 result applied to an actual inequality

The completed partner theorem at

`math-open-problems@596288dcf1a153d7ba008dc6fc7d3097d340f37c`

handles the aligned one-heavy majority-sign boundary **at every finite bank size and globally in the output level**. In the present notation this is \(O=I\), \((m_1,m_2,m_3)=(1,m,m)\), with an arbitrary cap-one singleton law. It gives

\[
\boxed{
\sup_{m\ge1}\sup_{0\le f\le1,\,\int f=1}
\left\|p_{X_f^2+S_m^2-T_m^2}\right\|_\infty
\le
\frac{\pi\sqrt2}{3}\left(1+\frac4{\sqrt5}\right)
=4.130184516931749\ldots
<3\sqrt2.
}
\tag{4.1}
\]

This is not merely cited: (4.1) pays a boundary regime not covered by Theorem A, because there \(m_*=1\). Together, Theorem A and the partner inequality exclude both the fully diffuse interior and this exact finite one-heavy aligned boundary as mechanisms for an overshoot above \(3\sqrt2\).

## 5. Newest-Claude result applied at its exact scope

The required newest-source chain points to Theorem C in

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

For every exact rank-three signature \((+,+,-)\) target and every \(s\ge0\), it proves

\[
p_Q(s)\le\pi\sqrt2.
\]

Every finite three-bank matrix constructed in Sections 1--3 has exact nonzero spectrum \(\{1,1,-1\}\) and every physical input has density at most one. Therefore the theorem applies directly, giving the actual inequality

\[
\boxed{p_{Q_{m,O}}(s)\le\pi\sqrt2\qquad(s\ge0)}.
\tag{5.1}
\]

Combining (5.1) with Theorem B shows that in the one-heavy/arbitrarily-rotated two-diffuse stress family, the cone tip itself cannot reach \(3\sqrt2\); any unresolved finite-size overshoot would have to occur away from the tip. On the one-sheet side it is at least confined by \(\pi\sqrt2\), while the two-sheet side \(s<0\) remains the genuinely unpaid geometric side. This does not turn Theorem C into a full-rank-three or full-QFORM solution.

## 6. What this says about the sharp witness frontier

The certified universal lower obstruction remains

\[
C_{\rm universal}\ge3\sqrt2,
\]

realized by exact finite diffuse product families approaching the Gaussian cone tip. Theorem A shows that every orthogonal three-bank interval realization approaches this obstruction **from below**, uniformly over rotations and anisotropic diffuse rates, with an explicit first-order deficit. Theorem B shows that retaining one arbitrary cap-one macroscopic law while only two banks diffuse also loses at the central level, regardless of rotation. The partner theorem closes one important finite one-heavy boundary globally.

Consequently a witness above \(3\sqrt2\), if one exists, must use a mechanism outside these paid classes: e.g. two or more genuinely macroscopic non-collinear/shared-coordinate heavy structures, a multiscale/growing-activity construction not reducible to orthogonal bank sums, a coupled non-rank-one tail, or an off-center/two-sheet effect that survives the exact product constraints.

Nothing here proves that \(3\sqrt2\) is the unrestricted universal sharp constant, and nothing here proves full-target continuity.

## 7. Checks and correction discipline

The deterministic arithmetic checker is `check_r17.py`; saved output is `CHECK_OUTPUT.txt`. It verifies the partner gap, the exact reproduction `5295/21952`, the explicit minority-heavy value, and a grid sanity check for the analytic erf inequality. The grid is not used as proof; (3.4) is proved analytically.

Live corrections consumed before publication include the failures of law-uniform pointwise oscillatory decay, post-rotation independence, arbitrary-joint coarea, positive conditional projection-density moments, fixed-fragment localization, single-good-minor/cross-rank extraction, and other current correction-inbox entries. No such refuted premise is used.
