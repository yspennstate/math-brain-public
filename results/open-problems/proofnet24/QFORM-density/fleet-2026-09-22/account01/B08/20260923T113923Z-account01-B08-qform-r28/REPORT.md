# QFORM account01/B08 r28 — exact-Gram heavy-set peeling for the diffuse/localized split

Programme: `QFORM-DENSITY-3EIG-20260922`

Status: **supporting theorem/router; full QFORM remains OPEN**.  This report proves a conditioning-safe diffuse estimate for exact finite spectral range and turns failure into a bounded-cardinality localized spectral-range packet.  It does **not** delete an arbitrary complementary spectral tail, and it does not claim the unrestricted conjecture.

Execution status: `WITHOUT_VERIFIED_BRAIN`.

## 1. Setup

Let

\[
A=RDR^\top,
\qquad R\in\mathbb R^{n\times r},\quad R^\top R=I_r,
\qquad r>2,
\]

with `A` of exact rank `r`, and assume

\[
\min_{1\le j\le r}|D_{jj}|\ge L>0.
\]

The input coordinates are independent and have densities bounded by one.  Write the physical row leverage

\[
p_i=\|R_{i,*}\|_2^2,
\qquad \sum_i p_i=r.
\]

Fix `0<theta<1/2` and define the physical heavy set

\[
H=\{i:p_i>\theta\},\qquad T=H^c,
\]

and its exact removed-frame Gram

\[
S_H=R_H^\top R_H,\qquad \varepsilon=\|S_H\|_{op}.
\]

The point of using `epsilon` rather than the crude cardinality estimate `|H| max_i p_i` is that many conditioned physical coordinates can collectively remove little mass in every spectral direction.

## 2. Main theorem — `QFORM-EXACT-GRAM-HEAVY-PEEL-v1`

There is the following exhaustive alternative.

### Diffuse residual branch

If

\[
\varepsilon\le 1-2\theta,
\]

then `Q=X^TAX` has a continuous density vanishing at infinity and

\[
\boxed{
\|p_Q\|_\infty
\le
\frac{4r}{r-2}\,\frac{1}{(1-\varepsilon)L}
\le
\frac{2r}{(r-2)\theta L}
\le
\frac{6}{\theta L}.
}
\]

### Localized spectral-range branch

If

\[
\varepsilon>1-2\theta,
\]

then there is a unit vector `v` in `Ran(A)` such that

\[
\boxed{
\|v_H\|_2^2>1-2\theta,
\qquad
|H|<\frac r\theta.
}
\]

The localized object is a basis-invariant direction in the actual nonzero spectral range; it need not be one arbitrarily selected eigenvector.  Hence repeated eigenvalues cause no ambiguity.

## 3. Proof of the diffuse residual branch

Set

\[
G=R_T^\top R_T=I_r-S_H.
\]

Under `epsilon<=1-2 theta`,

\[
G\succeq (1-\varepsilon)I_r\succeq 2\theta I_r,
\]

so `G` is positive definite.

Condition on all original coordinates `X_H=x_H`.  The remaining conditional quadratic-affine form is

\[
Q_{x_H}(x_T)
=x_T^\top R_TDR_T^\top x_T
+2x_T^\top R_TDR_H^\top x_H+c(x_H).
\]

The induced linear vector belongs to `Ran(R_T)`, and because `G` and `D` are invertible,

\[
\operatorname{Ran}(R_TDR_T^\top)=\operatorname{Ran}(R_T).
\]

Therefore one can solve for a deterministic shift `h(x_H)` so that translating each surviving original coordinate by `h_i(x_H)` completes the square.  Coordinatewise translation preserves independence and the density caps `<=1`.  Thus it suffices, uniformly in `x_H`, to bound the exact-rank-`r` quadratic form with matrix

\[
A_{TT}=R_TDR_T^\top.
\]

Whiten the surviving spectral frame:

\[
W=R_TG^{-1/2},\qquad W^\top W=I_r,
\]

and

\[
K=G^{1/2}DG^{1/2},
\qquad A_{TT}=WKW^\top.
\]

For each `i in T`,

\[
\|W_{i,*}\|_2^2
=R_{i,*}G^{-1}R_{i,*}^\top
\le \frac{p_i}{1-\varepsilon}
\le \frac{\theta}{1-\varepsilon}
\le \frac12.
\]

Now apply the completed designated-partner theorem

`account02/B08, QFORM-EXACT-RANGE-CONDITIONING-FRESNEL-v1`

from

`yspennstate/math-open-problems@ac9b000da88c4923d8a3adb6a0a8bdccbd27ccae`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T093606Z-account02-B08-qform-diffuse-r25/REPORT.md`.

Use its `h=0` exact-range case on the already conditioned/whitened child.  Its physical leverage hypothesis is exactly the inequality above, and it gives

\[
\|p_{Q\mid X_H=x_H}\|_\infty
\le \frac{4r}{r-2}|\det K|^{-1/r}.
\]

This is an actual application of the designated partner result, not merely a citation.

The determinant is exact:

\[
|\det K|=\det(G)|\det D|.
\]

Since every eigenvalue of `G` is at least `1-epsilon` and every `|D_j|>=L`,

\[
|\det K|^{1/r}
\ge (1-\varepsilon)L.
\]

Hence uniformly in the conditioned values,

\[
\|p_{Q\mid X_H=x_H}\|_\infty
\le
\frac{4r}{r-2}\frac1{(1-\varepsilon)L}.
\]

Averaging the conditional densities proves the unconditional `L^infinity` bound.  The partner Fresnel receiver gives continuous `C_0` conditional densities; their uniform bound allows dominated convergence in the conditioning measure, so the averaged density is also continuous and vanishes at infinity.

Finally `1-epsilon>=2 theta` gives

\[
\frac{4r}{r-2}\frac1{(1-\varepsilon)L}
\le \frac{2r}{(r-2)\theta L}
\le \frac6{\theta L},
\]

because `r/(r-2)<=3` for `r>=3`.

## 4. Proof of the localized branch

If `epsilon>1-2 theta`, choose a unit `u in R^r` with

\[
u^\top S_Hu=\varepsilon.
\]

Put `v=Ru`.  Then `||v||=1`, `v in Ran(A)`, and

\[
\|v_H\|_2^2
=\|R_Hu\|_2^2
=u^\top S_Hu
=\varepsilon
>1-2\theta.
\]

Also every `i in H` satisfies `p_i>theta`, while `sum_i p_i=r`, so

\[
|H|\theta<\sum_{i\in H}p_i\le r,
\]

which proves `|H|<r/theta`.

No random-variable rotation appears anywhere in this argument.

## 5. Exact-rank-three consequences

For the actual three-direction exact-range case (`r=3`, `|D_j|>=L`), the theorem gives the following useful tradeoffs:

| theta | continuous density payment | otherwise spectral-range localization |
|---:|---:|---:|
| `1/4` | `||p_Q||inf <=24/L` | `>1/2` mass on at most `11` original coordinates |
| `1/8` | `<=48/L` | `>3/4` mass on at most `23` coordinates |
| `1/16` | `<=96/L` | `>7/8` mass on at most `47` coordinates |
| `1/32` | `<=192/L` | `>15/16` mass on at most `95` coordinates |

The `theta=1/4` version is particularly clean:

\[
\boxed{
\text{either }\|p_Q\|_\infty\le 24/L\text{ with }p_Q\in C_0,
\quad\text{or}\quad
\exists H,\ |H|\le11,\ \exists v\in\operatorname{Ran}(A),\ \|v_H\|^2>1/2.
}
\]

Moreover every `i in H` has physical range leverage `p_i>1/4`.  Applying the preceding account01/B08 r27 heavy-row identity at scale `L` with `d=L/4` gives, for every such heavy coordinate,

\[
\boxed{
\|A_{i,-i}\|_2\ge L/4
\quad\text{or}\quad
\bigl(|A_{ii}|>\sqrt3\,L/4\ \text{ and }\ s_2(A_{-i,-i})>3L/4\bigr).
}
\]

Thus failure of the diffuse payment does not leave an unstructured exact-rank-three state: it leaves a fixed-size physical core, carrying more than half of a genuine spectral-range direction, whose coordinates are each already in the star/pivot-two-child router.

## 6. Why this is useful and what it does not prove

This theorem complements localized-coordinate conditioning without using moments, support regularity, pointwise van-der-Corput decay, post-rotation independence, or a small-random-error interpretation of spectral tails.  It also improves the partner's coarse `h*delta` conditioning budget to the exact removed-frame operator mass `epsilon` and makes failure quantitatively localized.

It does **not** solve the full owner target because an arbitrary matrix can have complementary nonzero spectral directions outside the three selected large eigenvalues.  Those directions cannot be silently discarded.  The first remaining implication is therefore

`QFORM-HEAVY-GRAM-PEELING-WITH-SPECTRAL-REMAINDER-v1`:

build an analogue of this exact-Gram peeling for a genuine spectral window while retaining the whole complementary spectrum, likely by replacing the exact-range Fresnel payment with the one-scale ridge receiver after heavy-set conditioning.  The fixed-size localized survivor should then feed the existing star/pivot/grouped-anchor machinery.

Full universal essential boundedness: **OPEN**.

Full universal continuity: **OPEN**.  Continuity is proved only on the diffuse payment branch above.
