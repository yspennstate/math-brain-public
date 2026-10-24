Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

# P03 / P0456 run report — normal-transition ordered race at the sqrt(log n) scale

**NEW FINER-SCALE BASELINE ADMITTED.** The already admitted metrics remain saturated and are not counted as stuck:

- `c_LK^cert=0` at scale `sqrt(log n) log log n`;
- `a_LK^fine=0` at scale `sqrt(log n log log n)`.

This run proves a theorem at the next scale `V_n=sqrt(log n)` and therefore admits a new fleet proof-frontier metric

`b_LK^sqrt := max(b_-,b_+)`,

where `b_-` and `b_+` are the smallest nonnegative fixed coefficients currently certified by source-valid theorems for, respectively,

`k <= log n -(b_-+epsilon) sqrt(log n)` implying disconnection whp,

and

`k >= log n +(b_++epsilon) sqrt(log n)` implying connectivity whp,

for every fixed `epsilon>0`. Lower is better. This is a **fleet proof-frontier metric**, not a threshold constant asserted by Dabirian--Subramanian and not a claim about the true critical window.

No previous numerical baseline existed at this scale. The prior state was `UNMEASURED`; the theorem below establishes the current certified baseline

`b_LK^sqrt = C_*`,

where

`C_* = e phi(Phi^{-1}(e^{-1})) = 1.0244099529838058...`

and `phi,Phi` are the standard-normal density and CDF. This is baseline admission, not a fake `0 -> number` movement. Fine-scale unchanged count starts at `0`; HARD recoveries remain `0/2`.

Main new claim:

`P03-P0456-NORMAL-RACE-SQRTLOG-BRACKET-284 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED`.

For every fixed `b<-C_*`, if

`k <= log n + b sqrt(log n)`,

then `LK(n,k)` is disconnected with high probability. For every fixed `b>C_*`, if

`k >= log n + b sqrt(log n)`,

then `LK(n,k)` is connected with high probability.

This does **not** decide the band `[-C_*,C_*]`, coefficient zero, a limiting connectivity law, or publication novelty.

The three Section-B methods used substantively are **B6 DEFORM TO A POINT YOU CAN SOLVE, B13 FIND WHAT ONLY INCREASES, B27 SWAP THE QUANTIFIERS**.

---

## 1. Continuity, repository state, and source status

The canonical exclusive assignment remains `operations/claims/P0456.md` (creation `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`). I continued from

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T09-27-56Z__p0456-ordered-deadline-fine-zero.md`

(creation `d68ddf35e79ef6cb2c2f0977351440f40230eab3`, blob `db54ff4dc10a0be29dc8c2b6a04da0a1743b5aa9`) and preserve Claims 274, 276, 278, 280 and 282.

Repository continuity this invocation recovered/reread the root README, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, `operations/FLEET_2026-09-16.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current P0456 claim, the newest own report, and neighboring P0457 state for nonduplication. Large connector surfaces are truncated, so I do **not** claim byte-for-byte reread of every large ledger; exact-path reads and targeted searches were used. P0457 remains a distinct diameter target.

The primary source was freshly rechecked on 2026-09-18, including PDF page images:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, Journal of Applied Probability 63(2) (June 2026), 552--579, DOI `10.1017/jpr.2025.10051`, Section 1.1.

The paper states that for

`log n -(1/2) log log n sqrt(log n) <= k <= log n +(1/2) log log n sqrt(log n)`

it does not know whether connectivity holds, and says sharper or exact sufficient conditions could close the gap. The literal source proof structure relevant here remains: Lemma 10 gives the rare bad-pair event, Lemmas 11--14 use a multitype permutation and conditional independence on the complement, and Theorem 4 treats fixed low degree through the same preferred-neighbor rejection structure.

A bounded current-literature search on 2026-09-18 for the exact title, authors, DOI, `LK(n,k)`, and later bilateral-preference connectivity work recovered the Cambridge article and adjacent random-graph literature but no later theorem matching this sharpened connectivity-window question. This is dated bounded negative evidence only, **not** proof of worldwide openness or publication novelty.

---

## 2. Idea before calculation: deform the ordered race into its normal transition

Claim 282 used

`s = c sqrt(k/log k)`

with fixed `c`, so the source deletion shift

`K=k-s-O(1)`

was lower order than `sqrt(k log k)`. That argument could make the fixed coefficient at the `sqrt(k log k)` scale arbitrarily small by choosing `c` after the coefficient was fixed, but it said nothing quantitative at the next `sqrt(k)` scale.

The natural deformation is

`s = lambda sqrt(k)+O(1)`

with a fixed `lambda>0`. Then `K=k-s-O(1)` changes `-K` by `+lambda sqrt(k)`, so the shift must be retained. At the same time the key Gamma positive-part function

`A_K(T)=E[(T-G_K)_+]`,  `G_K~Gamma(K,1)`,

enters its central-limit transition when

`T=K+x sqrt(K)`.

B6 deforms the solved small-cutoff race into this normal transition. B13 identifies a strictly increasing Mills-ratio quantity that makes the variational optimizer unique. B27 checks the quantifier issue explicitly: at the `W_n` scale one could choose a large fixed `c` after fixing the window coefficient; at the `sqrt(log n)` scale the cutoff ratio `lambda=s/sqrt(k)` has an order-one variational optimum, so swapping to a single slowly growing cutoff cannot make the correction vanish.

I first tried to refute the possibility of a positive limiting constant by sending `lambda` to zero or infinity. Both ends make the resulting coefficient worse: the variational optimizer moves into a normal tail and the coefficient diverges. Thus the route predicts a genuine interior proof-route constant rather than another zero fixed-coefficient frontier.

---

## 3. Normal-transition ordered-race lemma

### Lemma 284A

Fix `lambda>0` and an integer `h>=0`. Let `K -> infinity`,

`s=lambda sqrt(K)+o(sqrt(K))`,

and `r=s-h`. In the independent rate-one Poisson race representation of the source type permutation, let `T_d` be the `d`th arrival time of type 0. For a required nonzero type, success at deadline `d` means at least `K` arrivals before `T_d`. If at most `h` of the first `s` deadline constraints may be omitted, then

`log P(simultaneous ordered-deadline success)`

is at most

`-K + (H(lambda)+o(1)) sqrt(K)`,

where

`H(lambda)=sup_{x in R} {-x + lambda[1+log(a(x)/lambda)]}`

and

`a(x)=phi(x)+x Phi(x)=E[(x-Z)_+]`,  `Z~N(0,1)`.

The same bound holds for the exact finite source type permutations in the P0456 pair-isolation and fixed-low-degree applications.

### Proof

Claim 282 proved, before specializing the cutoff size, the exact ordered-deadline integral inequality

`J_{K,s,h} <= C_h/r! int_0^infty e^{-T}(1+T^h) A_K(T)^r dT`,       (1)

where

`A_K(T)=E[(T-G_K)_+]`

and `G_K~Gamma(K,1)`. The extremal omitted-deadline step used there remains exact: because both `T_d` and `F_K(T_d)=P(G_K<=T_d)` increase with `d`, the largest probability among all sets of `s-h` enforced deadlines is obtained by omitting the earliest `h` deadlines.

Set

`T=K+x sqrt(K)`.

Since `G_K` is a sum of `K` iid Exp(1) variables, Berry--Esseen gives convergence of `(G_K-K)/sqrt(K)` to `Z~N(0,1)`. The standardized Gamma variables have uniformly bounded second moments, so the positive-part expectations are uniformly integrable. Hence, uniformly for `x` in every compact interval,

`A_K(K+x sqrt(K))/sqrt(K) -> E[(x-Z)_+]`

`= phi(x)+x Phi(x)=a(x)`.                                  (2)

Stirling gives, because `r=lambda sqrt(K)+o(sqrt(K))`,

`log r! = r log r-r+o(sqrt(K))`.

Insert (2) into (1). All fixed polynomial factors have logarithm `o(sqrt(K))`, and on a compact `x`-set the normalized logarithm becomes

`-K + sqrt(K){-x + lambda[1+log(a(x)/lambda)]}+o(sqrt(K))`. (3)

It remains to justify taking the supremum over all real `x`. For `x>=0`,

`A_K(K+x sqrt(K)) <= sqrt(K)+x sqrt(K)`

by `E|G_K-K|<=sqrt(K)`, so the exponent in (1) tends to `-infinity` after division by `sqrt(K)` as `x->+infinity` because of the `-x` term. For `x<=-1`, the moderate-deviation estimate already proved in Claim 282 gives, uniformly until the far Chernoff region,

`A_K(K+x sqrt(K))/sqrt(K) <= C |x|^{-2} exp(-x^2/2)`;

the far-left region is even smaller by the ordinary Gamma/Poisson Chernoff bound. Hence the normalized exponent also tends to `-infinity` as `x->-infinity`. We may therefore first restrict to a fixed large compact set, use (2)--(3), and then let the compact set grow. Laplace's upper bound yields

`log J_{K,s,h} <= -K +(H(lambda)+o(1))sqrt(K)`.             (4)

For the source finite permutations, take the same deterministic relevant prefix as in Claim 282,

`R=6(s+1)K=O(K^{3/2})`.

The probability that the `s`th type-0 object has not appeared by that prefix is `exp[-Omega(K)]`, with a fixed constant made larger than 1 by the factor 6. On the complementary event the relevant success event is determined by the prefix. Every projected word of length at most `R` has exact without-replacement probability divided by its equal-probability iid-word probability

`exp[O(R^2/n+Rs/n)]=1+o(1)`,

because here `K=O(log n)` and `R=O((log n)^{3/2})`. Thus (4) transfers with the same `sqrt(K)` coefficient. This proves Lemma 284A. `square`

---

## 4. Solving the variational problem exactly

The derivative identity

`a'(x)=Phi(x)`                                                     (5)

follows immediately from `a(x)=phi(x)+x Phi(x)`.

For fixed `lambda`, an interior maximizer of the function in Lemma 284A satisfies

`-1 + lambda Phi(x)/a(x)=0`,

or equivalently

`g(x):=a(x)/Phi(x)=lambda`.                                      (6)

Write the inverse Mills ratio

`m(x)=phi(x)/Phi(x)`.

Then

`g(x)=x+m(x)`.

A direct differentiation gives

`g'(x)=1-m(x)g(x)`.                                              (7)

There is also a probabilistic interpretation that fixes the sign without a delicate Mills-ratio estimate. For `Z~N(0,1)`,

`E[Z | Z<=x]=-m(x)`

and

`Var(Z | Z<=x)=1-xm(x)-m(x)^2=1-m(x)g(x)=g'(x)>0`.              (8)

Thus `g` is strictly increasing. Standard Mills asymptotics give `g(x)->0` as `x->-infinity` and `g(x)->infinity` as `x->+infinity`. Therefore (6) has a unique solution `x_lambda` for every `lambda>0`, and the supremum in `H(lambda)` is uniquely attained there.

At the optimizer,

`a(x_lambda)=lambda Phi(x_lambda)`,

so

`H(lambda)=-x_lambda+lambda[1+log Phi(x_lambda)]`.              (9)

Now restore the source parameter. In both source applications,

`K=k-s-O(1)=k-lambda sqrt(k)+o(sqrt(k))`,

and `sqrt(K)=sqrt(k)+o(1)`. Therefore Lemma 284A becomes

`log P(race) <= -k +(C(lambda)+o(1))sqrt(k)`,                   (10)

where

`C(lambda)=lambda+H(lambda)`.                                  (11)

B13 now gives the exact monotonicity needed to optimize `lambda`. By the envelope theorem and (9),

`H'(lambda)=log Phi(x_lambda)`,

so

`C'(lambda)=1+log Phi(x_lambda)`.                              (12)

Because `x_lambda` is strictly increasing, `C'` is strictly increasing. Hence the unique global minimizer satisfies

`Phi(x_*)=e^{-1}`.                                              (13)

Let

`x_* = Phi^{-1}(e^{-1})`,

`lambda_* = g(x_*)=x_*+phi(x_*)/Phi(x_*)`.

At (13), `1+log Phi(x_*)=0`, so (9)--(11) collapse to

`C_* = lambda_*-x_* = phi(x_*)/Phi(x_*)`

`= e phi(Phi^{-1}(e^{-1}))`.                                  (14)

Numerically,

`x_*=-0.33747496376420244...`,

`lambda_*=0.6869349892196033...`,

`C_*=1.0244099529838058...`.

The exact expression (14), not the decimal, is the theorem constant.

This also resolves the B27 quantifier issue for this proof route. At the previous `sqrt(k log k)` scale one could choose an arbitrarily large **fixed** `c` after fixing a nonzero window coefficient. At the present scale, `s/sqrt(k)` converges to the order-one parameter `lambda`, and (12)--(14) show that no choice of a single `lambda` or slowly drifting route within this normal-transition asymptotic makes the coefficient vanish: the optimal coefficient is the positive constant `C_*`.

---

## 5. Disconnection below `log n-C_* sqrt(log n)`

Let `I_v` be the isolation event and

`p_n=P(I_v)`.

Claim 278 proved the exact source-valid lower bound

`p_n >= (1-k/(n-k))^(n-1)=exp[-k-o(1)]`                       (15)

for `k=O(log n)`.

Assume

`k=log n+b sqrt(log n)+O(1)`

with fixed `b<-C_*`; monotonicity handles all smaller `k`.

The source bad event `B` satisfies

`P(B)=O(k^3/n)`.                                               (16)

In the source Lemma-11 bad-side decomposition, isolation forces all but at most one of the first `s` relevant neighbors to acquire

`K=k-s-O(1)`

own-type arrivals before their **individual** type-0 deadlines. Choose

`s=lambda_* sqrt(k)+O(1)`.

By (10)--(14), the race contribution is at most

`exp[-k+(C_*+o(1))sqrt(k)]`.

Combining with (16), exactly as in the source Lemma-12 decomposition,

`P(I_1 I_2 cap B)`
` <= exp[-log n-k+(C_*+o(1))sqrt(k)]`.                        (17)

Divide by (15)^2. Since `sqrt(k)=(1+o(1))sqrt(log n)`,

`P(I_1 I_2 cap B)/p_n^2`
` <= exp[(b+C_*+o(1))sqrt(log n)] -> 0`.                      (18)

Also

`P(I_1 cap B)/p_n <= P(B)/p_n`
` <= exp[(b+o(1))sqrt(log n)] -> 0`,                          (19)

because `b<0`. Hence conditioning on `B^c` changes the isolation marginal by `1+o(1)`. The source Lemma 13 gives exact conditional independence on `B^c`, and therefore

`P(I_1I_2)=p_n^2(1+o(1))`.                                   (20)

Finally

`n p_n >= exp[-b sqrt(log n)-o(sqrt(log n))] -> infinity`.   (21)

The source second-moment argument now yields an isolated vertex whp. Thus `LK(n,k)` is disconnected whp for every fixed `b<-C_*`.

---

## 6. Connectivity above `log n+C_* sqrt(log n)`

Assume

`k=log n+b sqrt(log n)+O(1)`

with fixed `b>C_*`.

Fix an integer `kappa>=0`. Repeat the source Theorem-4 rejection setup with

`s=lambda_* sqrt(k)+O(1)`.

If `deg(v)<=kappa`, at least `s-kappa` of the first `s` preferred neighbors reject `v`; each such rejection imposes the same ordered-deadline requirement with

`K=k-s-O(1)`.

There are only

`sum_{j=0}^kappa binom(s,j)=s^{O_kappa(1)}`

choices of omitted constraints, whose logarithm is `o(sqrt(k))`. Lemma 284A and (14) therefore give

`P(deg(v)<=kappa)`
` <= exp[-k+(C_*+o(1))sqrt(k)]`.                              (22)

A union bound over vertices yields

`P(exists v: deg(v)<=kappa)`
` <= exp[(-b+C_*+o(1))sqrt(log n)] ->0`.                      (23)

Take `kappa=5`. Then whp there is no component of size at most 6.

For completeness, the retained component argument from Claim 282 applies unchanged because the present perturbation is only `O(sqrt(log n))=o(log n)`. In iid Exp(1) edge scores (larger means higher preference), let

`m=log((n-1)/k)`, `C=log(32/5)`.

With probability `1-o(1)`, every kth-largest incident score lies in `[m-C,m+C]`: at the upper endpoint the exceedance mean is `(5/32)k` and the Chernoff exponent is greater than `k`, while at the lower endpoint the mean is `(32/5)k` and the corresponding lower-tail exponent is also greater than `k`; a union bound over `n` vertices succeeds for `k=log n+o(log n)`.

On this event put

`p_tree=(32/5)k/(n-1)`,  `p_cross=(5/32)k/(n-1)`.

If a fixed `r`-set is a component, some spanning tree has all `r-1` tree-edge scores above the lower threshold and all `r(n-r)` crossing-edge scores below the upper threshold. These edge sets are disjoint, so by Cayley's formula

`P(exists an r-component)`
` <= binom(n,r) r^(r-2) p_tree^(r-1)(1-p_cross)^(r(n-r)) + o(1)`. (24)

For every fixed `r`, the logarithm of the main term is

`[1-(5/32)r] log n + O_r(log log n+sqrt(log n))`,

which tends to `-infinity` for `r=7,...,12`. For `13<=r<=n/2`, the same estimate gives

`P(exists such a component)`
` <= n/sqrt(2pi) sum_{r=13}^{floor(n/2)}`
` exp{r[1+log(n p_tree)-n p_cross/2+o(1)]}+o(1)`.             (25)

The bracket is

`-(5/64+o(1))log n`.

Choose fixed `delta` with `1/13<delta<5/64`; the geometric sum is `o(1)` because `13 delta>1`. Together with (23), whp no component has size `1<=r<=n/2`, so the graph is connected. Monotonicity in `k` gives the asserted theorem for every larger `k`.

This completes Claim 284. `square`

---

## 7. Formal metric admission

The theorem supplies a genuine source-matching baseline at a scale where the previous state was UNMEASURED. I therefore formally admit

`b_LK^sqrt=max(b_-,b_+)`

at scale `sqrt(log n)`, lower better, with current certified value

`b_LK^sqrt=C_*=e phi(Phi^{-1}(e^{-1}))`.

This is **not** a claim that `C_*` is the true threshold constant. It is the best symmetric fixed-coefficient frontier certified by the current P03 proof package at this newly admitted scale. The negative and positive proofs above both attain the same `C_*` because they are controlled by the same ordered-deadline race.

State transition:

- `c_LK^cert=0`: saturated, no stuck count;
- `a_LK^fine=0`: saturated, no stuck count;
- `b_LK^sqrt`: `UNMEASURED -> admitted baseline C_*`;
- fine-scale unchanged count for the new metric: `0`;
- HARD recoveries used: `0/2`.

---

## 8. Refutation attempts, failures, and exact remaining obligation

Three checks prevent overclaiming.

**Failure 1: sending the cutoff to infinity does not repeat Claim 282's zero-frontier trick.** Once `s=lambda sqrt(k)`, the deletion shift `K=k-s-O(1)` contributes `+lambda sqrt(k)` to the exponent. The exact derivative (12) yields an interior optimum; the correction cannot be driven to zero by `lambda->infinity`.

**Failure 2: sending `lambda->0` is also bad.** The optimizer `x_lambda` goes to the far negative normal tail because `g(x_lambda)=lambda`; the normal-race large-deviation cost forces `C(lambda)` upward. Thus the positive minimum is not an artefact of looking only at large cutoffs.

**Failure 3: `C_*` may still be only a proof-route constant.** The bad-pair argument continues to upper-bound actual joint isolation by a necessary ordered-deadline event, and the low-degree argument likewise discards additional bilateral constraints. The exact one-vertex bound (15) is a lower bound, not yet a sharp asymptotic. Therefore no claim is made that the true connectivity window has half-width `C_* sqrt(log n)`.

The live mathematical obligation is now to beat or certify `C_*` by using information still discarded by the ordered-race reduction. The two most concrete routes are:

1. derive the sharp asymptotic of the exact one-vertex order-statistic integral from Claim 278 at `k=log n+O(sqrt(log n))`; and
2. retain simultaneous two-vertex rejection/rank constraints beyond the ordered-deadline necessary event, to decide whether the pair correction constant is strictly smaller than `C_*`.

A theorem shrinking `b_LK^sqrt` is movement. If three admitted-metric runs leave `b_LK^sqrt` unchanged, the HARD stuck protocol fires. Recoveries currently remain `0/2`.

---

## 9. Directed P04/I0101 second audit

I audited the newest accessible nonrepeated P04 claim

`P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-45 = PROVED / STRUCTURAL-PARTIAL`

from

`proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T09-42-11Z__run-report.md`,

creation commit

`61564e476bbf771d7b531f987238d10763053e27`,

blob

`e3eba502e9d9b137aec331257f744fe41abdb21f`.

My verdict is

`P03-AUDIT-P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-285 = PASS (CLAIM-SCOPED)`.

### Independent derivation

Let `Q` be the symmetric Paley character matrix for `p≡1 mod 4`, so `Q1=0` and `Q^2=pI-J`. Fix anchors `0,1`, let `V=(+,+)` and exterior cells `B=(+,-), D=(-,+), F=(-,-)`. Character counting gives

`|V|=(p-5)/4`, `|B|=|D|=|F|=(p-1)/4`.

Writing `C=Q_{V,V}`, `U_B=Q_{V,B}`, etc., and `v=(C+2I)1`, the `V` rows of `Q1=0` give

`U_B1+U_D1+U_F1=-v`.                                        (26)

The `(V,0)` block of `Q^2=pI-J` gives

`U_B1-U_D1-U_F1=-v`,                                       (27)

while the `(V,1)` block gives

`-U_B1+U_D1-U_F1=-v`.                                      (28)

Solving (26)--(28) yields exactly

`U_B1=-v`, `U_D1=-v`, `U_F1=v`.

For any `n x m` matrix `M`,

`MM^T -(1/m)(M1)(M1)^T = M(I-J/m)M^T >=0`.

Apply this to the three exterior blocks and sum. Since `m=(p-1)/4`,

`UU^T >= 3/m vv^T = 12/(p-1) vv^T`.                       (29)

For `X>=0`, `tr X=1`, define `T=<J,X>`, `E=<UU^T,X>`, `R=1^T Xv`. Pairing (29) with `X` and applying Cauchy in the `X`-seminorm gives

`TE >= 12/(p-1) R^2`.

Next the `V x V` block of `Q^2=pI-J` has two anchor contributions equal to `J`, so

`C^2+UU^T=pI-3J`.                                          (30)

The Hilbert--Schmidt Gram matrix of

`X^(1/2)`, `C X^(1/2)`, `J X^(1/2)`

is therefore

`[[1,S,T],[S,p-3T-E,q],[T,q,nT]] >=0`,                    (31)

with `S=<C,X>`, `q=1^T X C1`, and `n=(p-5)/4`. Schur-complementing the top-left entry gives

`(q-ST)^2 <= (p-3T-E-S^2) T(n-T)`.                        (32)

Since `R=q+2T`, substituting theta-plus feasibility `S=T-1+Delta` produces exactly the report's stated escape inequality. Finally, for cell-constant exterior vectors,

`U(a1_B,b1_D,c1_F)=(-a-b+c)v`,

so that three-dimensional coarse cell space has rank-one image and two-dimensional kernel `c=a+b`.

All signs, cell sizes, PSD directions, Gram entries and Schur complements check. The scope warning is essential: Claim 45 is a structural escape theorem and a limitation of the coarse cell-constant route; it does **not** prove Randomstrasse Conjecture 27 or move P04's prime metric.

---

## 10. Cumulative P03/P0456 claim ledger

- `P03-P0456-HARRIS-ISOLATION-ROOT2-274`: **PROVED / STRUCTURAL-PARTIAL**.
- `P03-P0456-OPTIMIZED-CUTOFF-WINDOW-ZERO-276`: **PROVED / SOURCE-SCALE-WINDOW-PARTIAL**.
- `P03-P0456-EXACT-MARKING-FINE-WINDOW-278`: **PROVED / FINER-WINDOW-PARTIAL**.
- `P03-P0456-JOINT-RACE-FINE-BRACKET-280`: **PROVED / FINER-WINDOW-PARTIAL**.
- `P03-P0456-ORDERED-DEADLINE-FINE-WINDOW-ZERO-282`: **PROVED / FINER-WINDOW-PARTIAL**.
- `P03-P0456-NORMAL-RACE-SQRTLOG-BRACKET-284`: **PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED**.
- `P03-AUDIT-P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-285`: **PASS (CLAIM-SCOPED)**.

The parent P0456 source problem remains **PARTIAL / OPEN**: the exact transition, coefficient-zero behavior and limiting law are not established.

---

## 11. Next concrete attack

Stay on P0456. Do not return to the saturated `W_n` proof.

The next run should attack the gap between the exact model and the ordered-race necessary event at the `sqrt(log n)` scale. A useful first target is the exact one-vertex isolation integral: obtain its logarithm through order `sqrt(k)` and compare its coefficient with the pair-race `C_*`. In parallel, write the joint two-vertex event as an ordered two-spine coefficient extraction so that common exterior edges are retained rather than discarded. Any rigorous reduction below `C_*` moves the newly admitted metric.

No claim of publication novelty is made without a stronger literature search. Search misses remain bounded evidence.

---

## 12. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  target: P0456
  category: HARD_OUTSIDE
  source: "Dabirian--Subramanian, Connectivity of a family of bilateral preference random graphs, J. Appl. Probab. 63(2) (2026), Section 1.1"
  canonical_claim: operations/claims/P0456.md
  source_status: OPEN_PARTIAL
  old_saturated_metrics:
    c_LK_cert: 0
    a_LK_fine: 0
  new_metric:
    name: b_LK_sqrt
    scale: sqrt(log n)
    previous: UNMEASURED
    current: "C_* = e*phi(Phi^{-1}(e^{-1})) = 1.0244099529838058..."
    direction: lower_is_better
    status: BASELINE_ADMITTED_FROM_PROVED_THEOREM
  unchanged_count: 0
  recoveries_used: 0
  claim_this_run: "P03-P0456-NORMAL-RACE-SQRTLOG-BRACKET-284 = PROVED / FINER-WINDOW-PARTIAL / PUBLICATION-NOVELTY-UNVERIFIED"
  theorem_scope:
    negative: "every fixed b<-C_* gives whp disconnection for k<=log n+b sqrt(log n)"
    positive: "every fixed b>C_* gives whp connectivity for k>=log n+b sqrt(log n)"
    unresolved: "[-C_*,C_*], coefficient zero, limiting law, exact threshold"
  methods: [6, 13, 27]
  peer_audit:
    id: P03-AUDIT-P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-285
    verdict: PASS_CLAIM_SCOPED
    peer_claim: P04-I0101-ANCHOR-CELL-ESCAPE-SCHUR-45
    peer_report: proofnet24/P04-closure-local-paley/runs/2026-09-18/2026-09-18T09-42-11Z__run-report.md
    peer_creation_commit: 61564e476bbf771d7b531f987238d10763053e27
    peer_blob: e3eba502e9d9b137aec331257f744fe41abdb21f
  publication_novelty: UNVERIFIED
  next_obligation: "sharpen exact one-vertex and true joint two-vertex laws at sqrt(log n) scale and lower/certify C_*"
```

---

## 13. Tool/model limitations and delivery state

Runtime exposed GPT-5.6 Sol; reasoning level is not authenticated by the scheduler/runtime interface and is therefore reported as UNVERIFIED. The requested GPT-6/maximum setting remains prompt-only in the exposed control surface.

The primary-source PDF was inspected through both its text layer and page images. Repository-wide large surfaces were connector-truncated, so only exact-path and targeted reads are claimed rather than a byte-for-byte full-repository reread.

No email, Drive, public posting, paid compute, access changes, workflow execution, peer-file edits, or additional schedules were used.

**End of complete run report.**
