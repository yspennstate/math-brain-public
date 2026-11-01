Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow I0076 remains `OPEN / PARTIAL / RETIRED-HANDOFF` at the historical carried `2/4`, with no surviving frozen counterexample candidate; free admission remains `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: for Talagrand F0111, the heterogeneous `k=2` Pascal compiler now has an explicit base-adaptive local constant `Gamma(q)` strictly stronger than the carried `1/(n-1)` bound at every finite base with at least three active coordinates, tending to `1` at the one-coordinate points at infinity and equaling `1` on support size at most two. Methods #6 DEFORM TO A SOLVED POINT, #10 DERANDOMIZE, #29 ADD THE POINTS AT INFINITY.**

# R15 retained screen — an adaptive heterogeneous `k=2` Pascal certificate

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All new mathematics below is **SELF_CHECK_ONLY**. Nothing here closes Talagrand Problem 10.9, and nothing reopens Burdzy–Scheutzow Problem 7.2 after its mandatory six-run handoff. No novelty claim is made without independent audits and a substantially broader citation search.

## 1. Continuity and source fidelity

Before doing new mathematics I refreshed the current repository state rather than restarting from the stale native title:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`;
- newest coordinator/task-health status, including the 2026-09-18T23:52Z reconciliation;
- controlling Burdzy–Scheutzow handoff `runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`;
- immediately preceding R15 report `runs/R15/20260918_2304Z_successor_screen_f0111_staircase_envelope_v68m.md`;
- the earlier coupled-Pascal compiler report `runs/R15/20260918_1924Z_successor_screen_f0111_coupled_pascal_cgamma_s64x.md`;
- newest neighboring F0111 admission screen `proofnet24/NM13-12/runs/2026-09-18/2026-09-18T23-55-30Z__post-e0086-admission-delta-screen-10-f0111-envelope.md`;
- exact F0111 intake/attempt continuity, including `F0111-A001`.

The newest coordinator/admission evidence still records no source-current, ownership-clear free CLOSABLE successor crossing admission. The neighboring NM13-12 screen likewise keeps F0111 `PENDING / NOT READY / retained screen`, not an admitted R15 assignment. I therefore create no new claim file and continue only the already-retained screening mathematics.

### Burdzy–Scheutzow Problem 7.2 is not reopened

I rechecked the primary paper, Krzysztof Burdzy and Michael Scheutzow, *Forward Brownian Motion*, arXiv:1302.6958v4 / PTRF 160 (2014), Definition 2.1 and Problem 7.2.

The source says:

- `X` is FBM if there are random times `S_n -> -infinity` a.s. such that each complete centered future from `S_n` is standard Brownian motion;
- BBM means the time-reversed process is an FBM;
- 2BM means there is one random time `S` for which the complete centered future and past half-paths are **independent standard Brownian motions**;
- Problem 7.2 assumes FBM + BBM and only that there exists an arbitrary random time `T` such that the complete centered forward and backward half-paths are independent, and asks whether this forces 2BM.

There is no stopping-time hypothesis on `T`, no deterministic-time replacement, and neither half at `T` is separately assumed Brownian. Problem 7.5 is different and remains excluded.

The six-run handoff is still controlling. The source-Theorem-6.1 non-2BM candidate had FBM, BBM and non-2BM but no source-valid independent real seam. The later Brownian-prefix/BES seam candidate had FBM, BBM and the desired seam independence but was proved actually 2BM. Hence there is no surviving frozen counterexample candidate on which the four source obligations can honestly be advanced. The historical `2/4` is only the carried retirement value.

Fresh dated 2026-09-18 exact-title / exact-`Problem 7.2` / citation queries again recovered the original publication and related citing material but no accessible later primary source explicitly claiming to settle exact Problem 7.2. This is bounded negative evidence only, not a worldwide openness certificate.

## 2. Retained source and previously proved compiler

The retained screen is Michel Talagrand, *Are Many Small Sets Explicitly Small?*, STOC 2010, Definition 10.1 and Problem 10.9.

For hazards `t=(t_i)`, under `zeta_t` coordinate `i` is present with probability `1-exp(-t_i)`. For an up-class `A`, write

`F_A(t)=-log(1-zeta_t(A))`.

Talagrand's `C_gamma` condition asks that for every base `q>=0` there exist a multilinear polynomial with nonnegative coefficients and no constant term,

`P(t)=sum_{empty != I} beta_I t_I`, `beta_I>=0`,

such that

`F_A(t)<=P(t)` for all `t>=0`,

and

`P(gamma q)<=gamma F_A(q)`.

Problem 10.9 asks whether there is one universal `gamma>0` for all cardinality thresholds

`A_{n,k}={X subset[n]: |X|>=k}`.

The previous R15 coupled-Pascal report proved, SELF_CHECK_ONLY, the following compiler. Write

`H(t)=F_{m,k}(t)`,
`L(t)=F_{m,k-1}(t)`,
`g(t)=L(t)-H(t)`,

and after adding a new hazard `s`,

`K(t,s)=H(t)+Phi(s,g(t))`,

where

`Phi(u,v)=-log(e^{-u}+e^{-v}-e^{-(u+v)})`.

Suppose `H` and `L` already possess `C_gamma` certificates at the old base `q`. The preceding endpoint result for `Phi` supplies `a,b,c>=0`, with `b<=1`, such that

`Phi(s,z)<=a s+b z+c s z`

and equality holds at the prescribed base `(s0,g(q))`. Then

`P_K(t,s)=a s+bP_L(t)+(1-b)P_H(t)+c s P_L(t)`

is a positive multilinear global majorant, and its base budget closes whenever

`g(q)>=gamma L(q)`.                                          (2.1)

The earlier all-threshold theorem used only the distribution-free ordered-gap estimate and therefore obtained

`A_{n,k} in C_{1/(n-k+1)}`.

This run asks how much stronger (2.1) becomes for `k=2` when the actual heterogeneous base `q` is used instead of the worst-case gap fraction.

## 3. Exact `k=2` gap and the local certificate problem

For `k=2` on an old block `S`, put

`L_S(q)=sum_{i in S} q_i`.

The exact threshold formula is

`F_{S,2}(q)=L_S(q)-log(1+sum_{i in S}(e^{q_i}-1))`,

so the Pascal gap is

`g_S(q)=L_S(q)-F_{S,2}(q)`
`       =log(1+sum_{i in S}(e^{q_i}-1)).`                    (3.1)

Thus the coupled compiler at that step needs only

`gamma <= g_S(q)/L_S(q)`.                                   (3.2)

For one fixed base `q`, define `Gamma_loc(q)` to be the supremum of `gamma<=1` for which a Talagrand-positive multilinear certificate exists **at that base** for `A_{n,2}`. This is a local/base-dependent quantity. It is not a claim that the whole class belongs to `C_{Gamma_loc(q)}` uniformly over all bases.

## 4. Method #10 — DERANDOMIZE the coordinate order

A naive implementation of the Pascal compiler could choose an arbitrary coordinate order. The useful observation is that the order can be made deterministic and adapted to the base.

Sort the base hazards as

`q_(1)>=q_(2)>=...>=q_(n)>=0`

and put

`R=sum_{j=3}^n q_(j)`.

For `a,r>=0`, not both zero, define

`psi(a,r)=log(e^a+r)/(a+r)`,                                 (4.1)

and set `psi(0,0)=1`.

### Lemma 4.1 — tail monotonicity

For each fixed `a>=0`, `psi(a,r)` is nonincreasing in `r>=0`.

#### Proof

Let `y=e^a+r`. Then

`partial_r psi`
` = [ (a+r)/(e^a+r) - log(e^a+r) ]/(a+r)^2`.

Since `e^a-a>=1`,

`a+r = y-(e^a-a) <= y-1`.

Hence

`(a+r)/y <= 1-1/y <= log y`

for `y>=1`. Therefore `partial_r psi<=0`. QED.

### Theorem 4.2 — deterministic adaptive `k=2` certificate

For every `n>=2` and every base `q>=0`,

`Gamma_loc(q) >= Gamma_P(q)`,                                (4.2)

where

`Gamma_P(q)=max{ psi(q_(1),R), psi(q_(2),R) }`.              (4.3)

The theorem is SELF_CHECK_ONLY because it depends on the preceding R15 endpoint-`C_1` and coupled-Pascal results, which themselves still await independent source-level audits.

#### Proof

First choose the second-largest coordinate `q_(2)` to be added **last**. Keep the largest coordinate, of hazard `a=q_(1)`, in the old block from the start. Begin with that anchor and one other coordinate. The two-coordinate threshold `A_{2,2}` is the all-elements endpoint and has the carried `C_1` certificate, hence a `C_gamma` certificate for every `gamma<=1`.

Now add the remaining coordinates one by one, leaving `q_(2)` until the final step. At every intermediate old block `S`, the anchor `a` is present and the total hazard of the other old coordinates is some `r_S<=R`. By `e^x-1>=x`, the exact gap (3.1) satisfies

`g_S(q)`
` =log(1+sum_{i in S}(e^{q_i}-1))`
` >=log(e^a+r_S)`.

Since `L_S(q)=a+r_S`,

`g_S(q)/L_S(q)>=psi(a,r_S)>=psi(a,R)`                        (4.4)

by Lemma 4.1. Therefore the coupled condition (2.1) holds at **every** recursive insertion step for every

`gamma<=psi(q_(1),R)`.

The coupled compiler propagates the certificate all the way through the final insertion of `q_(2)`. This proves

`Gamma_loc(q)>=psi(q_(1),R)`.

Repeating the identical deterministic construction with the largest coordinate `q_(1)` held back until the final step and `q_(2)` used as the permanent anchor proves

`Gamma_loc(q)>=psi(q_(2),R)`.

Taking the better of the two gives (4.3). QED.

### Why only two deterministic orders matter for this lower-bound compiler

For any proposed final coordinate `j`, the best permanent anchor among the remaining coordinates is the largest one there. If `j>=3`, the anchor is still `q_(1)` but the residual tail contains `q_(2)` and omits only `q_(j)`, so that residual tail is at least `R`. Lemma 4.1 shows that such a choice cannot beat the `j=2` lower bound `psi(q_(1),R)`.

If `j=1`, the best remaining anchor is `q_(2)`, producing `psi(q_(2),R)`.

Hence the base-adapted search over all possible final coordinates collapses to the **deterministic two-way comparison** in (4.3). No randomized order or sampled search is needed.

## 5. Strict improvement over the carried generic Pascal constant

For `a,r>=0`,

`log(e^a+r)>=a`,

so

`psi(a,r)>=a/(a+r)`.                                        (5.1)

Using the first term in (4.3),

`Gamma_P(q)>=q_(1)/(q_(1)+R)`.                              (5.2)

Because every `q_(j)<=q_(1)`,

`R<= (n-2)q_(1)`,

and therefore

`Gamma_P(q)>=1/(n-1)`.                                      (5.3)

This recovers the earlier dimension-dependent theorem for `k=2`. More importantly, if `R>0`, then

`log(e^{q_(1)}+R)>q_(1)`,

so the first inequality in (5.1) is strict. Thus the adaptive compiler yields a **strictly larger local constant than `1/(n-1)` at every finite base with at least three positive coordinates**, except that specialized certificates from earlier runs can of course be stronger still (for example the separately proved homogeneous-base `C_1` certificate).

When the support has size at most two, `R=0`, and

`psi(a,0)=1`.

Therefore Theorem 4.2 gives

`Gamma_loc(q)=1`                                             (5.4)

for every `k=2` base supported on at most two coordinates. This includes unequal two-point bases, not only the flat-support cases handled earlier.

For a useful concrete cone, (5.2) gives

`Gamma_loc(q)>=1/2`

whenever

`q_(1)>=R=sum_{j=3}^n q_(j)`.                               (5.5)

Notice that the second-largest coordinate is absent from this sufficient condition because it is deliberately postponed to the last Pascal step.

## 6. Method #6 — DEFORM TO A POINT YOU CAN SOLVE

Fix the residual tail mass `R>0` and deform the permanent anchor from `a` to larger values. The exact lower-bound profile is

`psi(a,R)=log(e^a+R)/(a+R)`.

It is tempting to assume this improves monotonically with `a`; that is false in general. The derivative is

`partial_a psi`
` = N_R(a)/(a+R)^2`,

where

`N_R(a)=(a+R)e^a/(e^a+R)-log(e^a+R)`.                       (6.1)

A direct differentiation gives the exact cancellation

`N_R'(a)=(a+R)e^a R/(e^a+R)^2 >=0`.                         (6.2)

For `R>0`,

`N_R(0)=R/(1+R)-log(1+R)<0`,

while `N_R(a)->R>0` as `a->infinity`. Hence there is a unique turning point `a_*(R)>0` satisfying

`(a_*+R)e^{a_*}/(e^{a_*}+R)=log(e^{a_*}+R)`,                (6.3)

and `psi(a,R)` decreases before `a_*` and increases after it.

So the deformation route contains a real warning: simply making one coordinate somewhat larger can initially **worsen** this particular compiler. After the unique turning point, however, the compiler improves monotonically all the way to the solvable point at infinity.

This is useful route information rather than a numerical plot: the turning-point statement follows exactly from (6.1)–(6.2).

## 7. Method #29 — ADD THE POINTS AT INFINITY

The compactified one-coordinate boundary is completely transparent in (4.1). For fixed `R`,

`log(e^a+R)=a+log(1+Re^{-a})`,

so

`psi(a,R)`
` = [a+log(1+Re^{-a})]/(a+R)`
` -> 1` as `a->infinity`.                                   (7.1)

More precisely,

`1-psi(a,R)`
` = [R-log(1+Re^{-a})]/(a+R)`
` = R/a+o(1/a)`                                             (7.2)

for fixed `R`.

Thus the adaptive Pascal certificate becomes asymptotically `C_1` whenever one retained anchor escapes to infinity while all coordinates beyond the two largest remain bounded.

There is also a simple explicit sufficient condition avoiding asymptotics. Since `psi(a,R)>=a/(a+R)`, for any fixed `0<gamma<1`,

`a >= gamma R/(1-gamma)`                                    (7.3)

implies

`psi(a,R)>=gamma`.

Consequently, on every cone satisfying (7.3), the heterogeneous `k=2` threshold has a local `C_gamma` certificate produced by the exact positive-multilinear Pascal compiler.

At the literal face `R=0`, the value is already `1` at finite `a`, which agrees with the fact that a two-coordinate threshold is the endpoint AND class.

## 8. Homogeneous and tropical checks

The theorem is not intended to replace the earlier specialized homogeneous `C_1` result, but it has the correct scale limits.

For `q=c 1_n`,

`R=(n-2)c`,

and the adaptive Pascal lower bound becomes

`Gamma_P(c1_n)`
` = log(e^c+(n-2)c)/((n-1)c).`                              (8.1)

As `c downarrow 0`, this tends to `1`, while as `c->infinity`,

`Gamma_P(c1_n)->1/(n-1)`.                                   (8.2)

So this particular compiler interpolates between an almost-`C_1` low-activity regime and the sharp one-coordinate-Pascal loss in the tropical/high-activity regime. The earlier symmetric tangent certificate is stronger at exactly homogeneous bases—it gives `C_1` for every finite `c`—so (8.1) should be read as a diagnostic of the **coupled Pascal route**, not as an optimal local constant.

The high-activity limit is consistent with the earlier proof that the one-coordinate Pascal loss `1/(n-1)` is asymptotically sharp for that route. The present result shows that the loss is not intrinsic at generic finite heterogeneous bases; it appears only after passing toward the hard tropical boundary.

## 9. What this changes and what remains open

This run does not solve F0111. It does remove one ambiguity from the retained route.

The generic statement

`A_{n,2} in C_{1/(n-1)}`

was a worst-base theorem. The actual coupled compiler is much more adaptive: at a prescribed base, its certified constant is at least the explicit quantity (4.3), which:

- is always at least `1/(n-1)`;
- is strictly larger at every finite base with a nonzero third-coordinate tail;
- is exactly `1` on support size at most two;
- tends to `1` when one anchor escapes to infinity with the lower tail fixed;
- has an exact one-turning-point deformation profile rather than a monotone heuristic;
- requires only a deterministic comparison of two coordinate orders.

The remaining source-level obstruction is therefore concentrated in bases where no specialized symmetry certificate applies and the tail behind the two largest coordinates is sufficiently large to keep every available local compiler bounded away from one. More importantly, Problem 10.9 still asks for a **single universal positive `gamma` across all `n,k` and every base**. A base-adaptive improvement for `k=2` is only a restricted theorem.

For the next run the useful question is no longer “which coordinate order should we try?” The order optimization above is closed for this anchored lower-bound compiler. A genuinely different route has to use either more than one permanent anchor, or a block certificate that lets the large second coordinate participate before the last step without paying for the non-polynomial first gap coefficientwise.

## 10. Current-literature / prior-art check

Dated public searches on 2026-09-18/19 included:

- exact Talagrand title, `Problem 10.9`, `C_gamma`, and cardinality-threshold wording;
- the original STOC 2010 source and an accessible PDF containing Definition 10.1 and Problem 10.9;
- DeMarco–Kahn, *Note on a problem of M. Talagrand*;
- Frankston–Kahn–Park and later threshold/down-set literature;
- Warnke, *Note on down-set thresholds* (2024);
- recent 2025–2026 threshold/container literature returned by exact-title/citation searches;
- exact-formula searches around the adaptive `log(e^a+R)/(a+R)` bound.

I found no accessible source explicitly stating the base-adaptive compiler theorem above or claiming a resolution of Talagrand's exact Definition-10.1 / Problem-10.9 positive-multilinear-majorant question. That is bounded negative evidence only. The proof uses elementary inequalities and a previously derived compiler, so **novelty remains UNVERIFIED** and publication language must not call it new without a proper citation-graph audit.

The fresh Burdzy–Scheutzow search likewise recovered the original paper and citation pages but no accessible later primary work explicitly claiming to settle exact Problem 7.2. Again, this is not a worldwide openness certificate.

## 11. Validation and artifacts

No numerical path samples were used. No finite claim was promoted, so no exact-arithmetic checker was manufactured merely to create a receipt. The movement is a parameter-uniform analytic theorem with its proof on the page.

Dependencies that still require independent audit before any closure use:

1. the R15 endpoint `Phi in C_1` proof from `runs/R15/20260918_1805Z_successor_screen_f0111_endpoint_gamma1_kl_r63v.md`;
2. the coupled-Pascal compiler from `runs/R15/20260918_1924Z_successor_screen_f0111_coupled_pascal_cgamma_s64x.md`;
3. the present adaptive-order theorem.

These are SELF_CHECK_ONLY. No P26 or second independent full-claim audit is credited here.

## 12. Structured `ledger_delta`

```yaml
ledger_delta:
  worker: R15
  source_native:
    id: I0076
    citation: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
    metric: "number of the four source-matching obligations proved for one frozen counterexample candidate"
    before: "historical carried 2/4; no surviving frozen candidate"
    after: "historical carried 2/4; no surviving frozen candidate"
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    unchanged_count: "terminal six-run handoff already reached; not incremented by successor-screen work"
    remaining_obligation: "future reassignment would require a new frozen candidate satisfying exact random-seam independence without becoming 2BM"
  successor_admission:
    metric: E_READY_CLOSABLE
    before: 0
    after: 0
    status: ADMISSION_PENDING
  retained_screen:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, STOC 2010, Problem 10.9"
    status: "PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED"
    movement: "For k=2, prove local adaptive certificate Gamma_loc(q) >= max{psi(q_(1),R), psi(q_(2),R)}, psi(a,R)=log(e^a+R)/(a+R), R=sum_{j>=3} q_(j); deterministic order reduction; exact one-turning-point deformation; C_1 at support<=2 and Gamma->1 at one-coordinate infinity."
    remaining_obligation: "one universal positive gamma for all n,k and all bases, with independent source-level audits"
  tried_moves:
    - 6
    - 10
    - 29
  evidence:
    - "runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md"
    - "runs/R15/20260918_2304Z_successor_screen_f0111_staircase_envelope_v68m.md"
    - "runs/R15/20260918_1924Z_successor_screen_f0111_coupled_pascal_cgamma_s64x.md"
    - "proofnet24/NM13-12/runs/2026-09-18/2026-09-18T23-55-30Z__post-e0086-admission-delta-screen-10-f0111-envelope.md"
  audit_ids: []
  next_moves:
    - 3
    - 17
    - 25
```

## 13. Model / scheduler control status

The runtime identifies this invocation as **GPT-5.6 Sol**. There is no authenticated reasoning-effort telemetry exposed here, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6 maximum.

The current scheduler-control surface still exposes task identity/title/prompt, schedule or relative-start fields, timing mode, and enabled state, but **no binding model-family selector, no binding reasoning-effort selector, no authenticated applied-model receipt, and no guaranteed hour-long execution setting**. The repository implementation manifest records the historical P26 response `You cannot modify this task` as an authorization-context boundary and also records later successful edits from an authorized context. The lawful workaround is the owning or otherwise authorized context, or an owner/admin/product/API surface that exposes those controls; not task duplication, permission bypass, or a repository edit represented as a scheduler change.

No scheduler, permission, email, Drive, or public-posting action was attempted in this run.
