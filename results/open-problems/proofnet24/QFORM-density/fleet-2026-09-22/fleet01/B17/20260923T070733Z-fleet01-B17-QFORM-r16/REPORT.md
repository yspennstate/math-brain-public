SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T07:07:37Z.
attacking: the full 3D equal-magnitude rotation orbit for centered unit-cube inputs via a spectral-ball majorant, with an exact null-pair control and the completed fleet02/B17 finite-bank theorem applied to a joint witness-exclusion inequality.

# QFORM-CENTERED-BOX-EQUALMAG-ROTATION-NOESCAPE-v1

Run: `20260923T070733Z-fleet01-B17-QFORM-r16`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **new supporting sharp-witness theorem; full QFORM OPEN / NOT PROVED**.  
Full-target continuity remains separate. This report proves bounded densities only in the stated branch and does not promote the candidate constant `3sqrt(2)` to a full theorem.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

## 1. Theorem: every 3D equal-magnitude rotation of a centered product box lies strictly below `3sqrt(2)`

Let `L_1,L_2,L_3>=1`, and let

\[
X_i\sim {\rm Unif}[-L_i/2,L_i/2]
\]

be independent. Their physical densities are `1/L_i<=1`. Let `O in O(3)`, put

\[
J={\rm diag}(1,1,-1),\qquad A=\lambda O^TJO,
\]

where `|lambda|>=1`, and define `Q=X^TAX`. Then `A` has exact spectrum

\[
\{\lambda,\lambda,-\lambda\}
\]

(up to the obvious sign reversal when `lambda<0`) and hence is an exact source-valid target matrix. I prove

\[
\boxed{
\|p_Q\|_\infty
\le {\pi\over \sqrt2|\lambda|}
{\sqrt{L_1^2+L_2^2+L_3^2}\over L_1L_2L_3}
\le {\pi\sqrt{3/2}\over |\lambda|}
<3\sqrt2 .
}
\tag{1.1}
\]

For the unit cube and `|lambda|=1`, the uniform orientation-independent ceiling is

\[
C_{\rm cube}=\pi\sqrt{3/2}=3.847649490485592\ldots,
\]

leaving the explicit gap

\[
3\sqrt2-C_{\rm cube}=0.394991196633694\ldots .
\]

Thus **no fixed three-dimensional orthogonal rotation of the common-magnitude signature `(1,1,-1)` can realize the known `3sqrt(2)` lower obstruction when the original independent laws are centered intervals**. The obstruction is genuinely higher-dimensional/diffuse in the presently known construction.

## 2. Product-safe proof by ball domination

Set `Y=OX`. I use the rotation only to describe the pushforward measure; I do **not** assert that the coordinates of `Y` are independent. The joint law of `Y` has density

\[
m\,1_K(y),\qquad m=(L_1L_2L_3)^{-1},
\]

where `K` is an orthogonal image of the centered physical box. Since orthogonal maps preserve Euclidean radius,

\[
K\subset B_R(0),\qquad
R={1\over2}\sqrt{L_1^2+L_2^2+L_3^2}.
\tag{2.1}
\]

Let

\[
S(y)=y_1^2+y_2^2-y_3^2.
\]

For every Borel set `E`, positivity gives the exact measure domination

\[
\Pr(S(Y)\in E)
=m\,|K\cap S^{-1}(E)|
\le m\,|B_R\cap S^{-1}(E)|.
\tag{2.2}
\]

It therefore suffices to compute the pushforward of Lebesgue measure on the Euclidean ball under `S`.

Write `rho^2=y_1^2+y_2^2` and `z=y_3`. Cylindrical coordinates and the delta identity give

\[
H_R(t)
=2\pi\int\int_{\rho^2+z^2\le R^2}
\rho\,\delta(t-(\rho^2-z^2))\,d\rho\,dz.
\tag{2.3}
\]

For fixed `z`, integration in `rho` contributes exactly `pi` when

\[
\rho^2=t+z^2\ge0,
\qquad
 t+2z^2\le R^2,
\]

and contributes zero otherwise. Hence

\[
H_R(t)=
\begin{cases}
\pi\sqrt{2(R^2-t)},&0\le t\le R^2,\\[2mm]
2\pi\left(\sqrt{(R^2+s)/2}-\sqrt{s}\right),&t=-s,\ 0\le s\le R^2,\\[2mm]
0,&|t|>R^2.
\end{cases}
\tag{2.4}
\]

The positive branch is decreasing in `t`. On the negative branch,

\[
{d\over ds}H_R(-s)
=\pi\left({1\over\sqrt{2(R^2+s)}}-{1\over\sqrt{s}}\right)<0
\qquad(s>0).
\tag{2.5}
\]

Therefore the ball pushforward is maximized at the cone level `t=0`, with

\[
\boxed{\|H_R\|_\infty=H_R(0)=\pi\sqrt2\,R.}
\tag{2.6}
\]

By (2.2), the pushforward of the rotated box is absolutely continuous and its density is bounded a.e. by `mH_R`. Scaling by `lambda` yields

\[
\|p_Q\|_\infty
\le {|\lambda|}^{-1}m\pi\sqrt2R
={\pi\over\sqrt2|\lambda|}
{\sqrt{L_1^2+L_2^2+L_3^2}\over L_1L_2L_3}.
\tag{2.7}
\]

Finally,

\[
{L_1^2+L_2^2+L_3^2\over L_1^2L_2^2L_3^2}
={1\over L_2^2L_3^2}+{1\over L_1^2L_3^2}+{1\over L_1^2L_2^2}
\le3,
\]

which proves the second inequality in (1.1). The strict comparison with `3sqrt(2)` is equivalent to `pi^2<12`; the elementary bound `pi<22/7` reduces this to `484<588`.

This proof is immune to the live arbitrary-joint-coarea correction: no bound is asserted for arbitrary joint densities. It uses the exact indicator-box provenance and a pointwise measure majorant by a ball. It also uses no post-rotation independence, no conditional-density moment, and no law-uniform pointwise oscillatory decay.

## 3. Higher-dimensional block-diagonal extension

Let `R_out` be **any** quadratic form of additional independent physical coordinates, with arbitrary symmetric coefficient matrix and arbitrary independent cap-one input laws. If there are no cross terms between the above three-coordinate core and the outside coordinates, then

\[
Q_{\rm total}=Q_{\rm core}+R_{\rm out}
\]

is a sum of independent random variables. Hence

\[
p_{Q_{\rm total}}=p_{Q_{\rm core}}*\mu_{R_{\rm out}},
\qquad
\|p_{Q_{\rm total}}\|_\infty\le\|p_{Q_{\rm core}}\|_\infty.
\tag{3.1}
\]

Thus (1.1) survives arbitrary-dimensional, arbitrary-spectrum **block-diagonal** tails. Cross-coupled tails are not covered by this argument.

## 4. Exact rotated null-pair control inside the orbit

A useful explicit orientation in the same common-magnitude orbit is

\[
A_0=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},
\qquad
Q_0=2X_1X_3+X_2^2,
\tag{4.1}
\]

whose eigenvalues are exactly `{1,1,-1}`. For iid `X_i~Unif[-1/2,1/2]`, the density of `W=2X_1X_3` is

\[
f_W(w)=-\log(2|w|),\qquad0<|w|<1/2,
\]

and the density of `U=X_2^2` is `u^{-1/2}` on `(0,1/4)`. Therefore

\[
p_{Q_0}(t)=
\int_{\max(0,t-1/2)}^{\min(1/4,t+1/2)}
{ -\log(2|t-u|)\over\sqrt u}\,du.
\tag{4.2}
\]

At zero,

\[
p_{Q_0}(0)
=-2\int_0^{1/2}\log(2v^2)\,dv
=2+\log2.
\tag{4.3}
\]

This is the global mode. For `t<0`, differentiation (including the moving endpoint when present, whose kernel vanishes there) gives `p'(t)>0`; for `t>1/4`, it gives `p'(t)<0`. For `0<t<1/4`, the principal-value derivative is

\[
p'(t)
=-{1\over\sqrt t}
\log {1/2+\sqrt t\over1/2-\sqrt t}<0.
\tag{4.4}
\]

Consequently

\[
\boxed{\|p_{Q_0}\|_\infty=2+\log2=2.693147180559945\ldots.}
\tag{4.5}
\]

This is an exact non-diagonal stress calculation, not a diagonal/`pi` control.

## 5. Source-valid lower obstruction and what the new theorem says about it

The live correction event `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH` pins the analytic target-level lower obstruction `C_univ>=3sqrt(2)` to `yspennstate/math-open-problems@8624982153e5a2154e4ae8922d2fe4dc77080efc`. It also records the finite six-uniform witness `p_Q(0)=2pi-7/3>pi`. The full existence conjecture remains open.

Combining that source-valid lower obstruction with (1.1) gives a structural constraint on any sharpness proof: **the known `3sqrt(2)` scale cannot be generated by a fixed three-coordinate centered product box under an arbitrary equal-magnitude orthogonal rotation.** In this branch there is a uniform gap of at least

\[
3\sqrt2-\pi\sqrt{3/2}=0.3949911966\ldots .
\]

Thus a sequence saturating the current lower obstruction must use a genuinely different mechanism: increasing-dimensional/diffuse aggregation, non-box fragmentation, unequal spectral magnitudes, cross-coupled tails, or another noncompact/multiscale geometry.

## 6. Designated partner theorem applied to an actual inequality

The latest **completed** `fleet02/B17` theorem available before publication is

`QFORM-ONE-HEAVY-MAJORITY-ALL-FINITE-BANKS-NOESCAPE-v1`,

canonical source
`yspennstate/math-open-problems@596288dcf1a153d7ba008dc6fc7d3097d340f37c`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T045156Z-fleet02-B17-QFORM-auto11/REPORT.md`.

It proves for every finite `m` and every cap-one singleton law in the exact family

\[
A_m={\rm diag}(1,J_m/m,-J_m/m)
\]

that

\[
\|p_{Q_m}\|_\infty
\le C_{\rm bank}
={\pi\sqrt2\over3}\left(1+{4\over\sqrt5}\right)
=4.130184516931749\ldots<3\sqrt2.
\tag{6.1}
\]

Apply (6.1) together with the new theorem to the actual union `C_box union C_bank` of the two exact source-valid stress classes (and, by convolution, to their independent block-diagonal tail extensions). Then

\[
\boxed{
\sup_{Q\in\mathcal C_{\rm box}\cup\mathcal C_{\rm bank}}
\|p_Q\|_\infty
\le
\max\left\{
\pi\sqrt{3/2},
{\pi\sqrt2\over3}\left(1+{4\over\sqrt5}\right)
\right\}
=C_{\rm bank}
<3\sqrt2.
}
\tag{6.2}
\]

This is an inequality-level application of the completed partner result, not merely a citation. Its strict comparison has the partner's exact certificate: with `pi<22/7`, it reduces to `88<41sqrt(5)`, and squaring gives `7744<8405`.

## 7. Corrections consumed, scope, and next step

Immediately before publication I re-read the fresh live correction inbox and the latest owner continuation; no later B17 stop was present. The argument deliberately does not use the refuted arbitrary-joint coarea lemma, positive conditional-density-moment interface, post-rotation independence, fixed fragment-count localization, or uniform pointwise oscillatory decay.

**What is proved:** a global density ceiling `<3sqrt(2)` for the full 3D common-magnitude orthogonal rotation orbit under centered product-uniform box laws, with arbitrary block-diagonal independent tails; plus the exact null-pair mode; plus the joint witness exclusion (6.2) using the completed designated partner theorem.

**What is not proved:** the unrestricted QFORM theorem; sharpness of `3sqrt(2)` for arbitrary A and arbitrary cap-one laws; any reduction of arbitrary laws to centered boxes; or the full continuity statement.

The next B17 witness search should therefore leave both paid mechanisms and attack **two or more genuinely non-collinear macroscopic rows with arbitrary fragmented cap-one laws and shared-coordinate coupling**, or an unequal-magnitude/multiscale configuration that cannot be dominated by the centered-box ball argument or reduced to the one-heavy-bank theorem.

## 8. Deterministic checks

`check_cube_rotation.py` verifies the constants, the elementary strict certificates, and a dense-grid sanity check of the exact analytic ball-density maximum. Saved output:

`C_cube=3.847649490485592`  
`C_partner=4.130184516931749`  
`C_null=2.693147180559945`  
`3sqrt2=4.242640687119286`  
`QFORM_B17_CENTERED_BOX_ROTATION_CHECK_PASS`.

The grid check is only a sanity check; the theorem uses the analytic monotonicity proof in (2.4)-(2.6).
