Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — **NO MOVEMENT: `Delta_8 = UNMEASURED -> UNMEASURED`; Tang remains RETIRED/FROZEN at `UNBOUNDED_ABOVE` with supported unchanged count `6`. Methods actually used: B18 SAY IT IN ANOTHER LANGUAGE, B22 READ THE FAILURES NOT THE SUCCESSES, B25 COUNT THE SAME THING TWICE.** GPT-6 / maximum was requested in prompt text, but this runtime exposes no authenticated model-family selector, reasoning-effort selector, or applied-run telemetry, so I do not claim otherwise.

# R09 CLOSABLE OUTSIDE — G0002: higher-order pivot geometry and a source-normalization discriminator

Date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.

## 1. Continuity and ownership

I did **not** reopen Pengfei Tang Question 4.11. Its periodic-tree clause remains mathematically refuted, audit-complete and packaged; its transitive-graph clause remains open; the former R09 metric remains frozen at `UNBOUNDED_ABOVE` after the six-unchanged CLOSABLE retirement threshold.

The active R09 successor is the exclusive G0002 claim in `operations/claims/G0002.md`: Raphaël Cerf, *theta(p_c,Z^d)=0?*, arXiv:2608.23661v1, Conjecture 53.1. Its frozen quantity is

`Delta_8 = max_{phi in {phi_2, phi_{2\1}}} [max_{outside band} phi(A) - max_{inside band} phi(A)]`

for increasing `A subset {0,1}^8`, where the conjectured band is

`{|omega| >= 5} subset A subset {|omega| >= 2}`.

The prior admission report left `Delta_8=UNMEASURED` because Cerf's exact formulas (51.1)-(52.1) had not been recovered. I preserve that value rather than certify the wrong functional.

## 2. Repository / status recovery

At run start I recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, the current owner directive, the G0002 claim, the newest own R09 report, and the G0002 intake / prior attempt. Exact-ID repository searches found no competing current G0002 owner and no later repository proof of Conjecture 53.1.

The canonical intake records an important warning. It says Cerf's `P_k^+(A,omega)` is a **set of pivots of order k**, that `phi_2(A)=sum_omega |P_2^+(A,omega)|`, and that `phi_{2\1}` is the corresponding count excluding first-order pivots. It also records Cerf's universal bound `E|P_2^+(A)| <= 6 sqrt(n)`. The old attempt nevertheless modeled a second-order pivot as an **unordered pair** `(i,j)` and itself noticed that this makes majority have order `n^(3/2)` expected count, contradicting the quoted source scale. The old pair model is therefore unusable.

Fresh 2026-09-17 searches for the exact paper/title/arXiv ID, `Conjecture 53.1`, `P_2^+`, `phi_2`, and formulas (51.1)-(52.1) did not surface a later source-matching resolution. This remains bounded negative current-literature evidence, not a novelty certificate. The exact source formulas themselves are still not exposed in the repository: the intake records that the 708-page PDF was acquired and sections 53-58 read, but only the extracted statement/attempt were committed, not the source text at a fetchable repository path.

## 3. B18 — say it in another language: coordinate section boundaries

The useful conceptual correction is to stop treating a higher-order pivot as a pair. For each coordinate `i`, define the ordinary positive-pivotal section boundary

`B_i(A) = { y in {0,1}^{n-1} : 1_A(y,i=1)=1 and 1_A(y,i=0)=0 }`.

For increasing `A`, ordinary pivotality of site `i` is exactly membership of the remaining coordinates in `B_i(A)`. Thus any definition in which an **order-two pivotal site** is a site that is already pivotal or can be made pivotal by changing one other site should be expressible through the radius-one Hamming neighborhood `N_1(B_i)`.

This suggests the following reconstruction:

> **H2 (research hypothesis; NOT source-verified):**  
> `i in P_2^+(A,omega)` iff `d_H(omega_{-i}, B_i(A)) <= 1`.

If H2 is Cerf's convention, then the two functionals become

`phi_2(A) = 2 sum_i |N_1(B_i(A))|`,

`phi_{2\1}(A) = 2 sum_i (|N_1(B_i(A))| - |B_i(A)|)`.

The factor two comes from the two possible values of the `i`-th coordinate, because the section-boundary condition depends only on `omega_{-i}`.

I emphasize: these identities are **not promoted to claims about Cerf's source** until formulas (51.1)-(52.1) are recovered. Their value this run is that they give a sharply testable normalization hypothesis and a route that is categorically different from the failed pair interpretation.

## 4. B22 — read the failures

There are two distinct failures to learn from.

### 4.1 Failure of the old intake attack

The old `G0002-A001` pair-count model predicts, for a central Hamming threshold, approximately `Theta(n^(3/2))` second-order pivots on average. That cannot coexist with the source-reported `O(sqrt n)` universal bound. This is not evidence against Conjecture 53.1; it is evidence that the attempted object was not Cerf's object.

The corrected site-neighborhood viewpoint has the right scale: for a central threshold, each section boundary is a central layer in an `(n-1)`-cube, and its radius-one neighborhood has size `Theta(2^n/sqrt n)`. Summing over `n` coordinates and dividing by `2^n` therefore gives `Theta(sqrt n)`, exactly the source-reported dimensional scale.

### 4.2 Failure reported by the source

The canonical intake says Cerf's Section 59 tries Steiner symmetrisation and fails. That warns against assuming a generic compression or symmetrisation step monotonically improves `phi_2`. The next proof attempt should therefore not start by forcing every maximizer to be a Hamming threshold. Instead, the finite `n=8` attack should optimize the true local section-neighborhood functional (once verified) over arbitrary monotone families, using symmetry only to quotient equivalent violation types.

Outcome of B22: the useful route is **local section geometry + exact finite optimization**, not a global compression theorem and not pair counting.

## 5. B25 — count the same thing twice: a normalization test on Hamming thresholds

Still conditional on H2, let

`A_t = {omega in {0,1}^n : |omega| >= t}`.

For `1 <= t <= n`, every section boundary `B_i(A_t)` is exactly the `(t-1)`-st Hamming layer of `{0,1}^{n-1}`. Hence its radius-one neighborhood is the union of layers `t-2,t-1,t`. Double-counting the pairs `(omega,i)` therefore gives

`phi_2(A_t) = 2 n [ C(n-1,t-2) + C(n-1,t-1) + C(n-1,t) ]`,

`phi_{2\1}(A_t) = 2 n [ C(n-1,t-2) + C(n-1,t) ]`.

For `n=8`, after division by `2^8`, the candidate values are:

| threshold `t` | `phi_2(A_t)/256` | `phi_{2\1}(A_t)/256` |
|---:|---:|---:|
| 1 | 0.5000 | 0.4375 |
| 2 | 1.8125 | 1.3750 |
| 3 | 3.9375 | 2.6250 |
| 4 | 5.6875 | 3.5000 |
| 5 | 5.6875 | 3.5000 |
| 6 | 3.9375 | 2.6250 |
| 7 | 1.8125 | 1.3750 |
| 8 | 0.5000 | 0.4375 |

The candidate H2 threshold maxima occur at `t=4,5`, both inside the Conjecture-53.1 band for `n=8`. This is **not** a proof even of the threshold subclass under the source definition, because H2 remains unverified. It is a useful discriminator: when formulas (51.1)-(52.1) are obtained, evaluating them on `A_4` and `A_5` should either reproduce these exact integers (`1456` and `896`, respectively) or immediately falsify H2 and identify what directional/order convention is missing.

The same calculation explains the source scale: the central three-layer neighborhood has binomial mass `Theta(n^{-1/2})`, so the expected number of candidate order-two pivotal sites is `Theta(sqrt n)`, not `Theta(n^(3/2))`.

## 6. What moved, and why the frozen metric did not

The mathematical understanding moved: the prior pair model is discarded, a source-scale-consistent site/section model is isolated, and there is now an exact finite normalization benchmark at `n=8`.

The **frozen metric did not move** because `Delta_8` is defined using Cerf's actual `phi_2` and `phi_{2\1}`, not H2. Until formulas (51.1)-(52.1) are recovered, assigning any numerical `Delta_8` would violate the source-preservation rule.

No exact checker was created this run. That is deliberate: there is an idea worth checking now, but the source predicate itself is still missing. A checker of H2 would certify a research hypothesis rather than the source problem.

## 7. Next attack

The next obligation is source normalization, not another abstraction lemma. Recover formulas (51.1)-(52.1) or a source-equivalent definition of `P_2^+`. Then:

1. evaluate the source formula on `A_4,A_5` at `n=8` and compare with the H2 benchmark `phi_2=1456`, `phi_{2\1}=896`;
2. if H2 matches, compile the exact monotone-family optimizer directly in the section-neighborhood language, which should be substantially smaller than a pair-pivot MILP;
3. if H2 fails, use the discrepancy to infer the missing directional/order restriction before any global optimization.

A good genuinely different next method triple is **B14 FIND THE GROUP ACTING, B20 FIND WHY THE ALGORITHM FAILS, B11 DUALIZE**: quotient `n=8` violation types under stabilizer groups, identify whether the exact source predicate still yields a local neighborhood objective, then dualize the finite optimization to obtain a checkable global upper-bound certificate.

## 8. Model / scheduler-control status

The limitation remains unchanged. The exposed task-management interface provides prompt/title/schedule/timing/enabled controls, but no model-family selector, reasoning-effort selector, or authenticated completed-run model telemetry. GPT-6/maximum therefore cannot be verified or enforced from this interface. The repository also records that historical `You cannot modify this task` failures were context-dependent; the lawful workaround is the task-owning authorized context or platform support, not a duplicate task or permission bypass. Actually enforcing GPT-6/maximum requires explicit model/reasoning controls plus runtime telemetry in the product/API or owning workspace.

No scheduler modification was attempted.

## 9. Prohibited-action audit

No email/Gmail, Drive, public posting, purchase, permission change, workflow execution, scheduler mutation, force-push, shared-root edit, peer-file edit, or paid compute was performed.

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R09
  run_id: 20260917T080455Z_g0002_section_neighborhood_reconstruction_4e91c8
  predecessor:
    source: "Tang arXiv:2012.01135, source-PDF Question 4.11"
    metric: "greatest rigorous lower bound for theta'' at a certified admissible parameter in the fixed periodic-tree family"
    before: UNBOUNDED_ABOVE
    after: UNBOUNDED_ABOVE
    unchanged_count: 6
    state: RETIRED_FROZEN
  active:
    id: G0002
    source: "Raphael Cerf, arXiv:2608.23661v1, Conjecture 53.1"
    metric: Delta_8
    before: UNMEASURED
    after: UNMEASURED
    stagnation_count: UNKNOWN
    status: CLAIMED_ACTIVE_CLOSABLE
    source_normalization: NOT_YET_RECOVERED
    old_pair_interpretation: REJECTED_BY_SOURCE_SCALE_SANITY_CHECK
    new_research_hypothesis: "H2: order-two pivotal sites correspond to radius-one neighborhoods of coordinate section boundaries"
    hypothesis_status: NOT_SOURCE_VERIFIED
    exact_threshold_benchmark_if_H2:
      n: 8
      maximizing_thresholds: [4, 5]
      phi_2_integer: 1456
      phi_2_minus_1_integer: 896
  methods_this_run: [18, 22, 25]
  next_methods: [14, 20, 11]
  new_exact_source_claim: NONE
  new_checker: NONE_SOURCE_DEFINITION_REQUIRED_FIRST
  overall: ACTIVE_G0002_NO_METRIC_MOVEMENT_BUT_NEW_SOURCE_SCALE_CONSISTENT_ROUTE
```
