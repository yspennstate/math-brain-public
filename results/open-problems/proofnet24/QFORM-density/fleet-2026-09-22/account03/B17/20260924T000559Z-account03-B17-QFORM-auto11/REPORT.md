# QFORM B17 — sharpened null-pair plus square theorem

Run: `20260924T000559Z-account03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Classification: **NEW SUPPORTING ANALYTIC IMPROVEMENT; FULL QFORM OPEN**  
Continuity: proved for this exact branch; full-target continuity remains open.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Result

Let `X,Y,Z` be independent real random variables with probability densities bounded by one. For nonzero real `a,b`, set

\[
Q=2aXY+bZ^2.
\]

Then `Q` has a continuous density and

\[
\boxed{
\|p_Q\|_\infty\le \mathcal C(a,b):=
\begin{cases}
\dfrac{2+\log(4|a|/|b|)}{|a|},& |b|\le4|a|,\\[1.1ex]
\dfrac4{\sqrt{|ab|}},& |b|\ge4|a|.
\end{cases}}
\tag{1}
\]

In particular, on the exact target range `|a|>=1, |b|>=1`,

\[
\boxed{\|p_Q\|_\infty\le 2+\log4=3.38629436111989\ldots<3\sqrt2.}
\tag{2}
\]

This strictly sharpens the previous source-valid `4/sqrt(|ab|)` null-pair theorem in its most important target normalization `|a|,|b|>=1`.

The physical matrix

\[
A_{a,b}=\begin{pmatrix}0&a&0\\a&0&0\\0&0&b\end{pmatrix}
\]

has eigenvalues `{a,-a,b}`. Thus every `|a|,|b|>=1` member is an exact non-diagonal target instance with three eigenvalues of magnitude at least one. No moments, bounded support, connected support, log-concavity, Gaussianity, or post-rotation independence are used.

## 2. Exact root formula

By reflecting `Q` and/or inputs it is enough to keep absolute values in the computation. For almost every `y!=0`, resolve the quadratic level equation in `x`:

\[
x={q-bz^2\over2ay}.
\]

Therefore

\[
p_Q(q)=\int_{\mathbb R}{f_Y(y)\over2|ay|}
\left[\int_{\mathbb R}f_Z(z)
 f_X\!\left({q-bz^2\over2ay}\right)dz\right]dy.
\tag{3}
\]

Denote the bracket by `I_y(q)`.

## 3. The missing probability-mass cap

The previous `4/sqrt(|ab|)` proof bounded the square density by its pointwise `t^{-1/2}` envelope and thereby discarded the fact that `f_Z` has total mass one. Retaining that fact gives two simultaneous bounds.

First, because `0<=f_X<=1`,

\[
I_y(q)\le\int f_Z(z)dz=1.
\tag{4}
\]

Second, because `0<=f_Z<=1`,

\[
I_y(q)\le \int_{\mathbb R}
 f_X\!\left({q-bz^2\over2ay}\right)dz.
\tag{5}
\]

Let

\[
\beta={|b|\over2|a y|}.
\]

After the change from `z` to the parabola coordinate, (5) is a one-dimensional bathtub problem. Among all `0<=f_X<=1` with mass one, the preimage length under `z -> c +/- beta z^2` is maximized by placing the unit `x`-mass immediately adjacent to the vertex. The maximal preimage length is exactly

\[
2\beta^{-1/2}=2\sqrt{2|ay|/|b|}.
\tag{6}
\]

Equivalently, one may write the Jacobian kernel as a constant multiple of `(c-x)_+^{-1/2}` and apply the elementary bathtub integral `int_0^1 u^{-1/2}du=2`.

Combining (4) and (6),

\[
I_y(q)\le \min\left\{1,\ 2\sqrt{2|ay|/|b|}\right\}.
\tag{7}
\]

Substitution into (3) gives the global, output-uniform envelope

\[
p_Q(q)\le\int f_Y(y)K_{a,b}(|y|)dy,
\tag{8}
\]
where

\[
K_{a,b}(r)=
\min\left\{
{1\over2|a|r},
{\sqrt2\over\sqrt{|ab|}\sqrt r}
\right\}.
\tag{9}
\]

The function `K_{a,b}` is even after composition with `|y|` and strictly decreasing in `r>0`.

## 4. Second bathtub and exact coefficient formula

Since `f_Y<=1` and has mass one, the bathtub principle applied to the decreasing reward (9) yields

\[
\int f_Y(y)K_{a,b}(|y|)dy
\le 2\int_0^{1/2}K_{a,b}(r)dr.
\tag{10}
\]

The two branches in (9) meet at

\[
r_0={|b|\over8|a|}.
\tag{11}
\]

If `|b|>=4|a|`, then `r_0>=1/2` and the square-root branch is active throughout `[0,1/2]`, giving

\[
2\int_0^{1/2}K_{a,b}(r)dr={4\over\sqrt{|ab|}}.
\tag{12}
\]

If `|b|<=4|a|`, split at `r_0`:

\[
\begin{aligned}
2\int_0^{1/2}K_{a,b}(r)dr
&=2\left[
{\sqrt2\over\sqrt{|ab|}}\int_0^{r_0}r^{-1/2}dr
+{1\over2|a|}\int_{r_0}^{1/2}{dr\over r}
\right]\\
&={2+\log(4|a|/|b|)\over|a|}.
\end{aligned}
\tag{13}
\]

This proves (1).

## 5. Target optimization

Assume `|a|>=1, |b|>=1` and put `rho=|b|/|a|`.

For `1<=rho<=4`, (13) is at most `2+log4`, with equality in this upper-bound formula at `|a|=|b|=1`. For `0<rho<1`, the constraint `|b|>=1` forces `|a|>=1/rho`, so

\[
\mathcal C(a,b)\le \rho\,[2+\log(4/\rho)]\le2+\log4,
\]

because the displayed scalar function is increasing on `(0,1]`. For `rho>=4`, (12) gives at most `2`. Hence

\[
\sup_{|a|,|b|\ge1}\mathcal C(a,b)=2+\log4.
\tag{14}
\]

A completely elementary strict comparison with the known universal obstruction is available: `log4<3/2` because

\[
e^{3/2}>1+{3\over2}+{(3/2)^2\over2}+{(3/2)^3\over6}={67\over16}>4.
\]

Thus

\[
2+\log4<{7\over2}<3\sqrt2,
\tag{15}
\]

where the last inequality follows by squaring: `49/4<18`.

## 6. Continuity in this branch

For every fixed `y!=0`, the variable `2ayX` has an `L^1` density and `bZ^2` has an `L^1` density, so their convolution has a continuous representative. Equation (7) divided by `2|ay|` supplies the integrable domination `K_{a,b}(|y|)`. By (10) this dominator is integrable against every cap-one `f_Y`. Dominated convergence in `y` therefore yields a continuous representative of `p_Q`.

This continuity conclusion is only for this exact branch. It does not establish full-target continuity.

## 7. Exact rotated stress interpretation and ambient extension

At `a=b=1`,

\[
A=\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}
\]

has spectrum `{1,1,-1}` and the exact physical form `Q=2XY+Z^2`. Its two eigenvectors in the first two coordinates are the 45-degree combinations `(e_1+e_2)/sqrt2` and `(e_1-e_2)/sqrt2`; hence this is genuinely non-diagonal in the independent physical coordinates.

Arbitrary affine terms in `X,Y,Z` can be removed by translations, exactly as in the previous null-pair theorem, and translations preserve the one-dimensional density caps. Therefore if an arbitrary ambient quadratic form contains this exact three-coordinate physical principal block, conditioning on all outside original coordinates leaves only affine perturbations and the same bound (1) holds uniformly in the conditioning.

## 8. Designated partner result applied to an actual inequality

The completed designated `account04/B17` report

`yspennstate/math-open-problems@2156b76156ad5956c214a881fcfd6d977d6f3b9f`,
`proofnet24/QFORM-density/fleet-2026-09-22/account04/B17/20260922T211900Z-account04-B17-QFORM-r3/REPORT.md`

constructs exact finite cap-one rotated matrices with nonzero spectrum `{1,1,-1}` and proves

\[
p_{Q_m}(0)=3\sqrt2\left(1-{5295\over21952m}+O(m^{-2})\right),
\]

hence every universal constant satisfies

\[
C_*\ge3\sqrt2.
\tag{16}
\]

Combining (2) and (16) gives the concrete mechanism-separation inequality

\[
\boxed{
\sup_{\substack{|a|,|b|\ge1\\ f_X,f_Y,f_Z\le1}}
\|p_{2aXY+bZ^2}\|_\infty
\le2+\log4
<3\sqrt2
\le C_*.
}
\tag{17}
\]

Thus a pair of complementary physical lightlike rows plus an independent square is not merely bounded below the known obstruction: the previous constant four can be improved by more than `0.61`, to `3.386294...`, for every arbitrary cap-one law in the branch.

## 9. What remains unpaid

The full QFORM conjecture remains open. The theorem pays one exact rotated rank-three architecture (and ambient forms containing that exact principal block), but it does not force such a block from the bare spectral hypothesis. It does not control several non-null macroscopic rows, fully coupled three-coordinate blocks without the null-pair algebra, near-null perturbations, or arbitrary higher-rank interactions.

For B17 witness search the consequence is sharp: the exact null-pair-plus-square family is now even farther below the `3sqrt2` lower obstruction, so a sharper witness must leave this algebraic architecture rather than tune fragmented one-dimensional laws inside it.

## 10. Integrity notes

No law-uniform pointwise oscillatory decay, post-rotation independence, arbitrary-joint coarea theorem, naive fiber-supremum integration, fixed-fragment extremality, conditional-density cap, or Monte Carlo histogram is used. All conditioning is on original independent coordinates. The proof is analytic and global in the output level.
