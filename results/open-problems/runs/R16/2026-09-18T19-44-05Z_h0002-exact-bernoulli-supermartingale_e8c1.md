Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the canonical frozen H0002 class, the concrete certified giant fraction moves from `rho*(q_prev-q0/64)` to `rho*(q_new-q0/64)`, where `q_prev=(q_old+q_arch)/2`, `q_new=(q_arch+q_KL)/2`, and `q_KL=1-(1+u_inf)exp(-u_inf)>q_arch`. More strongly, every fixed coefficient strictly below `rho*(q_KL-q0/64)` is certified. Section-B methods actually used: **#18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT, #30 DO ONE SCALE AT A TIME**. All 30 catalogued moves had already been used on H0002, so this is a nonconsecutive reuse on a genuinely new obligation rather than invented unused history.

# R16 — H0002: exact Bernoulli supermartingale breaks the previous CMW black-box envelope

## 1. Continuity, ownership, required reads, and source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: find natural conditions under which, at `p >= (1+epsilon)/lambda(G)`, bond percolation has a component of order `Omega(|G|)` with constant probability.

Before research I reread/reconciled the required control surfaces: `probability_campaign_2026_09/INDEX.md`, `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/H0002.md`, the H-intake row for H0002, the newest own report `runs/R16/2026-09-18T18-47-58Z_h0002-vanishing-scale-cmw-envelope_d42f.md`, and the newest recoverable same-source neighboring terminal/handoff records G0010 (Question 5.2) and G0011 (long-cycle conjecture). No release/handoff of H0002 was found.

Fresh 18 Sep 2026 primary/current checks still show arXiv:2608.19145 only as v1 from 19 Aug 2026; Yuval Wigderson's current publication page still lists that paper, and a bounded title/question/author search found no later source-matching resolution of Question 5.1. This is bounded-search evidence, not a worldwide novelty certificate.

The native Beck--Fiala title remains stale as an active research assignment. Bansal--Jiang arXiv:2508.03961v2 prove `O(sqrt(t))` for `t>=log^2 n` and weaker polylogarithmic bounds below that regime. More decisively, Guo--Fang--Lu arXiv:2609.11189v1 (10 Sep 2026) prove the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`. Karingula--Lovett ECCC TR26-188 (17 Sep 2026) independently give an elementary Komlos proof with constant 36. These are extremely recent primary-source baselines, not R16 discoveries.

Primary URLs checked this run:

- `https://arxiv.org/abs/2608.19145`
- `https://arxiv.org/abs/2508.03961`
- `https://arxiv.org/abs/2609.11189`
- `https://eccc.weizmann.ac.il/report/2026/188/`
- `https://ywigderson.math.ethz.ch/math/publications/`

## 2. Frozen H0002 class and incoming metric

Fix `0<epsilon<=1`, `rho,kappa>0`, let `n=|G|`, `lambda=lambda(G)`, and put

`a0 := 1-epsilon/8`,

`q0 := 1-exp(-epsilon^2/288)`,

`alpha0 := rho*q0/64`.

The frozen graph class is unchanged:

- **H1:** `lambda(G-S) >= a0 lambda` whenever `|S|<=rho n`;
- **H2:** `e_G(A,B) >= kappa lambda n` for disjoint `A,B` with `|A|,|B|>=alpha0 n`;
- **H3:** `lambda(G)->infinity`.

The tracked quantity is the largest explicit uniform giant fraction `g_twoaxis(epsilon,rho,kappa)` certified on this class.

The previous run defined

`u_inf := a0*(1+epsilon)-1 = epsilon*(7-epsilon)/8`,

`Psi_inf := u_inf^2/[4(1+u_inf)]`,

`q_arch := 1-exp(-Psi_inf)`,

and proved every fixed coefficient strictly below `rho*(q_arch-q0/64)`. Its single-number receipt was

`q_prev := (q_old+q_arch)/2`,

`g_prev := rho*(q_prev-q0/64)`.

That report also proved that `q_arch` is the ceiling of the *particular quadratic CMW Lemma 2.5 black-box bound* used there. The next obligation was therefore to improve the local exploration law itself rather than optimize the same quadratic again.

## 3. Method #18 — rewrite the exploration concentration as an exact exponential supermartingale

The earlier line used CMW Lemma 2.5(2), whose convenient quadratic lower-tail exponent contains the factor `p a(1-a)`. For Bernoulli edge queries one can retain the exact one-step Laplace transform instead.

### Exact predictable-query lemma

Let `(xi_i)` be the open/closed indicators of adaptively queried edges in Bernoulli-`p` bond percolation. At query `i`, let `x_i in [0,1]` be a predictable weight (measurable before `xi_i` is exposed). Write

`S_t := sum_{i<=t} xi_i x_i`,

`Q_t := sum_{i<=t} x_i`.

For every `a>=0`,

`M_t := exp( -a S_t + p(1-exp(-a)) Q_t )`

is a nonnegative supermartingale.

Indeed, conditionally on the past and on `x=x_i`,

`E exp(-a xi_i x) = 1-p+p exp(-a x)`

`                 = 1-p(1-exp(-a x))`.

Because `x -> 1-exp(-a x)` is concave on `[0,1]` and vanishes at zero,

`1-exp(-a x) >= x(1-exp(-a))`.

Hence

`1-p+p exp(-a x) <= 1-p x(1-exp(-a))`

`                    <= exp(-p x(1-exp(-a)))`,

which is exactly the supermartingale inequality. Since the graph is finite, the component exploration has a bounded stopping time, so optional stopping gives `E M_T<=1` without an integrability issue.

### Sharpened weighted component lemma

Use the same Perron-weighted breadth-first exploration as CMW. Let `H` be a graph and let `w in [0,1]^{V(H)}` satisfy

`sum_{y in N_H(x)} w(y) >= Lambda w(x)`

for every vertex `x`. Suppose

`p >= (1+u)/Lambda`, `0<u<=1`,

and fix `0<gamma<u/(1+u)`. Put

`b := (1+u)(1-gamma) > 1`.

For a starting vertex `v`, let `C_v` be its percolation component and `W=w(C_v)`. During the complete exploration of a component `C`, let `Q` be total queried target weight and `S` successful queried target weight.

If `|C|<=gamma Lambda`, then

`Q >= (1-gamma)Lambda W`.

This deterministic inequality can be checked directly: summing the weight-expansion inequality over `x in C` gives at least `Lambda W` total neighbor weight. The contribution of neighbors still inside `C` is at most `|C|W<=gamma Lambda W`; every edge from `C` to the complement is queried and contributes its outside endpoint weight to `Q`.

Also `S<=W`, because every successful query discovers a previously undiscovered component vertex and each such vertex is charged at most once.

Therefore, on

`E_C := {|C_v|<=gamma Lambda, W>=C}`,

the stopped supermartingale exponent obeys

`-a S + p(1-exp(-a))Q`

`>= [-a + b(1-exp(-a))] W`.

The exact scalar exponent is

`G_b(a) := b(1-exp(-a))-a`.

It is strictly concave, and its unique maximizer is

`a_* = log b`,

because `G_b'(a)=b exp(-a)-1`. The maximum is

`I(b) := G_b(log b) = b-1-log b`.

Consequently, Markov's inequality gives the sharpened exploration bound

`P( |C_v|<=gamma Lambda and w(C_v)>=C )`

`<= exp( -[b-1-log b] C ).`

In particular, normalizing a Perron vector so that the starting vertex has weight one yields the one-trial certificate

`q_KL(u,gamma) := 1-exp(-(b-1-log b))`

for producing a component larger than `gamma Lambda`.

This argument does **not** use the restriction `a<=1/2`; it proves the needed concentration directly from the Bernoulli query law.

## 4. Method #24 — identify the new extremal exponent and prove it strictly beats the old envelope

The previous architecture ceiling at scalar parameter `b>1` was

`f(b) := (b-1)^2/(4b)`.

The exact Bernoulli-supermartingale exponent is

`I(b) := b-1-log b`.

It is strictly larger for every `b>1`. Define

`R(b)=I(b)-f(b)`.

Then `R(1)=0` and

`R'(b) = (b-1)(3b-1)/(4b^2) > 0`

for `b>1`. Hence `I(b)>f(b)` strictly.

At the H0002 limiting first-round margin, set

`b0 := 1+u_inf = a0(1+epsilon)`.

The new local architecture limit is

`I_inf := u_inf-log(1+u_inf)`,

`q_KL := 1-exp(-I_inf)`

`      = 1-(1+u_inf)exp(-u_inf)`.

Since `I_inf>Psi_inf`,

`q_KL > q_arch`.

For orientation only:

- at `epsilon=0.5`, `q_arch≈0.0289140` while `q_KL≈0.0632355`;
- at `epsilon=1`, `q_arch≈0.0772133` while `q_KL≈0.1733585`.

These numbers are sanity checks only; strict movement is the analytic inequality above.

There is also a method-level sharpness reason for the rate function `I(b)`. If all query weights are one, `p->0`, and the number of queries is chosen so that the mean number of successes is `bC`, the lower-tail event of at most `C` successes converges to the corresponding Poisson large-deviation problem, whose rate per `C` is exactly `b-1-log b`. Thus no uniformly stronger scalar exponent can be expected from only `(S<=W, Q>=bW/p, x_i in [0,1])` in the sparse-query limit. Improving beyond `q_KL` will need genuinely more structural information about the exploration, not merely a sharper generic Bernoulli Chernoff step.

## 5. Method #30 — propagate the new local law at one vanishing scale

Reuse the valid vanishing-scale split from the preceding run:

`tau := lambda^(-1/3)`,

`d := epsilon tau`,

`p1 := (1+epsilon-d)/lambda`,

with independent `p2` defined by `1-p=(1-p1)(1-p2)` at `p=(1+epsilon)/lambda`. Then

`p2 >= epsilon lambda^(-4/3)`.

After any allowed deletion, H1 gives first-round residual margin

`u_tau := u_inf-a0 epsilon tau`,

and take component cutoff

`gamma_tau := tau`.

For all sufficiently large `lambda`, `gamma_tau<u_tau/(1+u_tau)`. Put

`b_tau := (1+u_tau)(1-tau)`,

`I_tau := b_tau-1-log b_tau`,

`q_tau := 1-exp(-I_tau)`.

The exact subtraction from the previous run remains

`0 <= b0-b_tau <= 3 tau`.

Since `I'(b)=1-1/b<=1` on `b>=1`,

`0 <= I_inf-I_tau <= 3 tau`,

and therefore

`0 <= q_KL-q_tau <= 3 tau`.

Hence for every fixed `zeta>0`, once `tau<=zeta/3` (and the basic admissibility bounds hold),

`q_tau >= q_* := q_KL-zeta`.

### Seed phase, restated

A successful first-round component has more than

`s_tau := a0 tau lambda = a0 lambda^(2/3)`

vertices. Run adaptive residual explorations until either successful mass reaches `q_* rho n` or total deleted mass reaches `rho n`. Each trial succeeds conditionally with probability at least `q_*`; successes have size `>s_tau`, failures have size `<=s_tau`.

Let `R=rho n`, `y=R/s_tau`, `k=ceil(q_* y)`, `r=floor((1-q_*)y)+1`. Failure of the target forces `r` comparison failures before the `k`-th success. The probability of reaching `k` successes first is

`P(Bin(k+r-1,q_*)>=k)`.

As `y->infinity` this tends to `1/2`; on bounded `y`, only finitely many `(k,r)` occur and each has strictly positive probability. Therefore the seed target has a uniform positive lower probability `c_seed(q_*)>0`.

### Sprinkle phase, restated on genuine connected seed components

Condition on seed mass `W>=q_* rho n`. The true seed-component quotient has at most

`m <= n/s_tau = n/(a0 lambda^(2/3))`

vertices. Provided `q_*>3q0/64`, if no sprinkled component captures at least `W-alpha0 n` seed vertices, the deterministic balanced-cut extraction on this **genuine** component quotient produces a cut with at least `alpha0 n` original vertices on each side. H2 supplies at least `kappa lambda n` host edges across that cut.

A fixed cut survives round two with probability at most

`exp(-kappa epsilon n lambda^(-1/3))`.

Union-bounding over all quotient cuts gives

`P(any bad cut | seed)`

`<= exp{ [(log 2)/(a0 lambda^(2/3)) - kappa epsilon/lambda^(1/3)] n }`

`= o(1)`.

Thus, for every fixed `zeta>0` with

`q_KL-zeta > 3q0/64`,

there exists an explicit `Lambda_0(epsilon,kappa,zeta)` such that on the frozen H1--H2--H3 class,

`P( L1(G_p) >= rho*(q_KL-zeta-q0/64) n )`

`>= c_seed(q_KL-zeta)-o(1)`

for every `p>=(1+epsilon)/lambda` and all sufficiently large graphs.

An admissible threshold is obtained by requiring

`lambda^(-1/3) <= min{1/2, u_inf/6, zeta/3}`

and

`lambda^(1/3) >= 2 log(2)/(a0 kappa epsilon)`.

Therefore **every fixed giant coefficient strictly below**

`g_KL_sup := rho*(q_KL-q0/64)`

is now certified.

## 6. Concrete fixed-metric movement

The incoming single-number receipt had seed coefficient

`q_prev=(q_old+q_arch)/2 < q_arch`.

Choose the new canonical midpoint

`q_new := (q_arch+q_KL)/2`.

Since `q_new<q_KL`, the theorem above applies with

`zeta_new := (q_KL-q_arch)/2>0`.

Moreover

`q_new > q_arch > q_prev`.

Hence the new concrete metric is

`g_new := rho*(q_new-q0/64)`,

with strict movement

`g_new-g_prev = rho*(q_new-q_prev) > 0`.

This is movement on exactly the same frozen H1--H2--H3 graph class; no hypothesis was strengthened and no metric was changed.

## 7. Prior-art scope and novelty label

The exponential-supermartingale calculation is a standard Chernoff/Bennett-type idea in probability, so I do **not** claim the generic inequality `b-1-log b` as novel. A bounded search for the exact displayed H0002 percolation reduction did not find a source stating this sharpened two-axis theorem or coefficient. That negative search is not a novelty certificate.

The R16 contribution here is the source-matching integration: replacing the quadratic CMW concentration black box inside the Perron-weighted adaptive exploration, proving the exact stopped-query inequality in the needed adaptive form, and propagating it through the already repaired genuine-component seed/sprinkle argument. Any publication claim needs a deeper literature search and outside proof audits.

## 8. Status, counter, and next direction

Status remains **PARTIAL / SOURCE OPEN / ACTIVE**.

The fixed metric moved, so the supported unchanged count remains/resets to **0**. No stuck recovery is active.

The previous quadratic envelope is genuinely broken. The new scalar sparse-query envelope is `q_KL`. The next substantive route should not re-optimize the same one-dimensional Laplace transform. To move beyond `q_KL`, exploit information discarded by the scalar query summary—e.g. the distribution of target weights, a second moment/variance profile of the Perron mass, or correlations forced by graph geometry—or improve the global gluing so that the final `alpha0` loss can be reduced under a source-natural hypothesis.

All 30 numbered methods have already been used on H0002. A later run should again reuse a nonconsecutive method only for a genuinely new obligation, explicitly recording that the catalog is exhausted.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R16
  canonical_target: H0002
  source: Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1
  status_before: PARTIAL / SOURCE OPEN / ACTIVE
  status_after: PARTIAL / SOURCE OPEN / ACTIVE
  metric: g_twoaxis(epsilon,rho,kappa), frozen H1-H2-H3 class
  value_before: rho*(q_prev-q0/64), q_prev=(q_old+q_arch)/2
  value_after: rho*(q_new-q0/64), q_new=(q_arch+q_KL)/2
  stronger_family: every fixed rho*(q_KL-zeta-q0/64) with zeta>0 and q_KL-zeta>3q0/64
  architecture_supremum: rho*(q_KL-q0/64), endpoint not claimed attained
  q_KL: 1-(1+u_inf)*exp(-u_inf)
  u_inf: epsilon*(7-epsilon)/8
  movement: strict
  unchanged_count_before: 0
  unchanged_count_after: 0
  methods_used: [18, 24, 30]
  previous_methods: [3, 5, 20]
  artifacts: none; analytic theorem, no finite computational core
  beck_fiala_current_primary_baseline: discrepancy < 3*sqrt(2*pi*t) for every integer t>=1 and all n, Guo-Fang-Lu arXiv:2609.11189v1; KNOWN not R16
```

## 10. Model and task-control limitation

The task-control limitation remains unchanged in the interface exposed to this run: there is no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt. GPT-6/maximum therefore remains a prompt request only; this run actually identifies as GPT-5.6 Sol with reasoning level UNVERIFIED.

Enforcing GPT-6/maximum would require explicit model-family and reasoning-effort fields in the authorized scheduler/API plus per-run runtime attestation. The repository also records that the historical P26 `You cannot modify this task` denial was authorization-context-specific and that a later update succeeded from an authorized context. For any task that still returns that error, the compliant route is the owning authorized workspace/account context or platform support, never duplication or permission bypass.

No scheduler modification, shared-root edit, peer-file edit, email, Drive action, public posting, purchase, permission change, or workflow execution was attempted in this run.