# Dimension-free density from an exact-rank physical crossing

**Status:** Rigorous structural theorem for arbitrary symmetric matrices, arbitrary within-bank terms, and arbitrary affine terms. It requires an exact-rank crossing block with controlled smallest nonzero singular value. It does not establish that every matrix satisfying (s_3(A)\ge1) has such a crossing.

## Theorem

Let (X_1,\ldots,X_n) be independent with densities bounded by one. Let (A) be any real symmetric matrix. Suppose a partition of its **original coordinate set** (S\sqcup T=[n]) has crossing block (B=A_{S,T}) of **exact rank (k\ge3)** and (s_k(B)\ge\beta>0). Then, for all affine coefficients (b,c), the law of
\[
 Q=X^TAX+b^TX+c
\]
has a bounded continuous density satisfying
\[
 \|p_Q\|_\infty
 \le\frac{2k}{(k-2)\beta}
 \le\frac6\beta.
\]

## Proof

Choose a thin singular value decomposition (B=R D W^T), with (R^TR=W^TW=I_k), (D=\operatorname{diag}(d_1,\ldots,d_k)), (d_j\ge\beta). The projected vectors (Z=R^TX_S) and (V=W^TX_T) are independent. Each is an orthogonal (k)-dimensional projection of independent cap-one original coordinates, and therefore its density satisfies the LPP product-projection bound
\[
 \|p_Z\|_\infty,\ \|p_V\|_\infty\le2^{k/2}.
\]
Write (Q=q_S(X_S)+q_T(X_T)+2Z^TDV+c), with each (q) containing arbitrary within-bank quadratic and affine terms. At any real frequency (t), disintegrate the modulated measures within the banks:
\[
 \alpha_t(z)=p_Z(z)\mathbb E[e^{itq_S(X_S)}\mid Z=z],\quad
 \gamma_t(v)=p_V(v)\mathbb E[e^{itq_T(X_T)}\mid V=v].
\]
Then (|\alpha_t|\le p_Z), (|\gamma_t|\le p_V), and
[
 \|\alpha_t\|_2\|\gamma_t\|_2
 \le\sqrt{\|p_Z\|_\infty\|p_V\|_\infty}\le2^{k/2}.
]
Because the crossing has **exact** rank (k), its entire phase is (e^{2it z^TDv}). Independence, Cauchy–Schwarz, and (k)-dimensional Plancherel imply
\[
 |\varphi_Q(t)|
 \le \frac{(2\pi)^{k/2}}{|\det(2tD)|^{1/2}}
 \|\alpha_t\|_2\|\gamma_t\|_2
 \le\left(\frac{2\pi}{\beta|t|}\right)^{k/2}
\]
for (t\ne0). Combine with ( |\varphi_Q(t)|\le1). Since (k>2), this is integrable, and Fourier inversion gives
\[
 \|p_Q\|_\infty
 \le\frac1{2\pi}\int_{\mathbb R}
 \min\left\{1,\left(\frac{2\pi}{\beta|t|}\right)^{k/2}\right\}dt
 =\frac{2k}{(k-2)\beta}.
\]
The characteristic function's integrability yields a bounded continuous density. No sign or size condition is needed for (A_{S,S}), (A_{T,T}), or the affine coefficients.

## Exact-rank warning

If (B) has additional tiny singular values, dropping those directions from the bilinear phase leaves a residual term jointly involving the two banks. Such a term cannot be absorbed into the separate complex amplitudes. The theorem applies with (k=\operatorname{rank}(B)), so (\beta=s_k(B)), and presently offers no bound depending only on (s_3(B)) when (k>3). The exact-rank-three diffuse spectral-frame theorem is a useful case: its balanced physical cut has (\operatorname{rank}(B)=3), and separate whitening proves a lower bound on (s_3(B)).


## Determinant refinement

The preceding proof can retain the singular-value product. Put
\[
 g_B=\left(\prod_{j=1}^k s_j(B)\right)^{1/k}.
\]
The Plancherel estimate before substituting $d_j\ge\beta$ is
\[
 |\varphi_Q(t)|\le\min\{1,(2\pi/(g_B|t|))^{k/2}\}.
\]
The same explicit integral therefore proves the sharper bound
\[
 \|p_Q\|_\infty\le\frac{2k}{(k-2)g_B}.
\]
This is at most $2k/[(k-2)\beta]$ because $g_B\ge s_k(B)\ge\beta$. In particular an exact rank-four crossing with singular values $(1,1,1,\varepsilon)$ yields $4\varepsilon^{-1/4}$, a useful quantitative but nonuniform estimate as $\varepsilon\downarrow0$. The exact-cross-rank requirement is unchanged.
