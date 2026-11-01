Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala metric remains a **KNOWN current-preprint baseline** at `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n`; on the active exclusive R16/H0002 successor, the strongest complete giant-fraction envelope moves strictly from `G_multi` to `G_coreavg>G_multi` on the same frozen H1--H2--H3 class. Section-B methods actually used: **#9 RANDOMIZE, #14 FIND THE GROUP ACTING, #27 SWAP THE QUANTIFIERS**. The immediately preceding triple was #2/#3/#13, so this is not a consecutive repeat. All thirty moves have already appeared somewhere in the long H0002 history; these are deliberate nonconsecutive reuses because the new route is genuinely different.

# R16 — H0002: average every certified subanchor into the whole connected core

## 1. Continuity, required reads, ownership, and current-source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1:

> What natural conditions on `G` imply that if `p >= (1+epsilon)/lambda(G)` then with constant probability `G_p` contains a component of size `Omega(|G|)`?

The source itself explains the obstruction: the spectral radius can be localized on a very small part of the graph, so robust connectivity alone need not prevent most of the graph from behaving subcritically at `(1+epsilon)/lambda(G)`.

Before new mathematics I reconciled the required state rather than restarting: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H0002 intake identity `arxiv_2608_19145::Question 5.1; Section 5, Concluding remarks`, the newest own report `runs/R16/2026-09-19T07-29-30Z_h0002-multi-anchor-layercake-absorption_e81c.md`, and its substantive connected-core proof repair `artifacts/R16/2026-09-19T07-32-10Z_h0002-multi-anchor-connected-core-proof-repair_e81c.md`.

I also checked the current neighboring CMW-family state. The older R7-07 CMW long-cycle line is not a competing H0002 claim; R7-07 has moved to the distinct F0012 random-sign-matrix target and its newest 19 Sep report is a STUCK2 run there. No competing H0002 ownership was found.

Fresh primary/current checks on **19 Sep 2026** recover:

- CMW only as arXiv:2608.19145v1, submitted 19 Aug 2026; the bounded search did not surface a later source-matching resolution of Question 5.1;
- Bansal--Jiang, arXiv:2508.03961v2, which reaches the Beck--Fiala `O(sqrt(t))` scale directly for `t>=log^2 n` and gives a weaker polylog-loss estimate below that regime;
- Guo--Fang--Lu, arXiv:2609.11189v1, submitted 10 Sep 2026, whose abstract states a `3 sqrt(2 pi)` Komlos bound and explicitly deduces discrepancy `<3 sqrt(2 pi t)` for every integer `t>=1`;
- Karingula--Lovett, ECCC TR26-188, 17 Sep 2026, which gives an elementary Komlos proof with constant `36` and explicitly describes itself as simplifying the Guo--Fang--Lu proof;
- Altschuler, arXiv:2609.19714 (17 Sep 2026), which gives improved *algorithmic* Beck--Fiala bounds under bounded row size; this does not reopen the existential all-`t` target already covered by the Komlos preprints.

These are extremely recent manuscripts / technical reports, not mature refereed consensus. Their stated theorems are current baselines, not R16 novelty. A bounded search for the exact full-core averaging mechanism below and for a later resolution of CMW Question 5.1 returned the CMW source and general spectral/expander percolation literature, but no source-matching later theorem. That negative search is not a novelty certificate.

## 2. Frozen H0002 class and incoming complete envelope

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n:=|G|`, `lambda:=lambda(G)`,

`h:=1-epsilon/8`,

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`,

`s:=1-rho>0`.

The graph class is unchanged:

1. **H1:** `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. **H2:** `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. **H3:** `lambda -> infinity`.

Use the established deficient-side parameterization

`a(d):=rho-alpha+d`,

`b(d):=alpha-d`,

so `a(d)+b(d)=rho`.

The all-padding report supplies a positive deterministic pair-capacity profile `F_pad(d)` on the certified interval

`d1 < d < dP`,

where `dP:=d_pad` is its first zero-capacity endpoint. Its inequalities use only H1, H2, the global spectral bound and the sizes of the three blocks. Consequently the conclusion is universal for the relevant host-graph pairs, not a property of one particular quotient realization:

> for every fixed `d in (d1,dP)` and every disjoint `A,B` with
> `|A|=a(d)n+o(n)`, `|B|=b(d)n+o(n)`,
> one has
> `e_G(A,B) >= F_pad(d) lambda n-o(lambda n)`.

At the frozen old anchor `d1`, retain the already-proved coefficient `Fanc>0` and rate

`Ranc:=1-exp[-Delta*Fanc/beta]`,

where

`beta:=alpha-d1`,

`Delta:=epsilon*(7-epsilon)/(8-epsilon)>0`.

Put

`aP:=a(dP)`

and define the old endpoint remaining-mass profile

`m(d):=[s-(dP-d)]_+`.

For `d in (d1,dP)` define the old multi-anchor attachment rate

`R(d):=1-exp[-Delta*F_pad(d)/b(d)]`,

and set `R(d1):=Ranc`.

The immediately preceding report, with the connected-core repair read alongside it, proved

`G_multi
 = aP + sup_{D finite, d1 in D subset [d1,dP)}
          integral_0^1 max_{d in D: R(d)>=t} m(d) dt`,

and every fixed `g<G_multi` satisfies

`P(L1(G_p)>=g n) -> 1`

uniformly on H1--H2--H3 for every `p>=(1+epsilon)/lambda`.

That theorem reused one absorption round against several nested *subanchors*. The new observation is that once those subanchors all sit inside one connected core, one can average over the entire orbit of subanchors and obtain a strictly stronger degree statement **into the full connected core itself**.

## 3. Endpoint cleanup: the all-padding endpoint is genuinely interior

This small lemma removes a possible boundary pathology needed later.

The standard double count of H2 over two uniformly random disjoint `alpha n`-sets gives the necessary asymptotic constraint

`kappa <= alpha^2`.

Indeed H2 forces the expected number of crossing edges to be at least `kappa lambda n`, whereas

`E e(X,Y)
 <= |E(G)| * 2(alpha n)^2/[n(n-1)]
 <= alpha^2 lambda n + o(lambda n)`

because `2|E(G)|/n <= lambda`.

Write

`r:=kappa/alpha^2 in [0,1]`.

At the formal boundary `d=alpha` we have

`a=rho`, `b=0`, `c=s`, `K=rho*r*alpha`.

Consider the zero-cut scalar tuple

`x=0`,

`q=rho*r`,

`z=rho*r*s`.

It satisfies both extreme padding equalities at the boundary:

- all-A padding: `alpha*q=K`;
- maximal-reservoir padding: if `alpha<=s`, then `(alpha/s)z=K`; if `alpha>s`, then `(alpha-s)q+z=K`.

It also satisfies the full-complement lower bound. If `s>=alpha`, then `Xi(alpha)=rho*r*s=z`. If `s<alpha`, then

`Xi(alpha)=rho*r*alpha-alpha+s`

and

`z-Xi(alpha)=(alpha-s)(1-rho*r)>=0`.

Finally the two spectral caps have a fixed strict slack at `b=0`:

`1-z^2/(rho*s)-q
 = 1-rho*r^2*s-rho*r
 = 1-rho*r(1+r*s)
 >= 1-rho(1+s)
 = s^2 > 0`.

The aggregate cap has the same denominator at `b=0`. Hence, by continuity of the finite scalar constraints, the tuple can be perturbed for all sufficiently small positive `b` while retaining `x=0`: choose `q` and `z` continuously just above their padding/full-complement lower bounds; the displayed fixed spectral slack absorbs the perturbation.

Therefore the zero-cut feasible set already occurs at some fixed `d<alpha`, and hence

`boxed: dP<alpha`.

In particular

`bP:=alpha-dP>0`.

This also places the first zero of `F_pad` in the interior of the scalar parameter domain. The explicit zero-feasibility formulas of the all-padding report and compactness of the scalar feasible set imply that on the terminal positive cell

`F_pad(d) -> 0` as `d up to dP`.

No numerical root estimate is used here.

## 4. Method #9 — randomize the subanchor inside the connected core

Fix

`d1<d<d3<dP`.

Suppose the already-established harvesting + gluing rounds have produced a connected component at least `a(d3)n-o(n)` in size. Use the connected-core repair from the preceding run: trim a spanning tree leaf-by-leaf to a connected core `W` of exactly

`|W|=a(d3)n+o(n)`.

Now fix **any** set

`B subset V\W`,

`|B|=b(d)n+o(n)`.

Instead of selecting one nested anchor `A subset W`, choose `A` uniformly from all `a(d)n`-subsets of `W`.

For every realization of `A`, the universal pair-capacity inequality gives

`e(A,B) >= F_pad(d) lambda n-o(lambda n)`.

On the other hand, by symmetry of uniform subset sampling,

`E_A e(A,B)
 = [a(d)/a(d3)+o(1)] e(W,B)`.

Averaging the deterministic lower bound over all `A` therefore yields

`boxed:
 e(W,B)
 >= [a(d3)/a(d)] F_pad(d) lambda n-o(lambda n).`

The multiplicative factor

`a(d3)/a(d)>1`

is the information lost by the previous multi-anchor proof. That proof selected a subanchor and then only used the edges certified into that smaller set. Since the capacity statement holds for **every** subanchor of the required cardinality, averaging over the full orbit certifies more edges into the one connected object that actually matters, namely `W`.

This is a deterministic conclusion. Randomization is only the averaging proof device.

## 5. Method #14 — the symmetric-group orbit turns pair capacity into a full-core degree quantile

The preceding averaging can be viewed as the action of the full symmetric group on the vertices of `W`: all `a(d)n`-subsets lie in one orbit, and every edge from `W` to `B` is counted with exactly the same frequency.

The averaged pair inequality immediately gives a stronger degree quantile into `W`.

### Lemma 5.1 (full-core lifted quantile)

Fix `theta in (0,1)` and `d1<d<d3<dP`. Then, apart from fewer than `b(d)n+o(n)` vertices of `V\W`, every vertex `v` satisfies

`d_W(v)
 >= (1-theta)
    [a(d3)/a(d)]
    [F_pad(d)/b(d)] lambda.`

Consequently there is a set `S_d(W) subset V\W` with

`|S_d(W)|/n
 >= m_{d3}(d)-o(1)`,

where

`m_{d3}(d):=[s-(d3-d)]_+`,

and every vertex of `S_d(W)` satisfies the displayed degree bound.

#### Proof

If `b(d)n+o(n)` outside vertices all had degree below the displayed threshold, choose `B` from them. Their degree sum into `W` would be strictly below

`[a(d3)/a(d)]F_pad(d)lambda n-o(lambda n)`,

contradicting Section 4.

The number of vertices outside `W` is `(1-a(d3))n+o(n)`. Subtracting the possible `b(d)n+o(n)` exceptions gives

`1-a(d3)-b(d)
 = 1-[rho-alpha+d3]-[alpha-d]
 = s-(d3-d)`.

Taking the positive part handles the vacuous case. `QED`

A second gain is conceptual: all these quantiles are now quantiles of the **same scalar degree `d_W(v)`**, rather than degree bounds into unrelated nested subanchors. Thus the set-valued information retained by the previous layer-cake proof is not lost; the threshold is simply stronger.

## 6. Method #27 — swap the quantifiers before sprinkling

The logical order in the previous proof was

`for each certified subanchor A, find many vertices with many edges into A`.

The stronger order is

`for every possible A subset W, pair capacity holds; average A first; then find many vertices with many edges into W`.

This swap is exactly what creates the factor `a(d3)/a(d)`.

Reserve, as before, a fixed absorption numerator `sigma<Delta` after the seed and gluing rounds. Conditional on the earlier rounds, the absorption round is independent. For a vertex in `S_d(W)`, the probability of opening an edge directly into the already-connected `W` is at least any fixed number below

`R_{sigma,d3,theta}(d)
 := 1-exp[-sigma(1-theta)
                (a(d3)/a(d))
                F_pad(d)/b(d)].`

For distinct outside vertices these attachment events use disjoint edge sets into `W`, so the same Poisson-binomial Chernoff argument applies.

For a finite set of anchors

`D={e1,...,ek} subset (d1,d3)`

(and retaining `d1` with its old valid rate if desired), define `S_i:=S_{e_i}(W)` and the corresponding rates. For each outside vertex use the maximum rate certified by the sets containing it. The same layer-cake identity then gives a connected final mass at least

`a(d3)
 + integral_0^1
     max_{d in D: R_{sigma,d3,theta}(d)>=t}
     m_{d3}(d) dt
 - o(1)`

with probability `1-o(1)`.

No additional sprinkling probability is spent. The gain comes entirely from changing the order of averaging and thresholding.

## 7. Remove the slack: the full-core-averaged envelope

Let `d3 up to dP`, `sigma up to Delta`, and `theta down to 0` after all finite choices are fixed.

For `d in (d1,dP)` define the lifted boundary rate

`boxed:
 Rcore(d)
 := 1-exp[-Delta
          (aP/a(d))
          F_pad(d)/b(d)].`

At `d1` it is enough to retain the already-valid old rate `Rcore(d1):=Ranc`; no strengthening at that isolated anchor is needed for the theorem below.

Define

`boxed:
 G_coreavg
 := aP
  + sup_{D finite, d1 in D subset [d1,dP)}
       integral_0^1
       max_{d in D: Rcore(d)>=t}
       m(d) dt.`

### Theorem 7.1 (full-core anchor averaging)

For every fixed

`g<G_coreavg`,

one has

`boxed:
 P(L1(G_p)>=g n) -> 1`

uniformly on the unchanged H1--H2--H3 class whenever

`p>=(1+epsilon)/lambda(G)`.

#### Proof

Fix `g<G_coreavg`. Choose a finite anchor set `D` whose displayed finite-anchor value exceeds `g` by a fixed margin. Choose `d3<dP` larger than every anchor in `D` and sufficiently close to `dP`; choose `sigma<Delta` sufficiently close to `Delta` and `theta>0` sufficiently small that the finite expression in Section 6 still exceeds `g` by half the margin.

The established two-scale harvesting argument remains supercritical because `sigma<Delta`. The established genuine-component gluing argument works up to `d3` because `F_pad` is uniformly positive on every compact subinterval below `dP`. Trim the resulting connected component to the controlled connected core `W` exactly as in the previous run's proof repair.

Sections 4--6 then give deterministic full-core degree quantiles for each anchor in `D`, followed by independent absorption variables for distinct outside vertices. Layer-cake handles arbitrary overlap and Chernoff concentration loses only `o(n)` vertices. Thus the final component exceeds `gn` with probability `1-o(1)`. `QED`

No endpoint attainment at `G_coreavg` is claimed.

## 8. The new envelope is strictly larger than `G_multi`

Pointwise rate improvement is immediate. For every

`d in (d1,dP)`,

we have

`aP/a(d)>1`,

`F_pad(d)>0`,

and hence

`boxed: Rcore(d)>R(d).`

Because both old and new envelopes are suprema over finite layer-cake unions, one still has to rule out the possibility that all those pointwise gains disappear when the supremum is taken. The one-dimensional semialgebraic structure of `F_pad` rules that out.

### 8.1 Rectangle-union representation

For the old rates define

`M(t):=sup{m(d): d in [d1,dP), R(d)>=t}`, 

with the supremum over the empty set equal to zero.

Then

`G_multi=aP+integral_0^1 M(t) dt`.

Indeed every finite-anchor layer-cake value is at most the right-hand side. Conversely `M` is bounded and nonincreasing. Given any `eta>0`, take a sufficiently fine threshold partition and, at each partition endpoint, choose one anchor whose mass is within `eta` of the defining supremum. The finite collection of those anchors gives the corresponding lower Riemann sum. Letting the mesh and `eta` go to zero recovers the integral. The same statement holds for `Rcore`, with frontier `Mcore(t)`.

Geometrically, these integrals are simply the areas of the unions of rectangles

`[0,R(d)] x [0,m(d)]`

and

`[0,Rcore(d)] x [0,m(d)]`.

### 8.2 A terminal exposed arc

The profile `F_pad` is the value of a fixed finite-dimensional optimization problem with polynomial/rational inequalities in `(d,x,z,q)` after clearing positive denominators. Therefore it is a semialgebraic value function. On the terminal positive cell below the interior first zero `dP`, the established zero-crossing formulas give

`F_pad(d)>0`,

`F_pad(d)->0` as `d up to dP`,

while `b(d)->bP>0`.

Hence

`E(d):=Delta*F_pad(d)/b(d)`

is positive and tends to zero. By the semialgebraic monotonicity theorem there is a fixed `eta0>0` such that on

`I:=(dP-eta0,dP)`

`E(d)`, and therefore `R(d)=1-exp[-E(d)]`, is continuous and strictly decreasing as `d` increases. Shrink `eta0` if needed so that `m(d)>0` throughout `I`; there `m(d)=s-dP+d` is strictly increasing.

Thus every point of this terminal rate--mass curve is Pareto exposed: moving right raises mass but lowers rate.

### 8.3 Positive area gain

Choose any `d0 in I`. Put

`r0:=R(d0)`,

`rc0:=Rcore(d0)>r0`,

`m0:=m(d0)>0`.

Choose `d_- in I` with `d_-<d0`, sufficiently close to `d0`. Since `R` is strictly decreasing,

`r_-:=R(d_-)>r0`.

The interval

`J:=(r0, min{rc0,r_-})`

has positive length.

For every `t in J`, the old rightmost anchor satisfying `R(d)>=t` lies strictly to the left of `d0`; call it `d(t)`. Any still earlier anchor has even smaller `m`, and every anchor to the right of `d0` has rate below `r0<t`. Therefore

`M(t)=m(d(t))<m0`.

But under the lifted rates, the single anchor `d0` itself qualifies throughout `J`, so

`Mcore(t)>=m0`.

Hence

`Mcore(t)>M(t)`

for every `t in J`, while `Mcore>=M` everywhere. Therefore

`boxed:
 G_coreavg-G_multi
 >= integral_J [m0-M(t)] dt
 >0.`

Define the explicit positive frontier-area gap

`delta_core
 := integral_J [m0-M(t)] dt >0`.

Then a frozen receipt strictly beyond the **entire incoming complete envelope** is, for example,

`boxed:
 g_receipt:=G_multi+delta_core/2`,

and

`P(L1(G_p)>=g_receipt*n)->1`.

This is genuine fixed-metric movement, not a restatement of the two-anchor bound from the preceding run.

## 9. Why the route is stronger than the preceding multi-anchor theorem

The previous theorem knew that a chosen subanchor `A_d` had many host edges to most outside vertices. Its attachment rate used the threshold

`F_pad(d)/b(d)`.

The present theorem uses the fact that **every** `a(d)n`-subset of the connected core satisfies the same pair-capacity statement. Averaging over the symmetric orbit forces the full connected core to have, against every `b(d)n`-set,

`aP/a(d)`

times as many certified edges in the endpoint limit. That multiplicative gain is then inherited by the exponential attachment rate.

Nothing about this argument requires Boolean signs to be replaced by vectors, changes the frozen H0002 hypothesis class, spends extra percolation probability, or assumes any density relation such as `lambda/n` bounded away from zero. It also survives the localization obstruction that killed the previous residual-Perron route: the proof averages host edges already certified at macroscopic scale, rather than trying to delocalize a residual eigenvector.

## 10. Failed alternatives this run

The 90-percent rule requires recording failed routes rather than hiding them.

### A. Use the exact `L2` degree vector to absorb the discarded `b(d)n` vertices

For an anchor `A`, the operator-norm identity gives

`sum_v d_A(v)^2 <= lambda^2 |A|`.

Together with the pair-capacity lower bound on the sum of the `b(d)n` smallest outside degrees, this yields a positive lower bound on the expected number of attachments even inside the discarded low-degree block. For example, using

`1-e^{-x} >= x/(1+x)`

and Cauchy gives a term of the form

`sigma*C(d)^2/[C(d)+sigma*a(d)]`.

This is real information, but I did **not** promote it: when several anchors are combined, that low-degree block can overlap the vertices already credited by other anchors, and I did not find a uniform additive decomposition that beats the entire old `G_multi` envelope. It is a useful secondary route only after one solves the overlap LP.

### B. Direct H2 against the final core

If the connected core has at least `alpha n` vertices, H2 alone implies a degree quantile into it for all but `alpha n` outside vertices, with threshold `kappa lambda/alpha`. This initially looks new. It is not: after averaging, it is exactly the `d=0` member of the same anchor family (when that parameter is admitted), and is dominated by the existing pair-capacity frontier. I therefore reject it as duplicate progress.

### C. Split the absorption reserve into more rounds

As already isolated in an earlier R16 run, if the degree threshold does not improve, splitting `sigma` into `sigma_1+...+sigma_k` changes

`prod_j exp(-sigma_j D)=exp(-sigma D)`

and gives exactly the same attachment exponent. The current gain is not a time-splitting trick; it changes the certified degree threshold itself.

## 11. Nominal Beck--Fiala metric and source status

No R16 novelty is claimed for the nominal scheduler title.

Bansal--Jiang v2 directly proves the conjectured order in the dense-sparsity regime `t>=log^2 n`, but that alone does not settle all `t`, exactly as the owner warned. The stronger current baseline is Guo--Fang--Lu v1:

`boxed: B(t,n)<3 sqrt(2 pi t)`

for every integer `t>=1` and every `n`, with no logarithmic restriction. Karingula--Lovett independently give the larger constant `36` for the stronger Komlos problem. These are current September 2026 preprint/technical-report baselines.

The active CMW source still presents Question 5.1 as open-ended in arXiv:2608.19145v1. This run remains a **PARTIAL** sufficient-condition theorem inside that question. It does not classify all natural graph conditions and does not claim closure, priority, or worldwide novelty.

Supported unchanged-count remains `0` because the frozen active metric moved. No stuck recovery is triggered.

## 12. Next research obligation

The new proof collapses the arbitrary-overlap difficulty further: after full-core averaging, every anchor is a lower quantile constraint on the **same** degree variable `d_W(v)`. The next genuinely new object is therefore not another collection of arbitrary sets but a one-dimensional order-statistic optimization.

The strongest next route is to retain the complete family of constraints

`for every d<dP, the b(d)n smallest degrees into W have total at least
 [aP/a(d)]F_pad(d)lambda n`,

rather than replacing each such sum constraint by one threshold. Optimizing

`sum_v [1-exp(-Delta*d_W(v)/lambda)]`

under that continuum of prefix-sum constraints and the spectral `L2` bound

`sum_v d_W(v)^2 <= lambda^2 |W|`

is a finite-dimensional convex/majorization problem after normalization. If solved exactly, it can absorb part of the remaining `bP n` deficit class and may move the giant fraction beyond the present rectangle-union envelope. A new run should attack that majorization problem directly, not add another checker to the already-moved quantity.

Recommended next Section-B moves: **#11 DUALIZE** the prefix-sum optimization, **#12 FIND WHAT IS CONSERVED** in the degree majorization constraints, and **#24 FIND THE EXTREMAL OBJECT** minimizing the concave attachment functional.

## 13. Model / scheduler control and permission status

The actual runtime identifies this model as GPT-5.6 Sol. The reasoning level is not authenticated, so it is reported as UNVERIFIED. The exposed automation control schema still provides title/prompt, schedule or relative-start fields, timing mode and enablement, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. GPT-6/maximum therefore remains request text only in this environment. Enforcing it requires platform-level scheduler/API fields for model family and reasoning effort plus per-run runtime attestation.

The current root ledger records that P26's historical `You cannot modify this task` failure was authorization-context-specific and that its full update later succeeded in an authorized context. It also records that some other native contexts still reject edits. The compliant workaround for any still-denied task is the owning authorized account/workspace or platform support; do not duplicate the task or bypass permissions.

Per the deployment boundary, this run made **no scheduler change**, no permission change, no workflow execution, no email/Drive action, no purchase, and no public posting. No finite checker was manufactured because the result is analytic and has no finite-enumeration core. This run writes only this own immutable R16 report.

```yaml
ledger_delta:
  track: R16
  source_claim: H0002
  nominal_scheduler_target: Beck-Fiala 1981
  nominal_B_t_n_current_literature_baseline: "B(t,n) < 3 sqrt(2 pi t), every integer t>=1, every n; Guo-Fang-Lu arXiv:2609.11189v1"
  nominal_target_status: KNOWN_CURRENT_PREPRINT_BASELINE
  active_target: "CMW arXiv:2608.19145v1, Question 5.1; frozen H1-H2-H3 sufficient-condition class"
  metric: g_twoaxis(epsilon,rho,kappa)
  before_complete_envelope: "G_multi = a(dP) + finite-anchor layer-cake supremum using R(d)=1-exp[-Delta F_pad(d)/b(d)]"
  after_complete_envelope: "G_coreavg = a(dP) + finite-anchor layer-cake supremum using Rcore(d)=1-exp[-Delta (a(dP)/a(d)) F_pad(d)/b(d)]"
  movement: "STRICT: G_coreavg > G_multi"
  strict_gap: "delta_core = integral_J [m(d0)-M(t)] dt > 0 on a terminal exposed rate-mass arc"
  mechanism: "average the universal pair-capacity inequality over the symmetric orbit of every subanchor inside the connected core before taking degree quantiles"
  supporting_endpoint_fact: "dP<alpha, so bP=alpha-dP>0"
  rejected_routes:
    - "L2 low-degree-block absorption is positive but overlap with old anchor credits prevents a uniform additive gain without a new majorization argument"
    - "direct H2 full-core quantile duplicates the d=0 anchor"
    - "multi-round reserve splitting with unchanged degree threshold leaves the exponential attachment rate unchanged"
  status: PARTIAL_SOURCE_OPEN_LOOKING_ACTIVE
  supported_unchanged_count: 0
  section_B_methods: [9, 14, 27]
  checker: NONE_ANALYTIC
  closure_claimed: false
  independent_audits_claimed: false
```