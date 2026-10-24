SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T00:26:14Z.
attacking: the exact matrix-rank threshold for law-uniform bounded/continuous quadratic pushforwards, and a zero-loss post-height C0 compiler at the target threshold.

# account03/B15 — rank three is the sharp qualitative C0 threshold

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T002614Z-account03-B15-qform-auto29`  
Status: `SHARP_REGULARITY_THRESHOLD_PROVED / PARTNER_APPLIED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and first unpaid implication

The unrestricted owner theorem remains OPEN:

\[
\sup_{\substack{n\ge3,\ s_3(A)\ge1\\ X_i\ \mathrm{independent},\ 0\le f_i\le1}}
\|p_{X^TAX}\|_\infty<\infty.
\]

No counterexample to that theorem is produced here.

The regularity side, however, can now be put at its exact matrix-rank threshold. The completed fixed-matrix theorem at

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`

proves that every fixed symmetric `A` with `rank(A)>=3` and every cap-one product input has an instance-dependent density in `C_0(R) cap L^infinity(R)`. The constants may deteriorate with `A`, so this does not pay the universal target height.

This run proves the converse sharpness: **rank three cannot be lowered in any law-uniform statement asserting that every cap-one product input has a bounded continuous output density.** For every nonzero rank-one matrix there is a cap-one product law giving an inverse-square-root blow-up. For every rank-two indefinite matrix there is a cap-one product law giving a logarithmic blow-up. For every rank-two semidefinite matrix the output is in fact bounded for every cap-one product law, but there is a cap-one product law for which no continuous density representative exists.

Thus rank three is the exact threshold for the property

\[
\boxed{\text{every cap-one product input produces a density in }C_0\cap L^\infty.}
\]

This is a qualitative regularity theorem, not a solution of the matrix-uniform height problem.

## 2. Source-valid inputs used

### 2.1 Fixed-matrix rank-three theorem

The completed source above (`9b8bb7e...`) proves

\[
\operatorname{rank}(A)\ge3
\Longrightarrow
p_{X^TAX}\in C_0(\mathbb R)\cap L^\infty(\mathbb R)
\]

for every collection of independent one-dimensional cap-one densities. Its proof treats nonzero physical diagonal and all-zero-diagonal matrices separately and does not use post-rotation independence.

### 2.2 Product projection cap

The Livshyts--Paouris--Pivovarov marginal theorem was source-pinned in

`yspennstate/math-open-problems@8e91df7441e0ad60997f82c12278b0c669d44344`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B18/20260923T015618Z-qform-B18-a01-r21/REPORT.md`.

For the present cap-one class it gives, in particular, for every two-dimensional orthogonal projection `Y=U^T X` of an original-coordinate product law,

\[
\boxed{\|p_Y\|_\infty\le2.}
\tag{2.1}
\]

No independence of the two projected coordinates is asserted.

### 2.3 Designated partner account04/B15

The completed partner report

`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`

proves the same-constant compiler:

if `rank(A)>=3` and a separate argument has already paid

\[
\Pr\{X^TAX\in I\}\le M|I|
\tag{2.2}
\]

for every interval, then the canonical fixed-instance representative lies in `C_0(R)` and satisfies the identical pointwise bound `||p||_infinity<=M`. I apply this at a concrete target inequality in Section 7.

## 3. A centered-cube projection lower bound in every orientation

The negative/sharpness examples below use the same original-coordinate product law for every matrix orientation:

\[
X=(X_1,\ldots,X_n),\qquad X_i\stackrel{\rm iid}{\sim}\mathrm{Unif}[-1/2,1/2].
\tag{3.1}
\]

Its joint density is `1_C` on the cube `C=[-1/2,1/2]^n`, hence it is an admissible cap-one product law.

Let `U` be an `n x r` matrix with orthonormal columns, `r=1` or `2`, and let

\[
Y=U^T X.
\]

Write `E=Range(U)` and decompose `x=Uy+z`, `z in E^perp`. Orthogonal coarea gives a projection density

\[
\rho_U(y)=\mathcal H^{n-r}\{z\in E^\perp:Uy+z\in C\}.
\tag{3.2}
\]

The cube contains the Euclidean ball `B_n(0,1/2)`. Hence for `|y|<=1/4`, every `z in E^perp` with `|z|<=sqrt(3)/4` satisfies

\[
|Uy+z|^2=|y|^2+|z|^2\le1/4,
\]

and therefore `Uy+z in C`. Consequently

\[
\boxed{
\rho_U(y)\ge c_{n,r}:=
\omega_{n-r}\left({\sqrt3\over4}\right)^{n-r}>0,
\qquad |y|\le1/4,
}
\tag{3.3}
\]

with the convention `omega_0=1`. This includes `n=r`: then the orthogonal image of the cube itself contains `B_r(0,1/2)`, so the density is one there.

The important point is not the dimension-dependent value of `c_{n,r}`. It is that **every spectral orientation has a strictly positive two-sided projected density near the quadratic critical point under one admissible original-coordinate product law**.

## 4. Rank one: absolute continuity does not imply boundedness

Let `A` be any real symmetric rank-one matrix,

\[
A=\lambda uu^T,\qquad |u|=1,\quad \lambda\ne0.
\]

Under (3.1), `Y=u^T X` has density `rho` satisfying (3.3) for `r=1`. The quadratic output is

\[
Q=\lambda Y^2.
\]

Assume first `lambda>0`; reflection handles `lambda<0`. For `0<t<lambda/16`, both roots `+-sqrt(t/lambda)` lie in `[-1/4,1/4]`, and the one-dimensional change of variables gives

\[
p_Q(t)
={\rho(\sqrt{t/\lambda})+\rho(-\sqrt{t/\lambda})
 \over 2\sqrt{\lambda t}}
\ge {c_{n,1}\over\sqrt{\lambda t}}.
\tag{4.1}
\]

Therefore

\[
\boxed{\|p_Q\|_\infty=\infty.}
\tag{4.2}
\]

The law is nevertheless absolutely continuous. This is the exact rank-one obstruction: coarea supplies a density, but a nondegenerate square creates the familiar inverse-square-root critical singularity.

## 5. Rank two, indefinite: logarithmic blow-up in every orientation

Let `A` have rank two and mixed signature. Write

\[
A=U\begin{pmatrix}\lambda&0\\0&-\mu\end{pmatrix}U^T,
\qquad \lambda,\mu>0,
\qquad U^TU=I_2.
\tag{5.1}
\]

For `Y=U^TX`, the density `rho` obeys (3.3) with `r=2`. Put

\[
u=\sqrt\lambda\,y_1,\qquad v=\sqrt\mu\,y_2.
\]

Choose

\[
r_0={1\over4\sqrt{\lambda^{-1}+\mu^{-1}}}>0.
\tag{5.2}
\]

If `|a|,|b|<=r_0` and

\[
u={a+b\over2},\qquad v={b-a\over2},
\]

then `|u|,|v|<=r_0` and hence

\[
|y|^2={u^2\over\lambda}+{v^2\over\mu}
\le r_0^2(\lambda^{-1}+\mu^{-1})={1\over16}.
\]

Thus `rho(y)>=c_{n,2}` throughout the image of that `(a,b)` rectangle. Moreover

\[
Q=u^2-v^2=ab,
\qquad du\,dv={1\over2}\,da\,db,
\qquad dy={du\,dv\over\sqrt{\lambda\mu}}.
\]

For `0<|t|<r_0^2`, the density therefore satisfies

\[
\begin{aligned}
p_Q(t)
&\ge {c_{n,2}\over2\sqrt{\lambda\mu}}
\int_{|a|,|b|\le r_0}\delta(t-ab)\,da\,db\\
&={c_{n,2}\over\sqrt{\lambda\mu}}
\log{r_0^2\over|t|}.
\end{aligned}
\tag{5.3}
\]

Indeed, after integrating in `b`, the admissible `a` satisfy `|t|/r_0<=|a|<=r_0`, and

\[
\int_{|t|/r_0\le|a|\le r_0}{da\over|a|}
=2\log{r_0^2\over|t|}.
\]

Consequently

\[
\boxed{\|p_Q\|_\infty=\infty}
\tag{5.4}
\]

for this single cap-one product law, for **every** rank-two indefinite orientation. The obstruction is logarithmic, exactly as expected for a hyperbolic quadratic critical point.

## 6. Rank two, semidefinite: bounded for all laws, but continuity can fail

Now let `A` have rank two and one sign. After replacing `A` by `-A` if necessary,

\[
A=U\begin{pmatrix}\lambda_1&0\\0&\lambda_2\end{pmatrix}U^T,
\qquad \lambda_1,\lambda_2>0.
\tag{6.1}
\]

### 6.1 Every cap-one product law has a bounded density

For an arbitrary admissible product law, the projected pair `Y=U^TX` has a joint density `rho` with `||rho||_infinity<=2` by (2.1). With `u_i=sqrt(lambda_i)y_i`,

\[
Q=|u|^2,\qquad dy={du\over\sqrt{\lambda_1\lambda_2}}.
\]

The Lebesgue pushforward of `u -> |u|^2` has constant density `pi` on `(0,infinity)` because

\[
|\{u:|u|^2\le t\}|=\pi t.
\]

Therefore, for almost every `t>0`,

\[
\boxed{
 p_Q(t)\le{2\pi\over\sqrt{\lambda_1\lambda_2}},
 \qquad
 \|p_Q\|_\infty\le{2\pi\over\sqrt{\lambda_1\lambda_2}}.
}
\tag{6.2}
\]

So rank-two semidefinite forms are qualitatively different from rank one and rank-two indefinite forms: bounded density is automatic, with a clean orientation-free fixed-matrix constant.

### 6.2 But a continuous representative need not exist

Return to the centered product cube (3.1). Let `lambda_min=min(lambda_1,lambda_2)`. If

\[
0<t<\lambda_{\min}/16,
\]

the ellipse `lambda_1 y_1^2+lambda_2 y_2^2=t` lies inside `|y|<1/4`, so (3.3) gives

\[
p_Q(t)
\ge {c_{n,2}\pi\over\sqrt{\lambda_1\lambda_2}}
=:m_0>0
\quad\text{for a.e. }t\in(0,\lambda_{\min}/16).
\tag{6.3}
\]

On the other hand `p_Q(t)=0` for almost every `t<0`.

Suppose a continuous density representative `p_c` existed. Since it agrees almost everywhere with zero on the negative half-line, continuity forces `p_c(t)=0` for every `t<0` and hence `p_c(0)=0`. Since it agrees almost everywhere with a function bounded below by `m_0` on `(0,lambda_min/16)`, continuity forces `p_c(t)>=m_0` throughout that open interval and hence `p_c(0)>=m_0`. Contradiction.

Thus

\[
\boxed{\text{a rank-two semidefinite quadratic need not have any continuous density representative.}}
\tag{6.4}
\]

This is a strict separation between `L^infinity` and `C_0` regularity at rank two.

## 7. Sharp phase diagram and designated-partner application

Combining Sections 4--6 with the completed rank-at-least-three theorem gives the following exact qualitative phase diagram for cap-one product inputs.

### Theorem 7.1 — `QFORM-B15-SHARP-RANK3-C0-THRESHOLD-v1`

For a fixed real symmetric matrix `A`, consider the property

> `(P_A)`: for **every** family of independent real cap-one input densities, `X^TAX` has a bounded density with a representative in `C_0(R)`.

Then

\[
\boxed{(P_A)\ \text{holds whenever }\operatorname{rank}(A)\ge3,}
\tag{7.1}
\]

and this rank condition is sharp:

- `rank(A)=0`: the output is an atom;
- `rank(A)=1`: the centered cube law gives the inverse-square-root blow-up (4.1);
- `rank(A)=2`, indefinite: the centered cube law gives the logarithmic blow-up (5.3);
- `rank(A)=2`, semidefinite: every cap-one product law has the bounded density estimate (6.2), but the centered cube law gives no continuous representative by (6.3)--(6.4).

Therefore **rank three is exactly the first rank at which boundedness plus continuity is guaranteed for every admissible product law.**

### 7.2 Actual target inequality and account04/B15 application

The rank-two definite estimate also gives a useful target-valid product-bank branch. Split original coordinates into two disjoint independent banks `X` and `W`. Let

\[
Q= X^T B X + W^T C W,
\tag{7.2}
\]

where `B` has rank two, is positive or negative semidefinite on its range, and has nonzero eigenvalue magnitudes `lambda_1,lambda_2`. Assume `C!=0`. The first bank output has density bounded by (6.2). The second bank output is an independent probability law; convolution with a probability measure cannot increase an `L^infinity` norm. Hence

\[
\boxed{
\Pr\{Q\in I\}
\le {2\pi\over\sqrt{|\lambda_1\lambda_2|}}|I|
\quad\text{for every interval }I.
}
\tag{7.3}
\]

If, in addition, `C` has at least one eigenvalue of magnitude at least one and `|lambda_1|,|lambda_2|>=1`, then the block-diagonal full matrix is literally in the owner target and (7.3) gives

\[
\Pr\{Q\in I\}\le2\pi|I|.
\tag{7.4}
\]

Now apply the completed designated partner account04/B15 same-constant theorem (2.2) to this **actual** target interval inequality. Since the full matrix has rank at least three,

\[
\boxed{
 p_Q\in C_0(\mathbb R),\qquad
 \|p_Q\|_\infty
 \le {2\pi\over\sqrt{|\lambda_1\lambda_2|}}
 \le2\pi.
}
\tag{7.5}
\]

This application permits an arbitrarily oriented/diffuse rank-two semidefinite spectral block inside its original-coordinate bank; no independence of spectral coordinates is assumed. The only independence used in (7.3) is the genuine independence of the two disjoint original-coordinate banks.

## 8. Consequence for the owner continuity request

The owner asks separately for a continuous density. The source situation is now precise.

1. **Absolute continuity** is already valid for every nonzero quadratic under any absolutely continuous joint law; it needs neither rank three nor product structure.
2. **Fixed-instance boundedness and continuity** are source-complete for every rank-at-least-three cap-one product instance, by the completed `9b8bb7e...` theorem.
3. **Same-constant continuity after a paid interval bound** is source-complete by account04/B15 r8. Thus if the central universal QFORM height theorem is eventually proved with constant `C`, every target instance automatically has a canonical `C_0` representative with the **same** constant `C`; no second universal modulus is needed.
4. **The rank-three hypothesis in that zero-loss regularity compiler is qualitatively sharp.** Section 6 gives a rank-two semidefinite counterexample to continuity even though a uniform fixed-matrix `L^infinity` bound exists.
5. The remaining owner problem is therefore not qualitative regularity. It is the quantifier reversal from instance-dependent rank-three height bounds to one matrix-, dimension-, and law-uniform constant.

The shared `CLAIMS.json` still labels the full continuous-representative claim OPEN. This report does not edit that protected/consolidated state. It records the source-pinned proof status for the authorized B20/owner consolidator to reconcile.

## 9. Corrections respected

Nothing in the argument uses:

- pointwise law-uniform quadratic oscillatory decay;
- independence after spectral rotation;
- arbitrary-joint rank-three coarea height bounds;
- bounded projection density as a substitute for an indefinite rank-three pushforward;
- worst-fibre conditional density moments;
- fixed support diameter, fixed fragment count, Gaussianity, log-concavity, moments, or connected support;
- a single uniformly good physical minor.

The projection density cap is used only in the valid two-dimensional **definite** rank-two calculation (6.2). The indefinite rank-two lower bound is a direct construction under an original-coordinate product law. No claim about the unrestricted rank-three indefinite height follows from either calculation.

## 10. Exact status and next step

**Proved this run:**

- an arbitrary-orientation centered-cube lower bound (3.3);
- inverse-square-root failure of universal fixed-matrix boundedness at rank one;
- logarithmic failure at every rank-two indefinite orientation;
- orientation-free boundedness `2pi/sqrt(|lambda_1 lambda_2|)` for every rank-two semidefinite form;
- failure of continuous representatives for rank-two semidefinite forms under a concrete cap-one product law;
- consequently, rank three is the exact qualitative threshold for the property that every cap-one product input has a bounded `C_0` quadratic density;
- a target-valid rank-two-semidefinite-bank plus independent third-resource branch with height at most `2pi`, upgraded with the designated partner to `C_0` at the same constant.

**Still open:** the universal height constant for all target matrices with three large eigenvalues.

**Next mathematical step:** use the sharp threshold only as a regularity closure. Do not spend further fleet effort seeking a target-uniform continuity modulus (the previous B15 run ruled that out). The substantive open work remains a product-preserving universal interval estimate in the dense rank-three/higher-rank geometry; after that estimate is paid, continuity costs zero additional constant by the partner compiler.
