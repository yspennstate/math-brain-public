# QFORM B17 — arbitrary-heavy unequal-bank sharpening and a fragmented-bank cone-tip barrier

Run: `20260923T150426Z-fleet01-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: fleet01/B17, sharp constant and witnesses  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREMS; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Full-target continuity: separate and still open.

## 1. Main theorem: arbitrary heavy law + unequal opposite cube banks is globally below `3sqrt(2)` with the exact two-norm crossover

Let `a in R^m`, `b in R^n` be unit vectors. Let

`S_a=sum_i a_i U_i`, `T_b=sum_j b_j V_j`,

where all `U_i,V_j` are independent `Unif[-1/2,1/2]`. Let `X_f` be independent with an **arbitrary** probability density `0<=f<=1`; no centering, support, connectedness, moment, unimodality or finite-fragment assumption is made on `f`.

For `alpha,beta,gamma>=1`, put

`Q = alpha X_f^2 + beta S_a^2 - gamma T_b^2`.

The physical matrix is

`A=diag(alpha, beta aa^T, -gamma bb^T)`,

so its nonzero spectrum is exactly `{alpha,beta,-gamma}`. Thus every finite member is a genuine target instance with three eigenvalues of modulus at least one, and the two bank blocks are generally non-diagonal in the independent physical coordinates.

### Theorem `QFORM-ARBITRARY-HEAVY-UNEQUAL-CUBE-BANKS-SHARPENED-v1`

For every such `alpha,beta,gamma,a,b,f`,

\[
\boxed{
\|p_Q\|_\infty
\le {4\over\sqrt\alpha}
\int_0^1
{\min\left\{(2\beta)^{-1/2},\,[2\sqrt u(\beta\gamma)^{1/4}]^{-1}\right\}
\over\sqrt{1-u^2}}\,du
\le K_{\rm cone}<3\sqrt2,
}
\tag{1.1}
\]
where

\[
K_{\rm cone}
={\pi\sqrt2\over3}
+2\int_{1/2}^1{du\over\sqrt u\sqrt{1-u^2}}
=3.8172923460947289091100\ldots .
\tag{1.2}
\]

In particular the equal-magnitude class satisfies the strict uniform gap

\[
3\sqrt2-K_{\rm cone}
=0.4253483410245562372950\ldots .
\tag{1.3}
\]

This closes the first unpaid face left by the preceding fleet01/B17 run: **arbitrary cap-one heavy law together with arbitrary unequal centered-cube opposite bank profiles**.

## 2. Actual use of the completed fleet02/B17 result

The newest completed designated-partner theorem is source-pinned at

`yspennstate/math-open-problems@9cd98044087dd0e8bafe8ee2900cf1686552c802`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T142532Z-fleet02-B17-QFORM-auto11/REPORT.md`.

For `alpha=beta=gamma=1`, it proves for every output level `t`

\[
p_Q(t)\le P_{a,b}(t)\le P_{a,b}(0),
\tag{2.1}
\]
with

\[
P_{a,b}(0)
=4\int_0^1 {I(u)\over\sqrt{1-u^2}}\,du,
\qquad
I(u)=\int_0^\infty h_b(r)h_a(ur)\,dr,
\tag{2.2}
\]
where `h_a,h_b` are the two centered-cube projection densities. The global step is nontrivial: it removes the arbitrary heavy density by `f<=1` and uses symmetric unimodality of the two cube-bank densities to show the cap-one envelope is maximized at output zero.

The same pinned source, together with the Rudelson--Vershynin/Rogozin--Ball one-dimensional product-projection theorem, gives

\[
\|h_a\|_\infty,\|h_b\|_\infty\le\sqrt2,
\qquad
\|h_a\|_2^2,\|h_b\|_2^2\le1.
\tag{2.3}
\]
The `L^2` statement follows by applying the projection theorem to `(S_a-S_a')/sqrt(2)` and evaluating its density at zero.

Consequently

\[
I(u)\le {1\over\sqrt2},
\qquad
I(u)\le {1\over2\sqrt u}.
\tag{2.4}
\]
The **exact crossover is `u=1/2`**. Splitting (2.2) there, rather than at the nonoptimal `1/sqrt(2)` used for the partner's simpler closed constant, gives precisely (1.2):

\[
P_{a,b}(0)
\le 4\left[
{1\over\sqrt2}\int_0^{1/2}{du\over\sqrt{1-u^2}}
+{1\over2}\int_{1/2}^1{du\over\sqrt u\sqrt{1-u^2}}
\right]
=K_{\rm cone}.
\tag{2.5}
\]

Thus the partner theorem is applied to an actual new inequality, not merely cited:

\[
\boxed{
\sup_{\|a\|=\|b\|=1}\sup_{0\le f\le1}
\|p_{X_f^2+S_a^2-T_b^2}\|_\infty
\le K_{\rm cone}=3.81729234609\ldots<3\sqrt2.
}
\tag{2.6}
\]

The partner's previous elementary constant was

\[
K_*={\pi\over2}(\sqrt2+2^{1/4})
=4.089443637123813\ldots,
\]
so (2.6) improves it by

`K_*-K_cone = 0.27215129102908466...`.

For general `alpha,beta,gamma>=1`, scale the three independent aggregates by `sqrt(alpha),sqrt(beta),sqrt(gamma)`. The heavy density cap becomes `alpha^{-1/2}`; the bank `L^infinity` caps become `sqrt(2/beta),sqrt(2/gamma)` and the squared `L^2` norms become at most `beta^{-1/2},gamma^{-1/2}`. Repeating (2.1)--(2.5) gives the coefficient-sensitive first bound in (1.1). Since all three coefficients are at least one, it is at most the equal-magnitude value `K_cone`.

## 3. Elementary certificate below `3sqrt(2)`

For a decimal-free certificate, convexity of `u^{-1/2}` on `[1/2,1]` gives the chord bound

\[
u^{-1/2}
\le (2\sqrt2-1)+2(1-\sqrt2)u.
\]
Hence

\[
K_{\rm cone}
\le K_{\rm sec}
:={\pi(5\sqrt2-2)\over3}-2\sqrt3(\sqrt2-1).
\tag{3.1}
\]
Using `pi<22/7` and `sqrt(3)>5/3` in the sign-correct direction,

\[
K_{\rm sec}< {40\sqrt2+26\over21}<3\sqrt2,
\tag{3.2}
\]
because `26<23sqrt(2)`. In particular

\[
3\sqrt2-K_{\rm cone}>{23\sqrt2-26\over21}>0.
\tag{3.3}
\]

The checker reproduces the high-precision values and all exact matrix identities below.

## 4. New broader cone-tip theorem: the bank laws themselves may be arbitrary and fragmented

The global monotonicity in the partner theorem uses symmetric unimodality of centered cube projections. At the **cone tip**, however, that assumption is unnecessary.

Let the physical variables in the first bank be arbitrary independent cap-one variables `Y_i`, and in the second bank arbitrary independent cap-one variables `Z_j`; translations, disconnected supports and nonunimodal densities are allowed. Set

`S=sum_i a_i Y_i`, `T=sum_j b_j Z_j`, with `||a||_2=||b||_2=1`,

and let `X_f` be any independent cap-one variable. Put

`Q=X_f^2+S^2-T^2`.

The Rudelson--Vershynin/Rogozin--Ball theorem gives

\[
\|h\|_\infty,\|k\|_\infty\le\sqrt2
\tag{4.1}
\]
for the densities `h,k` of `S,T`. Applying it to the normalized self-differences gives

\[
\|h\|_2^2,\|k\|_2^2\le1.
\tag{4.2}
\]
Define the positive-half symmetrizations

\[
H(r)=h(r)+h(-r),\qquad K(r)=k(r)+k(-r),\quad r>0.
\]
Then

\[
\int_0^\infty H=\int_0^\infty K=1,
\quad
\|H\|_\infty,\|K\|_\infty\le2\sqrt2,
\quad
\|H\|_2^2,\|K\|_2^2\le2.
\tag{4.3}
\]
The density of `T^2` at `y>0` is `K(sqrt(y))/(2sqrt(y))`. Using only `f<=1` and polar coordinates in `(x,s)` gives the canonical cone-tip value

\[
\begin{aligned}
p_Q(0)
&\le \iint h(s){K(\sqrt{x^2+s^2})\over2\sqrt{x^2+s^2}}\,ds\,dx\\
&=\int_0^1{J(u)\over\sqrt{1-u^2}}\,du,
\qquad
J(u)=\int_0^\infty H(ur)K(r)\,dr.
\end{aligned}
\tag{4.4}
\]
From (4.3),

\[
J(u)\le2\sqrt2,
\qquad
J(u)\le {2\over\sqrt u}.
\tag{4.5}
\]
Again the exact crossover is `u=1/2`, so

\[
\boxed{p_Q(0)\le K_{\rm cone}<3\sqrt2.}
\tag{4.6}
\]

This is strictly broader at the cone tip than the cube-bank theorem: **both opposite banks may now come from arbitrary fragmented/nonunimodal cap-one physical marginals**. It does not claim the output mode is zero.

With coefficients `alpha,beta,gamma>=1`, the same scaling gives

\[
p_Q(0)
\le {1\over\sqrt\alpha}\int_0^1
{\min\{2\sqrt{2/\beta},\ 2/[\sqrt u(\beta\gamma)^{1/4}]\}
\over\sqrt{1-u^2}}\,du
\le K_{\rm cone}.
\tag{4.7}
\]

## 5. A global fallback for arbitrary fragmented banks: `pi sqrt(2)`

The same disjoint-bank architecture has a simple global bound even without unimodality. Since `X_f` and `S` are independent and have density caps `1` and `sqrt(2)`, their squared variables satisfy

\[
p_{X_f^2}(y)\le y^{-1/2},
\qquad
p_{S^2}(y)\le\sqrt2\,y^{-1/2},\quad y>0.
\]
Therefore the same-sign sum `A_+=X_f^2+S^2` has

\[
\|p_{A_+}\|_\infty
\le\sqrt2\int_0^y{du\over\sqrt{u(y-u)}}
=\pi\sqrt2.
\]
Convolution with the independent reflected law `-T^2` cannot increase `L^infinity`, hence

\[
\boxed{\|p_{X_f^2+S^2-T^2}\|_\infty\le\pi\sqrt2=4.44288293815\ldots.}
\tag{5.1}
\]

Combining (4.6) and (5.1), any hypothetical overshoot above `3sqrt(2)` inside this broad disjoint `1+rank1-rank1` architecture must be an **off-zero** phenomenon, and even then it is confined to the narrow window

\[
3\sqrt2 < \|p_Q\|_\infty\le\pi\sqrt2,
\qquad
\pi\sqrt2-3\sqrt2=\sqrt2(\pi-3)=0.2002422510\ldots .
\tag{5.2}
\]
This does not show that such an overshoot actually exists.

## 6. Exact fragmented/nonunimodal stress family

Take

\[
a=(1,1)/\sqrt2,
\qquad
b=(2,1,2)/3,
\]
so in six independent physical coordinates

\[
A=\begin{pmatrix}
1&0&0&0&0&0\\
0&1/2&1/2&0&0&0\\
0&1/2&1/2&0&0&0\\
0&0&0&-4/9&-2/9&-4/9\\
0&0&0&-2/9&-1/9&-2/9\\
0&0&0&-4/9&-2/9&-4/9
\end{pmatrix}.
\tag{6.1}
\]
Exactly `A^3=A`, `tr(A)=1`, `tr(A^2)=3`, hence

\[
\operatorname{spec}(A)=\{1,1,-1,0,0,0\}.
\tag{6.2}
\]

For any integer `M>=2` and separation `D>2`, one may choose **every** physical marginal to have density equal to the indicator of a union of `M` disjoint intervals of length `1/M`, separated by distances comparable to `D` (with different translations in the six coordinates if desired). These are probability densities with cap exactly one; their linear-bank densities are generally highly multimodal. The theorem above still gives

\[
p_Q(0)\le K_{\rm cone}<3\sqrt2,
\qquad
\|p_Q\|_\infty\le\pi\sqrt2.
\tag{6.3}
\]
Thus arbitrary fragment count and arbitrarily large support diameter in **all three physical groups** do not create a cone-tip witness above the diffuse obstruction for this non-diagonal bank matrix.

For centered unit-interval bank coordinates but an arbitrary fragmented heavy coordinate, the stronger global theorem (1.1) applies and gives the full `K_cone` bound at every output level.

## 7. Comparison with the newest exact dense finite witness

The immediately preceding fleet01/B17 source-pinned run

`yspennstate/math-open-problems@e83d0cc194d791acf31d6c86245204887cfd8171`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260923T144233Z-fleet01-B17-QFORM-auto11/REPORT.md`,

constructed a fully dense six-variable three-bank rotation with the same nonzero spectrum `{1,1,-1}` and exact cone-tip value

\[
p_{\rm dense}(0)=4.0630706168060372601\ldots .
\tag{7.1}
\]
This is already

\[
4.063070616806\ldots-K_{\rm cone}
=0.245778270711\ldots
\tag{7.2}
\]
**above the global ceiling of the entire arbitrary-heavy/unequal-centered-cube direct-sum architecture** in Theorem 1.

That comparison isolates a genuine sharpness mechanism: finite density amplification is not explained by an adversarial heavy coordinate or unequal leverage redistribution in two disjoint opposite rank-one banks. Coupling the sign geometry across all three independent banks can do strictly more. A sharp proof based only on one-heavy/two-bank reduction would lose real finite extremizers.

The best source-valid universal lower obstruction nevertheless remains the diffuse exact-spectrum construction

\[
\boxed{C_{\rm univ}\ge3\sqrt2=4.242640687119\ldots,}
\tag{7.3}
\]
source-pinned at `yspennstate/math-open-problems@15e9504309108d37a6c5f8bcacebac07eb4fe1ff`, where exact finite cube frames with spectrum `{1,1,-1}` approach `3sqrt(2)` from below.

## 8. What remains for B17

The new results eliminate or sharply constrain several witness mechanisms:

- unequal centered-cube opposite banks + arbitrary heavy law: **global `<3sqrt(2)`**, with ceiling `K_cone=3.81729...`;
- arbitrary fragmented/nonunimodal laws in both opposite disjoint banks: **cone tip `<3sqrt(2)`**, global `<=pi sqrt(2)`;
- fully dense three-bank rotations: can already reach `4.06307...`, so genuine cross-bank sign orientation matters;
- diffuse exact-spectrum frames still force `C_univ>=3sqrt(2)`.

The first serious unpaid sharp-witness mechanisms are therefore an **off-zero fragmented-bank peak**, genuinely shared/non-collinear intermediate-leverage rows, or additional active spectrum. Any proof of a sharp `3sqrt(2)` bound must handle those without using the refuted arbitrary-joint coarea, post-rotation independence, pointwise stationary-phase decay, bounded-fragment reduction, or a universally good single coordinate minor/cross cut.

No claim is made that `3sqrt(2)` is the unrestricted sharp constant, and no full-target continuity result is claimed.

## 9. Sources and correction discipline

Actual dependencies used:

1. fleet02/B17 completed unequal cube-bank envelope theorem: `math-open-problems@9cd98044087dd0e8bafe8ee2900cf1686552c802`, exact report path above.
2. Product-projection cap `sqrt(2)` and its source attribution to Rudelson--Vershynin/Rogozin--Ball: `math-open-problems@18fb381e300dd86514835d27eedcf2507ab09227`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T130245Z-fleet03-B02-QFORM-r11/REPORT.md`; that report cites Rudelson--Vershynin, IMRN 2015, Theorem 1.2, DOI `10.1093/imrn/rnu243`, arXiv `1402.4492`.
3. Exact dense six-variable witness: `math-open-problems@e83d0cc194d791acf31d6c86245204887cfd8171`, exact report path in Section 7.
4. Diffuse `3sqrt(2)` obstruction and negative first periodic Edgeworth correction: `math-open-problems@15e9504309108d37a6c5f8bcacebac07eb4fe1ff`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B17/20260922T123638Z-fleet01-B17-qform-diffuse-edgeworth-v1/REPORT.md`.

Fresh live corrections consumed before this proof include: law-uniform pointwise oscillatory decay is false; arbitrary-joint rank-three coarea is false; post-rotation independence is unavailable; positive conditional projection-density moments can diverge; a uniformly good physical minor/cross-cut need not exist; bounded fragment count is not a valid general reduction. None is used as a premise here.

Full QFORM status remains **OPEN / NOT PROVED / NOT DISPROVED**.
