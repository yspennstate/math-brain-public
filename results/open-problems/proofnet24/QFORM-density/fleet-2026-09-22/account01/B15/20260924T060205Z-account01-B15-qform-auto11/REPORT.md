# account01/B15 — source-Hölder stability and half-line continuity on the uniformly paid ruled sheet

Run: `20260924T060205Z-account01-B15-qform-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`, current owner control `2026-09-22.15`.  
Status: **FULL QFORM OPEN**. Supporting regularity theorems proved below. Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source-pinned designated-partner input

The newest completed designated-partner result is account02/B15

`yspennstate/math-open-problems@45779cb1dca5f453ac620431b380ad015a052e70`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260924T050354Z-account02-B15-QFORM-auto11-r1/REPORT.md`.

For an `n x 3` matrix `R` with orthonormal columns and

\[
q(X)=\langle r_1,X\rangle^2+\langle r_2,X\rangle^2-\langle r_3,X\rangle^2,
\]

where the original coordinates are independent with densities at most one, its Theorem 4.1 proves the following. If one original-coordinate factor is replaced by an arbitrary subdensity `0<=h<=1` of mass `m<=1`, then the positive-sheet output submeasure

\[
\nu_h^+(B)=\int 1_{\{q(x)\in B\cap[0,\infty)\}}h(x_j)\prod_{i\ne j}f_i(x_i)\,dx
\]

has a density `r_h^+` satisfying

\[
\boxed{\|r_h^+\|_\infty\le K\sqrt m,\qquad K=20\sqrt2.} \tag{1.1}
\]

The same source records the sharper probability-input one-sheet bound

\[
\boxed{\|r_f^+\|_\infty\le\pi\sqrt2.} \tag{1.2}
\]

All of these are interval/height statements first; continuity is not used. The proof remains in original product coordinates and does not assert independence after spectral rotation.

The report also contains an exact lower construction showing that the exponent `1/2` in a marginal-`L1` to output-`Linf` stability statement cannot be improved.

## 2. New abstract lemma: positivity removes the extra `sqrt(2)` loss

### Lemma 2.1 — `POSITIVE-SUBMASS-TO-SIGNED-STABILITY-v1`

Let `T` be any positive linear map from nonnegative scalar weights in one source coordinate to finite positive measures on `R`. Suppose that for every cap-one subdensity `0<=h<=1` of mass `m<=1`,

\[
Th\ll dt,\qquad \left\|\frac{dTh}{dt}\right\|_\infty\le K\sqrt m. \tag{2.1}
\]

Let `f,g` be cap-one probability densities, set

\[
\delta=\|f-g\|_1\le1,
\]

and let `Tf,Tg` have densities `p_f,p_g`. Then

\[
\boxed{\|p_f-p_g\|_\infty\le K\sqrt\delta,} \tag{2.2}
\]

and

\[
\boxed{\|p_f-p_g\|_1\le\delta.} \tag{2.3}
\]

Consequently, for every `1<=r<=infinity`,

\[
\boxed{
\|p_f-p_g\|_r
\le K^{1-1/r}\,
\delta^{(r+1)/(2r)}.
} \tag{2.4}
\]

### Proof

Put `a=f-g`. Positivity and linearity give, for every Borel set `E`,

\[
|T a(E)|\le T|a|(E).
\]

Taking the supremum over finite measurable partitions of `E` yields the measure domination

\[
|T a|\le T|a|. \tag{2.5}
\]

Here the left side is the total-variation measure of the signed output. Since `0<=|a|<=1` and `int|a|=delta<=1`, hypothesis (2.1) applies directly to the **single** subdensity `|a|`; there is no need to pay separately for `(f-g)_+` and `(g-f)_+`. Thus `T|a|` has density bounded by `K sqrt(delta)`, and (2.5) implies (2.2). Its total mass is at most `delta`, which gives (2.3). Interpolation between `L1` and `Linfinity` gives (2.4).

This is a strict constant improvement over the generic positive/negative splitting estimate, while retaining the same optimal exponent.

## 3. Apply the completed account02/B15 theorem

Fix all original-coordinate marginals except coordinate `j`, and let `r_f^+,r_g^+` denote the majority-sheet densities for the isotropic ruled rank-three form above. Applying Lemma 2.1 to the completed partner theorem (1.1) gives, whenever `delta=||f-g||_1<=1`,

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le20\sqrt2\,\sqrt\delta.
} \tag{3.1}
\]

The partner report obtained `40 sqrt(delta)` by splitting into positive and negative parts. Equation (3.1) uses the same proved submass theorem but dominates the signed output once by the pushforward of `|f-g|`, reducing the front constant from `40` to `20 sqrt(2)`.

The probability height (1.2) independently gives

\[
\|r_f^+-r_g^+\|_\infty\le2\pi\sqrt2. \tag{3.2}
\]

Thus the useful global local-stability envelope is

\[
\boxed{
\|r_f^+-r_g^+\|_\infty
\le \min\{20\sqrt2\sqrt\delta,\,2\pi\sqrt2\}
} \tag{3.3}
\]

for `delta<=1`, with (3.2) continuing to hold for arbitrary `delta<=2`.

Also

\[
\boxed{
\|r_f^+-r_g^+\|_r
\le (20\sqrt2)^{1-1/r}
\delta^{(r+1)/(2r)},\qquad1\le r<\infty.
} \tag{3.4}
\]

The completed partner lower example has

\[
|p_f(\delta)-p_g(\delta)|
=\sqrt\delta\left(1-\log2-\frac12\log(1+\delta/4)\right),
\]

so the exponent `1/2` in (3.1) is optimal even for one fixed owner-target matrix. Only the constant remains nonsharp.

## 4. Simultaneous product-source perturbations

Let `F=prod_i f_i` and `G=prod_i g_i` be two cap-one product sources for the same ruled matrix, and write

\[
\delta_i=\|f_i-g_i\|_1.
\]

Assume `delta_i<=1` for every `i`. Telescope by replacing one original marginal at a time. Every intermediate source is again a cap-one product probability law, so (3.1) applies at each step. Therefore

\[
\boxed{
\|r_F^+-r_G^+\|_\infty
\le20\sqrt2\sum_i\sqrt{\delta_i}.
} \tag{4.1}
\]

Likewise deterministic pushforward contracts total variation, so

\[
\boxed{
\|r_F^+-r_G^+\|_1\le\sum_i\delta_i.
} \tag{4.2}
\]

Thus the majority-sheet density map is Lipschitz in the root-`L1` product metric

\[
d_{1/2}(F,G)=\sum_i\|f_i-g_i\|_1^{1/2}
\]

with a dimension- and orientation-independent constant `20 sqrt(2)` on this paid chamber.

This is qualitatively stronger than a common height bound: a common `Linf` cap alone does not imply `Linf` convergence of output densities under `L1` source perturbation, whereas the submass theorem does.

## 5. New regularity consequence: rough majority-sheet densities are continuous on the closed half-line

### Theorem 5.1 — `QFORM-RULED-HALFLINE-C0-v1`

Under the same isotropic rank-three ruled hypotheses, for **arbitrary measurable cap-one product marginals**, the positive-sheet output submeasure has a canonical representative

\[
r^+\in C_0([0,\infty))
\]

(where `C_0([0,infinity))` means continuous on the half-line and tending to zero at `+infinity`) satisfying

\[
\boxed{\|r^+\|_\infty\le\pi\sqrt2.} \tag{5.1}
\]

This is a half-line statement for the majority-sheet submeasure; it is not a claim that its zero extension to negative `t` is continuous on all of `R`, and it does not pay the complementary minority/two-sheet output.

### Proof

**Step 1: cap-preserving smooth compact approximation.** For any cap-one probability density `f`, choose `M` with tail mass

\[
e_M=\int_{|x|>M}f(x)\,dx\to0.
\]

Define

\[
g_M=f1_{[-M,M]}+e_M1_{[M+2,M+3]}.
\]

Then `g_M` is a compactly supported probability density, `0<=g_M<=1`, and

\[
\|g_M-f\|_1\le2e_M.
\]

Convolving with a sufficiently narrow nonnegative `C_c^infinity` probability mollifier preserves the cap and total mass and gives a smooth compactly supported probability density `f^(k)` with

\[
\|f^{(k)}-f\|_1\to0. \tag{5.2}
\]

Do this for each of the finitely many original coordinates.

**Step 2: uniform output-density convergence.** Let `r_k^+` be the majority-sheet density for the smooth compact product source. By (4.1),

\[
\|r_k^+-r^+\|_\infty
\le20\sqrt2\sum_i
\|f_i^{(k)}-f_i\|_1^{1/2}\longrightarrow0. \tag{5.3}
\]

Here `r^+` is the density supplied by the partner's rough interval theorem; equivalently, (5.3) itself identifies the limiting density version.

**Step 3: smooth approximant density is continuous up to the sheet vertex.** For a smooth compact product density, the projected density `rho_k` of `Y=R^T X` belongs to `C_c^infinity(R^3)`. The completed ruled identity gives for `s>=0`

\[
r_k^+(s)=\frac12\int_0^{2\pi}\int_{\mathbb R}
\rho_k(\sqrt{s}\,e_\theta+t(e_\theta^\perp+e_3))\,dt\,d\theta. \tag{5.4}
\]

For `s>0` continuity is immediate; as `s downarrow0`, the integrand converges pointwise to

\[
\rho_k(t(e_\theta^\perp+e_3)).
\]

Compact support supplies one integrable dominating `t`-interval, so dominated convergence proves that `r_k^+` has a finite right limit at zero. Compact support also gives vanishing at infinity. Hence

\[
r_k^+\in C_0([0,\infty)). \tag{5.5}
\]

**Step 4: pass continuity after height/stability, not before.** Uniform convergence (5.3) shows that `r^+` is the uniform limit on `[0,infinity)` of the `C_0` functions `r_k^+`; therefore `r^+ in C_0([0,infinity))`. Each smooth approximation satisfies the completed probability height `pi sqrt(2)`, so the same bound passes to the uniform limit, proving (5.1).

This is the desired separation: the essential height theorem is paid first by the partner's ruled geometry; source-stability then transports a stronger continuity statement to rough marginals. Continuity is never used to manufacture the height.

### Why this is not a global `C_0(R)` statement

Take `R=I_3`, `q=x_1^2+x_2^2-x_3^2`, and iid `Unif[-1/2,1/2]`. At the sheet vertex, (5.4) gives exactly

\[
\lim_{s\downarrow0}r^+(s)
=\frac12\int_0^{2\pi}\int_{-1/2}^{1/2}dt\,d\theta
=\pi. \tag{5.6}
\]

The positive-sheet submeasure is zero for negative output values, so its zero extension has a jump at zero. Thus the natural new regularity is precisely continuity on the paid half-line; global continuity of the **full** output law requires combining both sheets and is a separate conclusion.

## 6. Actual exact-target inequality: `Q=2XY+Z^2`

Let

\[
A_0=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix},
\qquad \operatorname{spec}(A_0)=\{1,-1,1\}.
\]

Take `Y,Z~Unif[0,1]`. For `0<=epsilon<=1/2`, let

\[
X_0\sim\operatorname{Unif}[0,1],\qquad
X_\epsilon\sim\operatorname{Unif}[\epsilon,1+\epsilon].
\]

All densities are cap one, and

\[
\delta=\|f_{X_\epsilon}-f_{X_0}\|_1=2\epsilon\le1. \tag{6.1}
\]

Because all three variables are nonnegative,

\[
Q_\epsilon=2X_\epsilon Y+Z^2\ge0
\]

almost surely, so the partner's majority-sheet density is the **full output density** `p_epsilon`. The completed partner theorem and the new positivity refinement give the genuine owner-target inequalities

\[
\boxed{\|p_\epsilon\|_\infty\le\pi\sqrt2,} \tag{6.2}
\]

\[
\boxed{\|p_\epsilon-p_0\|_\infty\le40\sqrt\epsilon,} \tag{6.3}
\]

\[
\boxed{\|p_\epsilon-p_0\|_1\le2\epsilon,} \tag{6.4}
\]

and, at `r=2`,

\[
\boxed{\|p_\epsilon-p_0\|_2\le4\sqrt5\,\epsilon^{3/4}.} \tag{6.5}
\]

Moreover `2X_epsilon Y` has an `L1` density and `Z^2` has an `L1` density, and the two terms are independent. Therefore

\[
p_\epsilon=p_{2X_\epsilon Y}*p_{Z^2}\in C_0(\mathbb R). \tag{6.6}
\]

So this is an exact rank-three owner-target family where the universal height and the continuous representative coexist, and the source-to-density map has the optimal `1/2` `L1 -> Linfinity` exponent.

The partner's exact moved-mass construction for the same `Q=2XY+Z^2` yields a lower difference asymptotic

\[
(1-\log2)\sqrt\delta+o(\sqrt\delta),
\]

so no class-uniform exponent greater than `1/2` is possible even within this fixed target matrix and continuous-density branch.

## 7. Explicit downstream output modulus after one independent square

The distinction between a height theorem and a continuity theorem can be made quantitative without changing the product provenance. Add an independent `W~Unif[0,1]` and set

\[
\widetilde Q_\epsilon=2X_\epsilon Y+Z^2+W^2.
\]

The matrix spectrum is `{1,-1,1,1}`, so this remains an owner-target form. Let

\[
h(u)=\frac{1}{2\sqrt u}1_{(0,1)}(u)
\]

be the density of `W^2`. Then

\[
\widetilde p_\epsilon=p_\epsilon*h.
\]

Young's inequality and (6.2)--(6.3) give

\[
\boxed{
\widetilde p_\epsilon\in C_0(\mathbb R),\qquad
\|\widetilde p_\epsilon\|_\infty\le\pi\sqrt2,\qquad
\|\widetilde p_\epsilon-\widetilde p_0\|_\infty\le40\sqrt\epsilon.
} \tag{7.1}
\]

For `|a|<=1`, the square density has the exact translation distance

\[
\|\tau_a h-h\|_1=2\sqrt{|a|}. \tag{7.2}
\]

Indeed, for `a>=0`, on the overlap `[a,1]` the smaller of `h(u)` and `h(u-a)` is `h(u)`, whose overlap mass is `1-sqrt(a)`; the `L1` distance between two probability densities is twice one minus their overlap mass. The negative-shift case follows by translation invariance.

Hence

\[
\boxed{
\|\tau_a\widetilde p_\epsilon-\widetilde p_\epsilon\|_\infty
\le2\pi\sqrt2\,\sqrt{|a|},\qquad |a|\le1.
} \tag{7.3}
\]

Combining source and output perturbations gives the explicit joint regularity estimate

\[
\boxed{
\sup_t|\widetilde p_\epsilon(t+a)-\widetilde p_0(t)|
\le40\sqrt\epsilon+2\pi\sqrt2\sqrt{|a|}.
} \tag{7.4}
\]

This is an example of the intended logical order: a height is first paid by the ruled theorem, and only then does a genuine independent original-coordinate smoothing block supply a quantitative `C_0` modulus with no loss in the height.

## 8. Secondary fixed-matrix consequence

The source-pinned account03/B15 theorem

`yspennstate/math-open-problems@696a0784ba7d270db657c1596d9c2ee940a1745d`

proves, for each fixed symmetric `A` with `rank(A)>=3` and coordinate `j`, a finite constant `K(A,j)` such that every cap-one subdensity of mass `m` in coordinate `j` has a full quadratic output density in `C_0(R)` bounded by `K(A,j) sqrt(m)`. Its stated signed marginal stability bound pays a `sqrt(2)` factor by splitting positive and negative parts.

Lemma 2.1 applies verbatim and improves that fixed-matrix statement locally to

\[
\boxed{
\|p_f-p_g\|_\infty
\le K(A,j)\|f_j-g_j\|_1^{1/2}
\quad\text{when }\|f_j-g_j\|_1\le1.
} \tag{8.1}
\]

Thus, at fixed `A`, the canonical `C_0` output density is locally `1/2`-Holder in each marginal in the **sup norm**. The constants `K(A,j)` may deteriorate arbitrarily with the matrix and therefore do not solve the universal-height conjecture; this is a regularity compiler only.

## 9. Regularity hierarchy and remaining full-target gap

The logically distinct implications are now:

1. **Qualitative absolute continuity.** For any nonzero quadratic form and any absolutely continuous joint input, the scalar pushforward is absolutely continuous. This is much weaker than a density-height estimate and does not use the cap-one hypothesis.
2. **Uniform essential height on the ruled majority sheet.** The completed account02/B15 geometry pays this directly, with probability height `pi sqrt(2)` and submass height `20 sqrt(2) sqrt(m)`.
3. **Source-law regularity.** Positivity turns the submass estimate into the sharper `L1 -> Linfinity` estimate (3.1), with optimal exponent `1/2`.
4. **Output-variable continuity.** Uniform source stability transports smooth-core continuity to arbitrary rough inputs on the closed paid half-line, yielding Theorem 5.1. Global `C_0(R)` for a full output is a stronger statement and requires the complementary sheet or an independent smoothing resource.
5. **No universal output modulus follows from the bare target.** The earlier B15 exact-target construction with `A=I_3` and smooth cap-one inputs already shows that even a uniform height and smooth sources do not yield class-uniform equicontinuity. The explicit modulus (7.3) is possible only because a specific independent smoother is retained.

The full QFORM conjecture is still open. The principal unpaid implication remains the complementary minority/two-sheet side and, more globally, the higher-rank/diffuse configurations in which the three-large-eigenvalue hypothesis does not force one uniformly conditioned physical receiver. The live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction forbids replacing that step by a generic projection/X-ray norm; product provenance must remain coupled to the curvature.

## 10. Corrections preserved

- no uniform pointwise quadratic Fourier decay is used;
- no independence is asserted after rotation;
- no projection-only/X-ray shortcut is used to pay the missing two-sheet side;
- no arbitrary-joint coarea **height** estimate is used;
- no conditional density-cap preservation is assumed;
- continuity is always downstream of an already-paid height or of a source-stability theorem.

Full unrestricted target status: **OPEN / NOT PROVED**.
