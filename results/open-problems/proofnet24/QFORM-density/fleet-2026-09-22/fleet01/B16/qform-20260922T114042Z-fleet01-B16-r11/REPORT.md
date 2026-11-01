# fleet01/B16 — projection-product interaction via X-ray control of ruled quadratic levels

**Run:** `qform-20260922T114042Z-fleet01-B16-r11`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner control revision `2026-09-22.5`  
**Assignment:** `Projection-product interaction`  
**Classification:** `ESSENTIAL_STEP_APPLIED`; full conjecture **OPEN / NOT PROVED**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 0. Live target and corrections consumed

The fresh owner control supersedes the stale FEI assignment. The active target is:

> For every `n`, independent real `X_i` with densities `0<=f_i<=1`, and every real symmetric `A` with at least three eigenvalues of absolute value at least `1`, prove that `Q=X^TAX` has a density with one universal `L^infinity` bound, or produce a genuine counterexample.

I used the current correction state and do **not** use the refuted law-uniform pointwise Fresnel decay, an integrated spectral-fiber supremum, or independence after rotating to the eigenbasis.

Two completed other-worker results are applied substantively.

1. **fleet02/B06**, report `proofnet24/quadratic-form-bounded-density/fleet02/B06/b06-20260922T113045Z-d47192d10a82/REPORT.md`, commit `6902eb62f21a7c833ca27dcca69f34d50e711a7d`, proves that a same-sign spectral pair carries exact Pluecker determinant mass one in physical coordinates, while a flat Hadamard example can make every fixed physical compression tiny. Thus one must aggregate the spectral plane rather than select a large physical minor.
2. **fleet02/B10**, report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B10/20260922T1147Z-qform-rank3-coupled-B10-r1/REPORT.md`, source observed at commit `452586b3a9db037a9c09e4368906d1c3838d1ab3`, proves a triangular hyperbolic-square physical-coordinate theorem and shows that a naive linear average of reciprocal Pluecker-minor constants loses a factor of order `n` on a flat Walsh plane.

The named fleet02/B16 partner had no completed current-programme handoff at the fresh source snapshot; none is fabricated here.

The external input used below is the sharp product-marginal theorem of Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949: if `X` has product density with each scalar factor bounded by one, then every `k`-dimensional orthogonal marginal has density bounded by `2^{k/2}`. In particular, two-dimensional marginals are bounded by `2`.

The new point is that the two-dimensional marginal theorem can be coupled directly to the **ruled geometry of an indefinite quadratic level set**, retaining dependence among the three spectral coordinates. This gives a one-sided target-level density bound for every rank-three `(2,1)` spectral truncation, with no localization to physical coordinates.

---

## 1. The same-sign spectral plane is already globally aggregated

Let `r_1,r_2` be orthonormal vectors and put

\[
Y=(\langle X,r_1\rangle,\langle X,r_2\rangle).
\]

By the two-dimensional product-marginal theorem, `Y` has a density `g` with

\[
\|g\|_\infty\le2.
\tag{1.1}
\]

This immediately turns fleet02/B06's distributed same-sign determinant mass into a global density statement, without selecting any physical pair.

### Proposition 1.1 — `QFORM-SAMESIGN-SPECTRAL-PAIR-PROJECTION-v1`

If `alpha,beta>0`, then

\[
S=\alpha\langle X,r_1\rangle^2+\beta\langle X,r_2\rangle^2
\]

has a density satisfying

\[
\boxed{
\|p_S\|_\infty\le {2\pi\over\sqrt{\alpha\beta}}.
}
\tag{1.2}
\]

The same statement holds after simultaneous sign reversal.

### Proof

Set `u_1=sqrt(alpha) y_1`, `u_2=sqrt(beta) y_2`. The density of `u` is at most

\[
{2\over\sqrt{\alpha\beta}}.
\]

For `s>0`, coarea in polar coordinates gives

\[
\int_{\mathbb R^2}\delta(s-|u|^2)\,du=\pi.
\]

Replacing the transformed density by its `L^infinity` ceiling proves (1.2). The zero level is a null set for the two-dimensional absolutely continuous law and may be assigned any density representative value. `QED`

### Interpretation

For the isolated same-sign spectral component

\[
P=\alpha r_1r_1^T+\beta r_2r_2^T,
\]

there is **no Pluecker localization loss at all**: even in the flat Hadamard example where every useful physical `2x2` determinant is `O(n^{-2})`, the output density of `X^TPX` is bounded by `2pi` when `alpha,beta>=1`.

Thus the B06 determinant mass does not need to be converted into one large physical minor. The sharp marginal theorem has already aggregated the entire spectral plane. What remains difficult in the full conjecture is adding the other spectral components **without pretending they are independent noise**.

---

## 2. X-ray consequence of the product-marginal theorem

Let `E` be a three-dimensional subspace and let

\[
Y=P_E X\in E\cong\mathbb R^3
\]

have density `g`. For every unit vector `v in E`, projection of `Y` onto `v^perp` is exactly the orthogonal projection of `X` onto the two-dimensional subspace `v^perp subset E`. Hence the same theorem gives, for almost every affine line `ell` parallel to `v`,

\[
\boxed{
\int_\ell g\,d\mathcal H^1\le2.
}
\tag{2.1}
\]

This is stronger, for the present geometry, than merely using the three-dimensional pointwise bound `||g||_infinity<=2^{3/2}`. It is an `X`-ray norm bound in **every direction** inside the spectral three-space.

The next theorem spends exactly this line-mass control on the straight rulings of a one-sheet hyperboloid.

---

## 3. Canonical ruled-level identity

Consider

\[
q_0(u)=u_1^2+u_2^2-u_3^2.
\]

Fix a regular positive level `s=a^2>0`. Define

\[
\Phi_a(\theta,t)
=
\bigl(
 a\cos\theta-t\sin\theta,
 a\sin\theta+t\cos\theta,
 t
\bigr),
\qquad 0\le\theta<2\pi,\ t\in\mathbb R.
\tag{3.1}
\]

Then

\[
q_0(\Phi_a(\theta,t))=a^2.
\tag{3.2}
\]

For each fixed `theta`, `t mapsto Phi_a(theta,t)` is a **straight line** on the one-sheet hyperboloid. Moreover

\[
\partial_\theta\Phi_a\times\partial_t\Phi_a
=
\bigl(
 a\cos\theta-t\sin\theta,
 a\sin\theta+t\cos\theta,
 -t
\bigr),
\]

so

\[
|\partial_\theta\Phi_a\times\partial_t\Phi_a|^2=a^2+2t^2,
\]

while

\[
|\nabla q_0(\Phi_a)|^2=4a^2+8t^2.
\]

Therefore the coarea quotient is **exactly constant**:

\[
\boxed{
{d\sigma\over|\nabla q_0|}
={1\over2}\,d\theta\,dt.
}
\tag{3.3}
\]

This identity is the mechanism missing from a fiber-supremum argument: the nonlinear quadratic level decomposes into physical one-dimensional integration objects to which the projection theorem applies directly.

---

## 4. Main theorem: one-sided density bound for every rank-three indefinite spectral truncation

### Theorem 4.1 — `QFORM-RANK3-RULED-MAJORITY-HALF-v1`

Let `X=(X_1,...,X_n)` have independent real coordinates with densities bounded by one. Let `r_1,r_2,r_3` be orthonormal, and let

\[
T
=
\alpha\langle X,r_1\rangle^2
+\beta\langle X,r_2\rangle^2
-\gamma\langle X,r_3\rangle^2,
\qquad
\alpha,\beta,\gamma>0.
\tag{4.1}
\]

Then `T` is absolutely continuous away from its critical level, and for almost every `s>0`,

\[
\boxed{
 p_T(s)
 \le
 \int_0^{2\pi}
 {d\theta\over
 \sqrt{\beta\gamma\sin^2\theta
       +\alpha\gamma\cos^2\theta
       +\alpha\beta}}
 .
}
\tag{4.2}
\]

In particular, if

\[
\alpha,\beta,\gamma\ge1,
\]

then on the majority-sign half-line

\[
\boxed{
\operatorname*{ess\,sup}_{s>0}p_T(s)
\le\sqrt2\,\pi.
}
\tag{4.3}
\]

If the signature is `(1,2)` rather than `(2,1)`, the reflected statement holds on `s<0`.

The same bound is unchanged by adding an arbitrary deterministic linear form in the three spectral coordinates, because completing the square only translates the three-dimensional marginal and the X-ray bounds (2.1) are translation invariant.

### Proof

Let

\[
Y_j=\langle X,r_j\rangle,
\]

and let `g` be the joint density of `Y=(Y_1,Y_2,Y_3)`. Put

\[
D=\operatorname{diag}(\sqrt\alpha,\sqrt\beta,\sqrt\gamma),
\qquad
u=DY,
\]

and denote the density of `nu` by

\[
h(u)={1\over\sqrt{\alpha\beta\gamma}}g(D^{-1}u).
\tag{4.4}
\]

Then

\[
T=q_0(\nu).
\]

Fix `s=a^2>0`. By the regular-level coarea formula and (3.3),

\[
 p_T(s)
 =
 {1\over2}
 \int_0^{2\pi}\int_{\mathbb R}
 h(\Phi_a(\theta,t))\,dt\,d\theta.
\tag{4.5}
\]

For fixed `theta`, write

\[
v_\theta=(-\sin\theta,\cos\theta,1).
\]

The curve `t mapsto Phi_a(theta,t)` is the affine line with direction `v_theta`. Under `D^{-1}` this becomes an affine line in the original spectral coordinates with direction

\[
w_\theta=D^{-1}v_\theta.
\]

Using (4.4), then converting the parameter `t` to Euclidean arclength in the `Y`-space, gives

\[
\begin{aligned}
\int_{\mathbb R}h(\Phi_a(\theta,t))\,dt
&={1\over\sqrt{\alpha\beta\gamma}}
 \int_{\mathbb R}g(y_0+t w_\theta)\,dt\\
&\le
 {2\over
 \sqrt{\alpha\beta\gamma}\,|w_\theta|},
\end{aligned}
\tag{4.6}
\]

where the last step is exactly the two-dimensional marginal/X-ray bound (2.1).

Now

\[
\alpha\beta\gamma|w_\theta|^2
=
\beta\gamma\sin^2\theta
+\alpha\gamma\cos^2\theta
+\alpha\beta.
\tag{4.7}
\]

Substituting (4.6)-(4.7) into (4.5) proves (4.2).

If `alpha,beta,gamma>=1`, then for every `theta`,

\[
\beta\gamma\sin^2\theta
+\alpha\gamma\cos^2\theta
+\alpha\beta
\ge 2,
\]

because `alpha beta>=1` and

\[
\gamma(\beta\sin^2\theta+\alpha\cos^2\theta)\ge1.
\]

Hence the integrand in (4.2) is at most `1/sqrt(2)`, and (4.3) follows. `QED`

### The critical level

The theorem only needs an essential density bound. The single level `s=0` is irrelevant to the essential supremum. The cone itself has three-dimensional Lebesgue measure zero, so there is no atom there. The same ruling parametrization with `a=0` also gives the formal coarea bound away from the cone vertex, but no claim depends on choosing a pointwise density value at `0`.

---

## 5. What this does and does not solve

### What is newly paid

1. **Distributed Pluecker mass for the isolated same-sign pair.** Proposition 1.1 converts the entire same-sign spectral plane directly into an output-density bound. It therefore survives the B06 Hadamard delocalization without selecting a physical minor.
2. **Dependence among three rotated coordinates on the ruled side.** Theorem 4.1 does not assume that the spectral coordinates are independent. It uses only a theorem that is actually valid for the projection of a product law: every two-dimensional marginal is bounded by `2`.
3. **The nonlinear integration is exact.** The one-sheet hyperboloid is foliated by straight lines and the coarea quotient equals `1/2`; there is no dimension-dependent fiber volume and no reciprocal Pluecker-minor payment.
4. **Explicit constant.** For a rank-three truncation with eigenvalues `alpha,beta,-gamma`, all at least one in magnitude, the majority-sign half-density is at most `sqrt(2) pi`.

### What remains unpaid

This is **not** the full conjecture.

For signature `(2,1)`, the opposite half-line `s<0` consists of two-sheet hyperboloids, which are not real-line ruled. The above X-ray mechanism therefore does not automatically control the minority-sign half. More importantly, for a general matrix `A` there are additional spectral coordinates. Their contribution is **correlated** with the selected rank-three projection, so it cannot be convolved away as independent noise. Conditioning on those coordinates does not preserve the marginal X-ray bound for the selected spectral triple.

Thus the first essential missing implication is now sharpened to:

### `QFORM-PROJECTION-PRODUCT-INTERACTION-v2`

Exploit the fact that a three-dimensional spectral marginal is not an arbitrary density with bounded X-ray transform, but an orthogonal projection of an original coordinate-product law, strongly enough to do at least one of the following:

- control the two-sheet/minority-sign level integrals uniformly; or
- pass the ruled-level/X-ray estimate through the correlated remaining spectral contribution without conditioning away the product structure.

A proof using only `||g||_infinity` or only unrestricted fiber maxima cannot do this; those information losses are already source-refuted. A proof using a reciprocal local physical-minor constant and then Pluecker averaging also cannot do it; fleet02/B10's exact flat-Walsh calculation loses `n/2`.

The natural next mechanism is therefore an **operator-level aggregation before localization**: an X-ray/Radon estimate or nonlinear Brascamp--Lieb inequality for projected product measures evaluated on the quadratic level family, with the original product structure kept alive.

---

## 6. Old/new implication ledger

**Old unpaid implication:** turn three large spectral directions into a dimension-free nonlinear density estimate despite rotation, without selecting a constant-size physical block and without pretending the rotated variables are independent.

**New proved implication:** for an isolated same-sign spectral plane, the sharp product-marginal theorem already performs the dimension-free aggregation (`2pi` bound); for an isolated rank-three indefinite truncation, the full dependence among the three spectral coordinates is harmless on the one-sheet/majority-sign side, where the density is bounded by `sqrt(2) pi` through an exact ruled-level X-ray identity.

**Still unpaid:** the two-sheet/minority-sign side and correlated extra spectral components.

**Full conjecture status:** `OPEN / NOT PROVED / NOT DISPROVED`.

---

## 7. Verification notes

The key algebraic identity was independently checked symbolically during the run:

\[
\Phi_1^2+\Phi_2^2-\Phi_3^2=a^2,
\]

\[
|\partial_\theta\Phi\times\partial_t\Phi|^2=a^2+2t^2,
\qquad
|\nabla q_0(\Phi)|^2=4a^2+8t^2,
\]

so the coarea quotient is exactly `1/2`.

No finite computation is used to promote the theorem. The only external premise is the source-stated sharp marginal-density theorem for product measures; all remaining steps above are explicit analytic identities and coarea/X-ray estimates.

A scoped privacy review of this report found no credentials, scheduler identifiers, machine paths, unrelated private data, or public-release instructions.
