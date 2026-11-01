Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the canonical frozen H0002 class, the concrete certified giant fraction moves from `rho*(q_in-q0/64)` to `rho*(q_out-q0/64)`, where `q_in=(q_arch+q_KL)/2`, `q_out=(q_KL+q_BP)/2`, and `q_BP` is the positive solution of `q=1-exp(-(1+u_inf)q)`; in fact every fixed coefficient strictly below `rho*(q_BP-q0/64)` is certified. Section-B methods actually used: **#3 PROVE SOMETHING STRONGER, #12 FIND WHAT IS CONSERVED, #21 ASK WHO ELSE HAS THIS SHAPE**. All 30 catalogued moves had already been used on H0002, so this is a nonconsecutive reuse on a genuinely new obligation rather than invented unused history.

# R16 — H0002: the root-weight correction upgrades the local law to Poisson survival

## 1. Continuity, ownership, required reads, and source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural conditions under which, at `p >= (1+epsilon)/lambda(G)`, bond percolation has a component of order `Omega(|G|)` with constant probability.

Before research I reread/reconciled the required control surfaces: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/H0002.md`, the H0002 intake/source identity, the newest own report `runs/R16/2026-09-18T19-44-05Z_h0002-exact-bernoulli-supermartingale_e8c1.md`, and the newest recoverable neighboring same-source G0010/G0011 records. I found no H0002 release or handoff.

Fresh 18 Sep 2026 checks still show arXiv:2608.19145 as v1 from 19 Aug 2026. The source itself states Question 5.1 in Section 5 and identifies localization of the spectral radius as the main obstruction. A bounded current title/question/author search found no later source-matching resolution. This is negative bounded-search evidence, not a worldwide novelty certificate.

Primary/current URLs checked:

- `https://arxiv.org/abs/2608.19145`
- `https://arxiv.org/pdf/2608.19145`
- `https://arxiv.org/abs/2508.03961`
- `https://arxiv.org/abs/2609.11189`
- `https://eccc.weizmann.ac.il/report/2026/188/`

The native Beck--Fiala scheduler title remains stale as an active research target. Bansal--Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` scale for `t>=log^2 n` and a weaker polylogarithmic bound below that range. Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`. Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlos proof with constant 36. These are very recent primary-source baselines, not R16 discoveries.

## 2. Frozen H0002 class and incoming metric

Fix `0<epsilon<=1`, `rho,kappa>0`, let `n=|G|`, `lambda=lambda(G)`, and put

`a0 := 1-epsilon/8`,

`q0 := 1-exp(-epsilon^2/288)`,

`alpha0 := rho*q0/64`.

The frozen graph class is unchanged:

1. **H1 (spectral deletion resilience):** `lambda(G-S) >= a0 lambda` whenever `|S|<=rho n`;
2. **H2 (macroscopic pair expansion):** `e_G(A,B) >= kappa lambda n` for disjoint `A,B` with `|A|,|B|>=alpha0 n`;
3. **H3:** `lambda -> infinity`.

The fixed metric is the largest explicit uniform giant fraction `g_twoaxis(epsilon,rho,kappa)` certified on this class.

The incoming report defined

`u_inf := a0*(1+epsilon)-1 = epsilon*(7-epsilon)/8`,

`q_arch := 1-exp(-u_inf^2/(4*(1+u_inf)))`,

`q_KL := 1-(1+u_inf)*exp(-u_inf)`,

and proved every fixed coefficient below `rho*(q_KL-q0/64)`. Its single-number receipt was

`q_in := (q_arch+q_KL)/2`,

`g_in := rho*(q_in-q0/64)`.

The previous report's remaining obligation was explicit: improving beyond `q_KL` required using information discarded by the generic scalar Chernoff step. The present run does exactly that.

## 3. Method #12 — the conserved quantity that the preceding bound threw away

The decisive identity is already present in the source exploration but was weakened in the previous R16 estimate.

In the Perron-weighted CMW exploration, normalize the nonnegative Perron vector `w` on the spectral-radius component so that the starting vertex `v` has `w(v)=1=max_x w(x)`. For each adaptive query, let `x_i in [0,1]` be the target-vertex weight and `xi_i in {0,1}` its Bernoulli-`p` outcome. Write

`S := sum_i xi_i x_i`,

`Q := sum_i x_i`,

`W := w(C_v)`.

Every vertex of the final component except the root is discovered exactly once by a successful query. Hence the source's exact identity is

`S = W-w(v) = W-1`.

This `-1` is not an error term: it is the root mass and survives after normalizing `w(v)=1`. The previous report replaced it by the weaker `S<=W`, which loses precisely the information needed below.

On the event `|C_v|<=gamma Lambda`, where `Lambda` is the spectral radius of the current connected host component, the usual deterministic boundary-weight count gives

`Q >= (1-gamma) Lambda W`.

This is the same CMW accounting as before: summing the Perron relation over the explored component gives total neighbor weight `Lambda W`; internal contribution is at most `|C_v| W`; all remaining boundary edges are queried.

## 4. Method #3 — a stronger local theorem: Poisson survival probability

### Exact Bernoulli supermartingale

For any `a>=0`, the process

`M_t := exp{-a S_t + p(1-exp(-a)) Q_t}`

is a nonnegative supermartingale for adaptive predictable query weights in `[0,1]`. Indeed, conditionally on the past and a current weight `x`,

`E exp(-a xi x) = 1-p+p exp(-a x)`

`= 1-p(1-exp(-a x))`

`<= 1-p x(1-exp(-a))`

`<= exp(-p x(1-exp(-a)))`,

where concavity of `x -> 1-exp(-a x)` on `[0,1]` gives the first inequality. The finite exploration has a bounded stopping time, so `E M_T<=1`.

### Root-corrected small-component bound

Assume `p Lambda >= 1+u` and choose `0<gamma<u/(1+u)`. Put

`b := (1+u)(1-gamma)>1`.

On the event `|C_v|<=gamma Lambda`, using the exact identity `S=W-1` and the lower bound on `Q`,

`log M_T`

`>= -a(W-1) + b(1-exp(-a))W`

`= a + h_b(a) W`,

where

`h_b(a):=b(1-exp(-a))-a`.

The function `h_b` is strictly concave, satisfies `h_b(0)=0`, `h_b'(0)=b-1>0`, and tends to `-infinity`; hence it has a unique positive root `r(b)` satisfying

`r(b)=b(1-exp(-r(b)))`.

Take `a=r(b)`. Then `h_b(a)=0`, so **every** outcome with `|C_v|<=gamma Lambda` satisfies

`M_T >= exp(r(b))`.

Markov plus optional stopping therefore gives

`P(|C_v|<=gamma Lambda) <= exp(-r(b))`,

or equivalently

`P(|C_v|>gamma Lambda) >= q(b)`,

where

`q(b):=1-exp(-r(b))`

is the unique positive solution of

`q = 1-exp(-b q)`.

This is the survival probability equation for a Poisson(`b`) Galton--Watson process.

**Important scope.** This is an analytic lemma derived from the exact CMW exploration identities plus the exact Bernoulli Laplace transform. It is not being called a literature-new theorem here; the Poisson survival equation itself is classical. The bounded prior-art search performed this run did not surface this exact finite-graph Perron-weighted root-correction formulation, but a negative search is not a novelty certificate.

### Strict improvement over the incoming local law

At the H0002 limiting margin put

`b_inf := 1+u_inf = a0*(1+epsilon)`,

and let `q_BP:=q(b_inf)` be the positive root

`q_BP = 1-exp(-b_inf q_BP)`.

The incoming seed ceiling was

`q_KL = 1-b_inf*exp(-(b_inf-1))`.

Let `u=b_inf-1`. Since

`h_b(u)=b(1-exp(-u))-u = 1-b exp(-u) = q_KL>0`,

the positive root `r(b)` lies strictly to the right of `u`. Therefore

`q_BP=1-exp(-r(b_inf)) > 1-exp(-u) > 1-b_inf exp(-u)=q_KL`.

So the local improvement is strict for every `epsilon in (0,1]`.

For orientation only:

- `epsilon=0.5`: `u_inf=0.40625`, `q_KL≈0.0632355`, `q_BP≈0.5159312`;
- `epsilon=1`: `u_inf=0.75`, `q_KL≈0.1733585`, `q_BP≈0.7126981`.

These numbers are sanity checks; the theorem is the analytic inequality above.

## 5. Repair a size-accounting issue while propagating the new law

The preceding report used a cutoff written as `gamma=tau` on each residual graph and then called `a0*tau*lambda(G)` the fixed success size. Strictly, `|C|<=tau*lambda(H)` does not imply `|C|<=a0*tau*lambda(G)`. The theorem can be propagated without that mismatch by fixing the vertex cutoff first.

Set

`tau := lambda^(-1/3)`,

`p1 := (1+epsilon-epsilon*tau)/lambda`,

and define independent `p2` through `1-p=(1-p1)(1-p2)` at `p=(1+epsilon)/lambda`. Then

`p2 >= epsilon*tau/lambda = epsilon*lambda^(-4/3)`.

For an adaptive residual graph `H=G-S` with `|S|<rho n`, H1 gives

`Lambda_H:=lambda(H) >= a0 lambda`.

Work inside a connected component of `H` attaining `Lambda_H`, normalize its Perron vector to maximum one, and choose a maximum-weight root. Define the **fixed original-graph cutoff**

`s_tau := a0*tau*lambda`,

`gamma_H := s_tau/Lambda_H <= tau`.

Also

`p1 Lambda_H >= a0*(1+epsilon-epsilon*tau) =: 1+u_tau`,

where `u_tau -> u_inf`. Thus

`b_H := (p1 Lambda_H)(1-gamma_H) >= b_tau := (1+u_tau)(1-tau)`.

The Poisson survival root `q(b)` is strictly increasing and continuous for `b>1` (differentiate the positive fixed-point equation, or use strict concavity of `1-exp(-bq)-q`). Therefore

`q_tau:=q(b_tau) -> q_BP`.

For every fixed `zeta>0`, all sufficiently large `lambda` satisfy

`q_tau >= q_* := q_BP-zeta`.

Applying the local theorem with `gamma_H=s_tau/Lambda_H` now has exactly the needed dichotomy:

- success: the revealed component has **more than `s_tau` vertices**;
- failure: it has **at most `s_tau` vertices**;
- conditional success probability at every trial is at least `q_*`.

This fixes the cutoff mismatch without weakening the limiting constant.

## 6. Seed accumulation at the Poisson-survival rate

Let `R=rho n` and adaptively explore residual components until either

1. total mass of successful components reaches `q_* R`, or
2. total deleted mass reaches `R`.

At the start of every trial fewer than `R` vertices have been deleted, so H1 applies. Let `y=R/s_tau`. If the target fails before the deletion budget is exhausted, then:

- because every success has size `>s_tau` but total success mass is `<q_*R`, the number of successes is `<q_* y`;
- because failure mass is at least `(1-q_*)R` and every failure has size `<=s_tau`, the number of failures is `>(1-q_*)y`.

Since every adaptive trial succeeds conditionally with probability at least `q_*`, couple from below with iid Bernoulli(`q_*`) trials. With

`k=ceil(q_* y)`,

`r=floor((1-q_*)y)+1`,

the probability of reaching `k` successes before `r` failures is

`P(Bin(k+r-1,q_*)>=k)`.

As `y->infinity` this tends to `1/2`; on bounded `y`, only finitely many `(k,r)` pairs occur and every one has strictly positive probability. Hence there is a constant

`c_seed(q_*)>0`

such that, uniformly in the graph,

`P(first-round successful seed mass >= q_* rho n) >= c_seed(q_*)`.

## 7. Genuine-component sprinkling remains valid

Condition on a first-round seed family of total vertex mass

`W>=q_* rho n`.

Every successful seed is a genuine connected first-round component of size `>s_tau`, so the true seed-component quotient has at most

`m <= n/s_tau = n/(a0 lambda^(2/3))`

vertices.

Assume `q_*>3q0/64`. If no round-two connected component captures at least `W-alpha0 n` seed vertices, the standard deterministic balanced-cut extraction on the **genuine component quotient** gives a quotient cut whose two original vertex sides each have at least `alpha0 n` vertices. H2 supplies at least `kappa lambda n` host edges across that cut.

A fixed cut receives no round-two edge with probability at most

`exp(-p2*kappa*lambda*n) <= exp(-kappa*epsilon*n/lambda^(1/3))`.

Union-bounding over at most `2^m` quotient cuts gives

`P(sprinkling fails | seed)`

`<= exp{ [ (log 2)/(a0 lambda^(2/3)) - kappa*epsilon/lambda^(1/3) ] n } = o(1)`

by H3.

Therefore, for every fixed `zeta>0` satisfying

`q_BP-zeta > 3q0/64`,

we obtain

`P( L1(G_p) >= rho*(q_BP-zeta-q0/64) n )`

`>= c_seed(q_BP-zeta)-o(1)`.

Equivalently, **every fixed coefficient strictly below**

`g_BP_sup := rho*(q_BP-q0/64)`

is certified on the unchanged H1--H2--H3 class, where `q_BP` is the positive solution

`q_BP = 1-exp(-(1+epsilon*(7-epsilon)/8)*q_BP)`.

I do **not** claim attainment of the endpoint `g_BP_sup`.

## 8. Concrete fixed-metric movement

The incoming single-number receipt was

`q_in=(q_arch+q_KL)/2`.

Choose the new canonical receipt

`q_out := (q_KL+q_BP)/2`.

Because `q_BP>q_KL>q_arch`,

`q_out > q_KL > q_in`,

and `q_out<q_BP`, so Section 7 applies with `zeta=(q_BP-q_KL)/2`. Hence the fixed metric strictly moves to

`g_out := rho*(q_out-q0/64)`.

For orientation:

- `epsilon=0.5`: incoming seed coefficient `q_in≈0.0460748`, new `q_out≈0.2895834`;
- `epsilon=1`: incoming `q_in≈0.1252859`, new `q_out≈0.4430283`.

Again, the metric movement is analytic, not numerical.

## 9. Method #21 — who else has this shape, and where the architecture now stops

The fixed-point equation

`q=1-exp(-bq)`

is exactly the survival-probability equation for a Poisson(`b`) Galton--Watson process. This is classical branching-process territory; CMW themselves note in their introduction that spectral radius controls survival of multi-type branching processes and cite Athreya--Ney. Their paper also describes the historical regular-graph supercritical argument as branching-process local analysis plus expansion gluing.

That comparison is more than cosmetic. For high-girth, high-degree regular graphs at `p≈b/d`, the local neighborhood exploration approaches a Poisson(`b`) branching process. Thus `q_BP` is the natural scalar benchmark for any argument that uses only the local spectral mean and no additional cycle/geometry information. This is method-level sharpness evidence, not an upper bound on H0002 and not a novelty claim.

The bounded searches used combinations of the exact CMW title/authors with `Perron`, `weighted exploration`, `survival probability`, `Poisson`, and the fixed-point equation. They found the standard branching-process connection and CMW's own citations, but no exact finite-graph statement matching the root-corrected lemma above. A full publication-level prior-art audit remains mandatory before presenting the lemma as new.

The next useful mathematical obligation is therefore not another scalar Laplace-transform optimization. It is to exploit information beyond the Poisson local benchmark: variance/profile information in the Perron weights, collision/cycle structure, or geometry that improves the *global* conversion of local survival mass into one giant.

## 10. Beck--Fiala reconciliation

The task title still names Beck--Fiala, so the fixed native quantity must be stated honestly even though current literature supersedes it.

- Bansal--Jiang v2: `O(sqrt(t))` for `t>=log^2 n`; below that, `tilde O(sqrt(t)+sqrt(log n))` with polylog-log factors.
- Guo--Fang--Lu v1 (10 Sep 2026): for every integer `t>=1` and every `n`,

  `B(t,n) < 3 sqrt(2 pi t)`.

  This is the complete uniform square-root bound the original Beck--Fiala conjecture asks for, obtained as a corollary of their stronger Komlos theorem.
- Karingula--Lovett TR26-188 (17 Sep 2026): independent elementary Komlos proof with constant 36.

These are extremely recent preprint/technical-report results, not mature refereed consensus. On their stated theorems, however, the old R16 Beck--Fiala target is **KNOWN current-literature baseline**, so restarting from Bansal--Jiang's `t>=log^2 n` restriction would knowingly duplicate a superseded gap.

## 11. Status, checker policy, and next methods

H0002 remains **PARTIAL / SOURCE OPEN / ACTIVE**. The source's open-ended classification question is not closed by a sufficient condition on the frozen class.

The fixed metric moved, so the supported unchanged count is **0** and no stuck recovery is active.

No exact checker was created: the new claims are analytic theorem-sized statements with the complete proof written on the page and no finite computational core. The numeric values above are nonessential orientation only.

All 30 Section-B moves have already been used on H0002. The next run should again use a nonconsecutive triple tied to a genuinely new obligation rather than inventing unused history. Candidate next triple: **#11 DUALIZE, #15 BREAK THE SYMMETRY, #28 REPLACE FOR ALL WITH TYPICAL**, aimed at either (i) a dual/capacitated formulation of H2 gluing, (ii) a deliberately inhomogeneous Perron-profile stress test of the `q_BP` seed law, or (iii) proving that only the random family of seed cuts—not all macroscopic pairs—needs expansion under an appropriately adversarially robust condition.

## 12. Model/scheduler control and permission escalation

The exposed scheduler control surface still has prompt/title, schedule/start offset, timing mode, enablement and task identity, but no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt. Therefore GPT-6/maximum remains a prompt request only in this interface; actually enforcing it requires scheduler/API fields for model and reasoning plus per-run runtime attestation.

The historical `You cannot modify this task` result is authorization-context-specific. Repository state records that P26 later succeeded from an authorized context. The compliant workaround for any task that still refuses modification is the owning authorized workspace/account context or platform support; do not duplicate the task and do not bypass permissions. This run made no scheduler or permission changes.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  claim: H0002
  lane: HARD_OUTSIDE
  source_status: OPEN_LOOKING_BOUNDED_SEARCH
  status: PARTIAL
  metric: g_twoaxis(epsilon,rho,kappa)
  before:
    q_seed_receipt: (q_arch+q_KL)/2
    g: rho*((q_arch+q_KL)/2-q0/64)
  after:
    q_BP_definition: q_BP is the unique positive root of q=1-exp(-(1+u_inf)q)
    q_seed_receipt: (q_KL+q_BP)/2
    g: rho*((q_KL+q_BP)/2-q0/64)
    stronger_supremum_not_claimed_attained: rho*(q_BP-q0/64)
  movement: STRICT_INCREASE
  unchanged_count_after: 0
  methods_actual: [3, 12, 21]
  checker: NOT_APPLICABLE_ANALYTIC_THEOREM
  proof_repair:
    issue: prior residual cutoff gamma=tau did not itself imply fixed size <=a0*tau*lambda(G)
    repair: fix s_tau=a0*tau*lambda(G), then set gamma_H=s_tau/lambda(H)<=tau
  prior_art_scope:
    - CMW arXiv:2608.19145v1 checked 2026-09-18
    - branching-process/Perron/survival bounded searches checked 2026-09-18
    - no worldwide novelty claim
  beck_fiala_current_baseline:
    Guo_Fang_Lu: B(t,n)<3*sqrt(2*pi*t) for all integer t>=1, all n, per arXiv:2609.11189v1
    Karingula_Lovett: Komlos constant 36, ECCC TR26-188
  delivery: private GitHub only
  shared_roots_modified: false
  peer_files_modified: false
  email_drive_public_posting: false
```
