Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; there is no surviving frozen counterexample candidate, so the source four-obligation counterexample metric is presently NOT SCOREABLE and the historical `2/4` is only a retirement carry. The latest coordinator state admits P0219 to a different exclusive native slot and creates no free R15 successor, so R15 admission remains `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, an exact pair-smoothing theorem reduces the repaired heterogeneous `k=2` quadratic candidate to equal-support orbit strata, and a new rational bilinear majorant certifies every small–big two-coordinate face. Methods actually used on this new route: #14 FIND THE GROUP ACTING, #18 SAY IT IN ANOTHER LANGUAGE, #30 DO ONE DIRECTION AT A TIME. The long F0111 screening chain has already reused much of the 30-label menu; I do not falsely call these labels globally unused, but this route is different from the preceding #3/#24/#25 run.**

# R15 retained screen — orbit smoothing and a rational mixed-face kernel

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new Talagrand mathematics below is **SELF_CHECK_ONLY**. Nothing here reopens I0076, promotes F0111 from `PENDING / NOT READY`, claims publication novelty, or satisfies the two-independent-auditor closure rule.

## 1. Continuity, source fidelity, repository state, and admission

I continued from the newest complete own report

`runs/R15/20260919_0358Z_successor_screen_f0111_smallface_cone_y74c.md`

rather than restarting. I refreshed the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

and the newest neighboring F0111 handoff visible from R20,

`runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`.

The latest coordinator census read this run is `operations/task_health/runs/2026-09-19T045200Z/status.md`. It records a real new CLOSABLE admission, P0219, but that candidate is already exclusively assigned to native slot `6aa7ebbe26308191a40003a950a2307a`; the report also says the remaining successor gates still have no accepted successor and no root queue mutation creating a free CLOSABLE reserve. Thus no source-current, ownership-clear free successor is available to R15 in this run. I create no claim and edit no shared root.

### Exact Burdzy–Scheutzow source remains unchanged and retired-handed-off

I rechecked the primary PDF, Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.

- FBM: random origins `S_n -> -infinity` a.s. from each of which the complete centered future is standard Brownian motion.
- BBM: time reversal is FBM.
- 2BM: at one random origin the complete centered future and past are **independent standard Brownian motions**.
- Problem 7.2 assumes FBM + BBM and only independence of the two complete centered half-paths at an arbitrary random real time `T`. It does **not** assume `T` is a stopping time and does not separately assume either seam half is Brownian.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES candidate had the desired independent seam but was proved actually 2BM. There is no surviving frozen candidate on which a third or fourth source obligation can honestly be scored. Problem 7.5 remains excluded.

Fresh dated exact-title / `Problem 7.2` / later-author searches on 2026-09-19 again recovered the original paper and citation trail, but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only.

### Retained F0111 screen and fresh literature

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 / Problem 10.9. It asks whether one universal `gamma>0` puts every cardinality threshold `{X: |X|>=k}` into `C_gamma`, where the certificate at each base is a zero-constant multilinear polynomial with nonnegative coefficients that globally majorizes the threshold hazard and satisfies the scaled budget.

Fresh 2026-09-19 searches recovered Ascoli–He–Park–Talagrand, arXiv:2608.11183 (submitted 2026-08-11), which reformulates the broader discrete convexity conjecture through `k`-thresholds and proves substantial graph-property classes, and Jinyoung Park, arXiv:2609.14681 (2026-09-13), which gives a dimension-free comparison **toward** the conjecture using the fractional result. I found no accessible primary statement claiming the exact Definition-10.1 / Problem-10.9 positive-multilinear theorem screened here. Novelty/openness therefore remains **UNVERIFIED**.

## 2. Carried repaired candidate

For the cardinality-two threshold write

`F_n(t)=sum_i t_i - log(1+sum_i(exp(t_i)-1))`.                         (2.1)

The preceding two runs study the fully interior two-level bases

`q^(epsilon)=(epsilon,...,epsilon,b,b)`, `b=log 2`,                    (2.2)

with fourteen small coordinates, and the `theta=4/5` repaired positive quadratic exact-contact candidate. By symmetry it has the form

`P_epsilon(x,y,z)`
` = alpha_s(epsilon) X + beta_ss(epsilon) Q`
`   + alpha_b(epsilon)(y+z) + beta_bb(epsilon) y z`
`   + beta_sb(epsilon) X(y+z)`,                                       (2.3)

where

`X=sum_{i=1}^{14} x_i`, `Q=sum_{i<j}x_i x_j`.                         (2.4)

The carried limits are

`alpha_s -> 2/3-(4/9)log2`,
`beta_ss -> 13/45`,
`alpha_b -> 5/3-log3/log2`,
`beta_bb -> [log3-(4/3)log2]/(log2)^2`,
`beta_sb -> 2/9`.                                                      (2.5)

The preceding report proved the entire arbitrary small-only face globally. What remained was the genuinely mixed small/big geometry.

## 3. Method #14 — exact pair-smoothing / orbit-reduction theorem

The first new theorem is independent of the special coefficients.

### Theorem R15-F0111-PAIR-SMOOTH

Let `P` be any quadratic polynomial which is symmetric in a coordinate pair `(u,v)` and whose `uv` coefficient is `beta>1/6`. Hold every other coordinate fixed and hold the pair sum `s=u+v` fixed. Then the function

`(P-F_n)`

restricted to `u,v>=0`, `u+v=s`, attains its minimum only at

`u=v=s/2`                                                     (3.1)

or at an endpoint

`{u,v}={0,s}`.                                                (3.2)

In particular, at a global minimizer under a fixed orbit total, all positive coordinates in any symmetric orbit with pair coefficient `>1/6` are equal.

### Proof

Write

`u=s/2+x`, `v=s/2-x`, `0<=x<=s/2`.                           (3.3)

All terms of `P` except `beta uv` are affine in `u+v` when the outside coordinates are frozen, hence are constant on this segment. Since

`uv=s^2/4-x^2`,                                               (3.4)

the polynomial contributes `-beta x^2` up to an additive constant.

For the target, if the outside coordinates are `t_k`, then

`1+sum_i(exp(t_i)-1)=C+exp(u)+exp(v)`
`                    =C+2 exp(s/2) cosh x`,                  (3.5)

where

`C=sum_out exp(t_k)-(n-1)>=-1`.                               (3.6)

Thus, after discarding another additive constant, the gap is

`H(x)=-beta x^2+log(cosh x+A)`,                               (3.7)

with

`A=C/[2 exp(s/2)]>=-1/2`.                                    (3.8)

For `x>0`, set

`R_A(x)=sinh x/[x(cosh x+A)]`.                                (3.9)

Then

`H'(x)=x[R_A(x)-2 beta]`.                                     (3.10)

Suppose `x>0` is an interior critical point. Then `R_A(x)=2 beta`. We show it cannot be a local minimum.

A direct differentiation shows that `R_A'(x)>=0` is equivalent to

`A >= A_c(x):=[sinh x cosh x-x]/[x cosh x-sinh x]`.          (3.11)

For fixed `x`, `R_A(x)` decreases in `A`. Hence under `R_A'(x)>=0`,

`R_A(x)<=R_{A_c(x)}(x)`
`       =[x coth x-1]/x^2`.                                  (3.12)

The elementary inequality

`x coth x <= 1+x^2/3`                                        (3.13)

holds for every `x>0`: it is equivalent to

`(3+x^2)sinh x-3x cosh x>=0`,                                (3.14)

whose derivative is

`x(x cosh x-sinh x)>=0`; the latter bracket starts at zero and has derivative `x sinh x>=0`.

Therefore `R_A'(x)>=0` would imply `R_A(x)<=1/3`. But at a critical point

`R_A(x)=2 beta>1/3`,                                         (3.15)

a contradiction. Hence every nonzero interior critical point has `R_A'(x)<0`, and from (3.10)

`H''(x)=x R_A'(x)<0`.                                        (3.16)

Every nonzero interior critical point is thus a strict local maximum. A minimum on `[0,s/2]` can occur only at `x=0` or `x=s/2`. QED.

### Apply it to the repaired two-level candidate

The exact checker below certifies

`13/45>1/6`,                                                  (3.17)

and, using rigorous rational atanh-series bounds for `log2` and `log3`,

`[log3-(4/3)log2]/(log2)^2 > 1/6`.                           (3.18)

By (2.5) and continuity, for all sufficiently small positive `epsilon`, both actual within-orbit coefficients `beta_ss(epsilon)` and `beta_bb(epsilon)` are strictly above `1/6`.

Consequently, fix the total small mass `X` and total big mass `Y=y+z`. If the repaired candidate ever fails global majorization, minimize its gap on the compact product of the two fixed-total simplices. At such a minimizer:

- exactly `r` small coordinates are positive, for some `1<=r<=14`, and all `r` equal `X/r`;
- the two big coordinates are either equal `Y/2,Y/2` or one is zero.

So the arbitrary sixteen-variable mixed verification collapses **exactly** to finitely many equal-support strata. The previous run already settles `Y=0` for every small vector, so a new failure must genuinely use a big coordinate.

## 4. Method #18 — a new rational global mixed-face majorant

The second theorem solves the two-coordinate kernel with coefficients that sit strictly below the limiting small/big coefficients.

Let

`Phi(u,v)=u+v-log(exp(u)+exp(v)-1)`.                          (4.1)

### Theorem R15-F0111-MIXED-RATIONAL

For every `u,v>=0`,

`Phi(u,v)`
` <= (16/45)u + (2/25)v + (21/100)uv`.                       (4.2)

The swapped inequality is of course also valid.

### Proof

Fix `v` and put

`p=1-exp(-v)`.                                                (4.3)

Then

`Phi(u,v)=-log(1-p+p exp(-u))`.                              (4.4)

For `0<=w<=p`, the exact convex-conjugate identity is

`sup_{u>=0}[Phi(u,v)-w u]=D(w||p)`,                          (4.5)

where `D` is binary relative entropy. If `w>=p`, the supremum is zero because the derivative of `Phi` at `u=0` is `p` and `Phi` is concave in `u`.

Set

`a=16/45`, `b=2/25`, `c=21/100`,
`L(v)=a+c v`.                                                 (4.6)

When `L(v)>=p`, (4.2) is immediate. Assume `L(v)<p` and write

`h(v)=p-L(v)=29/45-(21/100)v-exp(-v)>0`.                     (4.7)

The standard inequality `D<=chi^2` for two Bernoulli laws gives

`D(L(v)||p) <= h(v)^2/[p(1-p)]`.                             (4.8)

It therefore suffices to prove

`h(v)^2 <= b v p(1-p)`.                                      (4.9)

The finite rational exponential inequalities used below are all archived by the exact checker in Section 6.

First, `h>0` forces

`2/3 < v < 14/5`.                                             (4.10)

Indeed `h'(v)=exp(-v)-21/100` is strictly decreasing. At `v=2/3`, the checker gives

`51/100 < exp(-2/3) < 13/25`,                                (4.11)

so

`h(2/3)=227/450-exp(-2/3)<0`,                                (4.12)

and `h'(2/3)>0`. At `v=14/5`, it gives

`3/50 < exp(-14/5) < 1/16`,                                 (4.13)

so

`h(14/5)=127/2250-exp(-14/5)<0`,                             (4.14)

and `h'(14/5)<0`. Concavity then gives (4.10).

The maximum of `h` occurs where `exp(-v)=21/100`, namely at `v=log(100/21)`. Since the checker proves

`log(100/21)>31/20`,                                         (4.15)

we have

`h(v)<=29/45-(21/100)(1+31/20)`
`     =1961/18000 < 11/100`.                                 (4.16)

Thus

`h(v)^2<121/10000`.                                          (4.17)

It remains to lower-bound the right side of (4.9). Put

`f(v)=v exp(-v)(1-exp(-v))`.                                 (4.18)

Its derivative has the sign of

`g(v)=1-v+(2v-1)exp(-v)`.                                   (4.19)

Moreover

`g'(v)=-1+(3-2v)exp(-v)<0`                                  (4.20)

throughout `[2/3,14/5]`: on `[2/3,3/2]`, use `(3-2v)<=5/3` and `exp(-v)<13/25`; beyond `3/2` the second term is nonpositive. Hence `f` has at most one interior critical point, necessarily a maximum, so its minimum on this interval is attained at an endpoint.

Using (4.11),

`f(2/3)>(2/3)(13/25)(12/25)=104/625>121/800`.               (4.21)

Using (4.13),

`f(14/5)>(14/5)(3/50)(15/16)=126/800>121/800`.              (4.22)

Therefore throughout the possible `h>0` region,

`b v p(1-p)=(2/25)f(v)>121/10000>h(v)^2`.                   (4.23)

Equations (4.8)--(4.23) imply `D(L(v)||p)<=bv`, hence (4.2). QED.

### Consequence for the actual repaired candidate

The limiting coefficients satisfy strict rational margins:

`alpha_s^* > 16/45`,                                         (4.24)
`alpha_b^* > 2/25`,                                          (4.25)
`beta_sb^*=2/9 > 21/100`.                                    (4.26)

For (4.24), `log2<7/10` suffices and is exactly checked. For (4.25),

`5/3-log3/log2 >2/25`

is equivalent to

`3^75 < 2^119`,                                               (4.27)

which the checker verifies by exact integer arithmetic. Equation (4.26) is rational.

By continuity, for every sufficiently small positive `epsilon` the **actual** repaired candidate has coefficients at least the three rational coefficients in (4.2). Hence every coordinate face with exactly one small and one big coordinate active is globally certified. This is new beyond the previous all-small-face theorem.

## 5. Method #30 — exact residual reduction for the one-big branch

The pair-smoothing theorem lets us state the next blocker without any high-dimensional ambiguity.

Suppose exactly `r` small coordinates are positive and equal to `x`, and one big coordinate is positive with value `y`. Define

`g_r(x)=log(1+r(exp(x)-1))`,                                  (5.1)
`F_r(x)=r x-g_r(x)`,                                         (5.2)
`Delta_r(x)=r alpha_s x + C(r,2) beta_ss x^2-F_r(x)`,        (5.3)
`w_r(x)=alpha_b+r beta_sb x`,                                (5.4)
`p_r(x)=1-exp(-g_r(x))`.                                     (5.5)

Here the coefficients are those of the fixed repaired `P_epsilon` under consideration.

The exact block identity gives

`F_{r+1,2}(x,...,x,y)=F_r(x)+Phi(g_r(x),y)`.                 (5.6)

Therefore the gap on this entire two-parameter branch is

`Delta_r(x)+w_r(x)y-Phi(g_r(x),y)`.                          (5.7)

Taking the exact conjugate in `y` collapses the quantifier over `y`:

`sup_{y>=0}[Phi(g_r(x),y)-w_r(x)y]`
` = 0`, if `w_r(x)>=p_r(x)`,
` = D(w_r(x)||p_r(x))`, if `0<=w_r(x)<p_r(x)`.              (5.8)

Thus the **entire one-big branch for support size `r` is globally valid iff**

`Delta_r(x) >= H_r(x)` for every `x>=0`,                     (5.9)

where `H_r` is the right side of (5.8).

For `r=1`, Theorem MIXED-RATIONAL already verifies the branch for sufficiently small `epsilon`. The unresolved one-big part of the repaired candidate is therefore reduced to thirteen explicit scalar inequalities, `r=2,...,14`.

For the two-big branch, pair smoothing reduces the problem to the fourteen surfaces with `r` equal positive small coordinates and `y=z`; there is no remaining asymmetric small-coordinate search. This is the next place to attack rather than running another 16-dimensional SDP or grid.

## 6. Exact checker and what it certifies

Idea and proofs were written before code. I then wrote and executed

`artifacts/R15/f0111_orbit_smoothing_mixedface_k75v.py`

and archived the exact output at

`artifacts/R15/f0111_orbit_smoothing_mixedface_k75v.out`.

The checker uses only `fractions.Fraction`, finite Taylor sums with a rigorous geometric tail for exponentials, the positive atanh series with a rigorous tail for logarithms, and exact integer arithmetic. It certifies every finite rational/transcendental inequality invoked above, including the `beta_bb>1/6` smoothing margin and ends

`ALL_EXACT_CHECKS_PASS`.

No numerical path sampling or floating optimization is used as verification of a Brownian law or of the Talagrand theorems.

## 7. What moved and what did not

The Burdzy–Scheutzow native metric did not move and is not restarted after retirement. F0111 remains

`PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED`.

The retained-screen movement is nevertheless substantive:

1. the repaired candidate's arbitrary mixed search is reduced exactly by an orbit T-transform theorem rather than numerically;
2. every small–big two-coordinate face is now globally certified by the rational majorant (4.2);
3. the remaining one-big branch is a finite family of scalar KL inequalities rather than a two-dimensional or sixteen-dimensional search;
4. the arbitrary small-only face remains fully settled by the preceding universal quadratic-cone theorem.

The next useful attack is therefore **not** another local Hessian calculation. It is to prove or refute (5.9) for `r=2,...,14`, then treat the equal-two-big surfaces. A failure there would give an explicit analytic counterexample to this repaired `C_1` candidate; success would produce a full global majorant for a genuinely interior heterogeneous base family.

## 8. Scheduler/model/authorization truth

The scheduler limitation is still unchanged. The exposed task interface provides identity/title, prompt, schedule/timing, enabled state and notification/email state, but no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort receipt, and no guaranteed hour-long execution control. GPT-6/maximum is therefore still prompt-only here.

The historical P26 `You cannot modify this task` event was an authorization-context boundary recorded in `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`. Root `RESULTS.md` records that a later authorized P/C context successfully performed the full P26 update. Thus the lawful workaround is an owning/authorized context or an owner/admin product/API/support surface that exposes the requested controls; no duplication, permission bypass, or scheduler change was attempted in this run.

## ledger_delta

```yaml
ledger_delta:
  worker: R15
  source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), Problem 7.2 / I0076"
  native_target: "FBM + BBM + source-exact independent centered half-processes at arbitrary random real T => 2BM?"
  native_metric:
    name: "four source-matching obligations for one frozen counterexample candidate"
    before: NOT_SCOREABLE_NO_LIVE_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_LIVE_FROZEN_CANDIDATE
    historical_retirement_carry: "2/4 positive-route handoff value; not a live candidate score"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: "frozen at mandatory six-run handoff"
  admission:
    free_r15_closable_before: 0
    free_r15_closable_after: 0
    note: "P0219 newly admitted elsewhere and already exclusively owned; not free R15 inventory"
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9 / F0111"
    status: "PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
    movement:
      - "proved pair-smoothing/equal-or-delete theorem for any symmetric quadratic orbit with beta>1/6"
      - "reduced repaired 16-variable candidate to equal-support small strata and equal-or-deleted big pair"
      - "proved global rational mixed kernel Phi(u,v)<=16u/45+2v/25+21uv/100"
      - "certified all small-big two-coordinate faces for sufficiently small positive epsilon"
      - "reduced one-big branch to 13 unresolved scalar KL inequalities r=2,...,14"
  tried_moves:
    - 14
    - 18
    - 30
  remaining_obligation: "prove/refute the scalar one-big KL inequalities for r=2,...,14 and the equal-two-big strata; parent Problem 10.9 remains much broader"
  evidence:
    - "runs/R15/20260919_0358Z_successor_screen_f0111_smallface_cone_y74c.md"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "artifacts/R15/f0111_orbit_smoothing_mixedface_k75v.py"
    - "artifacts/R15/f0111_orbit_smoothing_mixedface_k75v.out"
  audit_ids: []
  model_requested: "GPT-6 maximum"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
```
