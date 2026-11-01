Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `m_cert = 9 -> 9`; source remains REFUTED. Secondary fixed-graph/event threshold is now characterized exactly: the distinguished-edge marginal is nonmonotone iff `0<q<q_*`, where `q_*` is the smallest positive root of an explicit degree-21 integer polynomial and `1/32618 < q_* < 1/32617`. Section-B methods actually tried: #18 SAY IT IN ANOTHER LANGUAGE, #6 DEFORM TO A POINT YOU CAN SOLVE, #29 ADD THE POINTS AT INFINITY.**

# NM13-05 / C0146 — exact algebraic threshold for the 10-edge witness edge marginal

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim: **C0146**, `operations/claims/C0146.md`  
Canonical dedup key: `fk_q_less_than_1_monotone_coupling`  
Selection residue: `4 mod 13`  
Frozen metric: `m_cert`  
Metric before / after: **9 -> 9**  
Source mathematical status before / after: **REFUTED -> REFUTED**  
Exact minimum finite-simple-graph counterexample complexity: **10 edges**  
Secondary quantity before: one fixed rational pair certified the same graph for `0<q<=1/32618`  
Secondary quantity after: exact distinguished-edge derivative threshold `0<q<q_*`, with `1/32618<q_*<1/32617`  
Unchanged-run counter: **1 -> 2**  
Stuck recoveries: **0 -> 0**  
Required closure auditors: **P26 and NM13-06; neither has a C0146 PASS recovered in this invocation**

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still provides title/prompt, schedule or relative-start fields, timing mode, enabled state and task identity, but **no bindable model-family selector and no bindable reasoning-effort selector**. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model/effort controls together with authenticated per-run runtime attestation. The historical P26 response `You cannot modify this task` remains an authorization-context boundary; current repository policy records that another authorized context later succeeded. The lawful workaround for a denied modification is the owning/otherwise-authorized context or authorized platform/admin support for the same task, never duplication, permission changes or access-control bypass. No schedule was created, modified, disabled or probed in this invocation.

## 2. Authoritative continuity, ownership and required reads

This invocation continues the already admitted **C0146** assignment. Intake was not reopened and no new claim was created.

Before the new argument I reread or exact-target-recovered the current controlling state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized amendment `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/C0146.md`;
- C0146 intake and historical attempt `C0146-A001` in the Claude intake/attempt ledgers;
- newest own report `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T12-39-00Z__c0146-q-interval-sharpening-prior-art.md`;
- newest neighboring NM13-04 report `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T12-27-30Z__p0457-six-run-handoff-successor-screen.md`;
- newest neighboring/designated-auditor NM13-06 report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T12-36-30Z__post-p0195-successor-admission-screen-3-i-complete.md`;
- current exact C0146 ownership and P26/NM13-06 audit searches.

The broad append-only ledgers and JSONL files can be connector-truncated when rendered wholesale. I therefore do **not** claim a byte-for-byte visual rendering of every repository row. Exact canonical files, current immutable report paths, current root-file reads, exact ID/dedup searches and source/attempt hits are the continuity anchors. Missing or truncated text is never treated as a release.

The canonical claim still names `proofnet24/NM13-05` as exclusive owner. No release, retirement, POSTED/campaign settlement, competing C0146 owner, P26 C0146 PASS or NM13-06 C0146 PASS was recovered. The latest visible P26 work does not contain a C0146 audit verdict. The latest NM13-06 report explicitly remains on successor admission screening and notes C0146 as NM13-05 work, not an audit. Thus the mathematical source verdict stays **REFUTED**, while fleet closure remains blocked on the two required outside audits.

The historical attempt `C0146-A001` remains only a preliminary observation: stochastic monotonicity in `p` is necessary and a small-graph symbolic test was left as the next step. It did not contain the present witness or solution.

## 3. Exact source and bounded literature refresh — 2026-09-18

The current primary source is Gabor Pete, *Probability and Geometry on Groups*, live PDF dated **April 3, 2024**. I re-read the actual source page. Question 13.2 is still printed as:

> Is there a monotone coupling `(omega_p)_{p in [0,1]}` of the `FK(p,q)` measures for any `q in [0,1)`?

The present source refutation uses **strictly positive** `q`, so it does not depend on an endpoint convention at `q=0`.

Fresh bounded searches on 2026-09-18 included the exact source wording, `FK(p,q) monotone coupling q<1`, `random-cluster q<1 stochastic monotonicity`, `arboreal gas stochastic monotonicity Poudevigne`, and the earlier numerical signatures. The important prior-art qualification is unchanged but now rechecked directly: Noah Halberstam's 2023 Cambridge thesis explicitly states that the finite-graph arboreal gas is not stochastically monotone in its parameter, attributing this to **Remy Poudevigne, private correspondence**. Bauerschmidt--Crawford--Helmuth--Swan's published arboreal-gas paper identifies that model as the `q -> 0`, `p=beta q` random-cluster limit.

Recent q<1 papers found in the refresh are different in scope. Tang--Zhang, arXiv:2609.11578 (submitted 2026-09-10), prove negative correlation for high-degree regular graph classes while noting that even pairwise negative correlation remains open on arbitrary finite graphs. Park, arXiv:2608.08565 (submitted 2026-08-09), treats wired regular trees and branch negative dependence. Neither supplies the present general finite-graph monotone-in-`p` result or this exact witness.

Accordingly, **novelty remains UNVERIFIED**. In particular, I do not claim the broad small-`q` nonmonotonicity mechanism as new: once a strict finite arboreal-gas witness from the private correspondence is known, finite-dimensional continuity already pushes it to sufficiently small positive `q`. What is explicit and reproducible in this track is the 10-edge graph, its exact positive-`q` certificates, and now the exact algebraic threshold for one distinguished-edge marginal. A bounded negative search is not proof of worldwide novelty.

## 4. Frozen metric versus the new secondary theorem

The frozen metric remains exactly the one in the claim:

`m_cert` = the largest integer `m` for which NM13-05 has a rigorous source-valid certificate that every finite simple graph with at most `m` edges is stochastically monotone in `p` for every `q in (0,1)`.

The all-graphs theorem through nine edges gives `m_cert=9`, while the exact ten-edge source counterexample makes ten the minimum edge complexity. Nothing in this run changes that cutoff, so **`m_cert=9 -> 9`**. This is the second consecutive unchanged frozen-metric run, hence `unchanged_runs: 1 -> 2`.

The run nevertheless sharpens a source-relevant secondary quantity all the way from a one-sided rational certificate to a complete fixed-graph/event classification. The previous report gave one rational pair `x1=20.48`, `x2=20.49` proving reversal for `0<q<=1/32618`. Here I determine exactly for which `q` the **distinguished-edge marginal itself** can decrease as `p` varies.

This secondary theorem is not substituted for the frozen metric and does not claim that every increasing event on the same graph becomes monotone above the threshold.

## 5. Fixed witness and exact source coordinates

Keep the same seven-vertex ten-edge simple graph

`E = {(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,6),(5,6)}`

and distinguished edge `e*=(0,1)`.

For fixed `q>0`, introduce the strictly increasing source-coordinate change

`x = p/[q(1-p)]`, equivalently `p = xq/(1+xq)`.

As `p` runs through `(0,1)`, `x` runs through `(0,infinity)`. For an edge set `A subseteq E`, write

`c(A)=|A|-7+k(A)`

for cycle nullity, where `k(A)` is the number of connected components of `(V,A)`. After removing the common positive random-cluster factor, define

`D(x,q) = sum_A x^{|A|} q^{c(A)}`,

`N(x,q) = sum_{A contains e*} x^{|A|} q^{c(A)}`.

The distinguished-edge marginal is

`M_q(x)=N(x,q)/D(x,q)`.

The denominator is positive for `x,q>0`.

## 6. Method #18 — SAY IT IN ANOTHER LANGUAGE: turn coupling failure into an algebraic derivative problem

Differentiate the exact rational function. Exhaustive symbolic collection over all `2^10=1024` configurations gives

`M_q'(x) = G(x,q)/D(x,q)^2`,

with the exact factorization

`G(x,q) = (q x^2 + 2x + 1)^2 P(x,q)`.

The square is strictly positive for `x,q>0`, so the sign of the source edge-marginal derivative is exactly the sign of `P`. The polynomial is

```text
P(x,q) =
 q^5 x^14
 + 14 q^4 x^13 + 10 q^4 x^12 + 2 q^4 x^11
 + 81 q^3 x^12 + 114 q^3 x^11 + 61 q^3 x^10 + 14 q^3 x^9 + q^3 x^8
 + 248 q^2 x^11 + 636 q^2 x^10 + 804 q^2 x^9 + 630 q^2 x^8
 + 308 q^2 x^7 + 85 q^2 x^6 + 10 q^2 x^5
 + 304 q x^10 + 1184 q x^9 + 2384 q x^8 + 3000 q x^7 + 2445 q x^6
 + 1290 q x^5 + 428 q x^4 + 82 q x^3 + 7 q x^2
 - 12 x^8 + 124 x^7 + 473 x^6 + 702 x^5 + 573 x^4
 + 282 x^3 + 84 x^2 + 14 x + 1.
```

Two boundary facts are immediate and will be crucial below:

`P(0,q)=1` for every `q`, and for `q>0` the leading `x` coefficient is `q^5>0`, so `P(x,q)->+infinity` as `x->+infinity`.

**Outcome #18:** the fixed-event monotonicity question is now a real-algebraic sign problem for one explicit bivariate polynomial. This removes the arbitrary choice of two nearby `p` values that limited the previous certificate.

## 7. Method #6 — DEFORM TO A POINT YOU CAN SOLVE: the forest boundary explains the negative pocket

At the exactly solvable boundary `q=0`, the polynomial factors as

`P(x,0) = -(2x+1)^2 (3x^6 - 34x^5 - 85x^4 - 82x^3 - 40x^2 - 10x - 1)`.

The sextic in parentheses is negative at `x=0` and positive for sufficiently large `x`, so `P(x,0)` eventually becomes negative. Thus the negative derivative pocket is not a floating-point accident at tiny positive `q`; it is a deformation of a genuine forest-limit sign change.

This is compatible with the Halberstam/Poudevigne prior-art warning: the `q=0` direction already contains nonmonotonic behavior. What still needs exact work is where this particular finite-graph edge-marginal pocket disappears for `q>0`.

**Outcome #6:** the deformation supplies the correct starting chamber and explains why the previous source counterexample lived at very small positive `q`, but it does not by itself locate the positive threshold.

## 8. Method #29 — ADD THE POINTS AT INFINITY: resultant plus exact Sturm chambers

A change in the number of positive roots of `P(.,q)` can occur only when a root is multiple, reaches `x=0`, or escapes through `x=infinity`. The two boundary identities above rule out the latter two mechanisms for every fixed `q>0`: `P(0,q)=1`, and the leading coefficient is `q^5>0`. Therefore the positive-root count can change only when

`P(x,q)=P_x(x,q)=0`

for some positive `x`, so only at zeros of the exact resultant.

Direct exact elimination gives

`Res_x(P,P_x) = -8707129344 q^29 (q-2)^3 (q-1)^21 Q(q)`,

where

```text
Q(q) =
 92694159707929024 q^21
 -2391589630941253288 q^20
 +29746205595411967893 q^19
 -237584429857878700128 q^18
 +1368080890353907048044 q^17
 -6039373752940080693090 q^16
 +21204939066099517868732 q^15
 -60619470428749841791133 q^14
 +143269171746836332047798 q^13
 -282721908167836957015421 q^12
 +468637137631262035601528 q^11
 -654323732181611169153936 q^10
 +769297561572927490222677 q^9
 -758772176437803896017347 q^8
 +622783815342824868970470 q^7
 -419479318411046356889281 q^6
 +226682317220292450964951 q^5
 -94757337900579248668608 q^4
 +28805272039611809516928 q^3
 -5663605479498043130880 q^2
 +538678727161928773632 q
 -16509457795645440.
```

Let `q_*` be the smallest positive real root of `Q`. Exact Sturm counts give

- no root of `Q` in `(0,1/32618)`;
- exactly one root in `(1/32618,1/32617)`;
- no root in `(1/32617,1/2)`;
- exactly one root in `(1/2,3/5)`;
- no root in `(3/5,1)`.

Thus `Q` has exactly two roots in `(0,1)`, and

`1/32618 < q_* < 1/32617`.

For orientation only, numerical evaluation gives

`q_* = 0.0000306579402683398308536642587788...`.

No decimal approximation is used in the proof.

Now count positive roots of `P(.,q)` by exact Sturm arithmetic at one rational sample in each resultant chamber:

- at `q=1/40000`, there are exactly **2** positive roots;
- at `q=1/1000`, there are **0** positive roots;
- at `q=3/4`, there are **0** positive roots.

Because the positive-root count is locally constant away from resultant zeros and cannot change through `0` or `infinity`, these counts hold throughout the corresponding chambers. Therefore:

1. For every `0<q<q_*`, `P(.,q)` has exactly two simple positive roots. Since `P(0,q)>0` and `P(x,q)>0` for sufficiently large `x`, its sign is negative strictly between those two roots. Hence `M_q'(x)<0` somewhere.
2. For `q` in each open chamber above `q_*` and below `1`, `P(.,q)` has no positive roots and is positive at `x=0`; hence it is positive for every `x>0`.
3. At the two interior resultant roots themselves, `P` is nonnegative on `x>0`: if it were negative at some positive `x`, continuity in `q` would force a negative value in a neighboring no-root chamber, impossible. In particular `P>=0` at `q=q_*`.

Finally `x=p/[q(1-p)]` is strictly increasing in `p`. Thus a negative `x` derivative is exactly a local decrease in the source edge marginal as `p` increases.

This proves the complete fixed-graph/event theorem:

> **Theorem.** For the seven-vertex ten-edge graph above and distinguished edge `e*=(0,1)`, the function `p -> P_FK(p,q)(e* open)` is nonmonotone iff `0<q<q_*`, where `q_*` is the smallest positive root of the displayed degree-21 polynomial `Q`. For `q_*<=q<1`, this particular edge marginal is nondecreasing for all `p in [0,1]`.

In particular, the preceding rational endpoint `1/32618` lies strictly below the true derivative threshold, while `1/32617` lies strictly above it. So `1/32618` was already the largest reciprocal endpoint `1/n` that can sit below this `q_*`.

**Outcome #29:** compactifying the positive `x` line by controlling both endpoints turns a local derivative observation into a complete algebraic chamber classification.

## 9. Exact finite certificate and self-check

Only after the algebraic route was obtained did I write the exact checker

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_edge_marginal_threshold_checker.py`

created at commit

`2c7e3d8eb5aa965a0e3cb76305613dcaa36af1e6`.

It uses exact configuration enumeration and exact symbolic/Sturm arithmetic. It independently:

- enumerates all `1024` edge configurations;
- reconstructs `D,N` and the derivative numerator;
- verifies the displayed factorization by `P`;
- verifies the `q=0` factorization;
- computes and verifies the exact resultant factorization by `Q`;
- performs exact Sturm counts in the rational `q` chambers;
- performs exact positive-`x` Sturm counts at rational chamber samples.

I executed the checker. Its stdout is archived at

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_edge_marginal_threshold_checker.out`

created at commit

`3c345d294bfd6d26b467e031786f1e2cc124852e`.

It ends exactly

`ALL_EXACT_CHECKS_PASS`.

This is a **self-check**, not an independent audit.

## 10. What this does and does not establish

The parent source question is already refuted by the explicit positive-`q` witness from the preceding run. This theorem strengthens the internal understanding of that witness: it gives the exact algebraic endpoint of one increasing event's reversal, instead of merely certifying one rational subinterval.

It does **not** prove any of the following:

- that the same ten-edge graph is stochastically monotone for `q>=q_*`;
- that another increasing event on this graph cannot fail above `q_*`;
- that no different graph fails at larger `q`;
- that the explicit witness or threshold is publication-novel.

Those statements would require new arguments. The source-level conclusion needs none of them: one strictly positive `q` counterexample already refutes the universal Question 13.2.

## 11. Audit gate, counters and next step

No C0146 PASS was recovered from either required outside auditor:

- **P26: NOT PASSED**;
- **NM13-06: NOT PASSED**.

Therefore C0146 is mathematically **REFUTED** in this track but **not fleet-CLOSED**. No paper folder is created before the two-audit gate.

Because the frozen metric did not move, the unchanged-run counter advances **1 -> 2**. Stuck recoveries remain **0**. This does not yet trigger the three-unchanged Section-I protocol. The next high-value C0146 action is independent audit and prior-art reconciliation, not another arbitrary sharpening of a secondary witness parameter. If the next NM13-05 invocation again leaves the frozen metric/remaining closure obligation unchanged and no audit/source correction intervenes, it will be the third unchanged run and must use the owner Section-I stuck protocol rather than file another ordinary lemma.

Potential fresh Section-B routes, **reserved but not credited as tried**, are #4 PROVE SOMETHING WEAKER COMPLETELY, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, and #27 SWAP THE QUANTIFIERS; they should be used only if the audit gate exposes a concrete mathematical obligation rather than as make-work after source refutation.

## 12. Structured ledger delta for P26

```yaml
ledger_delta:
  track: NM13-05
  category: CLOSABLE_OUTSIDE
  source_id: C0146
  claim_file: operations/claims/C0146.md
  canonical_dedup_key: fk_q_less_than_1_monotone_coupling
  selection_residue_mod_13: 4
  source: "Gabor Pete, Probability and Geometry on Groups, Question 13.2"
  source_status_before: REFUTED
  source_status_after: REFUTED
  frozen_metric: m_cert
  metric_before: 9
  metric_after: 9
  exact_min_counterexample_edges: 10
  secondary_quantity: fixed_witness_distinguished_edge_q_threshold
  secondary_before: "one fixed rational pair certified reversal for 0<q<=1/32618"
  secondary_after: "edge marginal nonmonotone iff 0<q<q_*, q_* smallest positive root of explicit degree-21 Q; 1/32618<q_*<1/32617"
  methods_actual: [18, 6, 29]
  methods_outcomes:
    18: "rewrote edge marginal as exact rational N/D; derivative sign reduced to explicit polynomial P"
    6: "q=0 forest deformation exhibits the negative derivative pocket algebraically"
    29: "endpoint control + resultant + exact Sturm chambers yields the complete fixed-event threshold"
  exact_checker: proofnet24/NM13-05/artifacts/2026-09-18/c0146_edge_marginal_threshold_checker.py
  exact_checker_output: proofnet24/NM13-05/artifacts/2026-09-18/c0146_edge_marginal_threshold_checker.out
  self_check: PASS
  p26_audit: NOT_PASSED
  nm13_06_audit: NOT_PASSED
  closure: PENDING_TWO_OUTSIDE_AUDITS
  novelty: UNVERIFIED
  unchanged_runs_before: 1
  unchanged_runs_after: 2
  stuck_recoveries_before: 0
  stuck_recoveries_after: 0
  next_step: "audit/prior-art reconciliation first; if a third unchanged invocation occurs without an audit/source change, enter Section-I stuck protocol"
```

## 13. Write discipline

This invocation created only the substantive exact checker, its archived output, and this one immutable report in `proofnet24/NM13-05/`. It did not edit the canonical claim, shared root ledgers, peer namespaces, workflows, permissions, public surfaces, email/Gmail, Drive, paid compute, or any schedule. The report is to be read back at its creation commit; no receipt-only follow-up commit is warranted.
