# fleet01/B17 — infinitesimal spectral-frame Gaussian floor, sharp 3sqrt(2) mixed-frame witness, and tetrahedral Poisson loss

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T080908Z-fleet01-B17-auto11`  
Status: `NEW SUPPORTING THEOREM / EXACT ROTATED SHARP WITNESS / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Unrestricted continuity remains separate. This report concerns the sharp-constant mechanism in the exact-rank-three diffuse/infinitesimal spectral-frame chamber.

## 1. A cap-one subprobability variance lemma

### Lemma 1
Let `g:R-> [0,1]` be measurable with mass

\[
q=\int g(x)\,dx\in[0,1].
\]

Then for every `a in R`,

\[
\int (x-a)^2g(x)\,dx\ge \frac{q^3}{12}.
\tag{1.1}
\]

Equivalently, if `nu` is the subprobability measure with density `g`, then

\[
\int x^2\,d\nu(x)-\Big(\int x\,d\nu(x)\Big)^2\ge\frac{q^3}{12}.
\tag{1.2}
\]

#### Proof
If `q=0` there is nothing to prove. Normalize `h=g/q`. Then `h` is a probability density with `||h||_infinity<=1/q`. Among probability densities with cap `M`, the variance is minimized by the centered interval density `M 1_{[-1/(2M),1/(2M)]}`, so

\[
\operatorname{Var}_h(X)\ge\frac1{12M^2}\ge\frac{q^2}{12}.
\]

Thus the centered second moment of the submeasure is `q Var_h >=q^3/12`, proving (1.1) at the conditional mean and hence for every `a`. Also

\[
\int x^2d\nu-(\int x\,d\nu)^2
=q\operatorname{Var}_h(X)+q(1-q)(E_hX)^2
\ge q^3/12,
\]

which proves (1.2). `square`

The constant is exact, already at `q=1`, by a unit interval.

## 2. New theorem: every infinitesimal Parseval spectral array retains Gaussian covariance at least `I/12`

Let `R_m` be an `n_m x 3` real matrix with orthonormal columns,

\[
R_m^TR_m=I_3,
\]

and write its rows as `r_{mi}^T in R^3`. Let the physical variables `X_{mi}` be independent and have one-dimensional densities at most one. Choose deterministic centers `b_{mi}` and put

\[
Z_{mi}=r_{mi}(X_{mi}-b_{mi})\in\mathbb R^3,
\qquad
S_m=\sum_i Z_{mi}=R_m^T(X_m-b_m).
\tag{2.1}
\]

Assume the vector triangular array is infinitesimal,

\[
\forall\varepsilon>0:\quad
\max_i\Pr(\|Z_{mi}\|>\varepsilon)\longrightarrow0,
\tag{2.2}
\]

and that `S_m` converges in law. By the standard Levy--Khintchine convergence theorem for infinitesimal triangular arrays, the limit is infinitely divisible. Let `Sigma_G` be its Gaussian covariance matrix.

### Theorem 2 (`QFORM-INF-TARRAY-GAUSSIAN-FLOOR-v1`)
Under (2.1)--(2.2),

\[
\boxed{\Sigma_G\succeq\frac1{12}I_3.}
\tag{2.3}
\]

#### Proof
Fix a unit vector `u in R^3` and set

\[
a_{mi}=u^Tr_{mi},\qquad
W_{mi}=a_{mi}(X_{mi}-b_{mi}).
\]

The scalar array is infinitesimal because `|W_{mi}|<=||Z_{mi}||`. For fixed `epsilon>0`, let

\[
q_{mi}(\epsilon)=\Pr(|W_{mi}|\le\epsilon),
\qquad q_m^*(\epsilon)=\min_i q_{mi}(\epsilon).
\]

Then `q_m^*(epsilon)->1`. The law of `W_{mi}` has density cap `1/|a_{mi}|` when `a_{mi}!=0`. Restricting it to `[-epsilon,epsilon]` gives a subprobability density of mass `q_{mi}` and cap `1/|a_{mi}|`; applying Lemma 1 after scaling yields

\[
\int_{|w|\le\epsilon}w^2\,dF_{mi}(w)
-\left(\int_{|w|\le\epsilon}w\,dF_{mi}(w)\right)^2
\ge\frac{q_{mi}(\epsilon)^3a_{mi}^2}{12}.
\tag{2.4}
\]

The canonical Gaussian-variance formula in the infinitesimal triangular-array convergence theorem identifies `u^T Sigma_G u` with the `epsilon downarrow0` limit of the row sums of the left side of (2.4). Therefore, for every fixed `epsilon`,

\[
\liminf_m \sum_i[\cdots]
\ge \frac1{12}\liminf_m q_m^*(\epsilon)^3\sum_i a_{mi}^2.
\]

But Parseval gives

\[
\sum_i a_{mi}^2
=u^TR_m^TR_m u=1.
\]

Hence `u^T Sigma_G u>=1/12`. Since `u` was arbitrary, (2.3) follows. `square`

A useful side consequence is that (2.2) itself forces diffuse leverage: since a cap-one density places at most `2L` mass in an interval of radius `L`,

\[
\Pr(\|Z_{mi}\|\le\varepsilon)
\le \min\left(1,\frac{2\varepsilon}{\|r_{mi}\|}\right).
\]

Thus infinitesimality implies

\[
\max_i\|r_{mi}\|\to0.
\tag{2.5}
\]

## 3. Consequence: `3sqrt(2)` is an asymptotic ceiling for every infinitesimal exact-rank-three spectral-frame limit

Let `B` be real symmetric indefinite `3x3` with all three eigenvalue magnitudes at least one, and let

\[
A_m=R_mBR_m^T,
\qquad Q_m=X_m^TA_mX_m.
\tag{3.1}
\]

Suppose, after deterministic centering as above, the latent vector converges and the aggregate deterministic center also converges, so that

\[
R_m^TX_m\Rightarrow Y.
\]

The infinitely divisible limit has the Levy decomposition

\[
Y=G+M,
\]

where `G~N(0,Sigma_G)`, `M` is independent of `G`, and Theorem 2 gives `Sigma_G >= I_3/12`.

The completed designated-partner theorem `QFORM-RANDOM-LOCATION-GAUSSIAN-INDEFINITE-BARRIER-v1` from fleet02/B17, source

`yspennstate/math-open-problems@97d91254e56ad2f8c79b121a0ce8bf66472a11d9:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260924T074629Z-fleet02-B17-QFORM-auto11/REPORT.md`,

therefore gives the actual limit inequality

\[
\boxed{
\|p_{Y^TBY}\|_\infty\le3\sqrt2.
}
\tag{3.2}
\]

This is already a broad sharp-witness barrier: any exact-rank-three stress mechanism produced by an infinitesimal product spectral array can have arbitrary Levy jumps, singular or discrete components, but the cap-one hypothesis forces a surviving independent Gaussian core of covariance at least `I/12`.

There is also a finite-stage transfer. By (2.5), eventually every row leverage is at most `1/2`. Apply the completed Fresnel--Brascamp--Lieb Theorem F at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

with `I` equal to all coordinates. Here `G_I=R_m^TR_m=I_3` and there is no residual quadratic part. Since the active eigenvalue product has absolute value at least one,

\[
|\Phi_m(t)|
\le\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.
\tag{3.3}
\]

The right side is integrable with total mass `24pi`. Weak convergence of `Q_m` gives pointwise characteristic-function convergence; dominated convergence in (3.3) and Fourier inversion therefore yield

\[
\boxed{\|p_{Q_m}-p_{Y^TBY}\|_\infty\to0,}
\qquad
\boxed{\limsup_m\|p_{Q_m}\|_\infty\le3\sqrt2.}
\tag{3.4}
\]

So **within the exact-rank-three infinitesimal spectral-frame chamber, no non-Gaussian infinitely divisible limit can overshoot `3sqrt(2)`**.

This does not cover non-infinitesimal macroscopic physical rows, non-tight/escaping latent centers without a convergent recentering, or additional active spectrum interacting before the rank-three reduction.

## 4. Exact fully mixed rotated witness attaining `3sqrt(2)`

The ceiling in (3.4) is sharp even when every physical coordinate mixes all three spectral directions and the physical matrix is entrywise dense.

Let

\[
R_0=\frac12
\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},
\qquad R_0^TR_0=I_3,
\tag{4.1}
\]

and let

\[
n=\frac{(1,2,3)^T}{\sqrt{14}},
\qquad
B=I-2nn^T
=\frac17
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix}.
\tag{4.2}
\]

Then `B^2=I` and `spec(B)={1,1,-1}`. Stack `m` copies of `R_0/sqrt(m)` to obtain `R_m in R^{4m x 3}` and put

\[
A_m=R_mBR_m^T.
\tag{4.3}
\]

The physical `4x4` block is exactly

\[
R_0BR_0^T=
\begin{pmatrix}
-15/28&-5/28&1/4&17/28\\
-5/28&17/28&-1/4&15/28\\
1/4&-1/4&3/4&1/4\\
17/28&15/28&1/4&5/28
\end{pmatrix},
\tag{4.4}
\]

so **every entry of every `A_m` is nonzero**, and

\[
\boxed{\operatorname{spec}(A_m)=\{1,1,-1,0,\ldots,0\}.}
\tag{4.5}
\]

Moreover

\[
\max_{ij}|(A_m)_{ij}|=\frac{3}{4m}.
\tag{4.6}
\]

Thus every physical principal block `A_m[S]` with `|S|<=m` satisfies

\[
\|A_m[S]\|_{op}
\le |S|\max_{ij}|(A_m)_{ij}|
\le\frac34<1.
\tag{4.7}
\]

No target-scale eigenvalue is visible in any original-coordinate principal block using at most one quarter of the physical coordinates.

Now take iid

\[
X_i\sim U[-1/2,1/2].
\]

The latent vector `Y_m=R_m^TX` is a sum of `4m` independent vector increments. Its covariance is exactly

\[
\operatorname{Cov}(Y_m)=\frac1{12}R_m^TR_m=\frac1{12}I_3,
\]

and the row norms are `sqrt(3)/(2sqrt(m))`, so the multivariate Lindeberg CLT gives

\[
Y_m\Rightarrow G\sim N(0,I_3/12).
\]

Theorem F again upgrades this to global density convergence of the quadratic outputs. Since `B` is a reflection,

\[
G^TBG\stackrel d=G_1^2+G_2^2-G_3^2,
\]

whose global density maximum is

\[
\frac1{2\sqrt2(1/12)}=3\sqrt2.
\]

Therefore

\[
\boxed{\|p_{X^TA_mX}\|_\infty\longrightarrow3\sqrt2.}
\tag{4.8}
\]

This is a source-valid lower witness proving again

\[
\boxed{C_{\rm univ}\ge3\sqrt2,}
\tag{4.9}
\]

but now with a **fully mixed Parseval frame** rather than three disjoint coordinate banks. Diagonal/pi controls are irrelevant to this construction.

## 5. Same exact dense matrix, but tetrahedral Poisson fragmentation is strictly subcritical

Keep the exact same `R_m,B,A_m`. On every physical coordinate instead use

\[
f_m(x)=
\mathbf1_{[-(1-1/m)/2,(1-1/m)/2]}(x)
+
\mathbf1_{[\sqrt m-1/(2m),\sqrt m+1/(2m)]}(x).
\tag{5.1}
\]

This is an exact cap-one probability density. Let the four row vectors of `R_0` be `r_1,...,r_4`. For a physical coordinate of row type `alpha`, one satellite visit contributes asymptotically the vector jump `r_alpha` to the latent projection. A direct characteristic-function expansion gives

\[
R_m^TX\Rightarrow G+M,
\tag{5.2}
\]

where

\[
G\sim N(0,I_3/12),
\qquad
M=\sum_{\alpha=1}^4N_\alpha r_\alpha,
\qquad
N_\alpha\stackrel{ind}{\sim}\operatorname{Poisson}(1),
\tag{5.3}
\]

with `G` independent of the Poisson vector. Equivalently the limiting characteristic function is

\[
\exp\left(-\frac{|t|^2}{24}+\sum_{\alpha=1}^4(e^{it\cdot r_\alpha}-1)\right).
\tag{5.4}
\]

This jump law is genuinely non-axis-aligned: the four jump directions are the four mixed physical rows of `R_0`.

The partner's quantitative noncentral theorem applies to this actual limit. Since every row of `R_0` has norm `sqrt(3)/2`, and every row has first coordinate `1/2`,

\[
M=0\iff N_1=N_2=N_3=N_4=0,
\qquad \Pr(M=0)=e^{-4},
\tag{5.5}
\]

and on `M!=0`,

\[
|M|\ge\frac{\sqrt3}{2}.
\tag{5.6}
\]

Indeed a single jump has norm `sqrt(3)/2`, while two or more jumps have first coordinate at least one.

With `s=1/12`, the standardized noncentrality therefore obeys

\[
D=|M|^2/s\ge9.
\]

Write

\[
C_0=3\sqrt2,
\qquad
C_1=\frac{12e^{-1/2}}{\sqrt{2\pi}}.
\]

The completed fleet02/B17 quantitative inequality gives, on every nonzero atom,

\[
C_9=e^{-9/2}C_0+(1-e^{-9/2})C_1
=2.918523551643465\ldots .
\]

Averaging the zero and nonzero Poisson events yields the concrete global inequality

\[
\boxed{
\|p_{(G+M)^TB(G+M)}\|_\infty
\le e^{-4}C_0+(1-e^{-4})C_9
=2.942775602943225\ldots
<\pi<3\sqrt2.
}
\tag{5.7}
\]

Finally Theorem F gives the same integrable finite-stage characteristic-function majorant (3.3), so the finite output densities converge uniformly to the limit density. Hence

\[
\boxed{
\limsup_{m\to\infty}\|p_{X^TA_mX}\|_\infty
\le2.942775602943225\ldots .
}
\tag{5.8}
\]

This is the requested **actual application of the completed fleet02/B17 theorem to a new target family**. It uses the same exact dense target matrices as the sharp uniform witness, so the strict loss is caused by the non-Lindeberg tetrahedral fragmentation of the cap-one marginals, not by a different spectral geometry.

## 6. Constraint on any proposed sharp proof

Sections 2--5 isolate the sharp mechanism much more tightly:

* `3sqrt(2)` is attained asymptotically by an entrywise-dense, fully mixed, vanishing-leverage exact-rank-three frame; no target-scale small physical principal block is needed.
* Every **infinitesimal** exact-rank-three product spectral array that has a tight Levy limit necessarily retains an independent Gaussian covariance floor `I/12`, and the completed random-location Gaussian theorem caps every such limit by `3sqrt(2)`.
* Even a source-valid non-Lindeberg compound-Poisson perturbation along four non-collinear mixed directions is strictly subcritical (`<2.943`) when it survives only as an independent location component on top of the minimum-variance Gaussian core.

Therefore an overshoot above `3sqrt(2)`, if one exists, must leave this chamber: it must involve a genuinely non-infinitesimal/macroscopic physical row, a non-tight/escaping interaction not reducible to an independent location shift, or additional active spectrum/coupling that survives before exact-rank-three aggregation. This is a proof-mechanism constraint, not a proof that the unrestricted sharp constant equals `3sqrt(2)`.

## 7. Corrections preserved

No post-rotation independence of the original product law is used. No arbitrary-joint coarea bound, conditional projection-density moment bound, pointwise law-uniform quadratic-phase decay, fixed-fragment-count reduction, or fiberwise X-ray-only estimate is used. The finite-stage density convergence relies only on the source-pinned Theorem F in its exact leverage scope. The random-location inequality is used only after the explicit limiting Gaussian-plus-independent-jump decomposition.

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED. Full-target continuity remains OPEN.**
