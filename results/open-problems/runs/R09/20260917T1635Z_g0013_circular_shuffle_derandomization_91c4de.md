Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — NO MOVEMENT on active R09 successor G0013: `U_* = 1/9 -> 1/9`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported retirement count `6`, and G0002 remains handed off at `Delta_8=UNMEASURED`. Supported unchanged G0013 count: `1 -> 2`. Methods used: B6 DEFORM TO A POINT YOU CAN SOLVE, B10 DERANDOMIZE, B25 COUNT THE SAME THING TWICE.** GPT-6 / maximum was requested in prompt text, but the exposed scheduler surface still has no model-family selector, no reasoning-effort selector, and no authenticated applied-run telemetry, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0013 fourth active run: all circular two-piece shuffles are strictly subextremal

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and controlling state

I did **not** reopen Pengfei Tang Question 4.11. Its periodic-tree work remains retired/frozen in R09 with metric `UNBOUNDED_ABOVE` and supported retirement count `6`. I also did not reopen G0002 / Cerf Conjecture 53.1, which remains handed off at `Delta_8=UNMEASURED`.

The controlling exclusive claim is `operations/claims/G0013.md`. With `lambda=Unif[0,1]`, `nu=lambda tensor lambda`, and

`M = sup_{pi in Pi(lambda,lambda)} W_2^2(pi,nu)`, 

Catalano--Lavenant conjecture `M=1/10`, with the diagonal and antidiagonal maximizers. R09's frozen metric is

`U_* = the smallest rigorous source-valid global upper bound on M established by R09`.

The current full-class theorem from `runs/R09/20260917T1431Z_g0013_chatterjee_jacobi_bound_1f6a93.md` is

`1/10 <= M <= 1/9`.

The newest R09 report `runs/R09/20260917T1530Z_g0013_halfrotation_factorization_2c8f41.md` did not move `U_*`, but proved exactly that the half-rotation shuffle has squared distance `1/20`. This run starts from that state and extends the half-rotation mechanism to the entire circular two-piece family.

### Required repository continuity reads

Before new work I reread/recovered `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the owner directive, the current G0013 claim, the newest R09 G0013 report, the earlier R09 `1/9` proof report, the newest neighboring R08 report, and the historical same-source PROB20-05 reports.

The historical PROB20-05 worker retired this source on 2026-09-16 under a different counterexample-excess metric after six unchanged runs; that worker then rotated away. The later canonical G0013 claim explicitly re-admitted the exact source to R09 with the different global-upper-bound metric `U_*`, so there is no live ownership conflict. Historical PROB20-05 work remains evidence to preserve, including its two-slab and equal `3 x 3` checkerboard theorems.

Large intake JSONL files exceed a single connector rendering; exact-ID/current-claim/prior-attempt searches were used rather than pretending a bytewise visual reread of every intake row.

## 2. Source/current-literature and prior-art check

Primary source: Marta Catalano and Hugo Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034 (2025), Remark 3. It poses the Euclidean quadratic-Wasserstein supremum for two uniform marginals and conjectures the monotone/antimonotone couplings.

Later primary source: Stefan Schrott, *Couplings Farthest from the Independent Gaussian*, arXiv:2609.10467v1, submitted 2026-09-09. Its current abstract still states the uniform assertion as the Catalano--Lavenant conjecture and proves the Gaussian analogue instead.

Fresh bounded searches dated 2026-09-17 used the exact two paper titles, exact arXiv IDs, `Catalano Lavenant uniform copula Wasserstein`, `shuffle of Min Wasserstein independence circular shift copula`, `circular shift copula Wasserstein distance independence`, and `rotation Wasserstein copula diagonal antidiagonal`. They recovered general shuffle-of-Min literature (including Durante--Sarkoci--Sempi 2009 and Mikusinski--Taylor 2010) but no later source-level resolution and no source advertising the circular-shift certificate below. This is bounded negative evidence only; **publication novelty remains UNVERIFIED**.

## 3. New idea before code

The previous run solved only the midpoint

`g_{1/2}(s)=(s+1/2) mod 1`

because in rotated coordinates the target sum and difference variables factorized. For a general cut `c`, that exact target factorization disappears if one insists on using the source sign of `D=Y-X` to select the target branch.

The new idea is to extract a different hidden uniform coordinate from the independent square. In the rotated diamond, **conditional on the sum coordinate, the normalized position across the difference-fiber is uniform and independent of the sum**. That internal uniform variable can deterministically select the two target branches with exactly the desired probabilities for every `c`. This restores enough factorization to build one explicit coupling for the whole family.

That is the B10 derandomization step: no external coin is added; the source square already contains the exact independent coin needed for every cut parameter.

## 4. B6 + B10 — explicit coupling for every circular shuffle

For `0<=c<=1`, define

`g_c(s)=(s+c) mod 1`,

and

`pi_c = Law(S,g_c(S)),   S~Unif[0,1]`.

This is a two-piece orientation-preserving shuffle of Min for `0<c<1`; `c=0` and `c=1` both give the diagonal modulo a null endpoint.

> **Theorem 4.1 (uniform circular-shuffle certificate).** For every `0<=c<=1`,
>
> `W_2^2(pi_c,lambda^2) <= [c^2+(1-c)^2]/10`
>
> `                         = 1/10 - c(1-c)/5`.                (4.1)
>
> In particular, every nontrivial circular shift `0<c<1` is strictly below the conjectured extremal benchmark `1/10`. At `c=1/2`, the bound equals `1/20`, agreeing with the preceding run's exact optimal value.

### Proof

Let `(X,Y)~nu=lambda^2` and set

`Z=X+Y`,  `D=Y-X`.

Then

`X=(Z-D)/2`,  `Y=(Z+D)/2`,

and for any target `(U,V)` with `Z'=U+V`, `D'=V-U`,

`(X-U)^2+(Y-V)^2 = [(Z-Z')^2+(D-D')^2]/2`.                  (4.2)

The source square becomes the diamond

`|D| <= m(Z)`,  where `m(z)=min(z,2-z)`,

with constant `(Z,D)` density `1/2`. Hence, conditional on `Z=z`,

`D | Z=z ~ Unif[-m(z),m(z)]`.

Away from the null endpoints `m(Z)=0`, define

`R = [D+m(Z)]/[2m(Z)]`.

Then `R|Z=z ~ Unif[0,1]` for every `z`. Therefore

`R ~ Unif[0,1]` **and `R` is independent of `Z`**.             (4.3)

Let `H=F_Z(Z)`. Since the triangular law of `Z` is continuous, `H~Unif[0,1]`; because `H` is a function of `Z`, (4.3) implies that `H` and `R` are independent.

Now define the target branch deterministically from the source:

`B = 1_{R<c}`.

Thus `P(B=1)=c`, `P(B=0)=1-c`, and `B` is independent of `H`.

Set

if `B=0`:

`D'=c`,
`Z'=c+2(1-c)H`;                                             (4.4)

if `B=1`:

`D'=-(1-c)`,
`Z'=1-c+2cH`.                                                (4.5)

Because `H` is uniform and independent of `B`, conditional on `B=0`, `Z'` is uniform on `[c,2-c]`; conditional on `B=1`, `Z'` is uniform on `[1-c,1+c]`.

Invert the rotated coordinates:

`U=(Z'-D')/2`, `V=(Z'+D')/2`.

On `B=0`,

`U=(1-c)H in [0,1-c]`,  `V=U+c`.

On `B=1`,

`U=1-c+cH in [1-c,1]`,  `V=U+c-1`.

The branch probabilities exactly match the interval lengths, so `U~Unif[0,1]` and `(U,V)` has law exactly `pi_c`. Thus (4.4)--(4.5) define a valid deterministic transport from the independent square to the circular shuffle.

It remains only to calculate its cost.

## 5. B25 — count the same cost in the sum and difference coordinates

### 5.1 Sum-coordinate cost

The triangular source law is

`f_Z(z)=z` on `[0,1]`, `f_Z(z)=2-z` on `[1,2]`.

For a target uniform interval centered at `1` with half-width `r`, the monotone quantile map driven by `H=F_Z(Z)` is

`Z_r'=1+r(2H-1)`.

Three exact source moments suffice:

`E[(Z-1)^2]=1/6`,
`E[(2H-1)^2]=1/3`,
`E[(Z-1)(2H-1)]=7/30`.                                      (5.1)

For the cross moment, symmetry gives directly

`E[(Z-1)(2H-1)]`
` = 2 int_0^1 (z-1)(z^2-1) z dz`
` = 7/30`.

Therefore

`C_Z(r):=E[(Z-Z_r')^2]`
` = 1/6 - (7/15)r + (1/3)r^2`.                              (5.2)

The branch `B=1` has probability `c` and half-width `c`; branch `B=0` has probability `1-c` and half-width `1-c`. Hence

`E[(Z-Z')^2]`
` = c C_Z(c)+(1-c)C_Z(1-c)`
` = [2c^2-2c+1]/30`.                                        (5.3)

### 5.2 Difference-coordinate cost

Conditional on `Z`, write `m=m(Z)`. Since `D=m(2R-1)` and the target branch is cut at `R=c`, direct exact integration gives

`E[(D-D')^2 | m]`
` = int_0^c [m(2r-1)+(1-c)]^2 dr`
`   + int_c^1 [m(2r-1)-c]^2 dr`
` = m^2/3 + c(1-c)(1-2m)`.                                  (5.4)

Because `f_Z(z)=m(z)`,

`E[m]=2 int_0^1 z^2 dz = 2/3`,
`E[m^2]=2 int_0^1 z^3 dz = 1/2`.                            (5.5)

Averaging (5.4),

`E[(D-D')^2]`
` = 1/6 - c(1-c)/3`
` = [2c^2-2c+1]/6`.                                         (5.6)

### 5.3 Total cost

Using (4.2), (5.3), and (5.6), the cost of the explicit coupling is

`(1/2){ [2c^2-2c+1]/30 + [2c^2-2c+1]/6 }`
` = [2c^2-2c+1]/10`
` = [c^2+(1-c)^2]/10`
` = 1/10 - c(1-c)/5`.                                       (5.7)

Since Wasserstein cost is the infimum over all couplings, (5.7) proves (4.1). For `0<c<1`, the certified gap from the diagonal benchmark is strictly positive:

`1/10 - coupling_cost = c(1-c)/5 > 0`.                       (5.8)

QED.

## 6. Corollary — complete two-piece positive-orientation shuffle class

A nonidentity orientation-preserving interval exchange of `[0,1]` with exactly two continuity intervals must swap those two intervals. If the cut is at `a`, length preservation forces the map to be

`s -> s+(1-a)` on `[0,a)`,
`s -> s-a` on `[a,1)`,

which is exactly `g_c(s)=(s+c) mod 1` with `c=1-a`.

Therefore Theorem 4.1 controls the **entire two-piece positive-slope shuffle-of-Min class**: every nonidentity member has a strict explicit certificate below `1/10`. The previous exact half-rotation theorem is the symmetric point `a=c=1/2` of this complete family.

This remains a restricted-family result. It does not cover two-piece shuffles with a reflected piece, shuffles with three or more pieces, or arbitrary copulas, so it is **PARTIAL**, not source closure.

## 7. Exact self-check

The proof and coupling were derived before code. I then executed the exact-rational self-check

`artifacts/R09/20260917T1635Z_g0013_circular_shuffle_exact.py`

which verifies the scalar moments (5.1), the `m` moments (5.5), the polynomial identities (5.3), (5.6), (5.7), the benchmark gap (5.8), and the midpoint value `1/20`. It uses `fractions.Fraction` only.

Source creation commit: `ac45a0258cefd3915d020eb49f6765121e32704e`.

Executed output:

`artifacts/R09/20260917T1635Z_g0013_circular_shuffle_exact.out`

creation commit `08571d382069c780a113eff2238df52dc1b79081`; output ends

`SELF_CHECK_ONLY`
`PASS`.

The self-check certifies algebra only. The pushforward/coupling argument is the written proof above; this is not an independent audit.

## 8. Method outcomes

**B6 — DEFORM TO A POINT YOU CAN SOLVE: SUCCESS.** The previously solved `c=1/2` factorization point was deformed to every `c in [0,1]`. The obstruction at general `c` was not the family itself, but the old choice of branch variable.

**B10 — DERANDOMIZE: SUCCESS.** The normalized fiber coordinate `R=(D+m(Z))/(2m(Z))` is an internal uniform variable independent of the sum coordinate. It deterministically supplies exactly the Bernoulli(`c`) branch choice needed for the target; no external randomization is required.

**B25 — COUNT THE SAME THING TWICE: SUCCESS.** In `(Z,D)` coordinates the same transport cost becomes two one-dimensional exact moment calculations sharing the factor `2c^2-2c+1`, yielding the compact certificate (5.7).

Repository searches for prior method labels did not surface B6/B10/B25 in the historical PROB20-05 method triples; the immediately preceding R09 triple was B5/B24/B13, so no preceding triple is repeated.

## 9. Metric and status

The frozen **global** metric does not move:

`U_* : 1/9 -> 1/9`.

The new theorem controls a complete nontrivial shuffle subclass, but it is not a new global upper bound. G0013 therefore remains **OPEN_CURRENT / PARTIAL**.

Supported consecutive unchanged G0013 runs are now

`1 -> 2`.

A third consecutive unchanged run would trigger the owner's Section-I stuck protocol. This report does not pre-emptively relabel the restricted theorem as movement of `U_*`.

## 10. Next genuinely different methods

If G0013 remains active next run, do not repeat B6/B10/B25. The most useful new triple is:

- **B7 TAKE THE LIMIT:** make the all-grid checkerboard reduction explicit: prove that a uniform `1/10` bound for every finite permutation checkerboard at every grid size implies the full continuous source statement by Birkhoff plus checkerboard approximation;
- **B23 DO WHAT THE PROPOSER DID NOT EXPECT:** attack the smallest mixed-orientation two-piece shuffles, where one piece is reflected, as a possible counterexample mechanism rather than assuming monotone pieces are worst;
- **B27 SWAP THE QUANTIFIERS:** seek one transport construction that works uniformly for every grid permutation and every `n`, rather than solving a new finite optimizer separately for each permutation.

If that run also leaves `U_*` at `1/9`, it must be a formal Section-I stuck run under the three-unchanged rule, with the exact blocking inequality and one permitted recovery choice.

## 11. Model / scheduler control status

The limitation remains exactly the one recorded in the current policy and ledger. The exposed task-management schema provides title, prompt, schedule/start-offset, enabled state, and timing mode. It provides **no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry**. Thus GPT-6/maximum remains a prompt request here, not an enforceable or verifiable runtime setting.

Making it enforceable requires product/API fields selecting model and reasoning effort plus applied-run telemetry, or administration through an authorized owning surface that exposes those controls.

The historical P26 `You cannot modify this task` response was authorization-context-specific; repository evidence records a later successful P26 update from another authorized context. The lawful workaround is the owning authorized context, ownership/admin transfer, or platform support. It is not task duplication, permission bypass, or a repository-only edit.

No scheduler modification, email, Drive write, public posting, purchase, permission change, workflow execution, shared-root edit, or peer-file edit was performed in this run.

## 12. Structured ledger_delta

```json
{
  "track": "R09",
  "predecessors": {
    "Tang-2020-Q4.11": {
      "metric": "UNBOUNDED_ABOVE",
      "status": "RETIRED_FROZEN",
      "supported_retirement_count": 6
    },
    "G0002": {
      "metric": "Delta_8=UNMEASURED",
      "status": "HANDOFF_FROM_R09"
    }
  },
  "active": {
    "target": "G0013 / Catalano-Lavenant uniform-copula Wasserstein conjecture",
    "metric": "U_* = smallest rigorous source-valid global upper bound on M",
    "before": "1/9",
    "after": "1/9",
    "movement": "NO_MOVEMENT",
    "supported_unchanged_runs_on_G0013": {
      "before": 1,
      "after": 2
    },
    "status": "PARTIAL_OPEN_CURRENT",
    "new_restricted_theorem": "For pi_c=Law(S,(S+c) mod 1), W2^2(pi_c,lambda^2) <= [c^2+(1-c)^2]/10 = 1/10-c(1-c)/5; hence every nonidentity two-piece positive-orientation shuffle is strictly subextremal.",
    "source_bracket": "1/10 <= M <= 1/9",
    "next_stuck_trigger": "one further supported unchanged run"
  },
  "methods": [6,10,25],
  "model": "GPT-5.6 Sol",
  "reasoning": "UNVERIFIED"
}
```
