SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B15, 2026-09-24T05:03:54Z.
attacking: a uniform submass stability theorem on the ruled one-sheet, with exact rough-input interval passage and no use of continuity to create height.

# account02/B15 — a uniform square-root submass theorem on the isotropic ruled sheet

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T050354Z-account02-B15-QFORM-auto11-r1`  
Status: `RULED-SUBMASS-SQRT-PROVED / ROUGH-INTERVAL-BRIDGE-PROVED / EXPONENT-SHARP / FULL-QFORM-OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact contribution and the first unpaid implication

The unrestricted theorem remains OPEN. This report proves a new matrix-uniform regularity estimate in the exact target chamber consisting of the isotropic rank-three indefinite forms

\[
q(X)=\langle r_1,X\rangle^2+\langle r_2,X\rangle^2-\langle r_3,X\rangle^2,
\qquad r_1,r_2,r_3\ \text{orthonormal in }\mathbb R^n.
\]

The result is stronger than a height bound for probability inputs: it gains the sharp exponent `sqrt(m)` when one original-coordinate density is replaced by an arbitrary cap-one subdensity of mass `m`.

This is useful because the latest designated partner account03/B15 proved the same `sqrt(m)` exponent for every fixed rank-at-least-three matrix, but with a constant `K(A,j)` that may blow up along diffuse matrix families. Here the constant is absolute, independent of `n`, the orientation of the spectral frame, and the chosen original coordinate, on the completed ruled one-sheet.

The first unpaid implication after this report is not rough-input limiting and is not continuity. It is to obtain an analogous matrix-uniform aggregate estimate on the complementary convex/two-sheet side and through the structural higher-rank/no-good-pivot configurations, or otherwise route every such configuration into an already-paid receiver before reciprocal local-minor losses are taken.

## 2. Height language: no continuity premise

For a finite positive measure `nu` on `R`, define

\[
H(\nu)=\sup_{I:\,|I|>0}\frac{\nu(I)}{|I|}.
\]

If `H(nu)<infinity`, then `nu<=H(nu) dx`; in particular `nu` has an essentially bounded density. Thus all rough-input conclusions below are formulated first as interval domination. A continuous representative, when available from another theorem, is downstream and is never used to produce the height.

## 3. Source-pinned ruled input

The required source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its completed Theorem C gives the one-sheet estimate for signature `(+,+,-)`. In the isotropic coordinates

\[
q_0(y)=y_1^2+y_2^2-y_3^2,
\]

the level `q_0=s>=0` has ruling

\[
F(\theta,t)=\sqrt{s}\,e_\theta+t(e_\theta^\perp+e_3),
\]

and the source proves the exact coarea identity

\[
\delta(q_0-s)\,dy=\frac12\,d\theta\,dt. \tag{3.1}
\]

It then bounds each ruling line integral by a two-dimensional projection density of the original product law, whose universal cap is `2`. This yields the completed probability-input inequality

\[
\Pr\{q(X)\in I,\ q(X)\ge0\}\le \pi\sqrt2\,|I|. \tag{3.2}
\]

The later source audit requires an affine term to lie in the quadratic range. The theorem proved here is homogeneous, so this correction is automatically respected.

## 4. New theorem: uniform square-root submass gain

### Theorem 4.1 — `QFORM-RULED-SUBMASS-SQRT-UNIFORM-v1`

Let `R` be an `n x 3` matrix with orthonormal columns and rows `r_i in R^3`. Let the original coordinates be independent. For `i!=j`, let `f_i` be probability densities with `0<=f_i<=1`. In coordinate `j`, let `g` be an arbitrary measurable subdensity with

\[
0\le g\le1,\qquad \int g=m\in[0,1].
\]

Put

\[
Y=R^T X,\qquad q(X)=Y_1^2+Y_2^2-Y_3^2.
\]

Let `nu_g^+` be the positive output submeasure

\[
\nu_g^+(B)=\int \mathbf 1_{\{q(x)\in B\cap[0,\infty)\}}
 g(x_j)\prod_{i\ne j}f_i(x_i)\,dx.
\]

Then

\[
\boxed{H(\nu_g^+)\le20\sqrt2\,\sqrt m.} \tag{4.1}
\]

Equivalently, `nu_g^+` has an essentially bounded density `r_g^+` and

\[
\boxed{\|r_g^+\|_\infty\le20\sqrt2\,\sqrt m.} \tag{4.2}
\]

The constant is independent of `n`, `R`, `j`, the source laws, and `m`.

### Proof for smooth original-coordinate inputs

Let `rho_g` be the three-dimensional projected subdensity of `Y=R^T X`. For `s>=0`, the ruled formula (3.1) gives

\[
r_g^+(s)=\frac12\int_0^{2\pi}\int_{\mathbb R}
 \rho_g(\sqrt{s}e_\theta+t v_\theta)\,dt\,d\theta,
\qquad
v_\theta=e_\theta^\perp+e_3. \tag{4.3}
\]

Here `|v_theta|=sqrt(2)`. Let

\[
\widehat v_\theta=v_\theta/\sqrt2
\]

and let `U_theta` be a `2 x 3` matrix with orthonormal rows spanning `widehat v_theta^perp`. If `h_theta` denotes the two-dimensional density of the projection `U_theta Y`, then a line parameterised by `t v_theta` has arclength element `sqrt(2) dt`, so

\[
\int_{\mathbb R}\rho_g(y_0+t v_\theta)\,dt
=\frac1{\sqrt2}h_\theta(U_\theta y_0). \tag{4.4}
\]

The reciprocal speed in (4.4) is the same non-arclength factor that is essential in the source theorem.

Write

\[
b_i(\theta)=U_\theta r_i\in\mathbb R^2.
\]

Because the columns of `R` are orthonormal,

\[
\sum_i b_i b_i^T=I_2. \tag{4.5}
\]

Removing coordinate `j` leaves Gram matrix

\[
G_\theta=\sum_{i\ne j}b_i b_i^T=I_2-b_jb_j^T,
\qquad
\det G_\theta=1-|b_j|^2=:d_j(\theta). \tag{4.6}
\]

There are two independent bounds on `h_theta`.

First, complete `g` to a cap-one probability density `g+a`: choose `a>=0`, `a<=1-g`, `int a=1-m`. The projected submeasure generated by `g` is dominated by the projected probability measure generated by `g+a`. The two-dimensional product-projection theorem used in Theorem C therefore gives

\[
h_\theta\le2. \tag{4.7}
\]

Second, condition on `X_j`. For `d_j(theta)>0`, the projection of the remaining product probability law has linear map Gram matrix `G_theta`; after multiplication by `G_theta^{-1/2}` its two rows are orthonormal. The same two-dimensional projection theorem gives density cap

\[
\frac2{\sqrt{\det G_\theta}}.
\]

Integrating the conditional translate against `g`, whose total mass is `m`, gives

\[
h_\theta\le\frac{2m}{\sqrt{d_j(\theta)}}. \tag{4.8}
\]

At `d_j(theta)=0`, interpret the second bound as `+infinity`. Combining (4.7)--(4.8),

\[
\boxed{
h_\theta\le2\min\!\left(1,\frac{m}{\sqrt{d_j(\theta)}}\right).
} \tag{4.9}
\]

It remains to average the possible near-singularity of `G_theta` over the ruling angle.

Write the selected row as

\[
r_j=(u_1,u_2,c),\qquad \ell=|r_j|\le1.
\]

Since `U_theta` projects orthogonally to `widehat v_theta`,

\[
d_j(\theta)
=1-\ell^2+
\frac{(-u_1\sin\theta+u_2\cos\theta+c)^2}{2}. \tag{4.10}
\]

Set

\[
z(\theta)=\sqrt{d_j(\theta)},
\qquad
F(t)=\operatorname{Leb}\{\theta\in[0,2\pi):z(\theta)<t\}.
\]

We claim the uniform sublevel estimate

\[
\boxed{F(t)\le20\sqrt t\quad(t>0).} \tag{4.11}
\]

For `t>1/8`, this follows from `F(t)<=2pi<20 sqrt(t)`. Let `0<t<=1/8`. If `z(theta)<t`, then from (4.10)

\[
\ell^2>1-t^2\ge\frac{63}{64},
\quad
|-u_1\sin\theta+u_2\cos\theta+c|<\sqrt2\,t. \tag{4.12}
\]

Put `A=sqrt(u_1^2+u_2^2)`. If `A<1/4`, then

\[
|c|>\sqrt{59}/8,
\]

so the left side of the second inequality in (4.12) is at least

\[
|c|-A>(\sqrt{59}-2)/8>\sqrt2/8,
\]

contradicting `t<=1/8`. Hence `A>=1/4`.

After a phase shift the second condition in (4.12) is

\[
|\cos\phi-q|<\varepsilon,
\qquad
\varepsilon=\frac{\sqrt2 t}{A}\le4\sqrt2\,t. \tag{4.13}
\]

For every real `q` and `epsilon>0`, the elementary arcsine estimate

\[
\operatorname{Leb}\{\phi\in[0,2\pi):|\cos\phi-q|<\varepsilon\}
\le8\sqrt\varepsilon \tag{4.14}
\]

holds. One proof is to write the preimage measure as

\[
2\int_J(1-x^2)^{-1/2}\,dx,
\]

where `J` is an interval of length at most `2epsilon` inside `[-1,1]`; the integral is maximised at an endpoint, where it is `O(sqrt(epsilon))`, and the stated constant is a safe uniform choice. Applying (4.14) to (4.13) yields

\[
F(t)\le16\,2^{1/4}\sqrt t<20\sqrt t,
\]

proving (4.11).

Now use the exact layer-cake identity

\[
\min(1,m/z)=\int_0^1\mathbf 1_{\{z<m/u\}}\,du. \tag{4.15}
\]

Tonelli and (4.11) give

\[
\begin{aligned}
\int_0^{2\pi}\min\!\left(1,\frac m{z(\theta)}\right)d\theta
&=\int_0^1F(m/u)\,du\\
&\le20\sqrt m\int_0^1u^{-1/2}\,du\\
&=40\sqrt m. \tag{4.16}
\end{aligned}
\]

Finally (4.3), (4.4), (4.9), and (4.16) imply

\[
\begin{aligned}
r_g^+(s)
&\le \frac1{2\sqrt2}\int_0^{2\pi}h_\theta\,d\theta\\
&\le \frac1{\sqrt2}\int_0^{2\pi}
 \min\!\left(1,\frac m{z(\theta)}\right)d\theta\\
&\le20\sqrt2\,\sqrt m.
\end{aligned} \tag{4.17}
\]

This proves the smooth-input version of (4.1)--(4.2).

## 5. Rough-input bridge with zero height loss

The theorem is required for arbitrary measurable cap-one factors. No continuity argument is needed.

Choose a nonnegative probability approximate identity `rho_eta` and mollify only the original-coordinate factors:

\[
g^{(\eta)}=g*\rho_\eta,
\qquad
f_i^{(\eta)}=f_i*\rho_\eta.
\]

Then

\[
0\le g^{(\eta)},f_i^{(\eta)}\le1,
\qquad
\int g^{(\eta)}=m,
\qquad
\int f_i^{(\eta)}=1,
\]

and each factor converges in `L1`. The product subdensities satisfy

\[
\left\|
 g^{(\eta)}\prod_{i\ne j}f_i^{(\eta)}
-g\prod_{i\ne j}f_i
\right\|_1
\le
\|g^{(\eta)}-g\|_1
+m\sum_{i\ne j}\|f_i^{(\eta)}-f_i\|_1
\longrightarrow0. \tag{5.1}
\]

Restriction to the fixed event `{q>=0}` and deterministic pushforward by `q` both contract total variation. Hence, for every interval `I`,

\[
\nu_{g,\eta}^+(I)\to\nu_g^+(I). \tag{5.2}
\]

The smooth theorem gives

\[
\nu_{g,\eta}^+(I)\le20\sqrt2\sqrt m\,|I|
\]

with a constant independent of `eta`. Passing to the limit in (5.2) proves exactly

\[
\boxed{
\nu_g^+(I)\le20\sqrt2\sqrt m\,|I|
} \tag{5.3}
\]

for arbitrary rough cap-one inputs. Therefore `nu_g^+` is absolutely continuous with an `L-infinity` density bounded by the same constant. No pointwise trace of a rough representative and no output continuity enter.

This is also an independent check of the ruled rough-input bridge requested by the owner: the smooth coarea geometry is used only before the limit; the actual rough statement is transported as an interval inequality by total variation.

## 6. Uniform `L1`-to-output-`Linf` stability on the majority sheet

Let two cap-one probability densities `f_j` and `g_j` be used in one original coordinate, with all other marginals fixed, and set

\[
\delta=\|f_j-g_j\|_1.
\]

Write

\[
f_j-g_j=h_+-h_-,
\qquad
h_+=(f_j-g_j)_+,
\quad
h_-=(g_j-f_j)_+.
\]

Since both marginals have mass one,

\[
\int h_+=\int h_-=\delta/2.
\]

Apply Theorem 4.1 to the two positive submasses and subtract their output densities. Then

\[
\begin{aligned}
\|r_f^+-r_g^+\|_\infty
&\le20\sqrt2\left(\sqrt{\delta/2}+\sqrt{\delta/2}\right)\\
&=40\sqrt\delta.
\end{aligned}
\]

Thus

\[
\boxed{
\|r_f^+-r_g^+\|_\infty\le40\,\|f_j-g_j\|_1^{1/2}.
} \tag{6.1}
\]

Unlike the partner's fixed-matrix theorem, the constant `40` is uniform over all dimensions and all orientations of the isotropic rank-three frame, but only for the ruled one-sheet component.

## 7. The exponent `1/2` is sharp on the same ruled sheet

The newest designated partner account03/B15 result is

`yspennstate/math-open-problems@696a0784ba7d270db657c1596d9c2ee940a1745d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T032517Z-account03-B15-qform-auto32/REPORT.md`.

For the exact owner-target form

\[
Q=2XY+Z^2,
\]

with `Y,Z` iid `Unif[0,1]`, compare

\[
f_X=\mathbf1_{[0,1]},
\qquad
g_X=\mathbf1_{[m,1]}+\mathbf1_{[2,2+m]},
\qquad
0<m<1/2.
\]

Then

\[
\delta=\|f_X-g_X\|_1=2m
\]

and the partner computes exactly

\[
\boxed{
|p_f(\delta)-p_g(\delta)|
=\sqrt\delta\left[
1-\log2-\frac12\log\left(1+\frac\delta4\right)
\right].
} \tag{7.1}
\]

Because all three sources are supported in `[0,infinity)`, one has `Q>=0` almost surely. Thus (7.1) lies **entirely on the same ruled majority sheet** treated by (6.1). Consequently, for every `alpha>1/2`, there is no finite class-uniform constant `C_alpha` satisfying

\[
\|r_f^+-r_g^+\|_\infty
\le C_\alpha\|f_j-g_j\|_1^\alpha
\]

even for this one fixed target matrix.

The new upper theorem and the partner lower construction therefore identify the optimal stability exponent:

\[
\boxed{\text{majority-sheet marginal }L^1\to\text{output }L^\infty\text{ exponent}=1/2.} \tag{7.2}
\]

The constant is not claimed sharp.

## 8. Real target inequality obtained from the required source

Take again

\[
Q=2XY+Z^2.
\]

Its symmetric matrix has eigenvalues `{1,-1,1}`, so it exactly satisfies the owner hypothesis. Applying the completed `e5f71d79...` ruled theorem with all three curvature magnitudes equal to one gives the genuine target inequality

\[
\boxed{
\Pr\{2XY+Z^2\in I,\ 2XY+Z^2\ge0\}
\le\pi\sqrt2\,|I|.
} \tag{8.1}
\]

The new submass refinement says that if the `X` factor is any cap-one subdensity of mass `m`, then

\[
\boxed{
\Pr_g\{2XY+Z^2\in I,\ 2XY+Z^2\ge0\}
\le20\sqrt2\sqrt m\,|I|.
} \tag{8.2}
\]

For `m=1`, (8.1) is stronger. The content of (8.2) is the vanishing `sqrt(m)` gain required for input-law stability; (7.1) shows that this exponent is optimal.

At the triangular-kernel scale, (8.1) also gives

\[
\boxed{
\mathbb E[(\varepsilon-|Q-y|)_+\mathbf1_{\{Q\ge0\}}]
\le\pi\sqrt2\,\varepsilon^2.
} \tag{8.3}
\]

This is an essential-density payment, not a continuity consequence.

## 9. Independent geometric audit of the ruled coefficient

For completeness, the two delicate factors in the source are checked directly. With

\[
F(\theta,t)=\sqrt s\,e_\theta+t(e_\theta^\perp+e_3),
\]

a direct cross-product computation gives

\[
F_\theta\times F_t=\frac12\nabla q_0(F). \tag{9.1}
\]

Therefore

\[
\frac{d\sigma}{|\nabla q_0|}=\frac12\,d\theta\,dt. \tag{9.2}
\]

After spectral scaling for curvature magnitudes `(lambda_1,lambda_2,mu)`, the ruling direction is

\[
v_\theta=
\left(-\frac{\sin\theta}{\sqrt{\lambda_1}},
\frac{\cos\theta}{\sqrt{\lambda_2}},
\frac1{\sqrt\mu}\right). \tag{9.3}
\]

The parameter `t` is not arclength, so a line integral expressed through an orthogonal two-dimensional marginal picks up `1/|v_theta|`. The source's two-dimensional projection cap `2` then cancels the coarea factor `1/2`, recovering exactly

\[
C_+=(\lambda_1\lambda_2\mu)^{-1/2}
\int_0^{2\pi}\frac{d\theta}{
\sqrt{\sin^2\theta/\lambda_1+\cos^2\theta/\lambda_2+1/\mu}}. \tag{9.4}
\]

For the rough bridge, one mollifies the **original coordinates**, not the spectral coordinates. Thus independence is never asserted after rotation.

## 10. Regularity ledger

The implications are now separated as follows.

- **Absolute continuity:** if `A!=0` and the joint input law has an `L1` density, local coarea away from the proper critical subspace `ker A` proves that `X^TAX` is absolutely continuous. This is qualitative and supplies no universal height.
- **Essential boundedness:** in this report it is established directly by the interval estimate (5.3), ultimately from the ruled coarea identity and product-projection caps.
- **Continuity:** not used anywhere above. A separate fixed-instance `C_0` compiler may be applied after a height estimate when its hypotheses hold, but continuity does not generate (4.1), (5.3), (6.1), or (8.1).
- **Rough limiting:** carried out at the positive-measure/interval level in total variation, with zero loss in the height constant.

This avoids the prohibited implication `continuity => universal bound` and avoids post-rotation independence.

## 11. What remains

The theorem is deliberately one-sided and isotropic. It does **not** pay the two-sheet/convex side, arbitrary unequal spectral magnitudes with a uniform submass constant, arbitrary additional spectrum, or the global structural step that must identify a uniformly paid receiver from only `s_3(A)>=1`.

The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction remains binding: the missing complementary sheet cannot be replaced by a generic line-X-ray norm with product provenance discarded. The next useful B15 step is therefore to seek an aggregate submass estimate for the complementary side or a product-preserving reduction that feeds it into an existing grouped-bank/hub/Schur receiver before taking worst fibers.

Full QFORM status: **OPEN**.
