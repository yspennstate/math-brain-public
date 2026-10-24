SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B01, 2026-09-24T12:09:45Z.
attacking: the first unproved joint averaged-frequency estimate — replace a scalar bounded modulation density by an arbitrary dependent k-dimensional slope density in L^r, while retaining all deterministic cross-curvature among the original physical hubs.

# Joint L^r slope modulation theorem

## Status

**NEW SUPPORTING JOINT AVERAGED-FREQUENCY THEOREM / STRICT FULL-TARGET CHAMBER / COMPLETED ACCOUNT01-B01 PLANCHEREL ENDPOINT APPLIED / FULL QFORM OPEN.**

The unrestricted universal bounded-density conjecture remains open. This report proves a new product-coordinate chamber and keeps continuity separate.

## 1. Completed account01/B01 input

The completed account01/B01 report
\`dd9bdc8f347ef1849cb1647964d19d014843f877\`
proves the curvature-uniform scalar modulation identity
\[
\int_{\mathbb R}|G_{a,w}(t)|^2\,dw
\le \frac{\pi}{|t|},
\tag{1.1}
\]
for a cap-one physical density, irrespective of its scalar quadratic curvature. It then obtains
\[
|\phi(t)|\le \min\{1,\sqrt{\pi M/|t|}\}
\tag{1.2}
\]
when the random scalar modulation has density cap \(M\).

The present result uses (1.1) as the \(L^2\) endpoint of a joint Fourier operator and interpolates it before any pointwise reciprocal coefficient is taken. No uniform pointwise decay for a fixed quadratic phase is asserted.

## 2. Main theorem

### Theorem \`QFORM-B01-JOINT-LR-MODULATION-v1\`

Let \(k\ge2\). Let
\[
H=(H_1,\ldots,H_k)
\]
be genuine independent original coordinates, independent of an arbitrary environment \(Y\), and assume every \(H_j\) has a probability density bounded by one.

Let \(C\) be an arbitrary deterministic symmetric \(k\times k\) matrix. Let \(L=L(Y)\in\mathbb R^k\) have a joint Lebesgue density \(p_L\in L^r(\mathbb R^k)\), where
\[
1<r\le2.
\]
No independence among the coordinates of \(L\), and no independence between \(L\) and any other statistic of \(Y\), is assumed. Let \(T(Y)\) be arbitrary measurable and set
\[
Q=H^TCH+2H^TL(Y)+T(Y).
\tag{2.1}
\]
Write
\[
r'=\frac r{r-1},\qquad
\alpha=\frac{k}{r'}=\frac{k(r-1)}r,\qquad
P=\|p_L\|_r.
\tag{2.2}
\]
Then, for every \(t\ne0\),
\[
\boxed{
|\phi_Q(t)|
\le \min\{1,\pi^\alpha P\,|t|^{-\alpha}\}.
}
\tag{2.3}
\]

If \(\alpha>1\), equivalently \(r>k/(k-1)\), then \(\phi_Q\in L^1(\mathbb R)\), so \(Q\) has a canonical \(C_0\) density satisfying
\[
\boxed{
\|p_Q\|_\infty
\le \frac{\alpha}{\alpha-1}\,
P^{1/\alpha}.
}
\tag{2.4}
\]
Consequently
\[
\Pr(Q\in I)\le
\frac{\alpha}{\alpha-1}P^{1/\alpha}|I|.
\tag{2.5}
\]

For \(k=3,r=2\),
\[
\boxed{
|\phi_Q(t)|\le
\min\{1,\pi^{3/2}\|p_L\|_2|t|^{-3/2}\},
\qquad
\|p_Q\|_\infty\le3\|p_L\|_2^{2/3}.
}
\tag{2.6}
\]

### Proof

Let
\[
g(h)=\prod_{j=1}^k f_j(h_j),\qquad
g_t(h)=g(h)e^{it h^TCh},
\]
and define the physical-hub transform
\[
G_t(w)=\int_{\mathbb R^k}g_t(h)e^{i2t h^Tw}\,dh
=\widehat g_t(2tw).
\tag{2.7}
\]
Conditioning on \(Y\) and then disintegrating only with respect to the whole vector \(L\),
\[
|\phi_Q(t)|
\le \int_{\mathbb R^k}p_L(w)|G_t(w)|\,dw
\le \|p_L\|_r\|G_t\|_{r'}.
\tag{2.8}
\]
The conditional phase \(\mathbb E(e^{itT}\mid L=w)\) has modulus at most one, so arbitrary dependence between \(T\) and \(L\) costs nothing.

For the Fourier operator in (2.7), the trivial endpoint is
\[
\|\widehat u\|_\infty\le\|u\|_1.
\tag{2.9}
\]
The completed account01/B01 Plancherel calculation (1.1), now in \(k\) physical dimensions, is
\[
\|\widehat u\|_2=(2\pi)^{k/2}\|u\|_2.
\tag{2.10}
\]
Riesz--Thorin between (2.9) and (2.10) yields, for \(1<r\le2\),
\[
\|\widehat u\|_{r'}
\le (2\pi)^{k/r'}\|u\|_r.
\tag{2.11}
\]
After the change of variables \(\xi=2tw\),
\[
\|G_t\|_{r'}
=(2|t|)^{-k/r'}\|\widehat g_t\|_{r'}
\le \left(\frac{\pi}{|t|}\right)^\alpha\|g\|_r.
\tag{2.12}
\]
Because \(0\le f_j\le1\) and \(\int f_j=1\),
\[
\|g\|_r^r
=\prod_j\int f_j^r\le1.
\tag{2.13}
\]
Equations (2.8)--(2.13) prove (2.3).

When \(\alpha>1\), put
\[
t_0=\pi P^{1/\alpha}.
\]
Direct integration gives
\[
\int_{\mathbb R}|\phi_Q(t)|\,dt
\le
2\left[t_0+\pi^\alpha P\int_{t_0}^\infty t^{-\alpha}dt\right]
=
2\pi\frac{\alpha}{\alpha-1}P^{1/\alpha}.
\tag{2.14}
\]
Fourier inversion proves \(p_Q\in C_0\) and (2.4). QED.

## 3. What the joint estimate changes

The theorem does not require a coordinatewise product law for the slope vector \(L\). Only its genuine joint \(L^r\) density enters. In particular:

- all slope-coordinate dependence is retained;
- \(T(Y)\) may be maximally correlated with \(L(Y)\);
- the physical curvature \(C\) may contain arbitrary dense deterministic self-couplings;
- no scalar quadratic phase is assigned pointwise decay;
- no independence after rotation or separation of copy-sums and copy-differences is used.

The threshold
\[
r>\frac{k}{k-1}
\tag{3.1}
\]
is the exact integrability threshold produced by this mechanism. At equality the envelope is only \(O(|t|^{-1})\), so this proof correctly records the logarithmic endpoint rather than declaring it integrable.

## 4. Actual full-target inequality

Take six independent original cap-one coordinates
\[
H_1,H_2,H_3,Y_1,Y_2,Y_3
\]
and let \(C\) be any symmetric \(3\times3\) matrix. Set
\[
Q_C=H^TCH+2(H_1Y_1+H_2Y_2+H_3Y_3).
\tag{4.1}
\]
The slope vector \(L=(Y_1,Y_2,Y_3)\) has product density \(p_L\le1\), hence
\[
\|p_L\|_2\le1.
\tag{4.2}
\]
Applying (2.6),
\[
\boxed{
\|p_{Q_C}\|_\infty\le3,\qquad p_{Q_C}\in C_0.
}
\tag{4.3}
\]
For \(C=0\), the coefficient matrix is the direct sum of three hyperbolic blocks
\[
\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
so its spectrum is
\[
\{1,1,1,-1,-1,-1\}.
\tag{4.4}
\]
Thus (4.3) is a strict instance of the owner's full spectral target:
\[
\boxed{\Pr(Q_0\in I)\le3|I|.}
\tag{4.5}
\]
The estimate remains valid after adding arbitrary dense quadratic self-coupling \(C\) among the three physical hubs, whether or not the resulting spectrum is used separately.

Equation (4.3) is the requested actual application of the completed account01/B01 averaged-frequency endpoint: the scalar Plancherel identity is promoted by interpolation to the joint \(L^2\) slope inequality, producing integrable \(t^{-3/2}\) decay.

## 5. Remaining gap

This theorem pays any three-dimensional physical hub whose joint random slope has an \(L^r\) density above the threshold \(r>3/2\). The unresolved full-target step is structural: an arbitrary matrix with \(s_3(A)\ge1\) need not expose such a three-hub/slope packet in original coordinates with controlled joint \(L^r\) density. The punctured one-outer-pivot diffuse-row survivor from account01/B01 also supplies only one random row modulation, for which the half-Riesz endpoint is genuinely logarithmically critical.

The next mechanism must therefore either:

1. extract a third jointly nondegenerate original-coordinate slope direction; or
2. spend the inherited second spectral direction inside the one-row survivor without demanding an extra literal square.

The full universal bounded-density conjecture remains **OPEN**. Unrestricted continuity remains **OPEN**.

## 6. Source ledger

Fresh completed input: account01/B01 \`dd9bdc8f347ef1849cb1647964d19d014843f877\`, checked by \`a67d2d2f4ea90c7089463d7e6a0b5262442e828b\`. The Claude source pin remains \`e5f71d79eff325201dd0274053d20268ce65b837\`. Standing owner controls and Claude-review corrections were preserved. No scheduler, task, notification, authentication, workflow, permission, or production-store state was changed.
