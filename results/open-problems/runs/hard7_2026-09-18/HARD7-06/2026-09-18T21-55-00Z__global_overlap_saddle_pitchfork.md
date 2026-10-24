Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** Primary metric **no movement**: `L_6 >= 0 -> L_6 >= 0`; substantive auxiliary movement: the positive stationary-overlap count for the exact symmetric raw-count variational problem is **UNMEASURED -> 1**, with a unique global correlated maximizer isolated exactly; methods tried: **B1 / B6 / B20**.

# HARD7-06 run 2 — the d=6 raw-count instability is a unique global correlated saddle, born in a supercritical pitchfork

Status: **PARTIAL / Chang--Kolhe--Sohn k=3 sharpness conjecture remains OPEN under bounded current-status review.**

Canonical ownership remains `operations/claims/CKS-2024-RREG-HYPER2COL-K3.md`, owner HARD7-06. I recovered the prior run before doing new work; its exact result was

\[
S_d''(0)=\frac{2d-11}{11},\qquad S_6''(0)=\frac1{11}>0,
\]

for the symmetric-overlap rate of the ordinary unweighted balanced-coloring count in the d-regular 3-uniform configuration model. That run established only a **local** instability of independent overlap and left the source probability metric unchanged.

Exact checker added and read back:

- `artifacts/hard7_2026-09-18/HARD7-06/k3_d6_global_overlap_exact.py`, commit `4a45b711f239a774de33c163c5b0343a4030fa91`;
- executed exact output `artifacts/hard7_2026-09-18/HARD7-06/k3_d6_global_overlap_exact.out`, commit `19c929016d16ed4007b6b2dcb42f968cded54d89`, ending `ALL_EXACT_CHECKS_PASS`.

The finite algebraic certificate uses exact `Fraction` arithmetic only.

## 1. Continuity, ownership, and current-status check

I re-read `operations/hard7_2026-09-18/CONTROL.md`, the current HARD7-06 claim, the prior HARD7-06 report, and repository search results around the claim. A contemporaneous repository search also recovered another track explicitly describing this CKS target as exclusively owned by HARD7-06, so there is no ownership release or collision to act on.

A bounded current-literature search dated 2026-09-18 UTC / 2026-09-19 local checked the exact title, arXiv `2308.02075`, the phrases `random regular hypergraph 2-colorability d=6 threshold`, and 2025--2026 follow-up terms. It recovered the 2024 Chang--Kolhe--Sohn proceedings paper and current metadata pages; the source still states that locating the threshold for small fixed `k>=3` is open and that its explicit `d_*(k)` is conjecturally sharp. I found no later source in this bounded search proving the exact `k=3,d=6` lower side. This is bounded negative evidence, not proof of worldwide openness.

Primary source: Evan Chang, Neel Kolhe, Youngtak Sohn, *Upper Bounds on the 2-Colorability Threshold of Random d-Regular k-Uniform Hypergraphs for k >= 3*, APPROX/RANDOM 2024, DOI `10.4230/LIPIcs.APPROX/RANDOM.2024.47`, arXiv:2308.02075.

The frozen source metric remains

\[
L_6:=\sup\{L:\liminf_n\Pr(H_{n,6,3}\text{ is 2-colorable})\ge L\}.
\]

No source-model lower bound is proved here, hence honestly

\[
L_6\ge0\ \longrightarrow\ L_6\ge0.
\]

## 2. Starting point: the exact one-dimensional overlap problem

Use the notation from run 1. On the symmetric overlap slice

\[
q_{00}=q_{11}=\frac{1+\theta}{4},\qquad
q_{01}=q_{10}=\frac{1-\theta}{4},\qquad -1<\theta<1.
\]

For admissible ordered 3-edge joint patterns the exact partition polynomial is

\[
P(t)=6+12t+12t^2+6t^3=6(1+t)(1+t+t^2).
\]

Writing `u=log t`, the marginal constraint is

\[
\frac{tP'(t)}{P(t)}=\frac32(1+\theta).
\]

Solving for `theta` as a rational function of `t` gives

\[
\boxed{\theta(t)=
\frac{(t-1)(3t^2+5t+3)}{3(t+1)(t^2+t+1)}}. \tag{1}
\]

The Legendre-envelope identity from run 1 is

\[
H_p'(\theta)=-\frac32\log t(\theta),
\]

while

\[
H_q'(\theta)=-\operatorname{arctanh}\theta.
\]

Therefore the symmetric raw-count rate

\[
S_d(\theta)=(1-d)H_q(\theta)+\frac d3H_p(\theta)
\]

satisfies the exact derivative formula

\[
\boxed{S_d'(\theta)=(d-1)\operatorname{arctanh}\theta-\frac d2\log t(\theta).} \tag{2}
\]

The map `u -> theta` is strictly increasing because

\[
\frac{d\theta}{du}=\frac23\operatorname{Var}_u(N)>0
\]

throughout the interior. Hence `(1)` gives a bijection `t in (0,infinity) <-> theta in (-1,1)`.

## 3. B1 — change category: the transcendental d=6 saddle equation becomes one reciprocal polynomial

At `d=6`, a nonzero stationary point obeys, by `(2)`,

\[
\log t=\frac53\operatorname{arctanh}\theta. \tag{3}
\]

Set

\[
x=t^{1/5}>0.
\]

Equation `(3)` says

\[
e^{\operatorname{arctanh}\theta}=x^3,
\]

so

\[
\boxed{\theta=\frac{x^6-1}{x^6+1}.} \tag{4}
\]

Substitute `t=x^5` into `(1)` and equate it with `(4)`. Exact simplification gives

\[
\theta(x^5)-\frac{x^6-1}{x^6+1}
=
-\frac{2x^5(x-1)Q(x)}{D(x)}, \tag{5}
\]

where `D(x)>0` for `x>0` and

\[
\boxed{Q(x)=2x^{10}-x^9-x^8-x^7-x^6+3x^5-x^4-x^3-x^2-x+2.} \tag{6}
\]

Thus positive-overlap stationary points other than `theta=0` correspond exactly to roots `x>1` of `Q`.

The polynomial is reciprocal. Divide by `x^5` and put `y=x+x^{-1}`. The checker verifies the exact identity

\[
\frac{Q(x)}{x^5}=R(y),\qquad
R(y)=2y^5-y^4-11y^3+3y^2+12y+3. \tag{7}
\]

For `x>1`, `y>2`. Set `z=y-2`; then

\[
\boxed{R(z+2)=2z^5+19z^4+61z^3+73z^2+20z-1.} \tag{8}
\]

The descending coefficient signs in `(8)` are

\[
+,+,+,+,+,-,
\]

so Descartes' rule of signs gives **at most one positive root**. Because the value at `z=0` is `-1` and the polynomial tends to `+infinity`, there is exactly one. The exact checker additionally isolates it by

\[
R(2+43/1000)<0<R(2+44/1000).
\]

Equivalently, the unique `x>1` root satisfies

\[
\frac{1229}{1000}<x_*<\frac{1230}{1000},
\]

with both endpoint signs checked exactly. Since `(4)` is increasing in `x`, the unique positive stationary overlap obeys the exact rational bracket

\[
\boxed{
\frac{2445968453384696121}{4445968453384696121}
<\theta_*<
\frac{2462825991689}{4462825991689}
}. \tag{9}
\]

Numerically this is

\[
0.55015425<\theta_*<0.55185347,
\]

and a high-precision diagnostic solve gives `theta_* approx 0.55183305`.

### Global classification

Run 1 proved

\[
S_6''(0)=\frac1{11}>0,
\]

so `S_6'(theta)>0` for all sufficiently small positive `theta`. On the other hand `(1)` gives

\[
1-\theta(t)=
\frac{2(2t^2+4t+3)}{3(t+1)(t^2+t+1)}
\sim \frac{4}{3t},
\]

hence as `theta -> 1-` (equivalently `t->infinity`),

\[
\operatorname{arctanh}\theta
=\frac12\log t+O(1),
\]

and from `(2)`

\[
S_6'(\theta)=5\operatorname{arctanh}\theta-3\log t
=-\frac12\log t+O(1)\to-\infty. \tag{10}
\]

There is exactly one positive stationary point, so `(10)` and the positive sign near zero force

\[
S_6'(\theta)>0\quad(0<\theta<\theta_*),\qquad
S_6'(\theta)<0\quad(\theta_*<\theta<1).
\]

The rate is even in `theta` by global color-complement symmetry. Therefore:

> **The d=6 symmetric raw-count rate has exactly three interior stationary points: `0` and `±theta_*`. The independent point `0` is a strict local minimum; `±theta_*` are the unique nonzero stationary points and are the two global maxima on `(-1,1)`.**

This strengthens run 1 from a local curvature obstruction to a complete one-dimensional global saddle classification.

A high-precision diagnostic evaluation gives

\[
S_6(\theta_*)-S_6(0)\approx 0.00756443027,
\]

so the correlated saddle wins by a visible exponential rate. This decimal is diagnostic only; the exact theorem above does not depend on it.

## 4. B6 — deform through the exact replica-symmetric stability boundary

To understand how the correlated saddle is born rather than merely locating it at `d=6`, expand the exact Legendre rate around `theta=0`. Direct series inversion gives

\[
S_d(\theta)-S_d(0)
=a_2(d)\theta^2+a_4(d)\theta^4+a_6(d)\theta^6+O(\theta^8), \tag{11}
\]

with exact coefficients

\[
a_2(d)=\frac{2d-11}{22}, \tag{12}
\]

\[
a_4(d)=\frac{790d-14641}{175692}, \tag{13}
\]

\[
a_6(d)=\frac{270002d-19487171}{584615130}. \tag{14}
\]

Thus the stability boundary is exactly

\[
d_c=\frac{11}{2}.
\]

At this point

\[
a_2(d_c)=0,\qquad
\boxed{a_4(d_c)=-\frac{78}{1331}<0},\qquad
a_6(d_c)=-\frac{54552}{1771561}<0. \tag{15}
\]

Set `d=d_c+epsilon` and write `z=theta^2`. The nonzero stationary equation divided by `2theta` is

\[
0=a_2(d)+2a_4(d)z+3a_6(d)z^2+O(z^3). \tag{16}
\]

Since `2a_4(d_c) != 0`, the implicit-function theorem gives a unique analytic branch `z(epsilon)` through `(0,0)`. Its exact first derivative is

\[
\boxed{\theta_*^2
=\frac{121}{156}\,\epsilon+O(\epsilon^2).} \tag{17}
\]

Substituting `(17)` into `(11)` yields the rate gain

\[
\boxed{S_{d_c+\epsilon}(\theta_*)-S_{d_c+\epsilon}(0)
=\frac{11}{312}\,\epsilon^2+O(\epsilon^3).} \tag{18}
\]

Both rational coefficients in `(17)`--`(18)` are checked exactly in the archived artifact.

Equations `(15)`--`(18)` identify the transition as a **supercritical pitchfork** in the symmetric raw-count variational landscape: for `d<11/2`, independent overlap is locally stable; at `11/2` its quadratic curvature vanishes with a negative quartic term; just above `11/2`, two symmetry-related correlated maxima emerge continuously.

This is the precise deformation mechanism connecting the stable degree-5 raw-count saddle to the unstable degree-6 saddle.

## 5. B20 — identify exactly why the obvious algorithm/proof object fails

The ordinary second-moment proof object is the unweighted number `Z` of balanced proper 2-colorings. Its independent pair contribution is `theta=0`. The previous run showed only that `theta=0` is locally unstable at `d=6`. The present exact global classification shows more:

1. there is exactly one positive correlated saddle and its color-complement partner;
2. these saddles are the global maxima of the one-dimensional symmetric overlap rate;
3. they are not sporadic large-overlap endpoint artifacts: `(17)` shows they are born continuously at the exact local-stability threshold `d=11/2`.

Therefore the failure of the raw count is structural. Any proof strategy that keeps this same unweighted balanced-coloring partition function and requires independent-overlap dominance cannot work at `d=6`. One must change the counted object, truncate it, or reweight cluster/frozen-variable structure so that the positive `theta_*` saddle is suppressed.

This does **not** prove that every conceivable second-moment argument fails, and it does not prove anything negative about a correctly chosen cluster-weighted count. It identifies exactly what such a replacement must repair.

## 6. What moved and what did not

### Source metric

No movement:

\[
L_6\ge0\to L_6\ge0.
\]

The source simple-model 2-colorability probability remains unproved.

### Exact auxiliary progress

Before this run, only the local curvature at zero was known in this track. Now the symmetric raw-count landscape at `d=6` is globally classified:

- positive nonzero stationary points: **UNMEASURED -> exactly 1**;
- unique positive stationary overlap: exactly characterized by `(6)`--`(8)` and bracketed by `(9)`;
- global role: proved unique positive global maximizer, with symmetric negative partner;
- bifurcation type at `d_c=11/2`: **UNMEASURED -> supercritical pitchfork**, with exact slopes `121/156` and `11/312`.

These are theorem-sized route diagnostics, not movement of `L_6` and not closure of the source conjecture.

## 7. Next route

This is the second consecutive run with no movement in the frozen source metric, so it does not yet trigger the three-run stuck protocol. The next run must use a new method triple and should not recompute the raw-count landscape.

A useful next target is a genuinely changed counting object. The simplest nontrivial source-matched candidate is a nonlinear vertex weight depending on the number of incident constraints in which a vertex is the unique minority spin. A linear exponential weight is automatically constant because every proper 3-edge has exactly one minority vertex and therefore the total minority incidence is fixed at `nd/3`; that conservation law should be proved first so no fake one-parameter family is pursued. The first viable deformation must therefore be nonlinear (for example a centered quadratic or an explicit frozen-variable/cluster message weight), after which its two-replica Hessian can be compared against the exact raw-count pitchfork found here.

Suggested new methods for run 3: **B12** (exploit minority-incidence conservation), **B5** (introduce the first genuinely nonlinear weight parameter), **B3** (seek a stronger weighted statement whose induction/second moment can close). If the primary metric is unchanged again, section I requires the full stuck report rather than another auxiliary lemma.

## 8. Capability note

The requested GPT-6/maximum setting is still not exposed as a model or reasoning selector in this environment. This run actually identifies as **GPT-5.6 Sol**. Reasoning-effort telemetry is not exposed, hence **UNVERIFIED**. No claim is made that an hour of uninterrupted execution occurred. No scheduler was modified.

## 9. Structured ledger delta

```yaml
ledger_delta:
  track: HARD7-06
  source: "Chang-Kolhe-Sohn, APPROX/RANDOM 2024, sharpness of d_*(k) for random regular hypergraph 2-coloring"
  canonical_claim: operations/claims/CKS-2024-RREG-HYPER2COL-K3.md
  source_scope: "k=3 sharpness, boundary milestone d=6"
  status_before: PARTIAL
  status_after: PARTIAL
  primary_metric: "L_6 = largest proved liminf colorability-probability lower bound in source simple model"
  metric_before: ">=0"
  metric_after: ">=0"
  movement: no_movement_primary_metric_second_consecutive_run
  auxiliary_metric_1: "number of positive nonzero stationary points of exact symmetric raw-count S_6"
  auxiliary_before_1: UNMEASURED
  auxiliary_after_1: 1
  auxiliary_metric_2: "local bifurcation of correlated saddle at d_c=11/2"
  auxiliary_before_2: UNMEASURED
  auxiliary_after_2: "supercritical pitchfork; theta_*^2=(121/156)eps+O(eps^2), rate gain=(11/312)eps^2+O(eps^3)"
  methods_tried: [1, 6, 20]
  exact_artifact: artifacts/hard7_2026-09-18/HARD7-06/k3_d6_global_overlap_exact.py
  exact_output: artifacts/hard7_2026-09-18/HARD7-06/k3_d6_global_overlap_exact.out
  exact_output_status: ALL_EXACT_CHECKS_PASS
  source_closed: false
  next_methods: [12, 5, 3]
```
