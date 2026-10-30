# fleet01/B06 r52 — rank-one hub transverse P2 weighted curved-fiber receiver

**Run:** `20260924T093818Z-fleet01-B06-QFORM-r52`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** curved fiber integration / analytic exact identities  
**Status:** new supporting theorem; full target **OPEN**; global continuity **OPEN**  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (repository transport only; no authenticated native receiver-use evidence)

## 1. Exact target and scope

The target is: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove that the quadratic form has a density with one universal essential-supremum bound, or produce a valid counterexample. No Gaussian, log-concavity, moment, compact-support, connected-support, or diagonal-basis assumption is used below. In particular, no rotated pair of input coordinates is treated as independent.

The result in this report is a supporting endpoint for an **exact rank-one three-coordinate physical hub**. It proves essential boundedness when a two-dimensional transverse tail packet is nonzero. It does not prove the unrestricted conjecture and does not prove continuity of the output density.

## 2. Setup

Let the three literal original coordinates in a physical hub be

\[
Y=(Y_1,Y_2,Y_3),
\]

and let `Z` be a disjoint bank of original independent coordinates. Assume all coordinates in `(Y,Z)` are independent and have probability densities bounded by one. Consider

\[
Q=Y^T K Y+2Y^T MZ+2a^T Y+G(Z),
\]

where `G` is an arbitrary measurable quadratic-plus-affine expression in the tail coordinates (indeed, its exact form will never be used). Suppose

\[
K=\lambda uu^T,\qquad \|u\|_2=1,\qquad \lambda\ne0.
\]

Let

\[
P_\perp=I_3-uu^T.
\]

Choose any orthonormal basis `(v_1,v_2)` of `u^\perp`, write

\[
B=\begin{pmatrix}v_1^TM\\ v_2^TM\end{pmatrix},
\qquad
\Delta_\perp=\sqrt{\det(BB^T)}.
\]

The number `Delta_perp` is independent of the chosen orthonormal basis: it is the product of the two nonzero singular values of the map `P_perp M` when that map has rank two.

## 3. The theorem

### Theorem — `QFORM-RANKONE-HUB-TRANSVERSE-P2-WEIGHTED-v1`

If `Delta_perp>0`, then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le C_* |\lambda|^{-1/2}\Delta_\perp^{-1/4},
}
\]

where

\[
C_*={4\over3}2^{7/4}6^{1/4}(\pi e)^{1/4}
=11.9988639827\ldots<12.
\]

Thus, more simply,

\[
\boxed{
\|p_Q\|_\infty<12|\lambda|^{-1/2}\Delta_\perp^{-1/4}.
}
\]

This conclusion is only essential boundedness; continuity is not proved here.

## 4. A physical-coordinate geometry lemma

Fix `z` and define

\[
b=b(z)=Mz+a.
\]

Decompose

\[
b=b_\parallel u+b_\perp,
\qquad
\beta=\|b_\perp\|_2.
\]

For `beta>0`, let

\[
v={b_\perp\over\beta}\in u^\perp,
\qquad
w=u\times v.
\]

Then `(u,v,w)` is an orthonormal basis of `R^3`. For `k=1,2,3`, put

\[
g_k=|w_k|\sqrt{1-u_k^2}.
\]

We claim

\[
\boxed{\max_k g_k\ge {1\over\sqrt6}.}
\]

Indeed,

\[
\sum_k g_k^2
=\sum_k w_k^2(1-u_k^2)
=1-\sum_k u_k^2w_k^2.
\]

Set `p_k=u_k^2+w_k^2`. Since `u,w` are orthonormal, `0<=p_k<=1` and `sum p_k=2`. By `u_k^2w_k^2<=(p_k^2)/4`,

\[
\sum_k u_k^2w_k^2
\le {1\over4}\sum_kp_k^2
\le {1\over2},
\]

because the maximum of `sum p_k^2` on `0<=p_k<=1`, `sum p_k=2`, is `2`. Hence `sum g_k^2>=1/2`, so at least one `g_k^2>=1/6`.

This selects a **literal original coordinate** `Y_k`; it does not rotate the independent input pair.

## 5. Conditional parabolic fiber on two original coordinates

For fixed `z`, choose the least `k` attaining the preceding bound; this is a measurable choice away from the null set `beta=0`. Condition additionally on the literal original coordinate `Y_k`. Let `I={1,2,3}\setminus{k}`. The remaining two literal independent coordinates are `Y_I`.

Write

\[
r=\|u_I\|_2=\sqrt{1-u_k^2}.
\]

The quadratic part on this physical pair is rank one. In the orthonormal coordinates intrinsic to the algebra of the pair (used only to identify coefficients, not to assert probabilistic independence), its nonzero quadratic coefficient is

\[
\theta=\lambda r^2.
\]

Let `n_I` be a unit vector in `R^2` perpendicular to `u_I`. The null-direction coefficient of the linear term has magnitude

\[
|\beta_{\rm pair}|
=|n_I^Tb_I|
=\beta {|\det(u_I,v_I)|\over r}
=\beta {|w_k|\over r}.
\]

The extra linear term created by conditioning on `Y_k` is parallel to `u_I`, so it contributes nothing to this null direction. Consequently

\[
|\theta\beta_{\rm pair}|
=|\lambda|\beta r|w_k|
=|\lambda|\beta g_k
\ge {|\lambda|\beta\over\sqrt6}.
\]

Now apply the previously proved fleet01/B06 theorem `QFORM-PARABOLIC-PRODUCT-FIBER-v1` to these **two literal original independent coordinates**. It states that for a rank-one quadratic pair with nonzero quadratic coefficient `theta` and transverse null-direction slope `beta_pair`, arbitrary translation and additive constant retained,

\[
\|p\|_\infty\le {2^{7/4}\over\sqrt{|\theta\beta_{\rm pair}|}}.
\]

Therefore, conditionally on `(Z=z,Y_k)`,

\[
\boxed{
\|p_{Q\mid Z=z,Y_k}\|_\infty
\le 2^{7/4}6^{1/4}|\lambda|^{-1/2}\beta^{-1/2}.
}
\]

Averaging over `Y_k` preserves the same right-hand side.

## 6. Actual application of the designated fleet02/B06 product theorem

The remaining random vector is

\[
V=P_\perp(MZ+a)\in u^\perp.
\]

In the chosen orthonormal coordinates of `u^\perp`, this is `BZ+c`. The completed fleet02/B06 theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` gives for a rank-two linear image of independent cap-one coordinates

\[
\boxed{
\|p_V\|_\infty\le {e\over\sqrt{\det(BB^T)}}={e\over\Delta_\perp}.
}
\]

This is the designated partner result applied to the actual inequality needed in this proof. It uses original product structure before any curved integration.

For completeness, if an `R^2`-valued random vector `V` has density at most `L`, symmetric decreasing rearrangement (equivalently the bathtub principle) gives

\[
\mathbb E\|V\|^{-1/2}
\le {4\over3}(\pi L)^{1/4}.
\]

Indeed the maximizing density is `L` on the centered disk of radius `R=(pi L)^(-1/2)`, and

\[
L\,2\pi\int_0^R r^{1/2}\,dr
={4\over3}(\pi L)^{1/4}.
\]

Applying this with `L=e/Delta_perp` yields

\[
\mathbb E\beta^{-1/2}
\le {4\over3}\left({\pi e\over\Delta_\perp}\right)^{1/4}.
\]

Since `Delta_perp>0`, `V` has a two-dimensional density and therefore `beta=0` is null. Averaging the conditional density cap from Section 5 proves

\[
\|p_Q\|_\infty
\le {4\over3}2^{7/4}6^{1/4}(\pi e)^{1/4}
|\lambda|^{-1/2}\Delta_\perp^{-1/4}.
\]

This proves the theorem.

## 7. Exact aggregate P2 identity

The preceding continuous parameter `Delta_perp` is exactly the complete one-hub/two-tail physical minor packet. Let `m_p` be the `p`th column of `M`, and define

\[
P_2
=\sum_{i=1}^3\sum_{p<q}
\det[\,K_{:i},m_p,m_q\,]^2.
\]

Since `K_:i=lambda u_i u`,

\[
\begin{aligned}
P_2
&=\lambda^2\sum_i u_i^2
  \sum_{p<q}\det[u,m_p,m_q]^2\\
&=\lambda^2\sum_{p<q}\det[u,m_p,m_q]^2.
\end{aligned}
\]

In any orthonormal basis of `u^perp`, `det[u,m_p,m_q]` is exactly, up to sign, the `2x2` determinant formed by the projected columns of `B`. Cauchy--Binet therefore gives

\[
\boxed{P_2=\lambda^2\det(BB^T)=\lambda^2\Delta_\perp^2.}
\]

Thus the theorem is equivalently

\[
\boxed{
\|p_Q\|_\infty
<12\,(\lambda^2P_2)^{-1/8}.
}
\]

This is an aggregate-before-inversion certificate: the entire P2 bank is summed before any reciprocal cost is paid. No largest-minor extraction is used.

## 8. Exact flat survivor when P2 vanishes

If `P_2=0`, then `Delta_perp=0`, so

\[
\operatorname{rank}(P_\perp M)\le1.
\]

Therefore there exist `v in u^perp` and tail coefficient vectors `alpha,beta` such that

\[
\boxed{M=u\alpha^T+v\beta^T,}
\]

with the convention `beta=0` if the transverse projection is zero. Thus every tail coupling from the exact rank-one hub lives in at most two hub directions. This is a structural classification only, not a bounded-density proof for this survivor.

## 9. Relation to the current three-hub compiler and remaining debt

The completed fleet02/B06 r15 compiler already pays the branch `sigma_2(K)>=1/64` with a finite target-level constant. The present theorem reaches the opposite exact endpoint `sigma_2(K)=0` whenever the complete transverse P2 packet is nonzero.

The remaining local transition is therefore narrower:

**`QFORM-NEARRANKONE-HUB-OR-P2FLAT-TWODIRECTION-ROUTING-v1`.**

It contains two debts:

1. the collar `0<sigma_2(K)<1/64`, where the small hub remainder cannot simply be deleted; and
2. the exact rank-one/P2-flat survivor `M=u alpha^T+v beta^T`, where all hub-tail coupling occupies at most two hub directions and the third large spectral direction must be forced from the retained tail self-curvature or a larger grouped original-coordinate block.

Any next receiver must keep arbitrary same-bank `G(Z)` and original-coordinate product structure. It may not infer a large individual minor from aggregate mass, may not rotate the inputs and retain independence, and may not take an unrestricted curved-fiber supremum.

## 10. Regularity and target status

- Essential boundedness: **proved only in the theorem's stated `Delta_perp>0` exact-rank-one-hub branch**.
- Continuous density: **not proved by this argument**.
- Full arbitrary-dimensional QFORM theorem: **OPEN**.
- Target counterexample: **none found**.

## 11. Source pins

Owner source message:
`https://github.com/yspennstate/math-research-brain/blob/0dc369ddf8b860648dd780d8f92c62994dc53ecf/scheduled_tasks/README.md`

Current B06 predecessor consumed:
`yspennstate/math-open-problems@3a6a071259b600b9abd468d55a6e220d5d621e85:proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B06/20260924T083427Z-fleet01-B06-QFORM-r51/REPORT.md`

Designated partner theorem consumed:
`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`, theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`.

Numerical checks, if present beside this report, are sanity checks only and are not used as proof.