Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations are presently `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE` and the historical `2/4` is only the frozen handoff value, not a live-candidate score. Free `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: on Talagrand F0111, the thirteen unresolved one-big orbit inequalities `r=2,...,14` collapse to one support-size-free Bernoulli-KL inequality and are all proved; together with the carried `r=1` mixed-face theorem, every one-big stratum of the repaired `theta=4/5` interior candidate is globally certified for all sufficiently small positive epsilon. Methods #2 ATTACK THE NEGATION FIRST, #12 FIND WHAT IS CONSERVED, #21 ASK WHO ELSE HAS THIS SHAPE.**

# R15 retained screen — KL cancellation closes every one-big orbit

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

All Talagrand mathematics below remains **SELF_CHECK_ONLY / NOT CLAIMED**. Nothing here reopens Burdzy–Scheutzow Problem 7.2 after its mandatory six-run handoff, promotes F0111 from `PENDING / NOT READY`, supplies the two independent source-level audits required for closure, or establishes publication novelty.

## 1. Continuity, source fidelity, exclusions, and admission

I continued from the newest complete own report

`runs/R15/20260919_0455Z_successor_screen_f0111_orbit_smoothing_k75v.md`

rather than restarting. I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, the compact current `RESULTS.md`, `QUEUE.md`/admission state, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 handoff

`runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md`,

the newest R15 retained-screen report, current intake/search history, and the newest available coordinator health/admission report.

The current coordinator state has one genuinely admitted new CLOSABLE target, P0219, but it is already exclusively owned by native slot `6aa7ebbe26308191a40003a950a2307a`. The remaining successor gates still have no accepted free CLOSABLE successor. Thus R15 has no lawful new claim to create and its free-admission metric remains

`E_READY_CLOSABLE: 0 -> 0`.

I rechecked the primary Burdzy--Scheutzow PDF, including a page image of the open-problem page. Definition 2.1 says:

- FBM: there are random origins tending to `-infinity` from which the complete centered future is standard Brownian motion;
- BBM: the time-reversed process is FBM;
- 2BM: there exists one random time `S` at which the complete centered future and past are **independent standard Brownian motions**.

Problem 7.2 asks whether FBM + BBM plus independence of the two complete centered half-processes at an arbitrary random time `T` forces 2BM. The source does **not** say that `T` is a stopping time and does **not** separately assume either half at `T` is Brownian. Problem 7.5 is distinct and remains excluded.

The six-run handoff remains controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES candidate had an exact independent seam but was proved actually 2BM. Hence there is no surviving frozen counterexample candidate on which a third or fourth source obligation can honestly be scored.

Fresh public searches dated 2026-09-19 used the exact title/source plus `Problem 7.2`, later-author/citation searches, and the arXiv identifier. They recovered the original paper and citation trail but no accessible later primary source explicitly announcing a resolution of exact Problem 7.2. This is bounded negative evidence only; I do not infer worldwide openness from a search miss.

## 2. Method-history check and why this triple is honest

The F0111 R15 history has already used 28 of the 30 numbered Section-B moves at least once. Repository search showed that the only moves not previously recorded as **tried** on R15's F0111 screen were #2 and #12. I therefore use both now. A third unused number no longer exists for this retained problem, so #21 is the least-structurally-redundant forced reuse: the new reduction is literally a Bernoulli relative-entropy / convex-conjugacy calculation. This triple is not the preceding triple `[14,18,30]`.

The idea was written before the checker: attack the remaining one-big surfaces looking for a support size `r` and scale at which the repaired quadratic drops below the threshold hazard. Instead of producing a counterexample, the dual calculation exposes a cancellation which removes `r` entirely.

## 3. Carried orbit reduction

For the cardinality-two threshold let

`F_n(t)=sum_i t_i - log(1+sum_i(exp(t_i)-1))`.                 (3.1)

The carried `theta=4/5` repaired contact is built at

`q^(epsilon)=(epsilon,...,epsilon,b,b)`,
`b=log 2`, with fourteen small coordinates.                   (3.2)

Its coefficient limits as `epsilon ->0+` are

`alpha_s^* = 2/3 -(4/9)log2`,
`beta_ss^* = 13/45`,
`alpha_b^* = 5/3 - log3/log2`,
`beta_sb^* = 2/9`.                                            (3.3)

The preceding run proved an exact pair-smoothing theorem. Any global minimum of the full repaired gap can be taken so that all positive small coordinates are equal, while the two large coordinates are either equal or one of them is zero. It also globally certified the `r=1` one-small/one-big face. The unresolved one-big branch was therefore exactly thirteen scalar families, `r=2,...,14`.

Fix `r>=2` positive small coordinates, all equal to `x`, put

`s=rx`,
`q_r(s)=r(exp(s/r)-1)`,
`g_r(s)=log(1+q_r(s))`,
`p_r(s)=q_r(s)/(1+q_r(s))`.                                  (3.4)

Set

`a=alpha_b^*=5/3-log3/log2`,
`c=beta_sb^*=2/9`,
`d=1-alpha_s^*=1/3+(4/9)log2`,
`B_r=(13/90)(r-1)/r`.                                        (3.5)

The limiting small-block polynomial-minus-target gap is exactly

`Delta_r(s)=g_r(s)-d s+B_r s^2`.                             (3.6)

If the one active large coordinate has hazard `y`, the remaining full gap is

`Delta_r(s)+w(s)y-Phi(g_r(s),y)`,
`w(s)=a+cs`,                                                  (3.7)

where

`Phi(u,v)=u+v-log(exp(u)+exp(v)-1)`.                          (3.8)

## 4. Method #21 — the one-large optimization is Bernoulli KL

For fixed `g>=0` put `p=1-exp(-g)`. Then

`Phi(g,y)=-log(1-p+p exp(-y))`.                              (4.1)

The derivative in `y` decreases from `p` to `0`. Hence the exact half-line conjugate is

`sup_{y>=0} [Phi(g,y)-w y]`
` =0`,                              if `w>=p`,
` =D(w||p)`,                        if `0<=w<p`,              (4.2)

where

`D(w||p)=w log(w/p)+(1-w)log((1-w)/(1-p))`.                 (4.3)

This is the information-theoretic shape hidden in the previous orbit reduction.

If `w>=p_r`, the carried all-small global theorem already gives `Delta_r>=0`, so the one-big branch is done. Only `w<p_r` needs work.

## 5. Method #12 — exact normalizer cancellation

Write `q=q_r(s)` and `p=q/(1+q)`. Expanding the KL divergence gives

`D(w||p)`
` =w log w +(1-w)log(1-w)-w log q+log(1+q)`.                (5.1)

The same normalizer `log(1+q)` appears in `Delta_r`. It cancels **exactly**:

`Delta_r(s)-D(w||p)`
` =H(w)+w log q-ds+B_r s^2`,                                (5.2)

where

`H(w)=-w log w-(1-w)log(1-w)`.                              (5.3)

This is the conserved quantity of the run: after dualizing in the large coordinate, the entire Poisson-binomial normalizer disappears.

Two elementary inequalities remove the support size:

`q_r(s)>=s`                                                  (5.4)

from `exp(u)-1>=u`, and, for every `r>=2`,

`B_r >= 13/180=:B`.                                         (5.5)

Therefore every unresolved support size obeys the same lower bound

`Delta_r-D(w||p) >= K(s)`,                                  (5.6)

with

`K(s)=H(a+cs)+(a+cs)log s-ds+B s^2`.                        (5.7)

So thirteen scalar inequalities have collapsed to **one** scalar inequality independent of `r`.

## 6. Method #2 — try to make the scalar lower bound fail

The dangerous domain is itself compact.

First,

`q_r(s)<=exp(s)-1`.                                          (6.1)

Indeed, with `u=exp(s/r)-1`, Bernoulli's inequality gives

`exp(s)=(1+u)^r >= 1+ru =1+q_r(s)`.                          (6.2)

Thus

`p_r(s)<=1-exp(-s)<=s`.                                      (6.3)

If `s<=1/10`, then

`w(s)-s=a-(7/9)s >= a-7/90 >0`,                              (6.4)

so `w>p_r`; the KL branch cannot occur. On the other side, `w<p_r<1` forces

`s<s_*:=(1-a)/c`.                                            (6.5)

The exact checker certifies

`413/100 < s_* < 414/100`.                                  (6.6)

Hence a counterexample to (5.6) can only occur on

`1/10 < s < s_* < 4.14`.                                    (6.7)

I then attacked exactly this interval, not sampled path data and not a floating-point Brownian surrogate.

### Exact finite core

Created and executed:

`artifacts/R15/f0111_onebig_uniform_checker_m76a.py`

with archived output

`artifacts/R15/f0111_onebig_uniform_checker_m76a.out`.

The checker uses only `fractions.Fraction`. For every positive rational `x`, it rescales by a power of two to `y in [1,2)` and bounds

`log y = 2 sum_{j=0}^{12} z^(2j+1)/(2j+1) + R`,
`z=(y-1)/(y+1)`,                                             (6.8)

with the exact positive tail bound

`0 <= R <= 2 z^27 / (27(1-z^2))`.                           (6.9)

This also gives rational enclosures for `log2`, `log3`, `a`, `d`, and `s_*`.

On each of 1000 rational boxes partitioning `[1/10,413/100]`, the checker lower-bounds the two entropy terms using concavity (minimum at a box endpoint), lower-bounds `w log s` over its exact rectangle by the minimum of the four corner products, uses `-d s >= -d_hi s_hi`, and `B s^2 >= B s_lo^2`. Every resulting rational lower bound is strictly positive.

Near `w=1`, rather than interval-evaluating `-(1-w)log(1-w)`, drop this nonnegative term and use

`K(s) >= E(s):=w log(s/w)-ds+B s^2`.                        (6.10)

Ten exact rational boxes prove

`E(s)>0` for all `413/100 <= s <= 414/100`.                  (6.11)

Combined with (6.6), this proves

`K(s)>0` throughout the entire possible KL domain.           (6.12)

The archived output ends `ALL_EXACT_CHECKS_PASS`.

### Theorem R15-F0111-ONEBIG-LIMIT

For every integer `r>=2`, the limiting repaired quadratic polynomial globally majorizes `F_{r+1,2}` on the stratum consisting of `r` equal small coordinates and one active large coordinate.

**Proof.** If `w>=p_r`, use the carried global small-face theorem and (4.2). If `w<p_r`, equations (5.2)--(5.7) and the exact certificate (6.12) give strict positive slack after optimizing over every `y>=0`. QED.

Notice that the proof actually treats all `r>=2`, not merely the thirteen values needed for the fourteen-small-coordinate candidate.

## 7. Lift back to the actual interior `epsilon>0` candidate

The preceding theorem is not left as a boundary-only statement.

Let

`alpha_s(epsilon), beta_ss(epsilon), alpha_b(epsilon), beta_sb(epsilon)`

be the actual repaired coefficients. Their exact construction in the earlier report makes them continuous for positive `epsilon` and gives the limits in (3.3). The carried small-face theorem already says that for all sufficiently small positive `epsilon`, every arbitrary small-coordinate face is globally majorized.

Suppose, contrary to the claim, that no sufficiently-small interval of `epsilon` works for all one-big strata. Then there exist `epsilon_n ->0+`, a support size `r in {2,...,14}` after passing to a subsequence, and scales `s_n` on which the optimized one-big gap is negative. Such a failure must lie in the KL branch

`w_epsilon_n(s_n)<p_r(s_n)`.                                (7.1)

For sufficiently small `epsilon`, continuity of the coefficients and the strict margin in (6.4) rule out `s<=1/10`. Also `beta_sb(epsilon)->2/9>0` and `w_epsilon<1` give a uniform upper bound, say `s<5`. Pass to a subsequence `s_n->s_0`.

At the limit,

`1/10 <= s_0`,
`w_0(s_0)<=p_r(s_0)<1`,                                     (7.2)

so `s_0<s_*`. The Bernoulli divergence is continuous on this compact interior domain, and the exact limiting optimized gap is bounded below by `K(s_0)>0`. This contradicts convergence of negative gaps.

Therefore:

### Corollary R15-F0111-ONEBIG-INTERIOR

There exists `epsilon_0>0` such that for every `0<epsilon<epsilon_0`, every one-big orbit of the actual `theta=4/5` repaired fourteen-small/two-large contact is globally valid. The `r=1` orbit was already certified by the preceding rational mixed-face theorem, and this run certifies `r=2,...,14`.

Combined with pair smoothing, **any remaining global failure of this repaired candidate must now have both large coordinates positive and equal** (together with a possibly empty set of equal positive small coordinates). The unrestricted 16-variable search has therefore been reduced from arbitrary directions, then to orbit strata, and now to the equal-two-large branch only.

This is genuine movement of the retained screen, but it is not Talagrand Problem 10.9: it concerns one structured `k=2` contact family and does not provide a universal `gamma` for all cardinality thresholds/bases.

## 8. Current literature / source check

Dated 2026-09-19 queries included:

- `Burdzy Scheutzow Forward Brownian Motion Problem 7.2 arXiv 1302.6958`;
- exact-title / exact-problem-number searches plus later-author/citation searches;
- `Talagrand Are Many Small Sets Explicitly Small Problem 10.9`;
- `Talagrand convexity conjecture k-threshold 2026 Ascoli He Park Talagrand`.

The primary Talagrand PDF confirms Problem 10.9 asks whether one universal `gamma>0` puts every cardinality class `{X: card X>=k}` into `C_gamma`. The current search recovered Ascoli--He--Park--Talagrand, arXiv:2608.11183 (11 August 2026), which reformulates the discrete convexity conjecture through `k`-thresholds and proves broad graph-property classes, but the retrieved abstract does not claim resolution of this exact positive-multilinear Problem 10.9. Older related threshold work (e.g. DeMarco--Kahn and Warnke) also surfaced.

I found no accessible source in this bounded search stating the one-big KL cancellation/certificate above. That is **not** a novelty certificate. Bernoulli KL conjugacy, entropy cancellation and interval arithmetic are standard mechanisms, so publication novelty remains `UNVERIFIED`.

## 9. Artifact receipt

Exact checker source creation commit:

`684f2bf0beed71a926dce2484a80a842ad42d419`

Archived executed output commit:

`01ac3066335717a7c6319795f307503eef3aa612`

The output was read back at that exact commit before this report was written and records:

- `a > 7/90: PASS`;
- `413/100 < s_* < 414/100: PASS`;
- `K(s)>0 on [1/10,413/100]: PASS 1000 boxes`;
- endpoint `E(s)>0 on [413/100,414/100]: PASS 10 boxes`;
- `ALL_EXACT_CHECKS_PASS`.

No numerical Brownian path samples were used anywhere.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  worker: R15
  native_source:
    id: I0076
    citation: "Krzysztof Burdzy and Michael Scheutzow, Forward Brownian Motion, arXiv:1302.6958, Problem 7.2"
    metric: "number of four source-matching obligations proved for one frozen counterexample candidate"
    before: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    after: NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE
    historical_handoff_positive_route: "2/4 frozen; not a live-candidate score"
    status: OPEN / PARTIAL / RETIRED-HANDOFF
    unchanged_count: 6_FROZEN_AT_HANDOFF
    remaining_obligation: "future reassignment requires a new source-valid frozen candidate or a proof covering the source's complete arbitrary-random-time hypotheses"
    evidence:
      - runs/R15/20260916_2354Z_i0076_sixrun_handoff_phasefield_a20.md
    audits: []
  successor_admission:
    E_READY_CLOSABLE_before: 0
    E_READY_CLOSABLE_after: 0
    note: "P0219 is admitted but already exclusively owned by another native slot; no R15 claim created"
  retained_screen:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, Definition 10.1 / Problem 10.9"
    status: PENDING / PARTIAL / SELF_CHECK_ONLY / NOT CLAIMED
    metric_before: "after pair smoothing: r=1 one-big face certified; r=2,...,14 remained as 13 scalar KL inequalities; equal-two-big branch remained"
    metric_after: "all one-big strata r=1,...,14 globally certified for the actual theta=4/5 repaired interior candidate for all sufficiently small epsilon; any remaining failure must lie on an equal-two-big orbit"
    tried_moves:
      - "#2 ATTACK THE NEGATION FIRST"
      - "#12 FIND WHAT IS CONSERVED"
      - "#21 ASK WHO ELSE HAS THIS SHAPE (forced reuse; only #2/#12 were unused in prior F0111 R15 history)"
    remaining_obligation: "prove or refute the equal-two-big orbit family; even success there would only certify this structured k=2 base family, not source Problem 10.9"
    evidence:
      - runs/R15/20260919_0455Z_successor_screen_f0111_orbit_smoothing_k75v.md
      - artifacts/R15/f0111_onebig_uniform_checker_m76a.py
      - artifacts/R15/f0111_onebig_uniform_checker_m76a.out
    audits: []
```

## 11. Next route

Because this run consumes the last two previously unused Section-B numbers for R15/F0111, all 30 methods have now been tried at least once on this retained screen. If no free CLOSABLE successor is admitted by the next invocation, a further F0111 run necessarily has to reuse a method. The mathematically justified next target is narrow: the equal-two-large orbit. The cleanest fresh combination is to deform in the support-size parameter `t=1/r`, find the extremal `t`, and seek a monotone lower envelope for the remaining two-variable gap, rather than returning to another local SDP or serial-Pascal calculation.

## 12. Model / scheduler / permission boundary

The model-control limitation is still unresolved. The exposed scheduler/task surface provides task identity/title, prompt, schedule/timing, enabled state and notification controls, but **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model/effort attestation, and no guaranteed-duration field**. GPT-6/maximum therefore remains prompt-only here; this run actually exposed GPT-5.6 Sol and reasoning is UNVERIFIED.

Changing those unavailable settings would require an authorized product/workspace/admin or backend/API surface which actually persists model and reasoning routing and returns authenticated run telemetry. The historical P26 `You cannot modify this task` response is an authorization/context boundary, not a mathematical blocker; repository history records a later successful P26 update from an authorized P/C context. The lawful workaround is the owning/authorized context or platform support, never task duplication or permission bypass. No scheduler or permission change was attempted in this run.
