Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**. **FIXED-METRIC MOVEMENT:** active H0002 complete envelope `G_loc -> G_run > G_loc`. Methods actually used: **B7 / B16 / B17**.

# R16 — full running-floor limit strictly improves the local two-level tail envelope

Date: 2026-09-19 UTC.
Target: `H0002`, HARD OUTSIDE, exclusive owner R16.
Status: **PARTIAL / source OPEN-looking / ACTIVE**.

## 1. Required continuity, exclusions, and current-source check

I continued from the newest immutable R16 report

`runs/R16/2026-09-19T12-44-11Z_h0002-running-floor-local-refinement_a6e2.md`

rather than restarting. Before new mathematics I re-read/reconciled:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/H0002.md`;
- the newest R16 majorization/moment/tail reports; and
- the newest neighboring same-source record, `research7_2026-09-17/R7-07/handoffs/2026-09-18T032400Z__G0011_terminal_handoff.md`. G0011 is the distinct long-cycle conjecture and is already in terminal handoff, so it supplies neither a premise nor an ownership conflict here.

Fresh primary-source checks on 2026-09-19:

- Bansal--Jiang, arXiv:2508.03961v2, proves the Beck--Fiala `O(sqrt(t))` scale directly in the regime `t >= log^2 n`, with weaker polylogarithmic loss below that regime: https://arxiv.org/abs/2508.03961 .
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 2026-09-10, proves a stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduces discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`, with no restriction on `n`: https://arxiv.org/abs/2609.11189 .
- Karingula--Lovett, ECCC TR26-188, posted 2026-09-17, gives an elementary Komlos proof with constant `36`: https://eccc.weizmann.ac.il/report/2026/188/ .
- Christoph--Morawski--Wigderson, arXiv:2608.19145v1, submitted 2026-08-19, remains the current primary source surfaced for H0002. Its Question 5.1 asks for natural finite-graph conditions forcing a component of order `Omega(n)` for `p >= (1+epsilon)/lambda(G)` and explicitly points to spectral localization as the main obstruction: https://arxiv.org/abs/2608.19145 . A bounded current title/author/arXiv-ID search did not surface a later source-matching resolution. That is negative evidence only.

Thus the nominal Beck--Fiala existence target remains a **KNOWN current-preprint baseline**, not new R16 progress. The source-valid active R16 target remains H0002 on the frozen H1--H2--H3 sufficient-condition class.

## 2. Incoming theorem and notation

Retain every hypothesis and reduction from the preceding R16 chain. In endpoint notation:

- `d_P=d_pad<alpha`;
- `b_P=alpha-d_P>0`;
- `a_P=rho-b_P`;
- `Delta=epsilon(7-epsilon)/(8-epsilon)>0`;
- `t(b)` is the endpoint full-core threshold profile, extended by `t(b_P)=0`;
- `b_0>b_P` is the fixed maximizing point selected on the terminal compact interval;
- `t_0=t(b_0)>0`;
- `D_*:=b_P t_0>0`;
- `H_*:=a_P/D_*>t_0`;
- `phi_r(u):=1-exp(-r u)`;
- `g_r(u):=phi_r(u)/u`, with `g_r(0)=r`.

For a connected pre-absorption core `W` of density `a_3=c_3 a_P`, with `c_3 up 1`, sort normalized outside degrees increasingly as `x(q)`. For every finite old anchor family `D`, let `L_{D,3}(q)` be its old degree floor.

The established prefix and spectral-energy inequalities are, uniformly in finite `D`,

`int_0^{b_0} (x-L_{D,3})_+ dq >= c_3 D_*-o(1)`,          (2.1)

`int x(q)^2 dq <= c_3 a_P+o(1)`.                           (2.2)

The exact two-moment absorption term is

`eta_* = exp(-Delta t_0) D_* g_Delta(H_*)`.                (2.3)

The previous tail runs set

`Gamma:=H_*-t_0`,
`T_+:=t_0+Gamma/4`,
`Y:=t_0+Gamma/2`,                                          (2.4)

and then

`S:=(t_0+T_+)/2`,                                         (2.5)

so

`t_0<S<T_+<Y<H_*`.                                        (2.6)

They constructed fixed lengths `delta_S<=delta_loc` such that every old finite-anchor floor obeys the two-level bounds

`L_{D,3}(q)<=c_3 S+o(1)` on `[b_0,b_0+delta_S]`,           (2.7)

`L_{D,3}(q)<=c_3 T_++o(1)` on `[b_0,b_0+delta_loc]`.      (2.8)

The local two-level report then used

`A(X)=exp(-Delta t_0)D_*[g_Delta(X)-g_Delta(H_*)]`,        (2.9)

`V(X)=a_P-delta_loc X^2`,                                 (2.10)

`C(X)=exp(-Delta t_0)D_*`
`      *[g_Delta(V(X)/D_*)-g_Delta(H_*)]`                 (2.11)

on the feasible crossing branch, with `+infinity` when that branch is energy-impossible, and the two-level direct tail term `J_loc(X)`. It defined

`zeta_loc=sup_{X in [S,Y]} min{A(X),B_loc(X)}`,            (2.12)

`B_loc(X)=C(X)+J_loc(X)`,                                 (2.13)

and

`G_loc=min{1,G_coreavg+eta_*+zeta_loc}`.                  (2.14)

Every fixed `g<G_loc` is already certified to satisfy

`P(L_1(G_p)>=g n)->1`                                     (2.15)

uniformly on the same frozen H1--H2--H3 class whenever

`p >= (1+epsilon)/lambda(G)`.                              (2.16)

The only target this run is to replace the two-level staircase `(S,T_+)` by the **entire deterministic running floor**.

## 3. B16 — compute the first staircase cases and identify the limiting object

Define the deterministic running envelope

`bar_t(q):=sup{t(b): b_P<=b<=q}`.                          (3.1)

The preceding report established, uniformly over every finite old anchor family,

`L_D(q)<=bar_t(q)`,                                        (3.2)

and

`bar_t(b_0)=t_0`.                                          (3.3)

The one-cell approximation to `bar_t` is exactly the old constant level `T_+`; the two-cell approximation is exactly the previous `(S,T_+)` refinement. Now insert one more level

`S_-:=(t_0+S)/2`,                                         (3.4)

so

`t_0<S_-<S<T_+`.                                          (3.5)

By the same local continuity already used twice in the chain, choose a fixed

`0<delta_-<=delta_S`                                      (3.6)

such that

`bar_t(q)<=S_-` on `[b_0,b_0+delta_-]`.                   (3.7)

For every crossing threshold `X>=S`, the three-level staircase gives the previous `J_loc(X)` plus the strictly positive uniform increment

`chi_-:=delta_- [phi_Delta(S)-phi_Delta(S_-)]>0`.          (3.8)

This small-case computation shows the pattern: every inserted sublevel below the old left endpoint gives (i) a positive direct-tail gain on the preceding domain and (ii) room to move the crossing threshold further left. Nothing special occurs at three levels. The natural object is the monotone limit of the staircase itself.

No finite arithmetic claim is being made here; this is a symbolic decomposition of the already-established deterministic floor.

## 4. B7 — take the staircase limit and retain the full running floor

For a threshold

`X in (t_0,Y]`,                                            (4.1)

define the exact direct-tail gain against the deterministic running envelope by

`boxed: J_run(X):=`
`int_{b_0}^{b_0+delta_loc}`
`  [phi_Delta(X)-phi_Delta(bar_t(q))]_+ dq`.               (4.2)

This is precisely the monotone limit of the finite staircase tail gains. Since the integrand is bounded and increases under refinement of the lower staircase, monotone convergence (or dominated convergence) justifies passing to (4.2).

The no-cross branch remains unchanged:

`A(X)=exp(-Delta t_0)D_*[g_Delta(X)-g_Delta(H_*)]`.        (4.3)

Indeed, if every prefix degree stays below `X`, the proof of the sharp prefix two-moment estimate uses only the prefix surplus, the cap `X`, and the spectral-energy bound; it never used the coarse levels `S` or `T_+`.

If the no-cross case fails, some prefix degree exceeds `X`. Since `x(q)` is nondecreasing, the whole interval

`[b_0,b_0+delta_loc]`                                     (4.4)

then satisfies

`x(q)>=X-o(1)`.                                            (4.5)

The old finite-anchor baseline is at most `bar_t(q)` there. Hence the direct absorption improvement over **every** finite old anchor family is at least `J_run(X)-o(1)`.

The same monotone tail also consumes at least

`delta_loc X^2-o(1)`                                      (4.6)

of the global spectral `L^2` budget, so the energy-depleted prefix term stays exactly

`V(X)=a_P-delta_loc X^2`,                                 (4.7)

`C(X)=exp(-Delta t_0)D_*`
`      *[g_Delta(V(X)/D_*)-g_Delta(H_*)]`                 (4.8)

whenever `V(X)>0`. If the forced tail itself makes the crossing branch asymptotically impossible, set the crossing cost to `+infinity` as before.

Define

`boxed: B_run(X):=C(X)+J_run(X)`                          (4.9)

on the feasible branch, and `B_run(X):=+infinity` on the infeasible branch. Finally put

`boxed: zeta_run:=sup_{X in (t_0,Y]}`
`        min{A(X),B_run(X)}.`                             (4.10)

The function `A` is strictly decreasing in `X`. On every feasible interval, `C` is nondecreasing in `X` because `V(X)` decreases while `g_Delta` is decreasing; `J_run` is continuous and nondecreasing in `X` by dominated convergence. Thus the same one-dimensional minimax geometry used in the previous two reports remains valid.

## 5. Strict improvement over the complete incoming `zeta_loc`

The key comparison is already contained in the three-level test from Section 3.

For every `X in [S,Y]`, the running-floor integral dominates the two-level tail term by a fixed positive amount:

`boxed: J_run(X)>=J_loc(X)+chi_-`.                         (5.1)

Proof: on `[b_0,b_0+delta_-]`, the running floor is at most `S_-`, whereas the old local bound charges level `S`; on the rest of `[b_0,b_0+delta_S]` it is at most `S`; and on the remainder of `[b_0,b_0+delta_loc]` it is at most `T_+`. The first interval alone contributes the extra amount (3.8), while the other pieces reproduce at least `J_loc`.

Consequently, whenever the old crossing branch is feasible,

`boxed: B_run(X)>=B_loc(X)+chi_-`                         (5.2)

for every `X in [S,Y]`. If it is infeasible, both formulations correctly discard it.

Let

`z:=zeta_loc`                                              (5.3)

and take a maximizing point or limiting maximizer `X_* in [S,Y]` for the incoming minimax problem. There are the same three possibilities as in the preceding report.

### 5.1 Old optimum crossing-branch limited

If

`B_loc(X_*)<A(X_*)`,                                      (5.4)

then by (5.2)

`B_run(X_*)>z`                                            (5.5)

while `A(X_*)>z`. Therefore the new minimum is already strictly larger than `z` at the same threshold.

### 5.2 Old optimum a genuine crossing

If

`A(X_*)=B_loc(X_*)=z`,                                    (5.6)

then

`B_run(X_*)>=z+chi_-`.                                    (5.7)

Move `X` slightly to the left. Since `A` is strictly decreasing as a function of `X`, this raises `A` strictly above `z`; continuity of the feasible `B_run` keeps the crossing branch above `z`. If `X_*=S`, the newly opened domain `(t_0,S)` supplies precisely this left neighborhood.

### 5.3 Old optimum no-cross limited

If

`A(X_*)<B_loc(X_*)`,                                      (5.8)

the same left move raises `A`, while (5.2) and continuity keep `B_run` above `z`. Again the extension below `S` handles a left-endpoint optimizer.

At a boundary where `V(X)=0`, the preceding report already proved that the feasible-side limit of `C(X)` lies strictly above `A(X)`; replacing `J_loc` by the larger `J_run` cannot destroy that gap. If the crossing branch is impossible on a one-sided neighborhood, then `B_run=+infinity` there and the argument is easier.

All possibilities give

`boxed: zeta_run>zeta_loc`.                               (5.9)

This is strict movement beyond the **entire incoming two-level minimax envelope**, not merely beyond one selected threshold.

## 6. The incoming complete envelope still has headroom below one

Since

`zeta_loc<=sup_{X in [S,Y]} A(X)=A(S)`,                   (6.1)

we have

`eta_*+zeta_loc`
` <= eta_*+A(S)`
` = exp(-Delta t_0)D_* g_Delta(S)`
` < D_*/S`
` = b_P t_0/S`
` < b_P`,                                                  (6.2)

because `S>t_0` and `g_Delta(S)<1/S`.

The earlier full-core theorem gives

`G_coreavg<=1-b_P`.                                       (6.3)

Hence

`boxed: G_loc<1`.                                         (6.4)

Define the strengthened complete envelope

`boxed: G_run:=min{1,G_coreavg+eta_*+zeta_run}`.           (6.5)

Combining (5.9) and (6.4),

`boxed: G_run>G_loc`.                                     (6.6)

A frozen coefficient strictly beyond the whole incoming complete envelope is

`g_receipt:=G_loc`
` +(1/2)min{zeta_run-zeta_loc,1-G_loc}`.                  (6.7)

Thus

`G_loc<g_receipt<G_run`.                                  (6.8)

The same finite-anchor approximation, connected-core trimming, independent final sprinkling, and concentration argument already established in the previous R16 reports yields:

> **Theorem.** On the unchanged frozen H1--H2--H3 class, for every fixed `g<G_run` and every `p >= (1+epsilon)/lambda(G)`,
>
> `P(L_1(G_p)>=g n)->1`.

No endpoint attainment is claimed.

## 7. B17 — comparison with classical majorization / moment-extreme-point ideas

I searched for the shape of the residual variational problem in classical majorization, moment-set extreme points, isotonic optimization, and order-restricted optimization. Those literatures contain the expected generic tools — Schur/majorization inequalities, extreme-point reductions under finitely many moment constraints, and isotonic projection ideas — but the current feasible set simultaneously has:

1. a **continuum of one-sided lower-prefix constraints** inherited from all certified anchors;
2. monotonicity of the sorted degree profile;
3. a global **upper** `L^2` budget from the spectral norm; and
4. a concave increasing absorption objective.

The bounded search did not surface a theorem whose hypotheses directly identify the exact extreme points of this combined problem. I therefore do **not** claim a novelty certificate or import a black-box finite-plateau theorem.

The useful transfer is conceptual: once the complete deterministic running envelope is retained, the next problem should be attacked as an obstacle/majorization variational problem rather than by introducing yet another arbitrary scalar floor.

## 8. Routes tested but not promoted

- **Finite-plateau KKT claim:** I tried to jump directly to a statement that every extremizer has finitely many plateaus. I do not have a complete proof because the lower-prefix obstacle is a continuum of constraints and the active-set compactness/closure step is nontrivial. No theorem is claimed from this route.
- **Plain Schur-concavity:** concavity of `phi_Delta` alone is insufficient because the feasible relation is not ordinary fixed-sum majorization; it also includes an upper `L^2` budget and one-sided prefix lower bounds. I retained no claim from generic Schur-concavity.
- **Counterexample search against the running-floor step:** the only place a counterexample could enter is if a crossing prefix degree failed to persist into the tail. Sorted order rules this out deterministically: one prefix value above `X` forces every later order statistic to be at least `X`. Thus the new tail integral survives the negation test.

## 9. Status and next obstruction

The H0002 result remains **PARTIAL / source OPEN-looking / ACTIVE**. It is a stronger sufficient-condition theorem on the fixed H1--H2--H3 class; it is not a classification of the broad source Question 5.1.

The supported unchanged count is **0** because the complete envelope moved strictly this run.

The running-floor information at a **single crossing threshold** is now exhausted: finite staircase refinements converge exactly to `J_run`. The next genuine obstruction is the full coupled isotonic problem. In endpoint form, determine the minimum absorption cost over nondecreasing degree profiles `x` subject simultaneously to the complete nested prefix constraints and

`int x(q)^2 dq <= a_P`.                                   (9.1)

A useful next theorem would be either:

- a valid finite-plateau/extreme-point reduction for this obstacle problem; or
- an Euler/KKT-type description that proves the minimizer is the least nondecreasing majorant compatible with the active prefix obstacle plus one quadratic multiplier.

That is qualitatively different from another floor refinement.

## 10. Model / scheduler-control status

This run's actual model identity available to the worker is **GPT-5.6 Sol** and the reasoning level is **UNVERIFIED**. It is not GPT-6 at maximum, so this report does not claim otherwise.

The exposed task-control interface still has no binding model-family selector, no reasoning-effort selector, and no authenticated runtime model/reasoning receipt. GPT-6/maximum therefore remains prompt text only. Enforcing it would require platform-level scheduler fields for model and reasoning effort plus per-run runtime attestation.

The historical P26 `You cannot modify this task` event was authorization-context-specific; the current repository ledger records that a later P26 update succeeded from an authorized context. For any task that still rejects modification, the compliant workaround is the owning authorized workspace/account or platform support, never duplication or permission bypass.

No scheduler change was attempted in this run, consistent with the current owner instruction.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  claim: H0002
  nominal_source: Beck-Fiala discrepancy conjecture
  nominal_metric: complete uniform B(t,n)
  nominal_before: "B(t,n) < 3*sqrt(2*pi*t) for all integer t>=1, all n (current Guo-Fang-Lu preprint baseline)"
  nominal_after: "unchanged"
  nominal_status: KNOWN_CURRENT_PREPRINT_BASELINE
  active_source: "Christoph-Morawski-Wigderson, arXiv:2608.19145v1, Question 5.1"
  active_metric: complete H0002 giant-component envelope
  before: G_loc
  after: "G_run := min{1, G_coreavg + eta_* + zeta_run}"
  movement: "strict; G_run > G_loc"
  active_status: PARTIAL
  source_status: OPEN_LOOKING
  supported_unchanged_count: 0
  methods: [7, 16, 17]
  finite_checker: "none; analytic theorem, no finite core claimed"
  artifacts: []
  shared_root_updates: []
  scheduler_changes: []
  remaining_obligation: >-
    Solve the full coupled isotonic obstacle problem using every nested prefix
    constraint simultaneously with monotonicity and the spectral L2 budget;
    the broad source Question 5.1 remains open-looking and strictly broader.
```
