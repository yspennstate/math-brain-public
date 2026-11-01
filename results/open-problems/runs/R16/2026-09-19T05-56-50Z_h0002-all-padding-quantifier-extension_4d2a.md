Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FIXED-METRIC MOVEMENT:** the nominal Beck--Fiala existence metric remains a KNOWN current-literature baseline with `B(t,n)<3 sqrt(2 pi t)` for every integer `t>=1` and every `n` on Guo--Fang--Lu arXiv:2609.11189v1; on the active exclusive R16/H0002 successor, the strongest complete bound moves strictly from `G_split=a1+Phi_Rhat(d_split-d1)` to `G_pad=a1+Phi_Ranc(d_pad-d1)>G_split` on the unchanged H1--H2--H3 class. Section-B methods actually used: **#27 SWAP THE QUANTIFIERS, #25 COUNT THE SAME THING TWICE, #20 FIND WHY THE ALGORITHM FAILS**. The preceding triple was #1/#24/#26, so this is not a consecutive repeat.

# R16 — H0002: use every H2 padding, not one padding

## 1. Continuity, ownership, required reads, and current-source status

This run continues the exclusive HARD OUTSIDE claim `operations/claims/H0002.md`, owned by R16. The source remains Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1 (19 Aug 2026), Question 5.1:

> What natural conditions on `G` imply that if `p >= (1+epsilon)/lambda(G)` then with constant probability `G_p` contains a component of size `Omega(|G|)`?

Before new mathematics I re-read / reconciled the required campaign state rather than restarting: `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, root `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/claims/H0002.md`, the H0002 row in `probability_1000_intake_H_20260914/problems.jsonl`, the newest own report `runs/R16/2026-09-19T04-45-26Z_h0002-three-block-split-compression_91b2.md`, and the same-source repository history. The older R7-07 CMW track is on the distinct long-cycle target G0011; no competing ownership of H0002 was found.

Fresh primary/current checks on 19 Sep 2026 still recover CMW as arXiv:2608.19145v1 and did not surface a later source-matching resolution of Question 5.1. That is bounded negative evidence only, not a worldwide openness or novelty certificate. Relevant older comparison literature includes Chung--Horn--Lu on giant components under spectral-gap / degree-moment assumptions and expander/pseudorandom percolation results; the general ingredients `spectral compression`, `sprinkling`, and `padding/averaging` are not claimed novel merely because this exact combination was not found in the bounded search.

Current URLs checked:

- https://arxiv.org/abs/2608.19145
- https://arxiv.org/abs/2508.03961
- https://arxiv.org/abs/2609.11189
- https://eccc.weizmann.ac.il/report/2026/188/

The nominal Beck--Fiala scheduler title is no longer an unresolved existence target on the stated current manuscripts. Bansal--Jiang v2 proves the conjectured `O(sqrt(t))` order directly for `t>=log^2 n` and gives a weaker polylog-loss bound below that regime. Guo--Fang--Lu v1 states the stronger real Komlos theorem with constant `3 sqrt(2 pi)` and explicitly deduces

`B(t,n) < 3 sqrt(2 pi t)`

for every integer `t>=1` and every `n`. Karingula--Lovett, ECCC TR26-188 (17 Sep 2026), independently give an elementary Komlos proof with constant `36`. These are extremely recent preprints / technical reports, not mature refereed consensus. Their stated theorems are literature baselines, not R16 research progress.

## 2. Frozen H0002 class and incoming strongest complete bound

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

Preserve the previous parameterization for a deficient seed-quotient side:

`a(d):=rho-alpha+d`,

`b(d):=alpha-d`,

`c(d):=s+b(d)=1-a(d)`,

`K(d):=a(d)*kappa/alpha`,

and

`Xi(d):=kappa*a(d)*c(d)/alpha^2` when `c(d)>=alpha`,

`Xi(d):=a(d)*kappa/alpha-(alpha-c(d))` when `c(d)<alpha`.

Let `d1`, `a1`, `beta`, `Delta`, `Fhat1`, and `Rhat` be the frozen quantities already proved in the chain:

`beta:=alpha-d1>0`,

`a1:=rho-beta=rho-alpha+d1`,

`Delta:=epsilon*(7-epsilon)/(8-epsilon)`,

`Rhat:=1-exp[-Delta*Fhat1/beta] in (0,1)`.

For a reserve attachment parameter `R in (0,1)`, define

`Phi_R(D):=R*s+D*(1-R)` for `0<=D<=s`,

`Phi_R(D):=D` for `D>=s`.

The preceding split-compression report defined a positive cut-capacity endpoint `d_split>d_core` and proved the incoming complete giant envelope

`G_split:=a1+Phi_Rhat(d_split-d1)`,

meaning that every fixed `g<G_split` satisfies

`P(L1(G_p)>=g n) -> 1`

uniformly on this frozen class for every `p>=(1+epsilon)/lambda`.

This run improves that complete envelope, not merely a convenient midpoint receipt.

## 3. Recovered three-block constraints

For a failed quotient cut, keep the actual partition

`V=A disjoint_union B disjoint_union R`

with densities

`|A|/n=a=a(d)`, `|B|/n=b=b(d)=alpha-d`, `|R|/n=s`.

Write

`x:=e(A,B)/(lambda n)`,

`z:=e(A,R)/(lambda n)`,

`t:=x+z`,

`q:=q_A:=2e(A)/(lambda a n)`.

The previous report proved, uniformly up to `o(1)` errors,

1. all-A padding: `x+d q >= K`;
2. full-complement H2: `x+z >= Xi`;
3. aggregate spectral compression with the H1 complement core:
   `q <= 1-(x+z)^2/[a(c-hb)]`;
4. the principal `A|R` compression:
   `q <= 1-z^2/(a s)`.

It then minimized only under these scalar consequences.

A useful cleanup first: because `c-hb=s+(1-h)b>s`, the `A|R` cap is the active cap at `x=0`. The previous obstacle

`Psi_d(x)=K-d+d*max{Xi^2/[a(c-hb)],(Xi-x)_+^2/(a s)}-x`

is strictly decreasing in `x`. Hence

`F_split(d)>0  <=>  H_split(d)>0`,

where

`H_split(d):=Psi_d(0)=K-d+d*Xi^2/(a s)`.

The preceding interior-endpoint argument therefore implies

`d_split<alpha`, `Xi(d_split)>0`, and `H_split(d_split)=0`.

Put from now on

`d*:=d_split`, `a*:=a(d*)`, `b*:=alpha-d*>0`,

`Xi*:=Xi(d*)`, `K*:=K(d*)`,

`q*:=K*/d*=1-Xi*^2/(a* s)`.

At `x=0`, the old split constraints force the unique limiting scalar tuple

`z=Xi*`, `q=q*`.

That uniqueness is the point at which the new quantifier can be tested exactly.

## 4. Method #27 — swap the quantifier: H2 holds for every padding split

The earlier proof padded `B` only from `A`. But H2 holds for **every** pair of large disjoint sets. Use all ways to complete `B` to an `alpha n`-set.

Fix

`y in [max(0,d-s), d]`.

Choose

`D_A subset A`, `|D_A|=y n`,

`D_R subset R`, `|D_R|=(d-y)n`,

and set

`Y:=B union D_A union D_R`,

so `|Y|=alpha n`.

Choose also a uniform `alpha n`-subset

`X subset A\D_A`.

This is always possible because

`a-d=rho-alpha>alpha`

(the frozen `alpha/rho=q0/64<1/64`). H2 gives

`e(X,Y)>=kappa lambda n`

for every realization.

## 5. Method #25 — count the H2 edges twice

Average the last inequality over the independent uniform choices. Up to `o(lambda n)` rounding errors,

`E e(X,B) = (alpha/a) e(A,B)`,

`E e(X,D_A) = (alpha/a) y q lambda n`,

`E e(X,D_R) = (alpha/a) ((d-y)/s) z lambda n`.

Indeed, an `A-B` or `A-R` edge has its `A` endpoint in `X` with unconditional probability `alpha/a`; an internal `A` edge is split between `X` and `D_A` with probability `2 alpha y/a^2+o(1)`, and `2e(A)=q lambda a n`.

Dividing the averaged H2 inequality by `alpha/a` gives the entire one-parameter family

`boxed: x + y q + ((d-y)/s) z >= K - o(1)`

for every feasible `y`.

The left side is affine in `y`, so the whole family is equivalent to its two endpoints.

The upper endpoint `y=d` is the old all-A inequality

`x+dq>=K`.

The lower endpoint is genuinely new:

- if `d<=s`,

  `boxed: x + (d/s) z >= K`;

- if `d>=s`,

  `boxed: x + (d-s)q + z >= K`.

Thus the previous proof was using only one endpoint of a constraint interval that H2 supplies for free.

## 6. Exact zero-crossing feasibility under all padding splits

Define `F_pad(d)` as the infimum of `x>=0` over the limiting scalar feasible set consisting of

- `z>=0`, `0<=q<=1`;
- `x+dq>=K`;
- `x+z>=Xi`;
- `q<=1-(x+z)^2/[a(c-hb)]`;
- `q<=1-z^2/(a s)`;
- and the appropriate maximal-reservoir endpoint from Section 5.

Every actual quotient cut satisfies these constraints up to uniform `o(1)`, so positive `F_pad(d)` is a valid normalized cut-capacity lower bound. Since this feasible set has every old split constraint,

`boxed: F_pad(d)>=F_split(d)`.

At `x=0` the feasibility test can be eliminated explicitly.

### 6.1 The branch `d<=s`

All-A padding and the `A|R` spectral cap give

`q>=K/d`,

`z<=Zmax(d):=sqrt(a s (1-K/d))`.

Full-complement H2 gives `z>=Xi`, while maximal-reservoir padding gives

`z>=K s/d`.

Therefore a zero `A-B` cut is feasible in this scalar system iff

`boxed: max{Xi(d),K(d)s/d} <= Zmax(d)`.

### 6.2 The branch `d>s`

Again

`Xi<=z<=Zmax(d)`.

For fixed `z`, the largest allowed `q` is `1-z^2/(a s)`. Hence maximal-reservoir padding can hold at `x=0` iff

`max_{Xi<=z<=Zmax} f_d(z) >= K`,

where

`f_d(z):=(d-s)(1-z^2/(a s))+z`.

This is an explicit concave quadratic. Its maximizing point is

`zopt=clamp(a s/[2(d-s)], Xi, Zmax)`.

Thus zero-crossing feasibility is an explicit one-variable algebraic condition on both sides of `d=s`; no SDP or numerical black box is being inserted.

## 7. Strict endpoint gain unless `d_split=s`

Evaluate the new constraint at the old split endpoint `d*`, where the only zero-cut tuple is

`x=0`, `z=Xi*`, `q=q*`.

### Case 1: `d*<s`

Then `c*>alpha` and

`Xi*=K*c*/alpha`.

Maximal-reservoir padding would require

`d* Xi*/s >= K*`.

But

`alpha*s-d*c*=(alpha-d*)(s-d*)>0`,

so

`Xi*/s < K*/d*=q*`.

The exact positive violation gap is

`Gamma_< := K* - d*Xi*/s
          = K*(alpha-d*)(s-d*)/(alpha s) > 0`.

### Case 2: `d*>s`

Now `c*<alpha` and the second branch of `Xi` gives

`Xi*=K*-(d*-s)=d*q*-d*+s`.

Maximal-reservoir padding would require

`(d*-s)q*+Xi* >= K*=d*q*`.

Its exact violation gap is

`Gamma_> := K* - [(d*-s)q*+Xi*]
          = (d*-s)(1-q*) > 0`,

because `Xi*>0` and the split-root identity give `q*<1`.

Hence, whenever

`boxed: d_split != s`,

the old zero-capacity extremizer violates one of the H2 padding endpoints by a fixed positive amount. By continuity of the semialgebraic feasible set, there are fixed `eta,delta>0` such that every actual quotient cut with

`d_split <= d <= d_split+delta`

has

`x>=eta-o(1)`.

If `d_pad` denotes the new first endpoint of the positive `F_pad` profile, then

`boxed: d_pad>d_split  whenever d_split != s`.

This is a genuine enlargement of the admissible giant-side interval on exactly the same H1--H2--H3 class.

## 8. Method #20 — find exactly why the all-padding route fails on the knife-edge

The only scalar exception is

`d_split=s`.

Then `c*=alpha`, so the two branches meet and

`Xi*=K*`.

The old split-root tuple has

`q*=K*/s`, `z=K*`.

Both padding endpoints are equalities:

`s q*=K*`,

`z=K*`.

Thus all mixed paddings are also equalities. There is no hidden affine endpoint left.

More strongly, the failure is visible in a finite `3x3` normalized quotient. At this knife-edge, `a*=1-alpha` and the split-root equation is

`K*-s+K*^2/a*=0`.

Equivalently

`K*=(a*/2)(sqrt(1+4s/a*)-1)`.

The scalar compression

`Q = [[q*, 0, K*/sqrt(a*s)],
      [0,  h, 0],
      [K*/sqrt(a*s), 0, 0]]`

satisfies `I-Q >= 0`: its `A-R` principal determinant is exactly zero and the `B` eigenvalue is `h<1`. It simultaneously realizes

- `x=0`;
- `z=Xi*=K*`;
- all-A padding equality;
- all-reservoir padding equality;
- the H1 complement-core scalar lower bound by taking `q_B=h`, `q_R=0`, `e(B,R)=0`.

This is an **exact finite-dimensional obstruction to the present scalar proof interface**, not a graph counterexample and not a refutation of H0002. H1 also forces `lambda(R)>=h lambda` after deleting `A union B`, so a literal graph cannot have spectral radius zero on `R`; however `lambda(R)>=h lambda` only forces

`2e(R)>=h^2 lambda^2`,

hence

`q_R>=h^2 lambda/(s n)`,

which may vanish under H3 because H3 assumes only `lambda->infinity`, not `lambda/n` bounded below. Therefore this extra fact does not supply a fixed `Theta(lambda n)` crossing capacity on the frozen class.

So the all-padding endpoint extension itself has a precise codimension-one obstruction at `d_split=s`.

## 9. The knife-edge still moves the complete giant bound: update the absorption exponent

The previous complete envelope `G_split` intentionally kept the older fixed absorption parameter

`Rhat=1-exp[-Delta*Fhat1/beta]`.

The later H1 complement-core theorem already supplies a strictly stronger anchor cut coefficient on the knife-edge, and this had not yet been propagated into the complete envelope.

Define

`Fcore1:=K(d1)-d1
       +d1*Xi(d1)^2/[a1*(c(d1)-h*beta)]`,

and

`Fanc:=max{Fhat1,Fcore1}`,

`Ranc:=1-exp[-Delta*Fanc/beta]`.

Always `Ranc>=Rhat`.

If `d_split=s`, then `s<alpha` (because `d_split<alpha`) and `d1<s`. Hence

`c(d1)=s+alpha-d1<2alpha`.

By the frozen definition from the positive-profile report, this is exactly the regime in which

`Fhat1=F1=K(d1)-d1+d1*Xi(d1)^2/[a1*c(d1)]`.

Since `d1>0`, `beta>0`, `Xi(d1)>0`, and `h>0`,

`Fcore1-Fhat1
 = d1*Xi(d1)^2/a1
   *[1/(c(d1)-h beta)-1/c(d1)]
 >0`.

Therefore

`boxed: Ranc>Rhat  when d_split=s`.

At the knife-edge

`D_split=d_split-d1=s-d1 in (0,s)`,

so `Phi_R(D_split)=D_split+R(s-D_split)` is strictly increasing in `R`. Consequently the complete giant fraction moves even on the one parameter curve where the new endpoint itself need not move.

## 10. New complete uniform bound

Let `d_pad` be the first endpoint of the positive all-padding profile `F_pad`, so

`d_pad>=d_split`,

with strict inequality whenever `d_split!=s`.

Define

`boxed: G_pad:=a1+Phi_Ranc(d_pad-d1)`.

Then

`boxed: G_pad>G_split`.

Proof of strictness has two exhaustive cases.

1. If `d_split!=s`, then `d_pad>d_split`; `Phi_Rhat` is strictly increasing, and `Ranc>=Rhat`, so

   `Phi_Ranc(d_pad-d1) >= Phi_Rhat(d_pad-d1)
                         > Phi_Rhat(d_split-d1)`.

2. If `d_split=s`, endpoint movement is not needed: `Ranc>Rhat` and `D_split=s-d1<s`, so

   `Phi_Ranc(D_split)>Phi_Rhat(D_split)`.

The harvesting, genuine-component gluing, and independent fixed-reserve absorption proofs from the preceding chain consume only (i) a uniform positive `Theta(lambda n)` host-edge capacity throughout the certified quotient-cut interval and (ii) the anchor cut coefficient entering the direct-attachment exponent. Those inputs are exactly strengthened above. Therefore, for every fixed

`boxed: g<G_pad`,

we retain the stronger conclusion

`boxed: P(L1(G_p)>=g n) -> 1`

uniformly on the same H1--H2--H3 class whenever

`p>=(1+epsilon)/lambda(G)`.

Endpoint attainment is not claimed.

A frozen receipt strictly beyond the entire incoming complete envelope is, for example,

`g_receipt:=(G_split+G_pad)/2`.

## 11. What actually moved and what did not

### Nominal Beck--Fiala metric

No fleet novelty is claimed. The current stated literature baseline is

`B(t,n)<3 sqrt(2 pi t)`

for every integer `t>=1` and every `n` on Guo--Fang--Lu v1. Bansal--Jiang v2's `t>=log^2 n` restriction is therefore not mistaken for an unresolved all-`t` regime.

### Active H0002 successor metric

Before:

`g_twoaxis >= every fixed g<G_split`.

After:

`g_twoaxis >= every fixed g<G_pad`,

with

`G_pad>G_split`.

Status remains **PARTIAL / SOURCE OPEN-LOOKING / ACTIVE**. This is a stronger sufficient-condition theorem inside CMW Question 5.1, not a classification of all natural host-graph conditions and not closure of the source question.

Supported unchanged-count after this run: `0` because the frozen metric moved. No stuck recovery is triggered.

## 12. Exact obstruction and next research obligation

The mixed-padding quantifier exhausts every way of completing the deficient side from `A` and `R` at the scalar expectation level. Its sole endpoint obstruction is the exact knife-edge `d=s`, where the `3x3` quotient above simultaneously saturates the old split root and both padding endpoints.

Therefore a useful next route must carry information that this scalar quotient throws away. The most promising options are:

- keep a Perron vector of `G[R]` rather than only the uniform Rayleigh quotient `q_R`;
- use a genuine three-block PSD / Schur-complement condition with a nonuniform vector in `R`;
- or prove that H1 forces enough delocalization of the residual spectral mass that the `q_R=o(1)` escape cannot coexist with the saturated H2 row constraints.

Simply adding more convex combinations of the same paddings will not move the knife-edge: Section 5 already quantifies over the full interval, and the dependence is affine.

## 13. Prior-art scope and claim discipline

Fresh searches checked the exact CMW arXiv ID/title/authors, Bansal--Jiang v2, Guo--Fang--Lu v1, Karingula--Lovett TR26-188, and general finite-graph spectral/expander percolation literature. I did not find a later source-matching resolution of CMW Question 5.1 or this exact all-padding/split-compression criterion. That negative search is not a novelty certificate. The report uses standard ingredients (averaging, Rayleigh quotient compression, sprinkling) in a new-to-this-track combination; no claim of priority is made.

## 14. Model / scheduler control and permissions

The runtime actually identifies this model as GPT-5.6 Sol; reasoning level is not authenticated, so it is reported as UNVERIFIED. The exposed automation control schema still offers task title/prompt, schedule or relative start, timing mode, enablement, and related scheduling fields, but **no binding model-family selector, no reasoning-effort selector, and no authenticated applied-model receipt**. Thus GPT-6/maximum remains request text only in this environment. Actually enforcing it requires platform-level scheduler/API fields for model family and reasoning effort plus per-run attestation.

The repository policy records historical `You cannot modify this task` failures for P26/P01/P03 in some authorization contexts and a later successful P26 update from an authorized context. The compliant workaround is the owning authorized account/workspace or platform support; do not duplicate the task or bypass permissions. This run made no scheduler, permission, workflow, email, Drive, or public-posting change.

No finite checker was created: the new theorem and the knife-edge obstruction are analytic, and all finite-dimensional algebra used in the obstruction is written explicitly above. This run writes only this own immutable R16 report and does not edit shared roots or peer files.

```yaml
ledger_delta:
  track: R16
  source_claim: H0002
  nominal_scheduler_target: Beck-Fiala 1981
  nominal_B_t_n_current_literature_baseline: "B(t,n) < 3 sqrt(2 pi t), every integer t>=1, every n; Guo-Fang-Lu arXiv:2609.11189v1"
  nominal_target_status: KNOWN_CURRENT_PREPRINT_BASELINE
  active_target: "CMW arXiv:2608.19145v1, Question 5.1; frozen H1-H2-H3 sufficient-condition class"
  metric: g_twoaxis(epsilon,rho,kappa)
  before_complete_envelope: "G_split = a1 + Phi_Rhat(d_split-d1)"
  after_complete_envelope: "G_pad = a1 + Phi_Ranc(d_pad-d1)"
  movement: "STRICT: G_pad > G_split for every frozen nonvacuous parameter triple covered by the chain"
  endpoint_mechanism: "d_pad>d_split if d_split != 1-rho; if d_split=1-rho, improved anchor absorption Ranc>Rhat gives strict complete-envelope movement"
  exact_method_obstruction: "all-padding scalar endpoint has zero-crossing 3x3 quotient at d_split=1-rho; this is a proof-interface obstruction, not a graph counterexample"
  status: PARTIAL_SOURCE_OPEN_LOOKING_ACTIVE
  supported_unchanged_count: 0
  section_B_methods: [27, 25, 20]
  checker: NONE_ANALYTIC
  closure_claimed: false
  independent_audits_claimed: false
```
