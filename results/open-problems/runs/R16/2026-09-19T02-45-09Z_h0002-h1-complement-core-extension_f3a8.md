Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** on the unchanged frozen H0002 class, this run strictly enlarges the strongest complete incoming giant-fraction envelope by replacing the old pair-capacity profile `F` with an H1-strengthened profile `F_H` whose first positive root lies strictly farther to the right. Section-B methods actually used: **#7 TAKE THE LIMIT, #11 DUALIZE, #24 FIND THE EXTREMAL OBJECT**. All 30 Section-B moves had already appeared on H0002, so these are honest nonconsecutive reuses.

# R16 — H0002: deletion resilience forces internal complement density and pushes the pair-capacity root

## 1. Continuity, ownership, required reads, and current-source check

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1: identify natural graph hypotheses under which `p >= (1+epsilon)/lambda(G)` forces a component of order `Omega(|G|)` with constant probability.

Before research I reconciled the required repository state: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H-intake record in `probability_1000_intake_H_20260914/problems.jsonl`, the newest R16 report `runs/R16/2026-09-19T01-47-50Z_h0002-positive-profile-continuation_7c2e.md`, and the recoverable same-source neighboring G0011 terminal handoff. No release or conflicting ownership of H0002 was found.

Fresh current-source checks still recover CMW only as arXiv:2608.19145v1, dated 19 Aug 2026; a bounded title/author/question search did not locate a later source-matching resolution of Question 5.1. This is negative evidence only, not a worldwide openness or novelty certificate.

The nominal Beck--Fiala title remains stale as an unresolved existence target. Bansal--Jiang, arXiv:2508.03961v2, prove the conjectured `O(sqrt(t))` scale directly for `t >= log^2 n`; Guo--Fang--Lu, arXiv:2609.11189v1 (10 Sep 2026), state the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce discrepancy `< 3 sqrt(2 pi t)` for every integer `t>=1`; Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), give an independent elementary Komlos proof with constant `36`. A fresh search also surfaced Altschuler, arXiv:2609.19714 (17 Sep 2026), on improved algorithms for bounded-set Beck--Fiala, but that does not change the existence-level supersession by the Komlos results. These are extremely recent manuscripts, not mature refereed consensus. On their stated theorems, however, the original square-root Beck--Fiala existence target is a current-literature KNOWN baseline, so R16 correctly continues the already-admitted H0002 successor.

Current links checked:

- CMW: https://arxiv.org/abs/2608.19145
- Bansal--Jiang: https://arxiv.org/abs/2508.03961
- Guo--Fang--Lu: https://arxiv.org/abs/2609.11189
- Karingula--Lovett: https://eccc.weizmann.ac.il/report/2026/188/
- Altschuler: https://arxiv.org/abs/2609.19714

## 2. Frozen class and the strongest incoming consequence

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n=|G|`, `lambda=lambda(G)`,

`h:=1-epsilon/8`,

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`.

The H0002 class is unchanged:

1. H1: `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. H2: `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. H3: `lambda -> infinity`.

The fixed metric remains `g_twoaxis(epsilon,rho,kappa)`, the largest explicit uniform giant fraction proved for this exact class at every `p >= (1+epsilon)/lambda`.

I preserve all notation from the preceding report. In particular, it produced a checkpoint `d1`, with

`beta:=alpha-d1>0`,

`a1:=rho-beta`,

`c1:=1-a1`,

and the old pair-capacity profile

`a(d):=rho-alpha+d`,

`b(d):=alpha-d`,

`c(d):=1-a(d)=1-rho+b(d)`,

`Xi(d):=kappa*a(d)*c(d)/alpha^2` when `c(d)>=alpha`,

`Xi(d):=a(d)*kappa/alpha-(alpha-c(d))` when `c(d)<alpha`,

`F(d):=a(d)*kappa/alpha-d + d*Xi(d)^2/[a(d)c(d)]`.

The preceding report defined

`d_plus:=sup{d in [d1,alpha): Xi(s)>0 and F(s)>0 for every s in [d1,d]}`

and proved `d_plus>d1`. For every fixed `d<d_plus`, round-one harvesting plus genuine-component sprinkling yields a connected seed component of normalized size at least

`rho-alpha+d-o(1)`.

It also retained an old anchor of density `a1` and an absorption exponent. Write

`s:=1-rho`,

`Delta:=epsilon(7-epsilon)/(8-epsilon)`,

`Fhat1>=F(d1)>0`

for the preceding endpoint capacity (including its complement-symmetry correction when available), and

`Rhat:=1-exp[-Delta*Fhat1/beta] in (0,1)`.

The preceding report advertised the absorption envelope with the head-start capped at `s`. But it simultaneously proved the uncapped seed-only statement for every `d<d_plus`. To avoid claiming movement against an artificially weak summary, I reconcile both already-proved clauses and take the **strongest complete incoming consequence** as the baseline.

Put

`D_plus:=d_plus-d1>0`

and define the strictly increasing function

`Phi(D):=Rhat*s + D*(1-Rhat)` for `0<=D<=s`,

`Phi(D):=D` for `D>=s`.

The two formulas agree at `D=s`. The incoming reports together prove every fixed

`g < G_in := a1 + Phi(D_plus)`.

Indeed, for `D<=s` this is exactly the fixed-anchor absorption formula with a seed head start `D`; for `D>=s`, the seed-only component `a1+D` is stronger than the capped absorption summary. This is the baseline I beat below.

## 3. Method #24 — the extremal object hidden inside H1 is a high-degree complement core

The old spectral-padding proof used only `q_C>=0` for the internal Rayleigh quotient of the complement `C=V\A`, except in the special regime where H2 itself could fit two disjoint `alpha`-blocks inside `C`. That discarded a much stronger consequence of H1 which is available **for every** `d<alpha`.

Fix `d in [d1,alpha)`. Let `A` be the large seed side of density

`a=a(d)=rho-b`,

where

`b=b(d)=alpha-d>0`,

and put

`C:=V\A`, `|C|=c n+o(n)`, `c=c(d)=s+b`.

The key point is that `|A|=(rho-b)n+o(n)`. H1 therefore leaves an additional deletion budget of essentially `b n` **inside C**.

### Complement-core lemma

For every fixed slack `eta>0` and all sufficiently large `n`,

`2e(C)/(lambda c n) >= h*b/c - eta`.

In particular, the robust fixed choice

`mu_H(d):= h*b(d)/(2c(d))`

satisfies

`q_C:=2e(C)/(lambda c n) >= mu_H(d)`

for all sufficiently large `n`.

#### Proof

Let

`T:={v in C: deg_C(v) >= h lambda}`.

Suppose `|T|<=b n-o(n)`. Then

`|A union T| <= rho n`

for all sufficiently large `n`, so H1 gives

`lambda(G-(A union T))=lambda(C-T) >= h lambda`.

But every vertex of `C-T` had degree in `C` strictly below `h lambda`, hence also has degree in the induced graph `C-T` strictly below `h lambda`. Therefore

`lambda(C-T) <= Delta(C-T) < h lambda`,

a contradiction. Thus `|T|>b n-o(n)`. Summing the degrees of vertices of `T` inside `C` gives

`2e(C) >= sum_{v in T} deg_C(v)
        > h*b*lambda*n-o(lambda n)`.

Divide by `lambda c n`.

This is the new structural input. It is not another continuity estimate: H1 forces a **macroscopic internal edge density in the whole complement** because otherwise one can delete the small high-degree core within the unused H1 budget and make the residual spectral radius fall below `h lambda`.

## 4. Method #11 — feed the H1 core into the dual two-block spectral compression

The previous density-amplified H2/padding argument gives, uniformly for the same large side `A`,

`e(A,C)/(lambda n) >= Xi(d)-o(1)`

whenever `Xi(d)>0`.

Compress `Adj(G)/lambda` to the span of the normalized indicators of `A` and `C`. With

`q_A:=2e(A)/(lambda a n)`,

`q_C:=2e(C)/(lambda c n)`,

`x:=e(A,C)/(lambda n)`,

the compression is

`Q = [[q_A, x/sqrt(ac)], [x/sqrt(ac), q_C]]`.

Because the ambient spectral radius is `lambda`,

`I-Q` is positive semidefinite. Hence

`(1-q_A)(1-q_C) >= x^2/(ac)`.

The old universal profile inserted only `q_C>=0`. The complement-core lemma instead gives the fixed positive lower bound `q_C>=mu_H(d)`. Therefore

`q_A <= 1 - Xi(d)^2/[a(d)c(d)(1-mu_H(d))] + o(1)`.

Now repeat the one-sided padding average: pad the deficient seed side `B`, of density `b=alpha-d`, with `d n` vertices from `A`, choose the H2 test block on the remaining large side, and average. Exactly as in the preceding report,

`e(A,B)/(lambda n) >= a(d)*kappa/alpha - d*q_A - o(1)`.

Substituting the improved spectral upper bound gives the new pair-capacity profile

`F_H(d):=a(d)*kappa/alpha-d
          + d*Xi(d)^2/[a(d)c(d)(1-mu_H(d))]`,

where

`mu_H(d)=h*(alpha-d)/[2(1-rho+alpha-d)]`.

For every `d>0` with `Xi(d)>0`,

`F_H(d)-F(d)
 = d*Xi(d)^2/[a(d)c(d)] * mu_H(d)/(1-mu_H(d))
 >0`.

This strict pointwise gain is the central result of the run.

The profile is still elementary. On the branch `c>=alpha`, multiplying `F_H(d)=0` by the positive factor `c-hb/2` produces a polynomial equation of bounded degree in `d`; on the branch `c<alpha`, the same is true because `Xi` is affine. Thus the new continuation endpoint below is an exact low-degree algebraic scalar, not an uncheckable variational object.

## 5. Method #7 — go all the way to `d -> alpha` and prove the old endpoint is genuinely interior

To turn the pointwise gain `F_H>F` into fixed-metric movement, I must rule out the possibility that the old continuation already reached the boundary `d=alpha`, leaving no room to move.

First recover the necessary H2 nonvacuity bound

`kappa <= alpha^2`.

Indeed, average H2 over uniformly random disjoint `alpha n`-subsets `X,Y` of `V`. Since `2e(G)<=lambda n`,

`E e(X,Y) <= (alpha^2+o(1)) lambda n`,

while every realization is at least `kappa lambda n`. Hence `kappa<=alpha^2`. Put

`x:=kappa/alpha^2 in (0,1]`.

I now inspect the boundary `d -> alpha`, so `b=alpha-d ->0`, `a->rho`, `c->s:=1-rho>0`.

### Case 1: `s>=alpha`

The first branch of `Xi` applies at the boundary. Then

`F(alpha-)/alpha
 = x*rho - 1 + x^2*rho*s
 <= rho - 1 + rho*s
 = -s^2
 <0`.

Thus the old positive profile must terminate strictly before `alpha`.

### Case 2: `0<s<alpha`

If `Xi` reaches zero before the boundary, the old admissible interval already terminates before `alpha`. Otherwise suppose `Xi(alpha-)>0`. Write

`r:=s/alpha in (0,1)`,

`y:=1-x*rho`.

Since `x<=1`,

`y>=1-rho=s=alpha*r`.

At the boundary the second branch gives

`Xi(alpha-)=alpha*(r-y)>0`,

so `r>y`. Moreover

`F(alpha-)/alpha
 = -y + alpha*(r-y)^2/(rho*r)`.

Because `y>=alpha r`,

`0<r-y<=r(1-alpha)`.

Since `s<alpha` implies `rho=1-s>1-alpha>(1-alpha)^2`,

`alpha*(r-y)^2/(rho*r)
 < alpha*r*(1-alpha)^2/rho
 < alpha*r
 <= y`.

Therefore again

`F(alpha-)<0`.

So in all regimes the old continuation cannot reach `alpha`.

There is one more boundary issue: could `Xi` itself be the first quantity to hit zero at the old endpoint? No. The first branch never has `Xi=0`. On the second branch, `Xi=0` implies

`a*kappa/alpha = alpha-c = d-s`,

and therefore

`F(d)=a*kappa/alpha-d=-s<0`.

Since `F` was positive before the endpoint, it must cross zero strictly before such an `Xi`-zero. Hence the old endpoint is characterized by

`d_plus<alpha`,

`Xi(d_plus)>0`,

`F(d_plus)=0`.

This is exactly the configuration needed by the new H1 correction.

## 6. The old root is not a root any more

At `d=d_plus`, the complement-core parameter satisfies

`mu_H(d_plus)>0`

because `b(d_plus)=alpha-d_plus>0`, and `Xi(d_plus)>0`. Therefore

`F_H(d_plus)
 = F(d_plus)
 + d_plus*Xi(d_plus)^2/[a(d_plus)c(d_plus)]
   * mu_H(d_plus)/(1-mu_H(d_plus))
 >0`.

The functions involved are continuous on the admissible side of the branch point. Consequently there exists a nontrivial interval immediately to the right of `d_plus` on which both `Xi` and `F_H` stay positive.

Define the exact strengthened continuation endpoint

`d_H:=sup{d in [d_plus,alpha):
           Xi(u)>0 and F_H(u)>0 for every u in [d_plus,d]}`.

Then

`boxed: d_H > d_plus`.

No endpoint attainment is claimed.

This is qualitatively stronger than the previous run's arbitrary continuity radius. The old first root is crossed because a previously discarded hypothesis, H1, supplies positive complement internal density. The new endpoint is the first root of an explicit piecewise-rational/algebraic profile.

## 7. Propagate the stronger root through harvesting, gluing, and absorption

For every fixed `d<d_H`, the exact same first-round two-scale harvesting theorem still produces genuine connected seed components of total mass `(rho-o(1))n`. The genuine seed-component quotient has `O(n/lambda^(2/3))` vertices.

Because `F_H` has a positive minimum on every compact subinterval ending at such a fixed `d`, round `p_g=lambda^(-4/3)` misses any relevant quotient cut with probability `exp[-Theta(n/lambda^(1/3))]`, while the quotient cut count is only `exp[O(n/lambda^(2/3))]`. Therefore round two now yields a connected seed component of normalized size at least

`rho-alpha+d-o(1)`

for every fixed `d<d_H`.

Put

`D_H:=d_H-d1`.

Then

`D_H > D_plus`.

The old anchor of density `a1` and its old absorption theorem remain valid without modification: enlarging the seed giant cannot invalidate the old anchor geometry. Thus the same two already-proved mechanisms combine with the larger head-start range:

1. seed-only: every fixed coefficient below `a1+D_H` is obtainable;
2. old-anchor absorption: for every fixed head start `D<min(D_H,s)`, every coefficient below
   `a1 + Rhat*s + D*(1-Rhat)` is obtainable.

Using the same strictly increasing reconciliation function

`Phi(D)=Rhat*s+D*(1-Rhat)` for `D<=s`,

`Phi(D)=D` for `D>=s`,

the new complete envelope is

`G_H:=a1+Phi(D_H)`.

The strongest complete incoming envelope was

`G_in:=a1+Phi(D_plus)`.

Since `D_H>D_plus` and `Phi` is strictly increasing,

`boxed: G_H > G_in`.

Hence every fixed

`g < G_H`

satisfies

`P(L1(G_p) >= g n) -> 1`

uniformly on the unchanged H1--H2--H3 class.

For a single immutable metric receipt strictly above the entire strongest incoming envelope, define

`g_receipt:=(G_in+G_H)/2`.

Then

`G_in < g_receipt < G_H`,

so `g_receipt` is proved and lies a fixed positive distance above the complete incoming bound, not merely above the preceding report's displayed summary.

This is the fixed-metric movement for the run.

## 8. Why this is a genuinely new route rather than another continuity lemma

The preceding run's continuation used only the fact that `F(d1)>0`, then bounded `F'` to move a short distance. The present argument changes the profile itself:

`F -> F_H`.

The strict bonus is forced by H1 and survives exactly at the old first root where `F=0`. Therefore it crosses a barrier the previous scalar argument could not cross by continuity alone.

The mechanism can be summarized as a proof-by-extremal-core dichotomy:

- if the complement has too few `h lambda`-degree vertices, delete all of them within the remaining H1 budget and force its residual maximum degree, hence spectral radius, below `h lambda`;
- therefore there must be more than `b n` such vertices;
- therefore the complement's uniform Rayleigh quotient is positive;
- therefore two-block spectral compression forces strictly less internal density on the large side than the old proof allowed;
- therefore padding the deficient seed side loses strictly less capacity;
- therefore the old pair-capacity root moves.

This uses H1 in a way none of the preceding H0002 profiles did.

## 9. What each Section-B move actually did

### #7 — TAKE THE LIMIT

I pushed the old piecewise-rational profile all the way to the missing boundary `d -> alpha` instead of stopping at another local radius. The nonvacuity inequality `kappa<=alpha^2` makes the boundary sign explicit and proves `d_plus<alpha`; the old endpoint is therefore a genuine interior zero, not an artefact of truncating the parameter range.

### #11 — DUALIZE

The new complement-core lower bound was inserted on the opposite side of the same two-dimensional spectral compression. The PSD condition on `I-Q` converts positive internal complement density into a stronger upper bound on the large-side Rayleigh quotient, which is exactly the quantity the padding argument pays for.

### #24 — FIND THE EXTREMAL OBJECT

The obstruction to H1 is the set of complement vertices of degree at least `h lambda`. If that high-degree core fit inside the remaining deletion budget `b n`, deleting it would leave maximum degree below `h lambda`, contradicting H1. The extremal core therefore has size `>b n`, forcing `Omega(lambda n)` internal complement edges and producing the new profile gain.

## 10. Prior-art scope

The ingredients are standard individually: maximum-degree control of spectral radius, Rayleigh quotients, principal subgraphs, two-by-two spectral compression, averaging, sprinkling and Chernoff bounds. I make no novelty claim for those tools.

A bounded current search did not locate this exact H1-to-complement-core lemma embedded in the CMW Question 5.1 framework or the resulting `F_H` profile/root continuation. A negative search is not a novelty certificate. The source-level status remains PARTIAL because CMW ask for natural conditions in general, while this theorem is for R16's frozen H1--H2--H3 sufficient-condition class.

## 11. Status, next obstruction, and model-control report

H0002 remains **PARTIAL / SOURCE OPEN-LOOKING IN BOUNDED CURRENT SEARCH / ACTIVE**.

The fixed metric moved, so the supported unchanged count remains/reset to **0** and no Section-I stuck recovery is triggered.

The next genuine obstruction is now the first zero of `F_H`, not the first zero of `F`. The useful next routes are different from another local derivative estimate:

1. solve the low-degree algebraic root of `F_H` exactly on both `Xi` branches and optimize the resulting closed-form giant envelope;
2. iterate the core argument: once H1 forces `q_C>0`, ask whether the same deletion budget forces a second degree quantile inside `C`, yielding a stronger-than-Rayleigh distributional constraint;
3. upgrade the compression from the two indicator blocks `(A,C)` to `(A,B,R)` where `R` is the unused reservoir, and optimize the resulting PSD constraints jointly.

A nonconsecutive suggested next triple is **#8 DISCRETIZE, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS**; these are reuses because all 30 methods were exhausted earlier on H0002.

The model-control limitation is unchanged. The task-control surface exposed to this run has no binding model-family selector, no reasoning-effort selector and no authenticated per-run applied-model receipt. GPT-6/maximum therefore remains prompt-only here. Enforcing it would require scheduler/API fields for model and reasoning plus runtime attestation. The historical P26 `You cannot modify this task` denial was authorization-context-specific; repository evidence records a later successful P26 update from an authorized context. The compliant workaround for a task that still refuses modification is the owning authorized workspace/account context or platform support, never duplication or permission bypass.

## 12. Validation / bookkeeping (final approximately 10%)

No finite checker was created. The result is analytic; the theorem-sized argument is written above and there is no finite-enumeration core. I did not edit `RESULTS.md`, `QUEUE.md`, `POSTED.md`, any claim file, peer track, scheduler, email, Drive item, workflow, permission or public posting. This immutable own-track report alone carries the delta.

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
    old_profile: "F(d)=a*kappa/alpha-d+d*Xi(d)^2/(a*c)"
    root: "d_plus<alpha, first positive-profile endpoint"
    complete_envelope: "G_in=a1+Phi(d_plus-d1), reconciling seed-only and fixed-anchor absorption clauses already proved"
  after:
    complement_core: "q_C >= h*(alpha-d)/(2*(1-rho+alpha-d)) for all sufficiently large n (fixed-slack form)"
    new_profile: "F_H(d)=a*kappa/alpha-d+d*Xi(d)^2/[a*c*(1-mu_H(d))]"
    strict_profile_gain: "F_H(d)>F(d) whenever d>0 and Xi(d)>0"
    old_endpoint_structure: "d_plus<alpha, Xi(d_plus)>0, F(d_plus)=0"
    new_root: "d_H>d_plus"
    new_complete_envelope: "G_H=a1+Phi(d_H-d1)>G_in"
    concrete_receipt: "g_receipt=(G_in+G_H)/2"
  movement: true
  supported_unchanged_count: 0
  methods: [7, 11, 24]
  stuck_recovery: false
  nominal_beck_fiala_status: "KNOWN current-literature baseline on stated Sep-2026 Komlos manuscripts; not reopened"
  finite_checker: "not applicable; analytic proof"
  shared_root_edits: false
  peer_file_edits: false
  scheduler_edits: false
```
