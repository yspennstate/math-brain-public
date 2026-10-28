SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T18:16:40Z.
attacking: the true near-coloop exact-graph null-ruling endpoint: replace the missing square curvature by a dyadic integrated-Fourier estimate for the surviving internal bilinear term, while retaining the rank-two crossing.

# account03/B11 r39 — rank-two crossing + internal bilinear curvature

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner continuation:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
**Status:** `NEW SUPPORTING THEOREM / EXACT-GRAPH CONTINUITY CLOSURE / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Regularity:** the new Fourier theorem proves a bounded continuous density in its scope. Combined with r37 and r38, the full exact-graph branch below has a continuous representative with the already-proved uniform height bound. This does not prove continuity for the unrestricted target.

The unrestricted conjecture remains OPEN. No Gaussianity, log-concavity, moments, compact support, connected support, independence after spectral rotation, or law-uniform pointwise van-der-Corput estimate is used.

## 1. Rank-two logarithmic benchmark

For independent centered unit uniforms, the opposite-sign rank-two control remains

\[
p_{2XY}(t)=\log\frac1{2|t|},\qquad 0<|t|<\frac12.
\]

Thus a rank-two saddle alone is genuinely at the logarithmic endpoint. In r38 a nonzero square curvature transverse to an exact rank-two crossing supplied the missing integrated Fourier gain. The remaining exact null-ruling case has no transverse square; the only available third curvature is an internal bilinear term. The theorem below shows that this is still enough after dyadic averaging.

## 2. New analytic theorem

### Theorem `QFORM-RANK2-CROSS-INTERNAL-BILINEAR-DYADIC-v1`

Let `X` and `Y` be independent random vectors. Let

\[
u=U^T X\in\mathbb R^2,\qquad z=w^T X\in\mathbb R,\qquad v=V^T Y\in\mathbb R^2,
\]

where `[U,w]` has three orthonormal columns in the `X` source space and `V` has two orthonormal columns in the `Y` source space. Assume `(u,z)` has probability density `rho(u,z)`, and write

\[
m(u)=\int_{\mathbb R}\rho(u,z)\,dz.
\]

Fix a unit vector `e in R^2` and let

\[
g_e(x)=\int_{e^\perp}m(xe+y)\,dy.
\]

Assume the three projection caps

\[
\|\rho\|_\infty\le M_3,\qquad \|m\|_\infty\le M_2,\qquad \|g_e\|_\infty\le M_1.
\]

Assume `v` has density bounded by `M_Y`. Let `S=diag(sigma_1,sigma_2)` with `sigma_1,sigma_2>0`. Let `d in R^2`, `D=|d|>0`, and `e=d/D`. Suppose

\[
Q=F(u)+2z\,d^Tu+2u^TSv+G(Y),                                      \tag{2.1}
\]

where `F` and `G` are arbitrary measurable real-valued functions. Then `Q` has a bounded continuous density and

\[
\boxed{
\|p_Q\|_\infty
\le \frac{M_1}{\pi D}
+\frac{\sqrt{M_Y}}{\sqrt{\sigma_1\sigma_2}}\,
\mathcal S(M_2,M_3),
}                                                                  \tag{2.2}
\]

where

\[
\mathcal S(M_2,M_3)
:=\sum_{j=0}^\infty 2^{-j/2}
\sqrt{\,2M_2+\pi M_3(1+2j\log2)\,}.                              \tag{2.3}
\]

The same estimate permits an affine `z` term `2 eta z`: replacing `d^Tu` by `d^Tu+eta` merely translates the scalar coordinate used below.

### Proof

For each `t`, push the complex measure `exp(itG(Y)) dP_Y` onto `v`. Its density `b_t(v)` satisfies

\[
|b_t(v)|\le p_v(v),\qquad \|b_t\|_2\le M_Y^{1/2}.               \tag{2.4}
\]

On the `X` side define

\[
a_t(u)=e^{itF(u)}\int_{\mathbb R}e^{i2tz d^Tu}\rho(u,z)\,dz.   \tag{2.5}
\]

The exact rank-two crossing Plancherel inequality gives, for `t\ne0`,

\[
|\phi_Q(t)|
\le \frac{\pi}{|t|}(\sigma_1\sigma_2)^{-1/2}
\|a_t\|_2\|b_t\|_2.                                              \tag{2.6}
\]

Put

\[
A:=\pi M_Y^{1/2}(\sigma_1\sigma_2)^{-1/2},\qquad
H(t):=\|a_t\|_2.
\]

Thus

\[
|\phi_Q(t)|\le A|t|^{-1}H(t).                                   \tag{2.7}
\]

It remains to obtain an integrated estimate for `H` without any pointwise quadratic-phase decay.

Choose coordinates `u=xe+y` with `y in e^perp`. For fixed `u`, let

\[
\widehat\rho_u(\xi)=\int e^{i\xi z}\rho(u,z)\,dz.
\]

Then

\[
H(t)^2=\int_{\mathbb R^2}|\widehat\rho_u(2Dt x)|^2\,du.          \tag{2.8}
\]

Fix `T>0` and `r>0`. On the slab `|x|\le r`, use `|\widehat\rho_u|\le m(u)`:

\[
\begin{aligned}
\int_T^{2T}\int_{|x|\le r}|\widehat\rho_u(2Dtx)|^2\,du\,dt
&\le T\int_{|x|\le r}m(u)^2\,du\\
&\le T M_2\int_{|x|\le r}m(u)\,du\\
&\le 2TM_1M_2r.                                                   \tag{2.9}
\end{aligned}
\]

On `|x|>r`, Plancherel in `z` gives

\[
\begin{aligned}
\int_T^{2T}|\widehat\rho_u(2Dtx)|^2dt
&\le \frac1{2D|x|}\int_{\mathbb R}|\widehat\rho_u(\xi)|^2d\xi\\
&=\frac\pi{D|x|}\int\rho(u,z)^2dz\\
&\le\frac{\pi M_3}{D|x|}m(u).                                   \tag{2.10}
\end{aligned}
\]

Because `g_e` is a probability density bounded by `M_1`, whenever `0<r\le1/M_1`,

\[
\int_{|x|>r}\frac{g_e(x)}{|x|}\,dx
\le M_1\left(1+2\log\frac1{M_1r}\right).                       \tag{2.11}
\]

Indeed, on `r<|x|\le1/M_1` use `g_e\le M_1`, and beyond `1/M_1` use `1/|x|\le M_1` together with total mass one.

Now set

\[
T_0:=\frac{M_1}{D},\qquad T_j:=2^jT_0,\qquad r_j:=\frac1{DT_j}.
\]

Then `r_j\le1/M_1`, and (2.9)--(2.11) imply

\[
\boxed{
\int_{T_j}^{2T_j}H(t)^2dt
\le \frac{M_1}{D}
\left[2M_2+\pi M_3(1+2j\log2)\right].
}                                                                  \tag{2.12}
\]

Consequently, Cauchy--Schwarz on each dyadic block gives

\[
\begin{aligned}
\int_{T_j}^{2T_j}|\phi_Q(t)|dt
&\le \frac A{T_j}\sqrt{T_j}
\left(\int_{T_j}^{2T_j}H(t)^2dt\right)^{1/2}\\
&\le A2^{-j/2}
\sqrt{2M_2+\pi M_3(1+2j\log2)}.                                 \tag{2.13}
\end{aligned}
\]

The same estimate holds on the negative block. On `|t|<T_0`, simply use `|\phi_Q(t)|\le1`. Summing all blocks yields

\[
\int_{\mathbb R}|\phi_Q(t)|dt
\le \frac{2M_1}{D}+2A\mathcal S(M_2,M_3).                       \tag{2.14}
\]

The series converges because of the geometric factor `2^{-j/2}`. Fourier inversion proves (2.2). Since `\phi_Q\in L^1`, the density has a bounded continuous representative. QED.

### Scope note

This is an integrated, not pointwise, estimate. A phase-aligned rough density may still make the `z`-Fourier transform large at isolated frequencies. The dyadic `L^2(dt)` calculation forces those frequencies to occupy too little aggregate mass once the internal bilinear frequency `2t d^Tu` sweeps through the scalar marginal. The physical rank-two crossing remains intact throughout and contributes its separate `|t|^{-1}` Plancherel factor.

The theorem does **not** permit a nonzero `alpha z^2` term to be discarded merely because `alpha` is small. No perturbative small-quadratic-error claim is made.

## 3. Application to the exact-graph true-near-coloop boundary

Use the exact-rank-three state from account03/B11 r37--r38:

\[
A=RMR^T,\qquad R^TR=I_3,\qquad s:=\min|\lambda(M)|\ge1,
\]

with a heavy physical hub `r_0=\sqrt c\,e`, `c>63/64`, and residual rows `r_j=s_j e+w_j`.

### 3.1 Designated partner result applied at an actual inequality

The completed account04/B11 theorem at commit `50b07997bec888ff7cc6820cd42be8e34d0ffc48` proves

\[
\|p_Q\|_\infty\le\frac{128\sqrt2}{s\sqrt{g_{ij}}},\qquad
g_{ij}=\|r_i\wedge r_j\|^2.                                    \tag{3.1}
\]

For the hub-leaf pair,

\[
g_{0j}=c\|w_j\|^2.
\]

Hence if any residual row has `\|w_j\|^2\ge1/36`, then

\[
g_{0j}>\frac{63}{64}\frac1{36}=\frac7{256},
\]

and the partner theorem gives the actual full-line inequality

\[
\boxed{
\|p_Q\|_\infty
<\frac{2048\sqrt{2/7}}s
=\frac{1094.703\ldots}s.
}                                                                  \tag{3.2}
\]

Thus the surviving chamber may assume all transverse leaf leverages are `<1/36`.

### 3.2 Exact graph cut and crossing constants

The r37 determinant-pair coloring gives a literal original-coordinate partition `S\sqcup T` of the residual leaves with

\[
\lambda_{\min}(G_S),\lambda_{\min}(G_T)>\frac{17}{288},
\]

where `G_B=\sum_{j\in B}w_jw_j^T`. Suppose one bank is an exact graph; after relabeling,

\[
\rho_T=0.
\]

Let `H={0}\cup S`. Then the physical cross block `A[H,T]` has exact rank two. Let its nonzero singular values be `sigma_1\ge sigma_2>0`. The r38 calculation gives

\[
\boxed{
\sigma_1\sigma_2>\kappa_0s^2,
\qquad
\kappa_0=\frac{34}{111}\left(\frac{17}{288}\right)^{3/2}
=0.00439279148\ldots .
}                                                                  \tag{3.3}
\]

The same calculation gives, for the `H`-side spectral Gram,

\[
\lambda_{\min}(\Gamma_H)>\beta_0,
\qquad
\beta_0:=\frac{17}{288}\frac{34}{111}
=0.01808058058\ldots .                                            \tag{3.4}
\]

Choose an SVD of the crossing and let `[U,w]` be the orthonormal basis of `range(R_H)` in which `U` spans the two crossing directions and `w` is the unique cross-null direction. The `H`-side quadratic matrix in this basis is

\[
C=\begin{pmatrix}C_0&d\\d^T&\alpha\end{pmatrix}.               \tag{3.5}
\]

Writing `R_H=E K` with `E=[U,w]` and `K^TK=\Gamma_H`, one has

\[
C=K M K^T,
\]

so

\[
\sigma_{\min}(C)\ge s\lambda_{\min}(\Gamma_H)>\beta_0s.         \tag{3.6}
\]

Therefore

\[
\sqrt{|d|^2+\alpha^2}=\|Ce_3\|\ge\sigma_{\min}(C)>\beta_0s.     \tag{3.7}
\]

This is the quantitative cross-null curvature dichotomy.

### 3.3 Nonzero square curvature

If `alpha\ne0`, the r38 theorem `QFORM-RANK2-CROSS-INTERNAL-SQUARE-L4-v1` applies directly and proves that this exact-graph law has a bounded **continuous** density. Its displayed bound depends on `|alpha|^{-1/5}` and is therefore not used as a uniform estimate as `alpha\to0`.

### 3.4 Exact null ruling: internal bilinear exit

Now assume the genuinely missing r38 endpoint

\[
\alpha=0.                                                        \tag{3.8}
\]

Then (3.7) forces

\[
|d|>\beta_0s.                                                     \tag{3.9}
\]

The variables `(u,z)` are a three-dimensional orthogonal projection of the original product law on `H`; `u` and `e\cdot u` are its two- and one-dimensional subprojections. The current product-projection theorem therefore gives

\[
M_3\le2^{3/2},\qquad M_2\le2,\qquad M_1\le\sqrt2.               \tag{3.10}
\]

Likewise `v` is a two-dimensional orthogonal projection of the disjoint `T` bank, so

\[
M_Y\le2.                                                          \tag{3.11}
\]

Apply Theorem 2.1 with (3.3), (3.9)--(3.11). It gives

\[
\|p_Q\|_\infty
\le \frac{\sqrt2}{\pi\beta_0s}
+\frac{\sqrt2}{\sqrt{\kappa_0}s}\,\mathcal S_0,                 \tag{3.12}
\]

where

\[
\mathcal S_0
=\sum_{j\ge0}2^{-j/2}
\sqrt{4+2\sqrt2\pi(1+2j\log2)}.                                 \tag{3.13}
\]

A deterministic 40-term computation plus the concave tangent tail bound

\[
\sqrt{A+Bj}
\le \sqrt{A+BN}
+\frac{B}{2\sqrt{A+BN}}(j-N),\qquad j\ge N,
\]

at `N=40` gives

\[
\mathcal S_0<20.759.                                               \tag{3.14}
\]

Hence

\[
\boxed{\|p_Q\|_\infty<468/s}                                     \tag{3.15}
\]

by this Fourier argument alone, and this density is continuous.

### 3.5 Exact-graph continuity closure with the sharper inherited height bound

The preceding r37 theorem `QFORM-ONEBANK-EXACT-GRAPH-DEPENDENT-PAIR-v1` already proves, for **every** value of `alpha` in the same exact-graph branch, an essentially bounded density with

\[
\operatorname*{ess\,sup}p_Q<128/s.                               \tag{3.16}
\]

Sections 3.3 and 3.4 now show that every such law also has a continuous density representative: r38 when `alpha\ne0`, and the new dyadic theorem when `alpha=0`. Any continuous representative equals the r37 bounded density almost everywhere. If it exceeded `128/s` at one point, continuity would force it to exceed `128/s` on a set of positive measure, contradicting (3.16). Therefore the entire exact-graph branch satisfies

\[
\boxed{
\text{continuous density and }\quad \|p_Q\|_\infty\le128/s.
}                                                                  \tag{3.17}
\]

This closes the regularity gap left by r37 without making a false small-`alpha` perturbation. The argument is sign-blind after the exact-rank-three factorization, so it applies to both `(+,+,-)` and `(+,-,-)`.

## 4. What the third direction is doing

The exact opposite-sign rank-two law has the logarithmic singularity above. In the exact-graph true-near-coloop chamber, the cross-null third direction cannot disappear because `C` is quantitatively invertible. It removes the singularity in one of two mutually exhaustive ways:

1. `alpha\ne0`: the direction carries square curvature, and r38 supplies an integrated `L^4(dt;L^2)` gain;
2. `alpha=0`: invertibility forces `d\ne0`, so the direction couples bilinearly to the crossing plane, and the present dyadic `L^2(dt)` estimate supplies the missing aggregate decay.

Neither mechanism invokes law-uniform pointwise quadratic-phase decay, nor does either rotate the original independent coordinates and then claim independence.

## 5. Remaining gap

The next B11 structural gap is still the **punctured double-graph collar**

\[
0<\rho_S,\rho_T\ll1,
\]

where both selected physical banks have small but nonzero third source directions. The exact rank-two crossing becomes rank three with a tiny third singular scale. A successful continuation must be stable as both graph defects tend to zero and must not divide by that tiny singular value, use input moments, or use conditional-density suprema.

Separately, the full owner target still requires the bridge from exact rank three to arbitrary additional nonseparable spectrum. No small matrix tail is treated as a small random quadratic error. The unrestricted universal theorem and its global continuity conclusion remain OPEN.

## 6. Source pins

- latest owner continuation consumed: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`;
- preceding B11 r38 source: `yspennstate/math-open-problems@430d0746f305abeeea58af4d319efe98be87d563`, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B11/20260923T175922Z-account03-B11-QFORM-r38/`;
- exact-graph r37 source: `yspennstate/math-open-problems@60366e6dcbf3a321423e2ff1b0f4ecb9a78776f6`;
- designated partner account04/B11 theorem: `yspennstate/math-open-problems@50b07997bec888ff7cc6820cd42be8e34d0ffc48`;
- projected-crossing/product-projection source used for projection caps: `yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`, `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`;
- execution label: `WITHOUT_VERIFIED_BRAIN`.
