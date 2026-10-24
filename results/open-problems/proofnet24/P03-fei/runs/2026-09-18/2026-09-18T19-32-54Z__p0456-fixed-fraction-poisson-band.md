Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED. This is not GPT-6 at maximum.**

**NO SOURCE-LEVEL COEFFICIENT-METRIC MOVEMENT; NEW FIXED-FRACTION POISSON BAND.** The saturated frontiers remain `c_LK^cert=a_LK^fine=b_LK^sqrt=0`; HARD recoveries remain `0/2`. This run uses Section-B methods **#10 DERANDOMIZE, #23 DO WHAT THE PROPOSER DID NOT EXPECT, #26 HUNT THE SPORADIC CASE**. The main advance is a source-faithful extension of the Poisson isolated-vertex law from every `o(log n)` offset window to the explicit fixed-fraction band `|k-log n| <= 0.01 log n`.

# P03 / P0456 run report — constructive Palm sampler and fixed-fraction Poisson band

Run timestamp: **2026-09-18T19:32:54Z**  
Track: **P03**  
Canonical target: **P0456**  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Category: **HARD OUTSIDE**

---

## 1. Continuity, repository screen, source status, and audit gate

The exclusive assignment remains

`operations/claims/P0456.md`,

creation commit `9d9c9545783bf8ae09805830d72f5d935be9afb1`, blob `74b9c5ebda19b1ded526457c1c7ea12654419bcb`.

The newest complete P03 report entering this run was

`proofnet24/P03-fei/runs/2026-09-18/2026-09-18T18-31-39Z__p0456-rank-palm-growing-window.md`,

creation commit `b6a9af78598dbe128cbfee3d375ec1d837f8b28f`, blob `851447c376a00b5ae3dea998dce077ae89951a1e`; its exact-commit readback recovered `**End of complete run report.**`.

I preserve Claims 274, 276, 278, 280, 282, 284, 286 and the candidate-complete/audit chain 288--294.

This invocation reread/recovered the root `README.md`, `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`, current `FLEET_RULES.md`, `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`, campaign `probability_campaign_2026_09/INDEX.md`, the canonical P0456 claim, the complete newest P03 report, the Claim-291 bounded-omission kernel, the Claim-278 component envelope, the current P26 stream, and the neighboring P0457 stream only for nonduplication. Shared root/campaign search surfaces can be connector-truncated; I do **not** represent them as byte-for-byte rereads when the connector returned only excerpts. Exact-path reads controlled the mathematical dependencies used below.

P0457 remains the distinct diameter problem and is not resumed here.

### Fresh primary-source verification

The primary source is still:

Hossein Dabirian and Vijay Subramanian, *Connectivity of a family of bilateral preference random graphs*, *Journal of Applied Probability* 63(2) (June 2026), 552--579, published online 18 December 2025, DOI `10.1017/jpr.2025.10051`.

The Cambridge HTML still states the bilateral model literally: iid continuous edge weights on `K_n`, an edge retained iff it lies among the `k` lowest incident weights at both endpoints. Section 1.1 still says that connectivity is unknown in the displayed band

`log n -(1/2) loglog n sqrt(log n) <= k <= log n +(1/2) loglog n sqrt(log n)`

and attributes the gap to analytically simpler sufficient conditions. Fresh checks also recovered:

- Lemma 10: the source bad pair event has probability `O(k^3/n)`;
- Lemma 14: the source second-moment pair ratio for its negative-side window;
- Theorem 4: fixed low degree vanishes on the published positive side;
- Theorem 5: for `k=floor(t log n)`, all components above a fixed `O(1/t)` size vanish whp;
- Theorem 6: connectivity whp for the published positive window, and in particular for every fixed `t>1` with `k=floor(t log n)`.

Fresh bounded 2026-09-18 searches for the exact title/DOI/authors, `LK(n,k) Poisson isolated vertices`, `LK(n,k) log n+c connectivity`, and bilateral-preference constant-window results recovered the primary paper and adjacent work but no later theorem matching Claims 288--294 or the fixed-fraction strengthening below. This is dated bounded negative evidence only; **publication novelty remains UNVERIFIED**.

### Fresh outside-audit screen

A repository-wide search for `P0456`, Claims 288--294, `audit`, and `PASS` still finds **no P26 or distinct OTHER-track full-chain audit** of the source-matching proof. The newest concrete P26 report recovered is

`proofnet24/P26-proof-audit-recovery/runs/2026-09-18/2026-09-18_22-00-00__run-report.md`,

which audits historical P04/I0101 Claim 17, not P0456. P04 remains rotation-stopped; its newest recovered record explicitly creates no mathematical theorem. Therefore the directed P03->P04 duty has no genuinely new claim to audit and no repeat audit is fabricated.

The closure gate remains

`P0456_ACTIVE_AUDIT_PENDING / OUTSIDE_AUDITS_FOUND_0_OF_2`.

Self-audits do not count. No final paper folder is created.

---

## 2. Preserved chain and new theorem

The candidate-complete source-matching chain remains:

- `P03-P0456-POISSON-CRITICAL-WINDOW-288 = PROVED / SOURCE-MATCHING-CANDIDATE-COMPLETE / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289 = PROVED / SELF-AUDIT-REPAIR / SOURCE-MATCHING-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- `P03-P0456-MARKED-POISSON-CROSSCHECK-290 = PROVED / SELF-AUDIT-STRENGTHENING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`;
- Claims 291--294 remain supporting self-audit kernels.

This run adds:

### Claim `P03-P0456-FIXED-FRACTION-POISSON-BAND-295`

**Status:** `PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

Uniformly over all integers `k` satisfying

`|k-log n| <= (1/100) log n`,                                (2.1)

let `Z_n` be the number of isolated vertices of `LK(n,k)` and put

`lambda_n=n e^{-k}`.                                          (2.2)

Then

`d_TV(Law(Z_n),Poisson(lambda_n)) -> 0`,                      (2.3)

and

`P(LK(n,k) is connected)=exp(-lambda_n)+o(1)`,               (2.4)

uniformly under (2.1).

Thus the Poisson isolated-vertex description is not merely an `o(log n)`-offset phenomenon: it survives a genuine fixed positive fraction of `log n` around the threshold. The constant `1/100` is a deliberately conservative proved radius, **not** claimed sharp or maximal.

---

## 3. #10 DERANDOMIZE — an explicit finite Palm sampler, and the exact obstruction to naive monotone surgery

Claim 293 used a regular conditional local-block sampler. That is mathematically legitimate but not maximally transparent. Here is an explicit finite accept/reject realization of the same Palm law.

Choose a uniform root `V`. In the ordinary weighted complete graph let `S` be the labels of the first `k` incident edges at `V` and put

`A={V} union S`.                                               (3.1)

Split the edge weights into:

- the **far block**: edges with both endpoints outside `A`;
- the **local block**: all edges touching `A`.

Conditional on `S`, the far block is independent of the local block and of the event `I_V=1`, because isolation of `V` is decided entirely by the root star and the stars of selected neighbors, all of which lie in the local block.

Construct `G^s` from an ordinary graph `G` as follows.

1. If `I_V(G)=1`, set `G^s=G`.
2. If `I_V(G)=0`, keep the entire far block fixed.
3. Repeatedly sample a fresh local block from its exact law conditional on `Top_k(V)=S` until the sampled local block satisfies `I_V=1`; use the first successful local block.

The procedure terminates almost surely because `P(I_V=1 | Top_k(V)=S)>0`. By label symmetry `S` is uniform over `k`-subsets both unconditionally and under the isolated-root Palm law. Conditional on `S`, the accepted local block has exactly the law

`Law(local block | Top_k(V)=S, I_V=1)`.                        (3.2)

Because the far block is kept at its independent unconditional law, the output graph satisfies exactly

`Law(G^s)=Law(G | I_V=1)`.                                    (3.3)

Hence `Z_n(G^s)` is exactly the size-biased law of `Z_n`.

This is a **constructive randomized** sampler; it is not a deterministic coordinatewise surgery. I tried to obtain the latter and found the precise obstruction. A surgery that holds the root star fixed and only lowers selected-neighbor competitor weights cannot be Palm-exact, because conditioning on isolation also tilts the distribution of the root order vector itself: for root proposal deadlines `d_1,...,d_k`, the root-star density is reweighted by the simultaneous rejection probability, a nonconstant function of the `d_i`. Therefore any exact deterministic transport must move the root order vector and the selected-neighbor stars jointly. A Rosenblatt/quantile transport exists abstractly, but it is no simpler than the conditional sampler and gives no additional monotonicity. I do not mislabel the accept/reject construction as a deterministic derandomization.

The coupling is at least as favorable as Claim 293's independent local-block coupling: when the ordinary root is already isolated it changes nothing; otherwise the Palm local block has the same conditional marginal as before. All rank-witness influence bounds therefore continue to apply.

---

## 4. Quantifying the one-root saddle on a fixed `0.99--1.01` log band

The only new quantitative issue in passing from Claim 294's `o(log n)` offsets to (2.1) is the replacement of the true Poisson mean

`mu_n=n P(I_v)`                                               (4.1)

by the explicit `lambda_n=n e^{-k}` when `lambda_n` can now grow like `n^{0.01}`. A bare relative `1+o(1)` estimate is insufficient. We need an exponentially small relative saddle error.

Claim 294 already proved such an exponential margin. I make a conservative exponent explicit here.

For the clean marked event write, as in Claims 288/294,

`M_{k,k}=(m)_{k+1}/k! int_0^1 Q_k(x)^k(1-x)^(m-k-1) dx`,      (4.2)

where

`m=n+O(1)`, `N=n+O(k)`,
`Q_k(x)=E[(x-B_k)_+]`,
`B_k~Beta(k,N-k+1)`,
`beta=E B_k=k/(N+1)`.                                         (4.3)

The mean-replacement integral is exact:

`M_0=(1-beta)^m=e^{-k}(1+O(k^2/n))`.                          (4.4)

Put

`x_0=beta+k/(2N)`.                                            (4.5)

### 4.1 Upper side of the split

For `x>=x_0`, beta/order-statistic duality gives

`P(B_k>x)=P(Bin(N,x)<=k-1)`.                                  (4.6)

At `x=x_0`, `Nx=(3/2+o(1))k`. The elementary Chernoff bound therefore yields

`P(B_k>x_0)
 <= exp[-(gamma+o(1))k]`,

where

`gamma=1/2-log(3/2)=0.0945348918...`.                         (4.7)

Let `R(x)=E[(B_k-x)_+]`. Since `sd(B_k)=O(sqrt(k)/n)`, Cauchy--Schwarz and (4.7) give

`R(x)<=O(sqrt(k)/n) exp[-(gamma/2+o(1))k]`.                  (4.8)

Because `x-beta>=k/(2N)`,

`k R(x)/(x-beta)
 <= O(sqrt(k)) exp[-(gamma/2+o(1))k]`.                        (4.9)

Using the exact identity

`Q_k(x)=x-beta+R(x)`,                                         (4.10)

raising to the `k`th power changes the mean-replacement integrand on this region by

`1+O(sqrt(k)e^{-k/25})`                                      (4.11)

for all sufficiently large `n`, because `1/25=0.04<gamma/2`.

### 4.2 Lower side of the split

Write

`t=(x-beta)N/k`.                                              (4.12)

For `k^{-1/4}<=t<=1/2`, the crude bound

`Q_k(x)<= (x-beta)+E|B_k-beta|
        =(k/N)(t+O(k^{-1/2}))`                                (4.13)

is enough. Relative to the mean-replacement saddle at `t=1`, the normalized log-integrand rate is

`log t +1-t+o(1)`.                                            (4.14)

On `t<=1/2`,

`log t +1-t <= log(1/2)+1/2=-0.193147...`.                   (4.15)

For `t<k^{-1/4}` (and also for `x<=beta`), (4.13) is replaced by

`Q_k(x)<=O(k^{3/4}/N)`,                                      (4.16)

which loses `(1/4)k log k+O(k)` relative to the saddle and is superexponentially smaller on the `e^{-k}` scale. Consequently the entire lower region contributes

`O(e^{-0.15k}) M_0`.                                         (4.17)

Combining (4.4), (4.11), and (4.17),

`M_{k,k}
 =e^{-k}[1+O(k^2/n)+O(sqrt(k)e^{-k/25})]`                    (4.18)

uniformly whenever

`0.99 log n <= k <= 1.01 log n`.                              (4.19)

### 4.3 From the clean event to exact isolation

The sparse-internal-edge correction from Claims 286/288/294 is uniform on the compact ratio band (4.19): on a fixed `Lk/n` root-threshold event, one active selected-selected edge has an extra `O(k/n)` cost, two or more have `O(k^6/n^2)` total probability, and the threshold tail can be chosen with arbitrarily large polynomial decay by increasing fixed `L`. The fixed-defect marked saddle remains uniform for `k=Theta(log n)`.

Therefore

`P(I_v)
 =e^{-k}[1+O(sqrt(k)e^{-k/25})+n^{-1+o(1)}]`                 (4.20)

uniformly on (4.19).

Let `mu_n=nP(I_v)`. Under (2.1),

`lambda_n=n e^{-k}<=n^{0.01}`.                               (4.21)

Hence, by (4.20),

`|mu_n-lambda_n|
 <= n^{0.01} O(sqrt(log n) n^{-0.99/25})
    +n^{0.01}n^{-1+o(1)}
 =o(1)`,                                                       (4.22)

because

`0.01-0.99/25=-0.0296<0`.                                    (4.23)

This is the quantitative point at which the fixed `1%` band is certified.

---

## 5. Palm/Stein coupling error on the same fixed-fraction band

Claim 294's exact rank-witness classification remains valid. For an outside test vertex `w`, a mark flip under the local-block Palm resampling requires either:

- a proposal-rank crossing by some changed edge `w--A`; or
- a reciprocity-rank crossing by an edge `u--A` for one of the at most `k` far proposals of `w`.

There are `O(k^2)` candidate witness edges. Claim 294's exact binomial/rank lemma gives `O(k/n)` Palm low-edge probability for each, uniformly for **all** selected-neighbor rejection thresholds `0<=h<=k`.

Claim 291's bounded-omission marked-saddle proof extends uniformly from bounded offsets to any compact ratio band `c log n<=k<=C log n`: its proof uses only `k->infinity`, `k=O(log n)`, `m mu/k->1`, a fixed number of omitted deadlines, and beta/order-statistic saddle estimates whose constants are uniform on compact positive ratios. Thus, after exposing one witness and omitting the bounded number of touched deadlines, the remaining isolation cost is

`exp[-k+o(k)]`                                                (5.1)

uniformly on (4.19).

Choose fixed `L` so the far `k`th-order threshold tail has Chernoff exponent large enough that its union contribution is `n^{-3}` throughout (4.19). Then the expected number of outside mark flips is

`O(k^3 e^{-k+o(k)})+n^{-3}
 =n^{-0.99+o(1)}`.                                           (5.2)

Selected-neighbor flips contribute at most

`k e^{-k+o(k)}=n^{-0.99+o(1)}`,                              (5.3)

and the residual root term contributes

`e^{-k+o(k)}=n^{-0.99+o(1)}`.                                (5.4)

For the explicit Palm coupling in Section 3,

`E|Z_n^s-(Z_n+1)|=n^{-0.99+o(1)}`.                           (5.5)

The standard size-bias Stein inequality now gives

`d_TV(Law(Z_n),Poisson(mu_n))=o(1)`                           (5.6)

uniformly under (2.1). Together with

`d_TV(Poisson(mu_n),Poisson(lambda_n))<=|mu_n-lambda_n|`      (5.7)

and (4.22), this proves Claim 295 equation (2.3).

No sharp Stein constant is claimed.

---

## 6. Connectivity formula without extrapolating the component envelope

A fixed-fraction band need not be handled by forcing Claim 278's global component envelope beyond the range where it was originally optimized. Instead split the band at

`D_n=(log n)^(3/4)`.                                         (6.1)

### Central zone: `|k-log n|<=D_n`

Because `D_n=o(log n)`, Claim 294 applies directly and gives

`P(connected)=exp(-lambda_n)+o(1)`                            (6.2)

uniformly in the central zone, with nontrivial components eliminated under the literal bilateral-preference definition.

### Lower flank: `k<=log n-D_n`

Here

`lambda_n>=e^{D_n}->infinity`.                               (6.3)

By the already-proved uniform TV-Poisson estimate,

`P(Z_n=0)=e^{-lambda_n}+o(1)=o(1)`.                           (6.4)

Connectivity implies no isolated vertices, hence

`P(connected)<=P(Z_n=0)=o(1)`.                               (6.5)

Since `e^{-lambda_n}=o(1)`, equation (2.4) follows uniformly on the lower flank. No mean-degree inference and no component extrapolation is needed.

### Upper flank: `k>=log n+D_n`

The source Theorem 6 applies for every

`k>=log n+t' loglog n sqrt(log n)`

with fixed `t'>1/2`. Since

`D_n / [loglog n sqrt(log n)] -> infinity`,                   (6.6)

all sufficiently large `n` in the upper flank satisfy the source theorem, so

`P(connected)->1`                                            (6.7)

uniformly there. Also

`lambda_n<=e^{-D_n}->0`,                                     (6.8)

so

`exp(-lambda_n)->1`.                                         (6.9)

Thus (2.4) holds uniformly on the upper flank as well.

Combining the three zones proves Claim 295 equation (2.4). This patch deliberately uses the source's own Theorem 6 rather than inventing a fixed-fraction extension of an internal component lemma.

---

## 7. #23 DO WHAT THE PROPOSER DID NOT EXPECT — hunt a surviving first correction

I assumed the Poisson law might fail at its first correction order and checked the three most plausible mechanisms before accepting Claim 295.

### 7.1 One-root saddle correction

The exact mean-replacement term is

`(1-beta)^m
 =e^{-k}[1+O(k^2/n)]`.                                (7.1)

At the true critical window `k=log n+O(1)`, multiplying the correction by `n` gives only

`n e^{-k} O(k^2/n)=O(k^2/n)->0`.                              (7.2)

The beta-tail correction from Section 4 is even smaller, `O(sqrt(k)e^{-k/25})` relatively. Thus no nonzero `O(1)` correction to the Poisson mean survives.

### 7.2 Size-two components

Claim 291's literal tree-plus-external-rejection estimate at `r=2` gives

`P(exists a two-vertex component)=n^{-1+o(1)}`                (7.3)

at `k=log n+O(1)`. Therefore two-components do not contribute an `O(1)` correction to the limiting connectivity probability.

### 7.3 Joint-isolation dependence

Claim 292's interaction graph and Claim 293/294's Palm coupling show that nonclean interaction patterns carry at least one extra `n^{-1+o(1)}` codimension factor. The absolute size-bias error is `n^{-1+o(1)}` at the critical window. Thus pair and higher interaction corrections also vanish at first order.

**Outcome of #23:** I found no surviving first correction. The present proof certifies only that all three candidate corrections vanish; it does **not** identify the exact next asymptotic coefficient or rate, which remains open.

---

## 8. #26 HUNT THE SPORADIC CASE — where Claim 294 first genuinely needed new work

Claim 294 only asserted every `o(log n)` offset. The first sporadic regime to test is

`k=(1-alpha)log n+O(1)`                                      (8.1)

for fixed `alpha>0`, where the Poisson mean grows polynomially:

`lambda_n=n^alpha e^{O(1)}`.                                 (8.2)

The Palm coupling itself does **not** fail here: its error is essentially `poly(k)e^{-k}=n^{-1+alpha+o(1)}`, which still vanishes for every fixed `alpha<1`.

The first real obstruction is instead the absolute accuracy of the one-root mean. A relative saddle error `e^{-eta k}` becomes harmless only if

`alpha < eta(1-alpha)`.                                      (8.3)

Section 4 makes `eta=1/25` available on the present compact ratio band, and `alpha=1/100` safely satisfies

`0.01 < (1/25)(0.99)=0.0396`.                                (8.4)

Thus the first fixed-fraction probe succeeds rather than failing. I do **not** extrapolate to the maximal `alpha`; determining the optimal fractional radius requires optimizing the exact marked-saddle error, and possibly replacing the current coarse split. Claim 295 therefore records only the rigorously safe `1%` band.

---

## 9. What moved, what failed, and honesty boundaries

New theorem:

`P03-P0456-FIXED-FRACTION-POISSON-BAND-295 = PROVED / SELF-AUDIT-STRENGTHENING / SUPPORTING / AUDITS-PENDING / PUBLICATION-NOVELTY-UNVERIFIED`.

What moved:

- Claim 294's `o(log n)` offset class is strengthened to the explicit fixed-fraction band `|k-log n|<=0.01 log n` for TV-Poisson approximation and the connectivity formula.
- Claim 293's abstract conditional local-block sampler is replaced by an explicit finite accept/reject Palm sampler.
- The first-correction hunt rules out one-root, size-two-component, and interaction corrections at `O(1)` scale, although no exact next coefficient is identified.

What did **not** move:

- all three admitted coefficient metrics were already saturated at zero;
- no source-level CLOSED label is claimed;
- no publication novelty is claimed from a bounded search miss;
- no maximal fixed-fraction radius is claimed;
- the accept/reject sampler is randomized, not a deterministic monotone surgery;
- no sharp Stein rate or first correction coefficient is claimed.

---

## 10. Directed peer-audit duty

The directed duty remains P03 -> P04/I0101. The newest recovered P04 record is a rotation-stop/disabled administrative record and explicitly creates no mathematical theorem. I therefore do not recycle an older P04 result or fabricate a new audit.

---

## 11. Metric, stuck, recovery, and exact remaining obligation

Current state:

`P0456_ACTIVE_AUDIT_PENDING / c_LK^cert=0 SATURATED / a_LK^fine=0 SATURATED / b_LK^sqrt=0 SATURATED / OUTSIDE_AUDITS_FOUND_0_OF_2 / CLAIM_295_FIXED_FRACTION_AUDIT_KERNEL_READY / RECOVERIES_USED=0/2`.

No saturated `0 -> 0` coefficient is counted as a stuck run. External-audit waiting is not converted into a fake mathematical stuck count.

The controlling obligations remain:

1. P26 must perform a genuine end-to-end audit of the Claim-288/289 source-matching chain, preferably using Claims 291--295 as compact audit kernels;
2. one distinct OTHER track must independently audit the same full chain;
3. any gap found by either audit overrides strengthening work and must be repaired before closure;
4. only after two genuine outside PASS audits may P03 create the final self-contained paper folder and request shared-ledger closure through `ledger_delta`.

### Next mathematical attack if no outside audit has arrived

Use fresh Section-B methods **#5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT**:

- parameterize the saddle split and compute the best certified exponential relative-error rate `eta_*`; this directly controls the largest fixed-fraction Poisson band accessible to the present Palm proof;
- find a monotone envelope for the root-star tilt under isolation to test whether the accept/reject Palm sampler can be replaced by an ordered deterministic transport;
- identify the extremal deadline profile maximizing the Palm influence error and determine whether the `O(k^2)` witness count can be reduced at the level of expected influence.

Do not freeze a new metric unless a source-relevant reason requires one.

---

## 12. `ledger_delta` for P26

```yaml
ledger_delta:
  track: P03
  intake: P0456
  source: "Dabirian--Subramanian, Connectivity of a family of bilateral preference random graphs, J. Applied Probability 63(2) (2026), Section 1.1"
  canonical_claim: operations/claims/P0456.md
  source_status: OPEN_IN_PUBLISHED_SOURCE__CANDIDATE_COMPLETE_INTERNAL_PROOF__AUDITS_PENDING
  source_metric_c_LK_cert: 0
  fine_metric_a_LK_fine: 0
  sqrtlog_metric_b_LK_sqrt: 0
  metrics_state: SATURATED_DO_NOT_COUNT_AS_STUCK
  metric_movement_this_run: false
  recoveries_used: 0/2
  preserved_claims:
    - P03-P0456-POISSON-CRITICAL-WINDOW-288
    - P03-P0456-UNIFORM-POISSON-INTERACTION-REPAIR-289
    - P03-P0456-MARKED-POISSON-CROSSCHECK-290
    - P03-P0456-PAIR-SMALLCOMP-AUDIT-KERNEL-291
    - P03-P0456-FINITE-PALM-INTERACTION-GRAPH-292
    - P03-P0456-LOCALBLOCK-SIZEBIAS-STEIN-293
    - P03-P0456-RANK-PALM-SUBLINEAR-WINDOW-294
  new_claim: P03-P0456-FIXED-FRACTION-POISSON-BAND-295
  new_claim_status: PROVED_SELF_AUDIT_STRENGTHENING_SUPPORTING_AUDITS_PENDING_PUBLICATION_NOVELTY_UNVERIFIED
  new_claim_statement: "Uniformly for all integers |k-log n| <= 0.01 log n, d_TV(Law(Z_n),Poisson(n e^-k))->0 and P(LK(n,k) connected)=exp(-n e^-k)+o(1)."
  constructive_palm_sampler: "Keep the far block; if the ordinary root is not isolated, accept/reject-resample the local block conditional on the same top-k label set until root isolation holds. Output has exact isolated-root Palm law."
  first_correction_hunt: "No O(1) correction survives from the one-root saddle, size-two components, or joint-isolation interactions; exact next coefficient remains open."
  outside_audits_found: 0/2
  newest_p26_screen: "2026-09-18_22-00-00__run-report.md audits P04/I0101 Claim 17, not P0456."
  closure_state: P0456_ACTIVE_AUDIT_PENDING
  paper_package_created: false
  publication_novelty: UNVERIFIED
  p04_directed_audit: "No genuinely new P04 theorem available; no repeat audit fabricated."
  next_methods: [5, 13, 24]
```

**End of complete run report.**