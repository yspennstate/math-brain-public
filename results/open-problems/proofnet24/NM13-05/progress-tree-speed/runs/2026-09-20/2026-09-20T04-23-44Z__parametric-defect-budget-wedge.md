Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6/maximum was requested, but no authenticated applied-model/reasoning-effort telemetry is exposed, so GPT-6/maximum is not claimed. SUBSTANTIVE MOVEMENT: the Lyons--Pemantle--Peres parent problem remains OPEN, but the preceding fixed `1/100` rare-tail theorem is upgraded to a parametric defect-versus-boundary theorem. For every adjacent no-leaf law `P(nu=d)=1-p, P(nu=d+1)=p`, every integer `d>=2`, and every `0<delta<=1`, strict parent-bias decrease is proved on `0<=lambda<=d-delta` whenever `p<=delta` or `1-p<=delta`. In particular `{3,4}` laws with `p<=1/10` or `p>=9/10` are certified through `lambda=2.9`, and with `p<=1/20` or `p>=19/20` through `lambda=2.95`. No simulated sign is used.**

# NM13-05 T06 — parametric endpoint-defect budget up to the minimum-degree boundary

Date: 2026-09-20.  
Repository: private `yspennstate/math-open-problems`, branch `master`.  
Own root: `proofnet24/NM13-05/progress-tree-speed`.  
Parent target: T06 / P0066, Lyons--Pemantle--Peres monotonicity of biased-walk speed on a supercritical Galton--Watson tree without leaves.  
Status: **PARTIAL / OPEN parent; NEW RESTRICTED THEOREM CANDIDATE pending later independent review.**

## 1. Compact continuity handoff

The controlling instruction is `operations/PROGRESS20_2026-09-20.md`; current LIVE20 assigns NM13-05 to T06 by escape-probability/regeneration coupling, complementary to P01's analytic regeneration-derivative route.

Historical P0066 status remains `attempted_unsolved`. The old attempt observed only that for a fixed offspring count `k`, the local radial drift

`(k-lambda)/(k+lambda)`

decreases with parent bias `lambda`; it did not control the `lambda`-dependent environment seen from the walker. That failure is preserved and is not relabelled as progress.

The immediate predecessor is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T03-31-00Z__adjacent-rare-tail-all-d.md`.

It proved, for every adjacent law `{d,d+1}`, the fixed strip

`p<=1/100 or p>=99/100  =>  ell'_lambda<0 on 0<=lambda<=d-1/100`.

Its unresolved route was to cross the singular boundary `lambda=d` using an occupation-weighted regeneration sensitivity estimate. That route remains unresolved; this report does not claim a cross-`d` result.

The latest complementary P01 report consumed is

`proofnet24/P01-progress-speed/runs/2026-09-20/2026-09-20T03-58-29Z__run-report.md`.

P01 proves broad bounded-support regions through a pairwise-Gini covariance certificate, including every law with `3<=nu<=44` through `lambda=2.01` and every law with `3<=nu<=5` through `lambda=2.7`. The present theorem is complementary: it reaches arbitrarily close to the minimum-degree boundary for adjacent endpoint mixtures, with the allowed endpoint contamination explicitly tied to the remaining distance from that boundary.

The latest relevant PROB10-06 report consumed is

`runs/prob10_2026-09-20/PROB10-06/20260920T0416Z_global_coupled_tilt_all_mixtures_1d7c5a90.md`.

It improves the all-mixture `{2,3}` endpoint to `1.8539`. It also records two failed routes useful here: differentiating the static branch-addition ratio itself is false in the required form, and a central two-type first-generation contraction has Perron radius above one. This report avoids both by keeping only the proved static branch-addition ratio and matching the singular escape budget directly to rare endpoint mass.

`POSTED.md` was checked through current repository search. No posted source-wide P0066 closure is recorded; restricted T06 theorems do not close the parent problem.

## 2. Exact offspring assumptions and bias convention

Fix an integer `d>=2` and

`P(nu=d)=1-p,   P(nu=d+1)=p,   0<=p<=1`.                       (2.1)

There are no leaves and the mean is `m=d+p>1`.

Use parent bias `lambda`:

`P(parent | nu=k)=lambda/(lambda+k)`,
`P(each fixed child | nu=k)=1/(lambda+k)`.                      (2.2)

Increasing `lambda` pushes toward the root, so the desired sign is

`ell'_lambda<0`.                                                  (2.3)

The Ben Arous--Fribergh--Sidoravicius child-bias convention is reciprocal:

`beta=1/lambda`.                                                  (2.4)

Thus for `v(beta)=ell_{1/beta}`,

`v'(beta)=-ell'_{1/beta}/beta^2`.                               (2.5)

The new region always has `lambda<=d-delta<d<=m`, so it stays inside the transient side of the source problem.

## 3. Primary-source and current-literature recovery

Recovered on 2026-09-20:

- Ben Arous--Fribergh--Sidoravicius, arXiv:1111.5865, *A proof of the Lyons-Pemantle-Peres monotonicity conjecture for high biases*. The arXiv abstract states that the child-bias speed is increasing for `beta>=717` on Galton--Watson trees without leaves.
- He--Wang--Xiang, arXiv:1610.08151, now published as He--Wang--Xiang, *The speed of a biased walk on a Galton--Watson tree without leaves is monotonic for low values of bias*, Journal of Applied Probability 62 (2025), 1044--1052, published online 5 March 2025. For minimum offspring `m_1>=2`, they prove strict parent-bias decrease on

  `0<=lambda<=m_1/(1+sqrt(1-1/m_1))`.                           (3.1)

- Bowditch--Tokushige provide differentiability/analyticity in the relevant ballistic regimes; those regularity results do not supply the missing monotonicity sign.
- Song--Liu (2026) treats regular trees and does not settle genuinely random offspring laws.

A bounded fresh web search dated 2026-09-20 recovered the 2025 low-bias publication and 2026 regular-tree paper but no checked source-wide solution and no checked theorem matching the parametric adjacent endpoint wedge below. This is bounded negative evidence only, not a novelty certificate.

## 4. Parent-problem before/after and demonstrated mechanism gain

### Parent problem

Before: **OPEN**.  
After: **OPEN**.

No theorem for all no-leaf offspring laws on the full transient interval is claimed.

### Restricted source-level scope before

For every adjacent `{d,d+1}` law the strongest NM13-05 all-`d` near-boundary theorem was the single fixed point

`p<=1/100 or p>=99/100  =>  lambda<=d-1/100`.                   (4.1)

### Restricted source-level scope after

### Theorem A — parametric endpoint-defect wedge

For every integer `d>=2`, every `0<delta<=1`, and the law (2.1), if

`p<=delta  or  1-p<=delta`,                                     (4.2)

then the parent-bias speed is strictly decreasing throughout

`0<=lambda<=d-delta`.                                            (4.3)

Equivalently, in child-bias notation,

`v'(beta)>0  for  beta>=1/(d-delta)`                             (4.4)

inside this restricted family.

Concrete new regions include

- `{3,4}`, `p<=1/10` or `p>=9/10`: strict decrease through `lambda=29/10=2.9`;
- `{3,4}`, `p<=1/20` or `p>=19/20`: strict decrease through `lambda=59/20=2.95`;
- `{2,3}`, `p<=1/20` or `p>=19/20`: strict decrease through `lambda=39/20=1.95`.

The previous `delta=1/100` theorem is exactly one slice of this new continuum.

### Mechanism gain

The previous proof treated `delta=1/100` as a fixed numerical endpoint. The new argument identifies the invariant scaling law:

> **distance to the minimum-degree singularity pays for endpoint contamination linearly.**

The escape-sensitivity budget grows like `1/delta` as `lambda` approaches `d`, while branch addition shows that the escape-tilted defect mass is at most order `delta` when the original defect mass is at most `delta`. Their product stays strictly below the deterministic radial term. This turns one fixed rectangle into an entire exact wedge.

This is an escape-probability coupling mechanism, not P01's pairwise degree-covariance route.

## 5. Exact adjacent-family derivative reduction

Work first on `1<=lambda<d`. Let `B` be the quenched probability of escaping to infinity before hitting the parent of the present vertex, and put `U=-dB/dlambda>=0`.

For conditional current offspring `k`, take iid copies `B_0,...,B_k` with corresponding `U_i`. Set

`S_k=sum_i B_i`,
`D_k=lambda-1+S_k`,

`c_k=E[(1/(k+1))*S_k/D_k]`,                                     (5.1)

`h_k=E[(1/(k+1))*sum_i(B_i+(lambda-1)U_i)/D_k^2]`.              (5.2)

Then direct differentiation gives

`c_k'=-h_k`.                                                       (5.3)

For the two-point law define

`C=(1-p)c_d+p c_{d+1}`,
`theta=p c_{d+1}/C`,
`M=d+theta`.                                                       (5.4)

Aidekon's symmetrized speed representation reduces exactly to

`ell_lambda=(M-lambda)/(M+lambda)`,                              (5.5)

hence

`ell'_lambda=2(lambda M'-M)/(M+lambda)^2`.                       (5.6)

Moreover

`theta'=theta(1-theta) Delta`,                                  (5.7)

where

`Delta=h_d/c_d-h_{d+1}/c_{d+1}`.                                (5.8)

Therefore

`M-lambda M'`
` = d+theta-lambda theta(1-theta)Delta`.                         (5.9)

Strict positivity of (5.9) is exactly the desired derivative sign.

## 6. Consumed branch-addition coupling

For `lambda>1`, let

`phi(s)=s/(lambda-1+s)`.

It is increasing, concave, and `phi(0)=0`. Comparing an iid `(d+1)`-branch sum with a `(d+2)`-branch sum, and averaging all leave-one-out sums, gives the proved bound

`(d+1)/(d+2) <= t:=c_{d+1}/c_d <=1`.                            (6.1)

Thus

`theta=p t/(1-p+p t)`,                                           (6.2)

and therefore

`theta<=p`,                                                       (6.3)

while, writing `r=1-p`,

`1-theta`
` = r/[r+(1-r)t]`
` <= (d+2)r/(d+1+r).                                             (6.4)

No derivative of (6.1) is taken; PROB10-06 already found that such a derivative comparison fails in general.

## 7. Escape-sensitivity budget at distance `delta` from `d`

The established bounded-support escape comparison for `lambda<d` gives

`B>=1-lambda/d`,
`0<=U<=B/(d-lambda)`.                                            (7.1)

The same pathwise calculation as in the predecessor yields

`Delta <= d(d-1)/[(d-lambda)(d^2-lambda)]`.                     (7.2)

Fix

`L=d-delta`, `0<delta<=1`.                                       (7.3)

The function

`lambda*d(d-1)/[(d-lambda)(d^2-lambda)]`

is increasing on `[1,L]`. Hence

`lambda Delta<=A_{d,delta}`,                                    (7.4)

where

`A_{d,delta}`
` := d(d-1)(d-delta)/[delta(d(d-1)+delta)]`.                    (7.5)

Combining (5.9) and (7.4), it is enough to lower-bound

`F(theta):=d+theta-A theta(1-theta)`,                            (7.6)

with `A=A_{d,delta}`.

## 8. Proof of Theorem A: small upper-degree contamination

Assume

`p<=delta`.                                                       (8.1)

By (6.3), `theta<=delta`. Since `1-theta<=1`,

`F(theta)`
` >= d-A theta`
` >= d-A delta`.                                                  (8.2)

Substituting (7.5) gives the exact identity

`d-A delta`
` = d^2 delta/[d(d-1)+delta]`.                                  (8.3)

This is strictly positive for every `d>=2`, `delta>0`. Therefore

`M-lambda M' >0`                                                  (8.4)

uniformly on `1<=lambda<=d-delta`, proving strict decrease there for every `p<=delta`.

The explicit derivative margin is

`-ell'_lambda`
` >= 2 d^2 delta /`
`    [(d(d-1)+delta)(2d+1-delta)^2]`.                           (8.5)

Here we used `M<=d+1` and `lambda<=d-delta` in the denominator of (5.6).

## 9. Proof of Theorem A: small lower-degree contamination

Assume

`r:=1-p<=delta`.                                                  (9.1)

By (6.4),

`eta:=1-theta`
` <= eta_0:=(d+2)delta/(d+1+delta)`.                             (9.2)

Rewrite (7.6) as

`F=d+1-eta-A eta(1-eta)`.                                        (9.3)

Dropping the nonnegative term `A eta^2`,

`F>=d+1-(A+1)eta`
` >=d+1-(A+1)eta_0`.                                             (9.4)

A direct common-denominator calculation gives

`d+1-(A+1)eta_0`
` = [d(d-1)+delta(d+1)(d^2+1)-delta^2]`
`   /[(d+1+delta)(d(d-1)+delta)]`.                              (9.5)

For `d>=2` and `0<delta<=1`, the numerator is strictly positive because

`d(d-1)>0`,
`delta(d+1)(d^2+1)-delta^2`
` =delta[(d+1)(d^2+1)-delta]>0`.                                (9.6)

Thus again `M-lambda M'>0` uniformly on the whole interval.

An explicit derivative margin is therefore

`-ell'_lambda`
` >= 2 G_high/(2d+1-delta)^2`,                                  (9.7)

where

`G_high`
` := [d(d-1)+delta(d+1)(d^2+1)-delta^2]`
`    /[(d+1+delta)(d(d-1)+delta)]`.                             (9.8)

This proves strict decrease on `1<=lambda<=d-delta` for every `1-p<=delta`.

## 10. Stitching to `lambda<1`

He--Wang--Xiang prove strict decrease on

`0<=lambda<=theta_d:=d/(1+sqrt(1-1/d))`.                        (10.1)

For every `d>=2`, `theta_d>1`. Since `0<delta<=1` implies `d-delta>=1`, their theorem covers the entire lower segment up to and beyond `1`, while Sections 8--9 cover `[1,d-delta]`. Therefore Theorem A holds on the full interval (4.3).

No unproved differentiability assertion at an endpoint is needed for the monotonicity stitching: the published theorem supplies strict monotonicity below the overlap, and (5.6)--(9.8) give a strict derivative sign on the upper compact interval.

## 11. Exact arithmetic checks

The reusable checker is

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T04-23-44Z__parametric-defect-budget-wedge-check.py`.

Actual executed output is archived at

`proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T04-23-44Z__parametric-defect-budget-wedge-check.out`.

The checker uses only exact rational arithmetic. It verifies the algebraic identities in (8.3) and (9.5) on 693 representative `(d,delta)` pairs as a sanity check and prints exact margins for the `{3,4}` examples. The theorem itself is proved symbolically above; the finite grid is not used as proof.

For `d=3`, `delta=1/10`, the exact values are

`A=1740/61`,
`G_small=9/61`,
`G_high=999/2501`,                                               (11.1)

and on `1<=lambda<=29/10`,

`-ell'_lambda >= 200/32269`  on `p<=1/10`,                      (11.2)

`-ell'_lambda >= 22200/1323029` on `p>=9/10`.                   (11.3)

For `d=3`, `delta=1/20`,

`-ell'_lambda >= 7200/2337841` on `p<=1/20`,                    (11.4)

`-ell'_lambda >= 2559200/189365121` on `p>=19/20`,              (11.5)

through `lambda<=59/20`.

The archived output ends

`ALL_EXACT_CHECKS_PASS`.

No simulated derivative sign is used anywhere in the claim.

## 12. Residual obstruction and next attack

The parent problem remains open. The present wedge is still fundamentally one-sided with respect to the minimum-degree singularity: (7.1) pays `1/(d-lambda)`, so the argument cannot cross `lambda=d` for any fixed nonzero defect probability.

The precise missing mechanism is an occupation-weighted regeneration sensitivity estimate of the form

`bad sensitivity <= (probability a regeneration block actually encounters degree d) * finite local cost`,

rather than the present pathwise worst-case charge applied to every environment. Such an estimate could plausibly cross `d` when `1-p` is sufficiently small. A future run should attack that regeneration occupation term directly; merely optimizing the rational constants in (7.5) will not cross the boundary.

There is no three-run stagnation trigger here: the last several NM13-05 substantive runs all produced strict theorem-scope gains. No rotation is invoked.

## 13. ledger_delta

```yaml
ledger_delta:
  track: NM13-05
  parent: T06
  source_id: P0066
  status_before: OPEN
  status_after: OPEN
  offspring_family: "P(nu=d)=1-p, P(nu=d+1)=p, integer d>=2"
  bias_convention:
    parent_bias: lambda
    child_bias: beta=1/lambda
  source_scope_before: "all d>=2 only fixed delta=1/100 tail slice: p<=1/100 or p>=99/100 => lambda<=d-1/100"
  source_scope_after: "for every 0<delta<=1: p<=delta or 1-p<=delta => strict parent-bias decrease on 0<=lambda<=d-delta"
  mechanism_before: "fixed-distance branch-addition endpoint retention"
  mechanism_after: "parametric defect-budget matching: 1/delta escape sensitivity times O(delta) tilted defect mass"
  demonstrated_examples:
    - "d=3, p<=1/10 or p>=9/10, lambda<=29/10"
    - "d=3, p<=1/20 or p>=19/20, lambda<=59/20"
    - "d=2, p<=1/20 or p>=19/20, lambda<=39/20"
  exact_checker: "proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T04-23-44Z__parametric-defect-budget-wedge-check.py"
  exact_output: "proofnet24/NM13-05/progress-tree-speed/runs/2026-09-20/2026-09-20T04-23-44Z__parametric-defect-budget-wedge-check.out"
  exact_output_terminal: ALL_EXACT_CHECKS_PASS
  simulated_signs_used: false
  parent_closed: false
  candidate_label: PARTIAL_RESTRICTED_THEOREM_PENDING_INDEPENDENT_REVIEW
  failed_routes_preserved:
    - "historical P0066 fixed-degree local drift did not control environment change"
    - "cross-minimum-degree occupation-weighted regeneration derivative remains unresolved"
    - "PROB10 derivative comparison for branch-addition ratio fails in general"
  next_attack: "derive an occupation-weighted regeneration sensitivity bound capable of crossing lambda=d for 1-p small"
```
