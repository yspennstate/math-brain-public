Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala `B(t,n)` metric remains a KNOWN current-literature baseline on the stated September 2026 Komlos preprints, while the active R16/H0002 successor moves strictly from the complete envelope `G_H=a1+Phi(d_H-d1)` to `G_core=a1+Phi(d_core-d1)>G_H` on the unchanged H1--H2--H3 class. Section-B methods actually used: **#5 ADD A PARAMETER AND DIFFERENTIATE, #15 BREAK THE SYMMETRY ON PURPOSE, #20 FIND WHY THE ALGORITHM FAILS**. All 30 Section-B moves were already exhausted on H0002, so these are honest nonconsecutive reuses; the preceding triple was #7/#11/#24.

# R16 — H0002: remove the artificial half-slack in the H1 complement core

## 1. Continuity, ownership, required reads, and current-source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source is Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural graph hypotheses under which `p >= (1+epsilon)/lambda(G)` forces a component of order `Omega(|G|)` with constant probability.

Before doing new mathematics I reconciled the current repository state rather than restarting: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H0002 intake record under `probability_1000_intake_H_20260914/problems.jsonl`, the newest R16 report `runs/R16/2026-09-19T02-45-09Z_h0002-h1-complement-core-extension_f3a8.md`, and the newest recoverable report of the former same-source neighbor R7-07. R7-07 has already rotated away from the CMW source, so no current peer ownership conflict was found. H0002 remains R16-exclusive.

A fresh bounded web check still recovered CMW as arXiv:2608.19145v1 dated 19 Aug 2026 and did not surface a later source-matching resolution of Question 5.1. This is negative search evidence only, not a worldwide openness or novelty certificate.

The nominal Beck--Fiala scheduler title remains stale as an unresolved existence target. The exact current comparison is:

- Bansal--Jiang, arXiv:2508.03961v2, directly obtain the conjectured `O(sqrt(t))` order for `t >= log^2 n`, and weaker polylogarithmic loss below that range.
- Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce

  `B(t,n) < 3 sqrt(2 pi t)`

  for every integer `t>=1` and every `n`, with no logarithmic restriction.
- Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlos proof with universal constant `36`.

These are extremely recent manuscripts, not mature refereed consensus. On their stated theorems, however, the fixed Beck--Fiala existence metric is already uniformly bounded by `3 sqrt(2 pi t)` for all `t,n`; R16 does not relabel this literature theorem as a new fleet result and continues the already-admitted H0002 successor.

Current source links checked:

- https://arxiv.org/abs/2608.19145
- https://arxiv.org/abs/2508.03961
- https://arxiv.org/abs/2609.11189
- https://eccc.weizmann.ac.il/report/2026/188/

## 2. Frozen H0002 class and incoming strongest bound

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n=|G|`, `lambda=lambda(G)`,

`h:=1-epsilon/8`,

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`.

The hypothesis class is unchanged:

1. H1: `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. H2: `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. H3: `lambda -> infinity`.

The tracked quantity is still `g_twoaxis(epsilon,rho,kappa)`, the largest explicit uniform giant fraction proved for this exact class at every `p >= (1+epsilon)/lambda`.

For a nonvacuous H1 sequence we necessarily have `rho<1`: if `rho>=1`, then `S=V(G)` is admissible and H1 would require `0=lambda(empty) >= h lambda>0`. Thus throughout the nonvacuous case

`s:=1-rho>0`.

Preserve the preceding notation

`a(d):=rho-alpha+d`,

`b(d):=alpha-d`,

`c(d):=1-a(d)=s+b(d)`,

and

`Xi(d):=kappa*a(d)*c(d)/alpha^2` if `c(d)>=alpha`,

`Xi(d):=a(d)*kappa/alpha-(alpha-c(d))` if `c(d)<alpha`.

The previous report used the fixed-slack complement parameter

`mu_H(d)=h*b(d)/(2*c(d))`

and the profile

`F_H(d)=a(d)*kappa/alpha-d
        +d*Xi(d)^2/[a(d)c(d)(1-mu_H(d))]`.

It defined the first positive-profile endpoint `d_H`, proved `d_H>d_plus`, and obtained the complete envelope

`G_H:=a1+Phi(d_H-d1)`.

Here `d1`, `a1`, and the strictly increasing function `Phi` are exactly those frozen in the preceding report:

`beta:=alpha-d1`, `a1:=rho-beta`,

`Rhat:=1-exp[-Delta*Fhat1/beta] in (0,1)`,

`Delta:=epsilon*(7-epsilon)/(8-epsilon)`,

`Phi(D):=Rhat*s+D*(1-Rhat)` for `0<=D<=s`,

`Phi(D):=D` for `D>=s`.

Every fixed `g<G_H` was already proved with probability tending to one. This is the strongest complete incoming bound I compare against.

## 3. Method #5 — keep the complement-core slack as a parameter

The preceding complement-core lemma actually proved more than the fixed choice `mu_H=hb/(2c)` that was fed into the spectral compression. For a large side `A` of density `a=rho-b` and complement `C` of density `c=s+b`, it proved

`q_C:=2e(C)/(lambda*c*n) >= h*b/c-o(1)`.

For completeness, here is the argument in the form needed below. Let

`T={v in C: deg_C(v)>=h lambda}`.

If `|T| <= (b-o(1))n`, then `|A union T|<=rho n` for all sufficiently large `n`, so H1 gives

`lambda(C-T)>=h lambda`.

But every vertex of `C-T` has degree in `C`, hence also in `C-T`, strictly below `h lambda`. Therefore

`lambda(C-T)<=Delta(C-T)<h lambda`,

a contradiction. Hence `|T|>=(b-o(1))n`, and summing degrees inside `C` gives

`2e(C)>=h*b*lambda*n-o(lambda n)`.

Divide by `lambda*c*n`.

Introduce a slack parameter `theta in (0,1]` and put

`m(d):=h*b(d)/c(d)`,

`F_theta(d):=a(d)*kappa/alpha-d
 + d*Xi(d)^2/[a(d)c(d)(1-theta*m(d))]`.

For every fixed `theta<1`, the preceding proof applies literally for all sufficiently large `n`. More importantly, because the actual bound is `q_C>=m(d)-o(1)`, the limiting `theta=1` profile is itself valid asymptotically on every compact interval on which it has a positive margin.

The dependence on `theta` is strictly monotone whenever `d>0` and `Xi(d)>0`:

`partial_theta F_theta(d)
 = d*Xi(d)^2*m(d)
   /[a(d)c(d)(1-theta*m(d))^2]
 >0`.

The preceding report used `theta=1/2`. There is no mathematical reason to freeze that artificial half-slack in an asymptotic theorem.

Define the **full complement-core profile**

`F_core(d):=F_1(d)`

so that, using `c=s+b`,

`boxed: F_core(d)
 = a(d)*kappa/alpha-d
   +d*Xi(d)^2/[a(d)*(c(d)-h*b(d))].`

The denominator is always positive in the nonvacuous regime because

`c-hb=s+(1-h)b=s+(epsilon/8)b>0`.

### Uniformity on a fixed compact range

The passage from `q_C>=m-o(1)` to `F_core` does not interchange an uncontrolled limit with the cut union bound. Fix any `d_*<alpha` for which `Xi(u)>0` and `F_core(u)>0` on `[d1,d_*]`. By continuity on this compact interval,

`min Xi(u)>0`, `min F_core(u)>0`.

The rounding/harvesting errors in the complement-core and padding calculations are uniform `o(1)` errors in normalized edge counts. Equivalently, choose one `theta<1` sufficiently close to one that `F_theta` still has a positive minimum on `[d1,d_*]`; then take `n` large enough for the complement-core lower bound to dominate `theta*m(u)` uniformly. Thus every cut in the quotient range receives a fixed positive `Theta(lambda n)` crossing lower bound. No endpoint attainment is used.

## 4. The previous `d_H` endpoint is an interior zero with `Xi(d_H)>0`

To prove strict metric movement rather than a pointwise profile improvement, I need the structure of the old `theta=1/2` endpoint.

First, H2 itself forces

`kappa<=alpha^2`.

Indeed, average H2 over uniformly random disjoint `alpha n`-subsets `X,Y` of `V`. Since `2e(G)<=lambda n`,

`E e(X,Y) <= (alpha^2+o(1))*lambda*n`,

whereas every such pair has at least `kappa lambda n` edges.

Put `x:=kappa/alpha^2 in (0,1]`. As `d->alpha-`, we have `b->0`, `a->rho`, `c->s`, and the old complement correction `mu_H(d)->0`, so `F_H` has the same boundary limit as the pre-core profile.

If `s>=alpha`, then the first branch of `Xi` applies and

`F_H(alpha-)/alpha
 = x*rho-1+x^2*rho*s
 <= rho-1+rho*s
 = -s^2<0`.

If `0<s<alpha`, either `Xi` vanishes before the boundary, or on the second branch set

`r:=s/alpha`, `y:=1-x*rho`.

Then `y>=s=alpha*r`. If `Xi(alpha-)>0`, then `Xi(alpha-)=alpha(r-y)>0`, hence `r>y`, and

`F_H(alpha-)/alpha
 = -y+alpha*(r-y)^2/(rho*r)`.

Because `y>=alpha*r`,

`0<r-y<=r(1-alpha)`.

Also `rho=1-s>1-alpha>(1-alpha)^2`, so

`alpha*(r-y)^2/(rho*r)
 < alpha*r*(1-alpha)^2/rho
 < alpha*r
 <= y`.

Thus again `F_H(alpha-)<0`. Therefore

`d_H<alpha`.

The endpoint cannot be caused by `Xi` reaching zero. On the first branch `Xi>0` automatically. On the second branch, `Xi(d)=0` implies

`a(d)*kappa/alpha=alpha-c(d)=d-s`,

so at such a point

`F_H(d)=a*kappa/alpha-d=-s<0`.

Since `F_H` is positive before its first endpoint, it crosses zero strictly before any `Xi`-zero. Consequently

`boxed: d_H<alpha, Xi(d_H)>0, F_H(d_H)=0.`

## 5. The full core profile crosses the old root

At `d=d_H`, write `a_H=a(d_H)`, `b_H=b(d_H)`, `c_H=c(d_H)`, `Xi_H=Xi(d_H)`. Then `d_H>0`, `b_H>0`, and `Xi_H>0`. The new and old profiles differ by

`F_core(d_H)-F_H(d_H)
 = d_H*Xi_H^2/a_H
   *[1/(c_H-h*b_H)-1/(c_H-h*b_H/2)]`

`= d_H*Xi_H^2/a_H
   * (h*b_H/2)
   /[(c_H-h*b_H)*(c_H-h*b_H/2)]`

`>0`.

Since `F_H(d_H)=0`,

`boxed: F_core(d_H)>0.`

Define the new first positive-profile endpoint directly from the full profile:

`d_core:=sup{d in [d1,alpha):
  Xi(u)>0 and F_core(u)>0 for every u in [d1,d]}`.

The old profile is positive up to `d_H`, and `F_core>=F_H` there; the strict inequality at `d_H` plus continuity gives

`boxed: d_core>d_H.`

The new endpoint is still interior. As `d->alpha-`, `m(d)->0`, hence `F_core(alpha-)` has exactly the same negative boundary limit computed above. Also an `Xi`-zero on the second branch again gives `F_core=-s<0`. Thus

`d_core<alpha`,

and the endpoint is the first zero of an explicit piecewise-rational function rather than a boundary artifact. After clearing the positive denominator `a(c-hb)`, each branch is a bounded-degree polynomial equation in `d`.

This is the run's theorem-sized new result.

## 6. Propagation to the full giant-fraction metric

Fix any `d<d_core`. By the compact-margin argument in section 3, every relevant macroscopic quotient cut up to deficiency `d` has a fixed crossing capacity

`e(A,B)>=c_d*lambda*n`

for some `c_d>0` depending only on the frozen parameters and `d`.

The already-proved two-scale harvesting theorem produces genuine first-round seed components of total mass `(rho-o(1))n`; their quotient has only `O(n/lambda^(2/3))` vertices. The independent gluing round uses `p_g=lambda^(-4/3)`. For each relevant cut its survival probability is at most

`exp[-Theta(n/lambda^(1/3))]`,

while the number of quotient cuts is only

`exp[O(n/lambda^(2/3))]`.

Therefore the union bound tends to zero and round two produces a connected seed component of normalized size at least

`rho-alpha+d-o(1)`.

The old absorption argument at the fixed anchor `a1` is unchanged. Put

`D_core:=d_core-d1`.

Using exactly the same strongest-complete combination of seed-only and fixed-anchor absorption as the preceding report gives

`boxed: G_core:=a1+Phi(D_core).`

The incoming strongest complete envelope was

`G_H=a1+Phi(d_H-d1)`.

Because `s>0`, `Rhat in (0,1)`, and hence `Phi` is strictly increasing. Since `d_core>d_H`,

`boxed: G_core>G_H.`

Consequently every fixed

`g<G_core`

satisfies

`boxed: P(L1(G_p)>=g*n)->1`

uniformly on the unchanged H1--H2--H3 class for every `p>=(1+epsilon)/lambda(G)`.

No endpoint attainment is claimed.

For a single frozen receipt strictly above the entire previous envelope, define

`g_receipt:=(G_H+G_core)/2`.

Then

`G_H<g_receipt<G_core`,

so the metric moves strictly and the supported unchanged count remains zero.

## 7. Method #15 — break the padding symmetry by using the untouched reservoir

I also tested a genuinely different way of padding a deficient quotient side. Write the harvested seed partition as `A union B`, with densities

`a=rho-b`, `b=alpha-d`,

and let the untouched reservoir be `R` of density `s=1-rho`.

When `d<s`, instead of padding `B` with `d n` vertices taken from `A`, pad it with `d n` vertices taken from `R`. Average H2 simultaneously over an `alpha n`-subset of `A` and a `d n`-subset of `R`. If

`x=e(A,B)/(lambda n)`, `z=e(A,R)/(lambda n)`,

then the exact asymptotic inequality is

`x+(d/s)z >= a*kappa/alpha-o(1)`.

This is structurally different from the old contamination term `d q_A`.

There is a useful scalar upper bound on the total cross mass `T=x+z`. Since `a>2alpha`, averaging H2 inside `A` gives

`q_A:=2e(A)/(lambda*a*n) >= kappa*a/alpha^2-o(1)`.

The full H1 core gives

`q_C>=h*b/c-o(1)`

for `C=B union R`. The `2x2` PSD compression therefore yields

`T <= U(d)+o(1)`,

`U(d):=sqrt{a*c*(1-kappa*a/alpha^2)*(1-h*b/c)}`.

Hence reservoir padding proves the conditional lower bound

`x >= [a*kappa/alpha-(d/s)U(d)]/(1-d/s)-o(1)`

whenever `d<s`.

This can beat the one-sided-A padding profile in some parameter subregimes, but it is **not** a uniform replacement: it is unavailable when `d>=s`, and even for `d<s` the displayed numerator is not forced positive by H1--H2 alone. Under the owner's rule I therefore do not promote it to the tracked metric. It is recorded as a failed full-bound route, not as a new theorem label.

## 8. Method #20 — why mixed padding does not fix that obstruction with the present scalar data

The natural next attempt is to pad `B` with `y n` vertices from `A` and `(d-y)n` vertices from `R`. Averaging the H2 test over these choices gives, asymptotically,

`x + y*q_A + ((d-y)/s)*z >= a*kappa/alpha`,

where `max(0,d-s)<=y<=d`.

If one uses only the scalar bounds currently available,

`q_A<=Q(d)`

from the two-block spectral compression and

`z<=U(d)`

from the total-cross estimate above, then the certified lower bound is

`x >= a*kappa/alpha-y*Q(d)-(d-y)*U(d)/s`.

The right side is affine in `y`. Therefore its optimum over the admissible interval is always an **endpoint**: pure A-padding or maximal reservoir-padding. There is no interior mixed-padding gain at this information level.

This precisely identifies what the next genuinely new route must contain. A three-block `(A,B,R)` PSD/compression argument would have to control the **joint feasible region** of `(q_A,z,x)` rather than separately maximizing `q_A` and `z`. Without such correlation information, changing the padding mixture is only a reparameterization of the two endpoint routes.

## 9. Prior-art scope and honest status

Nothing here is labeled as a closure of CMW Question 5.1. H0002 remains a source-valid **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE** theorem on the already-frozen H1--H2--H3 class. The high-degree-core argument and two-block spectral compression are elementary mechanisms; the bounded search did not locate this exact full-slack profile in the source literature, but absence from a bounded search is not a novelty certificate.

The original Beck--Fiala existence target is not reopened. On the stated Guo--Fang--Lu theorem the complete current-literature bound is

`B(t,n)<3 sqrt(2 pi t)` for all integer `t>=1` and all `n`,

with no `log n` restriction. This is recorded as **KNOWN**, not as R16 movement.

## 10. Model/scheduler control check

The model-control limitation is still unchanged. The exposed task controls allow prompt/scheduling/enablement fields but expose **no binding model-family selector, no reasoning-effort selector, and no authenticated runtime-model receipt**. Thus `GPT-6 / maximum` remains prompt text only here; this run is actually GPT-5.6 Sol with reasoning level UNVERIFIED. Enforcing the requested configuration would require platform-level scheduler/API fields for model and reasoning plus per-run applied-model attestation.

The historical P26 `You cannot modify this task` denial was authorization-context-specific. Root `RESULTS.md` records that the P26 full update later succeeded from an authorized context. If such a denial recurs, the compliant workaround remains the owning authorized workspace/account context or platform support, never task duplication or permission bypass. No scheduler was modified in this run.

## 11. Run disposition

- target: H0002 / CMW Question 5.1;
- lane: HARD OUTSIDE;
- source status: OPEN-LOOKING in bounded current search;
- frozen class: unchanged H1--H2--H3;
- metric before: every fixed `g<G_H=a1+Phi(d_H-d1)`;
- metric after: every fixed `g<G_core=a1+Phi(d_core-d1)`, with `d_core>d_H`;
- movement: **YES, strict**;
- supported unchanged count: `0`;
- stuck recovery: `false`;
- finite checker: none, because the new result is analytic and has no finite computational core;
- peer/shared files modified: none;
- email/Drive/public posting/workflow/permission/scheduler actions: none.

Next substantive target: do not spend another run taking a smaller slack. The full H1 complement-core inequality has now been exhausted. The next useful route is a genuine three-block `(A,B,R)` PSD optimization, or an exact analysis of the first algebraic zero of `F_core` that produces a stronger global cut statement. The mixed-padding calculation above shows why a scalar two-block reparameterization cannot supply that by itself.

```yaml
ledger_delta:
  track: R16
  canonical_target: H0002
  source: "Christoph-Morawski-Wigderson arXiv:2608.19145v1 Question 5.1"
  lane: HARD_OUTSIDE
  status_before: "PARTIAL / SOURCE OPEN-LOOKING / ACTIVE"
  status_after: "PARTIAL / SOURCE OPEN-LOOKING / ACTIVE"
  frozen_metric: "g_twoaxis(epsilon,rho,kappa) on unchanged H1-H2-H3"
  before: "every fixed g < G_H = a1 + Phi(d_H-d1)"
  after: "every fixed g < G_core = a1 + Phi(d_core-d1), where d_core>d_H"
  new_profile: "F_core(d)=a*kappa/alpha-d+d*Xi(d)^2/[a*(c-h*b)]"
  strict_root_gain: "d_core>d_H"
  concrete_receipt: "g_receipt=(G_H+G_core)/2"
  movement: true
  supported_unchanged_count: 0
  methods: [5, 15, 20]
  method_outcomes:
    B5: "SUCCESS: full asymptotic H1 complement-core profile crosses the previous half-slack root"
    B15: "REJECTED AS UNIFORM ROUTE: reservoir padding is conditional on d<s and can have nonpositive certified numerator"
    B20: "BARRIER: mixed padding is affine in the mixing parameter under current scalar bounds, so only endpoint routes survive"
  stuck_recovery: false
  nominal_beck_fiala_status: "KNOWN current-literature baseline on stated Sep-2026 Komlos manuscripts"
  nominal_uniform_bound: "B(t,n) < 3 sqrt(2 pi t) for every integer t>=1 and all n, per Guo-Fang-Lu arXiv:2609.11189v1"
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: "UNVERIFIED"
  model_selector_exposed: false
  reasoning_selector_exposed: false
```
