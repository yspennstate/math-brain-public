SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T11:41:12Z.
attacking: the full orthogonal three-partial-heavy perturbation of the diffuse {1,1,-1} obstruction; determine the sharp second-order orientation penalty and close the off-zero loophole.

# QFORM-ORTHOGONAL-THREE-PARTIAL-HEAVY-LOCAL-MAX-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner order: `2026-09-22.5`; owner control observed as `2026-09-22.15`  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM / FULL QFORM OPEN**  
Continuity: proved only for the scoped family below; unrestricted target continuity remains open.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

Fresh control at start was `math-research-brain@d63c2daec23cf0b19197617929f7aaf62dbfe34e`; a later prepublication refresh still had QFORM as the only active target and no B17 stop. The live corrections were respected: no arbitrary-joint 3D coarea bound, no post-rotation independence, no conditional-cap moment, no fixed-fragment reduction, no pointwise law-uniform stationary-phase bound, and no universal-good-minor premise is used.

## 1. Statement

Put

\[
\sigma^2=1/12,\qquad M=3\sqrt2,
\]

and let `U_1,U_2,U_3` be independent `Unif[-1/2,1/2]`, while `G_1,G_2,G_3` are independent `N(0,sigma^2)`, independent of the uniforms. For a leverage vector

\[
\ell=(\ell_1,\ell_2,\ell_3)\in[0,1)^3
\]

define independent latent coordinates

\[
Y_j=\sqrt{\ell_j}\,U_j+\sqrt{1-\ell_j}\,G_j.
\tag{1.1}
\]

For `u in S^2`, let

\[
B_u=I_3-2uu^T,
\tag{1.2}
\]

so `B_u` has spectrum `{1,1,-1}`. Write `p_{ell,u}` for the density of

\[
Q_{\ell,u}=Y^TB_uY.
\]

Set

\[
W=\sum_{j=1}^3\ell_j^2,\qquad
w_*=\max_j\ell_j^2,
\]

and

\[
D_u(\ell)=\frac1{640}\sum_{j=1}^3
\bigl(57+6u_j^2-39u_j^4\bigr)\ell_j^2.
\tag{1.3}
\]

### Theorem

Uniformly in `u in S^2` and in the direction of `ell`, as `r=max_j ell_j ->0`,

\[
\boxed{
\|p_{\ell,u}\|_\infty
=M\,[1-D_u(\ell)+o(W)].
}
\tag{1.4}
\]

The orientation penalty has the **sharp exact minimum**

\[
\boxed{
\inf_{u\in S^2}D_u(\ell)
=\frac{57W-33w_*}{640}
\ge\frac{3W}{80}.
}
\tag{1.5}
\]

The first equality is attained when the negative eigendirection `u` is a physical spectral axis carrying the largest heavy leverage. Consequently there is an absolute `r_0>0` such that for every nonzero `ell` with `max ell_j<=r_0`,

\[
\boxed{
\sup_{u\in S^2}\|p_{\ell,u}\|_\infty
\le
M\left[1-\frac{57W-33w_*}{1280}\right]
<M.
}
\tag{1.6}
\]

Thus the fully diffuse Gaussian obstruction is a **strict local maximizer against every combination of up to three mutually orthogonal physical uniform heavy rows**, globally in the output level, not only at the cone tip.

## 2. One-dimensional variance-matched expansion

Let

\[
Z_\ell=\sqrt\ell\,U+\sqrt{1-\ell}\,G.
\]

Its characteristic function is

\[
\widehat h_\ell(t)
=e^{-(1-\ell)t^2/24}\operatorname{sinc}(\sqrt\ell t/2)
=e^{-t^2/24}
\left(1-\frac{\ell^2t^4}{2880}
-\frac{\ell^3t^6}{181440}+O(\ell^4t^8)\right).
\tag{2.1}
\]

The linear term vanishes exactly because the uniform and Gaussian components have the same variance `1/12`. For any fixed small `ell_0<1`, differentiation of the analytic function

\[
e^{\ell t^2/24}\operatorname{sinc}(\sqrt\ell t/2)
\]

and the residual Gaussian factor `e^{-t^2/24}` gives a polynomial times `e^{-c t^2}` majorant, uniformly for `0<=ell<=ell_0`. Fourier inversion therefore gives a weighted uniform expansion

\[
\boxed{
h_\ell(y)
=\gamma_\sigma(y)
\left[1-\frac{\ell^2}{20}H_4(y/\sigma)\right]
+O(\ell^3)(1+|y|)^{-8},}
\tag{2.2}
\]

where `H_4(z)=z^4-6z^2+3`. Indeed `gamma_sigma^{(4)}=sigma^{-4}H_4 gamma_sigma=144H_4 gamma_sigma`, and `144/2880=1/20`.

Multiplying the three independent coordinates gives, with `r=max ell_j`,

\[
\rho_\ell(y)
=\gamma_\sigma^{(3)}(y)
\left[1-\frac1{20}\sum_j\ell_j^2H_4(y_j/\sigma)\right]
+R_\ell(y),
\tag{2.3}
\]

with

\[
|R_\ell(y)|\le C rW(1+|y|)^{-8}.
\tag{2.4}
\]

The cross-products of two second-order terms are `O(W^2)=O(r^2W)`, while `sum ell_j^3<=rW`.

## 3. Uniform quadratic pushforward and global-mode reduction

For `T_u` the pushforward by `q_u(y)=y^TB_uy`, orthogonal invariance reduces the radial error to the standard form `z_1^2+z_2^2-z_3^2`. For

\[
w(y)=(1+|y|)^{-8},
\]

cylindrical coordinates give the uniform bound

\[
\sup_{u,s}T_uw(s)
\le \pi\int_{\mathbb R}(1+|z|)^{-8}\,dz
=\frac{2\pi}{7}.
\tag{3.1}
\]

Hence

\[
p_{\ell,u}(s)
=p_0(s)-\frac1{20}\sum_j\ell_j^2J_{u,j}(s)+O(rW)
\tag{3.2}
\]

uniformly in `(u,s)`, where

\[
J_{u,j}(s)
=T_u\left[\gamma_\sigma^{(3)}(y)H_4(y_j/\sigma)\right].
\tag{3.3}
\]

The same radial formula with polynomial-Gaussian integrand makes `J_{u,j}` jointly continuous in `(u,s)`, with a uniform modulus on compact `u`.

At `ell=0`, isotropy removes `u`; in a spectral basis

\[
Q_0=G_1^2+G_2^2-G_3^2.
\]

Since `G_1^2+G_2^2` is exponential with rate 6,

\[
p_0(s)=M e^{-6s},\qquad s\ge0.
\tag{3.4}
\]

For `a>0`, if `b` is the density of `G_3^2`,

\[
p_0(-a)=\int_0^\infty 6e^{-6w}b(w+a)\,dw<M,
\tag{3.5}
\]

because `b` is strictly decreasing. Thus `s=0` is the unique global maximizer of `p_0`.

Equation (3.2) gives `p_{ell,u}->p_0` uniformly at rate `O(W)`, so every maximizing (or asymptotically maximizing) output tends uniformly to zero. Joint continuity of all `J_{u,j}` then implies

\[
\|p_{\ell,u}\|_\infty
=p_0(0)-\frac1{20}\sum_j\ell_j^2J_{u,j}(0)+o(W)
\tag{3.6}
\]

uniformly in orientation and leverage direction. This is the same product-safe global-mode upgrade proved in the completed partner account02/B17 theorem cited in Section 7 below; here it is applied to the three-coordinate signed perturbation (2.3).

## 4. Exact cone moments

Scale by `sigma` and let `Z` be standard Gaussian. Under the normalized Gaussian `delta(q_u(Z))` measure at the cone tip, write

\[
Z=R\omega,\qquad
\omega=\frac{\varepsilon u+v(\theta)}{\sqrt2},
\]

where `epsilon=+/-1` is symmetric, `v(theta)` is uniform on the unit circle in `u^perp`, and the radial law has density proportional to `e^{-R^2/2}` on `[0,infty)`. Therefore

\[
E R^2=1,\qquad ER^4=3.
\tag{4.1}
\]

Put `x_j=u_j^2`. Circular moments give

\[
E\omega_j^2=\frac{1+x_j}{4},
\qquad
E\omega_j^4=\frac{3+18x_j-13x_j^2}{32}.
\tag{4.2}
\]

Consequently

\[
\frac{J_{u,j}(0)}{p_0(0)}
=E[H_4(Z_j)\mid q_u(Z)=0]
=3E\omega_j^4-6E\omega_j^2+3
=\boxed{\frac{57+6x_j-39x_j^2}{32}}.
\tag{4.3}
\]

Substituting (4.3) into (3.6) proves (1.4).

## 5. Sharp orientation optimization

Let `w_j=ell_j^2`. Multiplying (1.3) by 640 gives

\[
F_w(x)=57W+6\sum_jw_jx_j-39\sum_jw_jx_j^2,
\qquad x_j\ge0,\quad\sum_jx_j=1.
\tag{5.1}
\]

`F_w` is concave on the simplex, so its minimum is attained at a vertex. At `x=e_k`,

\[
F_w(e_k)=57W-33w_k.
\tag{5.2}
\]

The minimum therefore occurs at an index with `w_k=w_*`, proving the first identity in (1.5). Since `w_*<=W`,

\[
57W-33w_*\ge24W,
\]

which proves the second inequality. The remainder in (1.4) is uniform and is `O(rW)`, so choosing one absolute `r_0` makes it at most half of the minimum penalty and proves (1.6).

This exact optimization identifies the dangerous orientation: **the negative eigendirection aligns with whichever orthogonal heavy row has the largest leverage.** Mixing that negative direction between heavy axes only increases the second-order deficit.

## 6. Explicit dense rotated stress family

For the fully coupled orientation

\[
u_*=(1,1,1)/\sqrt3,
\qquad
B_*=I-2u_*u_*^T
=\frac13
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix},
\tag{6.1}
\]

all entries are nonzero. Taking equal heavy leverage

\[
\ell_1=\ell_2=\ell_3=\ell
\]

gives `x_j=1/3` and

\[
\boxed{
D_{u_*}(\ell,\ell,\ell)=\frac{41}{160}\ell^2,}
\tag{6.2}
\]

so

\[
\boxed{
\|p_{(\ell,\ell,\ell),u_*}\|_\infty
=3\sqrt2\left[1-\frac{41}{160}\ell^2+o(\ell^2)\right].}
\tag{6.3}
\]

Uniformly over all orientations with three equal heavies, (1.5) improves to

\[
D_u(\ell,\ell,\ell)\ge\frac{69}{320}\ell^2.
\tag{6.4}
\]

Now realize this with genuinely independent physical coordinates. For finite `m`, let `C_{m,ell}` have, for each `j=1,2,3`, one column `sqrt(ell)e_j` and `m` columns `sqrt((1-ell)/m)e_j`. Then

\[
C_{m,\ell}C_{m,\ell}^T=I_3,
\tag{6.5}
\]

and

\[
A_{m,\ell}=C_{m,\ell}^TB_*C_{m,\ell}
\tag{6.6}
\]

has exact nonzero spectrum `{1,1,-1}` for every finite `m`. Put independent `Unif[-1/2,1/2]` laws on all `3(m+1)` physical coordinates. Every input density is exactly one. Since every entry of `B_*` and every column scale in `C_{m,ell}` is nonzero for `0<ell<1`, **every entry of the physical matrix `A_{m,ell}` is nonzero**: this is an exact dense rotated stress, not a diagonal/pi control.

For `ell<=1/2` and `m>=2`, every row leverage in the rank-three frame is at most `1/2`. The pinned Fresnel--Brascamp--Lieb Theorem F,

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,

gives the actual finite-matrix characteristic-function bound

\[
|\phi_{m,\ell,u}(t)|
\le\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.
\tag{6.7}
\]

The right side is integrable. The three residual banks converge jointly to the Gaussian components in (1.1), hence dominated convergence in Fourier space gives

\[
\boxed{
\|p_{m,\ell,u}-p_{\ell,u}\|_\infty\to0
\qquad(m\to\infty).}
\tag{6.8}
\]

This also supplies a continuous density representative for every finite matrix in this scoped leverage regime and for the limit model; no unrestricted continuity claim is made.

Combining (6.3), (6.4), and (6.8): for each sufficiently small fixed positive `ell`, all sufficiently large finite dense matrices (6.6) have global density peak strictly below `3sqrt(2)`.

Conversely choose `ell_k downarrow0` and then `m_k` so large that (6.8) is within `1/k`, with additionally `m_k ell_k -> infinity`. The distinguished physical-row leverage `ell_k` is then arbitrarily larger than each residual-bank leverage `(1-ell_k)/m_k`, every finite matrix is dense and has exact spectrum `{1,1,-1}`, yet

\[
\|p_{Q_{m_k,\ell_k,u_*}}\|_\infty\to3\sqrt2.
\tag{6.9}
\]

Thus this exact rotated source-valid family independently preserves the lower obstruction

\[
\boxed{C_{\rm univ}\ge3\sqrt2.}
\tag{6.10}
\]

It also shows that near-saturation cannot be reduced to frames whose physical leverages are all comparable: three distinguished rows may be parametrically heavier than the diffuse remainder while the peak still approaches the obstruction.

## 7. Completed partner result actually applied

Required partner source:

`yspennstate/math-open-problems@1db8b3d52c99a32e0ce352173f7023c69cdbdae3`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T104613Z-account02-B17-QFORM-auto11c/REPORT.md`.

The partner theorem proves, for the exact face

\[
(\ell_1,\ell_2,\ell_3)=(\ell,\ell,0),
\]

that

\[
\|p_{\ell,u}\|_\infty
=M[1-c_{12}(u)\ell^2+o(\ell^2)],
\]

uniformly in `u`, with

\[
c_{12}(u)=\frac{114+6(u_1^2+u_2^2)-39(u_1^4+u_2^4)}{640}
\ge\frac{81}{640}.
\]

I apply that completed result to the actual two-heavy face of (1.1): there is a single `delta_p>0` such that

\[
\boxed{
0<\ell\le\delta_p
\Longrightarrow
\sup_{u\in S^2}\|p_{(\ell,\ell,0),u}\|_\infty
\le3\sqrt2\left(1-\frac{81}{1280}\ell^2\right).
}
\tag{7.1}
\]

This is a genuine inequality, not a citation-only comparison. It is also the exact two-coordinate face of the new coefficient formula: from (1.3),

\[
D_u(\ell,\ell,0)=c_{12}(u)\ell^2.
\]

The partner's Section 5 global-mode argument is then applied to the new three-coordinate signed perturbation (2.3), yielding the off-zero upgrade in Section 3. The orientation minimization in Section 5 extends its `81/640` face constant sharply to arbitrary unequal triples.

For the partner's fully coupled `u_*`, the two-heavy coefficient is `41/240`; adding the third equal heavy changes it to the exact three-heavy coefficient `41/160` in (6.2).

## 8. What this constrains, and what remains unpaid

The theorem closes a nontrivial local witness mechanism: **no small insertion of one, two, or three mutually orthogonal macroscopic uniform physical rows into an isotropic diffuse rank-three obstruction can push the global peak above `3sqrt(2)`**. The penalty is quadratic because variance matching kills the linear term; its exact orientation is (1.3), and the dangerous signature direction is characterized by (1.5).

This does NOT prove the unrestricted QFORM theorem and does NOT prove that `3sqrt(2)` is the global sharp constant. The remaining sharp-witness frontier includes intermediate leverage outside the perturbative regime, multiple non-orthogonal/shared-coordinate heavy rows, finite/mesoscopic non-Gaussian residual banks whose surviving component is dependent on the heavy core, and genuinely multiscale fragmentation not reducible to the orthogonal-bank completion above.

No scheduler state, task identity, notification state, email state, permissions, public release, or cross-account authentication was changed in this run.
