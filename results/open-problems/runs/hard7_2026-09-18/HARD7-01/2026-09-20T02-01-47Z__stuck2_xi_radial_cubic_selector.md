Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. No movement in the frozen source metric `B_cart: infinity -> infinity`; full-source dimension `2 -> 2`. This is the second Section-I stuck/recovery run on the current BLYZ target. Methods tried: B13 / B19 / B27.**

# HARD7-01 — STUCK2: log-coordinate Xi region, radial monovariant, and a cubic-root generalized-radii selector

**Status:** `PARTIAL / SOURCE OPEN / STUCK2`.

The unrestricted Böröczky–Lutwak–Yang–Zhang log-Brunn–Minkowski conjecture is not solved here. This run executes the recovery chosen in the previous report rather than adding another product-tensorization lemma. The substantive output is a new exact structural reduction of Xi's three-dimensional generalized-radii feasible set, an explicit selector that repairs the previous AF-point failure on every aligned equal-volume box pair, and an exact obstruction showing that the two scalar Aleksandrov–Fenchel inequalities alone do not force that selector to exist for arbitrary mixed-volume data.

## 1. Continuity, ownership, exclusions, and consumed repository state

I resumed from

`runs/hard7_2026-09-18/HARD7-01/2026-09-20T01-03-08Z__stuck1_xi_generalized_radii.md`

rather than restarting. That report consumed the first allowed Section-I recovery, froze the source metrics at

`B_cart = infinity`, `d_full = 2`,

and selected Xi's generalized-radii mechanism with reserved methods **B13/B19/B27**.

For this run I reread the controlling files

- `operations/hard7_2026-09-18/CONTROL.md`,
- `operations/NEW_METHODS_2026-09-16.md`,
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`,
- root `POSTED.md`,
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`,
- the active claim `operations/claims/LOG-BRUNN-MINKOWSKI-SYMMETRIC.md`,
- the newest own checkpoint and repository alias/ownership hits for the same canonical claim.

The claim remains exclusively HARD7-01. No peer claim is overwritten, no shared root ledger is edited, and no posted/excluded result is reused as a new target.

A fresh bounded literature check on 20 September 2026 again found no unrestricted `n>=3` solution. The two newest directly relevant sources remain:

1. Dongmeng Xi, *A very short unified proof of Dar's conjecture and Log-Brunn--Minkowski in the plane*, arXiv:2609.08495, 8 Sep 2026, whose Section 3 proposes the generalized-radii route in `R^3`: https://arxiv.org/abs/2609.08495 .
2. XiaoRui Lu, *Logarithmic Brunn--Minkowski Inequality under n-2 Reflection Symmetries*, arXiv:2608.20730, 21 Aug 2026, proving a reflection-symmetric class rather than the unrestricted conjecture: https://arxiv.org/abs/2608.20730 .

Searches for `generalized radii log-Brunn-Minkowski`, Xi's arXiv identifier, and `Steiner polynomial discriminant mixed volumes log-Brunn-Minkowski` did not surface the reduction below. This is a bounded search, not a priority certificate.

## 2. Source problem and frozen metric

The source remains BLYZ Problem 1.1: for every origin-symmetric convex bodies `K,L subset R^n` and `lambda in [0,1]`, prove

\[
V_n((1-\lambda)\cdot K+_0\lambda\cdot L)
\ge V_n(K)^{1-\lambda}V_n(L)^\lambda.
\]

The admission metric was already saturated by the exact product theorem:

\[
\boxed{B_{\rm cart}:\infty\to\infty.}
\]

The unrestricted source dimension remains

\[
\boxed{d_{\rm full}:2\to2.}
\]

Hence this run records **NO MOVEMENT** in the source metric and is correctly labeled `STUCK2`, the second allowed recovery cycle on this target.

## 3. Normalize Xi's three-dimensional problem

As in the previous run, scale an equal-volume pair in `R^3` so that

\[
|K|=|L|=1.
\]

Write

\[
a:=3V(K,K,L),\qquad b:=3V(K,L,L),
\]

and

\[
M_0:=\tfrac12\cdot K+_0\tfrac12\cdot L,
\qquad
M_1:=\frac{K+L}{2},
\]

with

\[
m:=|M_0|,
\qquad
q:=|M_1|,
\qquad
A:=\frac{3V(M_0,M_0,M_1)}{m}.
\]

Minkowski's mixed-volume inequality gives `a,b >= 3`. By the cubic volume expansion,

\[
|K+L|=|K|+3V(K,K,L)+3V(K,L,L)+|L|,
\]

so

\[
\boxed{q=\frac{2+a+b}{8}.}
\tag{3.1}
\]

Xi's feasible set consists of positive `(t_1,t_2)` satisfying

\[
b\ge \frac1{t_1t_2}+t_1+t_2,
\qquad
 a\ge \frac1{t_1}+\frac1{t_2}+t_1t_2.
\tag{3.2}
\]

The target selector must additionally satisfy, with

\[
\lambda_i=\frac12\left(\sqrt{t_i}+\frac1{\sqrt{t_i}}\right),
\]

\[
A\ge \lambda_1+\lambda_2+\frac{q}{m\lambda_1\lambda_2},
\tag{X_-}
\]

and

\[
A\le \lambda_1+\lambda_2+\frac{q}{\lambda_1\lambda_2}.
\tag{X_+}
\]

The simultaneous selector would imply `m>=1`, hence midpoint log-BM in dimension three.

## 4. B13 — a radial monovariant hidden in Xi's feasible set

The previous report treated `(t_1,t_2)` as an opaque two-dimensional feasible region. The correct coordinates are logarithmic and symmetric in **three** variables.

Set

\[
z_1=t_1,\qquad z_2=t_2,\qquad z_3=(t_1t_2)^{-1},
\]

so `z_1z_2z_3=1`, and write

\[
z_i=e^{s_i},\qquad s_1+s_2+s_3=0.
\]

Then the two feasibility inequalities become

\[
E_+(s):=\sum_{i=1}^3e^{s_i}\le b,
\qquad
E_-(s):=\sum_{i=1}^3e^{-s_i}\le a.
\tag{4.1}
\]

Thus Xi's feasible set is exactly the `S_3`-symmetric compact convex set

\[
\boxed{
\mathcal C_{a,b}
=\{s\in\mathbb R^3:\ s_1+s_2+s_3=0,\ E_+(s)\le b,\ E_-(s)\le a\}.
}
\tag{4.2}
\]

### Proof of compactness and convexity

Each `E_+` and `E_-` is strictly convex on the plane `H={sum s_i=0}` because for every nonzero tangent vector `v in H`,

\[
D^2E_+(s)[v,v]=\sum_i e^{s_i}v_i^2>0,
\]

and similarly for `E_-`. Their sublevel sets are convex. Since `a,b>=3`, the origin belongs to both by `E_+(0)=E_-(0)=3`. Finally (4.1) gives `e^{s_i}<=b` and `e^{-s_i}<=a`, hence

\[
-\log a\le s_i\le \log b,
\]

so `C_{a,b}` is compact.

### Radial monotonicity

Fix a nonzero direction `v in H` and put `s=rv`, `r>=0`. Then

\[
\frac{d^2}{dr^2}E_+(rv)=\sum_i v_i^2e^{rv_i}>0,
\]

while

\[
\frac d{dr}E_+(rv)\bigg|_{r=0}=\sum_i v_i=0.
\]

Therefore `E_+(rv)` is strictly increasing for every `r>0`. The same argument applies to `E_-(rv)` because its first derivative at `0` is `-sum v_i=0` and its second derivative is positive.

Consequently every ray from the origin meets `C_{a,b}` in one interval

\[
\{rv:0\le r\le R(v)\},
\]

with a unique first boundary point when the pair is nontrivial. This is the first useful monovariant: there is no need to search an arbitrary two-dimensional cloud of `(t_1,t_2)` values.

Now define a third generalized radius

\[
\lambda_i:=\frac12(e^{s_i/2}+e^{-s_i/2})=\cosh(s_i/2),\qquad i=1,2,3.
\]

A direct expansion using `s_1+s_2+s_3=0` gives the exact identity

\[
\boxed{
8\lambda_1\lambda_2\lambda_3
=2+E_+(s)+E_-(s).
}
\tag{4.3}
\]

Indeed with `x_i=e^{s_i/2}` and `x_1x_2x_3=1`, expanding `prod_i(x_i+x_i^{-1})` yields the two constant terms, the three `z_i`, and the three `z_i^{-1}`.

Combining (3.1), (4.1), and (4.3), every Xi-feasible point obeys

\[
\boxed{
\lambda_1\lambda_2\lambda_3\le q.
}
\tag{4.4}
\]

Moreover along every nonzero ray the product in (4.4) is strictly increasing, since it equals `(2+E_++E_-)/8`.

This is a real structural gain: the natural monovariant is not either Xi defect separately but the **three-radius product**.

## 5. Simultaneous saturation is a cubic discriminant condition

Equality in (4.4) occurs exactly when both Xi feasibility constraints saturate:

\[
E_+(s)=b,\qquad E_-(s)=a.
\tag{5.1}
\]

Because `z_1z_2z_3=1`, the numbers `z_i` then have elementary symmetric functions

\[
z_1+z_2+z_3=b,
\qquad
z_1z_2+z_1z_3+z_2z_3=a,
\qquad
z_1z_2z_3=1.
\]

Hence they are the roots of

\[
P_{a,b}(z)=z^3-bz^2+az-1.
\tag{5.2}
\]

Its discriminant is

\[
\Delta(a,b)=a^2b^2-4a^3-4b^3-27+18ab.
\tag{5.3}
\]

### Proposition 5.1 — exact double-boundary criterion

For `a,b>0`, there exists a positive triple `(z_1,z_2,z_3)` with product one and elementary sums `(b,a)` if and only if

\[
\boxed{\Delta(a,b)\ge0.}
\tag{5.4}
\]

#### Proof

If such a positive triple exists, (5.2) has three real roots, so its discriminant is nonnegative.

Conversely, if `Delta>=0`, the cubic has three real roots counting multiplicity. Their product is one. They cannot consist of one positive root `r` and two negative roots `-u,-v` with `u,v>0`: the positive sum condition `b=r-u-v>0` gives `r>u+v`, and then

\[
a=uv-r(u+v)<uv-(u+v)^2<0,
\]

contrary to `a>0`. All three roots are therefore positive. Their Vieta sums are exactly `(b,a,1)`.

This proves the criterion.

### Why this matters

The two scalar Aleksandrov–Fenchel consequences

\[
a^2\ge3b,
\qquad
b^2\ge3a
\tag{5.5}
\]

do **not** imply (5.4). The exact rational pair

\[
a=\frac{61}{20},\qquad b=\frac{31}{10}
\]

satisfies

\[
a^2-3b=\frac1{400}>0,
\qquad
b^2-3a=\frac{23}{50}>0,
\]

but

\[
\boxed{\Delta(a,b)=-\frac{2699}{40000}<0.}
\tag{5.6}
\]

I do **not** claim that this rational pair is realized by some convex-body pair; the point is narrower and rigorous: any proof of the cubic selector based only on the two scalar AF inequalities is insufficient. Additional geometric information about realizable mixed-volume pairs would be needed.

This is the counterexample-oriented negative result of B13/B19: it kills the tempting claim that ordinary AF automatically makes both Xi constraints simultaneously tight.

## 6. B19 — an explicit cubic-root selector, and why it repairs the previous box failure

When `Delta(a,b)>=0`, Proposition 5.1 gives a canonical algebraic candidate: take the three positive roots `z_1,z_2,z_3` of (5.2), choose any two as `(t_1,t_2)`, and use the third as `(t_1t_2)^{-1}`. This selector satisfies both Xi feasibility inequalities with equality and maximizes the three-radius product at

\[
\lambda_1\lambda_2\lambda_3=q.
\tag{6.1}
\]

It is fundamentally different from the AF point that failed in the previous run.

### Proposition 6.1 — Xi's generalized-radii inequalities hold exactly for every aligned equal-volume box pair

Let

\[
K=\prod_{i=1}^3[-a_i,a_i],
\qquad
L=\prod_{i=1}^3[-r_i a_i,r_i a_i],
\qquad r_1r_2r_3=1.
\tag{6.2}
\]

Then Xi's pair `(X_-),(X_+)` is satisfied exactly by

\[
\boxed{t_1=r_1^{-1},\qquad t_2=r_2^{-1}}
\tag{6.3}
\]

(and any permutation of the indices).

#### Proof

Normalize the common volume to one. For boxes, coefficient comparison in `|K+sL|` gives

\[
a=r_1+r_2+r_3,
\qquad
b=r_1^{-1}+r_2^{-1}+r_3^{-1}.
\tag{6.4}
\]

With `z_i=r_i^{-1}`, we have `z_1z_2z_3=1`, `sum z_i=b`, and `sum z_iz_j=a`. Therefore (6.3) saturates both inequalities (3.2).

Set

\[
c_i:=\frac12\left(\sqrt{r_i}+\frac1{\sqrt{r_i}}\right).
\]

The midpoint logarithmic body is the coordinatewise geometric box, so `m=|M_0|=1`. The ordinary midpoint body has coordinate ratios `c_i` relative to `M_0`, hence

\[
q=|M_1|=c_1c_2c_3
\tag{6.5}
\]

and the box mixed-volume polynomial gives

\[
A=\frac{3V(M_0,M_0,M_1)}{|M_0|}=c_1+c_2+c_3.
\tag{6.6}
\]

For the selector (6.3), `lambda_i=c_i` for all three generalized radii because `lambda(t)=lambda(t^{-1})`. Thus

\[
\frac q{\lambda_1\lambda_2}=\lambda_3,
\]

and, since `m=1`, both `(X_-)` and `(X_+)` reduce to the same identity

\[
A=\lambda_1+\lambda_2+\lambda_3.
\]

This proves the proposition.

The proof is preserved under one common invertible linear map, so it also applies to common-GL images of aligned boxes.

### Exact repair of the prior AF-point witness

The previous run used

\[
(r_1,r_2,r_3)=(4,2,1/8)
\]

to prove that Xi's AF-guaranteed point fails `(X_-)`. The new selector instead takes

\[
(t_1,t_2)=(1/4,1/2),
\]

with third radius `8`. Exactly,

\[
q=\frac{135}{64},
\qquad
\lambda_1+\lambda_2+\lambda_3
=\frac54+\frac{15}{8}\sqrt2,
\qquad
\lambda_1\lambda_2\lambda_3=\frac{135}{64}.
\]

So the very same equality-case box that defeated the AF selector is solved exactly by the cubic-root selector. This confirms that the previous obstruction was to the **selector**, not to Xi's conjecture.

## 7. B27 — swap the selector formula for a compact variational existence problem

The original form asks, for every body pair, to somehow guess `(t_1,t_2)`. The log-coordinate reduction allows the quantifier to be swapped into a compact optimization problem.

For `s in C_{a,b}`, let

\[
\lambda_i(s)=\cosh(s_i/2).
\]

For each omitted index `k`, let `{i,j}={1,2,3}\setminus\{k\}` and define

\[
F_c^{(k)}(s)
:=\lambda_i(s)+\lambda_j(s)
+\frac{c}{\lambda_i(s)\lambda_j(s)}.
\tag{7.1}
\]

Permuting the three `z_i` simply corresponds to choosing which two generalized radii are called `(t_1,t_2)`. Therefore Xi's selector statement is equivalent to

\[
\exists s\in\mathcal C_{a,b},\ \exists k\in\{1,2,3\}:\quad
F_{q/m}^{(k)}(s)\le A\le F_q^{(k)}(s).
\tag{7.2}
\]

Equivalently define the compact min-max defect

\[
\boxed{
\Psi(K,L)
:=\min_{s\in\mathcal C_{a,b}}\min_{k=1,2,3}
\max\left\{
F_{q/m}^{(k)}(s)-A,
A-F_q^{(k)}(s)
\right\}.
}
\tag{7.3}
\]

Then Xi's three-dimensional conjectural selector is exactly

\[
\boxed{\Psi(K,L)\le0.}
\tag{7.4}
\]

This is not a numerical replacement for a proof. It is an exact variational restatement with a compact, convex feasible domain. Together with the radial lemma, it gives a deterministic search architecture:

1. parameterize a unit direction `v(phi)` in the plane `sum s_i=0`;
2. find the unique radial cap `R(phi)` where the first of `E_+=b` and `E_-=a` becomes tight;
3. optimize (7.3) over `0<=r<=R(phi)` and the three omitted indices.

For a theorem one still needs an analytic inequality forcing `Psi<=0`; finite sampling of `(phi,r)` would not suffice.

For aligned equal-volume boxes, Proposition 6.1 gives `Psi=0` exactly at the cubic-root selector.

## 8. What moved mathematically, and what did not

### Source metric

No movement:

\[
B_{\rm cart}:\infty\to\infty,
\qquad
 d_{\rm full}:2\to2.
\]

### Auxiliary progress, kept separate

1. Xi's two-dimensional positive feasible region was rewritten exactly as a compact `S_3`-symmetric convex set in the zero-sum log plane.
2. Along every nonzero ray, **both** feasibility functions and the three-radius product increase strictly; there is a unique radial cap.
3. The exact identity
   \[
   8\prod_i\lambda_i=2+E_++E_-
   \]
   converts the Minkowski-sum volume `q=(2+a+b)/8` into a sharp product cap `prod lambda_i<=q`.
4. Existence of a point saturating both Xi feasibility inequalities is characterized exactly by one cubic discriminant `Delta(a,b)>=0`.
5. Pairwise scalar AF inequalities alone do not force that discriminant condition; the exact rational diagnostic (5.6) proves this.
6. A new **cubic-root selector** solves Xi's generalized-radii inequalities exactly for every aligned equal-volume box pair and repairs the previous AF-point failure.
7. The full three-dimensional selector is reduced exactly to the compact min-max defect `Psi` in (7.3).

These are auxiliary structural results. They do not prove unrestricted dimension-three log-BM.

## 9. Exact checker actually run

The algebraic finite core was checked with exact SymPy arithmetic before persistence. It verifies:

- the product identity (4.3),
- the box volume identity `q=c_1c_2c_3`,
- exact saturation by `t_i=1/r_i`,
- exact repair of the prior `(4,2,1/8)` witness,
- the rational AF-only / negative-discriminant diagnostic.

Artifacts:

- `artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T02-01-47Z__xi_radial_selector_exact.py` @ `95a42b170ea45fc21cf724b71cad8c892b7becb6`;
- `artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T02-01-47Z__xi_radial_selector_exact.out` @ `fcfea9358ffd2afe66e285cbb188c6f0041801a0`;
- terminal line: `ALL_EXACT_CHECKS_PASS = True`.

This checker is a self-check for the finite algebraic identities only. The convexity/radial and box propositions are proved on the page above.

## 10. Exact obstruction after this run

The previous opaque obligation

> choose `(t_1,t_2)` satisfying Xi's two inequalities

is now replaced by the sharper statement

\[
\boxed{
\Psi(K,L)\le0
\quad\text{for every equal-volume origin-symmetric }K,L\subset\mathbb R^3,
}
\tag{10.1}
\]

with `Psi` given by the explicit compact optimization (7.3).

The new information is that the generalized-radii domain itself is no longer mysterious: its geometry, radial parametrization, product cap, and double-boundary locus are explicit. The remaining difficulty sits in the **cross-geometry quantities** `m=|M_0|` and `A=3V(M_0,M_0,M_1)/m`. Neither `a,b` nor ordinary AF inequalities control them strongly enough to force (10.1).

What a proof must contain that this run still lacks is therefore one inequality linking `(m,A)` to the log-coordinate feasible region. A sufficient source-level lemma would be any body-geometric estimate that forces the min-max defect (7.3) nonpositive. Without such a link, further algebra on `(a,b)` alone cannot close the target.

## 11. Section-I lifecycle decision

This is the **second** stuck/recovery run on the current BLYZ target. The owner protocol allows at most two such recoveries. Therefore the next invocation must not produce a third no-movement Xi lemma.

If the next run finds an immediate source-level movement mechanism connecting `(m,A)` to `C_{a,b}`, it may record that movement. Otherwise it must preserve this handoff and rotate to a fresh unowned hard target in the HARD7-01 lane, releasing the canonical BLYZ claim according to the repository protocol rather than silently continuing.

If one last direct attempt is mathematically justified before rotation, it must use a **different** triple from this run; candidate unused moves are **B1 / B11 / B29**: recast `(m,A)` through the Hilbert/centro-affine operator, dualize the min-max defect, and add the boundary at infinity/degenerate-body limit. These are not executed here.

## 12. Runtime/model and scheduler capability honesty

The actual model exposed for this invocation is **GPT-5.6 Sol**. The applied reasoning-effort level is **UNVERIFIED**. I therefore do not claim GPT-6 maximum.

The scheduler interface available to this worker still exposes title/prompt, schedule or relative start, timing mode, enabled state and task identity, but no binding model-family selector, no reasoning-effort selector and no guaranteed-duration field. Making GPT-6/maximum enforceable would require product/backend support for persistent authorized model/effort routing fields plus authenticated per-run telemetry.

The recorded P26 `You cannot modify this task` event remains an authorization-context restriction. The lawful workaround is to use the task-owning authorized product/workspace/API/admin context or platform support; it is not to bypass permissions or create a duplicate task. No scheduler modification was attempted.

## 13. Ledger delta

```yaml
ledger_delta:
  worker: HARD7-01
  target: LOG-BRUNN-MINKOWSKI-SYMMETRIC
  source_status: OPEN
  research_status: PARTIAL_STUCK2
  runtime_model: GPT-5.6 Sol
  reasoning_level: UNVERIFIED
  fixed_metric: B_cart
  before: infinity
  after: infinity
  full_source_dimension_before: 2
  full_source_dimension_after: 2
  movement: NO_MOVEMENT
  methods: [B13, B19, B27]
  section_I_recovery_number: 2
  auxiliary_progress:
    xi_log_feasible_region: compact_convex_S3_symmetric
    radial_monovariant: proved
    radius_product_identity: proved
    double_boundary_criterion: Delta_ab_ge_0
    AF_only_counterdiagnostic: [61/20, 31/10, -2699/40000]
    cubic_root_selector_boxes: proved
    full_selector_minmax_defect: Psi_exact_reduction
  source_theorem_claimed: false
  artifacts:
    - artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T02-01-47Z__xi_radial_selector_exact.py
    - artifacts/hard7_2026-09-18/HARD7-01/2026-09-20T02-01-47Z__xi_radial_selector_exact.out
  claim_changed: false
  shared_roots_edited: false
  schedule_changed: false
  next_no_movement_action: HANDOFF_AND_ROTATE
```

GitHub-only boundaries were preserved: no email, Drive, public posting, permission change, workflow execution, force-push, shared-ledger rewrite, new schedule, or modification of another schedule was performed.
