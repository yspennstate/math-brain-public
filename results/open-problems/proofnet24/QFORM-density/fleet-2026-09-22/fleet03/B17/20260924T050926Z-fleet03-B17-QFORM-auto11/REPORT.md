SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B17, 2026-09-24T05:09:26.837764Z.
attacking: the first unpaid global off-tip implication in the one-heavy/shared-diffuse N3 mechanism — prove that the minority-axis boundary has no hidden negative two-sheet spike, identify the exact fragmented optimizer at every output level, and compare it to fleet04/B17's newest dense fragmented witness.

# QFORM B17 — global off-tip rigidity at the minority-axis one-heavy boundary

Run: `20260924T050926Z-fleet03-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **PROVED SUPPORTING GLOBAL STRESS-FAMILY THEOREM; FULL QFORM OPEN / NOT PROVED / NOT DISPROVED.**  
Continuity: proved in the theorem below under its stated bounded-continuous positive-core hypothesis, and for the exact finite bank family for `m>=2`; full-target continuity remains open.  
Execution memory: `WITHOUT_VERIFIED_BRAIN`.

## 1. Why this is the next missing implication

The completed one-heavy coupled N3 work proves a strict `3 sqrt(2)` gap at the cone tip for

`Q_a=-aX^2+2sqrt(1-a^2)XB+aB^2+C^2`, `0<a<=1`,

with `X` an arbitrary cap-one law and `(B,C)` the minimum-variance Gaussian diffuse complement.  What it does **not** prove is a global-in-output bound in the coupled interior: an off-zero negative two-sheet peak could in principle be larger than the cone-tip value.

This report attacks that global question at the minority-axis boundary `a=1` and, more generally, isolates the exact one-dimensional mechanism that makes the boundary globally rigid.  The result is not a diagonal-`pi` restatement: it optimizes over **all** cap-one heavy laws at **every** output level, explicitly allows the levelwise optimizer to become disconnected, and applies verbatim to nontrivial positive bank cores.  It therefore tests the precise off-tip/fragmentation obstruction that survives the cone-tip analysis.

No law-uniform pointwise van-der-Corput estimate, post-rotation independence, arbitrary-joint coarea theorem, conditional projection-density moment, bounded fragment-count assumption, or histogram is used.

## 2. Monotone positive core minus one square: exact global bathtub theorem

### Theorem `QFORM-MONOTONE-CORE-MINUS-SQUARE-GLOBAL-v1`

Let `S>=0` be independent of a real random variable `X`.  Assume that `S` has a probability density `h` on `[0,infinity)` that is nonincreasing.  Let `lambda>0`, and assume only

`0<=f_X<=1`, `integral f_X=1`.

Put

`Q=S-lambda X^2`.

Then `Q` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le M_\lambda(h):=
\int_{-1/2}^{1/2}h(\lambda x^2)\,dx
=2\int_0^{1/2}h(\lambda x^2)\,dx .
}
\tag{2.1}
\]

The bound is sharp over the class of cap-one laws for `X`: equality is attained at output level `q=0` by

`f_X=1_{[-1/2,1/2]}`.

More precisely, for every fixed output level the exact bathtub optimizer can be described.

* If `q>=0`, one may take the centered interval `[-1/2,1/2]`.
* If `q=-lambda r^2<0`, `r>0`, one may take the **disconnected two-interval set**

\[
E_r=[r,r+1/2]\cup[-r-1/2,-r].
\tag{2.2}
\]

Thus negative-level coordinatewise extremizers are generally fragmented even though the global maximum is at the cone tip.

If in addition `h` is bounded and continuous on `[0,infinity)`, then for every admissible `f_X`, the density `p_Q` is continuous on `R`.

### Proof

Conditioning on `X=x` gives for a.e. `q`

\[
p_Q(q)=\int_{\mathbb R}f_X(x)
 h(q+\lambda x^2)\,\mathbf1_{\{q+\lambda x^2\ge0\}}\,dx.
\tag{2.3}
\]

#### Nonnegative levels

For `q>=0`, monotonicity of `h` gives

\[
h(q+\lambda x^2)\le h(\lambda x^2).
\]

The reward `x\mapsto h(\lambda x^2)` is even and nonincreasing in `|x|`.  The one-dimensional bathtub principle under `0<=f<=1`, `integral f=1` therefore yields

\[
p_Q(q)
\le\int f_X(x)h(\lambda x^2)dx
\le\int_{-1/2}^{1/2}h(\lambda x^2)dx
=M_\lambda(h).
\tag{2.4}
\]

#### Negative levels and the exact fragmented optimizer

Write `q=-lambda r^2`, `r>0`.  Then

\[
p_Q(-\lambda r^2)
=\int_{|x|\ge r}f_X(x)
 h(\lambda(x^2-r^2))dx.
\tag{2.5}
\]

The reward in (2.5) is zero on `(-r,r)`, takes its largest value immediately outside the two boundary points `+-r`, and decreases as `|x|` moves away from those boundaries.  Its superlevel sets are exactly symmetric two-sided shells.  Hence the cap-one, mass-one bathtub maximizer is the set `E_r` in (2.2), whose total Lebesgue measure is one.  Consequently

\[
\begin{aligned}
p_Q(-\lambda r^2)
&\le2\int_r^{r+1/2}h(\lambda(x^2-r^2))dx\\
&=2\int_0^{1/2}h(\lambda(y^2+2ry))dy\\
&\le2\int_0^{1/2}h(\lambda y^2)dy
=M_\lambda(h),
\end{aligned}
\tag{2.6}
\]

again by monotonicity of `h`.  This proves (2.1).  At `q=0`, taking `X` uniform on `[-1/2,1/2]` gives equality, proving sharpness over heavy laws.

For continuity, extend `h` by zero to the negative half-line.  Although this extension may jump at zero, for each fixed `x` the function of `q` is continuous except possibly at the single point `q=-lambda x^2`; for any convergent sequence of output levels the exceptional `x`-set has Lebesgue measure zero.  The integrand is dominated by `||h||_infty f_X(x)`, which is integrable.  Dominated convergence gives continuity of (2.3).  QED.

### Important structural consequence

This theorem explicitly shows why a global proof cannot simply impose connected-support extremizers on every conditional level: for every negative output `q`, the exact cap-one optimizer in this branch is two separated intervals.  Yet the fragmented optimizer still loses globally because the shell is pushed outward and `h` is decreasing.

## 3. Two symmetric-unimodal banks produce a monotone positive core

Let `Y,Z` be independent with even densities `g_1,g_2` that are nonincreasing on `[0,infinity)`.  Put

`S=Y^2+Z^2`.

For `s>0`, polar coarea gives

\[
\boxed{
h(s)=\frac12\int_0^{2\pi}
 g_1(\sqrt{s}\cos\theta)
 g_2(\sqrt{s}\sin\theta)\,d\theta .}
\tag{3.1}
\]

For every fixed `theta`, both absolute arguments in (3.1) increase with `s`; hence each factor and their product are nonincreasing.  Therefore

\[
\boxed{h(s)\text{ is nonincreasing on }[0,infinity).}
\tag{3.2}
\]

When `g_1,g_2` are bounded and continuous, `h` is bounded and continuous as well.  Combining (3.2) with Theorem 2 gives a global all-output theorem for arbitrary cap-one `X`.

## 4. Exact finite source-valid target family

For each integer `m>=2`, let

\[
B_m=m^{-1/2}\sum_{j=1}^mU_j,
\qquad
C_m=m^{-1/2}\sum_{j=1}^mV_j,
\]

where all `U_j,V_j` are independent `Unif[-1/2,1/2]`.  Their common density `g_m` is even and log-concave (convolution and scaling preserve log-concavity), hence nonincreasing in `|x|`; for `m>=2` it is continuous.

Let `X` be any independent cap-one probability density and fix `lambda>=1`.  Define

\[
Q_{m,\lambda}=B_m^2+C_m^2-\lambda X^2.
\tag{4.1}
\]

This is an exact physical QFORM target.  Indeed, in the original `2m+1` independent coordinates its matrix is

\[
A_{m,\lambda}
=(-\lambda)\oplus\frac1mJ_m\oplus\frac1mJ_m,
\tag{4.2}
\]

and therefore

\[
\boxed{\operatorname{spec}_{\ne0}(A_{m,\lambda})=
\{-\lambda,1,1\}.}
\tag{4.3}
\]

There are exactly three eigenvalues of modulus at least one.  The two positive modes are genuine nonseparable original-coordinate banks when `m>1`; no independence is asserted after spectral diagonalization.

Let `h_m` denote the density of `B_m^2+C_m^2`.  By Section 3 it is nonincreasing.  Theorem 2 gives the exact sharp heavy-law/global-output identity

\[
\boxed{
\sup_{0\le f_X\le1,\ \int f_X=1}
\|p_{Q_{m,\lambda}}\|_\infty
=M_{m,\lambda}
:=2\int_0^{1/2}h_m(\lambda x^2)dx .}
\tag{4.4}
\]

In particular `M_{m,\lambda}` is nonincreasing in `lambda`, so strict minority-sign spectral slack cannot worsen this entire aligned-bank boundary:

\[
\boxed{M_{m,\lambda}\le M_{m,1}\qquad(\lambda\ge1).}
\tag{4.5}
\]

For every negative level `q=-lambda r^2`, the levelwise cap-one optimizer is the disconnected set (2.2), but (2.6) proves its value cannot exceed the cone-tip value.  Thus **there is no hidden negative two-sheet finite-row spike anywhere in this endpoint family**.

## 5. Gaussian diffuse limit and its exact global ceiling

The local CLT for normalized centered-uniform sums gives

\[
g_m\to\gamma_{1/12}
\]

uniformly on compact sets.  Applying (3.1) on `0<=s<=1/4` therefore gives

\[
h_m(s)\to6e^{-6s}
\]

uniformly on that compact interval.  Hence

\[
M_{m,1}\longrightarrow
C_-:=12\int_0^{1/2}e^{-6x^2}dx
=\sqrt{6\pi}\,\operatorname{erf}(\sqrt{3/2}).
\tag{5.1}
\]

The limit statement also follows from the weighted local Edgeworth theorem already used in earlier B17 work, but no finite-order expansion is needed here.

For the Gaussian endpoint itself, with `B,C iid N(0,1/12)`, Section 2 is exact for every output level and every cap-one heavy law:

\[
\boxed{
\sup_{f_X\le1}\|p_{B^2+C^2-X^2}\|_\infty
=C_-
=3.9801056750420088\ldots .}
\tag{5.2}
\]

At `q>=0`, the optimizing law is the centered unit interval and

\[
\sup_f p_Q(q)=C_-e^{-6q}.
\tag{5.3}
\]

At `q=-r^2<0`, the exact optimizer is

\[
f=\mathbf1_{[r,r+1/2]\cup[-r-1/2,-r]},
\]

and the exact optimized value is

\[
\boxed{
\sup_f p_Q(-r^2)
=12\int_0^{1/2}e^{-6(y^2+2ry)}dy,
}
\tag{5.4}
\]

which is strictly decreasing in `r>0`.  Thus (5.2) is a **global**, not merely cone-tip, statement.

A previously established elementary certificate, reproduced here for completeness, is

\[
C_-<\frac{97}{24}<3\sqrt2.
\tag{5.5}
\]

One route is the Mills lower bound at `z=sqrt(3/2)`, together with `pi<22/7` and `e^{3/2}<9/2`, yielding

`C_-<sqrt(6pi)-(3/2)e^{-3/2}<35/8-1/3=97/24`;

and `(97/24)^2<18` proves the final comparison.

## 6. Required application of the completed fleet04/B17 result

The newest completed designated-partner result read for this run is

`QFORM-MACROFRAGMENTED-STRICTSLACK-DENSE-WITNESS-v1`,

from

`yspennstate/math-open-problems@4be63022324b82f254f1d7a4353a3e883f08d10a`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B17/20260924T011922Z-fleet04-B17-QFORM-r6/REPORT.md`.

For every

\[
0<\theta<\frac13\log\left(\frac{3\sqrt2}{4}\right),
\]

it constructs an entrywise-dense exact-target sequence with spectrum

\[
\{1,1,-(1+1/m)\}
\]

and independent normalized cap-one two-component laws of arbitrarily separated support, satisfying

\[
\liminf_m\|p_{Q_m^{\rm partner}}\|_\infty
\ge3\sqrt2\,e^{-3\theta}.
\tag{6.1}
\]

Apply this theorem at the concrete value `theta=1/100`.  Since `e^{-x}>1-x` for `x>0`,

\[
3\sqrt2e^{-3/100}
>\frac{291\sqrt2}{100}.
\tag{6.2}
\]

Moreover

\[
\frac{291\sqrt2}{100}>\frac{97}{24},
\tag{6.3}
\]

because after cancelling `97`, (6.3) is equivalent to `72sqrt(2)>100`, or `18sqrt(2)>25`, whose square is the exact integer inequality `648>625`.

Combining (5.5), (6.1)-(6.3) gives the actual equation-level separation

\[
\boxed{
\liminf_m\|p_{Q_m^{\rm partner}}\|_\infty
>\frac{97}{24}
>C_-
=\sup_{f_X\le1}\|p_{B^2+C^2-X^2}\|_\infty .}
\tag{6.4}
\]

Numerically only as a check,

`3sqrt(2)e^{-0.03}=4.117251705266084...`

while

`C_-=3.980105675042009...`.

Thus the partner's dense rotated, fragmented strict-slack family is rigorously more dangerous than the **entire global output profile** of the minority-axis one-heavy Gaussian-complement endpoint, not just more dangerous than its cone tip.

This comparison is especially informative because both mechanisms have the same limiting three-mode mixed signature.  The excess danger cannot be attributed merely to negative output levels in the aligned one-heavy endpoint; it requires leaving this monotone-core-minus-square structure (through cross-sign physical mixing, fragmented diffuse components, or another genuinely coupled mechanism).

## 7. What this rules out — and what remains open

This report closes one precise off-tip escape route:

* one arbitrary cap-one heavy coordinate;
* two same-sign symmetric-unimodal diffuse banks;
* arbitrary minority magnitude `lambda>=1`;
* every finite bank size `m>=2`;
* every output level, including the negative two-sheet side;
* arbitrary heavy-law fragmentation.

The negative-level optimizer is itself fragmented, so the theorem does not rely on a false connected-support principle.

It does **not** close the coupled interior `0<a<1` of

`-aX^2+2sqrt(1-a^2)XB+aB^2+C^2`,

where the cross term destroys the monotone-core representation.  It also does not address two or more non-collinear macroscopic rows, rough surviving non-Gaussian shared components, arbitrary additional active spectrum, or the unrestricted full matrix problem.

Therefore:

**Full QFORM: OPEN / NOT PROVED / NOT DISPROVED.**  
**Full-target continuity: OPEN.**

The next B17 step should attack the interior negative two-sheet kernel itself, or a two-heavy shared-diffuse family; repeating cone-tip or Gaussian-limit calculations would be redundant.
