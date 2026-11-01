Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala existence metric remains a **KNOWN current-preprint baseline** with `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n` on Guo--Fang--Lu arXiv:2609.11189v1; on the active exclusive R16/H0002 successor, the strongest complete bound moves strictly from `G_pad` to the multi-anchor layer-cake envelope `G_multi`, with an explicit two-anchor constant `G_2A` satisfying `G_multi >= G_2A > G_pad` on the unchanged H1--H2--H3 class. Section-B methods actually used: **#2 ATTACK THE NEGATION FIRST, #3 PROVE SOMETHING STRONGER, #13 FIND WHAT ONLY INCREASES**. The preceding triple was #27/#25/#20, so this is not a consecutive repeat.

# R16 — H0002: simultaneous nested anchors reuse one sprinkling round

## 1. Continuity, required reads, ownership, and current-source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1:

> What natural conditions on `G` imply that if `p >= (1+epsilon)/lambda(G)` then with constant probability `G_p` contains a component of size `Omega(|G|)`?

Before new mathematics I reconciled the required state rather than restarting: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H0002 intake row in `probability_1000_intake_H_20260914/problems.jsonl`, the newest own report `runs/R16/2026-09-19T05-56-50Z_h0002-all-padding-quantifier-extension_4d2a.md`, and the newest neighboring R7-07 state. R7-07 is now on the distinct F0012 random-matrix target; its older G0011 CMW line is a different long-cycle question and remains separately claimed/handed off. No competing H0002 ownership was found.

Fresh current checks on 19 Sep 2026 recover CMW only as arXiv:2608.19145v1, submitted 19 Aug 2026; the bounded search did not surface a later source-matching resolution of Question 5.1. That is negative search evidence only, not a worldwide openness or novelty certificate.

Current primary/status URLs checked:

- https://arxiv.org/abs/2608.19145 — CMW source;
- https://arxiv.org/abs/2508.03961 — Bansal--Jiang v2;
- https://arxiv.org/abs/2609.11189 — Guo--Fang--Lu v1, 10 Sep 2026;
- https://eccc.weizmann.ac.il/report/2026/188/ — Karingula--Lovett, 17 Sep 2026.

The nominal Beck--Fiala scheduler title is no longer an unresolved existence target on the stated current manuscripts. Bansal--Jiang v2 prove the conjectured `O(sqrt(t))` order directly for `t>=log^2 n`, with a weaker polylogarithmic-loss estimate below that range. Guo--Fang--Lu v1 state the stronger Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduce

`B(t,n) < 3 sqrt(2 pi t)`

for every integer `t>=1` and every `n`. Karingula--Lovett independently give an elementary Komlos proof with constant `36`. These are extremely recent preprint / technical-report results, not mature refereed consensus; their stated theorems are literature baselines, not R16 novelty.

## 2. Frozen H0002 class and incoming complete bound

Fix `0<epsilon<=1` and fixed `rho,kappa>0`. Write

`n:=|G|`, `lambda:=lambda(G)`,

`h:=1-epsilon/8`,

`q0:=1-exp(-epsilon^2/288)`,

`alpha:=rho*q0/64`,

`s:=1-rho>0`.

The hypothesis class is unchanged:

1. H1: `lambda(G-S) >= h lambda` whenever `|S|<=rho n`;
2. H2: `e_G(X,Y) >= kappa lambda n` for all disjoint `X,Y` with `|X|,|Y|>=alpha n`;
3. H3: `lambda -> infinity`.

Use the established deficient-side parameterization

`a(d):=rho-alpha+d`,

`b(d):=alpha-d`,

so `a(d)+b(d)=rho` and the unused-reservoir density is always `s=1-rho`.

The preceding chain supplies:

- a fixed anchor `d1` with `beta:=alpha-d1>0`, `a1:=a(d1)`;
- the reserve margin `Delta:=epsilon*(7-epsilon)/(8-epsilon)>0`;
- an anchor cut coefficient `Fanc>0` and

  `Ranc:=1-exp[-Delta*Fanc/beta] in (0,1)`;

- the all-padding cut-capacity profile `F_pad(d)`, positive on the certified interval below its first endpoint `d_pad`, with `d_pad>d1`;
- the complete incoming envelope

  `G_pad:=a1+Phi_Ranc(d_pad-d1)`,

  where

  `Phi_R(D)=R*s+D*(1-R)` for `0<=D<=s`,

  `Phi_R(D)=D` for `D>=s`.

The preceding theorem means that every fixed `g<G_pad` satisfies

`P(L1(G_p)>=g n) -> 1`

uniformly on the frozen class for every `p>=(1+epsilon)/lambda`.

It is useful to rewrite this bound in a form that exposes exactly what was discarded. Put

`dP:=d_pad`, `DP:=dP-d1>0`, `aP:=a(dP)=a1+DP`,

`m1:=(s-DP)_+`.

Then directly from the definition of `Phi`,

`boxed: G_pad = aP + Ranc*m1.`

Interpretation: the old proof used the degree quantile from **one anchor**, `a1`, and pessimistically allowed the entire seed-giant head start `DP` to consume high-degree vertices from that one quantile set.

This run removes that one-anchor bottleneck.

## 3. Method #2 — attack the knife-edge obstruction as if it were a real graph

The preceding report isolated a scalar `3 x 3` PSD obstruction at `d_split=s`, suggesting that the next route might be to contradict it using the Perron vector of the residual `R` block.

I tried that negation first. H1 indeed gives `lambda(G[R])>=h lambda` after deleting the other `rho n` vertices, but without a lower bound on `lambda/n` the Perron vector of `G[R]` may localize. The uniform Rayleigh quotient can be only

`2e(R)/(lambda |R|) >= h^2 lambda/(s n)`,

which may vanish under H3. A nonuniform two-vector compression has the same problem: localization can make its coupling to a uniform anchor vanish on the fixed `Theta(lambda n)` scale required by sprinkling.

So this does **not** yield a uniform contradiction on the frozen class. I reject it as the primary route for this run rather than adding another localized spectral lemma.

The failure points to the useful invariant: one should not try to strengthen a single anchor; one should retain several already-certified anchor degree quantiles simultaneously.

## 4. Method #3 — prove a stronger deterministic statement: every certified anchor gives its own reservoir quantile

The fixed-reserve absorption report proved the following degree-quantile lemma. I restate it in the notation needed here.

### Lemma 1 (anchor quantile)

Fix `d<dP` in the certified positive-profile interval, and suppose every disjoint pair `A,B` with

`|A|=a(d)n+o(n)`, `|B|=b(d)n+o(n)`

satisfies

`e(A,B) >= C(d) lambda n-o(lambda n)`

for some fixed `C(d)>0`.

Then for every fixed `theta in (0,1)` and every such `A`, all but fewer than `b(d)n+o(n)` vertices outside `A` have

`d_A(v) >= (1-theta) C(d) lambda/b(d)`.

Hence there is a set `H_d(A) subset V\A` with

`|H_d(A)| >= (s-o(1))n`

such that every `v in H_d(A)` satisfies the displayed degree lower bound.

#### Proof

If `b(d)n+o(n)` vertices outside `A` all had degree below `(1-theta)C(d)lambda/b(d)`, choose `B` from them. Then

`e(A,B)<(1-theta)C(d)lambda n+o(lambda n)`,

contradicting the pair-capacity lower bound. Since

`1-a(d)-b(d)=1-rho=s`,

the number of guaranteed high-degree vertices is at least `(s-o(1))n`. `QED`

For the old anchor set

`C(d1):=Fanc`,

and for every `d in (d1,dP)` we may use

`C(d):=F_pad(d)>0`.

Thus **every** anchor below the endpoint supplies a separate high-degree set of asymptotic density `s`. The previous proof used only the one at `d1`.

## 5. Nested anchors inside one pre-absorption giant

Fix finitely many certified anchors

`d1 = e1 < e2 < ... < ek < dP`.

Later we will take the supremum over all finite choices. First choose a gluing target

`d3 in (ek,dP)`

sufficiently close to `dP`. The established harvesting + genuine-component gluing argument, using the positive cut-capacity profile on the compact interval up to `d3`, produces with probability `1-o(1)` a connected round-one/two seed component `A_*` with

`|A_*| >= (a(d3)-o(1))n`.

Condition on rounds one and two and on such an `A_*`. Choose nested subsets

`A_1 subset A_2 subset ... subset A_k subset A_*`

with

`|A_i|=a(e_i)n+o(n`)

(the rounding typo in this display is harmless; throughout it means `a(e_i)n+o(n)`). The fixed gaps `d3-e_i>0` make this possible for all sufficiently large `n`.

For each anchor let `H_i:=H_{e_i}(A_i)` be supplied by Lemma 1. Since

`|A_*\A_i|/n <= d3-e_i+o(1)`,

at most that many vertices of `H_i` can already have been swallowed by the larger pre-absorption giant. Therefore the set

`S_i:=H_i\A_*`

of still-external high-degree vertices satisfies

`|S_i|/n >= m_i(d3)-o(1)`,

where

`m_i(d3):=[s-(d3-e_i)]_+`.

This is the first monotone quantity: for fixed `d3`, later/larger anchors have larger guaranteed external high-degree mass.

## 6. One sprinkling round can exploit every anchor simultaneously

As in the fixed-reserve theorem, reserve a fixed numerator `sigma<Delta` from the total percolation probability, use an `o(1/lambda)` gluing round, and leave an independent absorption round with

`p_a lambda -> sigma`.

For anchor `e_i`, put

`b_i:=alpha-e_i`,

and choose a fixed `c_i<C(e_i)`. For every `v in S_i`, Lemma 1 gives

`d_{A_i}(v) >= (1-theta)c_i lambda/b_i`.

Since `A_i subset A_*`, the probability that the independent absorption round opens at least one edge from `v` into `A_*` is at least any fixed number below

`r_i(sigma,c_i,theta)
 :=1-exp[-sigma(1-theta)c_i/b_i]`.

The key point is that **no probability reserve is split between anchors**. All anchors are deterministic subsets of the same already-connected `A_*`, and every one is tested against the same independent round-three edge set.

For distinct vertices outside `A_*`, the attachment events use disjoint sets of edges into `A_*`, hence are independent.

## 7. Method #13 — the layer-cake monovariant for overlapping high-degree sets

The sets `S_i` can overlap arbitrarily, so summing their sizes would be invalid. The correct quantity is the lower envelope of attachment probabilities pointwise.

For an outside vertex `v`, let

`p_v := max{r_i: v in S_i}`,

with `p_v=0` if `v` lies in no `S_i`. Its actual attachment probability is at least `p_v` because membership in `S_i` certifies enough edges into the nested anchor `A_i subset A_*`.

Use the layer-cake identity

`sum_{v outside A_*} p_v
 = integral_0^1 | union_{i:r_i>=t} S_i | dt`.

For every `t`, a union contains each set occurring in it, so

`| union_{i:r_i>=t} S_i |
 >= max_{i:r_i>=t} |S_i|`.

Hence

`(1/n) sum p_v
 >= integral_0^1 max_{i:r_i>=t} m_i(d3) dt-o(1)`.

This lower bound is valid for **every possible overlap pattern** among the anchor quantile sets. It is the quantity the one-anchor proof threw away.

Because the actual attachment indicators are independent across outside vertices, a standard Chernoff bound for independent non-identically distributed Bernoulli variables implies that the number of successful attachments is at least

`[ integral_0^1 max_{i:r_i>=t} m_i(d3) dt - o(1) ] n`

with probability `1-o(1)`.

Every successful vertex joins the component containing `A_*`. Therefore the final connected mass is at least

`a(d3)
 + integral_0^1 max_{i:r_i>=t} m_i(d3) dt
 - o(1)`.

This is the multi-anchor absorption lemma.

## 8. Remove all slack and define the new complete envelope

For the old anchor define

`R(d1):=Ranc=1-exp[-Delta*Fanc/beta]`.

For every `d in (d1,dP)` define

`R(d):=1-exp[-Delta*F_pad(d)/(alpha-d)] in (0,1)`.

Also define the endpoint remaining-mass profile

`m(d):=[s-(dP-d)]_+`.

For a finite anchor set

`D={d1=e1<e2<...<ek<dP}`

put

`L(D):=integral_0^1 max_{d in D:R(d)>=t} m(d) dt`,

with the maximum over the empty set interpreted as zero.

Define

`boxed: G_multi
 := a(dP) + sup_{D finite, d1 in D subset [d1,dP)} L(D).`

### Theorem 2 (multi-anchor layer-cake envelope)

For every fixed

`g<G_multi`,

we have

`boxed: P(L1(G_p)>=g n) -> 1`

uniformly on the unchanged H1--H2--H3 class whenever

`p>=(1+epsilon)/lambda(G)`.

#### Proof

Fix `g<G_multi`. Choose a finite anchor set `D` whose displayed value exceeds `g` by a fixed margin. Choose `d3<dP` sufficiently close to `dP`, then choose `sigma<Delta`, `c_i<C(e_i)`, and `theta>0` sufficiently close to their boundary values that the finite-anchor expression in Sections 5--7 still exceeds `g` by half the margin. All parameters are now fixed.

The previously established two-scale harvesting argument works because `sigma<Delta` leaves a fixed positive supercritical margin under H1. The genuine-component gluing argument works up to `d3` because the certified cut profile is uniformly positive on that compact subinterval. Conditional on the resulting connected `A_*`, Sections 5--7 give independent round-three attachment variables and the layer-cake lower bound. Chernoff concentration then gives the claimed component size with failure probability `o(1)`. Finally let the fixed slack choices approach their boundary values. `QED`

No endpoint attainment at `G_multi` is claimed.

## 9. A completely explicit two-anchor strict improvement over the entire incoming envelope

The abstract finite-anchor supremum above is stronger, but strict fixed-metric movement can be seen with exactly two anchors and no optimization ambiguity.

Set

`eta := (1/2) min{dP-d1, s} > 0`,

`d2 := dP-eta`.

Then

`d1<d2<dP`,

`b2:=alpha-d2>0`,

`F2:=F_pad(d2)>0`,

and

`R2:=1-exp[-Delta*F2/b2] in (0,1)`.

Define

`m1:=[s-(dP-d1)]_+`,

`m2:=s-(dP-d2)=s-eta`.

By the choice of `eta`,

`boxed: m2>m1>=0`,

indeed:

- if `dP-d1<=s`, then `m1=s-(dP-d1)` while `m2=s-(dP-d1)/2`;
- if `dP-d1>s`, then `m1=0` while `m2=s/2`.

For two anchors the layer-cake integral is explicit. Put

`A_2(Ranc,R2;m1,m2)
 := Ranc*m1 + R2*(m2-m1)` if `Ranc>=R2`,

and

`A_2(Ranc,R2;m1,m2)
 := R2*m2` if `R2>Ranc`.

This is exactly the worst-overlap lower bound: if the higher attachment rate belongs to the smaller quantile set, nest that set inside the larger one; if the larger quantile set has the higher rate, its contribution alone dominates.

Define

`boxed: G_2A:=a(dP)+A_2(Ranc,R2;m1,m2).`

Then

`boxed: G_2A>G_pad.`

Indeed the incoming envelope is exactly

`G_pad=a(dP)+Ranc*m1`.

If `Ranc>=R2`,

`G_2A-G_pad=R2*(m2-m1)>0`.

If `R2>Ranc`,

`G_2A-G_pad=R2*m2-Ranc*m1
                >Ranc*(m2-m1)>=0`,

with strictness because `R2>0` and `m2>m1`.

Consequently

`boxed: G_multi >= G_2A > G_pad.`

This is strict movement beyond the **entire previous complete envelope**, not merely beyond a midpoint receipt.

A frozen single-number receipt may be taken as

`g_receipt := (G_pad+G_2A)/2`,

for which

`P(L1(G_p)>=g_receipt*n)->1`.

## 10. Why this is a real new route rather than another padding identity

The preceding report exhausted all scalar ways of padding one deficient side with vertices from `A` and `R`. Adding another convex combination of those constraints cannot help at its knife edge.

This run does something different: it keeps **several distinct anchor sizes**, each with its own independently valid degree quantile, and uses the same random absorption round against all of them at once. No scalar padding identity can reproduce the layer-cake gain because the gain comes from retaining the set-valued information `H_d(A)` across different `d` rather than collapsing every anchor to a single cut coefficient.

The two-anchor gain is especially robust: it uses only positivity of `F_pad(d2)`, not a derivative, an endpoint slope, a numerical root estimate, or any assumption that the all-padding endpoint itself moves.

## 11. What moved and status

### Nominal Beck--Fiala metric

No fleet novelty is claimed. Current stated primary literature gives

`B(t,n)<3 sqrt(2 pi t)`

for every integer `t>=1` and every `n` (Guo--Fang--Lu v1). Bansal--Jiang v2's `t>=log^2 n` result is therefore retained only as the comparison requested by the nominal scheduler title.

### Active H0002 metric

Before:

`g_twoaxis >= every fixed g<G_pad`.

After:

`g_twoaxis >= every fixed g<G_multi`,

with the explicit strict chain

`boxed: G_multi >= G_2A > G_pad`.

Status remains **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE**. This is a stronger sufficient-condition theorem inside CMW Question 5.1, not a classification of all natural host-graph conditions and not closure of the source question.

Supported unchanged-count after this run: `0` because the frozen metric moved. No stuck recovery is triggered.

## 12. Next research obligation

The natural next object is no longer the first scalar zero of one cut profile. The multi-anchor theorem turns the problem into an explicit **rate-versus-mass frontier**:

`d -> ( m(d), R(d) )`.

The complete absorption gain is the layer-cake area under the upper frontier of these points. The strongest next routes are therefore:

1. prove monotonicity or concavity properties of `R(d)` to evaluate `G_multi` in closed form;
2. optimize the semialgebraic `F_pad(d)/(alpha-d)` profile and identify which anchors are actually exposed points of the layer-cake frontier;
3. only after that, return to the nonuniform Perron-vector knife-edge if it can move that frontier rather than merely strengthen an already-dominated anchor.

This is a materially different obstruction from the preceding scalar-padding bottleneck.

## 13. Prior-art discipline

The general ingredients here—sprinkling, degree quantiles, nested connected anchors, Chernoff concentration, and layer-cake identities—are standard. I do not claim any one of them as novel. The bounded current search did not locate a later source-matching resolution of CMW Question 5.1 or this exact simultaneous-anchor sufficient-condition theorem. That negative search is not a novelty certificate.

## 14. Model / scheduler control and permissions

The runtime actually identifies this model as GPT-5.6 Sol; the reasoning level is not authenticated, so it is reported as UNVERIFIED. The exposed task-control surface still has no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt. GPT-6/maximum therefore remains request text only in this environment. Enforcing it would require platform-level scheduler/API fields for model family and reasoning effort plus per-run runtime attestation.

The repository records that the historical P26 `You cannot modify this task` error was authorization-context-specific and that a later P26 update succeeded in an authorized context. For any task that still rejects modification, the compliant workaround is the owning authorized account/workspace or platform support, never task duplication or permission bypass.

No scheduler, permission, workflow, email, Drive, purchase, or public-posting change was made. No finite checker was created because the new theorem is analytic and its finite-anchor overlap inequality is proved on the page; there is no finite enumeration claim requiring a checker. This run writes only this own immutable R16 report and does not edit shared roots or peer files.

```yaml
ledger_delta:
  track: R16
  source_claim: H0002
  nominal_scheduler_target: Beck-Fiala 1981
  nominal_B_t_n_current_literature_baseline: "B(t,n) < 3 sqrt(2 pi t), every integer t>=1, every n; Guo-Fang-Lu arXiv:2609.11189v1"
  nominal_target_status: KNOWN_CURRENT_PREPRINT_BASELINE
  active_target: "CMW arXiv:2608.19145v1, Question 5.1; frozen H1-H2-H3 sufficient-condition class"
  metric: g_twoaxis(epsilon,rho,kappa)
  before_complete_envelope: "G_pad = a(d_pad) + Ranc * [s-(d_pad-d1)]_+"
  explicit_after_bound: "G_2A = a(d_pad) + two-anchor layer-cake contribution; G_2A>G_pad"
  after_complete_envelope: "G_multi = a(d_pad) + sup over finite certified anchor sets of layer-cake absorption area"
  movement: "STRICT: G_multi >= G_2A > G_pad"
  mechanism: "simultaneous nested-anchor degree quantiles reuse one independent absorption sprinkling round; overlap handled by layer-cake union lower bound"
  rejected_route: "directly contradict knife-edge scalar quotient with residual Perron vector; localization can erase fixed-scale coupling when lambda/n -> 0"
  status: PARTIAL_SOURCE_OPEN_LOOKING_ACTIVE
  supported_unchanged_count: 0
  section_B_methods: [2, 3, 13]
  checker: NONE_ANALYTIC
  closure_claimed: false
  independent_audits_claimed: false
```