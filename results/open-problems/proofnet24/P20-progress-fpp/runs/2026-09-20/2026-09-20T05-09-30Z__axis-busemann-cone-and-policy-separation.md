Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied model/reasoning receipt is exposed, so I do not claim GPT-6. ORIGINAL AXIS/DIAGONAL MILESTONE `c_*` REMAINS `0 -> 0`; this run changes mechanism materially and proves a quantitative axis-support Busemann residual cone gap, a distinct-mean Busemann policy-separation lemma, and a new asymmetric strict-triangle pair with explicit finite residual error using P04's newest length-8 transfer.**

# P20 T10 — axis-support Busemann cone exclusion and distinct-policy separation

Date: 2026-09-20 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Controlling policy: `operations/PROGRESS20_2026-09-20.md`.  
Canonical parent claim: `operations/claims/PROB10-10.md`; ownership remains with the native PROB10-10 lane. P20 is the complementary LIVE20 Busemann/variational route and does not overwrite owner files.  
Model: nearest-neighbor **undirected** FPP on `Z^2` with iid physical-edge weights `Exp(1)`.  
Status: **PARTIAL / OPEN** for full strict convexity. New theorem arguments below are complete modulo the explicitly cited ADH reconstructed-Busemann/coalescence dependencies and P04 finite-transfer inputs; they are `CANDIDATE_PROVED` pending later independent review.

## 1. Exact source and fixed before/after quantities

The source remains Auffinger--Damron--Hanson, *50 years of first passage percolation*, arXiv:1511.03262v2, Question 4 in the strict-convexity discussion: for continuous passage-time laws, prove strict convexity of the FPP limit shape. P20 continues only the source-valid specialization to iid `Exp(1)` **undirected** nearest-neighbor edge weights on `Z^2`. Directed integrable models, directed-versus-undirected comparisons, and sampled numerical curvature are not substitutes for this target.

Write `mu` for the deterministic time-constant norm and retain the canonical first directional milestone

\[
\Delta_{12}=2\mu(e_1)-\mu(1,1),
\qquad
c_*:=\sup\{c\ge0:\Delta_{12}\ge c\text{ is rigorously proved in this track}\}.
\]

Before this run: `c_*=0`.  
After this run: `c_*=0`.

So there is **no claim that the axis/diagonal pair is solved** and no claim of full strict convexity. The demonstrated gains are separate:

1. the symmetric axis-support Busemann residual now has an explicit strictly positive asymptotic density on the whole P04 cone `|y|/x >= 907/500`, with finite-scale positive certificates;
2. two stationary coalescing Busemann cocycles with distinct mean slopes must have positive local policy-disagreement probability, hence a strictly positive local mixed Bellman gap;
3. P04's new length-8 axis block enlarges P20's asymmetric strict-triangle family: the explicit pair `(10,21),(10,-20)` has a positive defect `>0.0953`, while the preceding P20 `A0` compiler gave a negative lower bound for that same pair;
4. the corresponding finite-target Bellman residual is already rigorously positive at scale `n=32` with an explicit error budget.

This is source-valid restricted-direction and mechanism progress, not source closure.

## 2. Essential state consumed and preserved failures

Only dependencies needed for the present mechanism were recovered:

- `operations/PROGRESS20_2026-09-20.md` and the LIVE20 mapping;
- `operations/claims/PROB10-10.md`;
- newest P20 report `proofnet24/P20-progress-fpp/runs/2026-09-20/2026-09-20T04-08-54Z__p04-wide-cone-residual-bootstrap.md`;
- newest P04 companion report `proofnet24/P04-progress-curvature/runs/2026-09-20/2026-09-20T04-47-14Z__ladder8-cone1814-transfer.md`, creation commit `33663b916927b4432e2688f07381c4b6f9e47e94`;
- current canonical PROB10-10 reports through `20260920T0416Z__cone-tilt-15over8-extension.md`;
- P20's earlier reconstructed-Busemann residual identity / sharp local Bellman-gap reports;
- the exact source status and a bounded 2026-09-20 literature refresh.

The historical R08 failures remain binding:

1. local deletion/detour savings can share one bypass, so multiplying local margins is invalid;
2. finite pointwise strict triangle saving fails on positive-probability cylinder events;
3. old fixed-corner exact blocks did not cross the axis/diagonal threshold;
4. R07 fluctuation/KPZ results do not imply curvature.

The present run does **not** multiply local surgeries. The Busemann cone theorem is an exact cocycle identity plus P04's macroscopic bounds; the new finite asymmetric residual is a three-distance identity plus expectation estimates. The policy-separation lemma is qualitative and is not falsely promoted to a global defect without a bypass-control theorem.

## 3. Fresh source/literature boundary

A bounded 20 September 2026 search again recovered no theorem closing ordinary iid Exp(1), nearest-neighbor, undirected `Z^2` strict convexity. The exact ADH source remains arXiv:1511.03262. Dembin--Elboim--Peled's quantitative planar coalescence theorem still assumes a nontrivial extreme-point hypothesis; Jacquet's 2024 theorem is strict unrestricted-versus-directed time-constant comparison rather than direction-to-direction strict convexity; recent 2026 spread-out-cycle FPP is a different graph/model. Search misses are bounded negative evidence only; publication novelty and exhaustive worldwide openness are **UNVERIFIED**.

For the Busemann step, this report uses the same ADH/Damron--Hanson reconstructed-Busemann machinery already recovered by P20: a chosen supporting functional `rho` admits a stationary cocycle in the reconstructed weak-limit measure, and ADH Lemma 5.10 identifies

\[
\mathbb E B(x,y)=\rho\cdot(y-x).
\]

The associated planar geodesic graph has the coalescence property used below. These are external theorem dependencies, not reproved here.

## 4. New P04 input: length-8 axis block and the 1.814 cone

P04's newest exact length-8 ladder computation proves

\[
\boxed{
\mu(e_1)\le A_8
:=
\frac{4688722489067361283750127182134186345695457354381617699}
{7437921710332085596529852377779940412620800000000000000}
=0.6303807261851404\ldots .
}
\tag{4.1}
\]

The finite expectation transfer has zero interface loss at concatenated length-8 scales.

It also proves, for

\[
\rho_0=\frac{907}{500}=1.814,
\qquad
c_1=\frac{63039}{100000}=0.63039,
\tag{4.2}
\]

that for every integer `a>=1`, every integer `b` with `b/a>=rho_0`, and every `n>=1`,

\[
\Pr\!\left(T(0,n(a,b))\le c_1an\right)
\le C_1\widehat\beta^{an},
\tag{4.3}
\]

where

\[
C_1=
\frac{26633487052538711}{2329665975000},
\qquad
\widehat\beta=\frac{12497}{12500}<1.
\tag{4.4}
\]

Consequently

\[
\mu(a,b)\ge c_1a
\qquad (b/a\ge907/500).
\tag{4.5}
\]

The earlier P04 slope-2 certificate remains valid and stronger in its narrower cone:

\[
\mu(a,b)\ge \frac23a
\qquad (b\ge2a),
\tag{4.6}
\]

with finite lower-tail constants

\[
C_0=\frac{27865448}{206955},
\quad
\beta_0=
\frac{713425217726611388616507115106921327}
{740604339057582092285156250000000000}<1.
\tag{4.7}
\]

The crucial new strict margins against the **same axis support** are therefore

\[
\boxed{
\gamma_2:=\frac23-A_8
=
\frac{269891984487362447269774403052440596051742645618382301}
{7437921710332085596529852377779940412620800000000000000}
=0.036285940481526315\ldots
}
\tag{4.8}
\]

and

\[
\boxed{
\gamma_{1.814}:=c_1-A_8
=
\frac{68977908882155446326458294510291016568757618382301}
{7437921710332085596529852377779940412620800000000000000}
=9.273814859645214\times10^{-6}>0.
}
\tag{4.9}
\]

These signs were checked by exact rational arithmetic in the archived checker.

## 5. Axis-symmetric supporting functional

Let

\[
a_*:=\mu(e_1)=\mu(e_2)>0.
\]

### Lemma 5.1 — a symmetric axis support exists

There is a supporting linear functional at `e1` equal to

\[
\boxed{\rho^{\rm ax}=(a_*,0).}
\tag{5.1}
\]

#### Proof

The subdifferential of the norm `mu` at nonzero `e1` is nonempty. If `(p,q)` is any supporting functional there, then necessarily `p=mu(e1)=a_*`. Reflection invariance under `(x,y)->(x,-y)` makes `(a_*,-q)` another supporting functional at `e1`. The subdifferential is convex, so their average `(a_*,0)` is supporting. QED.

Fix an ADH reconstructed stationary Busemann cocycle `B^ax` associated with this supporting functional. Its mean is

\[
\mathbb E B^{\rm ax}(x,y)=\rho^{\rm ax}\cdot(y-x).
\tag{5.2}
\]

For an oriented physical edge `(x,y)`, define the nonnegative Busemann residual

\[
r^{\rm ax}(x,y):=\tau_{xy}-B^{\rm ax}(x,y)\ge0.
\tag{5.3}
\]

The inequality follows from the passage-time triangle inequality in the Busemann limiting construction; reversing the edge also gives `|B^ax(x,y)|<=tau_xy`, hence integrability.

## 6. Exact Busemann residual metric identity

For vertices `x,y`, define

\[
R^{\rm ax}(x,y)
:=\inf_{\gamma:x\to y}
\sum_{(u,v)\in\gamma}r^{\rm ax}(u,v).
\tag{6.1}
\]

### Lemma 6.1 — residual equals passage time minus cocycle

Samplewise,

\[
\boxed{
R^{\rm ax}(x,y)=T(x,y)-B^{\rm ax}(x,y).
}
\tag{6.2}
\]

#### Proof

For every finite path `gamma=(x=x_0,...,x_k=y)`, cocycle telescoping gives

\[
\sum_{i=0}^{k-1}r^{\rm ax}(x_i,x_{i+1})
=
\sum_{i=0}^{k-1}\tau_{x_ix_{i+1}}-B^{\rm ax}(x,y).
\]

The second term is independent of the path. Infimizing the first term over paths gives `T(x,y)`. QED.

Taking expectations and using (5.2), for every integer vector `v`,

\[
\boxed{
\mathbb E R^{\rm ax}(0,nv)
=
\mathbb E T(0,nv)-n\rho^{\rm ax}\cdot v.
}
\tag{6.3}
\]

This is the exact infinite-volume Busemann analogue of P20's finite-target residual identity.

## 7. Quantitative Busemann cone gap

### P20-FPP-AXIS-BUSEMANN-CONE-GAP-17

**Claim: CANDIDATE_PROVED, dependent on the ADH reconstructed-Busemann mean identity and P04's proved transfer bounds.**

Let `v=(a,b)` with integers `a>=1`, `b>=0`.

### (A) New shallow cone `b/a >= 907/500`

If `b/a>=907/500`, then for every `n>=1`,

\[
\boxed{
\frac{\mathbb E R^{\rm ax}(0,nv)}{an}
\ge
\gamma_{1.814}-c_1C_1\widehat\beta^{an}.
}
\tag{7.1}
\]

Hence

\[
\boxed{
\liminf_{n\to\infty}
\frac{\mathbb E R^{\rm ax}(0,nv)}{an}
\ge\gamma_{1.814}>0.
}
\tag{7.2}
\]

Moreover the exact checker certifies, without floating-point sign decisions, that the right side of (7.1) is positive whenever `an>=90000`; at `an=90000` it is already larger than

\[
6.171812808351498\times10^{-6}.
\tag{7.3}
\]

### (B) Stronger slope-2 cone

If `b>=2a`, then

\[
\boxed{
\frac{\mathbb E R^{\rm ax}(0,nv)}{an}
\ge
\gamma_2-rac23C_0\beta_0^{an}.
}
\tag{7.4}
\]

In particular

\[
\boxed{
\liminf_{n\to\infty}
\frac{\mathbb E R^{\rm ax}(0,nv)}{an}
\ge\gamma_2
=0.03628594048\ldots .
}
\tag{7.5}
\]

The exact checker verifies that (7.4) is already positive for `an=209`, with margin

\[
2.829960006843609\times10^{-5}.
\tag{7.6}
\]

#### Proof

For the shallow cone, P04's tail estimate gives, using only nonnegativity of passage times,

\[
\begin{aligned}
\mathbb E T(0,nv)
&\ge c_1an\,\Pr(T(0,nv)>c_1an)\\
&\ge c_1an\left(1-C_1\widehat\beta^{an}\right).
\end{aligned}
\tag{7.7}
\]

By (6.3), `rho^ax . v = a_* a`, and P04's axis upper bound gives `a_*<=A8`. Therefore

\[
\begin{aligned}
\mathbb E R^{\rm ax}(0,nv)
&\ge c_1an(1-C_1\widehat\beta^{an})-a_*an\\
&\ge an\left[(c_1-A_8)-c_1C_1\widehat\beta^{an}\right],
\end{aligned}
\]

which is (7.1). Letting `n->infinity` proves (7.2).

For the explicit `an=90000` sign, use

\[
\widehat\beta^{90000}
=\left(1-\frac3{12500}\right)^{90000}
\le e^{-108/5}.
\]

The checker lower-bounds `e^{108/5}` by its degree-30 Taylor polynomial, all with exact `Fraction` arithmetic, and verifies the resulting rational lower bound in (7.3) is positive.

The slope-2 proof is identical with `c_1,C_1,beta_hat` replaced by `2/3,C_0,beta_0`; the `an=209` comparison is performed exactly. QED.

### Corollary 7.2 — deterministic contact-sector exclusion

Let

\[
\mathcal C_{\rm ax}:=
\{v\ne0:\mu(v)=\rho^{\rm ax}\cdot v\}
\]

be the contact cone of the symmetric axis supporting functional. Then in the right half-plane,

\[
\boxed{
\mathcal C_{\rm ax}
\cap
\{(x,y):x>0,\ |y|/x\ge907/500\}
=\varnothing.
}
\tag{7.8}
\]

Indeed for such `v`, P04 gives `mu(v)>=c_1x>A_8x>=a_*x=rho^ax.v`. Vertical vectors `x=0` are also not contacts because `mu(0,y)>0=rho^ax.(0,y)` for `y!=0`.

Thus every ADH Busemann geodesic associated with this support is confined to the corresponding contact sector strictly inside the `907/500` cone. This is a genuine infinite-volume Busemann geometric consequence of P04's block transfer, not sampled curvature.

## 8. Distinct-mean Busemann cocycles force local policy disagreement

The preceding theorem gives a quantitative residual sector but still does not address the diagonal-support flat-face scenario directly. The next lemma identifies the exact local variational order parameter that must be transferred by P04.

Let `B^1,B^2` be two stationary Busemann cocycles on a common Exp(1) environment in a stationary joining. Define residuals

\[
r^k_x(e)=\tau_{x,x+e}-B^k(x,x+e),
\qquad k=1,2,\quad |e|_1=1.
\tag{8.1}
\]

Use the prior P20 sharp-star result: under the continuous Exp law, each cocycle has almost surely a **unique** outgoing zero-residual edge at every fixed vertex. Let `s_k(x)` be that successor. Assume also the standard planar coalescence conclusion for each reconstructed Busemann geodesic graph.

### P20-FPP-DISTINCT-BUSEMANN-POLICY-SEPARATION-18

**Claim: CANDIDATE_PROVED under the stated reconstructed-Busemann uniqueness/coalescence dependencies.**

If the two mean slopes are distinct,

\[
\rho_1\ne\rho_2,
\qquad
\mathbb E B^k(0,z)=\rho_k\cdot z,
\]

then

\[
\boxed{
\Pr(s_1(0)\ne s_2(0))>0.
}
\tag{8.2}
\]

Furthermore, for every `0<theta<1`, define the mixed local residual gap

\[
\kappa_\theta(x)
:=
\min_{|e|_1=1}
\left[\theta r^1_x(e)+(1-\theta)r^2_x(e)\right].
\tag{8.3}
\]

Then

\[
\boxed{
0<\mathbb E\kappa_\theta(0)<\infty.
}
\tag{8.4}
\]

#### Proof of policy separation

Assume for contradiction that `Pr(s_1(0)=s_2(0))=1`. Stationarity gives the same probability-one equality at every `x`; because `Z^2` is countable, with probability one

\[
s_1(x)=s_2(x)\quad\text{for all }x.
\tag{8.5}
\]

Call the common successor map `s`. Along every successor edge `(x,s(x))`, uniqueness and zero residual give simultaneously

\[
B^1(x,s(x))=\tau_{x,s(x)}=B^2(x,s(x)).
\tag{8.6}
\]

Let `C=B^1-B^2`, itself a cocycle. Then `C=0` on every common successor edge. Because the common geodesic graph is coalescing, for arbitrary vertices `x,y` their forward successor rays meet at some `z`. Hence

\[
C(x,z)=0=C(y,z),
\]

and the cocycle identity yields

\[
C(x,y)=C(x,z)-C(y,z)=0.
\]

Thus `B^1=B^2` on all vertex pairs almost surely, contradicting distinct means `rho_1!=rho_2`. Therefore (8.2) holds.

#### Proof of positive mixed gap

On the disagreement event the unique zero of `r^1_0` and the unique zero of `r^2_0` occur on different edges. For each of the four outgoing edges at least one residual is therefore strictly positive. Since `0<theta<1` and there are finitely many edges,

\[
\kappa_\theta(0)>0
\quad\text{on }\{s_1(0)\ne s_2(0)\}.
\]

By (8.2), `Pr(kappa_theta(0)>0)>0`, so `E kappa_theta(0)>0` once integrability is checked.

For an upper bound, take the zero edge of `r^1`. On that edge

\[
\kappa_\theta(0)
\le (1-\theta)r^2_0(e).
\]

The edgewise Busemann inequalities `|B^2(0,e)|<=tau_e` imply `r^2_0(e)<=2tau_e`. Therefore

\[
\kappa_\theta(0)
\le2\max_{|e|=1}\tau_e,
\]

which is integrable for four iid Exp(1) variables. This proves (8.4). QED.

### Flat-face specialization

Under the contradiction hypothesis `Delta_12=0`, norm symmetry and triangle equality force the first-quadrant norm to be `a_*(x+y)`; the diagonal interior of that flat face has the supporting slope

\[
\rho^{\rm diag}=(a_*,a_*),
\tag{8.7}
\]

while Section 5 supplies the distinct symmetric axis support

\[
\rho^{\rm ax}=(a_*,0).
\tag{8.8}
\]

The canonical retained lower bound `a_*>=0.3002823` makes the mean-slope separation quantitatively nonzero, but positivity alone suffices for Lemma 18. Therefore **flatness forces a strictly positive local mixed Bellman-gap expectation between an axis-support and diagonal-support Busemann policy.**

This is not yet a contradiction. The unresolved global step is to convert `E kappa_theta(0)>0` into a positive asymptotic residual cost for every relevant long path despite the possibility that a path avoids the disagreement set. That is now the exact P20/P04 interface.

## 9. New asymmetric strict-triangle family from the same length-8 block

The latest P04 axis bound also strengthens the preceding P20 finite-target compiler. This is secondary to the Busemann attack but gives a concrete source-valid defect with a small finite scale.

Let

\[
u=(a,b),\qquad v=(c,-d),
\]

with `a,c>0`. Suppose each leg has a certified P04 lower coefficient `L_u,L_v`, meaning

\[
\mu(u)\ge L_u a,
\qquad
\mu(v)\ge L_v c,
\]

where one may take

\[
L=\frac23\quad\text{if slope }\ge2,
\qquad
L=c_1\quad\text{if slope }\ge907/500.
\tag{9.1}
\]

Put `H=|b-d|`. Since `u+v=(a+c,b-d)`, the new axis block gives

\[
\mu(u+v)
\le A_8(a+c+H).
\tag{9.2}
\]

Hence

### P20-FPP-HETEROGENEOUS-CONE-DEFECT-19

\[
\boxed{
\mu(u)+\mu(v)-\mu(u+v)
\ge
(L_u-A_8)a+(L_v-A_8)c-A_8H.
}
\tag{9.3}
\]

This formula permits the two legs to use different certified cone regimes.

In the strong slope-2/slope-2 case it becomes

\[
\Delta(u,v)
\ge
\gamma_2(a+c)-A_8H.
\tag{9.4}
\]

Thus the allowed transverse-mismatch ratio is now

\[
\boxed{
\frac{H}{a+c}<\frac{\gamma_2}{A_8}
=0.057561944669718965\ldots .
}
\tag{9.5}
\]

The preceding P20 compiler, before the length-8 P04 improvement, allowed only `0.0329618084...` in its slope-2 regime. This is a strict directional-scope gain.

### Explicit pair newly certified by the improved block

Take

\[
\boxed{u=(10,21),\qquad v=(10,-20),\qquad u+v=(20,1).}
\tag{9.6}
\]

Both legs lie in the slope-2 cone and `H/(a+c)=1/20=0.05`, which lies **outside** the old P20 mismatch threshold but inside (9.5). The exact lower bound is

\[
\boxed{
\Delta(u,v)
\ge
\kappa_*:=
\frac{33767485746661317221207660900696455968542645618382301}
{354186748111051695072850113227616210124800000000000000}
=0.09533808344538588\ldots>0.
}
\tag{9.7}
\]

For comparison, substituting the preceding axis upper constant `A0=0.645393...` into the same formula gives `-0.2199267054...`, so this pair was not certified by P20's previous asymmetric theorem.

## 10. Finite-target residual for the new pair: positive already at n=32

For `n` divisible by eight, set

\[
A_n=n(10,21),
\qquad
Z_n=n(20,1),
\]

and let `Gamma_n` be the unique `0`-to-`A_n` geodesic. Define the target-`Z_n` residual energy

\[
\mathcal R_n
=
\sum_{e\in\Gamma_n}
\left(\tau_e+T(e^+,Z_n)-T(e^-,Z_n)\right).
\]

Telescoping gives exactly

\[
\mathcal R_n
=T(0,A_n)+T(A_n,Z_n)-T(0,Z_n).
\tag{10.1}
\]

The slope-2 lower-tail bounds on the two legs give

\[
\mathbb E T(0,A_n),\ \mathbb E T(A_n,Z_n)
\ge
\frac{20}{3}n\left(1-C_0\beta_0^{10n}\right)
\]

leg-by-leg, equivalently total lower-tail loss

\[
\frac23C_0\left(10\beta_0^{10n}+10\beta_0^{10n}\right)n.
\tag{10.2}
\]

Because `8|n`, coordinate-axis concatenation with P04's exact length-8 expectation transfer yields

\[
\mathbb E T(0,Z_n)
\le A_8(20n+n)=21A_8n.
\tag{10.3}
\]

Therefore

\[
\boxed{
\frac{\mathbb E\mathcal R_n}{n}
\ge
\kappa_*
-
\frac23C_0\left(20\beta_0^{10n}\right).
}
\tag{10.4}
\]

At the explicit scale `n=32`, the executed exact checker gives

\[
\text{error}=0.011429683765066338\ldots,
\]

so

\[
\boxed{
\frac{\mathbb E\mathcal R_{32}}{32}
>0.08390839968031955,
\qquad
\mathbb E\mathcal R_{32}>2.685068789770225.
}
\tag{10.5}
\]

This is an exact-rational sign certificate; the decimals are renderings only. It is not sampled curvature.

## 11. Why this run changes the attack materially

The previous run bootstrapped a wide-cone norm inequality into a finite residual family. This run does not stop at replugging constants. It moves to an **infinite-volume support/cocycle mechanism**:

1. identify the reflection-symmetric axis support `rho^ax`;
2. turn P04's block lower bounds into a strictly positive Busemann residual time constant with finite errors;
3. exclude an explicit cone from the contact sector of the axis Busemann support;
4. prove that two coalescing Busemann cocycles with distinct mean slopes cannot share their local optimal policy almost surely;
5. under the target flatness hypothesis, obtain a positive local mixed Bellman curvature order parameter `E kappa_theta>0`.

This isolates a more precise global obstruction than the old generic phrase “need positive-density pivots.” The remaining issue is now **pathwise avoidance of a positive-density disagreement field**.

## 12. P04 handoff: exact missing block theorem

P04 now has two calibration targets.

### Calibration A — proved macroscopic axis-support residual

For slope `>=2`, the Busemann residual density is at least `gamma_2=0.03628594...`; for slope `>=907/500`, it is at least `gamma_1.814=9.2738e-6`, with the explicit finite error formulas (7.1) and (7.4).

Any proposed asynchronous frontier/block compression for the axis-support Busemann state should recover a positive fraction of these known residual densities. If it outputs zero on these calibration directions, the compression has discarded essential continuation information.

### Calibration B — flatness-forced local two-support curvature

Under `Delta_12=0`, a stationary joining of axis-support and diagonal-support Busemann cocycles has

\[
\mathbb E\kappa_\theta(0)>0.
\]

A sufficient P04 transfer theorem would be any rigorous separator/compiler of the form

\[
\liminf_{n\to\infty}\frac1n
\inf_{\gamma\in\mathcal P_n}
\sum_{x\in\gamma}\kappa_\theta(x)
\ge c_{\rm sep}>0
\tag{12.1}
\]

for the relevant residual paths, or a block version with an explicit interface loss `epsilon_L<c_sep`. Such a theorem would turn the local mixed Bellman gap into a strict macroscopic variational gap and would directly attack the flat-face hypothesis rather than merely widen the already-solved opposing-cone region.

The present report does **not** assume (12.1). It names it as the residual obstruction.

## 13. Next P20 attack

The next attack should not further optimize the local Exp toll or merely update cone constants. It should target the **two-support avoidance problem**.

Concrete route:

1. construct a stationary joining of the axis-support and diagonal-support reconstructed Busemann environments under the contradiction hypothesis `Delta_12=0`;
2. mark policy-disagreement sites `D={x:s_ax(x)!=s_diag(x)}` and the positive mixed gap `kappa_theta(x)`;
3. use planar coalescence to study connected components of the common-successor graph on `D^c`;
4. prove a block dichotomy: either a long residual path crosses linearly many disagreement blocks, paying a controlled truncated `kappa_theta` mass, or it remains for a macroscopic distance in a common-successor component;
5. rule out the latter by showing that an infinite common-successor ray would have to be a geodesic simultaneously compatible with the distinct support/contact sectors. P04's new contact-cone exclusion supplies the first quantitative outer barrier for this step.

The hard point is that positive **spatial** density of `D` does not automatically imply positive density along an adversarial residual path. That is the exact place where a separator or common-forest theorem is needed. Until that is proved, the full axis/diagonal defect remains open.

## 14. Exact checker and output

Essential arithmetic was executed with Python `Fraction` arithmetic and no sampled passage-time simulation:

- checker: `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T05-09-30Z__busemann-cone-check.py`, creation commit `a2435d77674e723fcb843aa13363c9b0e59069cf`;
- output: `proofnet24/P20-progress-fpp/artifacts/2026-09-20/2026-09-20T05-09-30Z__busemann-cone-check.out`, creation commit `b484fa112d4fcb87ae511e38c65a6fa369d19470`.

The output verifies:

- `gamma_2>0` and `gamma_1.814>0` exactly;
- the new asymmetric pair has positive exact `kappa_*`;
- the preceding P20 `A0` bound is nonpositive for that pair, proving the directional-scope gain is genuine relative to the previous compiler;
- the `n=32` finite residual margin is positive;
- the slope-2 Busemann finite residual is positive at `an=209`;
- the slope-1.814 Busemann finite residual is positive at `an=90000` using a rigorous rational Taylor lower bound for `exp(108/5)`;
- final marker `ALL_EXACT_CHECKS_PASS`.

The checker only certifies arithmetic inside proved inequalities. It is not a numerical substitute for the FPP theorem.

## 15. Short cyclic-interval handoff, no audit waiting

The displaced P20 cyclic-interval result remains preserved and untouched: `P20-FOKAM-BITJOKA-CI241-SEMICIRCLE-MAJORITY-01` is still the source-literal YES proof candidate; its supplementary exact sanity check remains PASS; P26's full-proof/source-quantifier audit remains PASS; the last recovered state had only one of the two independent audits required for campaign certification. No completed certification, publication or novelty claim is made here. This FPP run spent no research time waiting for the missing second audit.

## 16. Honest status and residual obstruction

### Original problem

- full ADH strict convexity: **OPEN -> OPEN/PARTIAL**;
- frozen axis/diagonal `c_*`: **0 -> 0**.

### Demonstrated mechanism gains

- axis-support contact-sector exclusion: newly quantified to slope `<907/500` in the right half-plane;
- axis-support Busemann residual density: `>=gamma_1.814>0` in the new P04 cone and `>=gamma_2>0` in the slope-2 cone, both with finite errors;
- distinct-mean coalescing Busemann policies: local disagreement probability **strictly positive**, hence mixed local Bellman gap has positive finite expectation;
- asymmetric opposing-cone mismatch threshold in the slope-2 regime improves from `0.0329618...` to `0.0575619...`;
- explicit new pair `(10,21),(10,-20)` gets defect `>=0.09533808...` and finite expected residual `>2.685` at scale 32.

### Residual obstruction

The exact missing theorem is no longer local strictness. It is a **pathwise separator/common-forest transfer** converting the positive local two-support gap into a positive cost along every relevant long residual path, with interface error controlled below the accumulated gap. Positive spatial density alone is insufficient because an optimized path may avoid disagreement sites.

No claim beyond these statements is made.

## ledger_delta

```text
P20 | T10 Exp(1) undirected Z2 FPP strict convexity | full source OPEN -> OPEN/PARTIAL; axis/diagonal c_* 0 -> 0 | NEW CANDIDATE_PROVED: symmetric axis support rho=(mu(e1),0); exact Busemann residual R=T-B; P04 length-8 input implies residual density >= 0.03628594048... on slope>=2 and >=9.27381486e-6 on slope>=907/500, with explicit finite positive scales an=209 and an=90000 respectively | NEW CANDIDATE_PROVED: distinct-mean coalescing Busemann cocycles must disagree locally with positive probability, giving E kappa_theta(0)>0 for every theta in (0,1) | NEW restricted source defect: (10,21)+(10,-20) has strict triangle defect >=0.095338083445...; finite target residual positive at n=32 with E R_32>2.68506878977 | residual obstruction: prove separator/common-successor transfer preventing optimized paths from avoiding positive-density two-support disagreement field | next: joint axis/diagonal Busemann policy-block dichotomy with P04 interface control | cyclic CI241 proof/audit state preserved, no audit waiting
```

END OF P20 FPP RUN REPORT
