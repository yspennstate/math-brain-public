# B05 QFORM auto18 — hub-retained Fourier shell bound

**Status:** `SUPPORTING_THEOREM_PROVED / POWER_LOSS_REMOVED_TO_LOG^(1/3) / FULL_QFORM_OPEN`.

**Run:** `20260923T221248Z-fleet01-B05-QFORM-auto18`  
**Assignment:** quadratic coarea / equivalent interval bound, preserving the original product source.  
**Exact owner target:** arbitrary independent real coordinates with densities bounded by one and a real symmetric quadratic form having at least three eigenvalues of absolute value at least one.  
**Full target status after this run:** OPEN; neither a full proof nor a counterexample.  
**Continuity status:** not proved for the full target; the result below gives an essentially bounded density only.

## 1. Why this run changes mechanism

The preceding B05 run obtained a punctured-shell estimate for the canonical exact-target family
\[
Q_b=2HL+2bLP+V^2
\]
but still paid a logarithm after summing shells. The current run does not repeat that physical-space annulus mechanism. Instead it keeps the genuinely independent hub variable \(H\) inside the Fourier calculation before taking absolute values. This inserts a factor \(|\widehat f_H(\zeta/b)|\) into the curved-tube integral. Its \(L^2\) mass is \(O(|b|^{1/2})\), which cancels the source theorem's \(|b|^{-1/2}\) Fresnel loss. The only surviving deterioration is a square-root logarithm on the middle Fourier annulus; after the final shell/large-hub optimization this becomes \(\log^{1/3}\).

The argument uses no moment, compact-support, connected-support, log-concavity, Gaussianity, or rotated-coordinate independence assumption.

## 2. Source result used

Use the two-bank curved-tube Fourier setup from

`proofnet24/QFORM-density/interactive/20260923T202245Z-two-bank-curved-tube/REPORT.md`

at source commit

`5e23223ed8626d8df8343d2d26879c08cf139093`.

Let \(A=(L_A,V_A,P_A)\) and \(B=(L_B,V_B,P_B)\) be independent three-dimensional banks, let
\[
(L,V,P)=A+B,
\]
and assume the bank \((L,V)\)-marginal density caps and three-dimensional density caps satisfy
\[
\|m_i\|_\infty\le M_{2,i},\qquad
\|g_i\|_\infty\le M_{3,i}\qquad(i=A,B).
\]
Put
\[
K_2=(M_{2,A}M_{2,B})^{1/2},\qquad
K_3=(M_{3,A}M_{3,B})^{1/2}.
\]
The source defines
\[
S(\zeta)=\int_{\mathbb R^2}
|\phi_A(\xi_l,\xi_v,\zeta)\phi_B(\xi_l,\xi_v,\zeta)|
\,d\xi_l\,d\xi_v
\]
and proves
\[
\tag{2.1} S(\zeta)\le (2\pi)^2K_2,
\qquad
\tag{2.2}\int_{\mathbb R}S(\zeta)\,d\zeta\le(2\pi)^3K_3.
\]
Its Fresnel calculation, on a shell \(r\le |L|\le2r\), gives the factor
\[
\tag{2.3}
C a r^{3/2}|b|^{-1/2}|\zeta|^{-1/2}
\]
after Fourier transforming the transverse shear coordinate \(P\). The present proof keeps the independent hub Fourier factor instead of discarding it.

## 3. New theorem: hub-retained two-bank shell estimate

### Theorem `QFORM-HUB-RETAINED-FOURIER-SHELL-v1`

Let \(H\) be independent of the two banks \(A,B\), with probability density \(f_H\) satisfying
\[
0\le f_H\le m<\infty.
\]
Let \((L,V,P)=A+B\) satisfy the assumptions above. Fix \(0<|b|\le1\). For arbitrary real affine coefficients absorbed into the phase, consider an interval event whose shell reduction has the form
\[
H+bP+c+dL+\frac{\gamma+V^2}{2L}\in[-a,a],
\qquad r\le|L|\le2r,
\]
where \(0<r\le1\). Then there is a universal constant \(C\) such that
\[
\tag{3.1}
\Pr\!\left(
 r\le|L|\le2r,
\left|H+bP+c+dL+\frac{\gamma+V^2}{2L}\right|\le a
\right)
\le C a r^{3/2}G_b,
\]
where
\[
\tag{3.2}
G_b=
K_2+K_2\sqrt{m\log(e/|b|)}+\sqrt{mK_2K_3}.
\]
The constant is independent of \(a,r,b,c,d,\gamma\) and of the supports or moments of all input variables.

In particular, compared with the source shell coefficient \(|b|^{-1/2}\), the entire algebraic singularity in \(b\) is removed.

### Proof

Choose the same shell cutoffs and Gaussian transverse regularizer as in the source curved-tube proof. Let
\[
\theta(u)=e^{1-u^2}\ge1\quad(|u|\le1).
\]
After averaging over \(H\), the shear majorant contains
\[
\kappa_a(z)=\int_{\mathbb R}f_H(h)\,\theta((h+z)/a)\,dh.
\]
With the convention \(\widehat f(\xi)=\int e^{-i\xi x}f(x)\,dx\),
\[
\tag{3.3}
\widehat\kappa_a(\eta)
=a\,\widehat\theta(a\eta)\,\widehat f_H(-\eta).
\]
Therefore Fourier transformation in \(p\) contributes exactly the source factor with one additional multiplier:
\[
\tag{3.4}
\frac a{|b|}\widehat\theta(a\zeta/b)
\widehat f_H(-\zeta/b)
\exp[-i(\zeta/b)F(l,v)].
\]
Running the unchanged Fresnel estimate in \((l,v)\) gives
\[
\tag{3.5}
\sup_{\xi_l,\xi_v}|\widehat W(\xi_l,\xi_v,\zeta)|
\le
C a r^{3/2}|b|^{-1/2}|\zeta|^{-1/2}
|\widehat f_H(\zeta/b)|,
\]
where \(|\widehat\theta|\) has been absorbed into \(C\).

The rough density assumption is exactly enough for Plancherel:
\[
\tag{3.6}
\int_{\mathbb R}|\widehat f_H(\eta)|^2\,d\eta
=2\pi\|f_H\|_2^2
\le2\pi m,
\]
because \(f_H\) has mass one and \(f_H\le m\). Also \(|\widehat f_H|\le1\).

Thus the remaining scalar Fourier integral is
\[
\tag{3.7}
J_b:=\int_{\mathbb R}|\zeta|^{-1/2}
|\widehat f_H(\zeta/b)|S(\zeta)\,d\zeta.
\]
Split it into three regions.

#### Low frequencies: \(0<|\zeta|\le|b|\)

Using \(|\widehat f_H|\le1\) and (2.1),
\[
\tag{3.8}
J_b^{\rm low}
\le C K_2\int_{|\zeta|\le|b|}|\zeta|^{-1/2}\,d\zeta
\le C K_2|b|^{1/2}.
\]

#### Middle frequencies: \(|b|<|\zeta|\le1\)

Again use (2.1), then Cauchy--Schwarz and (3.6):
\[
\begin{aligned}
J_b^{\rm mid}
&\le C K_2
\left(\int_{|b|<|\zeta|\le1}
|\widehat f_H(\zeta/b)|^2\,d\zeta\right)^{1/2}
\left(\int_{|b|<|\zeta|\le1}|\zeta|^{-1}\,d\zeta\right)^{1/2}\\
&\le C K_2\sqrt{m|b|\log(e/|b|)}.
\end{aligned}
\tag{3.9}
\]

#### High frequencies: \(|\zeta|>1\)

Use Cauchy--Schwarz with one copy of \(S\) in each factor:
\[
\begin{aligned}
J_b^{\rm high}
&\le
\left(\int_{|\zeta|>1}
|\widehat f_H(\zeta/b)|^2S(\zeta)\,d\zeta\right)^{1/2}
\left(\int_{|\zeta|>1}|\zeta|^{-1}S(\zeta)\,d\zeta\right)^{1/2}\\
&\le C\sqrt{m|b|K_2K_3},
\end{aligned}
\tag{3.10}
\]
where the first factor uses \(S\le CK_2\), the change of variables \(\zeta=b\eta\), and (3.6), while the second uses \(|\zeta|^{-1}\le1\) and (2.2).

Combining (3.8)--(3.10),
\[
\tag{3.11}
J_b\le C|b|^{1/2}
\left[K_2+K_2\sqrt{m\log(e/|b|)}+\sqrt{mK_2K_3}\right].
\]
Multiplying by the prefactor in (3.5) cancels \(|b|^{-1/2}\) exactly and proves (3.1).

The only regularity point is Fourier justification for rough \(f_H\). It is enough to replace \(f_H\) by the increasing subdensities \(f_H\mathbf1_{[-N,N]}\). Each has mass at most one, \(L^\infty\) norm at most \(m\), and the same estimates (3.6); convolution with the Gaussian \(\theta_a\) is then an admissible rapidly decaying regularization. Letting \(N\to\infty\) and then removing the source Gaussian transverse cutoff by monotone/dominated convergence gives the stated bound. No normalization of the truncated subdensity is needed.

## 4. New global interval consequence for the canonical exact-target family

Let
\[
\tag{4.1}Q_b=2HL+2bLP+V^2,
\]
where \(H\) is independent of \((L,V,P)\), \(0\le f_H\le m\), and the latter is supplied by the two-bank product construction above. For an interval \(I\) of length \(h\), on a dyadic shell \(r\le|L|\le2r\),
\[
Q_b\in I
\]
implies
\[
\left|H+bP+\frac{V^2-y_I}{2L}\right|
\le \frac{h}{4r}
\]
for the interval midpoint \(y_I\). Hence (3.1) with \(a=h/(4r)\) gives
\[
\tag{4.2}
\Pr(Q_b\in I,\ r\le|L|\le2r)
\le C h\,G_b\sqrt r.
\]

Summing over dyadic shells covering \(0<|L|\le R\le1\), using
\[
\sum_{k\ge0}\sqrt{R/2^{k+1}}
=(1+\sqrt2)\sqrt R,
\]
yields
\[
\tag{4.3}
\Pr(Q_b\in I,\ 0<|L|\le R)
\le C_0hG_b\sqrt R.
\]
On \(|L|>R\), condition on every variable except \(H\). Since the derivative of \(Q_b\) with respect to \(H\) is \(2L\),
\[
\tag{4.4}
\Pr(Q_b\in I,\ |L|>R)\le \frac{mh}{2R}.
\]
Therefore
\[
\tag{4.5}
\frac{\Pr(Q_b\in I)}{|I|}
\le A_b\sqrt R+\frac{m}{2R},
\qquad A_b=C_0G_b,
\qquad 0<R\le1.
\]
If \((m/A_b)^{2/3}\le1\), choosing
\[
R=(m/A_b)^{2/3}
\]
gives
\[
\tag{4.6}
\frac{\Pr(Q_b\in I)}{|I|}
\le \frac32 A_b^{2/3}m^{1/3}.
\]
Otherwise choose \(R=1\), giving at most \(A_b+m/2<3m/2\). Consequently
\[
\tag{4.7}
\|p_{Q_b}\|_{\infty,\mathrm{ess}}
\le C\left[m+m^{1/3}G_b^{2/3}\right],
\qquad 0<|b|\le1.
\]
For the cap-one hub \(m=1\) and uniformly bounded two-bank constants \(K_2,K_3\), this is
\[
\tag{4.8}
\boxed{\|p_{Q_b}\|_{\infty,\mathrm{ess}}
\le C_{K_2,K_3}\,[\log(e/|b|)]^{1/3}.}
\]
Thus the previous power deterioration \(|b|^{-1/3}\) and the previous B05 global logarithmic deterioration are both improved to \(\log^{1/3}(e/|b|)\).

### Interval-to-density closure, written explicitly

Equation (4.5), optimized as above, holds for every finite interval \(I\). If \(D_b\) denotes its right-hand constant, every open set \(O\subset\mathbb R\) is a countable disjoint union of intervals, so
\[
\Pr(Q_b\in O)\le D_b|O|.
\]
For a Lebesgue-null Borel set \(E\), choose open \(O\supset E\) with \(|O|<\varepsilon\); then \(\Pr(Q_b\in E)\le D_b\varepsilon\), hence the law is absolutely continuous. Its Radon--Nikodym derivative satisfies \(p_{Q_b}\le D_b\) almost everywhere by Lebesgue differentiation. This closes the interval-to-Borel step without assuming a priori that a density exists.

## 5. Exact-target spectrum check

In the orthonormal coordinate basis \((H,L,P,V)\), the coefficient matrix of (4.1) is
\[
\tag{5.1}
B_b=
\begin{pmatrix}
0&1&0&0\\
1&0&b&0\\
0&b&0&0\\
0&0&0&1
\end{pmatrix}.
\]
The \((H,L,P)\) block has characteristic polynomial
\[
-\lambda(\lambda^2-(1+b^2)),
\]
so
\[
\tag{5.2}
\operatorname{spec}(B_b)
=\{\sqrt{1+b^2},-\sqrt{1+b^2},0,1\}.
\]
Hence **for every real \(b\), including \(b=0\), this family already has three eigenvalues of absolute value at least one.** It is therefore a legitimate exact-target control family, not a low-rank surrogate. The extra two-bank hypothesis restricts the source geometry and is why this theorem is supporting rather than a full solution.

## 6. Mandatory partner application at an actual inequality

At \(b=0\), the family becomes
\[
Q_0=2HL+V^2.
\]
Apply fleet02/B05's completed theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` (report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B05/20260923T200516Z-fleet02-B05-QFORM-auto11c/REPORT.md`). With cap-one hub and the product-projection bound \(\|p_{(L,V)}\|_\infty\le2\) used in the preceding B05 exact-target control, that theorem gives
\[
\tag{6.1}
\boxed{
\|p_{Q_0}\|_{\infty,\mathrm{ess}}
\le 7.761982175235\,2^{2/3}<12.322.
}
\]
Thus the endpoint is uniformly bounded while (4.8) still grows slowly as \(b\to0\). This proves the remaining loss is a defect of the current punctured Fourier interpolation, not a genuine singularity visible at the endpoint.

## 7. Precise missing factor: the middle Fourier annulus

After inserting the independent hub, the low frequencies and high frequencies both have exactly the \(|b|^{1/2}\) gain needed to cancel the Fresnel factor. The only unpaid region is
\[
\tag{7.1}|b|<|\zeta|<1.
\]
There the presently available information is only
\[
\tag{7.2}
S(\zeta)\le CK_2,
\qquad
\int S\le CK_3,
\qquad
\int|\widehat f_H(\zeta/b)|^2d\zeta\le C m|b|.
\]
Cauchy--Schwarz therefore pays
\[
\sqrt{|b|\log(1/|b|)}.
\]
This is sharp at the level of these three abstract norm constraints: on \([|b|,1]\), the profile
\[
F_b(\zeta)
=\sqrt{\frac{|b|}{\log(1/|b|)}}\,\zeta^{-1/2}
\]
has \(L^2\) mass of order \(|b|\), while
\[
\int_{|b|}^1F_b(\zeta)\zeta^{-1/2}\,d\zeta
\asymp\sqrt{|b|\log(1/|b|)}.
\]
This is only an abstract saturation profile, **not** a claim that it is the Fourier transform of an admissible probability density or that it arises from a product bank. It proves that removing the logarithm requires additional structural information beyond (7.2).

The next exact obligation is therefore

`QFORM-HUB-BANK-MIDDLE-ANNULUS-CANCELLATION-v1`:

> Prove a product-sensitive improvement on the middle annulus, ideally
> \[
> \int_{|b|<|\zeta|<1}
> |\widehat f_H(\zeta/b)|\,|\zeta|^{-1/2}S(\zeta)\,d\zeta
> \le C\sqrt{|b|},
> \]
> or replace this absolute-Fourier step by a physical coarea/moving-center estimate. Such an estimate must exploit characteristic-function/product structure not captured by the separate \(L^2/L^\infty/L^1\) norms above.

This is compatible with the live correction that bounded densities may have phase-aligned fragmented supports; no pointwise van-der-Corput decay is assumed.

## 8. Scope and quantifiers

What is proved here:

- arbitrary rough cap-bounded one-dimensional source densities are allowed;
- no moments or support restrictions enter;
- original-coordinate product structure is preserved through the two independent banks and the independent hub;
- for every fixed nonzero \(b\), the displayed exact-target family has a bounded density with the quantitative \(\log^{1/3}\) estimate;
- at \(b=0\), the completed partner theorem gives a uniform constant.

What is **not** proved:

- no uniform constant as \(b\to0\) is obtained by the present interpolation;
- the two-bank balanced/diffuse geometry is not every possible original-coordinate geometry;
- no full general coarea inequality for arbitrary symmetric \(A\) is obtained;
- continuity of the density is not obtained from these interval estimates;
- therefore the owner conjecture remains OPEN.

## 9. Product-source implementation note

When the projected triple \((L,V,P)=U^TY\) comes from independent original coordinates \(Y_j\) with densities bounded by one, any row partition into independent banks whose Gram matrices are uniformly nondegenerate gives finite universal \(K_2,K_3\) via the standard bounded-density projection theorem. This is exactly the same source-preserving hypothesis as in the two-bank curved-tube report. No rotation of the original \(Y_j\) is being declared independent.

## 10. Research status

Result label: `QFORM-HUB-RETAINED-FOURIER-SHELL-v1` plus global corollary `QFORM-HUB-RETAINED-LOG13-DENSITY-v1`.

This is a strict mechanism improvement on the immediately preceding B05 punctured estimate: the singular power of \(|b|\) cancels, and the remaining global degradation is only \(\log^{1/3}(e/|b|)\). The endpoint itself is already uniformly bounded by the partner theorem, so the missing issue is now isolated to one intermediate-frequency annulus and one absent product-sensitive cancellation.
