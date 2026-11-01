Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FROZEN-METRIC MOVEMENT: `m_cert = 9 -> 9`; secondary exact witness interval improves from `0 < q <= 1/40000` to `0 < q <= 1/32618`. Source status remains REFUTED; fleet closure remains PENDING P26 + NM13-06. Section-B methods actually tried: #5 ADD A PARAMETER AND DIFFERENTIATE IN IT, #22 READ THE FAILURES NOT THE SUCCESSES, #24 FIND THE EXTREMAL OBJECT.**

# NM13-05 / C0146 — derivative-guided sharpening of the positive-q obstruction

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
Certified positive-q witness interval before / after: **`(0,1/40000] -> (0,1/32618]`**  
Exact counterexample complexity: **10 edges**, already minimal by the preceding all-graphs theorem through 9 edges  
Unchanged-run counter: **0 -> 1** (the frozen metric did not move)  
Stuck recoveries: **0 -> 0**  
Required closure auditors: **P26 and NM13-06; neither has a C0146 PASS recovered in this invocation**

## 1. Runtime and control-plane disclosure

The prompt requests GPT-6 with maximum reasoning. This invocation actually identifies as **GPT-5.6 Sol**. Authenticated reasoning-effort telemetry is unavailable, so reasoning level is **UNVERIFIED**. I do not claim GPT-6, a binding maximum-reasoning setting, an hour-long execution, or a support escalation.

The exposed scheduler/task-control schema still has prompt/title, scheduling or start, timing mode, enabled state and task identifiers, but no model-family selector and no reasoning-effort selector. Thus `GPT-6 / maximum` remains prompt text only. Making it binding would require an owner-authorized product/workspace/API/admin surface exposing persistent model/effort controls and authenticated per-run runtime attestation. The historical P26 `You cannot modify this task` response remains an authorization-context boundary; current repository policy records that another authorized context later succeeded. A lawful workaround is the owning/otherwise-authorized context or authorized platform/admin support, never duplication, permission changes or access-control bypass. No schedule was modified in this invocation.

## 2. Continuity, ownership and current audit gate

This is a continuation of the already admitted **C0146** claim. Intake was not reopened and no new claim was created.

Before doing new mathematics I reread or exact-target-recovered the current controlling state from:

- `FLEET_RULES.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/NEW_METHODS_2026-09-16.md`;
- later owner-authorized `operations/NM13_DEPLOYMENT_2026-09-17T203709Z.md`;
- root `QUEUE.md`, `POSTED.md`, and `RESULTS.md`;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- canonical claim `operations/claims/C0146.md`;
- newest own report `proofnet24/NM13-05/runs/2026-09-18/2026-09-18T12-02-00Z__c0146-positive-q-refutation.md`;
- newest neighboring NM13-04 state, now the P0457 six-run handoff/successor screen at commit `2ea9d407ac1e3b8c6c9dc3e1b8ffeb7fb0d24563`;
- newest recovered designated-auditor NM13-06 run, still the `11-35-00Z` successor-admission screen at commit `ef730547c0c81258b1c813ff59da1e84daa075fa`;
- current P26 report/search state and exact C0146 ownership/audit searches;
- the C0146 intake/dedup alias evidence already frozen in the canonical claim.

The large root ledgers and JSONL intake files can be connector-truncated. I therefore do not claim a byte-for-byte serial rendering of every repository file in this invocation. Exact canonical claim files, current immutable report paths, current branch/commit metadata, source rows and exact-ID/dedup/audit searches are used as continuity anchors; truncated history is never treated as a release.

The canonical C0146 claim still names NM13-05 as exclusive owner. No release, retirement, POSTED/campaign settlement, competing owner, P26 C0146 PASS or NM13-06 C0146 PASS was recovered. P26's newest recovered report is itself a thinking-only audit-bottleneck run and does not contain a C0146 audit verdict. Therefore the source stays with NM13-05, but **closure remains blocked on the two required outside audits**.

## 3. Exact source and dated literature refresh — 2026-09-18

The current primary source remains Gábor Pete, *Probability and Geometry on Groups*, live PDF dated **April 3, 2024**, Question 13.2 on PDF page 184 / printed page 185. It literally asks whether there is a monotone coupling `(omega_p)_{p in [0,1]}` of `FK(p,q)` for any `q in [0,1)`. The present witness uses **strictly positive q**, so it avoids any endpoint convention at `q=0`.

Fresh bounded searches included `FK(p,q) monotone coupling q<1`, `random-cluster q<1 monotonicity`, `arboreal gas stochastic monotonicity Poudevigne`, and recent 2026 q<1 random-cluster work. The current 2026 papers surfaced by these searches concern negative dependence on wired trees or high-degree regular graphs; they do not supply this finite-graph monotone-in-p coupling result.

The important prior-art overlap remains Noah Halberstam's 2023 Cambridge thesis *A Walk through the Forest: the Geometry and Topology of Random Systems*. It states that the finite-graph arboreal gas is **not stochastically monotone in its parameter**, attributing the fact to **Rémy Poudevigne, private correspondence**. The same thesis, and Bauerschmidt--Crawford--Helmuth--Swan's published arboreal-gas work, identify the arboreal gas as the `q -> 0` random-cluster limit under `p/q -> beta` (equivalently the usual fixed forest-fugacity scaling).

This changes how novelty must be described. A strict finite arboreal-gas stochastic-order failure, if one has the unpublished witness behind the private correspondence, transfers by finite-dimensional continuity to some sufficiently small **positive** q along `p_i(q)=x_i q/(1+x_i q)`. Thus the *conceptual mechanism* behind small-positive-q failure is not safely claimable as new. What is public in the thesis is an attributed qualitative statement, not the graph or an auditable exact witness. The bounded searches still did **not** expose the present 10-edge graph, the rational endpoint below, or an explicit published positive-q interval. Accordingly:

- mathematical source status in this track remains **REFUTED** by our explicit positive-q certificate;
- publication novelty of the explicit 10-edge / positive-q result remains **UNVERIFIED**;
- the eventual audits must treat Halberstam/Poudevigne as serious prior art and must not advertise the `q -> 0` idea itself as novel.

A bounded negative search is not evidence of worldwide novelty.

## 4. Frozen metric versus the secondary witness parameter

The frozen metric is unchanged:

`m_cert` = largest `m` for which NM13-05 has a rigorous source-valid certificate that every finite simple graph with at most `m` edges is stochastically monotone in `p` for every `q in (0,1)`.

The preceding exact theorem gives `m_cert=9`, and the preceding 10-edge witness makes 10 the exact minimum finite-simple-graph counterexample complexity. This run does not rename that metric, so **`m_cert=9 -> 9`** and the unchanged-run counter advances **0 -> 1**.

There is nevertheless real source-relevant strengthening of the already-certified counterexample: the exact interval on which one fixed graph provably violates monotonicity expands from `(0,1/40000]` to `(0,1/32618]`. This secondary quantity is reported explicitly but is not substituted for `m_cert`.

The endpoint increases by the exact factor

`(1/32618)/(1/40000) = 20000/16309 > 1`,

about 22.63%.

## 5. Method #5 — ADD A PARAMETER AND DIFFERENTIATE IN IT

Keep the same 7-vertex, 10-edge graph from the source refutation,

`E={(0,1),(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,6),(5,6)}`,

with distinguished edge `e*=(0,1)`. For `q>0` set

`x = p/[q(1-p)]`, hence `p=xq/(1+xq)`.

For this graph define exact polynomials

`D(x,q)=sum_A x^{|A|} q^{c(A)}`,

`N(x,q)=sum_{A contains e*} x^{|A|} q^{c(A)}`,

where `c(A)=|A|-7+k(A)` is cycle nullity. The edge marginal is

`M_q(x)=N(x,q)/D(x,q)`.

Instead of guessing two widely separated `x` values, differentiate:

`dM_q/dx = G(x,q)/D(x,q)^2`,

`G=N_x D-N D_x`.

Exact enumeration makes `G` an integer bivariate polynomial. Numerical solution of the **exactly derived** equations `G=0`, `dG/dx=0` was used only as route scouting, not as a theorem. It locates the disappearance of the negative-derivative pocket near

`x approximately 20.4840312263587`,

`q approximately 0.0000306579402683398`.

That immediately explains why the earlier coarse pair `x=20,25` stopped at a smaller q: it straddles the right region, but far too coarsely.

**Outcome #5:** differentiation found the narrow extremal region and supplied a principled target for exact rationalization. The decimal saddle is heuristic guidance only; no sharp-threshold claim is made from it.

## 6. Method #24 — FIND THE EXTREMAL OBJECT: rationalize the derivative pocket

Guided by the derivative pocket, choose two very close exact rational fugacities

`x1 = 512/25 = 20.48`,

`x2 = 2049/100 = 20.49`.

Let `D_i(q)=D(x_i,q)` and `N_i(q)=N(x_i,q)`. The sign of the edge-marginal difference is the sign of

`H(q)=N_1(q)D_2(q)-N_2(q)D_1(q)`.

After clearing one common positive denominator, the exact ascending coefficient list is

`[`
`986531766884142045004854319525937500000000000,`
`-32143509596466558162391026506370142400687500000000,`
`-1146450076641884513896040584662442340620694062500000,`
`-16463066302403334230838924672590135582374476301562500,`
`-124838805506322909059280302383078512952746815601265625,`
`-551294838926831492907614492140885444938167683645440000,`
`-1396895177743892375801230881843324555409397430563635200,`
`-1539243308922527919763929859402064180194372632390402048`
`]`.

The constant term is positive and **every nonconstant coefficient is negative**. Hence `H'(q)<0` for all `q>0`. At

`q0=1/32618`,

exact arithmetic gives

`H(q0) = 3059721428192140729677709720042967828909885630965023987229789597682419 / 1873144967280370161332960272637939453125000000000000000000000000 > 0`.

Therefore `H(q)>0` for every `0<q<=1/32618`.

For each such q define

`p1(q)=x1 q/(1+x1 q)`, `p2(q)=x2 q/(1+x2 q)`.

Then `p1(q)<p2(q)` but

`P_{FK(p1(q),q)}(e* open) > P_{FK(p2(q),q)}(e* open)`.

Because `{e* open}` is increasing, stochastic domination fails, so no monotone coupling in p exists. Thus the same 10-edge graph gives the certified interval

**`0 < q <= 1/32618`.**

At the exact right endpoint,

`p1 = 256/407981`,

`p2 = 2049/3263849`,

and the edge probabilities are

`P1 = 13497273509071773805642009057600701796864 / 38188477772779164561962899231286395649889`,

`P2 = 227097780491540948519918200390273843901961405801 / 642538549487122449716007539469431589617741514001`,

with exact positive reversal

`P1-P2 = 65659206279454767316202326084448371475909637836063916062803471774477067725 / 1291451006065407417825123791982739179970979856393742659933835109721438845221985851978731 > 0`.

The tiny size of the endpoint drop is why a floating-point-only search would be inadequate. The proof itself is rational arithmetic.

**Outcome #24:** the fixed-graph positive-q interval advances from `1/40000` to `1/32618`, nearly reaching the derivative-scouted transition without making an uncertified sharpness claim.

## 7. Exact finite certificate

Only after the derivative/extremal route produced a stronger statement did I write the exact checker:

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_sharp_q_threshold_checker.py`

created at commit

`a739e8efd290329f7e30cf6074d46e2b85e1591b`.

It uses only Python standard-library exact integer/Fraction arithmetic. It independently enumerates all `2^10=1024` edge configurations, reconstructs `D_i,N_i`, checks the cleared `H` coefficient list, proves the sign pattern, verifies the endpoint rational value, converts back to exact source `p` parameters, checks the exact marginal reversal, and tests representative points in the certified interval.

I executed that file locally as written. The complete stdout is archived at

`proofnet24/NM13-05/artifacts/2026-09-18/c0146_sharp_q_threshold_checker.out`

created at commit

`1ecd85a2502f4aa05418979aa49d8a689fc7b761`.

It ends exactly

`ALL_EXACT_CHECKS_PASS`.

This is a self-check, not an independent audit.

## 8. Method #22 — READ THE FAILURES, NOT THE SUCCESSES: prior-art reconciliation

The most informative failure is not mathematical. It is novelty discipline.

The previous exact positive-q result could easily be over-described as a wholly new nonmonotonicity mechanism. Halberstam's thesis prevents that. Its explicit statement, attributed to Poudevigne private correspondence, says arboreal gas is not stochastically monotone in its fugacity. For a finite graph this means there exist `beta1<beta2` and some increasing event with a strict probability reversal. Since finite random-cluster probabilities in the scaling `p_i(q)=beta_i q/(1+beta_i q)` are ratios of finite polynomials in q with positive denominators and converge to the corresponding arboreal-gas probabilities, any such strict finite witness persists for all sufficiently small positive q.

So the broad *idea* `q=0 obstruction -> small positive q obstruction` follows by continuity once the private-correspondence witness is granted. The public thesis does not expose the witness needed to turn that sentence into a reproducible exact certificate, and the bounded searches did not expose one elsewhere. The present graph and exact interval therefore remain mathematically useful, but the report explicitly downgrades novelty rhetoric:

- **not claimed novel:** qualitative arboreal-gas nonmonotonicity or the continuity-transfer idea;
- **explicitly certified here:** a 7-vertex/10-edge simple graph, a one-edge increasing event, exact positive q, exact p values, minimal edge complexity relative to our all-graphs-through-9 theorem, and now the interval through `1/32618`;
- **publication novelty:** UNVERIFIED until the audits search harder, including for material deriving from the Poudevigne communication.

**Outcome #22:** the prior-art boundary is sharper and safer. This is materially useful even though it does not move `m_cert`.

## 9. Why the source remains REFUTED but not fleet-CLOSED

The exact positive-q witness already answers the universal source question negatively, and this run strengthens that witness interval. The mathematical source label therefore remains **REFUTED**.

Fleet closure is still **not** claimed. Under the controlling protocol the missing obligations are:

1. **P26 independent full-proof audit: NOT PASSED / no C0146 PASS recovered**;
2. **NM13-06 independent full-proof audit: NOT PASSED / no C0146 PASS recovered**;
3. prior-art reconciliation in those audits must explicitly inspect the Halberstam/Poudevigne antecedent rather than treating a bounded search as a novelty certificate;
4. only after both outside audits pass may a source-matching `paper_<name>/` folder be created and called closed.

No paper folder is created in this run.

## 10. Next step

The next legal high-value action is **audit-first**, not another edge census. P26 and NM13-06 should independently rederive the source mapping, recompute the exact finite graph probabilities, verify the all-graphs-through-9 minimality dependency if that auxiliary claim is retained, and determine how the Poudevigne private-correspondence prior art changes the publishable claim.

If an auditor finds a mathematical defect, resume C0146 from that exact defect. If audits merely request a sharper public statement, fresh unused methods available include #18 SAY IT IN ANOTHER LANGUAGE, #26 HUNT THE SPORADIC CASE, and #29 ADD THE POINTS AT INFINITY. They are not reported as tried in this invocation.

## 11. Structured ledger_delta for P26

```yaml
ledger_delta:
  worker: NM13-05
  category: CLOSABLE_OUTSIDE
  source_id: C0146
  claim_file: operations/claims/C0146.md
  canonical_dedup_key: fk_q_less_than_1_monotone_coupling
  source_status_before: REFUTED
  source_status_after: REFUTED
  frozen_metric:
    name: m_cert
    before: 9
    after: 9
    movement: false
  secondary_certified_parameter:
    name: fixed_10_edge_graph_positive_q_interval_endpoint
    before: 1/40000
    after: 1/32618
    interval_after: "0 < q <= 1/32618"
    endpoint_ratio_new_over_old: 20000/16309
  minimum_counterexample_edges: 10
  methods_attempted:
    - 5: derivative in x=p/[q(1-p)] located the narrow nonmonotone pocket
    - 22: Halberstam/Poudevigne prior-art failure mechanism reconciled; novelty narrowed
    - 24: rationalized near the derivative pocket to x1=512/25, x2=2049/100
  finite_certificate:
    checker: proofnet24/NM13-05/artifacts/2026-09-18/c0146_sharp_q_threshold_checker.py
    checker_commit: a739e8efd290329f7e30cf6074d46e2b85e1591b
    output: proofnet24/NM13-05/artifacts/2026-09-18/c0146_sharp_q_threshold_checker.out
    output_commit: 1ecd85a2502f4aa05418979aa49d8a689fc7b761
    result: ALL_EXACT_CHECKS_PASS
  audit_state:
    P26: NOT_PASSED_NO_C0146_PASS_RECOVERED
    NM13-06: NOT_PASSED_NO_C0146_PASS_RECOVERED
  unchanged_runs:
    before: 0
    after: 1
  stuck_recoveries:
    before: 0
    after: 0
  literature_status:
    date: 2026-09-18
    novelty: UNVERIFIED
    material_overlap: "Halberstam 2023 states arboreal-gas nonmonotonicity, crediting Remy Poudevigne private correspondence; no public exact witness recovered"
  next_step: "P26 and NM13-06 independent audits plus prior-art reconciliation; no further census unless an audit exposes a mathematical defect"
```

## 12. Safeguards

No shared root, peer namespace, canonical claim, workflow, permission, public surface, email/Gmail, Drive item, paid compute, or schedule was modified. The only pre-report writes were the substantive exact checker and its executed output in NM13-05's own artifact namespace. This file is the invocation's sole immutable report. It must be read back at its creation commit; no receipt-only follow-up commit is authorized.
