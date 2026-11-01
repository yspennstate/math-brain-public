Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. FROZEN-METRIC NO MOVEMENT: `m_cert = 9 -> 9`; SOURCE STATUS MOVEMENT: `PARTIAL -> REFUTED` by an exact 10-edge positive-`q` witness, so the minimum finite-simple-graph counterexample edge complexity is exactly 10. Section-B methods actually tried: #30 DO ONE SCALE/PARAMETER/DIRECTION AT A TIME, #10 DERANDOMIZE, #3 PROVE SOMETHING STRONGER. Fleet closure is still PENDING the required P26 and NM13-06 audits.**

# NM13-05 / C0146 — exact positive-q refutation and sharp 10-edge witness complexity

Run date: 2026-09-18 UTC  
Repository / branch: `yspennstate/math-open-problems` / `master`  
Track / namespace: `proofnet24/NM13-05/`  
Category: **CLOSABLE OUTSIDE**  
Canonical source / claim: **C0146**, `operations/claims/C0146.md`  
Canonical dedup key: `fk_q_less_than_1_monotone_coupling`  
Selection residue: `4 mod 13`  
Frozen metric: `m_cert`  
Metric before / after: **9 -> 9**  
Source mathematical status before / after: **PARTIAL -> REFUTED**  
Exact counterexample complexity: **10 edges**; previous all-graphs theorem through 9 edges makes this edge count minimal  
Unchanged-run counter: **0 -> 0** (source status moved)  
Stuck recoveries: **0**  
Required closure auditors: **P26 and NM13-06; neither is presumed to pass**

## 1. Runtime and control-plane disclosure

The task prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is not exposed, so the reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed task-control surface still offers prompt/title, start or schedule fields, timing mode, enabled state, and task identifiers, but no bindable model-family selector and no bindable reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface that exposes persistent model/reasoning controls plus authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` event remains an authorization-context boundary; repository policy records later successful modification from another authorized context. The lawful workaround is an owning/otherwise-authorized context or authorized platform/admin support, never duplication, permission changes, or bypass.

## 2. Authoritative continuity and ownership

This is a continuation of the already admitted exclusive C0146 claim; intake was not reopened and no new claim was created.

Before the present argument I reread or targeted-recovered the required current state:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/C0146.md`;
- newest own report `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T10-23-51Z__c0146-m9-graphic-matroid-bernstein.md`;
- newest neighboring NM13-04 report `proofnet24/NM13-04/runs/2026-09-18/2026-09-18T11-18-00Z__p0457-audit-gate-hold-5.md`;
- newest neighboring/designated-auditor NM13-06 report `proofnet24/NM13-06/runs/2026-09-18/2026-09-18T11-35-00Z__post-p0195-successor-admission-screen-2-h-i0059.md`;
- exact C0146 ownership/audit searches and the current source/prior-art surfaces described below.

A pre-report comparison from the preceding C0146 report commit `74a16ef8f9de1a272b3ee79fc224d30f527ba9fa` to current master was **133 commits ahead and 0 behind**. It showed no change to `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign `INDEX.md`/`RANKING.md`, or an intake source ledger that would release or settle C0146. No competing owner or owner-authorized release was recovered. The canonical claim remains exclusively NM13-05.

The controlling predecessor proved that **every finite simple graph with at most nine edges** has the desired monotonicity for every `q in (0,1)`, moving `m_cert` from 8 to 9. It explicitly reserved methods #3/#10/#30 rather than another blind census. This run uses exactly those three methods.

A first exact positive-q checker for the witness below had already landed in this namespace before this report, at commit `0376ad306d90108ce49405643daf08677a9ce240`. I read its code/output, independently rederived the algebra below, and added a second exact checker for the whole positive-q interval rather than treating the pre-report artifact as a substitute for a written argument.

## 3. Exact source and current literature check — 2026-09-18

The current primary source is Gábor Pete, *Probability and Geometry on Groups*, Question 13.2. The live primary PDF still asks:

> Is there a monotone coupling `(omega_p)_{p in [0,1]}` of the `FK(p,q)` measures for any `q in [0,1)`?

The source text is still present in the current PDF around printed page 185 / PDF page 184. The counterexample below uses **strictly positive q**, so it does not depend on how a `q=0` endpoint convention is interpreted.

Dated bounded searches on 2026-09-18 included the exact source question, `FK q<1 monotone coupling`, `random-cluster q<1 stochastic monotonicity`, `arboreal gas stochastic monotonicity`, `Poudevigne arboreal gas monotonicity`, and searches for the exact numerical signature `5/14`, `6/17` and an explicit finite witness.

A significant prior-art correction emerged. Noah Halberstam's 2023 Cambridge thesis *A Walk through the Forest: the Geometry and Topology of Random Systems* states in its random-forest introduction that the arboreal gas is **not** stochastically monotone in its edge-weight parameter on every finite graph, citing **Rémy Poudevigne, private correspondence**. Thus the qualitative `q -> 0` nonmonotonicity mechanism is not something I claim as new. Bauerschmidt--Crawford--Helmuth--Swan, *Random Spanning Forests and Hyperbolic Symmetry* (CMP 381 (2021), 1223--1261), gives the standard finite-graph arboreal-gas definition and identifies it as the `q -> 0`, `p = beta q` limit of the random-cluster model.

In the public material recovered here, Halberstam's thesis does not give the finite counterexample graph or an exact positive-q FK witness. The bounded searches did not surface the 10-edge graph, the fractions below, or a published positive-q interval matching this report. **That is bounded negative evidence only. Publication novelty of the explicit positive-q witness remains UNVERIFIED.** In particular, a strict unpublished arboreal-gas witness from the cited private correspondence would, by continuity, already suggest small positive q; the present contribution is an explicit finite graph and exact positive-q arithmetic, not a claim that the limiting idea itself is novel.

## 4. Frozen metric and what changes

The frozen metric remains

`m_cert` = largest integer `m` for which NM13-05 has a rigorous source-valid certificate that every finite simple graph with at most `m` edges is monotone in `p` for every `q in (0,1)`.

Before this invocation, `m_cert = 9`. This report does **not** rename or replace that metric. The new 10-edge counterexample means the metric stays exactly **9**, but the universal source question is false.

Because the previous report proved all finite simple graphs through 9 edges and this report gives a finite simple 10-edge counterexample, the **minimum number of edges in a finite simple counterexample is exactly 10**. This is recorded as terminal witness complexity, not as a new definition of `m_cert`.

## 5. Method #30 — DO ONE PARAMETER/DIRECTION AT A TIME: localize at q -> 0

Consider the 7-vertex, 10-edge simple graph

`E = {(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,6),(5,6)}`

and distinguish `e*=(0,1)`. It is 2-connected. Structurally it is a theta graph with five internally disjoint `0`--`1` paths of lengths

`1,2,2,2,3`.

At `q -> 0` with the standard forest scaling, the model becomes the arboreal gas. Exact enumeration of forests gives, by forest size `r=0,...,6`,

`D_r = [1,10,45,117,185,168,68]`

for all forests and

`N_r = [0,1,9,33,62,60,24]`

for forests containing `e*`. Hence the distinguished-edge probability in the fixed-size forest layers drops from

`60/168 = 5/14`

to

`24/68 = 6/17`,

with exact drop

`5/14 - 6/17 = 1/238 > 0`.

Equivalently, for forest fugacity `x`,

`D_0(x)=1+10x+45x^2+117x^3+185x^4+168x^5+68x^6`,

`N_0(x)=x+9x^2+33x^3+62x^4+60x^5+24x^6`,

and the derivative numerator of `N_0/D_0` factors exactly as

`-(1+2x)^4 (3x^6-34x^5-85x^4-82x^3-40x^2-10x-1)`.

Thus the limiting forest model has a concrete edge-marginal nonmonotonicity mechanism. This is consistent with the qualitative prior-art statement in Halberstam/Poudevigne, but the present graph and counts are explicit.

**Outcome of #30:** localization to the `q -> 0` direction isolates a strict, finite, one-edge obstruction on a 10-edge graph.

## 6. Method #10 — DERANDOMIZE: turn the limiting obstruction into an exact positive-q witness

For `q>0`, write the random-cluster weight of a subgraph `A` as

`p^{|A|}(1-p)^{10-|A|} q^{k(A)}`.

Let

`c(A)=|A|-7+k(A)`

be cycle nullity and set

`x = p/[q(1-p)]`.

Up to the positive factor `(1-p)^10 q^7`, the weight is exactly

`x^{|A|} q^{c(A)}`.

Therefore, for fixed `x`, if

`D_x(q)=sum_A x^{|A|} q^{c(A)}`

and

`N_x(q)=sum_{A contains e*} x^{|A|} q^{c(A)}`,

then the distinguished-edge probability is `N_x(q)/D_x(q)` and the corresponding FK parameter is

`p = xq/(1+xq)`.

Take the exact rational choices

`q = 1/40000`, `x_1=20`, `x_2=25`.

Then

`p_1 = 1/2001 < p_2 = 1/1601`.

The exact exhaustive checker gives

`P_{p1,q}(e* open) = 72488985858351 / 205113593435351`,

`P_{p2,q}(e* open) = 108671022567040625 / 307499119349131441`,

and their difference is

`395372934751065824378379416 / 63072249347906220400541234970791 > 0`.

The event `{e* open}` is increasing. If `FK_G(p1,q) <=_st FK_G(p2,q)`, every increasing event would have nondecreasing probability. The strict reverse inequality above therefore proves that stochastic domination fails, and hence a monotone coupling in `p` cannot exist for this `q`.

The original exact checker is

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_qsmall_edge_counterexample.py`

with archived output

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_qsmall_edge_counterexample.out`.

It enumerates all `2^10` configurations with exact integer/Fraction arithmetic, checks the graph is 2-connected, checks the transformed weights against the original FK weights, and ends `ALL_EXACT_CHECKS_PASS`.

**Outcome of #10:** the source is refuted by a completely explicit positive-q rational witness; no continuity-only or floating-point step remains.

## 7. Method #3 — PROVE SOMETHING STRONGER: an exact interval 0 < q <= 1/40000

The same graph and the same two `x` values give a stronger result than one rational point.

Exact enumeration yields the ascending-q coefficient vectors

`D_20 = [4920154201, 102855224000, 1057225600000, 5274880000000, 10240000000000]`,

`N_20 = [1738187620, 61901144000, 819081600000, 4762880000000, 10240000000000]`,

`D_25 = [18316309626, 482490281250, 6230253906250, 39068603515625, 95367431640625]`,

`N_25 = [6470052525, 289686375000, 4820097656250, 35253906250000, 95367431640625]`.

Since all denominators are positive for `q>0`, the sign of

`N_20/D_20 - N_25/D_25`

is the sign of

`H(q)=N_20(q)D_25(q)-N_25(q)D_20(q)`.

The exact coefficients of `H`, in ascending powers of `q`, are

`[3526524430622595,`
` -118321183332671706000,`
` -4653083103659709181250,`
` -73613777846263924687500,`
` -612669333551171376953125,`
` -2953816334960937500000000,`
` -8152236328125000000000000,`
` -9765625000000000000000000]`.

The constant coefficient is positive and every nonconstant coefficient is negative, so `H'(q)<0` for every `q>0`. At the right endpoint,

`H(1/40000) = 148264850531649684141892281 / 262144000000 > 0`.

Therefore

`H(q) >= H(1/40000) > 0`

for every `0<q<=1/40000`. Consequently, for every such `q`, setting

`p_1(q)=20q/(1+20q)`,

`p_2(q)=25q/(1+25q)`

gives `p_1(q)<p_2(q)` but

`P_{FK(p1(q),q)}(e* open) > P_{FK(p2(q),q)}(e* open)`.

So this single 10-edge graph refutes monotonicity for the entire exact interval

**`0 < q <= 1/40000`.**

I wrote and executed a second independent exact checker for this interval:

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_positive_q_interval_checker.py`

and archived its output at

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_positive_q_interval_checker.out`.

It re-enumerates all `2^10` configurations from the graph, reconstructs the four q-polynomials, verifies the `H` coefficients and endpoint value, verifies the endpoint FK probabilities, and ends `ALL_EXACT_CHECKS_PASS`. The checker source was created at commit `965e61b1f49a8a70b3ce4bd79b98fe0667b2542a`; the archived output was created at `3a87e9b441ca97d9bbd6be905ae5ea46ecf334f2`.

**Outcome of #3:** the refutation is not an isolated rational point; one explicit graph violates the desired order for every `q` in a nontrivial positive interval.

## 8. Source-level theorem and proof

**Theorem.** Pete Question 13.2 is false as stated. There is a finite simple 2-connected graph with 10 edges such that, for every `q` with `0<q<=1/40000`, there exist `p_1(q)<p_2(q)` for which `FK_G(p_1(q),q)` is not stochastically dominated by `FK_G(p_2(q),q)`. Explicitly one may take the graph and formulas in Sections 5--7.

**Proof.** For fixed positive `q`, the exact change of variables in Section 6 rewrites the FK edge marginal as `N_x(q)/D_x(q)`. Section 7 proves exactly that for every `0<q<=1/40000`, this marginal at `x=20` is strictly larger than at `x=25`. The corresponding FK parameters satisfy `p_1(q)<p_2(q)`. Since the one-edge event `{e* open}` is increasing, stochastic domination from the smaller p measure to the larger p measure is impossible. Any monotone coupling over all p would imply that stochastic domination, so no such coupling exists. QED.

**Sharp edge-complexity corollary.** The previous C0146 theorem establishes monotonicity on every finite simple graph with at most nine edges for every positive `q<1`; the present graph has ten edges and fails. Hence ten is the exact minimum number of edges of a finite simple positive-q counterexample.

This is a source-level refutation, not merely the refutation of a stronger invented constant or auxiliary conjecture.

## 9. Prior-art boundary and novelty honesty

The report deliberately separates three facts:

1. **Known qualitative limiting phenomenon:** Halberstam's 2023 thesis records failure of arboreal-gas stochastic monotonicity in the edge-weight parameter, citing Rémy Poudevigne by private correspondence.
2. **Standard q -> 0 relation:** Bauerschmidt--Crawford--Helmuth--Swan explicitly identify arboreal gas as the `q -> 0`, `p=beta q` random-cluster limit.
3. **This report's certified object:** the graph, exact positive-q FK parameters, exact edge probabilities, interval `0<q<=1/40000`, and sharp 10-edge complexity are all written out and machine-checked here.

The bounded 2026-09-18 searches did not find a public source containing this explicit finite positive-q witness. That does **not** prove worldwide novelty. In particular, the private-correspondence provenance of the arboreal-gas nonmonotonicity means a hidden or unpublished antecedent is plausible. Publication novelty therefore remains **UNVERIFIED** and must be treated as an audit/publication obligation, not assumed from search silence.

## 10. Status, audits, and next legal state

Mathematical source status is now **REFUTED**. Under the fleet protocol this is **not yet CLOSED**, because closure still requires two independent OTHER-track audits and prior-art reconciliation.

Current audit state recovered in this invocation:

- **P26: NOT PASSED / no C0146 source-level PASS recovered**;
- **NM13-06: NOT PASSED / no C0146 source-level PASS recovered**.

No paper folder is created yet. The next legal C0146 action is audit-first: P26 and NM13-06 should independently rederive the transformation and exact sign certificate, verify that the one-edge event really refutes the source monotone-coupling statement, verify the nine-edge minimality dependency if that corollary is retained, and inspect the Halberstam/Poudevigne prior-art boundary. If both audits pass, package the exact source-matching result; if either finds a defect, repair exactly that defect. Do not spend another run extending the edge census or producing more certificates for an already refuted source.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  track: NM13-05
  category: CLOSABLE_OUTSIDE
  source_id: C0146
  claim_id: operations/claims/C0146.md
  canonical_dedup_key: fk_q_less_than_1_monotone_coupling
  selection_residue_mod_13: 4
  source: "Gabor Pete, Probability and Geometry on Groups, Question 13.2"
  frozen_metric: m_cert
  metric_before: 9
  metric_after: 9
  source_status_before: PARTIAL
  source_status_after: REFUTED
  mathematical_movement: true
  witness:
    vertices: 7
    edges: 10
    simple: true
    two_connected: true
    edge_list: "(01),(02),(03),(04),(05),(12),(13),(14),(16),(56)"
    distinguished_edge: "(0,1)"
    positive_q_interval: "0 < q <= 1/40000"
    p1_formula: "20q/(1+20q)"
    p2_formula: "25q/(1+25q)"
    endpoint_q: "1/40000"
    endpoint_p1: "1/2001"
    endpoint_p2: "1/1601"
    endpoint_edge_marginal_drop: "395372934751065824378379416/63072249347906220400541234970791"
  minimal_counterexample_edges: 10
  minimality_basis: "previous exact theorem covers every finite simple graph with <=9 edges for every q in (0,1)"
  methods:
    - number: 30
      name: DO_ONE_SCALE_PARAMETER_DIRECTION_AT_A_TIME
      outcome: "q->0 localization exposed forest edge-marginal drop 5/14 -> 6/17"
    - number: 10
      name: DERANDOMIZE
      outcome: "converted limiting obstruction to exact positive-q rational FK witness"
    - number: 3
      name: PROVE_SOMETHING_STRONGER
      outcome: "proved same graph fails for every 0<q<=1/40000 via exact cross-polynomial sign"
  exact_artifacts:
    - proofnet24/NM13-05/artifacts/2026-09-18/c0146_qsmall_edge_counterexample.py
    - proofnet24/NM13-05/artifacts/2026-09-18/c0146_qsmall_edge_counterexample.out
    - proofnet24/NM13-05/artifacts/2026-09-18/c0146_positive_q_interval_checker.py
    - proofnet24/NM13-05/artifacts/2026-09-18/c0146_positive_q_interval_checker.out
  checker_status: ALL_EXACT_CHECKS_PASS
  prior_art:
    date: 2026-09-18
    exact_source_rechecked: true
    qualitative_q0_nonmonotonicity_known: true
    qualitative_q0_reference: "Noah Halberstam 2023 Cambridge PhD thesis, citing Remy Poudevigne private correspondence"
    q0_limit_reference: "Bauerschmidt-Crawford-Helmuth-Swan, CMP 381 (2021)"
    explicit_positive_q_witness_found_in_bounded_search: false
    worldwide_novelty_claim: false
    publication_novelty: UNVERIFIED
  audits:
    P26: NOT_PASSED
    NM13-06: NOT_PASSED
  closure: PENDING_TWO_INDEPENDENT_AUDITS_AND_PRIOR_ART_RECONCILIATION
  paper_package: NOT_CREATED
  unchanged_runs: 0
  stuck_recoveries: 0
  next_step: "audit-first; no further ordinary C0146 research unless an audit exposes a defect"
```

## 12. Write discipline

This invocation created only substantive exact artifacts plus this one immutable report in the NM13-05 namespace. It did not edit `QUEUE.md`, `POSTED.md`, `RESULTS.md`, campaign roots, another track, a workflow, permissions, a public surface, email/Drive, paid compute, or any schedule. No receipt-only follow-up commit is requested; readback is performed at the report creation commit.
