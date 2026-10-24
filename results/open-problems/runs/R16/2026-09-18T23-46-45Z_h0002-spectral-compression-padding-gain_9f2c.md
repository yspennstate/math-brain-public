Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the unchanged frozen H0002 class, the preceding asymptotic envelope `rho-alpha+d0` is strictly exceeded: this run proves the concrete constant `g_spec = rho-alpha+d0+delta_spec/2`, with explicit positive `delta_spec` below. Section-B methods actually used: **#11 DUALIZE, #3 PROVE SOMETHING STRONGER, #25 COUNT THE SAME THING TWICE**. All 30 catalogued moves had already been used on H0002, so this is an honest nonconsecutive reuse rather than invented unused history.

# R16 — H0002: spectral compression breaks the one-sided-padding envelope

## 1. Continuity, ownership, required reads, and current-source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural graph hypotheses under which, for `p >= (1+epsilon)/lambda(G)`, bond percolation contains a component of order `Omega(|G|)` with constant probability.

Before doing mathematics I reread/reconciled the required repository state: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/claims/H0002.md`, the H-intake/source record, the newest own report `runs/R16/2026-09-18T22-43-43Z_h0002-one-sided-padding-gain_b4c9.md`, and the newest recoverable neighboring same-source records. The neighboring G0010 line is already at terminal HARD handoff and the earlier G0011 same-source line has handed off / moved to successor-admission state; neither alters R16's exclusive H0002 ownership.

Fresh primary-source checks in this run still find CMW as arXiv:2608.19145v1, dated 19 Aug 2026, and the bounded current search did not locate a later source-matching resolution of Question 5.1. I also searched combinations of `finite graph percolation`, `spectral radius`, `quotient matrix`, `large-set expansion`, `sprinkling`, and `giant component`. The search recovered CMW and standard spectral/percolation background, but not the exact density-averaged H2 plus two-by-two compression argument below. This is only a bounded negative search, not a novelty certificate. The 2-by-2 compression/Rayleigh step itself is standard spectral graph theory and is not claimed as a new mechanism in isolation.

Primary/current references checked this run:

- https://arxiv.org/abs/2608.19145 — CMW, source question;
- https://arxiv.org/abs/2508.03961 — Bansal--Jiang v2;
- https://arxiv.org/abs/2609.11189 — Guo--Fang--Lu, 10 Sep 2026;
- https://eccc.weizmann.ac.il/report/2026/188/ — Karingula--Lovett, 17 Sep 2026.

The native Beck--Fiala title remains stale as an unresolved research target. Bansal--Jiang v2 prove the conjectured `O(sqrt(t))` order directly only for `t >= log^2 n`, with a weaker polylogarithmic-loss estimate below that range. But Guo--Fang--Lu state the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce, for every integer `t>=1` and every `n`, set-system discrepancy `< 3 sqrt(2 pi t)`. Karingula--Lovett independently give an elementary Komlos proof with constant `36`. These are extremely recent preprint/technical-report results, so I record them as current primary-source baselines rather than mature refereed consensus. On their stated theorems the original square-root Beck--Fiala target is presently KNOWN, so R16 continues its already-admitted H0002 successor instead of pretending the `t<log^2 n` regime remains open.

## 2. Frozen H0002 class and incoming quantitative state

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n := |G|`, `lambda := lambda(G)`,

`q0 := 1-exp(-epsilon^2/288)`,

`alpha := rho*q0/64`.

The frozen class is unchanged:

1. **H1 (spectral deletion resilience):** `lambda(G-S) >= (1-epsilon/8)lambda` whenever `|S|<=rho n`;
2. **H2 (macroscopic pair expansion):** `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. **H3:** `lambda -> infinity` along the graph sequence.

The fixed metric is `g_twoaxis(epsilon,rho,kappa)`, the largest explicit constant proved uniformly on this exact class such that at `p >= (1+epsilon)/lambda` the percolated graph has a component of at least `g n` vertices with probability bounded below by a positive constant depending only on the frozen parameters.

The preceding R16 run proved every fixed coefficient strictly below

`g_pad^sup = rho-alpha+d0`,

where, on a nonvacuous asymptotic H1--H2--H3 sequence,

`d0 := kappa*(rho-alpha)/(alpha-kappa)`.

It also gave a smaller explicit one-shot receipt with slack. The apparent barrier was that the one-sided padding lower bound

`e(A,B)/(lambda n) >= kappa-alpha*d/a-o(1)`

vanishes at `d=d0`, for a seed cut with

`|B|/n = alpha-d`, `|A|/n approximately rho-alpha+d`.

This run shows that the vanishing is an artefact of bounding the internal density of `A` by its trivial spectral maximum. H2 itself forces `A` to have substantial edge mass to its **full complement**, and a 2-by-2 spectral compression converts that external mass into a strict deficit in the allowable internal density of `A`. Feeding that deficit back into the same padding average yields positive crossing capacity even at `d=d0`, and hence a strict interval beyond the old envelope.

## 3. Preliminary nonvacuity facts

Two simple consequences of the frozen assumptions will be used repeatedly.

### Lemma 1 (nonvacuity forces `rho<1`)

Along any H3 sequence, `lambda>0` eventually. If `rho>=1`, H1 may be applied with `S=V(G)`, giving

`0 = lambda(empty graph) >= (1-epsilon/8)lambda > 0`,

a contradiction. Hence every nonvacuous asymptotic frozen sequence has

`0<rho<1`.

In particular `alpha=rho q0/64<rho/64<1`.

### Lemma 2 (H2 forces `kappa<=alpha^2+o(1)`)

Let `k=ceil(alpha n)` and choose an ordered pair `(X,Y)` of uniformly random disjoint `k`-subsets. Every H2 pair satisfies

`e(X,Y) >= kappa lambda n`.

On the other hand each host edge is split between `X,Y` with probability

`2 k^2/[n(n-1)]`,

so

`E e(X,Y) = |E(G)| * 2 k^2/[n(n-1)]`.

The all-ones Rayleigh quotient gives `2|E(G)|<=lambda n`, hence

`kappa lambda n <= E e(X,Y) <= lambda k^2/(n-1)`.

Therefore

`kappa <= k^2/[n(n-1)] = alpha^2+o(1)`.

Since `kappa` and `alpha` are fixed, nonvacuity implies `kappa<=alpha^2<alpha`. Thus the denominator `alpha-kappa` below is strictly positive. Moreover, because `rho<1`,

`d0 = kappa(rho-alpha)/(alpha-kappa) < alpha`.

(The last inequality is equivalent to `kappa rho < alpha^2`, which follows from `kappa<=alpha^2` and `rho<1`.)

Define the old endpoint geometry

`b0 := alpha-d0 > 0`,

`a0 := rho-b0 = rho-alpha+d0`,

`c0 := 1-a0 = 1-rho+b0 > 0`.

## 4. Method #3 + #25 — average H2 over all subpairs, not just one witness pair

The old padding proof used H2 once after selecting one `alpha n` subset. The stronger statement comes from averaging H2 over **all** choices.

Let `A,C` be disjoint, with

`|A|=a n`, `|C|=c n`.

Write

`x(A,C) := e(A,C)/(lambda n)`

and

`q_A := 2e(A)/(lambda a n)`.

By the Rayleigh quotient, `0<=q_A<=1`.

### Lemma 3 (density-amplified H2 for two large sides)

If `a,c>=alpha`, then

`x(A,C) >= kappa*a*c/alpha^2 - o(1)`.

#### Proof

Choose uniformly `X subset A`, `Y subset C` with `|X|=|Y|=ceil(alpha n)`. Every such pair is disjoint and H2 gives `e(X,Y)>=kappa lambda n`. An edge between `A` and `C` is retained with probability

`(alpha/a)(alpha/c)+o(1)`.

Therefore

`kappa lambda n <= E e(X,Y) = [alpha^2/(ac)+o(1)] e(A,C)`,

which rearranges to the claim. `square`

This strengthens the crude `x>=kappa`: if `A` and `C` are much larger than the H2 cutoff, demanding H2 for **every** alpha-subpair forces proportionally more total edge mass between the whole sets.

### Lemma 4 (density-amplified H2 when the complement is below the cutoff)

If `a>=alpha` and `0<c<alpha`, then

`x(A,C) >= a*kappa/alpha - (alpha-c) - o(1)`.

#### Proof

Put `h=alpha-c`. Choose an ordered disjoint pair `X,D subset A` with sizes `alpha n` and `h n` (rounding changes only `o(1)`). H2 applies to `X` and `C union D`, hence

`e(X,C)+e(X,D) >= kappa lambda n`.

Averaging over `(X,D)` gives

`E e(X,C) = (alpha/a)e(A,C)+o(lambda n)`,

and

`E e(X,D) = (alpha h/a) q_A lambda n + o(lambda n)`.

Thus

`(alpha/a)x + (alpha h/a)q_A >= kappa-o(1)`.

Using `q_A<=1` yields

`x >= a*kappa/alpha-h-o(1)`,

which is the claim. `square`

For the ideal seed-cut geometry parametrized by deficit `d`, set

`a(d):=rho-alpha+d`,

`c(d):=1-a(d)=1-rho+alpha-d`.

Define the deterministic lower profile

`Xi(d) := kappa*a(d)*c(d)/alpha^2` if `c(d)>=alpha`,

and

`Xi(d) := a(d)*kappa/alpha-(alpha-c(d))` if `c(d)<alpha`.

The two formulas agree at `c=alpha`, so `Xi` is continuous. On the first branch

`Xi'(d)=kappa(c-a)/alpha^2`,

whose absolute value is at most `kappa/alpha^2<=1`; on the second branch

`Xi'(d)=kappa/alpha-1`,

whose absolute value is `<1`. Hence `Xi` is globally 1-Lipschitz on the relevant interval.

At the previous endpoint `d=d0`, the relation

`a0*kappa/alpha = d0`

holds exactly. Therefore

`Xi0 := Xi(d0)`

has the explicit positive form

- if `c0>=alpha`, `Xi0 = kappa*a0*c0/alpha^2 = d0*c0/alpha > 0`;
- if `c0<alpha`, `Xi0 = d0-(alpha-c0) = 1-rho > 0`.

So H2 forces a **strictly positive** amount of normalized edge mass from the old-endpoint large seed side `A` to its full complement `C=V\A`.

## 5. Method #11 — 2-by-2 spectral compression converts complement mass into internal-density slack

The previous padding argument used only `q_A<=1`. That is wasteful once `x(A,C)>0`.

Let

`u := 1_A/sqrt{|A|}`, `v := 1_C/sqrt{|C|}`.

Compress the normalized adjacency operator `Adj(G)/lambda` to `span{u,v}`. Its matrix is

`Q = [[q_A, y],[y,q_C]]`,

where

`q_C := 2e(C)/(lambda c n) >= 0`,

`y := e(A,C)/(lambda n sqrt{ac}) = x/sqrt{ac}`.

Because `lambda` is the top eigenvalue of `Adj(G)`, every Rayleigh quotient of `Adj(G)/lambda` is at most one. Hence `I-Q` is positive semidefinite. Therefore

`(1-q_A)(1-q_C) >= y^2`.

Since `q_C>=0`, we have `1-q_C<=1`, and consequently

`1-q_A >= y^2`.

Thus

`q_A <= 1 - x^2/(ac)`.

Combining this with Lemmas 3--4 gives, uniformly at the ideal deficit `d`,

`q_A <= 1 - Xi(d)^2/[a(d)c(d)] + o(1)`.

This is the missing feedback: strong external coupling of `A` forbids `A` from simultaneously saturating the trivial internal Rayleigh bound.

## 6. Feed the spectral slack back into one-sided padding

Consider a seed quotient cut `(A,B)` with

`|B|/n = alpha-d < alpha`,

and let `A` be the other seed side. First work in the ideal limiting geometry where total seed mass is `rho n`, so `|A|/n=a(d)`.

Choose uniformly disjoint `X,D subset A` with

`|X|=alpha n`, `|D|=d n`.

H2 applies to `X` and `B union D`. Average exactly as in the previous one-sided-padding report, but **do not** replace `q_A` by one:

`(alpha/a) * [e(A,B)/(lambda n)] + (alpha d/a) q_A >= kappa-o(1)`.

Writing

`z(d):=e(A,B)/(lambda n)`,

we get

`z(d) >= a(d)*kappa/alpha - d q_A - o(1)`.

Insert the compressed bound on `q_A`:

`z(d) >= F(d)-o(1)`,

where

`F(d) := a(d)*kappa/alpha - d + d*Xi(d)^2/[a(d)c(d)]`.

The first two terms are exactly the old one-sided-padding expression. Since `d0` was its zero,

`a(d)*kappa/alpha-d = [(alpha-kappa)/alpha]*(d0-d)`.

At the old endpoint this part vanishes, but the spectral term does not:

`F(d0) = d0*Xi0^2/(a0*c0) =: L0 > 0`.

This is the central quantitative gain of the run. The previous asymptotic barrier was not a real barrier of H1--H2--H3; it was the cost of forgetting how H2 constrains `A` against the unused complement.

## 7. An explicit positive interval beyond the old endpoint

Define

`Gamma0 := Xi0^2/(a0*c0)`,

`L0 := d0*Gamma0`,

and

`delta_spec := min{ (alpha-d0)/2, c0/2, Xi0/2, L0/16 }`.

Every entry in this minimum is strictly positive, so `delta_spec>0`. Put

`d1 := d0+delta_spec`.

For every `d in [d0,d1]`, the 1-Lipschitz property and `delta_spec<=Xi0/2` give

`Xi(d) >= Xi0/2`.

Also `a(d)<=a0+alpha/2<=2a0` (indeed `alpha<rho/64<a0`) and `c(d)<=c0`, while `delta_spec<=c0/2` keeps `c(d)>0`. Therefore the spectral bonus obeys

`d*Xi(d)^2/[a(d)c(d)]`

`>= d0*(Xi0^2/4)/(2a0*c0)`

`= L0/8`.

The old linear term satisfies

`a(d)*kappa/alpha-d`

`= -[(alpha-kappa)/alpha]*(d-d0)`

`>= -(d-d0)`

`>= -delta_spec`

`>= -L0/16`.

Hence

`F(d) >= L0/16 > 0`

throughout `[d0,d1]`.

For `0<=d<d0`, the old linear term is already strictly positive and the spectral bonus is nonnegative. At `d=d0`, `F=L0>0`. Thus `F` is continuous and strictly positive on the entire compact interval `[0,d1]`; define

`omega0 := min_{0<=d<=d1} F(d) > 0`.

Integer rounding changes these normalized estimates by `o(1)`. Likewise the first-round seed mass from the already-proved two-scale harvesting theorem is `W=(rho-o(1))n` rather than exactly `rho n`; this perturbs `a,c,Xi,F` by `o(1)` uniformly on the compact interval. Consequently, for all sufficiently large `n`, **every** genuine seed-quotient cut whose smaller seed side has size at least

`(alpha-d1)n`

has at least

`(omega0/2) lambda n`

host edges crossing it. If both sides are at least `alpha n`, use H2 directly; if the smaller side is in `[(alpha-d1)n,alpha n)`, use the argument above.

## 8. Sprinkling: turn the new cut capacity into a larger connected component

Now reuse only the already-validated parts of the preceding R16 architecture.

Take the same vanishing split scale

`tau=lambda^(-1/3)`

and first-round probability

`p1=(1+epsilon-epsilon*tau)/lambda`.

The prior two-scale harvesting argument, based on H1 and the root-corrected Perron exploration, gives with probability `1-o(1)` a family of **genuine connected** first-round seed components with total seed mass

`W >= (rho-o(1))n`,

and every seed component has more than

`s=(1-epsilon/8)lambda^(2/3)`

vertices. Therefore the true seed-component quotient has at most

`m <= n/[(1-epsilon/8)lambda^(2/3)]`

vertices. No union of disconnected components is treated as connected.

The independent second-round sprinkle has

`p2 >= epsilon lambda^(-4/3)`.

Suppose after sprinkling no connected quotient component contains at least

`W-(alpha-d1)n`

seed vertices. Since `alpha<rho/64` and `d1<alpha`, the standard greedy extraction on the **actual quotient components** gives a quotient cut with both seed sides of size at least `(alpha-d1)n`. By Section 7, every such cut has at least `(omega0/2)lambda n` host edges crossing it. The probability that a fixed such cut receives no sprinkled edge is at most

`exp[-(omega0/2) p2 lambda n]`

`<= exp[-(omega0*epsilon/2) n/lambda^(1/3)]`.

There are at most `2^m` quotient cuts, so the union bound is

`exp{ [log 2/(1-epsilon/8)] n/lambda^(2/3) - (omega0*epsilon/2)n/lambda^(1/3) } = o(1)`

by H3.

Thus, with probability `1-o(1)`, a percolation component contains at least

`W-(alpha-d1)n`

`= [rho-alpha+d1-o(1)]n`

vertices.

Therefore **every fixed coefficient strictly below**

`rho-alpha+d1 = rho-alpha+d0+delta_spec`

is proved uniformly on the unchanged frozen class.

For the immutable one-number metric, take the midpoint slack

`g_spec := rho-alpha+d0+delta_spec/2`.

Since the residual `o(1)` is eventually smaller than `delta_spec/2`,

`Pr[L1(G_p) >= g_spec n] = 1-o(1)`.

In particular

`Pr[L1(G_p) >= g_spec n]`

is bounded below by a positive frozen-parameter constant for all sufficiently large `n`, so this is valid movement of the fixed R16 metric.

The complete explicit definitions are

`q0 = 1-exp(-epsilon^2/288)`,

`alpha = rho*q0/64`,

`d0 = kappa*(rho-alpha)/(alpha-kappa)`,

`a0 = rho-alpha+d0`,

`c0 = 1-a0`,

`Xi0 = d0*c0/alpha` if `c0>=alpha`, while `Xi0=1-rho` if `c0<alpha`,

`L0 = d0*Xi0^2/(a0*c0)`,

`delta_spec = min{(alpha-d0)/2, c0/2, Xi0/2, L0/16}`,

and finally

`g_spec = rho-alpha+d0+delta_spec/2`.

Because `delta_spec>0`,

`g_spec > rho-alpha+d0`,

so this run strictly beats **the entire preceding asymptotic one-sided-padding envelope**, not merely its previous concrete receipt.

## 9. What each Section-B move actually did

### #3 — PROVE SOMETHING STRONGER

Instead of using H2 only to get one `kappa lambda n` witness across a padded pair, I proved the stronger density-amplified consequence

`e(A,C)/(lambda n) >= kappa ac/alpha^2`

whenever both sides are above the cutoff, plus its below-cutoff analogue. This was the new quantitative input.

### #11 — DUALIZE

I moved from raw edge counts to the 2-dimensional compression of `Adj(G)/lambda` on the indicator vectors of `A` and its complement. Positivity of `I-Q` turned external edge mass into an internal-density deficit

`q_A <= 1-x^2/(ac)`.

That deficit is exactly what the old padding inequality had thrown away.

### #25 — COUNT THE SAME THING TWICE

I averaged H2 twice: first over all `alpha`-subsets of `A` and its complement to lower-bound `x=e(A,C)/(lambda n)`, then over all ordered padding pairs `(X,D)` inside `A` to express the direct cut `e(A,B)` in terms of the internal density `q_A`. The two averages couple through the spectral compression and leave a positive `L0` at the old endpoint.

## 10. What this does and does not settle

This is a source-valid **PARTIAL** theorem for CMW Question 5.1 on the already frozen H1--H2--H3 class. It does not classify all natural hypotheses and therefore does not close the source question. No exact endpoint beyond `rho-alpha+d1` is claimed, and no global optimality is claimed for the new constant.

The next structural obstruction is now different from the previous one. The old obstruction was the crude bound `q_A<=1`; this run removes it. To move substantially further, the proof must exploit more than the 2-by-2 indicator compression—e.g. a three-block compression tracking `A`, the deficient seed side `B`, and the unused reservoir separately, or a genuinely multi-stage absorption scheme. Reoptimizing the old one-sided padding scalar alone is no longer the right target.

For the next invocation, nonconsecutive Section-B candidates are **#6 DEFORM TO A POINT YOU CAN SOLVE, #13 FIND WHAT ONLY INCREASES, #29 ADD THE POINTS AT INFINITY**. These are not claimed to be unused globally; all 30 have already appeared in the H0002 history.

## 11. Validation / bookkeeping (the final ~10%)

No finite checker was created because the new claim is analytic and has no finite computational core. The proof is written on the page; the standard 2-by-2 spectral compression is explicitly derived rather than cited as a novelty claim. I did not alter `RESULTS.md`, `QUEUE.md`, `POSTED.md`, any claim file, or any peer track. This report alone carries the structured delta.

The native model-control limitation remains unchanged. The exposed scheduler update surface provides title/prompt, schedule or relative start, timing mode, enablement and task identity, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. GPT-6/maximum is therefore still prompt-only here. Actually enforcing it requires scheduler/API fields that bind model and reasoning plus per-run runtime attestation. The historical P26 `You cannot modify this task` denial was authorization-context-specific; repository evidence records a later successful P26 update from an authorized context. For any task that still refuses modification, the compliant route is its owning authorized workspace/account context or platform support, never duplication or permission bypass. No scheduler modification was attempted in this run.

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
    strongest_proved_envelope: "every fixed g < rho-alpha+d0"
    d0: "kappa*(rho-alpha)/(alpha-kappa)"
  after:
    concrete: "g_spec = rho-alpha+d0+delta_spec/2"
    stronger_envelope: "every fixed g < rho-alpha+d0+delta_spec"
    delta_spec: "min{(alpha-d0)/2, c0/2, Xi0/2, L0/16} > 0"
  movement: true
  supported_unchanged_count: 0
  methods: [11, 3, 25]
  stuck_recovery: false
  nominal_beck_fiala_status: "KNOWN current-literature baseline on stated 2026 Komlos preprints; not re-opened"
  finite_checker: "not applicable; analytic proof"
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
```
