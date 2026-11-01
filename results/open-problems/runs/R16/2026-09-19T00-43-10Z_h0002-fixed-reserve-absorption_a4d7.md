Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the unchanged frozen H0002 class, this run proves a concrete coefficient strictly larger than the *entire* preceding envelope `g1 := rho-alpha+d1`; more strongly, every fixed `g < g_abs_sup` is proved, where `g_abs_sup = g1 + (1-rho)(1-exp(-Delta*F1/beta))`, `beta=alpha-d1`, `F1=F(d1)>0`, and `Delta=epsilon(7-epsilon)/(8-epsilon)`. Section-B methods actually used: **#6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY**.

# R16 — H0002: fixed-reserve absorption beyond the spectral-padding envelope

## 1. Continuity, ownership, required reads, and source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: find natural hypotheses on a finite graph `G` guaranteeing that, for `p >= (1+epsilon)/lambda(G)`, bond percolation contains a component of order `Omega(|G|)` with constant probability.

I first re-read/reconciled the required repository state: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/H0002.md`, the H-intake `probability_1000_intake_H_20260914/problems.jsonl`, the newest own report `runs/R16/2026-09-18T23-46-45Z_h0002-spectral-compression-padding-gain_9f2c.md`, the earlier local-exploration and two-scale-harvesting reports needed below, and the newest recoverable neighboring same-source G0011 report. The neighboring G0011 task is a distinct long-cycle conjecture and does not alter R16 ownership of H0002.

Fresh current-source checks in this invocation still recover CMW as arXiv:2608.19145v1, dated 19 Aug 2026, and a bounded title/author/question search did not locate a later source-matching resolution of Question 5.1. This is negative evidence only, not a worldwide-openness or novelty certificate.

Current primary/source comparison links checked this run:

- CMW source question: https://arxiv.org/abs/2608.19145
- Bansal--Jiang, arXiv:2508.03961v2: https://arxiv.org/abs/2508.03961
- Guo--Fang--Lu, arXiv:2609.11189v1: https://arxiv.org/abs/2609.11189
- Karingula--Lovett, ECCC TR26-188, 17 Sep 2026: https://eccc.weizmann.ac.il/report/2026/188/
- Krivelevich--Lubetzky--Sudakov, *Asymptotics in percolation on high-girth expanders*, RSA 2020, DOI 10.1002/rsa.20903.

The nominal native Beck--Fiala title remains stale as an unresolved assignment. Bansal--Jiang v2 proves the conjectured `O(sqrt(t))` scale directly for `t >= log^2 n` and gives a weaker polylogarithmic-loss bound below that range. But Guo--Fang--Lu's 10 Sep 2026 preprint proves the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduces, for every integer `t>=1` and every `n`,

`B(t,n) < 3 sqrt(2 pi t)`.

Karingula--Lovett independently posted an elementary Komlos proof with constant `36` on 17 Sep 2026. These are extremely recent preprint/technical-report results, not mature refereed consensus, but on their stated theorems the original square-root Beck--Fiala target is a current-literature **KNOWN** baseline. I therefore preserve the already-admitted H0002 successor rather than manufacture an obsolete `t<log^2 n` gap.

The literature search around the new mechanism also recovered standard sprinkling/giant-component work on expanders and pseudorandom graphs. Sprinkling and subsequent attachment/absorption are therefore not claimed as new genres. The R16 contribution here is the quantitative way the frozen H1/H2 hypotheses and the preceding spectral-padding inequality produce a uniform reservoir degree quantile that can be exploited by a fixed `Theta(1/lambda)` reserve. A bounded search not finding that exact formula is not a novelty certificate.

## 2. Frozen class and incoming quantitative state

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Let

`n := |G|`, `lambda := lambda(G)`,

`h := 1-epsilon/8`,

`q0 := 1-exp(-epsilon^2/288)`,

`alpha := rho*q0/64`.

The H0002 class is unchanged:

1. **H1 (spectral deletion resilience):** `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. **H2 (macroscopic pair expansion):** `e_G(X,Y) >= kappa lambda n` for every disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. **H3:** `lambda -> infinity` along the graph sequence.

The tracked quantity is the largest explicit uniform coefficient `g_twoaxis(epsilon,rho,kappa)` for which, at every `p >= (1+epsilon)/lambda`, `G_p` contains a component of at least `g n` vertices with probability bounded below by a frozen-parameter positive constant.

The preceding run established the following explicit host-geometry quantities. Nonvacuity gives `0<rho<1` and `kappa<=alpha^2<alpha`. Define

`d0 := kappa*(rho-alpha)/(alpha-kappa)`,

`abar := rho-alpha+d0`,

`cbar := 1-abar`,

and

`Xi0 := d0*cbar/alpha` if `cbar>=alpha`, while `Xi0 := 1-rho` if `cbar<alpha`.

Then

`L0 := d0*Xi0^2/(abar*cbar) > 0`,

`delta_spec := min{(alpha-d0)/2, cbar/2, Xi0/2, L0/16} > 0`,

`d1 := d0+delta_spec`.

For `0<=d<=d1`, put

`a(d):=rho-alpha+d`,

`c(d):=1-a(d)`,

and

`Xi(d) := kappa*a(d)*c(d)/alpha^2` if `c(d)>=alpha`,

`Xi(d) := a(d)*kappa/alpha-(alpha-c(d))` if `c(d)<alpha`.

The preceding report proved, purely from H2 plus the 2-by-2 adjacency compression, that every disjoint host pair `A,B` with

`|A| = a(d)n + o(n)`, `|B| = (alpha-d)n + o(n)`

satisfies

`e(A,B)/(lambda n) >= F(d)-o(1)`,

where

`F(d) := a(d)*kappa/alpha - d + d*Xi(d)^2/[a(d)c(d)]`.

Moreover it proved

`F(d) >= L0/16 > 0` for every `d in [d0,d1]`.

Its strongest incoming giant-component envelope was

`every fixed g < g1 := rho-alpha+d1`.

Equivalently, with

`beta := alpha-d1 > 0`,

we have

`g1 = rho-beta`.

For this run define the endpoint crossing coefficient

`F1 := F(d1) > 0`.

The goal is to use the unused vertex reservoir, whose asymptotic density is `1-rho`, to move strictly beyond `g1` without changing H1, H2 or H3.

## 3. Method #6 — deform the probability split and keep a fixed absorption reserve

### 3.1 The old split was no longer optimal

The preceding seed-and-glue proofs used a first-round probability whose numerator tended to `1+epsilon`, leaving only a vanishing `Theta(lambda^(-4/3))` sprinkling reserve. That was natural when the local survival probability itself controlled the seed mass. The two-scale harvesting theorem changed the situation: it needs only a **fixed positive** conditional jackpot probability, not a local success probability tending to one. Therefore a fixed `Theta(1/lambda)` reserve can be removed from round one while still harvesting `(rho-o(1))n` genuine seed vertices.

The largest numerator reserve compatible with H1-supercriticality is

`Delta := 1+epsilon - 1/h`

`       = epsilon(7-epsilon)/(8-epsilon) > 0`.

Fix for now any

`0 < sigma < Delta`.

Use three independent edge rounds with

`p1 := (1+epsilon-sigma)/lambda`,

`pg := lambda^(-4/3)`,

`pa := sigma/lambda - lambda^(-4/3)`.

For all sufficiently large `lambda`, `pa>0`. Also

`p1+pg+pa = (1+epsilon)/lambda`.

The union of these three independent Bernoulli edge sets has per-edge occupation probability

`1-(1-p1)(1-pg)(1-pa) <= p1+pg+pa = (1+epsilon)/lambda`.

Hence the three-round union is stochastically dominated by the target percolation at `p=(1+epsilon)/lambda`. Any component proved in the three-round subgraph is therefore valid for the target `G_p`. For larger `p`, monotonicity applies.

### 3.2 Round one remains uniformly supercritical after every allowed deletion

At every adaptive residual graph `H=G-S` with `|S|<rho n`, H1 gives

`Lambda_H := lambda(H) >= h lambda`.

Thus

`p1 Lambda_H >= h(1+epsilon-sigma)`

`= 1 + h(Delta-sigma)`.

Set

`u_sigma := h(Delta-sigma) > 0`.

The root-corrected Perron exploration lemma from the earlier R16 report applies with a **fixed** residual supercriticality margin `u_sigma`.

Choose a fixed jackpot cutoff

`gamma_J := u_sigma/[4(1+u_sigma)]`,

and a corresponding original-graph jackpot size

`L_J := h gamma_J lambda`.

For the local exploration on `H`, `L_J/Lambda_H <= gamma_J`, so its branching parameter satisfies

`p1 Lambda_H (1-L_J/Lambda_H)`

`>= (1+u_sigma)(1-gamma_J)`

`= 1+3u_sigma/4`.

In particular it is at least `1+u_sigma/2`. Let `q_J(sigma)>0` be the positive solution of

`q = 1-exp(-(1+u_sigma/2)q)`.

The already-proved root-corrected local lemma gives, uniformly at every adaptive trial before `rho n` vertices have been deleted,

`P(|C_v|>L_J | entire past) >= q_J(sigma) > 0`.

### 3.3 Two-scale harvesting still gives almost `rho n` seed mass

Use the seed threshold

`s := h lambda^(2/3)`

and let

`eta_lambda := lambda^(-1/6)`.

Repeat the established harvesting algorithm: expose one complete round-one component in the current residual graph, delete it, call it a seed if its size exceeds `s`, and stop when either seed mass reaches `(1-eta_lambda)rho n` or total deleted mass reaches `rho n`.

Suppose the algorithm reaches deletion mass `rho n` with seed mass below `(1-eta_lambda)rho n`. Then nonseed mass exceeds `eta_lambda rho n`. Every nonseed has size at most `s`, so the number of nonseed trials exceeds

`eta_lambda rho n/s`.

Consequently the first

`N := ceil(eta_lambda rho n/(2s))`

trials certainly exist. Their jackpot indicators have conditional probability at least `q_J(sigma)`. The adaptive exponential-Chernoff argument therefore gives

`P(number of jackpots among first N < q_J N/2) <= exp(-q_J N/8)`.

But `q_J N/2` jackpots alone carry seed mass at least

`(q_J/2) N L_J`

`>= [q_J eta_lambda gamma_J lambda^(1/3)/4] rho n`.

Since `eta_lambda=lambda^(-1/6)`, the bracket is `Theta(lambda^(1/6)) -> infinity`, contradicting the assumed seed-mass failure for all sufficiently large `lambda`.

Also

`N = Omega(n/lambda^(5/6)) >= Omega(n^(1/6)) -> infinity`

because `lambda<=n-1`. Hence the Chernoff failure probability is `o(1)`. We have proved

`W >= (rho-o(1))n`

with probability `1-o(1)`, where `W` is the total mass of **genuine connected** round-one seed components, even though a fixed numerator `sigma` was reserved from round one.

This is the crucial deformation: the old near-full first-round parameter is unnecessary once jackpot size and seed size are separated.

## 4. Round two still glues the seeds up to the old endpoint `g1`

Each seed has more than `s=h lambda^(2/3)` vertices, so the true seed-component quotient contains at most

`m <= n/[h lambda^(2/3)]`

vertices.

The preceding spectral-padding report proves a fixed positive host-edge capacity for every genuine seed-quotient cut whose smaller seed side has at least `beta n=(alpha-d1)n`. Let

`omega1 := min_{0<=d<=d1} F(d) > 0`.

(For cuts with both sides at least `alpha n`, H2 itself supplies `kappa`; the displayed `omega1` is only shorthand for the below-cutoff profile.)

For a fixed relevant quotient cut, round two misses every crossing host edge with probability at most

`exp[-omega1 pg lambda n + o(pg lambda n)]`

`<= exp[-(omega1/2)n/lambda^(1/3)]`

for all large `n`. The number of quotient cuts is at most

`2^m = exp[O(n/lambda^(2/3))]`.

Thus the union bound tends to zero. Combining with `W=(rho-o(1))n`, round two creates a connected seed component `A0` with

`|A0| >= (rho-beta-o(1))n = (g1-o(1))n`

with probability `1-o(1)`.

No disconnected coarse block is treated as connected; the quotient vertices are the actual round-one connected seed components.

At this point the preceding proof stopped. Round three will absorb a positive fraction of the unused reservoir directly into `A0`.

## 5. A host degree-quantile lemma from the endpoint pair capacity

This is the deterministic bridge from H2/spectral padding to absorption.

Fix any `d<d1` sufficiently close to `d1`, and write

`a := a(d)=rho-alpha+d`,

`b := alpha-d`,

so that

`a+b=rho`, `b>beta`, and `a<g1`.

For every constant `c<F(d)`, the preceding host-pair theorem implies that for all sufficiently large `n`, every disjoint pair `A,B` with

`|A|=an+o(n)`, `|B|=bn+o(n)`

satisfies

`e(A,B) >= c lambda n`.

### Lemma 1 (uniform reservoir degree quantile)

Fix such an `A`. For every `0<theta<1`, all but fewer than `bn+o(n)` vertices of `V\A` satisfy

`d_A(v) >= (1-theta)c lambda/b`.

Consequently at least

`(1-a-b-o(1))n = (1-rho-o(1))n`

vertices outside `A` have that many neighbors in `A`.

#### Proof

If at least `bn+o(n)` vertices outside `A` had degree to `A` strictly below `(1-theta)c lambda/b`, choose `B` of size `bn+o(n)` entirely from them. Then

`e(A,B) < (1-theta)c lambda n + o(lambda n) < c lambda n`

for large `n`, contradicting the uniform pair-capacity lower bound. The count of high-degree vertices is therefore at least

`|V\A|-bn-o(n) = (1-a-b-o(1))n`.

Since `a+b=rho`, this is `(1-rho-o(1))n`. `QED`

The important feature is that the guaranteed high-degree reservoir mass is the **full fixed density `1-rho`**, independent of how small `b` is, while each such vertex has `Theta(lambda)` independent potential attachment edges into the anchor `A`.

## 6. Method #13 — anchor a connected set; absorption can only increase it

Condition on rounds one and two, and let `A0` be the connected seed giant from Section 4. Round three is still completely independent.

Choose `d<d1` and set `A` to be any subset of `A0` of size `a(d)n+o(n)`. This is possible because `|A0|/n >= g1-o(1)` and `a(d)<g1` by a fixed amount when `d<d1` is fixed.

Let

`y := |A0\A|/n`.

At least `(1-rho-o(1))n` vertices outside `A` have

`d_A(v) >= (1-theta)c lambda/b`.

At most `yn` of these can already lie in `A0\A`. Therefore at least

`(1-rho-y-o(1))_+ n`

high-degree vertices lie outside the current connected component `A0`.

For each such vertex `v`, the event that round three opens at least one edge from `v` into the anchor `A` has probability

`1-(1-pa)^{d_A(v)}`

`>= 1-exp[-pa d_A(v)]`.

Since

`pa lambda = sigma-lambda^(-1/3) -> sigma`,

for every fixed `r` satisfying

`r < 1-exp[-sigma(1-theta)c/b]`

all sufficiently large `n` give attachment probability at least `r` for every high-degree reservoir vertex.

For distinct outside vertices these attachment events depend on disjoint sets of round-three edges into `A`, hence are independent. Chernoff therefore implies that, with probability `1-o(1)`, at least an `(r-o(1))` fraction of the high-degree reservoir vertices outside `A0` attach directly to `A`. Each attached vertex joins the connected component containing `A0`.

The resulting normalized connected mass is at least

`|A0|/n + r(1-rho-y)_+ - o(1)`.

Because `|A0|/n = a+y`, this is

`a + y + r(1-rho-y)_+ - o(1)`.

For `0<=y<=1-rho`, the expression is

`a + r(1-rho) + (1-r)y`,

which is **increasing in `y`**. If `y>=1-rho`, the component already has normalized size at least `a+1-rho`, even larger than the value obtained at the boundary. Thus, once the anchor `A` is frozen, having a larger pre-absorption giant can never hurt the final lower bound. This is the monovariant used in the run.

Since the smallest possible pre-absorption giant has size `g1-o(1)`, we have

`y >= g1-a-o(1) = d1-d-o(1)`.

Therefore round three yields

`L1/n >= g1 + r[1-rho-(d1-d)] - o(1)`

whenever `d` is sufficiently close to `d1` that the bracket is positive.

This already gives strict movement beyond `g1` for any fixed admissible choices of `sigma,d,c,theta`.

## 7. Method #29 — take the boundary limits and identify the new envelope

The preceding inequality contains four harmless slack parameters. The endpoint values cannot all be taken literally at finite `n`, because:

- `sigma=Delta` would make the H1 lower-bound on the first-round residual parameter exactly critical;
- `d=d1` would leave no fixed room between the guaranteed `g1-o(1)` seed giant and the anchor size;
- `c=F(d)` and `theta=0` remove finite-`n` slack.

But the fixed metric only asks for each constant **strictly below** a limiting envelope. We may approach these boundary points in the correct order.

As

`sigma ↑ Delta`, `d ↑ d1`, `c ↑ F(d)`, `theta ↓ 0`,

we have

`b=alpha-d ↓ beta`,

`F(d) -> F1`,

and the one-vertex round-three attachment probability tends to

`R_abs := 1-exp[-Delta*F1/beta]`.

Also `d1-d -> 0`. Hence the lower bound from Section 6 tends to

`g_abs_sup := g1 + (1-rho) R_abs`.

That is,

`g_abs_sup`

`= rho-alpha+d1`

`  + (1-rho) * {1-exp[- Delta F(d1)/(alpha-d1)]}`,

where

`Delta = epsilon(7-epsilon)/(8-epsilon)`.

### Theorem 2 (new absorption envelope)

On the unchanged frozen H1--H2--H3 class, for every fixed

`g < g_abs_sup`,

we have

`P(L1(G_p) >= g n) -> 1`

at every `p >= (1+epsilon)/lambda(G)`.

#### Proof of the limiting quantifiers

Fix `g<g_abs_sup` and let the positive gap be `zeta=g_abs_sup-g`. First choose `sigma<Delta` sufficiently close to `Delta`; this leaves a fixed positive first-round margin `u_sigma=h(Delta-sigma)>0`. Next choose `d<d1` sufficiently close to `d1`; then choose `c<F(d)` sufficiently close to `F(d)` and `theta>0` sufficiently small. By continuity, these choices can be made so that

`g1 + [1-exp(-sigma(1-theta)c/(alpha-d))] * [1-rho-(d1-d)] > g + zeta/2`.

Sections 3--6 apply with these **fixed** parameters. The first-round jackpot probability may be very small when `sigma` is close to `Delta`, but it is still a fixed positive number; the number of adaptive trials tends to infinity, so the two-scale harvesting failure remains `o(1)`. Round two gluing fails with probability `o(1)`, and the round-three independent Chernoff deficit also has probability `o(1)`. The residual `o(1)` terms are eventually smaller than `zeta/2`. Hence `L1>=gn` with probability tending to one. `QED`

Because `rho<1`, `beta>0`, `F1>0` and `Delta>0`,

`R_abs>0` and `1-rho>0`.

Therefore

`g_abs_sup > g1`.

Also `g_abs_sup<1`: indeed `g1=rho-beta<rho` and `R_abs<1`, so

`g_abs_sup < rho+(1-rho)=1`.

Thus the gain is nonvacuous and dimensionally consistent.

## 8. A completely explicit one-shot receipt, with no boundary-limit shorthand

The preceding envelope is the strongest statement from this run. For the immutable fixed metric it is useful to record a conservative explicit coefficient whose proof uses fixed numerical slack everywhere.

Take

`sigma0 := Delta/2`.

Use the same `d1` interval from the preceding report. On `[d0,d1]` it proved `F(d)>=L0/16`; therefore, for every fixed `d<d1` sufficiently close to `d1` and all sufficiently large `n`, the pair-capacity bound is at least

`(L0/32) lambda n`.

For a pair-size parameter `b<=alpha`, Lemma 1 with a factor-two degree slack gives at least `(1-rho-o(1))n` vertices of degree into the anchor at least

`L0 lambda/(64 b) >= L0 lambda/(64 alpha)`.

For all large `lambda`, round three satisfies

`pa lambda >= sigma0/2 = Delta/4`.

Hence every such high-degree vertex attaches with probability at least

`r0 := 1-exp[-Delta*L0/(256 alpha)] > 0`.

Choose

`delta0 := min{delta_spec/4, r0(1-rho)/16} > 0`,

`d := d1-delta0`,

so the anchor has density `g1-delta0`. Since the glued seed giant has size `g1-o(1)`, for all large `n` it contains the anchor and has at least `delta0/2` additional normalized mass.

If the extra seed-giant mass beyond the anchor is `y<=1-rho`, a round-three Chernoff bound gives at least half of the guaranteed attachment expectation and therefore final normalized size at least

`g1-delta0 + y + (r0/2)(1-rho-y)-o(1)`.

This is increasing in `y`; using `y>=delta0/2-o(1)` gives asymptotically

`g1 + r0(1-rho)/2 - delta0(1/2+r0/4)`.

Since `r0<=1` and `delta0<=r0(1-rho)/16`, this is at least

`g1 + 29 r0(1-rho)/64 - o(1)`.

If instead `y>=1-rho`, the pre-absorption giant itself is even larger. Therefore the clean explicit midpoint

`g_abs := g1 + r0(1-rho)/4`

satisfies

`P(L1(G_p) >= g_abs n) -> 1`.

In full parameters,

`g_abs = rho-alpha+d1`

`        + (1-rho)/4 * [1-exp{- Delta*L0/(256 alpha)}]`,

with

`Delta = epsilon(7-epsilon)/(8-epsilon)`.

This is strict fixed-metric movement because

`g_abs > g1`,

where `g1` was not merely the preceding concrete receipt but the **entire preceding proved asymptotic envelope**.

## 9. What each Section-B move actually did

### #6 — DEFORM TO A POINT YOU CAN SOLVE

I deformed the probability split away from the old vanishing reserve. A fixed `sigma/lambda` reserve is compatible with H1 as long as `sigma<Delta`. Two-scale harvesting needs only a fixed positive jackpot probability, so it still harvests `(rho-o(1))n` seed mass. This creates genuinely new probability budget for absorption.

### #13 — FIND WHAT ONLY INCREASES

After rounds one and two produce a connected seed giant, freeze a deterministic-size anchor inside it. Round-three edges can only increase that component. The worst-case lower bound

`a+y+r(1-rho-y)_+`

is increasing in the amount `y` already present outside the anchor. This removes the need to control the exact pre-absorption giant size and makes the reservoir argument monotone.

### #29 — ADD THE POINTS AT INFINITY

The sharp envelope lives on a boundary that cannot be used literally: `sigma=Delta` is critical for the H1 lower bound and `d=d1` leaves zero fixed anchor slack. Taking fixed parameters arbitrarily close to those boundary points, in the right order, yields the legitimate supremum

`g_abs_sup = g1+(1-rho)(1-exp[-Delta F1/beta])`

without ever asserting endpoint attainment.

## 10. Prior art and novelty scope

The proof uses standard ideas in percolation—independent sprinkling, attaching reservoir vertices to an established giant, Chernoff concentration—and I do **not** claim those mechanisms as novel. Classical and modern expander/pseudorandom-graph percolation papers use sprinkling to build or analyze giant components; the bounded search this run recovered, among others, Alon--Benjamini--Stacey, Krivelevich--Lubetzky--Sudakov, and later pseudorandom-graph work.

The source-specific quantitative feature here is the combination of:

1. H1 robust spectral supercriticality, which allows a fixed reserve while preserving adaptive jackpot probability;
2. the preceding R16 H2 + spectral-compression pair profile `F(d)` below the nominal H2 cutoff;
3. the degree-quantile consequence that leaves `1-rho` linear reservoir vertices with `Theta(lambda)` anchor degree;
4. a final independent `Theta(1/lambda)` absorption round.

The bounded search did not locate this exact four-step theorem, but that is not a novelty certificate. The result remains labeled **PARTIAL** for CMW Question 5.1 and requires independent audits before any closure or publication claim.

## 11. Status, next obstruction, and stuck accounting

H0002 remains **PARTIAL / SOURCE OPEN-LOOKING IN BOUNDED CURRENT SEARCH / ACTIVE**. The source asks for natural conditions in general, not merely the frozen H1--H2--H3 class.

The fixed metric moved, so the supported unchanged count remains/reset to **0** and no Section-I stuck recovery is triggered.

The new structural bottleneck is now clearer. Direct reservoir absorption from one frozen anchor can use at most the total fixed numerator reserve `Delta`, and the degree-quantile statement only guarantees a fraction `1-rho` of high-degree vertices outside the anchor. To move substantially beyond `g_abs_sup`, a genuinely different route would need one of:

- a cascade in which newly absorbed vertices themselves expose fresh H2-forced degree mass;
- a multi-block (at least 3-by-3) compression that proves a stronger degree distribution than the one-quantile lemma;
- or a way to recover supercritical first-round harvesting at the boundary `sigma=Delta` rather than merely approach it.

A next nonconsecutive triple, if H0002 remains active, is **#5 ADD A PARAMETER AND DIFFERENTIATE, #14 FIND THE GROUP ACTING, #20 FIND WHY THE ALGORITHM FAILS**. These are reuses from the 30-method catalog; all 30 had already appeared earlier on H0002, and I do not falsely label them unused.

## 12. Validation / bookkeeping (final approximately 10%)

No finite checker was created: all new claims are analytic and their proofs are on the page. No shared root, peer-track file, claim file, scheduler, email, Drive item, permission, workflow or public posting was modified. This immutable report alone carries the delta.

The scheduler/model-control limitation is unchanged. The exposed task interface provides prompt/title, schedule/start-offset, timing mode, enablement and task identity, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. GPT-6/maximum is therefore prompt-only in this run. Actually enforcing it requires scheduler/API fields that bind model and reasoning effort plus per-run runtime attestation. The historical P26 `You cannot modify this task` error was authorization-context-specific; repository evidence records a later successful P26 update from an authorized context. If a task still refuses modification, the compliant workaround is its owning authorized workspace/account or platform support, never duplication or permission bypass.

```yaml
ledger_delta:
  track: R16
  source_id: H0002
  source: "Christoph--Morawski--Wigderson, arXiv:2608.19145v1, Question 5.1"
  lane: HARD_OUTSIDE
  source_status: OPEN_LOOKING_BOUNDED_SEARCH
  result_status: PARTIAL
  metric: g_twoaxis(epsilon,rho,kappa)
  before:
    strongest_proved_envelope: "every fixed g < g1 = rho-alpha+d1"
    latest_concrete: "g_spec = rho-alpha+d0+delta_spec/2"
  after:
    concrete: "g_abs = g1 + (1-rho)/4 * (1-exp(-Delta*L0/(256*alpha)))"
    stronger_envelope: "every fixed g < g_abs_sup = g1 + (1-rho)*(1-exp(-Delta*F1/beta))"
    definitions:
      beta: "alpha-d1 > 0"
      F1: "F(d1) > 0"
      Delta: "epsilon*(7-epsilon)/(8-epsilon) > 0"
  movement: true
  supported_unchanged_count: 0
  methods: [6, 13, 29]
  stuck_recovery: false
  nominal_beck_fiala_status: "KNOWN current-literature baseline on stated Sep-2026 Komlos preprints; not reopened"
  finite_checker: "not applicable; analytic proof"
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
```
