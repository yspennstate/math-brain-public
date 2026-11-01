# QFORM B17 — unequal opposite cube banks have a global sharp-constant barrier

Run: `20260923T195641Z-fleet02-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: **NEW SUPPORTING ANALYTIC WITNESS-EXCLUSION; FULL QFORM OPEN**  
Continuity: not claimed as a full-target statement.

## 1. New theorem

Let `m,n>=1`, let `a in R^m`, `b in R^n` satisfy

\[
\|a\|_2=\|b\|_2=1,
\]

and let

\[
U_1,\dots,U_m,V_1,\dots,V_n
\]

be independent `Unif[-1/2,1/2]` variables.  Let `X` be an additional independent real random variable with an **arbitrary** probability density `f` satisfying `0<=f<=1`; no moment, support, connectedness or log-concavity assumption is imposed on `f`.  Set

\[
S=a\cdot U,\qquad T=b\cdot V,
\qquad Q=X^2+S^2-T^2.
\]

Equivalently, in the original physical coordinates,

\[
A_{a,b}=\operatorname{diag}(1,aa^T,-bb^T).
\]

Then

\[
\boxed{\operatorname{spec}_{\ne0}(A_{a,b})=\{1,1,-1\}}
\]

for every finite `m,n` and every two, **not necessarily equal**, leverage profiles `a,b`.

The full output law has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le K_{4/5}
:=2\sqrt2\,\arcsin(4/5)
 +\sqrt5\bigl(\pi/2-\arcsin(4/5)\bigr)
=4.061699170101463\ldots
<3\sqrt2.
}
\tag{1.1}
\]

Thus the identical-opposite-bank symmetry used in the earlier B17 theorem is unnecessary: **arbitrary redistribution of leverage in the positive and negative cube banks, independently of one another, still cannot produce a witness at the candidate sharp constant, even when the singleton law is an arbitrary cap-one density and even when the maximizing output level is allowed to move away from the cone tip.**

This is a scoped source-valid witness exclusion, not a proof of unrestricted QFORM.

## 2. Source validity and bank estimates

The spectrum claim is immediate.  `aa^T` has eigenvalues `1,0,...,0`, while `-bb^T` has eigenvalues `-1,0,...,0`; the singleton block contributes `1`.  Hence the physical matrix itself has exactly the three required nonzero eigenvalues, with no spectral post-rotation used to create independence.

Let `h` and `k` denote the densities of `S` and `T`.  Each is a convolution of centered interval densities, hence is even and log-concave and therefore nonincreasing on `[0,infinity)`.

The Ball/Rogozin cube-projection input used in the pinned Claude `RESULTS.md` gives

\[
\boxed{\|h\|_\infty,\|k\|_\infty\le\sqrt2.}
\tag{2.1}
\]

A second application to the actual doubled cube gives the useful `L^2` estimate.  If `S'` is an independent copy of `S`, then

\[
{S-S'\over\sqrt2}
={1\over\sqrt2}(a,-a)\cdot(U,U')
\]

is a unit-norm cube projection.  Therefore its density at zero is at most `sqrt(2)`, and scaling back yields

\[
\boxed{
\|h\|_2^2=p_{S-S'}(0)\le1.
}
\tag{2.2}
\]

The same argument gives `||k||_2^2<=1`.  These bounds use the original independent unit-height interval sources; they do not assume that a spectral rotation preserves independence.

## 3. A one-dimensional three-factor rearrangement lemma

We need one elementary lemma that replaces the old equality of the two banks.

**Lemma.** Let `F_1,F_2` be nonnegative symmetric nonincreasing functions on `R`.  Let `0<=g<=1` and `int g=1`.  Then for all real shifts `c_1,c_2`,

\[
\boxed{
\int_{\mathbb R}g(x)F_1(x-c_1)F_2(x-c_2)\,dx
\le
\int_{-1/2}^{1/2}F_1(x)F_2(x)\,dx.
}
\tag{3.1}
\]

**Proof.** Use layer cake for all three factors.  For a level `0<t<1`, the set `E_t={g>t}` has finite measure `m_t`.  Every positive superlevel set of each `F_j` is a centered interval.  At fixed three levels, the intersection of `E_t` and two arbitrarily translated intervals has length at most the minimum of their three lengths.  If all three sets are centered intervals, that minimum is attained.  After integrating the two `F_j` levels, this is the usual one-dimensional symmetric rearrangement inequality.  The remaining rearranged `g` is symmetric decreasing, bounded by one, and has mass one, so the bathtub principle places its mass on `[-1/2,1/2]`.  This proves (3.1).  No regularity or attainment assumption for the original `g` is needed.  `square`

## 4. Positive levels: apply the pinned ruled-surface theorem

This is where the required pinned result is used at a real inequality.  The completed Theorem C in

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`

proves the exact ruling parametrisation of the one-sheet level sets for the `(1,1,-1)` form.  We use its **identity**, not merely its generic `pi sqrt(2)` bound.

For `R>0`, parameterise `x^2+s^2-t^2=R^2` by

\[
(x,s,t)=
\bigl(R\cos\theta-u\sin\theta,
R\sin\theta+u\cos\theta,
 u\bigr).
\tag{4.1}
\]

The exact coarea element is

\[
\delta(x^2+s^2-t^2-R^2)\,dx\,ds\,dt
={1\over2}\,d\theta\,du.
\tag{4.2}
\]

Hence, for a.e. positive output level,

\[
p_Q(R^2)
={1\over2}\int_0^{2\pi}L_{R,\theta}(f)\,d\theta,
\tag{4.3}
\]

where

\[
L_{R,\theta}(f)
=\int_{\mathbb R}
 f(Rc-us)\,h(Rs+uc)\,k(u)\,du,
\quad c=\cos\theta,\ s=\sin\theta.
\tag{4.4}
\]

For `s c !=0`, change variable `x=Rc-us`.  Then

\[
L_{R,\theta}(f)
={1\over|s|}\int f(x)
 h\!\left({R\over s}-{c\over s}x\right)
 k\!\left({Rc-x\over s}\right)dx.
\tag{4.5}
\]

Because `h,k` are even nonincreasing, the last two factors are symmetric decreasing functions of `x` centered respectively at

\[
{R\over c},\qquad Rc.
\]

Apply Lemma (3.1), absorbing the scale factors `|c/s|` and `1/|s|` into `F_1,F_2`.  The two centers align at zero when `R=0`, so

\[
\boxed{
L_{R,\theta}(f)
\le L_{0,\theta}(\mathbf1_{[-1/2,1/2]})
}
\tag{4.6}
\]

for a.e. `theta`.  The exceptional angles have measure zero.  Integrating (4.6) in the exact ruling identity gives

\[
\boxed{
p_Q(R^2)\le C(a,b),\qquad R>0,
}
\tag{4.7}
\]

where

\[
C(a,b):=p_{U_0^2+S^2-T^2}(0),
\qquad U_0\sim\mathrm{Unif}[-1/2,1/2].
\tag{4.8}
\]

This is strictly stronger for this architecture than applying Theorem C's generic line-marginal cap directly, which would only give `pi sqrt(2)>3sqrt(2)`.  That generic constant failing to reach the candidate sharp value is a proof-constant limitation, not a counterexample.

## 5. Negative levels are also dominated by the same cone tip

Let the output level be `-r`, `r>0`.  Resolve the two roots in the negative bank variable `T`.  Since `k` is even,

\[
p_Q(-r)
=\int_{\mathbb R^2}
f(x)h(s)
 {k(\sqrt{r+x^2+s^2})\over\sqrt{r+x^2+s^2}}
\,dx\,ds.
\tag{5.1}
\]

The function `z -> k(z)/z` is nonincreasing on `(0,infinity)`.  Therefore, for every fixed `s`, the kernel in `x` is even nonincreasing in `|x|`; the bathtub principle gives

\[
\int f(x){k(\sqrt{r+x^2+s^2})\over\sqrt{r+x^2+s^2}}dx
\le
\int_{-1/2}^{1/2}{k(\sqrt{r+x^2+s^2})\over\sqrt{r+x^2+s^2}}dx.
\]

The right side is also pointwise nonincreasing in `r`.  Hence

\[
\boxed{
p_Q(-r)\le C(a,b),\qquad r>0.
}
\tag{5.2}
\]

Combining (4.7) and (5.2), the **entire real line** is controlled by the centered cone-tip integral.  This is the new global step that was unavailable from identical-bank symmetry once `a` and `b` were allowed to differ.

## 6. Universal cone estimate and a certified constant below `3 sqrt(2)`

Writing out (4.8),

\[
C(a,b)
=\int_{|x|\le1/2}\int_{\mathbb R}
 h(s){k(\sqrt{x^2+s^2})\over\sqrt{x^2+s^2}}\,ds\,dx.
\tag{6.1}
\]

Enlarge the `x` strip to all of `R` and use polar coordinates.  With

\[
I(u)=\int_0^\infty k(r)h(ur)\,dr,
\]

we get

\[
C(a,b)
\le4\int_0^1{I(u)\over\sqrt{1-u^2}}\,du.
\tag{6.2}
\]

The `L^infinity` and `L^2` estimates from Section 2 give, for every `u>0`,

\[
I(u)
\le \|h\|_\infty\int_0^\infty k(r)dr
\le {1\over\sqrt2},
\tag{6.3}
\]

and, by Cauchy--Schwarz on the half-line,

\[
I(u)
\le
\left(\int_0^\infty k^2\right)^{1/2}
\left(\int_0^\infty h(ur)^2dr\right)^{1/2}
\le {1\over2\sqrt u}.
\tag{6.4}
\]

For any `0<c<1`, use (6.3) on `[0,c]` and (6.4), together with `u^{-1/2}<=c^{-1/2}`, on `[c,1]`.  This yields the family

\[
C(a,b)
\le K(c)
:=2\sqrt2\,\arcsin c
+{2\over\sqrt c}\left({\pi\over2}-\arcsin c\right).
\tag{6.5}
\]

Taking `c=4/5` gives (1.1).  The comparison with `3sqrt(2)` can be made without trusting decimal arithmetic.  Put `alpha=arcsin(4/5)`.  Since `sin 1>1-1/6=5/6>4/5`, we have `alpha<1`.  Also

\[
\sqrt5<{161\over72},\qquad
\sqrt2<{99\over70},\qquad
\sqrt5>{223\over100},\qquad
\pi<{22\over7}.
\]

Thus

\[
2\sqrt2-\sqrt5<{3\over5},
\]

and therefore

\[
K_{4/5}
={\sqrt5\pi\over2}+(2\sqrt2-\sqrt5)\alpha
<{1771\over504}+{3\over5}
={10367\over2520}
<{140\over33}
<3\sqrt2.
\tag{6.6}
\]

The last inequality uses `(140/99)^2<2`.  The deterministic checker records the actual value `4.061699170101463...` and the exact rational comparison.

## 7. Latest partner result consumed: a sharper finite remote-cell threshold

The latest compatible `fleet03/B17` report is

`math-open-problems@0b4294a426049e36163b091b0900a585565099fc:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B17/20260923T190352Z-fleet03-B17-QFORM-auto11/REPORT.md`.

For its exact dense Householder irrational-null fragmentation family it proves, uniformly in fragment mass `eta`,

\[
p_{Q_R}(0)
\le (1-\eta)^4p_*+{252\sqrt6\over R},
\qquad p_*<{508\over125}.
\tag{7.1}
\]

Applying that completed result to a concrete finite-separation inequality and using

\[
\sqrt6<{49\over20}
\quad\text{because}\quad (49/20)^2=6+1/400,
\]

we improve its convenient rational threshold `R>=3600` to

\[
\boxed{R\ge3461.}
\tag{7.2}
\]

Indeed, at `R=3461`,

\[
{508\over125}+{252\over3461}{49\over20}
={1835363\over432625}
<{140\over33},
\]

with exact margin

\[
{140\over33}-{1835363\over432625}
={521\over14276625}>0.
\]

Thus the partner's exact irrational null-ray attack is already strictly below `3sqrt(2)` by `R=3461`.  This is a small quantitative corollary; the main theorem of this run is the new unequal-bank global barrier above.

## 8. What this rules out, and what it does not

This run closes the previously unpaid **unequal opposite rank-one bank** extension of the one-heavy witness family.  It permits:

- arbitrary finite bank sizes `m,n`;
- arbitrary and unrelated unit leverage vectors `a,b`;
- an arbitrary independent singleton density `f<=1`, including unbounded and fragmented support;
- the true global maximizing output level on either sign.

It still fixes the two diffuse banks to centered unit-interval physical sources and fixes the exact disjoint rank-one bank architecture.  It does **not** cover several non-collinear intermediate-leverage rows, coupled/shared-coordinate banks, arbitrary rough laws in every bank coordinate, extra active spectrum, or the unrestricted matrix problem.  A future peak above `3sqrt(2)` in one of those unpaid classes would refute the proposed sharp constant but would not, by itself, refute existence of a larger universal QFORM bound.

No pointwise law-uniform oscillatory decay, no arbitrary-joint three-dimensional coarea cap, no post-rotation independence, no conditional-density moment, no bounded-fragment extremality, and no hidden support or moment hypothesis is used.  Full QFORM and the full-target continuity question remain **OPEN**.

## 9. Source pins

Required source read and actually used:

- `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`: Ball/Rogozin cube-projection input underlying the completed `L^p` lemma.
- same commit, `COUNTEREXAMPLE_SEARCH.md`, completed Theorem C: exact ruled one-sheet parametrisation/coarea identity used in (4.1)--(4.6).
- same commit, `FOURIER_ROUTE_REPORT.md`: correction-compatible scope; its generic absolute Fourier constants are not misused as sharp constants.

Latest partner result actually applied is the fleet03/B17 report cited in Section 7.

Checker files in this immutable run directory: `CHECK.py`, `CHECK_OUTPUT.txt`.
