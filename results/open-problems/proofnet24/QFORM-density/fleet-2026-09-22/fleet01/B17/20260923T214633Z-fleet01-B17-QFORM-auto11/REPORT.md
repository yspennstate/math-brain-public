SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B17, 2026-09-23T21:46:33Z.
attacking: a full-rank escaped-support exact rotated witness that preserves the 3sqrt(2) lower obstruction, plus a concrete near-kernel fragmentation application of the completed fleet02/B17 theorem.

# QFORM B17 — full-rank escaped-support saturation of the 3sqrt(2) obstruction

Run: `20260923T214633Z-fleet01-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING SHARP-WITNESS THEOREM; FULL QFORM OPEN**  
Continuity: **not claimed for the unrestricted target**.  
Execution context: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. The result below does not increase the known numerical lower obstruction `3sqrt(2)`; it shows that this obstruction survives two reductions that a proposed proof might otherwise try to impose: it persists for exact **full-rank, entrywise-dense** matrices, with all formerly null eigenvalues replaced by nonzero spectrum, and for cap-one inputs whose supports all move to infinity and whose uncentered second moments diverge.

No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea cap, conditional projection-density moment bound, uniformly good physical minor, bounded-diameter/fixed-fragment reduction, or generic two-sheet X-ray shortcut is used.

## 1. Exact four-coordinate dense core

Set

\[
R_0={1\over2}
\begin{pmatrix}
1&1&1\\
1&-1&1\\
1&1&-1\\
1&-1&-1
\end{pmatrix},
\qquad
k_0={1\over2}(1,-1,-1,1)^T.
\tag{1.1}
\]

Then

\[
R_0^TR_0=I_3,\qquad R_0^Tk_0=0,\qquad \|k_0\|_2=1.
\tag{1.2}
\]

Take

\[
n={1\over\sqrt{697}}(7,18,18)^T,
\qquad B_*=I_3-2nn^T
={1\over697}
\begin{pmatrix}
599&-252&-252\\
-252&49&-648\\
-252&-648&49
\end{pmatrix}.
\tag{1.3}
\]

Thus `B_*^2=I_3`, with signature `(2,1)`. The physical four-coordinate compression is

\[
A_*:=R_0B_*R_0^T
={1\over2788}
\begin{pmatrix}
-1607&95&95&1797\\
95&1993&-795&1103\\
95&-795&1993&1103\\
1797&1103&1103&409
\end{pmatrix}.
\tag{1.4}
\]

Every one of its sixteen entries is nonzero. Also `A_*^3=A_*`, `rank(A_*)=3`, `tr A_*=1`, and `tr(A_*^2)=3`, so its nonzero spectrum is exactly

\[
\{1,1,-1\}.
\tag{1.5}
\]

This is already a genuinely rotated/dense finite core rather than a diagonal control.

## 2. Lift to dimension 4m and make the matrix full rank

For `m>=1`, let `W_m` be the `4m x 3` matrix formed by stacking `m` copies of `R_0/sqrt(m)`. Then

\[
W_m^TW_m=I_3.
\tag{2.1}
\]

Let

\[
P_m=W_mW_m^T,\qquad
A_m^{(0)}=W_mB_*W_m^T.
\tag{2.2}
\]

Thus `P_m` is the orthogonal projection onto `ran W_m`, and `A_m^(0)` has spectrum `{1,1,-1,0^(4m-3)}`.

Let `c_m` be the vector obtained by stacking `m` copies of `k_0/sqrt(m)`. Then

\[
\|c_m\|_2=1,\qquad W_m^Tc_m=0,\qquad P_mc_m=0,\qquad A_m^{(0)}c_m=0.
\tag{2.3}
\]

For either sign `sigma in {+1,-1}`, put

\[
\varepsilon_m=m^{-2},\qquad
\widetilde A_m^{\sigma}
=A_m^{(0)}+\sigma\varepsilon_m(I-P_m).
\tag{2.4}
\]

The two summands act on orthogonal invariant subspaces. Therefore

\[
\boxed{
\operatorname{spec}(\widetilde A_m^{\sigma})
=\{1,1,-1,\underbrace{\sigma m^{-2},\ldots,\sigma m^{-2}}_{4m-3}\}.
}
\tag{2.5}
\]

In particular every `\widetilde A_m^sigma` is **full rank** and satisfies the exact target hypothesis with three eigenvalues of magnitude one. The extra spectrum can be chosen entirely positive or entirely negative.

### Entrywise density

The `4 x 4` block of `P_m` is `P_*/m`, where

\[
P_*=R_0R_0^T={1\over4}
\begin{pmatrix}
3&1&1&-1\\
1&3&-1&1\\
1&-1&3&1\\
-1&1&1&3
\end{pmatrix}.
\tag{2.6}
\]

For two distinct physical coordinates, the leading entry of `A_m^(0)` has magnitude at least `95/(2788m)`, while the perturbation in (2.4) has magnitude at most `3/(4m^3)`. For a diagonal physical coordinate, the leading magnitude is at least `409/(2788m)` while the perturbation magnitude is less than `1/m^2`. At `m=7`, and hence for every `m>=7`,

\[
{95\over2788m}>{3\over4m^3},
\qquad
{409\over2788m}>{1\over m^2}.
\tag{2.7}
\]

Hence

\[
\boxed{m\ge7\implies \widetilde A_m^\sigma\text{ is entrywise nonzero for both }\sigma=\pm1.}
\tag{2.8}
\]

So the witness is simultaneously exact-spectrum, full rank and entrywise dense.

## 3. All input supports escape to infinity

Let the physical variables `U_1,...,U_{4m}` be independent `Unif[-1/2,1/2]` and define

\[
X^{(m)}=U+m c_m.
\tag{3.1}
\]

Every `X_i^(m)` still has a probability density exactly bounded by one: it is simply an indicator of a unit interval. But each coordinate of `m c_m` is `+sqrt(m)/2` or `-sqrt(m)/2`. Thus

\[
\operatorname{dist}(\operatorname{supp}X_i^{(m)},0)
\ge {\sqrt m\over2}-{1\over2}\longrightarrow\infty
\tag{3.2}
\]

for **every** physical coordinate. Also

\[
|\mathbb E X_i^{(m)}|={\sqrt m\over2},
\qquad
\mathbb E[(X_i^{(m)})^2]={m\over4}+{1\over12}\longrightarrow\infty.
\tag{3.3}
\]

Thus the sharp lower obstruction cannot be removed by first translating all cap-one laws into a bounded common region, nor by assuming a uniform bound on uncentered second moments. The variances remain `1/12`; no moment assumption is used in the target itself.

## 4. The full-rank tail contributes only a deterministic unit shift plus o(1)

Write `K_m=I-P_m`. From (2.3), `K_mc_m=c_m`. Therefore

\[
\begin{aligned}
\widetilde Q_m^\sigma
&:=(X^{(m)})^T\widetilde A_m^\sigma X^{(m)}\\
&=U^TA_m^{(0)}U
+\sigma\left[
1+{2\over m}c_m^TU+{1\over m^2}U^TK_mU
\right].
\end{aligned}
\tag{4.1}
\]

Since `||c_m||=1`, `||K_m||op=1`, and every coordinate of `U` has magnitude at most `1/2`,

\[
\|U\|_2\le\sqrt m.
\tag{4.2}
\]

Consequently, deterministically,

\[
\boxed{
\left|\widetilde Q_m^\sigma-\sigma-U^TA_m^{(0)}U\right|
\le {2\over\sqrt m}+{1\over m}
=:\delta_m\longrightarrow0.
}
\tag{4.3}
\]

The choice `epsilon_m=m^-2` and support translation of size `m c_m` is the key scale balance: all formerly zero eigenvalues become nonzero, all physical supports escape, yet the added quadratic tail is asymptotically just the fixed output translation `sigma`.

## 5. Gaussian cone limit and the 3sqrt(2) lower obstruction

Partition `U` into its `m` independent four-coordinate blocks `U^(ell)`. Then

\[
Y_m:=W_m^TU={1\over\sqrt m}\sum_{\ell=1}^m R_0^TU^{(\ell)}.
\tag{5.1}
\]

Each summand is centered and has covariance

\[
{1\over12}R_0^TR_0={1\over12}I_3.
\tag{5.2}
\]

The ordinary multivariate CLT therefore gives

\[
Y_m\Rightarrow G\sim N(0,I_3/12).
\tag{5.3}
\]

Moreover

\[
Q_m^{(0)}:=U^TA_m^{(0)}U=Y_m^TB_*Y_m
\Rightarrow Q_G:=G^TB_*G.
\tag{5.4}
\]

Because `G` is isotropic and `B_*` has signature `(2,1)`, `Q_G` has the same law as

\[
G_1^2+G_2^2-G_3^2.
\tag{5.5}
\]

Let `sigma_G^2=1/12`. Then `G_1^2+G_2^2` is exponential with density `(2sigma_G^2)^(-1)e^{-u/(2sigma_G^2)}`, while `G_3^2` has density `(sqrt(2pi)sigma_G sqrt(v))^(-1)e^{-v/(2sigma_G^2)}`. Hence the density of (5.5) is continuous at zero and

\[
\begin{aligned}
p_G(0)
&=\int_0^\infty
{e^{-v/(2\sigma_G^2)}\over2\sigma_G^2}
{e^{-v/(2\sigma_G^2)}\over\sqrt{2\pi}\sigma_G\sqrt v}\,dv\\
&={1\over2\sqrt2\,\sigma_G^2}
=\boxed{3\sqrt2}.
\end{aligned}
\tag{5.6}
\]

### Density existence at each finite m

`\widetilde A_m^sigma` is invertible. Thus the gradient of the quadratic map `x -> x^T\widetilde A_m^sigma x` vanishes only at `x=0`. Since the product input has a Lebesgue density, the coarea formula implies that its pushforward is absolutely continuous; denote a density by `p_m^sigma`. This step asserts **absolute continuity only**. No unrestricted continuity conclusion is being used or claimed.

### Small-ball transfer

Fix `h>0`. For any `eta in (0,h)`, (4.3) gives for all large `m`

\[
\{|Q_m^{(0)}|\le h-\eta\}
\subseteq
\{|\widetilde Q_m^\sigma-\sigma|\le h\}.
\tag{5.7}
\]

Therefore

\[
2h\,\|p_m^\sigma\|_\infty
\ge
\mathbb P(|\widetilde Q_m^\sigma-\sigma|\le h)
\ge
\mathbb P(|Q_m^{(0)}|\le h-\eta).
\tag{5.8}
\]

By (5.4) and continuity of the limiting distribution function,

\[
\liminf_{m\to\infty}\|p_m^\sigma\|_\infty
\ge {\mathbb P(|Q_G|\le h-\eta)\over2h}.
\tag{5.9}
\]

First let `eta downarrow0` and then `h downarrow0`. By (5.6),

\[
\boxed{
\liminf_{m\to\infty}\|p_m^\sigma\|_\infty\ge3\sqrt2,
\qquad \sigma=\pm1.
}
\tag{5.10}
\]

This is the main witness theorem of the run.

### Consequence

Any universal constant for the unrestricted QFORM target must still satisfy

\[
\boxed{C_{\rm univ}\ge3\sqrt2,}
\tag{5.11}
\]

**even if one restricts attention to** exact full-rank, entrywise-dense target matrices with the three large eigenvalues exactly `{1,1,-1}`, with all additional eigenvalues nonzero and of either chosen common sign, and to independent unit-interval input densities whose every support and uncentered second moment escapes to infinity.

This is a structural strengthening of the known lower obstruction, not a proof that `3sqrt(2)` is the unrestricted sharp upper constant. The `liminf` statement deliberately does not claim that the finite density maxima converge to `3sqrt(2)`; a larger finite peak would only strengthen the lower obstruction.

## 6. Actual application of the completed fleet02/B17 theorem

The newest completed designated partner result read and applied in this run is

`yspennstate/math-open-problems@c9a6d151fa7192bfb3bb973de4fd09823e707b55:proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T204259Z-fleet02-B17-QFORM-auto11/REPORT.md`,

`QFORM-DENSE-FRAGMENT-GLOBAL-AGGREGATE-v1`.

Its exact matrix is

\[
T={1\over\sqrt2}
\begin{pmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix},
\qquad
B=I_3-{2\over3}{\bf1}{\bf1}^T,
\qquad
A=T^TBT,
\tag{6.1}
\]

with exact nonzero spectrum `{1,1,-1}`. For finite/countable interval-fragment marginals it proves, writing `Delta=inf{|Tc|:Tc!=0}` over nonkernel product-cell centers,

\[
\Delta\ge84\quad\Longrightarrow\quad
\|p_{X^TAX}\|_\infty<{140\over33}<3\sqrt2.
\tag{6.2}
\]

Here is a concrete source-valid application containing exact remote cancellations. Set `R=120`. In each of the three physical pairs, give the odd coordinate density

\[
1_{[-1/4,1/4]}+1_{[R-1/4,R+1/4]},
\tag{6.3}
\]

and the even coordinate density

\[
1_{[-1/4,1/4]}+1_{[-R-1/4,-R+1/4]}.
\tag{6.4}
\]

Each is a cap-one probability density: two disjoint intervals, each of length `1/2`. For a product cell, each pair-center sum is exactly `0`, `R`, or `-R`; the remote/remote choice cancels exactly. Consequently every coordinate of `Tc` is `0` or `+/-R/sqrt(2)`, and

\[
\boxed{\Delta={R\over\sqrt2}=60\sqrt2>84}
\tag{6.5}
\]

because `7200>84^2=7056`. The partner theorem therefore pays the actual global inequality

\[
\boxed{
\|p_{X^TAX}\|_\infty<{140\over33}<3\sqrt2.
}
\tag{6.6}
\]

The last comparison is exact since

\[
140^2=19600<19602=18\cdot33^2.
\tag{6.7}
\]

Thus large remote fragments with exact kernel cancellations are globally subcritical in this dense Householder architecture. The partner theorem's remaining difficulty is genuinely **near-kernel resonance with bounded nonzero `|Tc|`**, not mere remote support or exact cancellation.

## 7. What this rules out for a prospective sharp proof

The two calculations constrain opposite directions:

1. The new full-rank family shows that a sharp proof cannot discard near-extremizers merely because `A` is invertible, because `A` has many additional nonzero eigenvalues, because all physical entries are nonzero, because supports are far from the origin, or because uncentered second moments are huge. The `3sqrt(2)` obstruction survives all of those properties simultaneously.

2. The partner application shows that remote two-fragment structure by itself is not dangerous in the exact dense six-variable pair-sum architecture when the nonkernel projected centers have a large gap. Exact remote cancellations are absorbed by the kernel aggregate; the dangerous fragmentation regime is bounded nonzero projected-center resonance.

The remaining sharp-witness search should therefore emphasize rough laws with **near-kernel nonzero resonance**, shared/intermediate-leverage structures not reducible to fixed periodic diffuse frames, off-zero modes, or more complicated active spectrum. The full unrestricted theorem and unrestricted continuity remain open.

## 8. Deterministic verification

`CHECK.py` verifies:

- `R_0^TR_0=I`, `R_0^Tk_0=0`, `||k_0||=1`;
- `B_*^2=I` and the exact rational matrices `A_*`, `P_*`;
- the rank/spectrum certification of `A_*` and nonzero physical entries;
- the explicit inequalities certifying entrywise density for `m>=7`;
- the partner application `Delta=60sqrt(2)>84` and `140/33<3sqrt(2)`;
- the Gaussian cone value `p_G(0)=3sqrt(2)`.

The executed output is

`QFORM_B17_FULLRANK_ESCAPED_SUPPORT_CHECK_PASS`.

The checker certifies the finite algebra and constants only; the CLT/coarea/small-ball argument is the analytic proof above.
