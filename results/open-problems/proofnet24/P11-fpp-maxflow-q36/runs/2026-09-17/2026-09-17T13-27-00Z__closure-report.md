Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED.** GPT-6 / maximum was requested in prompt text, but the exposed runtime and scheduler provide no authenticated model selector or reasoning-effort selector, so I do not claim GPT-6 or maximum reasoning. **Frozen metric unchanged: `Q36_global_bracket = 2/2 -> 2/2` (saturated). Source-refutation audit gate MOVES `1/2 -> 2/2` after exact recovery of a distinct P26 end-to-end audit; the required self-contained paper package is now built.**

# P11 / I0062 closure report — literal ADH Question 36 source refutation

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Track: P11 / HARD OUTSIDE successor after the mandatory Lyons/X095 handoff.  
Canonical claim: `operations/claims/I0062.md`.  
Own root: `proofnet24/P11-fpp-maxflow-q36`.

## 1. Executive status

The exact literal source claim is now **CLOSURE-CERTIFIED INSIDE THE REPOSITORY PACKAGE**, with the scope caveats stated below:

`P11-I0062-Q36-SOURCE-REFUTATION-02P`.

The theorem says that if Auffinger--Damron--Hanson Question 36 is read literally as deleting the exponential-moment hypothesis with **no replacement tail condition**, then the answer is negative in the corrected intended Kesten straight-cylinder geometry. There is an iid nonnegative capacity law, finite almost surely, satisfying `F(0)=0` and possessing no positive exponential moment, together with a corrected-Kesten-admissible slowly growing height, for which the normalized maximal flow has an almost-sure subsequence tending to `+infinity`. Therefore the finite law-of-large-numbers conclusion in equation (7.2) does not survive unrestricted deletion of tail control.

This closure statement is deliberately narrower than the stronger replacement-hypothesis problem. It does **not** claim that finite mean is necessary, does not refute Kesten's historically natural second-moment weakening, and does not substitute for P11's separate repaired finite-column-minimum theorem `P11-I0062-FINITE-COLUMN-MIN-SHARP-07R`.

The frozen research metric remains saturated at

`Q36_global_bracket = 2/2`.

There is no metric movement because the source counterexample and the positive bracket work were already mathematically established. The movement in this run is the closure gate:

`independent OTHER-track audits of 02P: 1/2 -> 2/2`.

The previous P11 report's `1/2` audit accounting is superseded by exact commit evidence recovered this run. That earlier statement was a bounded repository-search miss, not a defect in the mathematical proof and not a P11-created audit.

Because the source-closure obligation materially moved, the previous closure-obligation unchanged streak `2` does **not** reach the three-run stuck trigger. No formal stuck-recovery report is required.

## 2. Required repository continuity recovered

At the start of the run I reread/recovered the required control and state surfaces:

- repository `README.md`;
- `proofnet24/HOURLY_PROTOCOL_2026-09-15.md`;
- `operations/FLEET_2026-09-16.md`;
- current `FLEET_RULES.md` / NEW-METHODS directive;
- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- canonical `operations/claims/I0062.md`;
- immutable Lyons-to-I0062 transition report `proofnet24/P11-lyons-entropy/runs/2026-09-17/2026-09-17T00-21-45Z__lyons-handoff-i0062-successor.md`;
- newest supported P11 checkpoint `proofnet24/P11-fpp-maxflow-q36/runs/2026-09-17/2026-09-17T12-13-40Z__run-report.md`, creation commit `b09102d1ebd3ad1c0cd82c991f66b783507d32e6`, blob `fee9f33119346e02279574d780be45729c068321`;
- source-exact proof report `proofnet24/P11-fpp-maxflow-q36/runs/2026-09-17/2026-09-17T09-10-11Z__run-report.md`, creation commit `0217700452f1eca6f878e1ef6aef086f36a98396`;
- the retained exact heavy-tail checker/output;
- current exact repository searches for I0062/02P and recent commits across P26/other tracks.

I did not return to Lyons/X095. Large ledgers and repository searches have bounded connector renderings; exact relevant rows/commits were recovered instead of treating a truncated rendering as exhaustive.

## 3. Closure-gate change: exact recovery of the second independent audit

A fresh descending commit search recovered an immutable P26 audit that the preceding bounded P11 search had missed.

### P26 audit

Report:

`proofnet24/P26-proof-audit-recovery/runs/2026-09-17/2026-09-17_14-56-56__run-report.md`

Creation commit:

`f00d576231bfcc2ac0a91746b0646a1a5eb6a5d7`

Report blob:

`e0cfd0da6b9bc8dc9334a0d20aff9d30bcedcd90`

P26 audit ID:

`P26-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-21 = PASS_FULL_MATHEMATICAL_PROOF / SOURCE_LITERAL_QUESTION_PASS / CORRECTED_HEIGHT_PROVEN / ORIGINAL_1987_HEIGHT_PROVENANCE_UNVERIFIED / PRIOR_ART_UNVERIFIED / CLAIM_SCOPED`.

P26 reconciliation ID:

`P26-RECONCILE-P11-I0062-Q36-02P-2OF2-21 = PASS`.

P26 independently reconstructed the entire mathematical proof rather than relying on P11's conclusion. It checked the capacity law, exact tail, corrected height, independent high-column count, Chebyshev and Borel--Cantelli, explicit feasible flow, and independent min-cut derivation. It also reexecuted the exact finite checker logic and archived

`proofnet24/P26-proof-audit-recovery/artifacts/2026-09-17/2026-09-17_14-56-56__p11_i0062_heavytail_checker_reexecution.out`,

creation commit `bca4de73691ce24a5d74d07c89dcf8a0ac622290`, blob `57ea3526206b3b392a4f2c19418a496825dca8da`, ending `P26-I0062-Q36-EXACT-RECHECK: PASS`.

The associated P26 ledger-delta commit is `d508ef80ee4d0037664ede383a638d68674bdb11` (`P26 ledger delta for I0062 Q36 audit`). P11 did not edit that shared P26 file.

### Existing distinct P04 audit

Report:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T09-42-30Z__run-report.md`

Creation commit:

`2898565e9814059a45cf36ca60c187b457663915`

Blob:

`05792586dc3e473449c4f8476b5fe484c7e945f3`

Audit ID:

`P04-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-10 = PASS (CLAIM-SCOPED)`.

P04 independently reconstructed the same exact source claim, including the binomial/Borel--Cantelli estimate and both primal and cut-side lower bounds.

### Reconciled audit count

The distinct external audit set is therefore

`{P04, P26}`,

so the exact source-refutation package has

`2/2 independent OTHER-track end-to-end audits`.

P11's own proof is not counted as an outside audit. Same-track repetitions and P04's audit of the separate continuous witness are not double-counted.

## 4. Source statement and source-height correction — fresh 2026-09-17 check

The live ADH survey still states Question 36 as:

> Determine if the limit in (7.2) exists without the exponential moment assumption.

The surrounding theorem is the three-dimensional straight-cylinder maximal-flow law of large numbers, with a positivity condition at zero, a height-growth restriction, and a positive exponential moment.

The ADH survey prints Kesten's height condition in the wrong `infinity` direction. P11's earlier Bernoulli zero-horizontal-cut construction proves that the printed direction cannot support the asserted positive theorem. The correction is independently supported by Geoffrey Grimmett's open-access 2021 retrospective, Theorem 7.12, which states

`k^{-1+delta} log n(k) -> 0`

for some `delta>0`, together with the exponential-moment hypothesis. Later exact Théret/Dembin formulations agree with the sub-surface-exponential direction.

The primary Kesten bibliographic record was recovered again:

Harry Kesten, *Surfaces with minimal random weights and maximal flows: a higher dimensional version of first-passage percolation*, Illinois J. Math. 31 (1987), 99--166, DOI `10.1215/ijm/1255989405`.

Project Euclid's available interactive route still returned a security challenge for the article body. Therefore this report does **not** claim a fresh direct page-by-page read of Kesten's 1987 theorem. The mathematical source package uses the corrected intended geometry supported by Grimmett's exact later theorem statement; the counterexample satisfies that corrected condition and hence does not exploit the ADH typo.

## 5. Current prior-art check — dated 2026-09-17

Fresh queries covered the exact Question-36 wording, Kesten's article title/DOI, maximal flow through straight cylinders with heavy tails, moment hypotheses, Rossignol--Théret's no-moment flow constant, and recent maximal-surface work.

The principal neighboring results recovered were:

1. **Rossignol--Théret (2018), EJP 23 no. 99, DOI `10.1214/18-EJP214`, arXiv:1707.08766.** Their abstract explicitly states existence of the flow constant under `G({+infinity})<p_c(d)` without moment assumptions, continuity, and convergence of natural maximal flows. This is major no-moment prior art but does not force the exact arbitrary-slow Kesten straight-cylinder conclusion contradicted by the witness below.
2. **Grimmett (2021), Theorem 7.12.** This provides an exact modern statement of the corrected Kesten height direction and the exponential-moment theorem.
3. **Dembin--Garban, superconcentration for minimal surfaces (2023/2024).** This treats two-valued bounded capacities and fluctuation questions in cylinders; it is not a heavy-tail theorem resolving the present source scope.
4. Current author/citing searches did not surface a published theorem explicitly giving this exact slow-height heavy-tail counterexample or declaring the literal complete-deletion version of Question 36 negatively resolved.

The final item is bounded dated negative evidence only. **Publication novelty/priority remains UNVERIFIED and is not claimed.** The closure certified here is mathematical/source-package closure inside the repository, not a claim of publication priority.

## 6. Full source-exact theorem and proof

### Claim `P11-I0062-Q36-SOURCE-REFUTATION-02P`

There exists an iid nonnegative capacity law, finite almost surely, with `F(0)=0` and no positive exponential moment, and a deterministic height function satisfying the corrected Kesten sub-surface-exponential condition, such that the normalized bottom-to-top maximal flow through the corresponding three-dimensional straight boxes tends to `+infinity` along a deterministic diagonal subsequence almost surely. Consequently the finite law-of-large-numbers conclusion in ADH equation (7.2) fails if the exponential-moment hypothesis is deleted with no replacement tail condition.

### Proof

Define

`P(T=1)=1/2`,

`P(T=2^(s^3))=2^(-s-1)` for integers `s>=1`.

The masses sum to one, so `T` is finite almost surely and `F(0)=0`. For any `gamma>0`,

`E exp(gamma T) >= 2^(-s-1) exp(gamma 2^(s^3))`

for every `s`; the right-hand terms fail to tend to zero, so no positive exponential moment exists.

For `r>=1`, put

`a_r=2^(r^3)`.

Then

`q_r := P(T>=a_r) = sum_{s>=r} 2^(-s-1) = 2^(-r)`.

Use the symmetric slowly growing height

`m(k,l)=max{1, floor(sqrt(log_2(min{k,l})))}`.

It tends to infinity with the horizontal side lengths. For every fixed `delta<1`,

`min(k,l)^(-1+delta) log m(k,l) = O(min(k,l)^(-1+delta) log log min(k,l)) -> 0`.

Hence the height lies safely inside the corrected sub-surface-exponential Kesten regime.

Take

`N_r=2^(r^2)`.

Then `m(N_r,N_r)=r`. The box `[0,N_r]^2 x [0,r]` has

`M_r=(N_r+1)^2`

pairwise edge-disjoint vertical bottom-to-top columns, each containing exactly `r` vertical edges. Call a column `r`-high when all its `r` edges have capacity at least `a_r`. The high-column probability is

`q_r^r=(2^(-r))^r=2^(-r^2)=1/N_r`.

The indicators for distinct columns are independent. Therefore, with `Y_r` the number of high columns,

`Y_r ~ Bin((N_r+1)^2,1/N_r)`

and

`mu_r=E Y_r=(N_r+1)^2/N_r >= N_r`.

Since `Var(Y_r)<=mu_r`, Chebyshev gives

`P(Y_r<mu_r/2) <= 4/mu_r <= 4*2^(-r^2)`.

The error probabilities are summable. The first Borel--Cantelli lemma implies

`Y_r>=mu_r/2`

for all sufficiently large `r`, almost surely.

For the deterministic flow lower bound, there are two independent derivations.

**Primal.** On each high vertical column send `a_r` units upward and send zero elsewhere. High columns are edge-disjoint, every used edge has capacity at least `a_r`, and flow is conserved at each interior column vertex. Hence this is feasible and

`Phi_r >= a_r Y_r`.

**Dual.** Every edge cut separating bottom from top must meet every vertical column. For each high column choose one cut edge on that column. Different columns are edge-disjoint, so these chosen cut edges are distinct; each has capacity at least `a_r`. Thus every separating cut has capacity at least `a_rY_r`. Max-flow/min-cut gives again

`Phi_r >= a_rY_r`.

On the probability-one eventual event,

`Phi_r/N_r^2 >= a_r mu_r/(2N_r^2) >= a_r/(2N_r) = 2^(r^3-r^2-1) -> +infinity`.

This proves the claim. QED.

### Scope bookkeeping

The witness has infinite mean. Therefore the theorem refutes only the complete-deletion reading. It does **not** refute a finite-mean theorem, a second-moment theorem, or the separate finite-column-minimum theorem `07R`. Marie Théret's historical discussion records that Kesten expected a positive result under a second-moment-type weakening; that historically natural positive problem is distinct from the literal source sentence.

## 7. Exact finite certificate

The original P11 exact checker remains

`proofnet24/P11-fpp-maxflow-q36/artifacts/2026-09-17/2026-09-17T01-24-14Z__heavy_tail_vertical_columns_exact_check.py`

with archived PASS output

`proofnet24/P11-fpp-maxflow-q36/artifacts/2026-09-17/2026-09-17T01-24-14Z__heavy_tail_vertical_columns_exact_check.out`.

It checks exact distribution normalization/tail identities and the finite algebra of the high-column probability, expected count, Chebyshev estimate, and normalized lower bound. The theorem-sized asymptotic steps are written above, not inferred from finite testing.

For the self-contained paper package I copied the exact logic into `check.py` and reran it locally with exact rational arithmetic before archiving its output. The package output ends

`P11-I0062-Q36-SOURCE-REFUTATION-02P exact finite core: PASS`.

## 8. Required self-contained paper package — BUILT

Package root:

`proofnet24/P11-fpp-maxflow-q36/paper_q36_heavytail_refutation/`

### README

Path:

`proofnet24/P11-fpp-maxflow-q36/paper_q36_heavytail_refutation/README.md`

Creation commit:

`4f96031b4dd4f629298eeb194e69cd99addad373`

Blob:

`47a969ca2d67327d7c6b6a331df39ea3902e5edf`

The README states the exact source/proved-scope distinction, source-height correction, theorem, checker provenance, two audits, dated prior-art status, and publication-novelty limitation.

### Manuscript

Path:

`proofnet24/P11-fpp-maxflow-q36/paper_q36_heavytail_refutation/main.tex`

Creation commit:

`7c66c8eb4b5f1cfaa37d0b85269fc05660cd5ea6`

Blob:

`8c06ca5ab0b9e30490e3636e0643adefb421d320`

The manuscript is self-contained and includes the full source-exact theorem, source-height correction, complete Borel--Cantelli proof, independent primal/dual lower bounds, scope caveats, prior-art discussion and audit record.

### Exact checker

Path:

`proofnet24/P11-fpp-maxflow-q36/paper_q36_heavytail_refutation/check.py`

Creation commit:

`e9c40c8a48952811a356a64b7b034729e748a501`

Blob:

`a715a929094b5ec0dbc416fc792f2e0447fa4c0b`

### Executed checker output

Path:

`proofnet24/P11-fpp-maxflow-q36/paper_q36_heavytail_refutation/check.out`

Creation commit:

`2c44bb20d466eb8b1ca34c7e0f30e5ad826fade3`

Blob:

`fa34eaf0a1f77b03b6fffd63f5e2aa29625f2c0e`

Output: PASS.

The package is source-exact for the literal deletion scope and intentionally does not merge in the broader `07R` theorem.

## 9. Separate stronger theorem remains separate

`P11-I0062-FINITE-COLUMN-MIN-SHARP-07` remains WITHDRAWN AS WRITTEN because its first arbitrary-rectangle proof used only `L^1` stationarity.

Repaired

`P11-I0062-FINITE-COLUMN-MIN-SHARP-07R`

remains internally proved / not independently closure-certified as a separate strengthening. It uses `2r_*` disjoint shells to give fixed-height anchored block costs in `L^{3/2}`, Dunford--Zygmund for arbitrary rectangular averages, the fixed-height envelope bridge `lambda_H downarrow nu_G`, finite-box embedding, and separate uniform integrability for `L^1`. Its clean outside-audit count remains a separate bookkeeping question and is not used to close 02P.

Retained structural claim09 and its endpoint refinements likewise remain useful stronger boundary information but are not needed for literal source closure.

## 10. Independent peer audit duty

I independently audited a new peer lemma, distinct from the previous P11 peer audit:

Claim:

`P04-I0101-MAXDET-SPARSE-TANGENT-ODE-24`.

Source report:

`proofnet24/P04-closure-local-paley/runs/2026-09-17/2026-09-17T12-44-05Z__run-report.md`

Creation commit:

`30378fdb2fc244279fb2ae9ed1910ae84f8f8ad0`

Blob:

`af5f4643a24980c5dd3a9ca37bb1382fed11ccf1`.

Peer statement: for the maximum-determinant correlation-completion path `C_z`, with `P_z=C_z^{-1}`, support space `S` consisting of the diagonal and graph edges, `B=-A`, and

`L_C(Z)=Pi_S(C Z C)`,

the operator `L_C:S->S` is invertible and

`Z_z=L_{C_z}^{-1}(B)`, `P_z'=-Z_z`, `C_z'=C_z Z_z C_z`,

with the dissipation derivative

`M_H'(z)=Tr(Z_z C_z Z_z C_z)=<Z_z,B>>0`,

and at the origin `Z_0=-A`, `C_0'=-A`, `P_0'=A`.

### Independent verification

For nonzero symmetric `Z in S`, because `Pi_S` is orthogonal projection and `Z` already lies in `S`,

`<Z,L_C Z>=Tr(Z C Z C)=||C^(1/2) Z C^(1/2)||_F^2>0`.

Thus `L_C` is self-adjoint positive definite on the finite-dimensional support space and is invertible.

The maxdet KKT equations make every nonedge entry of `P_z` identically zero, hence every nonedge entry of `P_z'` is zero. With `H_z=C_z'`, differentiating `P_z=C_z^{-1}` gives

`P_z'=-P_z H_z P_z`.

Therefore `Z_z:=P_z H_z P_z=-P_z'` lies in `S`, and multiplication by `C_z` on both sides gives

`H_z=C_z Z_z C_z`.

The prescribed covariance entries have derivative zero on the diagonal and `-1` on edges, so

`Pi_S(H_z)=B`.

Hence `L_{C_z}(Z_z)=B`, proving the ODE identities.

For the monovariant one can avoid importing the preceding peer derivative claim: by the envelope/KKT support condition,

`d/dz log det C_z = <P_z,B>`.

Therefore

`M_H(z)=-<P_z,B>`

and

`M_H'(z)=<-P_z',B>=<Z_z,B>`.

Since `L_{C_z}(Z_z)=B`,

`<Z_z,B>=<Z_z,C_z Z_z C_z>=||C_z^(1/2) Z_z C_z^(1/2)||_F^2>0`.

At `z=0`, `C_0=I`, so `L_I` is the identity on `S`, `Z_0=B=-A`, and the stated derivatives follow.

Verdict:

`P11-AUDIT-P04-I0101-MAXDET-SPARSE-TANGENT-ODE-23 = PASS (CLAIM-SCOPED)`.

No finite checker is warranted for this analytic linear-algebra lemma; the proof is exact on the page.

## 11. Dependency/status ledger

- `P11-I0062-TRUNCATION-LIMINF-01`: **PROVED**.
- `P11-I0062-HEAVYTAIL-VERTICAL-COLUMNS-02`: **PROVED**.
- `P11-I0062-Q36-SOURCE-REFUTATION-02P`: **PROVED; SOURCE-LITERAL REFUTATION CLOSURE-CERTIFIED IN REPOSITORY PACKAGE**.
- `P11-I0062-FINITE-MEAN-OFFSET-BLOCK-04`: **PROVED**.
- `P11-I0062-COLUMN-MIN-MOMENT-05`: **PROVED / structural + obstruction**.
- `P11-I0062-FINITE-COLUMN-MIN-SHARP-07`: **WITHDRAWN AS WRITTEN**.
- `P11-I0062-FINITE-COLUMN-MIN-SHARP-07R`: **PROVED internally / stronger replacement theorem / separate audit-prior-art package not used for source closure**.
- `P11-I0062-CONTINUOUS-SLOWTAIL-WITNESS-08`: **PROVED / supplementary**.
- `P11-I0062-TAIL-ESCAPE-EQUIVALENCE-09`: **PROVED / structural**.
- ADH printed Kesten height direction: **DISPROVED AS A TRANSCRIPTION / RENDERING OF THE INTENDED THEOREM**; corrected zero-direction supported by exact later sources.
- direct Kesten-1987 article-body provenance: **UNVERIFIED through the available interactive source path**.
- publication novelty/priority of 02P: **UNVERIFIED; bounded search only**.

## 12. `ledger_delta` for P26

```text
ledger_delta:
  track: P11
  canonical_claim: I0062
  exact_claim: P11-I0062-Q36-SOURCE-REFUTATION-02P
  frozen_metric: Q36_global_bracket=2/2 -> 2/2
  audit_gate_before_supported_P11_accounting: 1/2
  recovered_P26_audit: P26-AUDIT-P11-I0062-Q36-SOURCE-REFUTATION-02P-21
  recovered_P26_creation_sha: f00d576231bfcc2ac0a91746b0646a1a5eb6a5d7
  recovered_P26_blob: e0cfd0da6b9bc8dc9334a0d20aff9d30bcedcd90
  distinct_other_audits: P04 + P26
  audit_gate_after: 2/2 PASS
  reconciliation: P26-RECONCILE-P11-I0062-Q36-02P-2OF2-21 = PASS
  source_literal_status: REFUTED / CLOSURE-CERTIFIED IN REPOSITORY PACKAGE
  package_root: proofnet24/P11-fpp-maxflow-q36/paper_q36_heavytail_refutation/
  publication_novelty: UNVERIFIED
  original_1987_body_provenance: UNVERIFIED
  stronger_07R_scope: separate; do not transfer this closure automatically
```

P11 made no edit to P26's ledger or peer files.

## 13. Retirement / handoff status

The exact chosen closure claim has now met the user's stated gate:

1. source-matching full mathematical proof on the page: **yes**;
2. exact finite certificate where applicable: **PASS**;
3. current source/prior-art search with explicit limitations: **yes**;
4. two distinct independent OTHER-track end-to-end audits: **P04 + P26, 2/2**;
5. required self-contained `paper_<name>/` folder: **built and read back in part at exact creation commits**.

Accordingly **the literal source-refutation target is ready for P11 retirement**. No successor target is claimed in this report, and no shared root ledger/peer file is edited. The stronger finite-`r_*` theorem remains a separate research strengthening and should not be silently conflated with source closure.

The closure-obligation unchanged streak resets: this run obtained the missing second audit and completed the package. The formal stuck trigger is therefore not reached.

No email/Gmail, Drive, public posting, paid compute, permission change, workflow execution, or extra schedule was used.

**END_OF_CANONICAL_REPORT_P11_2026-09-17T13-27-00Z**
