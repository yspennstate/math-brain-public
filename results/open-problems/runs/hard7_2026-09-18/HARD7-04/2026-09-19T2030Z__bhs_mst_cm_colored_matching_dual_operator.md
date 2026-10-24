Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen source metric: `beta_MST^- >= eta -> beta_MST^- >= eta`; STUCK1 recovery executed by porting the nearest solved configuration-model technique, using fresh methods B5 / B8 / B21.**

# HARD7-04 — BHS heavy-tailed configuration-model MST universality — colored-matching dual operator recovery

**Status:** PARTIAL / source OPEN / STUCK1 RECOVERY  
**Canonical claim:** `operations/claims/BHS-MST-CM-UNIV.md`  
**Owner:** HARD7-04  
**Frozen quantity:** `beta_MST^-`  
**Before:** `beta_MST^- >= eta`, `eta=(tau-3)/(tau-1)`.  
**After:** `beta_MST^- >= eta`. **No movement.**

The mathematical progress is route-level but substantive: the previous random stopping-time `available-degree` blocker is not intrinsic. An exact edge-color-first construction of the weighted configuration model defers every future-threshold pairing until after the lower-threshold principal component is known. In that representation the one-collar problem becomes a static marked-duality problem plus a two-type `2 x 2` reproduction operator. Its deterministic target has spectral radius exactly `(p+Delta) h_n'(q)` in the ideal dual law, reproducing the sharp `tau-3` collar margin from the previous analytic calculation.

## 1. Continuity, required reads, ownership, and exclusions

This run resumed the newest state rather than restarting admission. I read the current versions of:

- `operations/hard7_2026-09-18/CONTROL.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- the intake record/search surface for I0049;
- `operations/claims/BHS-MST-CM-UNIV.md` and neighboring `operations/claims/P0150.md`;
- the newest own checkpoint `2026-09-19T1930Z__bhs_mst_cm_stuck1_available_degree_duality.md` and the immediately preceding `1830Z` finite-`n` mesoscopic duality report.

I0049 remains `KNOWN / RESOLVED IN QUEUED SCOPE`; repository records point to Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs* (arXiv:2512.18937), so it is not reopened. The active Bhamidi--Sen configuration-model MST claim remains exclusively owned by HARD7-04. A fresh canonical-ID search showed references to this claim by other workers only as an already-owned HARD target; no competing owner was found.

The exact idea was written before code at

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T2028Z__bhs_mst_cm_colored_matching_idea.md`

creation commit `b859da2a6d2082ab8fd6c1b873cd6991b39055c5`, and was read back at that commit.

### Runtime/scheduler capability honesty

The scheduler situation is still the one recorded by CONTROL/RESULTS: the exposed task interface has title/prompt, schedule/timing mode, and enabled state, but **no model selector, no reasoning-effort selector, and no guaranteed execution duration**. GPT-6/maximum can therefore only be requested in prompt text. This run identifies as GPT-5.6 Sol; reasoning telemetry is unavailable, so the reasoning level is `UNVERIFIED`.

Changing that requires a platform/scheduler interface that actually exposes model and reasoning fields. Historical `You cannot modify this task` failures, including a P26 failure in one context, were authorization/context restrictions. Current `RESULTS.md` also records that P26 was later successfully updated in an authorized context, so the evidence is context-dependent rather than a mathematical/scheduler-model workaround. The compliant workaround for an edit denial is an owning/authorized context or platform support, never creating a duplicate task or bypassing permissions. No schedule was created, modified, disabled, or re-enabled in this run.

## 2. Fresh source/current-literature check — 19 September 2026

Primary source remains:

Shankar Bhamidi and Sanchayan Sen, *Geometry of the minimal spanning tree in the heavy-tailed regime: new universality classes*, Probab. Theory Relat. Fields 188 (2024), 729--804, DOI `10.1007/s00440-024-01259-3`, arXiv:`2009.10696`.

The source abstract describes the `tau in (3,4)` strong-disorder MST distance exponent as a well-known open problem for a broad class of heavy-tailed random graphs, proves the result for one rank-one inhomogeneous model, and says its limiting spaces are expected candidates for other heavy-tailed models. The admitted configuration-model extension remains exactly the source residual recorded in the canonical claim.

Fresh bounded searches used the exact title and the queries

- `configuration model minimum spanning tree heavy-tailed tau 3 4 2026`,
- `configuration model MST heavy-tailed Bhamidi Sen`, and
- the exact Bhamidi--Sen title with 2025/2026 variants.

They recovered the 2024 source and known neighboring MST/configuration-model work, but no later theorem matching the retained `tau in (3,4)` configuration-model MST scaling problem. This is bounded negative evidence, not a worldwide novelty certificate.

Nearest solved engine rechecked in full text:

Remco van der Hofstad, Svante Janson, Malwina Luczak, *Component structure of the configuration model: Barely supercritical case*, Random Structures & Algorithms 55 (2019), 3--55, DOI `10.1002/rsa.20837`.

Its Section 5 constructs the configuration model by exponential half-edge lifetimes and component exploration; at deterministic times the surrogate sleeping degree counts are independent binomials. Theorem 2.6 treats the barely supercritical giant under weak moment assumptions, and Remark 2.7 says the proof also gives degree counts in the largest component. This remains the closest published engine for the lower-color graph.

For B21 I also checked the configuration-model percolation literature around the standard “change order of percolation and pairing” device. In particular, the degree-dependent percolation construction in *Weighted Distances in Scale-Free Configuration Models* (J. Stat. Phys. 2018, DOI `10.1007/s10955-018-1957-5`) gives an equality in distribution between edge percolation and an artificial-vertex half-edge-percolation construction. That is related evidence that changing the order of percolation and pairing is standard. I therefore treat the finite colored-matching identity below as an elementary/folklore mechanism, **not as a novelty claim**. Its use here is to preserve two nested weight thresholds simultaneously and remove the specific stopping-time obstruction in this track.

## 3. Frozen metric and Section-I accounting

The fixed source metric remains

`beta_MST^- := sup { beta >= 0 : for every delta0 in (0,1) there is c_delta0>0 with liminf_n P(diam(M_n)>=c_delta0 n^beta)>=1-delta0 }`.

The `1631Z` run proved the source-predicted lower exponent

`beta_MST^- >= eta`,  `eta=(tau-3)/(tau-1)`.

The `1728Z`, `1830Z`, and `1930Z` runs did not move this number, triggering STUCK1. The `1930Z` stuck report selected exactly one recovery: **port the technique from the nearest solved problem**. This run executes that recovery. The frozen metric still does not move; however, the remaining obligation changes materially from a marked stopping-time available-degree identity to a static five-moment marked-dual profile for an ordinary configuration model. I therefore label this the STUCK1 recovery, not a source closure and not a new stuck declaration.

## 4. Fresh 90% methods — B5 / B8 / B21

These three moves had not been used previously on the current BHS target. Earlier BHS triples were B1/B2/B19, B6/B20/B30, B3/B11/B25, and B4/B13/B18.

### B5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Add one future-weight collar of width `Delta=p^+-p`, preserve it as a separate edge type, and compute the first-order two-type reproduction operator rather than collapsing all future stubs into one scalar `Q/S`. **Successful at the exact ideal-dual algebra level.** It recovers the same sharp coefficient `tau-3-delta` as the previous generating-function calculation.

### B8 — GO THE OTHER WAY AND DISCRETIZE

Work at the finite labeled-half-edge level before taking any random-graph limit. Conditional on edge-color counts, the weighted configuration model decomposes exactly into a uniform partition of half-edges and independent uniform within-color matchings. **Successful exactly.** This removes future-color pairings from the lower-threshold exploration.

### B21 — ASK WHO ELSE HAS THIS SHAPE

Compare the representation with known half-edge percolation/explosion methods and with the van der Hofstad--Janson--Luczak continuous-time exploration. **Successful as a route transfer, not as closure.** The remaining hard statement is now an ordinary-CM marked giant-profile estimate; the literature engine has the right deterministic-time independence but does not state the required growing weighted marks off the shelf.

Counterexample pressure came first: I tried to preserve the old scalar `available-degree` invariant under a different order of revealing the weighted matching. The exact colored construction shows that the claimed need to consume future-color boundary pairings during lower exploration is representation-dependent. That refutes the *necessity of the old route*, not the source statement.

## 5. Exact finite colored-matching decomposition

Let `H` be a set of `L=2m` labeled half-edges. Choose a uniform perfect matching `M` of `H`. Independently color each matched edge in three classes `A,B,C` with probabilities

`p`, `Delta`, `1-p-Delta`.

Here `A` means weight `<=p`, `B` means `p<weight<=p+Delta`, and `C` means weight `>p+Delta`. Let `N_A,N_B,N_C` be the numbers of colored edges, and let `H_A,H_B,H_C` be their incident half-edge sets.

**Lemma 1 (exact colored-matching decomposition).** Conditional on

`(N_A,N_B,N_C)=(a,b,c)`, `a+b+c=m`,

1. `(H_A,H_B,H_C)` is uniform over ordered partitions of `H` with sizes `(2a,2b,2c)`;
2. conditional on this partition, the restrictions `M_A,M_B,M_C` are independent uniform perfect matchings of `H_A,H_B,H_C`.

**Proof.** A colored perfect matching with these fixed color counts is in bijection with

- an ordered partition `(H_A,H_B,H_C)` of the prescribed sizes, and
- one perfect matching on each part.

Every colored matching in the count class has the same preconditioning probability

`(2m-1)!!^{-1} p^a Delta^b (1-p-Delta)^c`.

Therefore conditioning on the counts makes every tuple in the displayed bijection equiprobable. The product form of the counting measure gives uniformity of the partition and conditional independence/uniformity of the three internal matchings. QED.

This lemma includes loops and multiple edges because it is a statement about labeled half-edges before quotienting by vertices; no simplicity assumption is hidden.

**Immediate consequence.** Let `X_v=|H_A cap H(v)|`. Conditional on `H_A`, the lower graph is exactly the configuration model with degree sequence `(X_v)`. Its principal component `C_A` is measurable with respect to `(H_A,M_A)` only. Conditional additionally on `N_B`, `H_B` is a uniform `2N_B`-subset of `H\H_A`, and `M_B` is a fresh uniform perfect matching on `H_B`. Thus no `B`-pairing needs to be exposed while finding `C_A`.

This is the precise point where the STUCK1 stopping-time dependence disappears.

## 6. Ideal marked-dual identities

The finite colored model gives hypergeometric lower-color degrees. To identify the deterministic target, first replace that finite-population law by its product surrogate

`X_v ~ Bin(d_v,p)`, independently over vertices,

and put `R_v=d_v-X_v`. Let

`L=sum_v d_v`,

`h_n(s)=(1/L) sum_v d_v s^(d_v-1)`.

The size-biased excess pgf of the lower-color degree sequence is

`H_p(s)=h_n(1-p+ps)`.

Let `psi` be the nontrivial extinction root and define

`q=1-p+p psi`.

Then

`psi=H_p(psi)=h_n(q)`.

For one vertex of original degree `d`, differentiating

`E[psi^X]=(1-p+p psi)^d=q^d`

gives

`E[X psi^X]=psi p d q^(d-1)`,

`E[X(X-1) psi^X]=psi^2 p^2 d(d-1) q^(d-2)`,

`E[R psi^X]=(1-p)d q^(d-1)`,

`E[X R psi^X]=psi p(1-p)d(d-1) q^(d-2)`,

`E[R(R-1) psi^X]=(1-p)^2 d(d-1) q^(d-2)`.

Summing over vertices and using `h_n(q)=psi` yields

`S_A = sum E[X psi^X] = p L psi^2`,

`Q_A = sum E[X(X-1) psi^X] = p^2 L psi^2 h_n'(q)`,

`S_R = sum E[R psi^X] = (1-p)L psi`,

`T_AR = sum E[X R psi^X] = p(1-p)L psi h_n'(q)`,

`Q_R = sum E[R(R-1) psi^X] = (1-p)^2 L h_n'(q)`.

Hence the ordinary lower-dual excess mean is exactly

`Q_A/S_A = p h_n'(q)`.

## 7. B5 payoff — the two-color collar operator

Let

`theta=Delta/(1-p)`

be the fraction of non-`A` half-edges assigned to color `B` in the product target. The outside `B` half-edge mass is

`S_B,out = theta S_R = Delta L psi`,

while the total `B` half-edge mass is `Delta L`. Thus the ideal fraction of `B` stubs lying outside `C_A` is `psi`.

Count a nonbacktracking particle by the color of the edge on which it arrives. At an outside vertex, the raw `A->B` and `B->B` stub counts contain a factor `1/psi`; but a candidate `B` stub must pair to another outside `B` stub, contributing the compensating outside-pairing factor `psi`.

The four entries are therefore

`A->A = Q_A/S_A = p h_n'(q)`,

`A->B = psi * theta T_AR/S_A = Delta h_n'(q)`,

`B->A = theta T_AR/(theta S_R) = p h_n'(q)`,

`B->B = psi * theta^2 Q_R/(theta S_R) = Delta h_n'(q)`.

So the ideal dual reproduction matrix is

```text
M_dual = h_n'(q) * [[p, Delta],
                    [p, Delta]].
```

Its nonzero eigenvalue is

`rho(M_dual)=(p+Delta) h_n'(q)`.                            (7.1)

This calculation is exact for the displayed product dual moments; the transfer to the finite colored graph still needs concentration and is **not** silently assumed.

For the explicit Pareto-quantile subclass from the `1830Z` run,

`epsilon_n=lambda_n n^{-eta}`,

`p_n=(1+epsilon_n)/nu_n`,

`p_n^+=[1+(1+delta)epsilon_n]/nu_n`,

`Delta_n=delta epsilon_n/nu_n`, `0<delta<tau-3`,

and the already proved finite-`n` analytic dual law is

`p_n h_n'(q_n)=1-(tau-3+o(1))epsilon_n`.

Since `h_n'(q_n)=nu_n+o(1)`, (7.1) gives the target

`rho(M_dual,n)=1-(tau-3-delta+o(1))epsilon_n`.              (7.2)

Thus the two-color representation preserves exactly the sharp collar margin found analytically in the previous runs.

## 8. New exact blocker: MD5 instead of the stopped available-degree ratio

The previous STUCK1 blocker was

`R_n^av=h_n'(q_n)+o_P(epsilon_n)`

after a marked lower-threshold exploration and deletion. Lemma 1 shows this scalar stopped-process identity is not a canonical obligation.

For the explicit Pareto-quantile subclass and the fixed recovery sequence

`lambda_n=(log n)^3`,

`epsilon_n=(log n)^3 n^{-eta}`,

it is enough to establish the following five **static** marked-dual estimates for the ordinary lower-color configuration model. Let `X_v` be the actual lower-color degree, `R_v=d_v-X_v`, and `C_A` its principal component. With `psi_n=h_n(q_n)`:

```text
(MD5.1) sum_{v notin C_A} X_v
        = p_n L_n psi_n^2 + o_P(epsilon_n n),

(MD5.2) sum_{v notin C_A} X_v(X_v-1)
        = p_n^2 L_n psi_n^2 h_n'(q_n) + o_P(epsilon_n n),

(MD5.3) sum_{v notin C_A} R_v
        = (1-p_n)L_n psi_n + o_P(epsilon_n n),

(MD5.4) sum_{v notin C_A} X_v R_v
        = p_n(1-p_n)L_n psi_n h_n'(q_n) + o_P(epsilon_n n),

(MD5.5) sum_{v notin C_A} R_v(R_v-1)
        = (1-p_n)^2 L_n h_n'(q_n) + o_P(epsilon_n n).
```

Once MD5 holds, `H_B` is merely a without-replacement sample from the static complement stubs and `M_B` is a fresh uniform matching. The remaining `B`-sampling estimates are then finite-population concentration statements, not random stopping-time identities. The finite perfect-matching correction is order `1/(Delta_n n)`, and

`1/(Delta_n n)=o(epsilon_n)`

because `epsilon_n^2 n -> infinity` for `eta<1/3`.

### Why the MD5 fluctuation scale is plausible

Write `r=tau-1 in (2,3)`, `a=1/r`, `beta=r-2`, `eta=beta/r`, and

`1-q_n=y_n=n^{-a} z_n`, `z_n->infinity`,

so `epsilon_n asymp y_n^beta`. For the worst second-factorial marked sums, the independent deterministic-time surrogate variance is of order at most

`n y_n^(r-4)`.

Therefore

`sd/(epsilon_n n)
 <= [n y_n^(r-4)]^(1/2)/(n y_n^beta)
 = (n y_n^r)^(-1/2)
 = z_n^(-r/2) -> 0`.                                      (8.1)

So the desired `o(epsilon_n n)` error is larger than the natural deterministic-time fluctuation by a diverging factor. The hard part is not variance; it is transferring the continuous-time sleeping surrogate to the actual principal-component complement for these growing marks.

This is materially narrower than the old blocker: a five-observable weighted extension of an ordinary-CM giant-profile theorem, with no nested edge-weight stopping time.

## 9. Exact self-check — last 10%, not the research route

Only after the route was obtained, I wrote and executed

`artifacts/hard7_2026-09-18/HARD7-04/2026-09-19T2028Z__colored_matching_exact.py`.

It exhaustively enumerates all perfect matchings and three-colorings for `L=6` and `L=8`, verifies the bijective fixed-count decomposition exactly, and separately checks the marked-moment/two-type algebra in a rational cubic example with

`p=2/3`, `psi=1/4`, `q=1/2`, `Delta=1/12`, `h'(q)=1`.

The exact matrix is

`[[2/3,1/12],[2/3,1/12]]`

with spectral radius `3/4=(p+Delta)h'(q)`.

Archived output:

```text
L 6 matchings 15 colored 405 count_classes 10 unique representations 405
L 8 matchings 105 colored 8505 count_classes 15 unique representations 8505
q 1/2 psi 1/4 hprime 1 matrix ((Fraction(2, 3), Fraction(1, 12)), (Fraction(2, 3), Fraction(1, 12))) rho 3/4
ALL_EXACT_CHECKS_PASS = True
```

Code commit `f86130088111dbd20ef2bbef66884cad201d70cc`; output commit `2689d13a4c348319605187467ac90cc3ae55c7c1`. Both were read back successfully. This is explicitly a **self-check**, not an independent audit and not a proof of MD5.

## 10. What was refuted, what was proved, and what was not

### Proved in this run

1. The finite colored-matching decomposition of Lemma 1, by a complete bijective proof.
2. The exact product-dual marked moment identities.
3. The resulting ideal two-type collar operator and its spectral radius `(p+Delta)h_n'(q)`.
4. The algebraic compatibility of that operator with the previously proved heavy-tail collar deficit `tau-3-delta`.

### Refuted only as a route requirement

The statement “future-threshold boundary pairings must be revealed/consumed while exploring the lower-threshold giant” is false as a representation claim. The exact colored construction defers them. Consequently the old stopped scalar `R_n^av` identity is not logically necessary for the MST proof.

### Not proved

- MD5 for the actual lower-color configuration model;
- the hypergeometric-to-product transfer at the full marked-dual accuracy;
- the graph-level `o_P(epsilon_n)` two-type operator approximation;
- the one-collar outside-diameter theorem for the actual weighted graph;
- the Kruskal collar ladder;
- an upper bound matching `beta_MST^-<=eta`;
- the source's full scaling-limit universality statement.

The honest status remains **PARTIAL / source OPEN**.

## 11. Nearest solved problem after the recovery, and its remaining mismatch

The nearest solved problem is still van der Hofstad--Janson--Luczak (2019), but the mismatch is now much smaller and cleaner.

Their exploration already provides:

- an ordinary configuration model, exactly what `G_A` becomes after Lemma 1;
- independent binomial sleeping-degree surrogates at deterministic times;
- localization of the barely supercritical principal component between component-start stopping times;
- degree-count information for the largest component (Remark 2.7).

What is still absent from the statement used off the shelf is uniform control of the five **growing original-degree marks** in MD5 at absolute error `o(epsilon_n n)`. The deterministic-time variance calculation (8.1) has enough room. A proof must extend the sleeping-process comparison/semimartingale estimates to weighted observables and show that the component-start correction is also `o(epsilon_n n)` after the heavy-tail truncation.

This is the exact next mathematical obligation.

## 12. Next-run recovery target and methods

The current Section-I recovery was **port the technique**, and this run executed it. If the next invocation resumes this target, it should not go back to the old `R_n^av` formulation. It should attack MD5 directly for `lambda_n=(log n)^3`.

The next three unused Section-B moves reserved for that attempt are:

- **B12 FIND WHAT IS CONSERVED:** derive weighted sleeping-process compensators for the five MD5 marks;
- **B16 COMPUTE EVERY SMALL CASE:** use exact finite pairing/weighted exploration only if it tests a proposed compensator, not as a substitute for proof;
- **B28 REPLACE FOR ALL WITH TYPICAL:** prove MD5 first for the explicit Pareto-quantile subclass and one fixed mesoscopic sequence, not every admissible degree sequence.

If this recovery path reaches the second Section-I stuck episode without metric movement, only one further hard recovery is permitted before handoff/rotation under CONTROL.

## 13. Ledger delta

No shared root ledger was overwritten. For coordinator reconciliation only:

`HARD7-04 | BHS-MST-CM-UNIV | beta_MST^- | >=eta -> >=eta | PARTIAL / STUCK1 recovery; exact colored-matching decomposition removes marked stopping-time blocker; new blocker MD5`.

No paper folder is created because the source problem is not closed and there are not two independent outside audits.