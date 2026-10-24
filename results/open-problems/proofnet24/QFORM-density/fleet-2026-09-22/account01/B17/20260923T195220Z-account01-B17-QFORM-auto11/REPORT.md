SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B17, 2026-09-23T19:52:20Z.
attacking: close the minority-sign two-sheet global mode of the connected triangular Householder stress family, then apply account02/B17 finite-fragment domination to a genuine global inequality.

# QFORM B17 — two-sheet closure for the connected triangular Householder witness

Run: `20260923T195220Z-account01-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING ANALYTIC WITNESS CONSTRAINT; FULL QFORM OPEN**  
Continuity: no unrestricted continuity claim.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The full target remains **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a global subcriticality statement for one exact dense six-variable product witness and closes the two-sheet implication explicitly left unpaid by the pinned `account02/B17` partner report. It does not use the refuted generic two-sheet X-ray shortcut, post-rotation independence, or an arbitrary-joint coarea cap.

## 1. Source pins and exact target family

Fresh brain control used owner revision `2026-09-22.15`; QFORM is the sole research target and B17 is not paused. The live correction `QFORM-TWOSHEET-XRAY-ONLY-FALSE` is respected: the proof below uses the special product-triangular density and its permutation/log-concavity structure, not a generic line-X-ray estimate.

Designated partner source consumed in full:

- repository `yspennstate/math-open-problems`
- commit `3d6bfeb739f349e0b01175bf96c773787f6761f4`
- path `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260923T181721Z-account02-B17-QFORM-auto11/REPORT.md`
- checker at the same commit/path, `CHECK.py`.

The partner fixes

\[
n={1\over\sqrt3}(1,1,1)^T,
\qquad
B=I_3-2nn^T={1\over3}
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\]

Take six independent physical variables `X_{j,k} ~ Unif[-1/2,1/2]`, `j=1,2,3`, `k=1,2`, and

\[
S_j={X_{j,1}+X_{j,2}\over\sqrt2},
\qquad Q_*=S^TBS.
\]

Equivalently, if `C` has two rows `e_j/sqrt(2)` in each bank, `A=CBC^T`. Since `C^TC=I_3` and `B^2=I_3`, the physical `6 x 6` matrix has exact nonzero spectrum

\[
\operatorname{spec}_{\ne0}(A)=\{1,1,-1\}.
\]

Every entry of `A` is nonzero because every entry of `B` is nonzero. This is therefore a genuinely coupled dense physical target, not a diagonal control.

Each bank has density

\[
h(x)=\sqrt2\,(1-\sqrt2|x|)_+,
\qquad
\rho(y)=\prod_{j=1}^3h(y_j).
\]

The partner source proves the exact cone-tip value

\[
\boxed{
 p_*(0)=
 -{165\over4}+12\sqrt3+15\sqrt2
 +22\sqrt3\log {\sqrt6+3\sqrt2\over6}
 +\sqrt3\log {1+\sqrt2-1/\sqrt3\over1+\sqrt2+1/\sqrt3}
}
\]

and certifies

\[
p_*(0)=4.06307061680603726012548442259349995675\ldots
<3\sqrt2.
\tag{1.1}
\]

It also proves, by the source-pinned one-sheet identity plus Prékopa/log-concavity,

\[
\boxed{p_*(s)\le p_*(0),\qquad s\ge0.}
\tag{1.2}
\]

Its first explicitly unpaid implication was the minority-sign/two-sheet side `s<0`.

## 2. Exact two-sheet coarea formula

Write every latent point as

\[
y=tn+v,
\qquad v\perp n,
\]

so that

\[
y^TBy=|v|^2-t^2.
\]

Choose a unit circle `e_theta` in `n^perp` and set

\[
F_t(r)=\int_0^{2\pi}\rho(tn+r e_\theta)\,d\theta.
\]

The support cube of `rho` is `[-1/sqrt(2),1/sqrt(2)]^3`, hence `|t|<=T`, where

\[
T=\sqrt{3/2}.
\]

For `a>0`, one-dimensional delta/coarea in the polar radius gives the exact representative

\[
\boxed{
 p_*(-a^2)=\int_a^T F_t\!\left(\sqrt{t^2-a^2}\right)dt,
 \qquad
 p_*(0)=\int_0^T F_t(t)dt.
}
\tag{2.1}
\]

Indeed the radial Jacobian `r dr` cancels the derivative `2r`, and the `t>0` and `t<0` sheets contribute equally because `rho` is even.

We now pay (2.1) in two ranges.

## 3. Near the cone tip: the missing cone segment beats the inward radial shift

The triangular bank density satisfies `0<=h<=sqrt(2)` and `Lip(h)=2`. Therefore

\[
\operatorname{Lip}_{\mathbb R^3}(\rho)\le4\sqrt3,
\]

and for all `r_1,r_2>=0`

\[
|F_t(r_1)-F_t(r_2)|
\le8\pi\sqrt3\,|r_1-r_2|.
\tag{3.1}
\]

Put

\[
r_a(t)=\sqrt{t^2-a^2},
\qquad
I(a)=\int_a^T\bigl(t-r_a(t)\bigr)dt.
\]

For `0<a<=1/10`, split at `2a`. On `[a,2a]`, `t-r_a(t)<=a`; on `[2a,T]`,

\[
r_a(t)\ge{\sqrt3\over2}t,
\]

hence

\[
t-r_a(t)
={a^2\over t+r_a(t)}
\le(4-2\sqrt3){a^2\over t}.
\]

Thus

\[
I(a)\le a^2\left[1+k\log{T\over2a}\right],
\qquad k:=4-2\sqrt3.
\tag{3.2}
\]

By (3.1), the total possible gain caused by moving the retained cone circles inward is at most

\[
D(a):=8\pi\sqrt3\,I(a).
\tag{3.3}
\]

Against this gain, (2.1) deletes the entire interval `0<=t<a`. On the null cone `y=tn+t e_theta`, every coordinate obeys

\[
|y_j|\le t\left({1\over\sqrt3}+\sqrt{2\over3}\right).
\]

Since `(2+sqrt(2))/sqrt(3)<2`, for `t<=1/10`

\[
h(y_j)\ge\sqrt2(1-2t),
\]

and therefore

\[
F_t(t)\ge4\pi\sqrt2(1-2t)^3.
\]

Consequently the deleted mass is at least

\[
E(a):=\int_0^aF_t(t)dt
\ge4\pi\sqrt2\,a(1-2a)^3.
\tag{3.4}
\]

Combining (3.2)--(3.4),

\[
{D(a)\over E(a)}
\le
\sqrt6\,{a[1+k\log(T/(2a))]\over(1-2a)^3}.
\tag{3.5}
\]

The right side is increasing on `(0,1/10]`: the numerator `g(a)=a[1+k log(T/(2a))]` has

\[
g'(a)=1-k+k\log(T/(2a))>0,
\]

while `(1-2a)^3` decreases. At `a=1/10`,

\[
5T=5\sqrt{3/2}<{25\over4}<7<e^2,
\]

so `log(5T)<2`. Therefore

\[
{D(a)\over E(a)}
\le {25\sqrt6\over128}(9-4\sqrt3)
=0.9911806516\ldots<1.
\tag{3.6}
\]

The last strict inequality has an elementary exact certificate: after squaring it is enough to show

\[
467366<270000\sqrt3,
\]

and `sqrt(3)>433/250` gives `270000 sqrt(3)>467640`.

Hence the deleted segment dominates every possible inward-shift gain, and

\[
\boxed{
 p_*(-a^2)<p_*(0),
 \qquad 0<a\le1/10.
}
\tag{3.7}
\]

Equivalently, every negative output level in `[-10^{-2},0)` is strictly below the cone tip.

## 4. Away from the tip: a permutation/log-concavity envelope

For fixed `t`, the function

\[
v\mapsto\rho(tn+v),\qquad v\in n^\perp,
\]

is log-concave. It is invariant under the cyclic coordinate permutation, whose three-point orbit has barycenter zero on `n^perp`. Hence log-concavity gives

\[
\rho(tn+v)\le\rho(tn)
\]

for every `v in n^perp`. Consequently

\[
F_t(r)\le2\pi\rho(tn).
\tag{4.1}
\]

Along the diagonal axis,

\[
\rho(tn)=2\sqrt2\left(1-{t\over T}\right)^3,
\qquad 0\le t\le T.
\]

For `a>=1/10`, equations (2.1) and (4.1) therefore give

\[
\begin{aligned}
p_*(-a^2)
&\le\int_a^T2\pi\rho(tn)dt\\
&=\pi\sqrt3\left(1-{a\over T}\right)^4.
\end{aligned}
\tag{4.2}
\]

Since `sqrt(2/3)>4/5`, `pi<22/7`, and `sqrt(3)<7/4`,

\[
\boxed{
 p_*(-a^2)
 <{11\over2}\left({23\over25}\right)^4
 =3.94016128
 <3\sqrt2,
 \qquad a\ge1/10.
}
\tag{4.3}
\]

Together, (1.1), (1.2), (3.7), and (4.3) close the partner's unpaid two-sheet obstruction:

\[
\boxed{
\|p_*\|_\infty<3\sqrt2.
}
\tag{4.4}
\]

Using the partner's exact value (1.1), the far-negative bound in (4.3) is also below `p_*(0)`, so the explicit coarea representative is globally maximized at the cone tip:

\[
\boxed{
\|p_*\|_\infty=p_*(0)
=4.0630706168060372601\ldots<3\sqrt2.
}
\tag{4.5}
\]

For this explicit compact piecewise-linear source, the equality in essential supremum is also compatible with the one-sided coarea formulas by dominated convergence. No unrestricted continuity statement is inferred from this special case.

## 5. Actual application of the completed account02/B17 finite-fragment theorem

The pinned partner theorem proves that every fixed finite interval-fragmentation plan in this six-variable architecture admits, for sufficiently large remote scale `R`,

\[
\boxed{
\|p_R\|_\infty
\le\|p_*\|_\infty+{C_{\mathcal F}\over R},
\qquad
C_{\mathcal F}=4\sqrt6\sum_{d\in D}{1\over\|d\|}<\infty,
}
\tag{5.1}
\]

where `D` is the finite multiset of nonzero bank-center vectors. Before this run the useful implication of (5.1) was blocked by the unclosed two-sheet norm of `p_*`. Substituting (4.5) now gives the actual global inequality

\[
\boxed{
\|p_R\|_\infty
\le
4.0630706168060372601\ldots+{C_{\mathcal F}\over R}.
}
\tag{5.2}
\]

In particular every fixed finite fragmentation plan in the partner's scope is eventually strictly below the diffuse candidate level:

\[
R>{C_{\mathcal F}\over 3\sqrt2-p_*(0)}
\quad\Longrightarrow\quad
\|p_R\|_\infty<3\sqrt2,
\tag{5.3}
\]

with

\[
3\sqrt2-p_*(0)
=0.1795700703132478862\ldots.
\]

For the partner's explicit irrational null direction

\[
d_0=(1,1,4-3\sqrt2),
\qquad q(d_0)=0,
\qquad \|d_0\|^2=12(\sqrt2-1)^2,
\]

the single-cell coefficient is

\[
{4\sqrt6\over\|d_0\|}=4+2\sqrt2.
\]

At the level of the corresponding term in (5.2), `R=39` gives

\[
p_*(0)+{4+2\sqrt2\over39}
=4.2381584917995293\ldots
<3\sqrt2=4.2426406871192851\ldots.
\tag{5.4}
\]

The point of (5.2)--(5.4) is the partner-result application itself: fixed finite remote fragmentation, including exact irrational null-cone tuning, cannot produce a new `3sqrt(2)`-level global mode once the connected two-sheet profile is paid.

## 6. Sharp-constant consequence and remaining witness frontier

This theorem does **not** raise the strongest source-valid lower obstruction. That remains

\[
\boxed{C_{\rm univ}\ge3\sqrt2}
\]

from the diffuse exact-spectrum `{1,1,-1}` product-cube frames already recorded in the programme state.

What is newly excluded is a concrete finite architecture: the dense six-variable connected Householder triangular-bank witness is globally below `3sqrt(2)`, and every fixed finite remote fragmentation in the pinned partner class approaches it with only `O(1/R)` global-density error. Therefore a witness challenging `3sqrt(2)` must use a mechanism outside this paid class, such as fragment count growing with scale, center vectors tending to zero at an `R`-dependent rate, more general rough cap-one laws, genuinely different intermediate-leverage/shared-coordinate geometry, or additional active spectrum.

This is a sharp-witness constraint, not a proof that `3sqrt(2)` is the unrestricted optimal universal constant.

## 7. Verification

`CHECK.py` verifies the Householder algebra, the exact small-side comparison constant, the rational far-negative envelope, the pinned exact `p_*(0)` formula, the null direction `d_0`, its fragment coefficient, and the concrete `R=39` comparison. Saved output begins

`PASS QFORM_B17_HOUSEHOLDER_TWOSHEET_GLOBAL_CLOSURE`.

No schedule, task, notification, email, permission, visibility, or cross-account authentication state is changed by this mathematical run.
