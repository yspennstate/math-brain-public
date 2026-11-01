Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO NATIVE I0076 SOURCE-METRIC MOVEMENT: Burdzy–Scheutzow Problem 7.2 remains `OPEN / PARTIAL / RETIRED-HANDOFF`; no frozen counterexample candidate survives, so the four source-matching obligations remain `NOT_SCOREABLE_NO_SURVIVING_FROZEN_CANDIDATE`, and the historical `2/4` is only the frozen handoff value. Free `E_READY_CLOSABLE: 0 -> 0`. RETAINED-SCREEN MOVEMENT: the last unresolved equal-two-large orbit family of the Talagrand F0111 `theta=4/5` boundary-limit quadratic is proved globally for every small-coordinate support size; combined with the carried pair-smoothing, small-face, and one-big theorems, this proves a dimension-free **boundary-limit** positive quadratic majorant for every heterogeneous cardinality-two hazard. Methods #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #24 FIND THE EXTREMAL OBJECT, #25 COUNT THE SAME THING TWICE.**

# R15 retained screen — the equal-two-large branch closes in the boundary limit

Date checked: 2026-09-19 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.  
Worker: R15, CLOSABLE OUTSIDE.

Everything concerning Talagrand below is **SELF_CHECK_ONLY / NOT CLAIMED**. It does not reopen Burdzy–Scheutzow Problem 7.2, promote F0111 from successor-screen status, establish a positive-epsilon interior certificate, establish publication novelty, or satisfy the two-independent-audit closure rule.

## 1. Continuity, source fidelity, exclusions, and admission

I continued from

`runs/R15/20260919_0605Z_successor_screen_f0111_onebig_uniform_m76a.md`

rather than restarting. Before new mathematics I reread/recovered the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, the controlling I0076 six-run handoff, the newest own report, neighboring F0111 history, and current admission/ownership deltas. The very large intake JSONL family remains connector-display-limited, so I do not claim that every one of its roughly 780 records was rendered verbatim; I targeted I0076, its Burdzy--Scheutzow neighbors, the currently admitted successor deltas, and the ownership registry.

The newest reconciled task-health evidence still certifies zero **free** READY+CLOSABLE successors. P0219 did cross admission, but it crossed together with an exclusive claim by another native slot. No claim release or transfer to R15 was found. Hence

`E_READY_CLOSABLE: 0 -> 0`,

and I created no successor claim and edited no shared root.

### Exact Burdzy--Scheutzow source

I rechecked the primary *Forward Brownian Motion* PDF (arXiv:1302.6958), Definition 2.1 and Problem 7.2.

- FBM means there exist random origins tending to `-infinity` from which the complete centered future is standard Brownian motion.
- BBM means the time-reversed process is FBM.
- 2BM means there is one random time `S` at which the complete centered future and past are **independent standard Brownian motions**.
- Problem 7.2 assumes FBM + BBM and existence of an arbitrary random time `T` at which the two complete centered half-processes are independent. It does **not** say that `T` is a stopping time and does **not** separately assume either half at `T` is Brownian.
- Problem 7.5 is a different question and remains excluded.

The mandatory six-run handoff remains controlling. The source-Theorem-6.1 candidate had FBM, BBM and non-2BM but no source-valid independent seam. The later Brownian-prefix/BES candidate had the independent seam but was proved actually 2BM. Thus there is no surviving frozen counterexample candidate on which the requested four-obligation metric can honestly move.

Fresh dated public searches on 2026-09-19 used the exact title, arXiv identifier, `Problem 7.2`, later-author/citation terms, and the exact Talagrand Problem 10.9 title/number. They recovered the original Brownian source and current Talagrand follow-up literature but no accessible later primary source explicitly announcing a resolution of exact Burdzy--Scheutzow Problem 7.2. This is bounded negative evidence only.

## 2. Carried retained-screen state

For the cardinality-two threshold write

`F_n(t)=sum_i t_i - log(1+sum_i(exp(t_i)-1))`.                 (2.1)

The carried repaired contact is built at

`q^(epsilon)=(epsilon,...,epsilon,b,b)`, `b=log 2`,            (2.2)

with `m` symmetric small coordinates and two symmetric large coordinates. In the boundary limit `epsilon -> 0+`, its coefficients are

`alpha = 2/3 -(4/9)log2`,
`beta_s = 13/45`,
`a = 5/3 - log3/log2`,
`c = 2/9`,
`beta = [log3 -(4/3)log2]/(log2)^2`.                          (2.3)

Thus, with

`X=sum_i x_i`, `Q=sum_{i<j}x_i x_j`,

the limiting positive quadratic is

`P_m(x,y,z)`
` = alpha X + beta_s Q`
`   + a(y+z) + beta y z + c X(y+z)`.                          (2.4)

The preceding reports established, SELF_CHECK_ONLY:

1. `beta_s>1/6` and `beta>1/6`, so the exact pair-smoothing theorem applies independently inside the small orbit and the two-large orbit;
2. the whole arbitrary small-coordinate face is globally majorized;
3. every one-large branch is globally majorized for every positive-small support size, via the Bernoulli-KL cancellation;
4. therefore a failure of the limiting polynomial, if one exists, can be reduced to `r` equal positive small coordinates and **two equal positive large coordinates**.

That last family is the only branch attacked in this run.

## 3. Exact equal-two-large gap

Take `r>=1` positive small coordinates, all equal to `x`, and put

`s=rx`,
`q_r(s)=r(exp(s/r)-1)`,
`B_r=(13/90)(r-1)/r`,
`d=1-alpha=1/3+(4/9)log2`.                                   (3.1)

Set both large coordinates equal to `y`. Direct subtraction of (2.1) from (2.4) gives the exact gap

`G_r(s,y)`
` = log(q_r(s)+2exp(y)-1)`
`   - d s + B_r s^2`
`   + 2(a+cs-1)y + beta y^2`.                                (3.2)

For `r=0`, use the same formula with `s=0` and no small terms.

For every `r>=2`,

`q_r(s)>=s`,
`B_r>=13/180=:B`.                                             (3.3)

Writing

`A=2exp(y)-1`,                                                (3.4)

we therefore have

`G_r(s,y) >= h(y)+L(s,y)`,                                   (3.5)

where

`h(y)=log A+2(a-1)y+beta y^2`,                               (3.6)

`L(s,y)=log(1+s/A)+[-d+(4/9)y]s+B s^2`.                      (3.7)

This is Method #25: count the same gap in two pieces. The large-coordinate contact geometry is all in `h`; the support-size-free small/large coupling is all in `L`.

## 4. The pure two-large term is nonnegative

Let `b=log2`. From the definitions in (2.3), exact substitution gives

`h(0)=0`, `h(b)=0`, `h'(b)=0`, `h'(0)=2a>0`.                 (4.1)

The last inequality is equivalent to `5 log2>3 log3`, i.e. `32>27`.

Moreover

`h''(y)=2 beta - 2exp(y)/(2exp(y)-1)^2`.                      (4.2)

The second term in (4.2) is strictly decreasing in `y`, so `h''` is strictly increasing. At `y=b`,

`h''(b)=2(beta-2/9)>0`.                                      (4.3)

For the strict sign it is enough to show

`9log3-12log2-2(log2)^2>0`.                                  (4.4)

The exact checker below certifies `log3>109/100` and `log2<7/10`, which leave the rational margin

`9(109/100)-12(7/10)-2(7/10)^2=43/100>0`.                   (4.5)

Since `h''` is strictly increasing, `h'` first decreases and then increases. It starts positive and equals zero at `b`; (4.3) puts `b` on its increasing side. Hence `h` rises from `h(0)=0`, can only turn down toward `h(b)=0`, and then rises for `y>b`. Therefore

`h(y)>=0` for all `y>=0`.                                    (4.6)

## 5. Method #24/#5 — find and differentiate the exact `y`-extremizer of `L`

For fixed `s>0`,

`partial_y L`
` = s[4/9 -(A+1)/(A(A+s))]`.                                (5.1)

The ratio `(A+1)/(A(A+s))` is strictly decreasing in `A`, hence in `y`.

### Case 1: `s>=7/2`

At `A=1`, the ratio is `2/(1+s)<=4/9`, so the minimum occurs at `y=0`. Thus

`L(s,y)>=L(s,0)=log(1+s)-ds+B s^2`.                          (5.2)

For `s>=7/2`,

`d^2/ds^2 L(s,0)=-1/(1+s)^2+2B>0`.                           (5.3)

At `s=7/2`, the exact rational/log bounds in the checker give

`L'(7/2,0)>1/12`,
`L(7/2,0)>11/1200`.                                          (5.4)

Hence `L(s,y)>0` throughout this case.

### Case 2: `0<s<7/2`

There is one interior minimizing `A in (1,3)`, determined exactly by

`4A(A+s)=9(A+1)`,
`s=(3-A)(4A+3)/(4A)`.                                       (5.5)

Let `m(s)=min_y L(s,y)`. The envelope theorem gives `m'(s)=partial_s L` at this minimizer. Put

`x=(A+1)/4 in (1/2,1)`.                                     (5.6)

Then

`s=(1-x)(16x-1)/(4x-1)`                                     (5.7)

and a direct simplification yields

`m'(s)=J(x)`
` = (4/9)log x -(1-x)/(9x)`
`   +(13/90)(1-x)(16x-1)/(4x-1)`.                            (5.8)

Now set `z=(x-1)/(x+1)`, so `-1/3<=z<=0`. The atanh series gives the rigorous lower bound

`log x`
` >=2(z+z^3/3)+2 z^5/[5(1-z^2)]`.                           (5.9)

Substituting (5.9) into (5.8) and simplifying exactly gives

`J(x) >= (1-x) P(x) / [270 x (x+1)^3(4x-1)]`,               (5.10)

where

`P(x)=576x^5+637x^4+129x^3-459x^2+155x+42`.                 (5.11)

For `1/2<=x<=1`,

`P(x)>=Q(x):=-(653/4)x^2+155x+42`.                           (5.12)

Indeed, use `x^3>=x^2/2`, `x^4>=x^2/4`, and `x^5>=x^2/8`. The quadratic `Q` is concave, so its minimum on the interval is at an endpoint. The exact checker certifies

`Q(1)=135/4>0`,
`Q(1/2)=1259/16>0`.                                         (5.13)

Thus `m'(s)>=0`. Since `m(0)=0`,

`L(s,y)>=m(s)>=0` for `0<s<7/2`.                             (5.14)

Combining the two cases,

`L(s,y)>=0` for all `s,y>=0`.                                (5.15)

Equations (3.5), (4.6), and (5.15) prove `G_r>=0` for every `r>=2`.

## 6. The exceptional support size `r=1`

For one positive small coordinate,

`q_1(s)=exp(s)-1`, `B_1=0`.                                  (6.1)

The exact gap still splits as

`G_1(s,y)=h(y)+L_1(s,y)`,                                    (6.2)

where

`L_1(s,y)`
` =log(1+(exp(s)-1)/A)+[-d+(4/9)y]s`.                        (6.3)

Differentiate in `s`:

`partial_s L_1`
` = exp(s)/(A+exp(s)-1)-d+(4/9)y`.                           (6.4)

The first term in (6.4) is increasing in `s`, because its derivative is

`exp(s)(A-1)/(A+exp(s)-1)^2>=0`.                             (6.5)

It therefore suffices to check `s=0`. Define

`f(y)=1/A-d+(4/9)y`.                                         (6.6)

Then

`f'(y)=4/9-2exp(y)/(2exp(y)-1)^2`.                           (6.7)

Writing `t=exp(y)>=1`, the critical-point equation is

`8t^2-17t+2=0`,                                              (6.8)

whose roots are exactly `1/8` and `2`. Hence the unique admissible minimum is `t=2`, i.e. `y=log2`, and direct substitution gives

`f(log2)=0`.                                                  (6.9)

Thus `partial_s L_1>=0`, `L_1(0,y)=0`, and

`L_1(s,y)>=0`.                                                (6.10)

Together with `h>=0`, this proves `G_1>=0`. The case `r=0` is exactly `G_0=h>=0`.

## 7. New theorem: a dimension-free boundary-limit quadratic majorant for `k=2`

### Theorem R15-F0111-K2-BOUNDARY-QUADRATIC

For every integer `m>=0`, define `P_m` by (2.4). Then

`P_m(x_1,...,x_m,y,z) >= F_{m+2,2}(x_1,...,x_m,y,z)`          (7.1)

for all nonnegative coordinates.

**Proof.** Use the carried pair-smoothing theorem inside the symmetric small-coordinate orbit and the two-large orbit. Since `beta_s=13/45>1/6` and the carried exact certificate gives `beta>1/6`, repeated smoothing/deletion reduces any possible failure to one of three types:

1. no positive large coordinate: covered by the carried dimension-free small-face theorem;
2. exactly one positive large coordinate: covered by the carried one-big Bernoulli-KL theorem for every support size;
3. two positive large coordinates, equal after smoothing, with `r` equal positive small coordinates: covered by Sections 3--6 of this report for every `r>=0`.

All reduced branches are nonnegative, so no failure exists. QED.

The polynomial is not merely an arbitrary upper envelope: it is the `epsilon->0+` limit of the repaired exact-contact family and has exact value and first-order contact at the boundary base

`(0,...,0,log2,log2)`.                                       (7.2)

This is the strongest clean retained-screen theorem on this route so far. It is nevertheless **not Talagrand Problem 10.9**. The source asks for one universal positive `gamma` for all cardinality thresholds and all bases, while (7.1) concerns the `k=2` hazard and is a boundary-limit certificate. In particular, this report does not yet prove that the actual positive-`epsilon` exact-contact polynomial is globally valid.

The next real obstruction is therefore specific: lift (7.1) from the boundary to a fully interior exact-contact family without losing the support-size-free inequalities. A naive coefficientwise continuity argument is insufficient on noncompact coordinate space and would not be accepted as a proof.

## 8. Exact finite core

Idea first, checker second. After the analytic route above was complete I created and executed

`artifacts/R15/f0111_twobig_limit_checker_n77b.py`

and archived

`artifacts/R15/f0111_twobig_limit_checker_n77b.out`.

Source commit: `8667768b26cb3f692cf29129eaabe6d4fdd79c11`.  
Output commit: `833b312e4cfd1d5b1adaed674d1464188b1acdd1`.

The checker uses `fractions.Fraction` only. It certifies the exponential/logarithm bounds used in (4.5), the strict `beta>2/9` margin `43/100`, the two endpoint values in (5.13), the positive `s=7/2` margins in (5.4), and the exact roots in (6.8). The archived output was read back at its exact commit and ends

`ALL_EXACT_CHECKS_PASS`.

This checker certifies only the finite rational/log-bound core. The theorem-sized argument is the written proof in Sections 3--7, not a numerical sample.

## 9. Current literature / prior-art check

Dated 2026-09-19 searches included:

- `Burdzy Scheutzow Forward Brownian Motion Problem 7.2 arXiv 1302.6958` and exact-title/problem-number variants;
- later-author/citing-paper searches around exact Problem 7.2;
- `Talagrand Are Many Small Sets Explicitly Small Problem 10.9`;
- `Talagrand k-threshold Ascoli He Park Talagrand 2026`;
- Chen Li `On p-Spread Measures` / arXiv:2609.08967;
- Jinyoung Park `dimension-free comparison expectation thresholds fractional expectation thresholds` / arXiv:2609.14681.

The primary Talagrand PDF still states Problem 10.9 in the positive-multilinear `C_gamma` formulation. Ascoli--He--Park--Talagrand (arXiv:2608.11183, 11 August 2026) reformulate the broader discrete convexity conjecture via `k`-thresholds and prove substantial graph classes, but their abstract does not claim the full conjecture. Li (arXiv:2609.08967, 8 September 2026) states a solution of a **fractional** version. Park (arXiv:2609.14681, 13 September 2026) gives a dimension-free comparison explicitly described as a bound **toward** the conjecture. I found no accessible source in this bounded search stating Theorem R15-F0111-K2-BOUNDARY-QUADRATIC.

That search miss is not a novelty certificate. The proof uses elementary convexity, pair smoothing, and one-variable inequalities, so **publication novelty remains UNVERIFIED**.

## 10. Model / scheduler control

The operative implementation manifest remains unchanged on the requested control issue. The exposed scheduler surface provides task identity/title, prompt, schedule/timing mode, enabled state and notification-related controls, but no binding model-family selector, no reasoning-effort selector, no authenticated applied-model/effort receipt, and no guaranteed hour-long execution field. Therefore `GPT-6 / maximum` remains prompt text only in this run.

The historical P26 ID `6aa7b43682948191b697d72fec69d539` returned `You cannot modify this task` in the recorded unauthorized context. The boundary was not bypassed; later repository continuity records successful action only from an authorized P/C context. A real GPT-6/maximum guarantee would require an owning/authorized or owner/admin product/backend/API surface that persists those routing fields and attests them after execution.

No scheduler, permission, email, Drive, public-posting, purchase, or shared-root change was attempted.

## 11. Structured ledger delta

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
    status: "OPEN / PARTIAL / RETIRED-HANDOFF"
    unchanged_count: "6_FROZEN_AT_HANDOFF"
    remaining_obligation: "requires a genuinely new surviving source-valid candidate or a complete implication proof; retirement remains controlling"
  successor_admission:
    free_ready_closable_before: 0
    free_ready_closable_after: 0
    claim_created: false
    reason: "newly admitted closable work is already exclusively owned; no release to R15 found"
  retained_screen:
    id: F0111
    source: "Michel Talagrand, Are Many Small Sets Explicitly Small?, Problem 10.9"
    status: "PENDING / NOT READY / SELF_CHECK_ONLY / NOT CLAIMED"
    movement: true
    result: "dimension-free boundary-limit positive quadratic majorant for every heterogeneous k=2 hazard"
    new_branch_closed: "equal-two-large orbit for every small support size r>=0"
    remaining_obligation: "lift boundary-limit majorant to an actual fully interior exact-contact global certificate, then connect any k=2 result to source-uniform gamma/all-k scope"
  tried_moves:
    - "#5 ADD A PARAMETER AND DIFFERENTIATE IN IT"
    - "#24 FIND THE EXTREMAL OBJECT"
    - "#25 COUNT THE SAME THING TWICE"
  evidence:
    - "runs/R15/20260919_0605Z_successor_screen_f0111_onebig_uniform_m76a.md"
    - "artifacts/R15/f0111_twobig_limit_checker_n77b.py @ 8667768b26cb3f692cf29129eaabe6d4fdd79c11"
    - "artifacts/R15/f0111_twobig_limit_checker_n77b.out @ 833b312e4cfd1d5b1adaed674d1464188b1acdd1; ALL_EXACT_CHECKS_PASS"
    - "Burdzy--Scheutzow primary PDF checked 2026-09-19"
    - "Talagrand primary Problem 10.9 PDF checked 2026-09-19"
    - "Ascoli--He--Park--Talagrand arXiv:2608.11183 checked 2026-09-19"
    - "Li arXiv:2609.08967 checked 2026-09-19"
    - "Park arXiv:2609.14681 checked 2026-09-19"
  audit_ids: []
  novelty: UNVERIFIED
  next_methods: [6, 13, 29]
```

Next route: **#6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY**. The concrete target is an interior-lift theorem which uses exact contact at `s=m epsilon, y=log2` rather than a nonuniform coefficientwise continuity argument.
