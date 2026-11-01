Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; free admission `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111 I prove, SELF_CHECK_ONLY, the full heterogeneous finite-dimensional bound `A_{n,k} in C_{1/(n-k+1)}` for every cardinality threshold. Methods #11 DUALIZE, #21 ASK WHO ELSE HAS THIS SHAPE, #30 ONE SCALE / ONE DIRECTION AT A TIME.**

# R15 retained screen — coupled Pascal certificates for cardinality thresholds

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All mathematics newly derived below is **SELF_CHECK_ONLY** unless explicitly identified as source or previously proved R15 material. The parent Talagrand Problem 10.9 is **not** marked solved: the constant obtained below is `1/(n-k+1)`, which is not uniform in `n,k`. No novelty claim is made without independent audit and a fuller citation-graph search.

## 1. Required continuity, source fidelity, and admission state

I continued from current repository state rather than the stale native title. I reread or exact-target-recovered:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- current coordinator status `operations/task_health/runs/2026-09-18T190200Z/status.md`;
- controlling I0076 handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- immediately preceding R15 report `runs/R15/20260918_1805Z_successor_screen_f0111_endpoint_gamma1_kl_r63v.md`;
- earlier Pascal-gap report `runs/R15/20260918_0858Z_successor_admission_f0111_pascal_u54.md`;
- the neighboring F0111 admission reading in `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T18-56-30Z__post-e0086-admission-delta-screen-5-f0111-endpoint.md`.

The newest coordinator evidence has one newly admitted CLOSABLE source assigned to a different native slot, but records **no additional free READY CLOSABLE target** for the remaining gates. I therefore create no successor claim. F0111 remains a retained mathematical screen, not an admitted R15 successor.

### Burdzy--Scheutzow source is unchanged and not reopened

I rechecked the primary PDF, Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958 / PTRF 160 (2014). Definition 2.1 says:

- FBM: there are random times `S_n -> -infinity` a.s. such that each complete centered future `{X_{S_n+t}-X_{S_n}:t>=0}` is standard Brownian motion;
- BBM: time reversal is an FBM;
- 2BM: there is one random time `S` at which the complete centered forward and backward half-paths are independent **standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM + independence, at some arbitrary random time `T`, of the two complete centered half-paths forces 2BM. The source does **not** require `T` to be a stopping time and does **not** assume either half at `T` is Brownian. I do not replace the statement by deterministic-time independence, a stopping-time version, Problem 7.5, or an already-posted result.

The six-run handoff remains controlling. The Theorem-6.1-derived candidate failed to provide a source-valid independent seam. The later Brownian-prefix/Bessel candidate had the seam but was proved actually 2BM. Hence no frozen counterexample candidate survives. The historical `2/4` is only the carried retirement value. I0076 stays `OPEN / PARTIAL / RETIRED-HANDOFF` and is not attacked here.

Fresh dated 2026-09-18 exact-title / `Problem 7.2` / citing-material public queries recovered the original source and no accessible later primary paper explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not an openness certificate.

## 2. Retained source problem and carried exact ingredients

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9. For hazards `t=(t_i)` let `zeta_t` be the product law with inclusion probabilities `1-exp(-t_i)`. For an up-class `A`, write

`F_A(t)=-log(1-zeta_t(A))`.

Talagrand defines `A in C_gamma` if for every base `q>=0` there is a multilinear polynomial

`P(t)=sum_{empty != I subset S} beta_I t_I`, `beta_I>=0`,

such that

`F_A(t)<=P(t)` for all `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

The source notes that `C_gamma` increases as `gamma` decreases. Proposition 10.2 gives the nonempty class in `C_1`; Proposition 10.5 gives disjoint-block composition. Problem 10.9 asks whether there is one universal `gamma>0` such that **all** cardinality thresholds

`A_{n,k}={X subset [n]: |X|>=k}`

belong to `C_gamma`.

For these thresholds write

`F_{m,k}(t)=-log P_t(N_m<k)`.

The earlier R15 Pascal report proved the exact recursion

`F_{m+1,k}(t,s)=F_{m,k}(t)+Phi(s,G_{m,k}(t))`,              (2.1)

where

`G_{m,k}=F_{m,k-1}-F_{m,k}`                                (2.2)

and

`Phi(u,v)=-log(e^{-u}+e^{-v}-e^{-u-v})`.                   (2.3)

It also proved the gap ordering

`G_{m,2}>=G_{m,3}>=...>=G_{m,m+1}>=0`.                     (2.4)

The immediately preceding R15 report proved, SELF_CHECK_ONLY, Talagrand's explicit endpoint strengthening: for every base `(u0,v0)` there are `a,b,c>=0` such that

`Phi(u,v)<=a u+b v+cuv` for all `u,v>=0`,                  (2.5)

and

`a u0+b v0+c u0v0=Phi(u0,v0)`.                             (2.6)

Moreover the construction has

`0<=b<=1`.                                                   (2.7)

For an interior base, the proof writes

`b = D_Ber(w0 || 1-e^{-v0})/v0 in (0,1)`;

at the boundary the source-valid limiting/simple certificates have `b=0` or `b=1`. Thus (2.7) is part of the actual prior construction, not an extra numerical observation.

This run asks whether (2.1) can use (2.5) **without** first majorizing the gap `G` by its own positive polynomial.

## 3. Method #11 — DUALIZE the naive gap induction: it is impossible already in two variables

A natural but wrong plan is to try to put each gap `G_{m,k}` into a `C_gamma`-like positive-polynomial class on its own.

The smallest nontrivial gap is

`G_{2,2}(u,v)=u+v-Phi(u,v)=log(e^u+e^v-1)`.                 (3.1)

### Lemma 3.1 — no standalone positive-polynomial budget exists for the first gap

Fix any interior base `q=(u0,v0)` with `u0,v0>0` and any `gamma>0`. There is no nonnegative multilinear polynomial

`Q(u,v)=a u+b v+cuv`, `a,b,c>=0`,                           (3.2)

such that both

`G_{2,2}(u,v)<=Q(u,v)` for all `u,v>=0`,                    (3.3)

and

`Q(gamma u0,gamma v0)<=gamma G_{2,2}(u0,v0)`.              (3.4)

#### Proof

Putting `v=0` in (3.1) gives `G_{2,2}(u,0)=u`, so (3.3) forces `a>=1`. Similarly `G_{2,2}(0,v)=v` forces `b>=1`. Hence

`Q(gamma u0,gamma v0)>=gamma(u0+v0)`.                       (3.5)

But for `u0,v0>0`,

`e^{u0}+e^{v0}-1 < e^{u0+v0}`

because the difference of the right side and left side is

`(e^{u0}-1)(e^{v0}-1)>0`.

Therefore

`G_{2,2}(u0,v0)<u0+v0`,                                     (3.6)

and (3.5) contradicts (3.4). QED.

So the exact Pascal state cannot be closed by certifying the gap independently. Any successful induction must keep the adjacent hazards **coupled** so that cancellation survives.

## 4. Method #21 — the same shape as Talagrand's endpoint, but coupled

The right abstraction is a two-hazard composition lemma.

### Lemma 4.1 — coupled Pascal closure

Let `H,L : R_+^m -> R_+` satisfy `0<=H<=L`, and put

`g=L-H`.                                                     (4.1)

Fix `0<gamma<=1` and a base `q`. Suppose there are positive multilinear polynomials `P_H,P_L` such that

`H(t)<=P_H(t)`, `L(t)<=P_L(t)` for all `t>=0`,              (4.2)

and

`P_H(gamma q)<=gamma H(q)`,
`P_L(gamma q)<=gamma L(q)`.                                 (4.3)

For a new coordinate `s`, define

`K(t,s)=H(t)+Phi(s,L(t)-H(t))`.                              (4.4)

Assume the base gap satisfies

`g(q)>=gamma L(q)`.                                         (4.5)

Then `K` has a positive multilinear majorant `P_K` satisfying the same `C_gamma` budget at every prescribed new-coordinate base `s0>=0`.

#### Proof

Put `H0=H(q)`, `L0=L(q)`, `g0=L0-H0`. Apply the endpoint `gamma=1` theorem (2.5)--(2.7) to the base `(s0,g0)`. Thus there are `a,b,c>=0`, with `b<=1`, such that

`Phi(s,z)<=a s+b z+c s z` for all `s,z>=0`,                 (4.6)

and

`Phi(s0,g0)=a s0+b g0+c s0g0`.                             (4.7)

Define

`P_K(t,s)=a s+b P_L(t)+(1-b)P_H(t)+c s P_L(t)`.             (4.8)

Because `s` is a new coordinate, `s P_L(t)` is still multilinear, and every coefficient in (4.8) is nonnegative.

Using (4.6), (4.1), and `H>=0`,

`K(t,s)`
` <= H+a s+b(L-H)+c s(L-H)`
` = a s+bL+(1-b)H+c sL-c sH`
` <= a s+bL+(1-b)H+c sL`
` <= P_K(t,s)`.                                             (4.9)

So the global majorant holds. For the budget, (4.3) gives

`P_K(gamma q,gamma s0)`
` <= gamma[a s0+bL0+(1-b)H0+gamma c s0L0]`.                 (4.10)

Since `L0=H0+g0`, the non-`c` terms equal

`a s0+bL0+(1-b)H0=H0+a s0+b g0`.                           (4.11)

By (4.7),

`K(q,s0)=H0+a s0+b g0+c s0g0`.                             (4.12)

Subtracting the bracket in (4.12) from the bracket in (4.10) leaves exactly

`c s0(gamma L0-g0)<=0`                                      (4.13)

by (4.5). Therefore

`P_K(gamma q,gamma s0)<=gamma K(q,s0)`.                     (4.14)

This is the required certificate. QED.

### Why this bypasses Lemma 3.1

The construction never asks for a positive-polynomial majorant of `g=L-H`. The dangerous difference is used only **inside** `Phi`; after applying the endpoint certificate, the coefficient `b<=1` leaves the positive convex combination

`bP_L+(1-b)P_H`,

while the negative term `-c sH` can be discarded. The base-point cost of discarding it is exactly the gap condition (4.5). This is the cancellation the standalone-gap route destroyed.

## 5. An exact gap fraction from the ordered Pascal profile

The gap ordering (2.4) immediately gives the missing condition.

### Lemma 5.1 — adjacent gap fraction

For `2<=k<=m+1`,

`G_{m,k}(t)>=F_{m,k-1}(t)/(m-k+2)`                          (5.1)

for every `t>=0`.

#### Proof

Since `F_{m,m+1}=0`, telescoping (2.2) gives

`F_{m,k-1}=sum_{j=k}^{m+1} G_{m,j}`.                        (5.2)

There are `m-k+2` terms. By (2.4), each is at most the first one `G_{m,k}`. Hence

`F_{m,k-1}<= (m-k+2)G_{m,k}`,

which is (5.1). QED.

This is the distributional invariant that makes the coupled composition quantitative.

## 6. Main theorem — every finite cardinality threshold gets an explicit heterogeneous constant

### Theorem 6.1 — `A_{n,k} in C_{1/(n-k+1)}`

For every `n>=1` and `1<=k<=n`, the cardinality-threshold class

`A_{n,k}={X subset[n]: |X|>=k}`

belongs to

`C_{gamma_{n,k}}`, where `gamma_{n,k}=1/(n-k+1)`.           (6.1)

This statement covers **all heterogeneous base vectors** `q`; no symmetry or equal-coordinate hypothesis is imposed.

#### Proof

We induct on `n`.

For `k=1`, `A_{n,1}` is the nonempty class, which Talagrand Proposition 10.2 places in `C_1`, hence in `C_{1/n}` because `C_gamma` increases as `gamma` decreases. For `k=n`, `A_{n,n}` is the all-elements endpoint. The preceding R15 endpoint theorem gives it in `C_1`, exactly (6.1).

Now let `2<=k<=n-1`, put `m=n-1`, and set

`gamma=1/(n-k+1)=1/(m-k+2)`.                               (6.2)

Split off the `n`-th coordinate, with hazard `s`. In the notation of (2.1), let

`H(t)=F_{m,k}(t)`,
`L(t)=F_{m,k-1}(t)`,
`g(t)=G_{m,k}(t)=L(t)-H(t)`.                                (6.3)

By induction,

`L in C_{1/(m-(k-1)+1)}=C_{1/(m-k+2)}=C_gamma`.            (6.4)

Also

`H in C_{1/(m-k+1)}`.                                       (6.5)

Since

`gamma=1/(m-k+2) <= 1/(m-k+1)`,

monotonicity of the classes gives

`H in C_gamma`.                                              (6.6)

Thus, at every base `q`, `H` and `L` supply positive multilinear majorants satisfying (4.2)--(4.3). Lemma 5.1 gives

`g(q)=G_{m,k}(q)>=L(q)/(m-k+2)=gamma L(q)`.                 (6.7)

All hypotheses of the coupled Pascal closure Lemma 4.1 are therefore satisfied. Using the exact recursion (2.1),

`F_{n,k}(t,s)=H(t)+Phi(s,g(t))`,

so Lemma 4.1 gives `F_{n,k}` a `C_gamma` certificate at every base `(q,s0)`. This proves (6.1). QED.

### Immediate concrete consequences

1. For `n=3,k=2`, the full heterogeneous threshold satisfies

`A_{3,2} in C_{1/2}`.                                       (6.8)

This removes the homogeneous-base restriction from the earlier R15 `n=3,k=2` work.

2. For every `n`, the `k=2` threshold satisfies

`A_{n,2} in C_{1/(n-1)}`                                    (6.9)

for arbitrary heterogeneous bases.

3. Endpoint `k=n` remains `C_1`, while `k=1` is source-known `C_1`.

The theorem is genuinely stronger than the preceding homogeneous/flat-support certificates, but it is not the uniform constant requested by Problem 10.9.

## 7. Method #30 — one scale/direction: why the new induction still does not solve Problem 10.9

The gap fraction (5.1) is asymptotically sharp on the simplest homogeneous high-activity ray. This identifies the exact loss of the current induction.

Take `t_i=c` for all `1<=i<=m` and let `c->infinity`. The exact elementary-symmetric formula gives

`F_{m,k}(c 1)`
` =(m-k+1)c-log binom(m,k-1)+o(1)`,                         (7.1)

and

`F_{m,k-1}(c 1)`
` =(m-k+2)c-log binom(m,k-2)+o(1)`.                         (7.2)

Hence

`G_{m,k}(c1)`
` =c+log[binom(m,k-1)/binom(m,k-2)]+o(1)`
` =c+log[(m-k+2)/(k-1)]+o(1)`.                             (7.3)

Therefore

`G_{m,k}(c1)/F_{m,k-1}(c1) -> 1/(m-k+2)`.                  (7.4)

So no improvement of Lemma 5.1 alone can turn the inductive constant into a universal positive number. To solve Problem 10.9 by this architecture one must recover some of the term discarded in (4.9),

`-c s H`,                                                    (7.5)

or use a multi-coordinate/block update in which several adjacent gaps are paid jointly. In other words, the remaining loss is not a loose estimate hidden in the ordered-gap lemma; it appears already in the exact high-activity asymptotics.

This is a useful failure-to-glue result: the Pascal/endpoint mechanism now yields a full finite-dimensional theorem, and it also pinpoints why iterating it one coordinate at a time cannot by itself produce Talagrand's universal `gamma`.

## 8. Prior-art and current-status search — dated and bounded

I performed fresh 2026-09-18 public queries for:

- exact Talagrand title plus `Problem 10.9`, `C_gamma`, cardinality threshold;
- the formula/string `1/(n-k+1)` together with Talagrand / cardinality threshold;
- Pascal recursion / hazard / positive multilinear majorant formulations;
- later Talagrand-threshold work including DeMarco--Kahn, Frankston--Kahn--Park, Gunby--He--Narayanan, Warnke, and the Kahn--Kalai threshold literature;
- Burdzy--Scheutzow exact title / Problem 7.2 / citing material.

The search recovered Talagrand's STOC 2010 source, DeMarco--Kahn's 2015 note, and later threshold/down-set papers, but I did **not** find an accessible source explicitly stating the bound `A_{n,k} in C_{1/(n-k+1)}`, the coupled Pascal closure above, or a resolution of exact Problem 10.9 in this positive-polynomial formulation. This is bounded negative evidence only. The ingredients—Poisson-binomial recursion, ordered gaps, and Talagrand's endpoint function—are elementary/classical enough that **novelty remains UNVERIFIED**.

The parent F0111 must remain `PARTIAL / OPEN-looking / NOT CLAIMED` until current-status and ownership admission is completed and, for any new theorem, independent audits and prior-art review pass.

## 9. Validation discipline and closure status

No finite-search claim was introduced, so I did not manufacture a checker. The new claims are analytic and their proofs are on the page. Numerical path samples play no role, and there is no Brownian-law claim from simulation.

The theorem chain depends on the preceding SELF_CHECK_ONLY endpoint `gamma=1` proof and the preceding SELF_CHECK_ONLY Pascal gap-order theorem. Therefore the new Theorem 6.1 is also **SELF_CHECK_ONLY**. Before any promotion it needs:

1. an independent P26 full-proof audit;
2. a second genuinely independent OTHER-track audit;
3. a dedicated prior-art/citation-graph audit of the endpoint theorem and the new coupled induction;
4. only then a source-scoped paper package if the result is judged new and useful.

This does not satisfy closure for full Problem 10.9 because the constant in (6.1) tends to zero with `n-k+1`.

## 10. Model / scheduler control truth

The platform limitation remains unchanged. The exposed scheduler surface has task identity/title/prompt, schedule or start-time data, timing mode, and enabled state, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution field**. Therefore `GPT-6 / maximum` remains prompt text only here; this run identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

The historical P26 native ID once returned `You cannot modify this task` in one authorization context. Root continuity records a later successful P26 update from another authorized P/C context. The lawful workaround is the owning/authorized task context or an owner/admin/product/backend/support surface that exposes the desired controls, not duplication, permission bypass, or pretending prompt text is a model selector. I made no scheduler changes.

## 11. Next research direction

The prior triple was #18/#5/#24; this run used the prescribed fresh #11/#21/#30 triple. The next genuinely different attack, if F0111 remains only a retained screen, should target the exact discarded term (7.5), not another one-coordinate gap lemma. Two plausible routes are:

- a two-coordinate Pascal update, seeking a four-state entropy boundary whose tangent keeps the negative overlap correction instead of discarding it;
- a blockwise induction on the deficit `r=n-k+1`, where several adjacent gaps are coupled before paying a budget.

Natural fresh Section-B choices for that next run are #3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #25 COUNT THE SAME THING TWICE.

```yaml
ledger_delta:
  worker: R15
  lane: CLOSABLE OUTSIDE
  native_source: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion (2014), Problem 7.2 / I0076"
  native_metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
  native_before: "2/4 historical retirement value; no surviving frozen candidate"
  native_after: "2/4 historical retirement value; no surviving frozen candidate"
  native_status: "OPEN / PARTIAL / RETIRED-HANDOFF"
  native_unchanged_count: 6
  admission_metric: "E_READY_CLOSABLE free for R15"
  admission_before: 0
  admission_after: 0
  admission_status: "current bounded coordinator screen has no additional free READY CLOSABLE successor"
  retained_screen:
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9 / F0111"
    before: "endpoint C1 SELF_CHECK_ONLY; k=2 C1 only at homogeneous/flat-support bases; exact Pascal recursion and ordered gaps"
    after: "SELF_CHECK_ONLY theorem A_{n,k} in C_{1/(n-k+1)} for every n,k and arbitrary heterogeneous base; n=3,k=2 now C_{1/2}; one-coordinate loss asymptotically sharp"
    status: "PARTIAL relative to Problem 10.9; universal gamma still not obtained; novelty UNVERIFIED"
  tried_moves: [11, 21, 30]
  next_moves: [3, 14, 25]
  remaining_obligation: "full Problem 10.9 needs a gamma bounded below uniformly in n,k; current one-coordinate Pascal induction loses the asymptotically sharp factor 1/(n-k+1); endpoint/Pascal/new theorem all need two independent audits and prior-art audit"
  evidence:
    - "Burdzy--Scheutzow Definition 2.1 and Problem 7.2, primary PDF rechecked 2026-09-18"
    - "Talagrand Definition 10.1, Proposition 10.2, Proposition 10.5, Theorem 10.7, Problem 10.9, primary PDF rechecked 2026-09-18"
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_0858Z_successor_admission_f0111_pascal_u54.md"
    - "runs/R15/20260918_1805Z_successor_screen_f0111_endpoint_gamma1_kl_r63v.md"
    - "operations/task_health/runs/2026-09-18T190200Z/status.md"
  audit_ids: []
```