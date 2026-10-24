# account01 / B05 / QFORM r29

Status: **ESSENTIAL_STEP_APPLIED / SUPPORTING_TRANSITION_THEOREM_PROVED / PRECISE_REMAINING_FACTOR_IDENTIFIED / FULL_QFORM_OPEN**.

Continuity: proved in the positive-leak spread subbranch below by integrable Fourier decay; **full-target continuity remains open**.

Brain state: `WITHOUT_VERIFIED_BRAIN`. Repository retrieval was used; no claim of native learned-memory ingestion is made.

## 1. Purpose

The preceding B05 run isolated the exact-rank-three heavy-null survivor in which arbitrarily small nonzero longitudinal coefficients may sit on a transverse-majority support. This run asks whether the *magnitude* of that leak can be paid without conditioning away the same coordinates.

The answer is yes away from the endpoint, with an exact determinant cancellation. The resulting estimate is not uniform as the total leak tends to zero, so it does not prove the conjecture. It identifies the remaining endpoint-stability factor sharply.

## 2. Exact heavy-null coordinates

Let

\[
A=RBR^T,
\qquad R^TR=I_3,
\qquad s_{\min}(B)\ge 1,
\]

and suppose a physical row `h` of `R` has leverage

\[
r_h=\sqrt c\,e_1,\qquad \frac12<c\le 1,
\]

and is a null quadratic pivot:

\[
r_h^TBr_h=0.
\]

Thus `B_11=0`. Rotate only the active transverse plane `e_1^perp` so that `Be_1` points along `e_2`. Then

\[
B=
\begin{pmatrix}
0&\beta&0\\
\beta&\alpha&\delta\\
0&\delta&\gamma
\end{pmatrix}.
\tag{2.1}
\]

Because `s_min(B)>=1`,

\[
|\beta|=|Be_1|\ge1.
\tag{2.2}
\]

Also

\[
\det B=-\beta^2\gamma,
\qquad |\det B|=|\beta|^2|\gamma|\ge1,
\tag{2.3}
\]

so in particular `gamma != 0`.

Write the remaining rows of `R` as

\[
r_j=(u_j,w_j,v_j),\qquad j\ne h,
\]

and put

\[
U=\sum_{j\ne h}u_jX_j,
\quad L=\sum_{j\ne h}w_jX_j,
\quad V=\sum_{j\ne h}v_jX_j.
\]

The Parseval identity `R^TR=I_3` gives the exact orthogonality relations

\[
\|u\|_2^2=1-c,
\qquad \|w\|_2=\|v\|_2=1,
\qquad u\perp w,\quad u\perp v,\quad w\perp v.
\tag{2.4}
\]

The quadratic form is therefore

\[
Q=2\beta\sqrt c\,X_hL+2\beta UL+\alpha L^2+2\delta LV+\gamma V^2.
\tag{2.5}
\]

No rotated-coordinate independence has been used: `X_h` is one original coordinate and is independent of the entire original-coordinate light block `X_{-h}`; `U,L,V` are simultaneous linear forms of that block and are *not* declared independent.

## 3. Spread normalized leak and exact reduction

Assume first `c<1` and define

\[
\widehat u=\frac{u}{\sqrt{1-c}},
\qquad
\varepsilon=\frac{\sqrt{1-c}}{\sqrt c}.
\tag{3.1}
\]

Then `(w,v,uhat)` is an orthonormal three-frame on the original light coordinates. Impose only the following spread condition on this normalized frame:

\[
\boxed{
 w_j^2+v_j^2+\widehat u_j^2\le\frac12
 \quad\text{for every }j\ne h.
}
\tag{3.2}
\]

Normalize the output by

\[
Q_*=\frac{Q}{\beta\sqrt c}.
\]

From (2.5), exactly

\[
Q_*
=2X_hL+\lambda V^2+2L\langle q,X_{-h}\rangle,
\tag{3.3}
\]

where

\[
\lambda=\frac{\gamma}{\beta\sqrt c},
\qquad
q=\frac{\alpha}{2\beta\sqrt c}w
  +\frac{\delta}{\beta\sqrt c}v
  +\varepsilon\widehat u.
\tag{3.4}
\]

This is precisely the family of `single_hub_core/REPORT.md`, Proposition 2.3: the aligned `w` and `v` components are arbitrary, while the genuinely transverse component has magnitude `eps=epsilon` and direction `qhat=uhat`. Under (3.2), that theorem gives

\[
\|p_{Q_*}\|_\infty
\le 9.6\,(\varepsilon|\lambda|)^{-1/3}.
\tag{3.5}
\]

Its characteristic-function estimate is `O(|t|^{-3/2})`, hence integrable, so this branch in fact has a continuous `C_0` density.

## 4. Determinant cancellation

Scaling back from `Q_*` to `Q` gives

\[
\|p_Q\|_\infty
\le \frac{9.6}{|\beta|\sqrt c}
      (\varepsilon|\lambda|)^{-1/3}.
\]

But

\[
\varepsilon|\lambda|
=
\sqrt{\frac{1-c}{c}}\,
\frac{|\gamma|}{|\beta|\sqrt c}
=
\frac{|\gamma|\sqrt{1-c}}{|\beta|c}.
\]

Therefore every active coefficient cancels into the determinant:

\[
\boxed{
\|p_Q\|_\infty
\le
9.6\,|\det B|^{-1/3}[c(1-c)]^{-1/6}.
}
\tag{4.1}
\]

Since `|det B|>=1`,

\[
\boxed{
\|p_Q\|_\infty
\le 9.6[c(1-c)]^{-1/6}.
}
\tag{4.2}
\]

This is the main new B05 synthesis. It is invariant under arbitrarily bad separate sizes of `beta` and `gamma`; the potentially tiny square coefficient is exactly offset by the hub/output scale through `|det B|=|beta|^2|gamma|`.

For any fixed `eta in (0,1/2]`, if

\[
1-c\ge\eta,
\]

then `c(1-c)>=eta/2`, so

\[
\boxed{
\|p_Q\|_\infty
\le 9.6(2/\eta)^{1/6}.
}
\tag{4.3}
\]

For example, throughout

\[
\frac12<c\le\frac{127}{128},
\]

one gets the explicit universal bound

\[
\boxed{
\|p_Q\|_\infty<24.191.
}
\tag{4.4}
\]

The same proof permits arbitrary original-coordinate linear terms and coordinatewise quadratic modulations covered by Proposition 2.3; no moment or support hypothesis is introduced.

## 5. Actual designated-partner application: the exact endpoint

At `c=1`, (2.4) forces `u=0`. Hence every residual physical row is transverse to the heavy direction and the heavy row itself is purely longitudinal: the frame is exactly support-separated.

Apply the completed designated-partner result account02/B05 r23, `QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1`, to (2.1). Since `s_min(B)>=1`, its actual inequality is

\[
\boxed{
 c=1\quad\Longrightarrow\quad \|p_Q\|_\infty<248.
}
\tag{5.1}
\]

This is an equation-level use of the partner theorem, not a background citation.

Thus the positive-leak spread branch is controlled by (4.1), and the zero-leak endpoint is controlled by (5.1). What is missing is a **uniform bridge as `c -> 1-`**, not an estimate at either endpoint separately.

## 6. Combination with B05 r28

The previous B05 theorem says that if `H={j:u_j!=0 and (w_j,v_j)!=(0,0)}` and

\[
K_H=\sum_{j\in H}r_jr_j^T,
\qquad \kappa=\|K_H\|_{op},
\]

then

\[
\|p_Q\|_\infty<\frac{248}{1-\kappa}
\qquad(\kappa<1).
\tag{6.1}
\]

In particular `kappa<=1/2` gives `<496`. Combining (4.4), (5.1), and (6.1), the light-normalized-frame heavy-null survivor can be restricted simultaneously to

\[
\boxed{
127/128<c<1,
\qquad \kappa>1/2,
\qquad
w_j^2+v_j^2+\widehat u_j^2\le1/2\ \forall j.
}
\tag{6.2}
\]

Equivalently the total longitudinal leak obeys

\[
\|u\|_2^2=1-c<1/128,
\]

while more than half of a transverse spectral direction is carried on coordinates on which that tiny leak is nonzero.

This is much narrower than the previous qualitative phrase “infinitesimal overlap support”: the only unpaid spread branch is now a **tiny-total-leak / transverse-majority endpoint transition**.

## 7. Precise missing factor

Define

`QFORM-TINY-LEAK-ENDPOINT-STABILITY-v1`:

> In the exact-rank-three heavy-null normal form (2.1)-(2.5), under the normalized light-frame condition (3.2), prove an `L^infty` bound independent of `epsilon=sqrt((1-c)/c)` for `0<epsilon<1/sqrt(127)`, or prove the corresponding uniform interval bound directly, preserving the original product coordinates.

The existing source `rank_three_geometry/REPORT.md` names a sufficient product-sensitive estimate `(TW)` for precisely the light-frame hub/twist transition:

\[
J(\tau)
=
\sup_\theta\int_{\mathbb R^2}
\left|
\mathbb E e^{i(yV+uU+\langle\theta,X_L\rangle+\tau ZV)}
\right|\,dy\,du
\le K(1+|\tau|).
\tag{7.1}
\]

That report proves that such a bound closes its canonical light rank-three hub core uniformly in the leak parameter. Therefore (7.1), or a genuinely real-variable/coarea substitute with the same endpoint stability, is now the precise remaining factor for this B05 spread survivor.

The factor cannot be replaced by a generic bounded density of `(L,V,Z)`, a conditional density cap, a pointwise radial envelope, or an arbitrary-joint three-dimensional coarea bound: all of those relaxations are already invalidated in the correction inbox.

## 8. Sources actually used

1. Designated partner account02/B05 r23, theorem `QFORM-HEAVY-ROW-SUPPORT-SEPARATED-CLOSURE-v1`: repository `yspennstate/math-open-problems`, commit `ad7874e3ee0f4541714b2376aa09154517e60867`, path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B05/20260923T062009Z-account02-B05-QFORM-r23/REPORT.md`.
2. `single_hub_core/REPORT.md`, Proposition 2.3 (arbitrary hub law with transverse cross term): repository `yspennstate/math-open-problems`, commit `1679e3fca3c06c3dda173f23b19638c6459d20b5`, path `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/single_hub_core/REPORT.md`.
3. `rank_three_geometry/REPORT.md`, named `(TW)` sufficient estimate and light hub-core reduction: same repository, current source path `proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/rank_three_geometry/REPORT.md`; source blob read in this run `e99b63c3334a0abb24b66460081a49ce4664ad01`.
4. B05 r28 theorem `QFORM-HEAVY-ROW-OVERLAP-GRAM-EXIT-v1`: repository `yspennstate/math-open-problems`, commit `7b0448e370bab13079027a6d94a47830c5c2a292`, path `proofnet24/QFORM-density/fleet-2026-09-22/account01/B05/20260923T073123Z-account01-B05-QFORM-r28/REPORT.md`.

## 9. Scope and status

This is **not** a proof of full QFORM. It treats an exact-rank-three heavy-null subbranch under the normalized spread condition (3.2), and identifies the endpoint-stability estimate still needed there. It does not silently assume independence of `U,L,V`, bounded support, moments, Gaussianity, log-concavity, or connected supports.

Independent end-to-end review of this r29 theorem: `PENDING`.

Full conjecture: `OPEN_NOT_PROVED`.

Full-target continuity: `NOT_PROVED`.
