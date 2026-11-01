SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B11, 2026-09-23T19:14:01Z.
attacking: the punctured double-graph collar; test the natural same-bank mixed-L2 conditioning bridge, and retain a uniform rank-two crossing currency through nonzero graph defect.

# fleet03/B11 r40 — punctured-collar geometry and a mixed-slice obstruction

Programme: `QFORM-DENSITY-3EIG-20260922` (owner control revision 2026-09-22.15; current continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`).
Status: **new supporting structural lemma + rigorous counterexample to an intermediate analytic bridge / full QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.
Regularity: no new full branch is closed here; continuity of the unrestricted target remains open.

The full target remains unchanged: independent scalar inputs with densities <=1, arbitrary real symmetric A, at least three eigenvalues of absolute value >=1. No Gaussianity, moments, log-concavity, support, post-rotation independence, pointwise van-der-Corput decay, or arbitrary-joint coarea estimate is used.

## 1. Rank-two logarithmic benchmark

For independent centered unit uniforms,

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<1/2.
\]

Thus a rank-two indefinite crossing is genuinely at the logarithmic endpoint. The r38/r39 exact-graph mechanisms show that a third internal square or bilinear curvature can remove this endpoint by integrated Fourier estimates. The open interpolation is the punctured double-graph collar, where the third cross singular value is nonzero but may tend to zero.

## 2. Uniform dominant rank-two crossing survives the entire punctured collar

Retain the exact-rank-three true-near-coloop state from r37--r39:

\[
A=RMR^T,\quad R^TR=I_3,\quad s:=\min|\lambda(M)|\ge1,
\]
with hub row `r_0=sqrt(c)e`, `c>63/64`, leaves `r_j=s_j e+w_j`, and the literal original-coordinate split `S sqcup T` satisfying

\[
\lambda_{\min}(G_S),\lambda_{\min}(G_T)>g_0,\qquad g_0:=17/288,
\]
where `G_B=sum_{j in B} w_j w_j^T`.

As in r37, write

\[
\tau_B=\sum_{j\in B}s_j^2,\quad h_B=\sum_{j\in B}s_jw_j,\quad
\rho_B=\tau_B-h_B^TG_B^{-1}h_B\ge0.
\]
Let `H={0} union S` and `B=A[H,T]=R_HMR_T^T`. No exact-graph assumption is made in this section: `rho_T` may be any nonnegative value.

### Lemma `QFORM-PUNCTURED-COLLAR-TOP2-CROSS-v1`

Let `sigma_1>=sigma_2>=sigma_3>=0` be the singular values of `B`. Then throughout the whole collar,

\[
\boxed{\sigma_1\sigma_2>\kappa_*s^2},\qquad
\kappa_*:=\frac{34}{111}\left(\frac{17}{288}\right)^2
=0.0010672564926\ldots .
\]

#### Proof

The H-side Gram factorization from r38 is

\[
\Gamma_H=R_H^TR_H=L_S\,\mathrm{diag}(c+\rho_S,G_S)L_S^T,
\quad L_S=\begin{pmatrix}1&a_S^T\\0&I_2\end{pmatrix},
\]
with `a_S=G_S^{-1}h_S` and `||a_S||^2<9/34`. Hence

\[
\lambda_{\min}(\Gamma_H)>\beta_0,
\qquad \beta_0:=\frac{34}{111}\frac{17}{288}.
\]
Therefore

\[
\sigma_{\min}(R_HM)\ge s\sqrt{\beta_0}.
\]
For every matrix product `PQ`, singular-value monotonicity gives

\[
s_j(PQ)\ge \sigma_{\min}(P)s_j(Q).
\]
Apply this with `P=R_HM`, `Q=R_T^T`. The two largest squared singular values of `R_T^T` are the two largest eigenvalues of

\[
\Gamma_T=R_T^TR_T=
\begin{pmatrix}\tau_T&h_T^T\\h_T&G_T\end{pmatrix}.
\]
By Cauchy interlacing with the principal 2 by 2 block `G_T`,

\[
\lambda_1(\Gamma_T)\ge\lambda_1(G_T),\qquad
\lambda_2(\Gamma_T)\ge\lambda_2(G_T)>g_0.
\]
Thus `s_1(R_T^T)s_2(R_T^T)>g_0`, and

\[
\sigma_1\sigma_2>s^2\beta_0g_0
=s^2\frac{34}{111}\left(\frac{17}{288}\right)^2.
\]
QED.

This shows that the punctured collar does **not** lose the two directions responsible for the rank-two logarithmic endpoint. Only the third singular direction can vanish. That is the correct interpolation geometry.

The exact determinant identity also records the vanishing scale:

\[
\prod_{j=1}^3\sigma_j(B)
=|\det M|\sqrt{\det\Gamma_H\,\det G_T\,\rho_T},
\]
because `det Gamma_T=det G_T rho_T`. Hence a full rank-three crossing estimate necessarily sees a factor `rho_T^{1/2}` in the volume and deteriorates as `rho_T->0`; the dominant rank-two currency above remains fixed.

## 3. A natural vector-valued r39 bridge is false

A tempting way to extend r39 to the same-bank residual shear is to slice the three-dimensional projection `(v,W)` by `W=w`, use rank-two crossing Plancherel in `v`, and hope for a universal mixed-norm estimate

\[
\int_{\mathbb R}\|p_{v,W}(\cdot,w)\|_{L^2(\mathbb R^2)}\,dw\le C.
\tag{MS}
\]

The next theorem shows that (MS) is false even when `(v,W)` is an **orthogonal transform of three independent cap-one original coordinates**. Thus projection-density caps plus naive slice-L2 integration cannot close the same-bank residual shear.

### Theorem `QFORM-ORTHOGONAL-PRODUCT-MIXED-L1L2-UNBOUNDED-v1`

For every `N>=2` there exist three independent scalar variables `X,Y,Z`, each with probability density bounded by one, and an orthogonal transformation

\[
v_1=(X-Y)/\sqrt2,\qquad v_2=Z,\qquad W=(X+Y)/\sqrt2,
\]
such that the joint density `p_N(v_1,v_2,w)` satisfies

\[
\boxed{
\int \left(\int_{\mathbb R^2}p_N(v,w)^2\,dv\right)^{1/2}dw
=J_N\left[N+\frac{\sqrt2}{2}N(N-1)\right]
}
\]
where

\[
J_N=\frac43\,2^{-1/4}N^{-3/2}.
\]
Consequently

\[
\boxed{
\int \|p_N(\cdot,w)\|_2dw
=\frac43\,2^{-3/4}\sqrt N+O(N^{-1/2})\to\infty.
}
\]

#### Construction and proof

Set `ell=1/N`. Choose centers `a_1,...,a_N` so separated and Sidon that the intervals of pair sums

\[
[a_i+a_j,a_i+a_j+2\ell]
\]
are disjoint for distinct unordered pairs `{i,j}`. For example sufficiently rapidly increasing powers of 10 work. Put

\[
E_N=\bigcup_{i=1}^N[a_i,a_i+\ell],
\]
and let `X,Y` have density `1_{E_N}`; this is a probability density because `|E_N|=N\ell=1`. Let `Z` have density `1_[0,1]`. All three densities are <=1.

The map `(x,y,z)->(v_1,v_2,w)` above is orthogonal, so the transformed joint density is simply the indicator of the orthogonal image of `E_N x E_N x [0,1]`.

Consider one ordered cell `[a_i,a_i+ell] x [a_j,a_j+ell]`. After translating its center, put `s=x+y in[0,2ell]`. At fixed `w=s/sqrt2`, the `v_1`-section length is

\[
L_v(s)=\sqrt2\min(s,2\ell-s).
\]
The `v_2`-section has length one. Therefore the contribution of one isolated ordered cell to the mixed norm is

\[
\begin{aligned}
J_N
&=\int \sqrt{L_v(s)}\,dw\\
&=2^{-1/4}\int_0^{2\ell}\sqrt{\min(s,2\ell-s)}\,ds\\
&=\frac43\,2^{-1/4}\ell^{3/2}.
\end{aligned}
\]
For a diagonal pair `i=j` there is one such section. For `i<j`, the two ordered cells `(i,j)` and `(j,i)` have the same `w` band but disjoint `v_1` sections; squared L2 masses add, so the mixed-norm contribution is `sqrt(2) J_N`. Distinct unordered pair-sum bands are disjoint by construction, so contributions add exactly. Summing `N` diagonal bands and `N(N-1)/2` off-diagonal bands proves the formula.

The leading constant is

\[
\frac43 2^{-3/4}=0.7928047433\ldots .
\]

This is an obstruction to an intermediate proof interface, **not** a counterexample to QFORM. It exploits exactly the fragmented-support freedom that the owner corrections require us to retain.

## 4. Consequence for the same-bank residual shear

In the punctured collar, a full SVD of the physical crossing has the normal form

\[
2u^T\operatorname{diag}(\sigma_1,\sigma_2)v+2\sigma_3 zW,
\]
with `sigma_1 sigma_2` uniformly bounded below by Section 2 and `sigma_3->0` allowed. The r39 exact-boundary theorem pays `sigma_3=0` using the internal bilinear curvature `2z d^T u`.

The counterexample above shows that the following proposed extension route is invalid:

> condition/slice on the same-bank scalar `W`, apply the r39 rank-two estimate to each slice, and average using only a universal `L^1_W(L^2_v)` norm of the three-dimensional product projection.

That mixed norm has no universal bound. A successful uniform interpolation must keep the original scalar product structure through the `W` integration (for example via a decoupling/weighted-subset argument) or make an original-coordinate cut that gives the residual scalar source-disjoint provenance. Merely knowing the 3D projection cap is insufficient for this slice method.

## 5. Designated partner result applied at an actual inequality

The completed fleet04/B11 pair-area compiler at
`50b07997bec888ff7cc6820cd42be8e34d0ffc48` gives, in the exact-rank-three frame,

\[
\|p_Q\|_\infty\le\frac{128\sqrt2}{s\sqrt{g_{ij}}}.
\]
For the heavy hub and a leaf,

\[
g_{0j}=c\|w_j\|^2.
\]
Hence if any leaf has `||w_j||^2>=1/36`, then

\[
g_{0j}>\frac{63}{64}\frac1{36}=\frac7{256},
\]
and therefore

\[
\boxed{\|p_Q\|_\infty<\frac{2048\sqrt{2/7}}s<1094.703/s.}
\]
Thus the mixed-slice obstruction is relevant only after the already-paid large-leaf branch is removed; it occurs in the genuinely diffuse same-bank collar, not because a single physical pair was overlooked.

## 6. Remaining implication

The next B11 target is now more precise:

`QFORM-SAMEBANK-SHEAR-PRODUCT-DECOUPLING-v2`:

> In the normal form
> `F(u)+2z d^T u+2u^T S v+2kappa zW+G(Y)`, with `(v,W)` an orthogonal 3D projection of one original cap-one product bank, prove a bound uniform as `kappa->0` by retaining coordinate-product structure through the W integration; or force a source-disjoint residual cut. Do not use the false universal mixed `L1_W(L2_v)` bound above.

The new structural lemma guarantees that `sigma_1 sigma_2` stays uniformly paid throughout the punctured collar, so the only analytic instability that must be neutralized is the same-bank third shear. Arbitrary additional nonseparable spectrum remains a separate bridge to the full target.

## Sources consumed

- math-research-brain fresh main at startup: `55c2088d34860b89968d086ae247c7428266ebeb` and later refreshes; owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`.
- fleet03/B11 r37 exact graph geometry: `60366e6dcbf3a321423e2ff1b0f4ecb9a78776f6`.
- fleet03/B11 r38/r39 integrated square/bilinear receivers: r38 `430d0746f305abeeea58af4d319efe98be87d563`; r39 `b53315b2f91c6a917f8c5c17f3a5dba07904374b`.
- interactive projected crossing theorem: `d2f970d33fa7084f8de55412189402ac609e4da6`, `NEW_PROJECTED_CROSSING.md`.
- designated partner fleet04/B11 pair-area/disjoint-volume compiler: `50b07997bec888ff7cc6820cd42be8e34d0ffc48`.

No scheduler/task-state change, email, notification, paid model/API, Codex, public release, installation, permission expansion, workflow execution, or cross-account authentication was performed.