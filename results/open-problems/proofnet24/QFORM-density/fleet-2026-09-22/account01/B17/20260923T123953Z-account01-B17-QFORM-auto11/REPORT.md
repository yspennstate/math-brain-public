SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T12:39:53Z.
attacking: one genuinely macroscopic physical row in an arbitrary positive/negative spectral orientation, plus a shared infinitesimal residual; derive a global weak-limit ceiling and an exact finite rotated stress.

# QFORM B17 — weighted 3D rotation bound and one-macroscopic-row mixed-limit closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Worker: `account01/B17` — Sharp constant and witnesses  
Run: `20260923T123953Z-account01-B17-QFORM-auto11`  
Classification: **NEW SUPPORTING SHARP-WITNESS THEOREMS**  
Full unrestricted QFORM: **OPEN / NOT PROVED / NOT DISPROVED**  
Full-target continuity: **OPEN**  
Execution context: `WITHOUT_VERIFIED_BRAIN`


The strongest certified target-level lower obstruction remains

\[
C_*\ge 3\sqrt2.
\tag{0.1}
\]

The latest `account02/B17` diffuse-Lindeberg theorem gives a source-valid exact-rank-three sequence whose complete density norms tend to `3 sqrt(2)`; its source pin is

`yspennstate/math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/account02-B17-20260923T1142Z-r11/REPORT.md`.

The new work below does not increase (0.1). It closes a previously unpaid **one macroscopic row mixing the positive and negative eigenspaces, at all output levels, on the limiting-law side**, and supplies a concrete finite four-variable rotated stress with a uniform bound.

---

## 1. Weighted equal-magnitude three-variable theorem

### Theorem `QFORM-WEIGHTED-EQUALMAG-ROTATION-v1`

Let `X_1,X_2,X_3` be independent real random variables with densities satisfying

\[
\|f_i\|_\infty\le M_i,\qquad M_i>0.
\]

Let `B=B^T` be indefinite and satisfy

\[
B^2=\alpha^2 I_3,\qquad \alpha\ne0.
\]

For arbitrary `ell in R^3` and `c in R`, put

\[
Q=X^TBX+2\ell^TX+c.
\]

Then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le {2\over|\alpha|}
\left[
\pi\sqrt2\,(M_1M_2M_3)
\left(\sum_{i=1}^3M_i^{2/3}\right)^{3/2}
\right]^{1/2}.
}
\tag{1.1}
\]

When `M_1=M_2=M_3=1`, this reduces exactly to the previously proved constant

\[
2\sqrt{3\pi\sqrt6}=9.6095571059\ldots .
\]

No centering, moments, symmetry, support connectedness, unimodality, or smoothness is assumed.

### Proof

Complete the square and scale the output, reducing to `alpha=1`, `ell=0`, `c=0`, and a symmetric orthogonal involution `H=B` of signature `(2,1)`. Write `q(x)=x^THx`; then `|Hx|=|x|`.

Fix a radius `r>0` and an output interval `I` of length `eta`.

**Near field.** On `|x|<=r`, the original joint density is at most

\[
M:=M_1M_2M_3.
\]

An orthogonal diagonalization is used only for Lebesgue volume. The exact bounded-ball pushforward under `z_1^2+z_2^2-z_3^2` has density at most `pi sqrt(2) r`; hence

\[
P\{|X|\le r,\ q(X)\in I\}
\le M\pi\sqrt2\,r\,\eta.
\tag{1.2}
\]

**Far field with optimized coordinate thresholds.** Choose `c_i>0` with `sum c_i^2=1`. Since `|Hx|>r` outside the ball, the far field is covered by

\[
E_i=\{|(Hx)_i|>c_i r\},\qquad i=1,2,3.
\]

Condition on the other two **original physical coordinates**. As a function of `x_i`, `q` is quadratic and

\[
\partial_i q=2(Hx)_i.
\]

On `E_i`, the allowed line is the union of at most two monotone pieces, and the total inverse-image length of `I` is at most `eta/(c_i r)`. The conditional density cap is `M_i`, so

\[
P(E_i,\ q(X)\in I)\le {M_i\over c_i r}\eta.
\tag{1.3}
\]

Thus

\[
P(q(X)\in I)
\le\left[M\pi\sqrt2\,r+{1\over r}\sum_i{M_i\over c_i}\right]\eta.
\tag{1.4}
\]

The constrained minimum of `sum M_i/c_i` under `sum c_i^2=1` occurs at

\[
c_i={M_i^{1/3}\over(\sum_jM_j^{2/3})^{1/2}}
\]

and equals

\[
\left(\sum_iM_i^{2/3}\right)^{3/2}.
\tag{1.5}
\]

Optimizing (1.4) in `r` gives (1.1). Since the interval estimate is uniform in `I`, the output measure is dominated by the stated constant times Lebesgue measure. QED.

**Scope.** This argument proves essential boundedness, not continuity. It retains physical-coordinate product structure in the far field; the near-field rotation uses only a pointwise joint-density cap and unit Jacobian.

---

## 2. Global one-macroscopic-row Gaussian-completion theorem, arbitrary orientation

Let

\[
L:=\sqrt{6/\pi},
\]

the density supremum of `N(0,1/12)`.

### Theorem `QFORM-ONE-MACROSCOPIC-MIXED-LIMIT-GLOBAL-v1`

Let `J=J^T`, `J^2=I_3`, with indefinite signature. Let `u in S^2`, `0<=rho<=1`, let `X` have an arbitrary density bounded by one, and let

\[
Z\sim N\!\left(0,{I_3-\rho^2uu^T\over12}\right)
\]

be independent of `X`. Let `R` be **any** independent `R^3`-valued random vector. Then

\[
Q=(\rho uX+Z+R)^TJ(\rho uX+Z+R)
\]

has an essentially bounded density satisfying, for `0<rho<1`,

\[
\boxed{
\|p_Q\|_\infty\le F(\rho):=
\min\left\{
{3\sqrt2\over1-\rho^2},
\ 2\left[
\pi\sqrt2\,{L^2\over\rho}
\left(\rho^{-2/3}+2L^{2/3}\right)^{3/2}
\right]^{1/2}
\right\}.
}
\tag{2.1}
\]

At the endpoints use the evident limits/one-sided arguments. In particular

\[
\boxed{
\sup_{0\le\rho\le1}\|p_Q\|_\infty<16.375.
}
\tag{2.2}
\]

### Proof

Condition throughout on `R`; it becomes a deterministic affine shift.

For `rho<1`, condition also on `X`. The Gaussian covariance obeys

\[
{I-\rho^2uu^T\over12}\succeq {1-\rho^2\over12}I_3.
\]

The completed arbitrary-mean Gaussian theorem

`yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T070310Z-account03-B17-QFORM-r25/REPORT.md`

gives

\[
\|p_{Q\mid X,R}\|_\infty\le {3\sqrt2\over1-\rho^2}.
\tag{2.3}
\]

For the second bound, choose an orthonormal basis with first vector `u`. In that basis

\[
Z=(\sqrt{1-\rho^2}\,G_1,G_2,G_3),
\qquad G_j\stackrel{iid}{\sim}N(0,1/12).
\]

Put

\[
T=\rho X+\sqrt{1-\rho^2}\,G_1.
\]

Then `T,G_2,G_3` are independent and

\[
\|p_T\|_\infty\le1/\rho,
\qquad
\|p_{G_2}\|_\infty=\|p_{G_3}\|_\infty=L.
\]

After the orthogonal basis change the quadratic core is still a symmetric orthogonal involution; the deterministic conditioned value of `R` contributes only affine terms. Apply Theorem 1 with caps `(1/rho,L,L)` to obtain the second term in (2.1). Average over `R`.

The Gaussian branch is increasing in `rho`; the weighted-cap branch is decreasing. Taking the rational split `rho_0=43/50` gives

\[
{3\sqrt2\over1-\rho_0^2}=16.2927829766\ldots,
\]

while the weighted branch at `rho_0` is

\[
16.3749020608\ldots<16.375.
\]

Therefore (2.2) follows. QED.

This theorem is global in the output level and includes arbitrary random affine displacement `R`. It does **not** assert continuity.

---

## 3. Apply the completed `account02/B17` shared-frame theorem to the actual mixed-heavy inequality

A completed partner theorem is source-pinned at

`yspennstate/math-open-problems@907d4092f2d22b6c02146cb8165efa0b7416ffa5`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T171829Z-account02-B17-QFORM-r11/REPORT.md`.

It proves the general Gram version of the cap-one infinitesimal covariance floor: if light physical rows `w_{mk}` satisfy

\[
\sum_k w_{mk}w_{mk}^T\to G,
\qquad \max_k\|w_{mk}\|\to0,
\]

and, after deterministic rowwise translations, their independent vector contributions are probabilistically infinitesimal and have a convergent sum, then the Gaussian covariance in the Levy--Khintchine limit is at least `G/12`.

Apply it to an exact Parseval frame with one distinguished row `r_m->rho u` and light Gram

\[
\sum_{k\ge1}w_{mk}w_{mk}^T
=I-r_mr_m^T
\to I-\rho^2uu^T.
\tag{3.1}
\]

Assume the translated heavy scalar contribution converges and the cap-one heavy laws have a weak limit (the cap survives weak convergence). Then the light limit can be decomposed as

\[
Z+R,
\qquad
Z\sim N\!\left(0,{I-\rho^2uu^T\over12}\right),
\]

with `R` independent of `Z` and of the heavy limit. Theorem 2 therefore gives the **actual partner-to-new-theorem inequality**

\[
\boxed{
\|p_{Q_\infty}\|_\infty\le F(\rho)<16.375
}
\tag{3.2}
\]

for every convergent one-macroscopic-row / shared-infinitesimal-residual limit, with **arbitrary orientation** `u`, including a row mixing the positive and negative eigenspaces, and with the bound global in the output level.

This closes a branch explicitly left open in the partner report. It is a **weak-limit theorem**: it does not preclude a narrowing finite-stage spike invisible to weak convergence.

The newest completed `account02/B17` theorem,

`yspennstate/math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/account02-B17-20260923T1142Z-r11/REPORT.md`,

applies at the fully diffuse endpoint `rho=0`. For centered unit-interval diffuse banks it gives the stronger prelimit statement

\[
\boxed{
\|p_{Q_m}\|_\infty\longrightarrow3\sqrt2.
}
\tag{3.3}
\]

Thus the source-valid lower obstruction `3sqrt(2)` is retained, while the newly paid one-heavy mixed limit is uniformly finite even when the macroscopic row survives and is not an eigendirection.

---

## 4. Exact finite dense four-variable stress family

The weighted theorem also gives a clean finite target family that is neither diagonal nor a diffuse control.

Let

\[
r=\left({1\over2},{1\over2},{1\over2}\right),
\qquad
C={1\over6}
\begin{pmatrix}
5&-1&-1\\
-1&5&-1\\
-1&-1&5
\end{pmatrix},
\]

and make the `4 x 3` Parseval row matrix

\[
R=\begin{pmatrix}
r^T\\ (Ce_1)^T\\ (Ce_2)^T\\ (Ce_3)^T
\end{pmatrix}.
\]

Since

\[
rr^T+C^2=I_3,
\]

we have `R^TR=I_3`. With `J=diag(1,1,-1)`, put `A=RJR^T`. Exact arithmetic gives

\[
\boxed{
A=
\begin{pmatrix}
1/4&5/12&5/12&-7/12\\
5/12&25/36&-11/36&1/36\\
5/12&-11/36&25/36&1/36\\
-7/12&1/36&1/36&-23/36
\end{pmatrix},
}
\tag{4.1}
\]

whose nonzero spectrum is exactly

\[
\boxed{\{1,1,-1\}.}
\tag{4.2}
\]

Every entry of `A` is nonzero.

Take the first physical input `X` to have an **arbitrary** density bounded by one. Take the other three physical inputs independently with the cap-one Gaussian density

\[
g(x)=e^{-\pi x^2}
\]

(which is `N(0,1/(2pi))` and has `||g||_infty=1`). Put `rho=sqrt(3)/2` and `u=(1,1,1)/sqrt(3)`, so `r=rho u`; the matrix `C` has eigenvalue `1/2` along `u` and eigenvalue `1` on `u^perp`.

Rotational invariance of the three Gaussian inputs changes the active coordinates into

\[
T={\sqrt3\over2}X+{1\over2}G_1,
\qquad G_2,\qquad G_3,
\]

where `G_j` are iid with density `e^{-pi x^2}`. These coordinates are independent and have density caps

\[
\left({2\over\sqrt3},1,1\right).
\]

The spectral core after the same orthogonal change of basis still squares to the identity. Theorem 1 therefore yields the exact global finite-source bound

\[
\boxed{
\|p_{X^TAX}\|_\infty
\le
2\left[
\pi\sqrt2\,{2\over\sqrt3}
\left(\left({2\over\sqrt3}\right)^{2/3}+2\right)^{3/2}
\right]^{1/2}
=10.5848785163\ldots .
}
\tag{4.3}
\]

This is an exact four-coordinate, all-entry-nonzero, high-leverage rotated stress family with one arbitrary cap-one heavy law. It supplies a finite global control on a branch where the heavy row genuinely mixes the positive and negative spectral directions.

---

## 5. Sharp-witness consequences

The certified witness picture is now tighter.

1. The universal constant, if it exists, still satisfies `C_*>=3sqrt(2)`; the newest `account02/B17` theorem makes this a **global-density** diffuse saturation, not just a cone-tip limit.
2. An arbitrary three-variable equal-magnitude rotation with unequal input-density caps obeys the explicit weighted formula (1.1).
3. Every convergent one-macroscopic-row plus shared infinitesimal-residual limit is globally bounded by `<16.375`, uniformly over the row's orientation and over arbitrary independent Levy residual noise. This includes the previously unpaid case where the heavy row mixes positive and negative eigenspaces.
4. The exact dense four-variable family (4.1), with one arbitrary cap-one heavy input and three cap-one Gaussians, is globally bounded by `10.5848785163...`.

What remains genuinely dangerous on the witness side is therefore narrower: **two or more interacting macroscopic physical rows**, a **finite-stage/local spike not reflected in the weak limit**, or additional spectral directions coupled to those heavy rows. Nothing here proves `3sqrt(2)` is the unrestricted sharp constant, and nothing here proves full-target continuity.

---

## 6. Verification/source pins

Deterministic checker in this run verifies: the weighted-threshold constants, the rational Parseval identity, the exact physical matrix (4.1), its spectrum, and the numerical bound (4.3).

Primary source pins:

- fresh programme control/corrections: `yspennstate/math-research-brain@5a71ebdcdcfdd94ff5f68a96ec6df52b5dc4dc82`;
- completed `account02/B17` general-Gram infinitesimal covariance floor: `yspennstate/math-open-problems@907d4092f2d22b6c02146cb8165efa0b7416ffa5`, `.../account02/B17/20260922T171829Z-account02-B17-QFORM-r11/REPORT.md`;
- newest `account02/B17` diffuse-Lindeberg global theorem: `yspennstate/math-open-problems@1d2dd52680ec729f28b7289e74a6f3752a379127`, `.../account02/B17/account02-B17-20260923T1142Z-r11/REPORT.md`;
- arbitrary-mean Gaussian ceiling: `yspennstate/math-open-problems@dcf8885d5153370cacfa246ad1e29fb06d971769`, `.../account03/B17/20260923T070310Z-account03-B17-QFORM-r25/REPORT.md`;
- prior unweighted equal-magnitude theorem, generalized here: `yspennstate/math-open-problems@2737fd6225e7187ddd396f2bc1e8eadf24c409bd`, `.../account01/B17/QFORM-B17-20260923T033912Z-r13/REPORT.md`.

Status: **supporting theorems proved; full QFORM remains OPEN.**
