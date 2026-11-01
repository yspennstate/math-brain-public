Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the unchanged frozen H0002 class, this run proves a concrete constant strictly larger than the *entire* preceding absorption envelope `g_abs_sup`; more strongly, it gives a root-continuation envelope `g_cont_sup > g_abs_sup`. Section-B methods actually used: **#5 ADD A PARAMETER AND DIFFERENTIATE, #14 FIND THE GROUP ACTING, #20 FIND WHY THE ALGORITHM FAILS**. All 30 methods had already appeared on H0002, so these are honest nonconsecutive reuses.

# R16 — H0002: positive-profile continuation, complement symmetrization, and a strict gain beyond the absorption envelope

## 1. Continuity, ownership, required reads, and current-source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural graph hypotheses under which, for `p >= (1+epsilon)/lambda(G)`, bond percolation contains a component of order `Omega(|G|)` with constant probability.

I re-read/reconciled the required repository state before research: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, the controlling `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H-intake verification / `problems.jsonl`, the newest own report `runs/R16/2026-09-19T00-43-10Z_h0002-fixed-reserve-absorption_a4d7.md`, and the newest recoverable neighboring same-source G0011 terminal handoff. G0011 concerns the distinct long-cycle conjecture from the same CMW paper and does not alter H0002 ownership.

Fresh current-source checks in this invocation still recover CMW as arXiv:2608.19145v1, dated 19 Aug 2026. A bounded current title/author/question search did not locate a later source-matching resolution of Question 5.1. This is negative evidence only, not a worldwide openness or novelty certificate.

The nominal Beck--Fiala title remains stale as an unresolved assignment. Bansal--Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` scale directly for `t >= log^2 n` and give weaker polylogarithmic-loss bounds below that range. But Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`, with no `n` restriction. Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlos proof with constant `36` and explicitly describe it as a simplification of the Guo--Fang--Lu proof. These are extremely recent manuscripts, not mature refereed consensus; on their stated theorems the original square-root Beck--Fiala target is nevertheless a current-literature **KNOWN** baseline. R16 therefore continues its already-admitted H0002 successor rather than reopening the obsolete `t<log^2 n` gap.

Current links checked:

- CMW source: https://arxiv.org/abs/2608.19145
- Bansal--Jiang: https://arxiv.org/abs/2508.03961
- Guo--Fang--Lu: https://arxiv.org/abs/2609.11189
- Karingula--Lovett: https://eccc.weizmann.ac.il/report/2026/188/

## 2. Frozen class and incoming quantitative state

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n := |G|`, `lambda := lambda(G)`,

`h := 1-epsilon/8`,

`q0 := 1-exp(-epsilon^2/288)`,

`alpha := rho*q0/64`.

The H0002 class is unchanged:

1. **H1:** `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. **H2:** `e_G(X,Y) >= kappa lambda n` for every disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. **H3:** `lambda -> infinity`.

The fixed metric remains `g_twoaxis(epsilon,rho,kappa)`, the largest explicit uniform giant fraction proved for this exact class at every `p >= (1+epsilon)/lambda`.

The preceding spectral-padding and fixed-reserve-absorption reports established the following host-geometry quantities. Nonvacuity gives

`0<rho<1`, `0<kappa<=alpha^2<alpha`.

Set

`d0 := kappa*(rho-alpha)/(alpha-kappa)`,

`a0 := rho-alpha+d0`, `c0 := 1-a0`,

`Xi0 := d0*c0/alpha` if `c0>=alpha`, and `Xi0 := 1-rho` if `c0<alpha`,

`L0 := d0*Xi0^2/(a0*c0)`,

`delta_spec := min{(alpha-d0)/2, c0/2, Xi0/2, L0/16}`,

`d1 := d0+delta_spec`.

For `0<=d<alpha`, define

`a(d):=rho-alpha+d`, `c(d):=1-a(d)`,

and

`Xi(d) := kappa*a(d)*c(d)/alpha^2` if `c(d)>=alpha`,

`Xi(d) := a(d)*kappa/alpha-(alpha-c(d))` if `c(d)<alpha`.

On the interval where `Xi(d)>0`, the two-by-two spectral-compression padding argument gives the pair-capacity profile

`F(d) := a(d)*kappa/alpha - d + d*Xi(d)^2/[a(d)c(d)]`.

The preceding report proved `F(d)>0` for all `0<=d<=d1`. Put

`beta := alpha-d1 > 0`,

`g1 := rho-alpha+d1 = rho-beta`,

`a1 := g1`, `c1 := 1-g1 = 1-rho+beta`,

`Xi1 := Xi(d1) > 0`,

`F1 := F(d1) > 0`.

It then reserved a fixed amount of percolation probability for absorption. The maximal reserve numerator compatible with H1-supercriticality is

`Delta := 1+epsilon-1/h = epsilon(7-epsilon)/(8-epsilon) > 0`.

With

`R1 := 1-exp[-Delta*F1/beta]`,

the incoming strongest asymptotic envelope is

`g_abs_sup := g1 + (1-rho) R1`.

Every fixed `g<g_abs_sup` is already proved. The endpoint itself is not claimed.

The goal of this run is to move **strictly above that entire envelope**, not merely above the previous concrete slack receipt.

## 3. Method #5 — continue the positive pair-capacity profile past the artificial checkpoint `d1`

The key observation is that `d1` was chosen by a deliberately coarse continuity estimate; it was never a zero of `F`. In fact the incoming report explicitly has

`F(d1)=F1>0`, `Xi(d1)=Xi1>0`.

So the pair-capacity theorem must persist on a nontrivial interval to the right of `d1`. To make this quantitative rather than merely topological, differentiate the profile.

### 3.1 Uniform derivative bounds

On either smooth branch of `Xi`,

`|Xi'(d)|<=1`.

Also `0<Xi(d)<=1` wherever the spectral lower bound is used. For `d>=d1`, `a(d)>=a1`. Restrict temporarily to

`0<=d-d1<=min{beta/2,c1/2,Xi1/2}`.

Then

`d<alpha`, `c(d)>=c1/2`, `Xi(d)>=Xi1/2>0`,

and hence

`a(d)c(d) >= a1*c1/2`.

Write

`R(d):=Xi(d)^2/[a(d)c(d)]`.

On either branch,

`R'(d)=2 Xi Xi'/(ac) - Xi^2 (ac)'/(ac)^2`,

with `|(ac)'|=|c-a|<=1`. Therefore

`|R(d)| <= 2/(a1*c1)`,

and

`|R'(d)| <= 4/(a1*c1) + 4/(a1^2*c1^2)`.

Since

`F'(d)=kappa/alpha-1+R(d)+d R'(d)`

and `d<alpha`, every smooth branch satisfies

`|F'(d)| <= M1`,

where

`M1 := 1 + 2/(a1*c1)
          + alpha*[4/(a1*c1)+4/(a1^2*c1^2)]`.

The two formulas for `Xi` agree at the branch point `c=alpha`, so `F` is continuous there; the branchwise derivative bound implies the same global `M1`-Lipschitz estimate across a possible branch crossing.

### 3.2 An explicit extension radius

Define

`delta_cont := min{
    beta/2,
    c1/2,
    Xi1/2,
    (1-rho)/2,
    F1/(2 M1)
}`.

Every term is strictly positive, hence

`delta_cont>0`.

Put

`d2 := d1+delta_cont`,

`beta2 := alpha-d2 = beta-delta_cont > 0`,

`g2 := rho-alpha+d2 = g1+delta_cont`.

For every `d in [d1,d2]`, the Lipschitz estimate gives

`F(d) >= F1-M1(d-d1) >= F1/2 >0`,

and the `Xi1/2` restriction gives `Xi(d)>0`. Therefore the exact same density-averaging plus spectral-compression proof used in the incoming report remains valid throughout `[d1,d2]`.

Combining with the old positivity on `[0,d1]`, there is a fixed

`omega2 := min{ min_{0<=d<=d1} F(d), F1/2 } > 0`

such that, up to the already-controlled `o(1)` perturbation caused by integer rounding and seed mass `rho n-o(n)`, every genuine seed-quotient cut whose smaller side has at least

`beta2 n = (alpha-d2)n`

has `Theta(lambda n)` host crossing edges.

This is already a strict deterministic enlargement of the cut range on the **same H1--H2--H3 class**.

### 3.3 The stronger root-continuation parameter

The explicit `delta_cont` is conservative. The same argument identifies the natural maximal continuation point

`d_plus := sup{ d in [d1,alpha):
                Xi(s)>0 and F(s)>0 for every s in [d1,d] }`.

Continuity and `Xi1,F1>0` imply

`d_plus>d1`.

For every fixed `d<d_plus`, compactness gives a positive minimum of the pair-capacity profile on `[0,d]`, so the sprinkling proof applies with smaller-side threshold `(alpha-d)n`.

Thus `d_plus` is not asserted to be an attained endpoint; it is the exact continuation radius of this already-derived scalar host profile.

## 4. Round-one harvesting and round-two gluing now produce a strict seed head start

Use the same three-round decomposition as the incoming absorption report. For any fixed `0<sigma<Delta`, let

`p1=(1+epsilon-sigma)/lambda`,

`pg=lambda^(-4/3)`,

`pa=sigma/lambda-lambda^(-4/3)`.

The union is stochastically dominated by target percolation at `(1+epsilon)/lambda`.

H1 gives the fixed residual supercriticality

`p1 lambda(H) >= h(1+epsilon-sigma)>1`

throughout all adaptive deletions of at most `rho n` vertices. The already-proved root-corrected Perron exploration plus two-scale jackpot harvesting therefore still gives a family of **genuine connected** first-round seed components of total mass

`W >= (rho-o(1))n`

with probability `1-o(1)`; every seed has more than `h lambda^(2/3)` vertices. Hence the genuine seed-component quotient has only `O(n/lambda^(2/3))` vertices.

Round `pg` misses a fixed quotient cut with pair capacity at least `omega2 lambda n/2` with probability

`exp[-Theta(n/lambda^(1/3))]`,

whereas the quotient has only

`exp[O(n/lambda^(2/3))]`

cuts. The union bound therefore tends to zero.

Consequently round two now yields a connected seed component `A0` with

`|A0| >= (g2-o(1))n = (g1+delta_cont-o(1))n`

with probability `1-o(1)`.

More generally, for every fixed `d<d_plus`, it yields

`|A0| >= [rho-alpha+d-o(1)]n`.

This is the first strict improvement in the run: the incoming absorption theorem had only a pre-absorption guarantee `g1-o(1)`.

## 5. Method #14 — symmetrize the complement when H2 can see two disjoint blocks inside it

The two-by-two compression used in the preceding report treated the complement-side internal density merely as `q_C>=0`. There is a genuine symmetry gain when the complement is itself large enough to contain two H2-sized blocks.

Assume in this subsection that

`c1 >= 2 alpha`.

Let `C=V\A` with `|A|=a1 n+o(n)`, `|C|=c1 n+o(n)`. Choose uniformly two disjoint subsets `X,Y subset C`, each of size `alpha n+o(n)`. H2 applies to every such pair. Averaging over the action of the permutation group of `C` gives

`E e(X,Y) = [2 alpha^2/c1^2+o(1)] e(C)`.

Since every realization has at least `kappa lambda n` crossing edges,

`2e(C)/(lambda c1 n) >= kappa*c1/alpha^2-o(1)`.

Write this normalized internal density as `q_C`. To retain fixed slack and avoid any endpoint issue, set

`mu1 := kappa*c1/(2 alpha^2)`.

Because `kappa<=alpha^2` and `c1<1`, we have `0<mu1<1/2`, and eventually

`q_C >= mu1`.

At the same time the density-amplified H2 argument gives

`x:=e(A,C)/(lambda n) >= Xi1-o(1)`.

Compress `Adj(G)/lambda` to the span of the normalized indicators of `A,C`:

`Q=[[q_A,y],[y,q_C]]`, `y=x/sqrt(a1*c1)`.

As before `I-Q` is positive semidefinite, hence

`(1-q_A)(1-q_C) >= y^2`.

Using now `q_C>=mu1` rather than only `q_C>=0` yields

`q_A <= 1 - x^2/[a1*c1*(1-mu1)]`.

Feeding this into the one-sided padding average at deficit `d1` gives the improved endpoint pair capacity

`F1_sym := a1*kappa/alpha-d1
          + d1*Xi1^2/[a1*c1*(1-mu1)]`.

Since `d1>0`, `Xi1>0` and `mu1>0`,

`F1_sym > F1`.

For a uniform formula valid in both complement regimes, define

`Fhat1 := F1_sym` if `c1>=2 alpha`,

`Fhat1 := F1` if `c1<2 alpha`.

Then always

`Fhat1>=F1>0`,

with a strict inequality in the symmetric-complement regime.

This move is genuinely different from continuing `F(d)`: it extracts previously unused **internal** edge information from the complement by averaging H2 over its own disjoint alpha-blocks. It gives an additional improvement whenever the frozen parameters place the old endpoint complement above `2 alpha`.

## 6. Reuse the old anchor, but exploit the new seed head start

The important point is that the better round-two giant can be combined with the **old** anchor geometry. We do not need the new pair profile itself to improve the absorption exponent.

Freeze an anchor `A subset A0` of density `a1=g1`. This is possible because round two now gives `|A0|/n>=g1+delta_cont-o(1)`.

At the old anchor threshold `beta=alpha-d1`, the pair-capacity estimate gives, for every fixed `c<Fhat1` and all sufficiently large `n`,

`e(A,B) >= c lambda n`

for every disjoint `B` of size `beta n+o(n)`.

Therefore all but fewer than `beta n+o(n)` vertices outside `A` have

`d_A(v) >= c lambda/beta`.

Equivalently at least

`(1-a1-beta-o(1))n = (1-rho-o(1))n`

vertices outside the anchor have `Theta(lambda)` possible attachment edges into it.

Let

`y:=|A0\A|/n`.

The new seed head start gives

`y >= delta_cont-o(1)`.

At most `yn` of the high-degree reservoir vertices are already inside `A0\A`, so at least

`(1-rho-y-o(1))_+ n`

high-degree vertices remain outside the connected component.

In round `pa`, each such vertex attaches directly to `A` with asymptotic probability at least

`1-exp[-sigma*c/beta]`.

The events for distinct outside vertices use disjoint edge sets into the frozen anchor, hence are independent. Chernoff concentration gives final connected mass

`a1+y+r(1-rho-y)_+ - o(1)`,

for every fixed

`r < 1-exp[-sigma*c/beta]`.

As in the preceding report, this expression is increasing in `y`: on `y<=1-rho` its derivative is `1-r>0`, and for `y>=1-rho` the component is already larger.

Therefore the worst case is the **smallest** allowed head start.

## 7. New envelope: strict movement beyond the entire preceding absorption envelope

First use the explicit continuation amount `delta_cont`. Since `delta_cont<1-rho`, Sections 4--6 imply, after sending fixed slack parameters toward their admissible boundaries,

`every fixed g < g_exp_sup`

is proved, where

`Rhat := 1-exp[-Delta*Fhat1/beta]`,

`g_exp_sup := g1 + delta_cont
              + Rhat*(1-rho-delta_cont)`.

Equivalently,

`g_exp_sup = g1 + Rhat*(1-rho)
             + delta_cont*(1-Rhat)`.

The incoming envelope was

`g_abs_sup = g1 + R1*(1-rho)`,

where

`R1 = 1-exp[-Delta*F1/beta]`.

Since `Fhat1>=F1`, we have `Rhat>=R1`; and because `delta_cont>0` and `Rhat<1`,

`g_exp_sup-g_abs_sup
 = (1-rho)(Rhat-R1)
   + delta_cont*(1-Rhat)
 >0`.

Thus this run strictly beats the **entire preceding asymptotic envelope**, even in the regime `c1<2alpha` where Method #14 supplies no extra factor. The universal source of strictness is the positive continuation head start from Method #5.

### Explicit fixed receipt strictly above the old supremum

For a single frozen metric value that is completely explicit and does not use the conditional symmetry gain, note that

`1-R1 = exp[-Delta*F1/beta] >0`.

Define

`g_cont := g_abs_sup
          + (delta_cont/2)*exp[-Delta*F1/beta]`.

The no-symmetry continuation envelope already equals

`g_abs_sup + delta_cont*exp[-Delta*F1/beta]`.

Hence `g_cont` lies a fixed positive distance below the new proved envelope and a fixed positive distance **above** the old one. Therefore

`P(L1(G_p) >= g_cont n) -> 1`

uniformly on the unchanged H1--H2--H3 class.

This is the immutable fixed-metric movement for the run.

### Stronger root-continuation envelope

The explicit `delta_cont` only certifies a short interval. Let

`delta_plus := min{ d_plus-d1, 1-rho } >0`.

For every fixed `0<delta<delta_plus`, choose `d=d1+delta<d_plus`. The round-two seed giant has normalized size at least `g1+delta-o(1)`, while the old anchor still has density `g1`. Repeating Section 6 gives every fixed constant below

`g1 + delta + Rhat*(1-rho-delta)`.

This expression is increasing in `delta`, with derivative `1-Rhat>0`. Taking fixed `delta` arbitrarily close to `delta_plus` proves every fixed

`g < g_cont_sup`,

where

`g_cont_sup := g1 + Rhat*(1-rho)
              + delta_plus*(1-Rhat)`.

Again endpoint attainment is not claimed. The strict comparison is

`g_cont_sup-g_abs_sup
 = (1-rho)(Rhat-R1)
   + delta_plus*(1-Rhat)
 >0`.

Also `g_cont_sup<1`: since `delta_plus<=1-rho`,

`g_cont_sup <= g1+1-rho = 1-beta <1`.

So the bound is nonvacuous and dimensionally consistent.

## 8. Method #20 — why the obvious multi-round cascade does **not** by itself beat the old envelope

I also tested the most obvious proposed next route from the preceding report: split the absorption reserve into many stages and let newly attached vertices be absorbed successively.

If the only information carried from one stage to the next is the **same fixed anchor-degree lower bound**

`D lambda`, `D:=F1/beta`,

then staging is exactly neutral. Suppose a total absorption numerator `sigma` is split as

`sigma=sigma_1+...+sigma_m`.

For a reservoir vertex with `D lambda+o(lambda)` independent candidate edges, the asymptotic probability of surviving stage `j` unattached is `exp(-D sigma_j)`. Surviving every stage therefore has probability

`prod_j exp(-D sigma_j)
 = exp[-D*sum_j sigma_j]
 = exp(-D sigma)`.

Equivalently the total attachment probability is exactly

`1-exp(-D sigma)`,

the same exponent as one-shot sprinkling.

So a bare cascade that merely repartitions the same reserve and the same degree quantile cannot move the metric. A successful cascade must refresh the deterministic host information after growth: it needs `D(a)` to improve with the current anchor, a new reservoir quantile, or genuinely new cross-block information.

This failure diagnosis is useful because it prevents the next runs from mistaking more sprinkling stages for research progress. The two successful moves in this run do provide new host information: Method #5 extends the range of positive pair capacity, and Method #14 sometimes strengthens the endpoint capacity itself.

## 9. What each Section-B move actually did

### #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

I treated the old checkpoint `d1` as an interior point of the scalar pair-capacity profile rather than a final endpoint. Differentiating the explicit `F(d)` and bounding its derivative produced the positive extension radius `delta_cont`; the maximal version is the root-continuation parameter `d_plus`. This gave a larger pre-absorption connected seed component on exactly the same graph class.

### #14 — FIND THE GROUP ACTING

Inside a complement of density at least `2alpha`, averaging H2 over the permutation action on ordered pairs of disjoint `alpha`-subsets gives a positive lower bound on the complement's own internal normalized density `q_C`. Feeding that into the same 2-by-2 compression replaces the denominator `1` by `1-mu1` and strictly improves `F1` to `F1_sym` in that regime.

### #20 — FIND WHY THE ALGORITHM FAILS

I analyzed the tempting repeated-absorption cascade. Without a refreshed host-degree lower bound, the no-attachment exponents multiply and collapse to `exp(-D sigma)`; splitting the same reserve into arbitrarily many stages is exactly equivalent to one shot. This identifies the missing ingredient rather than generating a fake cascade lemma.

## 10. Prior art and novelty scope

The proof uses standard ingredients—averaging over subsets, quotient/spectral compression, sprinkling, Chernoff concentration, and monotonicity. None of those general mechanisms is claimed novel. The bounded current search did not locate the exact H1/H2 quantitative profile-continuation theorem or the complement-internal correction above, but a negative search is not a novelty certificate.

The source-level status remains **PARTIAL**. CMW Question 5.1 asks for natural conditions in general; this run proves a stronger quantitative theorem only on R16's already frozen H1--H2--H3 sufficient-condition class.

## 11. Status, obstruction, and next route

H0002 remains **PARTIAL / SOURCE OPEN-LOOKING IN BOUNDED CURRENT SEARCH / ACTIVE**.

The fixed metric moved, so the supported unchanged count remains/reset to **0** and no Section-I stuck recovery is triggered.

The present scalar continuation route has a sharply defined next obstruction: the first point where either `Xi(d)` or `F(d)` reaches zero. The next useful run should **not** spend its time deriving another arbitrary positive continuity radius. It should instead do one of the following genuinely different things:

1. analyze the first root of the explicit piecewise-rational `F(d)` exactly and determine whether H2 forces it all the way to `d=alpha`;
2. upgrade the 2-by-2 compression to the 3-block span of the large seed side, deficient side, and unused reservoir, so the missing cross terms are constrained simultaneously;
3. use the complement-internal averaging recursively to obtain a distributional degree statement rather than a single quantile.

A nonconsecutive next triple is **#7 TAKE THE LIMIT, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT**. These are reuses; all 30 methods were already exhausted historically on H0002.

## 12. Validation / bookkeeping (final approximately 10%)

No finite checker was created. The new claims are analytic and their proofs are on the page; there is no finite-enumeration core to certify. I did not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, any claim file, scheduler, peer track, email, Drive item, workflow, permission, or public posting. This immutable report alone carries the delta.

The model-control limitation is unchanged. The exposed scheduler interface provides task identity, title/prompt, schedule/start offset, timing mode and enablement, but **no binding model-family selector, no reasoning-effort selector, and no authenticated per-run model receipt**. GPT-6/maximum is therefore prompt-only here. Actually enforcing it requires scheduler/API support for those fields plus runtime attestation. The historical P26 `You cannot modify this task` failure was authorization-context-specific; the repository records a later successful P26 update from an authorized context. For any task that still refuses modification, the compliant workaround is the owning authorized workspace/account context or platform support, never duplication or permission bypass.

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
    strongest_proved_envelope: "every fixed g < g_abs_sup = g1 + (1-rho)*(1-exp(-Delta*F1/beta))"
  after:
    explicit_continuation_radius: "delta_cont = min{beta/2,c1/2,Xi1/2,(1-rho)/2,F1/(2*M1)} > 0"
    concrete: "g_cont = g_abs_sup + (delta_cont/2)*exp(-Delta*F1/beta)"
    stronger_envelope: "every fixed g < g_cont_sup = g1 + Rhat*(1-rho) + delta_plus*(1-Rhat)"
    root_parameter: "d_plus = sup{d>=d1: Xi,F stay positive on [d1,d]}, delta_plus=min{d_plus-d1,1-rho}>0"
    complement_refinement: "if c1>=2alpha, Fhat1=F1_sym>F1; otherwise Fhat1=F1"
  movement: true
  supported_unchanged_count: 0
  methods: [5, 14, 20]
  stuck_recovery: false
  nominal_beck_fiala_status: "KNOWN current-literature baseline on stated Sep-2026 Komlos manuscripts; not reopened"
  finite_checker: "not applicable; analytic proof"
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
```