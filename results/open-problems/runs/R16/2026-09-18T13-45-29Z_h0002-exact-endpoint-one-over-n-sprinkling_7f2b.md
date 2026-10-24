Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. METRIC MOVEMENT:** H0002 `g_twoaxis(epsilon,rho,kappa): rho*(q_127-q0/64) -> rho*(q_inf-q0/64)`, where `q0=1-exp(-epsilon^2/288)`, `eta_inf=epsilon*(7-epsilon)/8`, `q_inf=1-exp(-eta_inf^2/18)`; Section-B methods actually used: **#7 TAKE THE LIMIT, #15 BREAK THE SYMMETRY ON PURPOSE, #25 COUNT THE SAME THING TWICE**.

# R16 — H0002: exact endpoint seed mass from the one-over-n sprinkling scale

## 1. Continuity, ownership, required reads, and current source

This run continues the latest complete R16 research chain on the active HARD OUTSIDE target `H0002`, Question 5.1 of Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (submitted 19 Aug 2026). It does **not** restart the stale Beck--Fiala scheduler title, and it does not reopen the already handed-off H0022 route.

Before research I reread/reconciled the required campaign/control surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the verified H-intake material for H0002, the canonical claim `operations/claims/H0002.md`, and the newest own R16 report

`runs/R16/2026-09-18T12-42-44Z_h0002-coarse-block-sprinkling-no-h3_4d8c.md`.

I also checked the newest same-source neighboring history. G0010 (Question 5.2, subcritical component scale) has already reached terminal HARD handoff after both recoveries. G0011 (the long-cycle conjecture) also reached terminal handoff in its previous slot; its former worker has since rotated to a different target. Neither neighboring track changes the H0002 state.

The H-intake verification identifies H0002 exactly as Question 5.1, Section 5 of arXiv:2608.19145. A fresh current-source check on 18 Sep 2026 still shows arXiv:2608.19145v1 as the current version. The source proves the general `1/lambda(G)` critical scale and asks for natural conditions forcing a component of order `Omega(|G|)` with constant probability already at `p >= (1+epsilon)/lambda(G)`. A bounded current title/author/source search did not locate a later source-matching resolution. This is current-status evidence, not an exhaustive novelty certificate.

There remains a repository ownership inconsistency: `operations/claims/H0018.md` also names R16, while there is no H0002 release/handoff and the complete newest R16 chain is H0002. I did not invent a rotation or edit either claim. The mathematically continuous active state used here is H0002.

## 2. Frozen H0002 class and metric before this run

Fix

`0 < epsilon <= 1`, `0 < rho <= 1`, `kappa > 0`,

let `n=|G|`, `lambda=lambda(G)`, and define

`q0 := 1-exp(-epsilon^2/288)`,

`alpha := q0*rho/64`.

The canonical H0002 hypotheses used by this chain are:

**(H1) Spectral deletion resilience.** For every `S subseteq V(G)` with `|S|<=rho*n`,

`lambda(G-S) >= (1-epsilon/8)*lambda(G)`.

**(H2) Macroscopic pair expansion.** For every two disjoint `A,B subseteq V(G)` with

`|A|,|B| >= alpha*n`,

`e_G(A,B) >= kappa*lambda(G)*n`.

The original claim also recorded `lambda(G)->infinity`; the preceding R16 run proved that this extra hypothesis is unnecessary for the theorem by replacing an entropy-heavy all-cut union bound with coarse-block chain sprinkling. I retain the frozen metric name, but the theorem below applies to the strictly larger class defined only by H1 and H2.

The tracked quantity is the largest explicit giant fraction proved uniformly for this class at every

`p >= (1+epsilon)/lambda(G)`

with probability bounded below by a positive constant depending only on the frozen parameters.

The previous report proved the concrete value

`g_old = rho*(q_127-q0/64)`,

where

`eta_inf := (1+epsilon)*(1-epsilon/8)-1 = epsilon*(7-epsilon)/8`,

`q_127 := 1-exp(-((127/128)*eta_inf)^2/18)`.

It also proved every fixed sub-endpoint value obtained by replacing `127/128` with any fixed `sigma<1`, but deliberately did not claim `sigma=1`.

This run attains the endpoint exactly:

`q_inf := 1-exp(-eta_inf^2/18)`,

and proves

`g_new = rho*(q_inf-q0/64)`.

Since `q_inf>q_127`, the frozen quantitative metric strictly moves and the H0002 supported unchanged count remains `0`.

## 3. Method #15 — break the two-round symmetry at the unique compatible scale

By monotonicity it is enough to prove the result at

`p=(1+epsilon)/lambda`.

If this quantity exceeds `1`, there is no admissible `p` in the source statement, so in the non-vacuous case `lambda >= 1+epsilon > 1`.

The previous report used a fixed fraction of the supercritical margin for the first round and then took a fixed `sigma<1`. Instead, reserve only the one-edge-scale amount

`1/n`

from the numerator:

`p1 := (1+epsilon-1/n)/lambda`,

and define the independent second-round parameter `p2` by

`1-p = (1-p1)(1-p2)`.

Then

`p2 = (p-p1)/(1-p1) >= 1/(lambda*n)`.

Write

`a := 1-epsilon/8`,

`eta := eta_inf := (1+epsilon)*a-1 = epsilon*(7-epsilon)/8`,

`eta_n := eta-a/n`.

If an adaptive first-round exploration has already removed `S` with `|S|<rho*n`, H1 gives

`p1*lambda(G-S)`

`>= (1+epsilon-1/n)*a`

`= 1+eta_n`.

For all sufficiently large `n`, `eta_n>0`; moreover `eta_n<1` because `eta<=3/4` for `0<epsilon<=1`.

At the current residual graph choose a Perron eigenvector, normalize its maximum coordinate to `1`, and start at a maximizing vertex. Lemma 3.1(b) of the CMW source, applied with supercritical parameter `eta_n` and `C=1`, gives

`P(next p1-component has size > (eta_n/6)*lambda(G-S) | past)`

`>= q_n`,

where

`q_n := 1-exp(-eta_n^2/18)`.

Using H1 once more, every such successful component has size more than

`s_n := (a*eta_n/6)*lambda`.

A failed attempted component has size at most `s_n` by definition. Sequential component exploration preserves the needed conditional law because after a revealed component is removed, unexposed `p1`-edges in the residual graph remain independent Bernoulli(`p1`).

The only apparent problem is that `q_n<q_inf`. The rest of the run proves that the deficit is small enough that the endpoint `q_inf*rho*n` is nevertheless reached with uniformly positive probability.

## 4. Method #7 — take the endpoint limit with a vanishing bias deficit

Set

`R := rho*n`,

`y := R/s_n`.

Run the adaptive residual-CMW exploration until either

1. the total mass in successful discovered components reaches `q_inf*R`, or
2. the total deleted mass reaches `R`.

At every attempt, the conditional success probability is at least `q_n`; a success has size `>s_n`, and a failure has size `<=s_n`.

### Lemma 4.1 (vanishing-deficit endpoint lemma)

For the H0002 parameters above there exists a constant

`c_seed(epsilon,rho)>0`

such that for all sufficiently large `n`, uniformly over every graph satisfying H1,

`P(successful first-round mass >= q_inf*rho*n) >= c_seed(epsilon,rho)`.

### Proof

Couple the actual success indicators from below by iid Bernoulli(`q_n`) variables. Suppose the target `q_inf*R` is not reached and the process instead exhausts total deletion budget `R`. Let `S` and `F` be its numbers of successful and failed attempts.

Since every success has size `>s_n` but total successful mass is `<q_inf R`,

`S < q_inf*y`.

Since total deleted mass is at least `R`, failed mass is more than `(1-q_inf)R`; each failed component has size at most `s_n`, so

`F > (1-q_inf)*y`.

Define

`k := ceil(q_inf*y)`,

`r := floor((1-q_inf)*y)+1`,

`N := k+r-1 = ceil(q_inf*y)+floor((1-q_inf)*y)`.

Failure of the target forces `r` comparison failures to occur before the `k`-th comparison success. Therefore

`P(target succeeds)`

`>= P(Bin(N,q_n) >= k)`.

This is the exact point where the endpoint becomes tractable.

First,

`|N-y|<1`.

Second, put

`delta_n := q_inf-q_n`.

For `q(x)=1-exp(-x^2/18)`,

`q'(x) = (x/9)exp(-x^2/18) <= eta/9`

on `[eta_n,eta]`. Since `eta-eta_n=a/n`, the mean-value theorem gives

`delta_n <= eta*a/(9n)`.

For all large `n`, `eta_n>=eta/2`, hence

`s_n >= (a*eta/12)*lambda`,

and consequently

`y <= 12*rho*n/(a*eta*lambda)`.

Thus

`delta_n*y <= 4*rho/(3*lambda) <= 4*rho/3`.

Now compare the binomial threshold with its mean. Since `|N-y|<1`,

`k-N*q_n`

`= (k-q_inf*y) + q_inf*(y-N) + N*(q_inf-q_n)`

is bounded above by a constant depending only on `rho` and `epsilon` (indeed the first two terms are bounded absolutely and `delta_n N <= delta_n(y+1)=O_rho(1)`).

If `N->infinity`, then `q_n->q_inf in (0,1)` and the standardized threshold displacement

`(k-N*q_n)/sqrt(N*q_n*(1-q_n))`

tends to `0`. By the de Moivre--Laplace central limit theorem (or Berry--Esseen),

`P(Bin(N,q_n)>=k) -> 1/2`.

In particular it is at least `1/4` for all sufficiently large `N` and `n`.

If `N` remains below a fixed threshold `N0`, then for all sufficiently large `n`, `q_n>=q_inf/2`. The event that all `N` comparison trials are successes has probability at least

`(q_inf/2)^N0>0`

and certainly implies at least `k` successes. Taking the minimum of this finite-state lower bound and `1/4` proves a positive constant `c_seed(epsilon,rho)` independent of `n`, `lambda`, and the adaptive history. ∎

Therefore, with fixed positive probability, the first round contains a union `U` of successful components with

`W:=|U| >= q_inf*rho*n`.

### Why `1/n` is the exact compatibility scale for this architecture

The preceding proof also identifies a sharp method scale. More generally, take

`p1=(1+epsilon-r_n)/lambda`.

The first-round success probability is below `q_inf` by `Theta(r_n)` for small `r_n`, while the number of relevant attempts can be `Theta(n/lambda)`. In the worst bounded-`lambda` regime, the cumulative standardized bias is controlled only if

`r_n*n = O(1)`.

On the other hand H2 supplies `Theta(lambda*n)` candidate edges between two macroscopic blocks, and the second-round density is at least `r_n/lambda`. A prescribed macroscopic link has probability bounded away from zero only if

`r_n*n = Omega(1)`.

Thus

`r_n = Theta(1/n)`

is precisely the scale at which both endpoint seed mass and constant-probability macroscopic gluing can coexist uniformly when `lambda` may stay bounded. This is an obstruction/architecture diagnosis, not a statement that Question 5.1 itself has a unique proof scale.

## 5. Method #25 — count the stopping event in the binomial language

The combinatorial identity used above is simple but decisive and worth isolating because it is what removes the previous fixed-`sigma` loss.

For independent Bernoulli(`q_n`) trials, the event

`the k-th success occurs before the r-th failure`

can be counted in two equivalent ways:

- negative-binomial language: sum over the possible position of the `k`-th success before failure `r`;
- fixed-horizon language: among the first `N=k+r-1` trials there are at least `k` successes.

Hence exactly

`P(k-th success before r-th failure) = P(Bin(k+r-1,q_n)>=k)`.

The stopping geometry gives `N=y+O(1)`, while the one-over-n split gives `q_inf-q_n=O(1/n)`. Those two facts together make the endpoint threshold differ from the binomial mean by only `O(1)` trials, rather than by a growing large-deviation amount. The previous `sigma<1` proof did not exploit this matching of scales.

## 6. Coarse-block sprinkling at the endpoint

Condition on the seed event from Lemma 4.1. Recall

`alpha=q0*rho/64`.

Because `q_inf>q0`, we have `W>=q_inf*rho*n>64*alpha*n`, so there is ample seed mass.

Group the successful first-round components deterministically into full blocks

`B_1,...,B_m`

such that every full block has size at least `alpha*n`, leaving at most one remainder of size `<alpha*n`. One may take every already-large seed component as its own block and greedily aggregate smaller ones; unless a single component already has size at least `W-alpha*n`, in which case the desired giant is already present. The number of full blocks satisfies

`m <= 1/alpha`,

a constant depending only on `epsilon,rho`.

Connect only the predetermined chain

`B_1 -- B_2 -- ... -- B_m`.

For every consecutive pair H2 gives at least

`kappa*lambda*n`

host edges. Since

`p2 >= 1/(lambda*n)`,

the probability that at least one second-round edge opens between a fixed consecutive pair is at least

`1-(1-p2)^(kappa*lambda*n) >= 1-e^{-kappa}`.

The crossing-edge sets for distinct consecutive block pairs are disjoint, so these link events are independent. Therefore all links open with probability at least

`c_link(epsilon,rho,kappa)`

`:= (1-e^{-kappa})^(ceil(1/alpha)-1) > 0`.

On this event a single second-round component contains every full block, hence more than

`W-alpha*n`

`>= rho*(q_inf-q0/64)*n`

vertices.

The first and second rounds are independent, so Lemma 4.1 and the chain event give a fixed positive lower bound on the final giant event.

## 7. Main theorem and metric movement

### Theorem 7.1 (exact CMW-lemma endpoint for the two-axis class)

Fix `0<epsilon<=1`, `0<rho<=1`, `kappa>0`. Let `G=G_n` be any sequence of finite graphs satisfying H1 and H2 above; **no assumption `lambda(G_n)->infinity` is required**. Put

`eta_inf := epsilon*(7-epsilon)/8`,

`q_inf := 1-exp(-eta_inf^2/18)`,

`q0 := 1-exp(-epsilon^2/288)`.

Then for every

`p >= (1+epsilon)/lambda(G)`, 

for all sufficiently large `n`,

`P( L_1(G_p) >= rho*(q_inf-q0/64)*n )`

`>= c(epsilon,rho,kappa) > 0`,

where the positive constant is uniform over the graph sequence.

Equivalently,

`g_twoaxis(epsilon,rho,kappa)`

`>= rho*[ 1-exp(-epsilon^2*(7-epsilon)^2/1152)`

`          -(1-exp(-epsilon^2/288))/64 ]`.

### Proof

The first-round split and H1 give the adaptive success probability `q_n` and success-size threshold `s_n` in Section 3. Lemma 4.1 gives seed mass at least `q_inf*rho*n` with probability `c_seed>0`. Conditional on that seed event, Section 6 gives a second-round component containing all but fewer than `alpha*n=q0*rho*n/64` seed vertices with probability at least `c_link>0`. Independence of rounds gives probability at least `c_seed*c_link`, and the resulting component has the claimed size. Monotonicity extends equality `p=(1+epsilon)/lambda` to all larger `p`. ∎

Since

`q_inf > q_127`,

this strictly improves the previous explicit metric value

`rho*(q_127-q0/64)`.

Status remains **PARTIAL / SOURCE OPEN**: this is a sufficient-condition theorem for a concrete two-axis class, not a classification of all natural conditions answering Question 5.1.

## 8. What was tried, what failed, and what is now the real obstruction

This run was intentionally not another local-lemma/checker run.

**#7 TAKE THE LIMIT.** The fixed-`sigma<1` approximation looked at first like a genuine endpoint barrier because each trial only succeeds with probability `q_n<q_inf`. The attempted iid Bernoulli obstruction fails exactly at the `1/n` split: its expected success deficit over `Theta(n/lambda)` trials remains `O(1/lambda)`, so the endpoint still has constant probability. The endpoint theorem above closes this route completely.

**#15 BREAK THE SYMMETRY.** Giving almost all supercriticality to the seed phase and only `1/(lambda*n)` scale density to sprinkling works because coarse blocking leaves only `O_{epsilon,rho}(1)` prescribed links. A symmetric split wastes a fixed amount of the CMW success exponent. The calculation in Section 4 shows `1/n` is the compatible scale in the bounded-`lambda` regime.

**#25 COUNT THE SAME THING TWICE.** The stopping obstruction is exactly a negative-binomial event, equivalently one binomial tail at horizon `k+r-1`. Rewriting it this way exposes that the endpoint threshold differs from the mean by only `O(1)`, which is invisible in the earlier large-deviation treatment.

The remaining strong assumption is now clearly H2 itself: direct edge capacity between **every pair** of macroscopic sets. Ordinary one-set expansion does not imply this direct pair condition, because two seed blocks may both send their boundary through a third reservoir. The next genuinely new route must either use such a reservoir/multi-hop structure rather than direct links, or find a source-valid obstruction proving that some two-set control is actually necessary at the exact spectral threshold.

No further gain is available merely by changing the first/second-round split inside the present black-box architecture: the seed endpoint from Lemma 3.1(b) is now attained, and the remaining `alpha*n` loss comes from the fact that H2 gives no information about a leftover set smaller than its threshold.

## 9. Current prior-art / Beck--Fiala reconciliation

The stale scheduler title is not restarted. Fresh checks on 18 Sep 2026 give the following current baseline.

Bansal--Jiang, arXiv:2508.03961v2, still gives the Beck--Fiala square-root order in the regime `t>=log^2 n`, with polylogarithmic losses in the smaller-`t` regime.

Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), now states the stronger Komlos theorem with constant `3*sqrt(2*pi)` and explicitly derives for every set system of degree `t>=1`

`disc(F) < 3*sqrt(2*pi*t)`,

with no restriction on `n`.

Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), gives a separate elementary proof of Komlos with constant `36`.

These are extremely recent preprint/technical-report results rather than mature refereed consensus, but on their stated claims the old all-`t,n` Beck--Fiala metric has the complete current literature baseline

`B(t,n) < 3*sqrt(2*pi*t)`.

This is **KNOWN**, not an R16 result, and it is why the continuous R16 research state remains H0002 rather than duplicating the pre-September Beck--Fiala gap.

For H0002, the fresh source check found arXiv:2608.19145 still at v1. I also searched for combinations of the source authors/title with giant-component, spectral-deletion-resilience, Perron-delocalization and macroscopic-pair-expansion language. I did not find this exact theorem or a later resolution of Question 5.1. This is bounded negative evidence only; publication-level novelty still requires a deeper prior-art audit.

## 10. Verification budget and no-checker decision

No exact-arithmetic checker was manufactured. The new claim is an analytic asymptotic theorem with no finite computational core; its full proof is on the page. Spending the bookkeeping budget on a synthetic numerical certificate would violate the 90/10 instruction rather than increase confidence in the proof.

Self-audit items checked on the page:

1. `eta=epsilon*(7-epsilon)/8` lies in `(0,1)` for `0<epsilon<=1`, so the source lemma is applied in its parameter range.
2. `p1<p<=1` in every non-vacuous case, and the independent split satisfies `p2>=1/(lambda*n)`.
3. `q_inf-q_n=O(1/n)` with the explicit mean-value bound used above.
4. The relevant number of attempts is at most order `n/lambda`, giving bounded cumulative bias even for bounded `lambda`.
5. Coarse-block count is at most `1/alpha`, so no `lambda->infinity` hypothesis is hidden in the sprinkling step.
6. H2 is invoked only for disjoint sets of size at least exactly its frozen threshold `alpha*n`.

## 11. Structured ledger delta

```yaml
ledger_delta:
  worker: R16
  target: H0002
  source: Christoph-Morawski-Wigderson_arXiv_2608.19145v1_Question_5.1
  category: HARD_OUTSIDE
  status_before: PARTIAL_SOURCE_OPEN
  status_after: PARTIAL_SOURCE_OPEN
  metric_name: g_twoaxis(epsilon,rho,kappa)
  q0: 1-exp(-epsilon^2/288)
  eta_inf: epsilon*(7-epsilon)/8
  metric_before: rho*(q_127-q0/64)
  q_127: 1-exp(-((127/128)*eta_inf)^2/18)
  metric_after: rho*(q_inf-q0/64)
  q_inf: 1-exp(-eta_inf^2/18)
  movement: STRICT_INCREASE
  hypothesis_change: H3_lambda_to_infinity_remains_unnecessary
  supported_unchanged_count_before: 0
  supported_unchanged_count_after: 0
  stuck_recovery_active: false
  methods_used: [7, 15, 25]
  finite_claim: false
  checker_created: false
  ownership_note: H0002 chain continuous; H0018 duplicate-R16 claim left untouched for coordinator reconciliation
```

## 12. Next nonrepeating research moves

The next H0002 run should **not** optimize the two-round constant again. That route has reached the exact CMW-lemma endpoint.

Use three still-unused H0002 methods:

- **#9 RANDOMIZE:** randomize the coarse routing through a reservoir instead of demanding direct H2 edges between every prescribed pair;
- **#12 FIND WHAT IS CONSERVED:** identify a cut-capacity or flow invariant that survives contraction of first-round components and can be supplied by one-set isoperimetry;
- **#29 ADD THE POINTS AT INFINITY:** treat the sub-`alpha*n` remainder/reservoir as a boundary state in a closure process, so indirect multi-hop links may absorb it without pairwise expansion.

The substantive target is to replace H2 by a more standard one-set expansion plus a provable reservoir/multi-hop condition, or else construct a source-valid family showing why such a weakening cannot hold at the exact `1/lambda(G)` scale.

## 13. Model / scheduler control check

The exposed task-control surface still has prompt/title, schedule/start-offset, timing mode, enablement and task identity, but **no binding model-family selector, no reasoning-effort selector, and no authenticated per-run applied-model receipt**. Therefore GPT-6 / maximum remains requested only in prompt text; this run truthfully reports GPT-5.6 Sol and reasoning level UNVERIFIED.

To make GPT-6 / maximum enforceable rather than aspirational, the scheduler/API would need to expose model-family and reasoning-effort fields and return authenticated execution metadata on each run.

The historical P26 `You cannot modify this task` failure remains an authorization-context issue, not a research issue. The compliant workaround is to modify the task from its owning authorized workspace/account context or escalate to platform support. Duplicating the task or bypassing permissions is not a valid workaround.
