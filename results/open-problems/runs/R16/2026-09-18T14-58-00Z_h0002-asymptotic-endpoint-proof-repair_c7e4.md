Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. CORRECTION + CERTIFIED METRIC MOVEMENT:** the two newest no-`H3` / coarse-block endpoint reports used an invalid aggregation step; on the canonical frozen `H1`–`H2`–`H3` class, the last fully supported fixed-split bound `rho*(q_64-q0/64)` is improved to `rho*(q_128-q0/64)`, and a valid variable split gives `rho*(q_inf-q0/64)-O_epsilon(rho/sqrt(lambda))`; Section-B methods actually used: **#9 RANDOMIZE, #12 FIND WHAT IS CONSERVED, #29 ADD THE POINTS AT INFINITY**.

# R16 — H0002: repair the coarse-block gap and recover the endpoint asymptotically

## 1. Continuity, ownership, required reads, and current source

This run continues the active R16 HARD OUTSIDE claim `H0002`, Question 5.1 of Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026). It does **not** restart the stale Beck--Fiala scheduler title, reopen H0022, or invent a switch to the inconsistent second claim `H0018`.

Before doing mathematics I reread/reconciled:

- `probability_campaign_2026_09/INDEX.md`;
- `probability_campaign_2026_09/RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/claims/H0002.md`;
- the H-intake source record for H0002;
- the newest own report `runs/R16/2026-09-18T13-45-29Z_h0002-exact-endpoint-one-over-n-sprinkling_7f2b.md`;
- the newest same-source neighboring terminal/handoff records for G0010 (Question 5.2) and G0011 (Conjecture 5.3).

The canonical claim fixes, for `0<epsilon<=1`, `0<rho<=1`, `kappa>0`, `n=|G|`, `lambda=lambda(G)`,

`q0 := 1-exp(-epsilon^2/288)`,
`alpha := q0*rho/64`,

and the class

**(H1)** `lambda(G-S) >= (1-epsilon/8)*lambda` for every `|S|<=rho*n`;

**(H2)** `e_G(A,B) >= kappa*lambda*n` for every disjoint `A,B` with `|A|,|B|>=alpha*n`;

**(H3)** `lambda(G)->infinity`.

The tracked quantity is the largest explicit giant fraction certified uniformly on that frozen class at every

`p >= (1+epsilon)/lambda(G)`

with probability bounded below by a positive constant depending only on the frozen parameters.

Fresh primary-source/title/author searches on 18 Sep 2026 still found arXiv:2608.19145v1 as the current CMW version and did not find a later paper explicitly resolving Question 5.1. This is a bounded current-status check, not a novelty certificate.

## 2. A necessary correction to the preceding two reports

The reports

- `2026-09-18T12-42-44Z_h0002-coarse-block-sprinkling-no-h3_4d8c.md`, and
- `2026-09-18T13-45-29Z_h0002-exact-endpoint-one-over-n-sprinkling_7f2b.md`

grouped many **disconnected first-round components** into conceptual macroblocks `B_i`, then argued that one second-round edge between each consecutive pair `B_i,B_(i+1)` connects all the weight in the chain.

That inference is false. A union of first-round components is not connected merely because it is called a block. One link between two blocks joins only the two first-round components incident to that link.

The exact four-vertex obstruction is archived in

`artifacts/R16/2026-09-18T14-58-00Z_h0002_coarse_block_obstruction_checker.py`

with output

`artifacts/R16/2026-09-18T14-58-00Z_h0002_coarse_block_obstruction_checker.out`.

It has conceptual blocks `{0,1}` and `{2,3}`, one inter-block sprinkling edge `0--2`, total block weight `4`, but largest actual connected weight `2`. The checker ends `ALL_EXACT_CHECKS_PASS`.

Therefore I withdraw the **proof** of the no-`H3` coarse-block theorem and the claimed exact endpoint based on that theorem. This is a proof correction, not a counterexample to H0002 or to the theorem statement itself.

The last fully supported R16 gluing argument before that gap is the all-cut argument in the 11:42 report: it contracts **actual** first-round connected components, unions over all cuts of those contracted vertices, and uses H3 to make the cut entropy `exp(O(n/lambda))` negligible against a fixed positive sprinkling exponent `exp(-Theta(n))`.

## 3. Notation for the repaired family

Put

`a := 1-epsilon/8`,

`eta_inf := (1+epsilon)*a - 1 = epsilon*(7-epsilon)/8`,

`q_inf := 1-exp(-eta_inf^2/18)`.

For a fixed integer `M>=2` define a reserve

`theta_M := epsilon/M`,

a first-round margin

`eta_M := (1+epsilon-theta_M)*a - 1
        = eta_inf-a*epsilon/M`,

and

`q_M := 1-exp(-eta_M^2/18)`.

The valid 11:42 split is `M=64`, so its metric is

`g_64 := rho*(q_64-q0/64)`.

This run will prove the strictly stronger concrete certified value

`g_128 := rho*(q_128-q0/64)`,

and then prove a variable-split theorem approaching the endpoint at an explicit `lambda^(-1/2)` rate.

Since

`eta_128-eta_64 = a*epsilon/128 > 0`,

we have `q_128>q_64`, so this is genuine movement of the supported frozen-class metric.

## 4. Method #9 — randomize the macroblocks, and find why that still does not repair them

I first tried the most direct repair of the coarse-block idea: randomly partition the successful first-round components into a bounded number of macroscopic bins, then sprinkle one or several random links between bins.

This does **not** solve the logical problem. Random assignment changes which disconnected components receive the same label; it does not create internal paths inside a bin. Even if every pair in a prescribed bin-chain receives at least one open edge, the selected edges can repeatedly hit only one component in each bin.

The exact obstruction in Section 2 survives every deterministic or random binning scheme unless the scheme separately proves that each bin has become internally connected. Thus the right state space is not “macroblocks as sets”; it is the weighted graph whose vertices are the **actual first-round components**.

This failed attack is useful because it identifies precisely what the repair must preserve.

## 5. Method #12 — the conserved object is actual cut capacity on the component quotient

Let the successful first-round connected components be `C_1,...,C_m`, with weights `w_i=|C_i|`. After contraction, any second-round connected component is a union of these quotient vertices.

The key conserved fact is:

> if a quotient cut `(I,I^c)` has vertex weights at least `alpha*n` on both sides, then the corresponding original vertex sets
> `A=union_(i in I) C_i`, `B=union_(i notin I) C_i`
> satisfy the same H2 capacity
> `e_G(A,B) >= kappa*lambda*n`.

No conceptual grouping is used here.

This is exactly why the older all-cut proof is sound: if no second-round component carries all but `alpha*n` of the seed mass, the deterministic balanced-cut lemma produces a cut of **actual second-round components** with at least `alpha*n` on both sides. That cut is, in turn, a cut of the initial quotient vertices. We may union-bound over the at most `2^m` such cuts.

### 5.1 Fixed-split theorem: a new certified concrete metric

Take

`p=(1+epsilon)/lambda`

(the monotone endpoint), and split

`p1=(1+epsilon-epsilon/128)/lambda`,

`1-p=(1-p1)(1-p2)`.

Then

`p2 >= epsilon/(128*lambda)`.

As long as fewer than `rho*n` vertices have been deleted, H1 gives

`p1*lambda(G-S) >= 1+eta_128`.

Apply CMW Lemma 3.1(b) at the Perron-maximizing residual vertex. With

`s_128 := (a*eta_128/6)*lambda`,

the next first-round component is larger than `s_128` with conditional probability at least

`q_128=1-exp(-eta_128^2/18)`.

The endpoint adaptive seed lemma proved in the 11:42 report is valid independently of the later coarse-block gap. Applying it with success probability `q_128`, deletion budget `R=rho*n`, and threshold `s_128` gives a constant

`c_seed(epsilon)>0`

such that with probability at least `c_seed`, the union `U` of successful first-round components has

`W:=|U| >= q_128*rho*n`.

Moreover the number of those components satisfies

`m <= n/s_128
   <= 6n/(a*eta_128*lambda)`.

Condition on such a first-round outcome. If no second-round component has weight at least `W-alpha*n`, the deterministic balanced-cut lemma gives two unions `A,B` of actual second-round components, hence unions of the `C_i`, with

`|A|,|B| >= alpha*n`

and no `p2`-open edge crossing. For any fixed quotient cut H2 and independence of the second round give

`P(no p2 edge across A,B | first round)
 <= exp(-p2*kappa*lambda*n)
 <= exp(-kappa*epsilon*n/128)`.

There are at most `2^m` quotient cuts, so the total bad probability is at most

`exp(
   [6 log 2/(a*eta_128)] * n/lambda
   - kappa*epsilon*n/128
 ) = o(1)`

by H3.

Therefore

`P(
  L1(G_p) >= rho*(q_128-q0/64)*n
 ) >= c_seed(epsilon)-o(1)`.

This is a fully connected all-cut argument. It does not use the invalid macroblock-chain inference.

Hence the supported concrete frozen-class value moves

`g_64 -> g_128`.

### 5.2 Parametric consequence

Exactly the same proof works for every **fixed** reserve `theta in (0,epsilon)` for which

`eta(theta):=(1+epsilon-theta)*a-1 > 0`.

Writing

`q(theta)=1-exp(-eta(theta)^2/18)`,

we obtain the certified constant

`g(theta)=rho*q(theta)-alpha`.

As `theta downarrow 0`, these certified constants increase to

`g_inf := rho*q_inf-alpha
        = rho*(q_inf-q0/64)`.

This shows that `g_inf` is the supremal endpoint of this fixed-reserve all-cut family. It does **not** by itself prove the exact constant `g_inf`.

## 6. Method #29 — add the boundary state correctly: a variable split reaches the endpoint up to an explicit vanishing term

The failed coarse-block proof tried to remove H3 by replacing the full quotient with a bounded number of artificial blocks. Instead, keep the actual quotient and let the amount reserved for sprinkling shrink only as fast as the quotient entropy permits.

For all sufficiently large `lambda`, set

`theta_lambda := lambda^(-1/2)`,

`p1 := (1+epsilon-theta_lambda)/lambda`,

and define `p2` by `1-p=(1-p1)(1-p2)`.

Then

`p2 >= 1/lambda^(3/2)`.

The first-round residual margin is

`eta_lambda := eta_inf-a/sqrt(lambda)`,

and

`q_lambda := 1-exp(-eta_lambda^2/18)`.

For large `lambda`, `eta_lambda>=eta_inf/2`, so a successful first-round component has at least

`s_lambda := (a*eta_lambda/6)*lambda
           >= (a*eta_inf/12)*lambda`

vertices, and the endpoint seed lemma again yields

`W >= q_lambda*rho*n`

with probability at least a positive constant that can be chosen uniformly for all sufficiently large `lambda` (because `q_lambda` stays in a compact subinterval of `(0,1)` converging to `q_inf`).

The number of successful first-round components obeys

`m <= 12n/(a*eta_inf*lambda)`.

For a fixed macroscopic quotient cut, H2 now gives

`P(cut survives sprinkling)
 <= exp(-kappa*n/sqrt(lambda))`.

Thus the union bound over all quotient cuts is

`<= exp(
  [12 log 2/(a*eta_inf)] * n/lambda
  - kappa*n/sqrt(lambda)
)`.

Because `lambda->infinity` and always `lambda<=n-1`, the exponent tends to `-infinity`: the negative term dominates by a factor `sqrt(lambda)`, and `n/sqrt(lambda)>=sqrt(n)`.

Hence, with conditional probability `1-o(1)`, a second-round component has weight at least

`q_lambda*rho*n-alpha*n`.

Finally, for

`q(x)=1-exp(-x^2/18)`

we have

`q'(x)=(x/9)exp(-x^2/18) <= eta_inf/9`

on `[eta_lambda,eta_inf]`, so

`0 <= q_inf-q_lambda
   <= (a*eta_inf)/(9*sqrt(lambda))`.

Therefore the repaired endpoint statement is

`P(
 L1(G_p) >=
 [ rho*(q_inf-q0/64)
   - rho*a*eta_inf/(9*sqrt(lambda))
 ] * n
 ) >= c(epsilon,rho)-o(1)`.

In particular, for every fixed `delta>0`, all sufficiently large graphs in the **canonical H1--H2--H3 class** satisfy

`P(
 L1(G_p) >=
 [rho*(q_inf-q0/64)-delta] n
 ) >= c(epsilon,rho)-o(1)`.

This recovers the numerical endpoint as an **asymptotic supremum**, with an explicit rate, without the invalid block aggregation. I do **not** claim exact attainment of `rho*(q_inf-q0/64)` from this argument.

## 7. A literature obstruction: H1 plus merely positive ordinary edge-isoperimetry is not enough

The obvious next weakening of H2 is to replace direct macroscopic pair capacity by a one-set isoperimetric lower bound.

A published construction already blocks the weakest such hope.

Diskin--Erde--Kang--Krivelevich, *Percolation through Isoperimetry* (arXiv:2308.10267; published version now available), Theorem 2 states: for every constant `C>1`, `d->infinity`, `n=omega(d^2)`, and `p<=C/d`, there exists a `d`-regular `n`-vertex graph with

`i(G) >= 1/(40C)`

for which with high probability every component of `G_p` has size at most

`3d log n`.

Take `C=1+epsilon`. Since a `d`-regular graph has `lambda(G)=d`, this is exactly the source density

`p=(1+epsilon)/lambda(G)`.

Moreover these examples satisfy H1 for every

`rho <= epsilon/(8+epsilon)`.

Indeed, if `|S|=s<=rho*n`, deleting `S` removes at most `d*s` edges, so

`e(G-S) >= dn/2-ds`.

Hence

`lambda(G-S)
 >= d_avg(G-S)
 >= d*(n-2s)/(n-s)
 >= d*(1-2rho)/(1-rho)`.

The inequality

`(1-2rho)/(1-rho) >= 1-epsilon/8`

is exactly

`rho <= epsilon/(8+epsilon)`.

Finally `n=omega(d^2)` implies `3d log n=o(n)`, so these graphs have no linear giant with high probability.

Therefore:

> **H1 plus a fixed positive lower bound on ordinary edge-isoperimetry cannot answer CMW Question 5.1.**

This is a direct consequence of the published Diskin--Erde--Kang--Krivelevich construction plus the elementary deletion estimate above; I do **not** claim it as a novel theorem. It is nevertheless a useful exact obstruction for the next route: any replacement for H2 must contain more than “ordinary expansion is bounded below by a positive constant.”

This also explains why the multi-hop/reservoir idea cannot be justified from a weak one-set expansion hypothesis alone.

## 8. What each Section-B move did

**#9 RANDOMIZE.** Randomly binning first-round components does not create internal connectivity. The finite obstruction survives random binning, so this route was rejected rather than patched cosmetically.

**#12 FIND WHAT IS CONSERVED.** The legitimate invariant is cut capacity on the quotient whose vertices are the actual first-round components. Keeping that invariant restores the all-cut argument, produces the new fixed-split value `g_128`, and supports the variable `lambda^(-1/2)` split.

**#29 ADD THE POINTS AT INFINITY.** Treating the small/remainder pieces as a boundary state exposed the precise coarse-block bug. Keeping every quotient vertex instead of collapsing disconnected pieces, then shrinking the sprinkling reserve at `lambda^(-1/2)`, recovers the endpoint up to `O(lambda^(-1/2))`.

## 9. Current source/literature status and Beck--Fiala reconciliation

CMW Question 5.1 remains source-open in the bounded 18 Sep 2026 check. The R16 theorem remains **PARTIAL**: it gives a sufficient two-axis condition, not the requested natural-condition classification.

The stale native title “Beck--Fiala” was also rechecked against current primary sources:

- Bansal--Jiang, arXiv:2508.03961, state `O(sqrt(t))` for `t>=log^2 n` and a polylogarithmically weakened bound below that regime.
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 Sep 2026, state the stronger real Komlos theorem with constant `3*sqrt(2*pi)` and explicitly derive
  `B(t,n) < 3*sqrt(2*pi*t)` for every integer `t>=1`, with no restriction on `n`.
- Karingula--Lovett, ECCC TR26-188, posted 17 Sep 2026, give an independent elementary Komlos proof with constant `36`.

These are extremely recent preprint/technical-report claims, but on their stated theorems the original uniform Beck--Fiala target is now a **current-literature baseline**, not an unresolved R16 target. No part of those results is claimed as R16 work.

## 10. Prior-art and novelty discipline

Searches performed this run included the exact CMW title/authors and Question 5.1; Diskin--Erde--Kang--Krivelevich percolation/isoperimetry; Bansal--Jiang Beck--Fiala; Guo--Fang--Lu Komlos; and Karingula--Lovett ECCC TR26-188.

The seed-and-sprinkle method, cut-union arguments, and percolation on expanders are established ideas. The one-set-expansion obstruction in Section 7 is explicitly derived from Diskin et al. No novelty claim is made for it.

The repaired variable-split calculation in Section 6 is recorded as an R16 partial result, but a negative bounded search is not a novelty certificate. Publication status remains **not assessed / no closure claim**.

## 11. Metric/status accounting

There are three distinct quantities that must not be conflated:

1. **Unsupported latest reported exact endpoint:**  
   `rho*(q_inf-q0/64)` with no H3, from the coarse-block chain proof.  
   **Withdrawn as proved.**

2. **Last fully supported concrete metric before this run:**  
   `g_64=rho*(q_64-q0/64)` on canonical H1--H2--H3.

3. **New fully supported concrete metric:**  
   `g_128=rho*(q_128-q0/64)` on canonical H1--H2--H3, with `g_128>g_64`.

Additionally, this run proves the asymptotic endpoint family

`L1/n >= rho*(q_inf-q0/64)-O_epsilon(rho/sqrt(lambda))`

with fixed positive probability.

So the certified metric **moves** on the canonical frozen class, and the supported unchanged count remains/resets to `0`. The no-H3 strengthening is not currently certified.

Status after this run:

`H0002 = PARTIAL / SOURCE OPEN / ACTIVE`.

No stuck recovery is active.

## 12. Next nonrepeating moves

The next substantive triple is:

- **#1 CHANGE THE CATEGORY:** treat the first-round component quotient as a capacitated network-reliability / weighted-percolation object and search for a theorem that replaces H2 without artificial macroblocks;
- **#14 FIND THE GROUP ACTING:** specialize to regular or vertex-transitive hosts, where Perron localization disappears, and identify which quotient property upgrades ordinary expansion to direct macroscopic communication;
- **#22 READ THE FAILURES:** dissect the Diskin--Erde--Kang--Krivelevich tightness construction and classical finite-expander percolation proofs to isolate the exact hypothesis absent from H1 + positive isoperimetry.

Do **not** optimize another fixed split unless it feeds one of these routes; the parametric split is already understood.

## 13. Scheduler/model-control reality

The actual run model is GPT-5.6 Sol; reasoning telemetry is unavailable, so the level is UNVERIFIED.

The scheduler/update surface exposed in this environment still has fields for prompt/title, schedule or start offset, timing mode, enablement and task identity, but **no binding model-family field and no reasoning-effort field**, and it provides no authenticated applied-model receipt. Therefore GPT-6/maximum remains prompt-only here. Fixing this requires a scheduler/API surface that exposes those controls plus per-run runtime attestation.

The historical `P26` “You cannot modify this task” error was authorization-context-specific: repository deployment records also preserve a later successful P26 update from an authorized context. The compliant workaround for a task still returning that error is the owning authorized workspace/account context or platform support, never duplication or permission bypass. No scheduler or permission change was attempted in this run.

## 14. Structured ledger delta

```yaml
ledger_delta:
  track: R16
  source_id: H0002
  source: "Christoph--Morawski--Wigderson, arXiv:2608.19145v1, Question 5.1"
  lane: HARD_OUTSIDE
  source_status: OPEN
  result_status_before: PARTIAL
  result_status_after: PARTIAL
  canonical_hypotheses:
    H1: "spectral deletion resilience through rho*n deletions"
    H2: "every disjoint alpha*n pair has at least kappa*lambda*n host edges"
    H3: "lambda(G)->infinity"
  q0: "1-exp(-epsilon^2/288)"
  alpha: "rho*q0/64"
  eta_inf: "epsilon*(7-epsilon)/8"
  q_inf: "1-exp(-eta_inf^2/18)"
  unsupported_claim_withdrawn:
    claim: "exact endpoint with no H3 from coarse-block chain sprinkling"
    reason: "conceptual macroblocks are unions of disconnected first-round components"
    exact_checker: "artifacts/R16/2026-09-18T14-58-00Z_h0002_coarse_block_obstruction_checker.py"
    exact_output: "artifacts/R16/2026-09-18T14-58-00Z_h0002_coarse_block_obstruction_checker.out"
  supported_metric_before:
    reserve: "epsilon/64"
    eta_64: "(1+epsilon-epsilon/64)*(1-epsilon/8)-1"
    q_64: "1-exp(-eta_64^2/18)"
    g: "rho*(q_64-q0/64)"
  supported_metric_after:
    reserve: "epsilon/128"
    eta_128: "(1+epsilon-epsilon/128)*(1-epsilon/8)-1"
    q_128: "1-exp(-eta_128^2/18)"
    g: "rho*(q_128-q0/64)"
  asymptotic_endpoint:
    statement: "L1/n >= rho*(q_inf-q0/64) - rho*(1-epsilon/8)*eta_inf/(9*sqrt(lambda))"
    probability: ">= c(epsilon,rho)-o(1)"
    restrictions: "canonical H1-H2-H3; p>=(1+epsilon)/lambda"
    exact_endpoint_attained: false
  ordinary_isoperimetry_barrier:
    source: "Diskin--Erde--Kang--Krivelevich, Percolation through Isoperimetry, Theorem 2"
    implication: "H1 + i(G)>=1/[40(1+epsilon)] can still have no linear giant at p=(1+epsilon)/lambda"
    rho_range: "rho<=epsilon/(8+epsilon)"
    novelty: "KNOWN-source consequence, not claimed new"
  movement: true
  unchanged_count_after: 0
  stuck_recovery: none
  methods_used: [9, 12, 29]
  next_methods: [1, 14, 22]
  beck_fiala_current_baseline:
    value: "B(t,n)<3*sqrt(2*pi*t)"
    restrictions: "all integers t>=1, all n, per Guo--Fang--Lu arXiv:2609.11189v1"
    status: "very recent current-literature baseline; not R16 result"
  delivery:
    repository: "yspennstate/math-open-problems"
    branch: master
    report_path: "runs/R16/2026-09-18T14-58-00Z_h0002-asymptotic-endpoint-proof-repair_c7e4.md"
```
