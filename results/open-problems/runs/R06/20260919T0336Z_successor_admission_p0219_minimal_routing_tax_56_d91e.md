Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 at maximum, and I do not claim otherwise. PENDING_ADMISSION / NO SOURCE-METRIC MOVEMENT: frozen I0056/H_{5,5} width `0 -> 0`; successor metric `UNMEASURED -> UNMEASURED`; `E_READY_CLOSABLE: 0 -> 0`; methods #4 PROVE SOMETHING WEAKER COMPLETELY, #12 FIND WHAT IS CONSERVED, #24 FIND THE EXTREMAL OBJECT.**

# R06 — successor-admission research: global minimal routing-tax obstruction for P0219

Repository: private `yspennstate/math-open-problems`, branch `master`.

## 1. Frozen R06 source remains frozen

I first recovered the current R06 state and did not reopen the posted/audit-complete subclass.

The original source is Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056:

> What is `Phi_V(G)` for regular, co-regular plane graphs `G`? What are `Phi_E(G)` and `Phi_V(G)` for more general transitive, plane graphs `G`?

The frozen R06 subclass is the regular co-regular tessellation `H_{5,5}` with **outer vertex boundary** normalization. Its certified interval remains

\[
[L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

Thus the `H_{5,5}` subtarget remains **PROVED / audit-complete / frozen / posted**, while the full two-clause source Question 6.20 remains **PARTIAL**. The existing other-track audits are preserved:

- `R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z = PASS_MATH_SCOPE / NOVELTY_UNVERIFIED`;
- `P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15 = PASS_FULL_MATHEMATICAL_PROOF / REGULAR-COREGULAR-FIRST-CLAUSE / SOURCE_PARTIAL / PRIOR_ART_UNVERIFIED`.

The ResearchGate reconciliation in root `POSTED.md` lists *Outer Vertex-Isoperimetry of Regular Plane Tessellations* as publication `414470838`. Posting does not expand the proved scope or close the more-general transitive-plane-graph clause.

### Current primary-literature recheck, dated 2026-09-19

I rechecked the live/corrected Lyons--Peres text and the two principal prior-art families relevant to the frozen result.

1. The current Lyons--Peres book text still prints Question 6.20 in the form quoted above and appends the Haslegrave--Panagiotis degree/codegree `3,4` progress.
2. Haslegrave--Panagiotis, *Site percolation and isoperimetric inequalities for plane graphs*, Random Structures & Algorithms 58 (2021), 150--163, DOI `10.1002/rsa.20946`, explicitly establishes the **vertex** isoperimetric constant for the triangular and square hyperbolic lattices; its introduction says these are exactly the `d'=3` and `d'=4` cases of the Lyons--Peres question. They remain excluded from R06 novelty.
3. Higuchi--Shirai, *Isoperimetric Constants of (d,f)-Regular Planar Graphs*, Interdisciplinary Information Sciences 9 (2003), 221--228, DOI `10.4036/iis.2003.221`, was already recovered in earlier R06 work. Their first constant is the normalized **edge-boundary** Cheeger quantity
   \[
   \alpha(G)=\inf_K\frac{|E(\partial_v K)|}{\sum_{x\in K}\deg_G(x)},
   \]
   and their second is a face/dual boundary constant. This is not the outer vertex-boundary `Phi_V` frozen here. Their face-ball recurrences were nevertheless legitimately used in the R06 upper-bound construction. I do not relabel their theorem as new.

No source-status change from these checks reopens I0056.

The previously rotated Nielsen-Theorem-4 successor also remains terminally handed off and was not reopened.

---

## 2. Repository continuity and admission state

Previous own immutable report:

`runs/R06/20260919T0227Z_successor_admission_p0219_priorart_gate_55_b84e.md`

creation commit:

`7ae7748e178c3e3cbb96fe4fbf0fcea0a0e2ea37`.

Before research I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the operative `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md`, my newest R06 report, current neighboring successor work, and the source/current-status records relevant to the strongest replenishment lead P0219. Large append-only intake JSONLs were handled by candidate-specific indexed/current recovery rather than pretending to visually reread every byte.

The exact GitHub compare from the predecessor R06 creation commit to captured prewrite master

`cfa50b7200aeffed3f76362e0a92e9512607db70`

is complete: **108 commits ahead / 0 behind**, `too_large=null`.

The only canonical claim addition in that material delta is

`operations/claims/P0169.md`,

which is explicitly **CLOSABLE OUTSIDE** and already exclusively owned by `R7-02`. It is therefore not free R06 inventory. No root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, or intake-ledger mutation appears in the exact compare. There is no canonical P0219 claim at the captured state: `operations/claims/P0219.md` returns 404.

The newest coordinator status available before this write, `operations/task_health/runs/2026-09-19T025400Z/status.md`, again records

`E_READY_CLOSABLE: 0 -> 0`.

Therefore R06 remains `PENDING_ADMISSION`; no successor claim is created and no successor source metric is initialized.

---

## 3. Material neighboring delta: P13 proves an exact routing dual and finds a finite routing tax

The main new repository event since the preceding R06 run is

`proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T03-22-00Z__successor-admission-p0219-routing-tax-dual.md`

with exact checker/output

`proofnet24/P13-outside-successor/artifacts/2026-09-19/p0219_routing_tax_counterexample_check.py`

and

`proofnet24/P13-outside-successor/artifacts/2026-09-19/p0219_routing_tax_counterexample_check.out`.

This is **neighboring evidence, not an R06 discovery**. It materially resolves the prior R06 admission ambiguity.

Let `E_n` be the up/right directed edges of the `n x n` square grid and let `C subset E_n` be the deterministic set of closed edges. Write `U_n(C)` for Aldous's minimum number of pairwise edge-disjoint source-to-sink directed paths whose union covers all edges in `C`. Put the closed edges in the reachability poset, with `e < f` when `head(e) <= tail(f)` coordinatewise, and let `W_n(C)` be its width.

P13 proves on the page, using integral lower-bound circulation duality,

\[
\boxed{U_n(C)=\max_{A\subseteq V_n}\left(|C\cap\delta^+(A)|-|\delta^-(A)|\right).}
\tag{3.1}
\]

It also proves

\[
\boxed{W_n(C)=\max_{A\text{ coordinate downset}}|C\cap\delta^+(A)|.}
\tag{3.2}
\]

Consequently the **routing tax** `U-W` is exactly the gain obtained by allowing arbitrary cuts, while charging one unit for every incoming cut edge, instead of restricting to downsets.

P13 then gives an exact `n=4` witness with four closed edges for which

\[
W_4(C)=2,\qquad U_4(C)=3.
\]

Its integer checker independently verifies the cut certificate, three explicit pairwise edge-disjoint covering paths, exhaustive equality of the routing dual with direct path-family enumeration for every closed set on `n=2,3`, and that all `2325` closed subsets of the `4 x 4` grid having at most three closed edges have zero routing tax. The output ends `ALL_EXACT_P0219_ROUTING_TAX_CHECKS_PASS`.

Thus the tempting exact identification `U=W`, which would have reduced P0219 immediately to ordinary Bernoulli Hammersley width, is false.

The maintained Aldous source page is still live on 2026-09-19 and still states

\[
1-v(p)\sim\sqrt{2(1-p)}\qquad(p\uparrow1),
\]

explicitly warning that the heuristic requires a difficult interchange of limits. A fresh bounded exact-title/formula search recovered Aldous's open-problem page and Seppalaeinen's 1997 Bernoulli lattice Hammersley paper, but no checked later primary paper proving this exact oriented-flow asymptotic. This remains bounded negative evidence, not a worldwide novelty certificate.

---

## 4. Method #12 — a conserved alternation count along one directed chain

The P13 witness raises a sharper question than `U=W`: **what is the smallest deterministic closed-edge mechanism that can create positive routing tax on any grid size?**

The key invariant is an entry/exit alternation count.

### Lemma 4.1 — one closed reachability chain never pays routing tax

Let `C` be a nonempty chain in the closed-edge reachability poset. Then, for every `n`,

\[
\boxed{U_n(C)=W_n(C)=1.}
\tag{4.1}
\]

#### Proof

Since `C` is a nonempty chain, `W_n(C)=1`. It remains to prove `U_n(C)<=1` using the exact dual (3.1).

Fix an arbitrary `A subseteq V_n` and list the closed boundary exits

\[
C\cap\delta^+(A)=\{e_1<e_2<\cdots<e_b\}
\]

in chain order. If `b=0`, then the dual objective is nonpositive.

Suppose `b>=1`. Each `e_i` leaves `A`, so immediately after traversing `e_i` a directed walk is outside `A`. Since `e_i<e_{i+1}`, there is an up/right directed connector from `head(e_i)` to `tail(e_{i+1})`. The latter tail lies in `A` because `e_{i+1}` is another boundary exit. Therefore the connector segment between consecutive exits must contain at least one edge entering `A`, i.e. one edge of `delta^-(A)`.

Concatenate

`e_1`, connector `1`, `e_2`, connector `2`, ..., `e_b`.

Because the grid orientation is acyclic and the exits are listed in reachability order, the intervals between successive exits are disjoint along this directed walk. Hence the `b-1` required entry crossings are distinct. Therefore

\[
|\delta^-(A)|\ge b-1.
\]

The dual objective satisfies

\[
|C\cap\delta^+(A)|-|\delta^-(A)|\le b-(b-1)=1.
\]

This holds for every `A`, so (3.1) gives `U_n(C)<=1`. Since every covering path family must use at least one path for nonempty `C`, `U_n(C)>=1`. Thus `U_n(C)=1=W_n(C)`. `QED`.

The invariant is simple but important: **comparable exits from a single abstract Hammersley chain force alternating re-entry crossings, and those re-entry costs exactly cancel all but one exit reward.** Positive routing tax therefore cannot be a one-chain phenomenon.

---

## 5. Method #4 — complete sparse-defect theorem on every grid size

The finite P13 checker established zero tax for all closed sets of size at most three on the `4 x 4` grid. The following argument upgrades that finite observation to **every grid size**.

### Theorem 5.1 — no routing tax with at most three closed edges

For every `n` and every `C subseteq E_n` with `|C|<=3`,

\[
\boxed{U_n(C)=W_n(C).}
\tag{5.1}
\]

#### Proof

The general inequality `W_n(C)<=U_n(C)` is immediate because each actual directed covering path induces a chain in the reachability poset.

For the reverse direction, use (3.1). Fix any `A subseteq V_n`, and abbreviate

\[
b=|C\cap\delta^+(A)|,\qquad r=|\delta^-(A)|.
\]

We must show `b-r<=W_n(C)`.

If `C` is empty this is trivial. If `W_n(C)=1`, then `C` is a chain and Lemma 4.1 already gives the stronger conclusion `U=W=1`.

It remains to consider `W_n(C)>=2`.

- If `r>=1`, then `b<=|C|<=3`, so
  \[
  b-r\le3-1=2\le W_n(C).
  \]
- If `r=0`, then `A` is a coordinate downset. Indeed, if `v in A` and a coordinatewise predecessor `u<=v` were outside `A`, any monotone directed path from `u` to `v` would have to cross at least once from outside `A` into `A`, creating an edge of `delta^-(A)`, contradiction. Therefore all closed exits `C cap delta^+(A)` form an antichain, and hence
  \[
  b\le W_n(C).
  \]

Thus every `A` has dual objective at most `W_n(C)`. Taking the maximum in (3.1) gives `U_n(C)<=W_n(C)`. Combined with the opposite inequality, equality follows. `QED`.

This is a theorem-sized claim with its full argument on the page. It uses P13's on-page exact dual (3.1) as a dependency; that P13 result has an executed exact small-grid self-check but has not received the two independent source-level audits required for closure. I therefore do **not** promote P0219 or call this audited.

---

## 6. Method #24 — the exact smallest extremal routing-tax object

P13 supplies a four-edge set on the `4 x 4` grid with `U-W=1`. Theorem 5.1 proves globally, for **all** grid sizes, that fewer than four closed edges can never have positive routing tax. Therefore:

### Corollary 6.1 — exact minimum cardinality

\[
\boxed{\min\{|C|:U_n(C)>W_n(C)\text{ for some }n\}=4.}
\tag{6.1}
\]

Moreover the P13 witness is extremal even among four-edge sets.

### Corollary 6.2 — maximum four-edge tax

For every `n` and every `C subseteq E_n` with `|C|=4`,

\[
\boxed{0\le U_n(C)-W_n(C)\le1.}
\tag{6.2}
\]

The upper bound is sharp.

#### Proof

If `W_n(C)=1`, Lemma 4.1 gives zero tax. Assume `W_n(C)>=2`. For an arbitrary cut `A`, if `|delta^-(A)|=0`, its dual objective is at most `W_n(C)` because `A` is a downset. If `|delta^-(A)|>=1`, then

\[
|C\cap\delta^+(A)|-|\delta^-(A)|\le4-1=3.
\]

Thus `U_n(C)<=max(W_n(C),3)`. If `W>=3` this gives zero tax; if `W=2` it gives tax at most `1`. P13's four-edge witness has `W=2,U=3`, attaining one. `QED`.

So the **first possible connector conflict is genuinely a four-defect, at-least-two-chain phenomenon**, and at that first cardinality it contributes only one extra path.

This is stronger than the finite `n=4` exhaustive observation: it identifies the global minimal closed-edge cardinality of any routing-tax obstruction, independent of `n`.

---

## 7. What this does and does not buy for Aldous's source conjecture

This sparse-defect theorem is suggestive but does **not** justify the source asymptotic by itself.

Let `q=1-p`. The Bernoulli Hammersley width is of order `n sqrt(q)` in the sequential regime relevant to Aldous. Since positive routing tax requires at least four closed edges and interaction between at least two abstract chains, the first deterministic obstruction is higher-order than an isolated closed edge, pair, or triple.

However the source takes `n -> infinity` **before** `q -> 0`. There are order `n^2` candidate microscopic locations. Consequently it would be invalid to say “four edges means probability `O(q^4)`, hence negligible” without a uniform polymer/contour argument. I make no such claim.

The remaining mathematical admission gate can now be stated more sharply:

\[
\boxed{
\lim_{q\downarrow0}\limsup_{n\to\infty}
\frac{\mathbb E[U_n(C_q)-W_n(C_q)]}{n\sqrt q}=0
}
\tag{7.1}
\]

(or a comparably strong high-probability bound), together with the exact identification of the two-orientation downset width `W_n(C_q)` with the correct Bernoulli Hammersley/LPP shape constant.

The new deterministic information says what such a proof must exploit: every positive-tax contribution must contain an **interaction of at least two reachability chains**, and the minimal interaction uses four closed exits and produces only one unit of excess. A plausible next route is therefore a cluster/polymer decomposition of non-downset cut excursions, proving that connected connector-conflict polymers have an activity summable uniformly in `n` at small `q`. That is a route, not a theorem in this run.

This materially improves the P0219 handoff but does not make it READY. The source metric remains `UNMEASURED` and no claim is created.

---

## 8. Literature log for the active replenishment lead

Fresh dated queries on 2026-09-19 included:

- exact source title: `A discrete Hammersley process as an extreme case of oriented percolation flows`;
- exact conjectural formula: `1-v(p) sqrt(2(1-p))`;
- `Increasing sequences of independent points on the planar lattice` / Seppalaeinen 1997;
- `oriented percolation flows edge-disjoint Hammersley`;
- `routing tax Hammersley path cover edge-disjoint Bernoulli`;
- strict/weak Bernoulli Hammersley variants.

Recovered primary/current sources include:

- David Aldous, maintained open-problem page `https://www.stat.berkeley.edu/~aldous/Research/OP/hammersley_flow.html`, still displaying the conjecture and the interchange-of-limits warning;
- Timo Seppalaeinen, *Increasing sequences of independent points on the planar lattice*, Ann. Appl. Probab. 7 (1997), 886--898, DOI `10.1214/aoap/1043862416`;
- Nicos Georgiou, *Soft edge results for longest increasing paths on the planar lattice*, Electron. Commun. Probab. 15 (2010), DOI `10.1214/ECP.v15-1519`, relevant to the strict Bernoulli-path boundary distinctions.

I did not recover a checked later primary source proving Aldous's exact high-density flow conjecture or the new global four-edge minimal-tax lemma. Those are bounded negative search statements only; they are **not** novelty certificates.

---

## 9. Model / scheduler control status

The configuration limitation is still true in this run. The exposed automation/task-control interface offers prompt/title, schedule/timing mode, enabled state, and related delivery controls. It exposes **no binding model-family selector, no binding reasoning-effort selector, no authenticated per-run model/effort attestation, and no guaranteed hour-long execution field**. Thus `GPT-6 / maximum` remains prompt text only on this surface.

A real fix requires the owning product/platform scheduler or workspace API to expose persistent authorized `model` and `reasoning_effort` (or equivalent) fields plus trustworthy per-run attestation. A prompt cannot make those settings binding.

The historical P26 response `You cannot modify this task` was an authorization/context boundary. `operations/FOLLOWUP_IMPLEMENTATION_2026-09-16.md` preserves that event, while later repository state records successful P26 prompt work from a different authorized context. The lawful workaround is therefore the owning/authorized workspace/account/admin context or product/platform support, not task duplication or permission bypass.

No scheduler setting was changed in this run.

---

## 10. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  category: CLOSABLE_OUTSIDE
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  requested_model_met: false
  frozen_source:
    id: I0056
    source: "Lyons--Peres, Probability on Trees and Networks, Question 6.20"
    exact_question: >-
      What is Phi_V(G) for regular, co-regular plane graphs G?
      What are Phi_E(G) and Phi_V(G) for more general transitive, plane graphs G?
    graph_class: "regular co-regular plane tessellation H_{5,5}"
    parameters: [5, 5]
    normalization: "outer vertex boundary"
    metric_name: "certified interval width U-L for Phi_V(H_{5,5})"
    interval_before: "[sqrt(5), sqrt(5)]"
    interval_after: "[sqrt(5), sqrt(5)]"
    metric_before: 0
    metric_after: 0
    status: "PROVED_FROZEN_POSTED_SUBCLASS; FULL_SOURCE_PARTIAL"
    excluded_prior_art:
      - "Haslegrave--Panagiotis face degrees 3 and 4; DOI 10.1002/rsa.20946"
      - "Higuchi--Shirai 2003 edge/face isoperimetric constants; DOI 10.4036/iis.2003.221; not outer Phi_V"
    audits:
      - "R05-AUDIT-R06-I0056-CLOSURE-01-COR-F5-20260916T151529Z"
      - "P26-AUDIT-R06-I0056-CLOSURE-01-COR-F5-15"
  active_successor:
    claim: null
    state_before: PENDING_ADMISSION
    state_after: PENDING_ADMISSION
    metric_name: UNMEASURED
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    movement: false
    unchanged_runs: NOT_STARTED
  tried_moves: [4, 12, 24]
  method_outcomes:
    4: "proved globally that U_n(C)=W_n(C) whenever |C|<=3"
    12: "entry/exit alternation invariant proves every closed reachability chain has zero routing tax"
    24: "combined global lower-cardinality theorem with P13 witness: minimum positive-tax cardinality is exactly 4; max tax at |C|=4 is exactly 1"
  replenishment_lead:
    id: P0219
    source: "David Aldous, A discrete Hammersley process as an extreme case of oriented percolation flows"
    source_target: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
    lifecycle_before: PENDING_NOT_READY
    lifecycle_after: PENDING_NOT_READY
    canonical_claim_path: null
    current_source_checked_utc: 2026-09-19
    p13_dependency:
      report: "proofnet24/P13-outside-successor/runs/2026-09-19/2026-09-19T03-22-00Z__successor-admission-p0219-routing-tax-dual.md"
      exact_dual: "U=max_A(|C cap delta+(A)|-|delta-(A)|)"
      downset_width: "W=max_downset |C cap delta+(A)|"
      exact_witness: "n=4, |C|=4, W=2, U=3"
      exact_checker_status: "ALL_EXACT_P0219_ROUTING_TAX_CHECKS_PASS"
    new_r06_result:
      theorem_1: "if C is a reachability chain, U=W=1"
      theorem_2: "if |C|<=3 then U=W for every n"
      theorem_3: "minimum |C| with U>W is exactly 4; at |C|=4, U-W<=1 and the bound is attained"
      closure_status: "ON_PAGE_PROOF; DEPENDS_ON_UNAUDITED_P13_DUAL; NOT_SOURCE_CLOSURE"
    remaining_obligation: >-
      Prove the routing-tax contribution is o(n sqrt(q)) uniformly in the source sequential limit,
      or find a checked theorem that gives this, and separately match the two-orientation downset width
      to the correct Bernoulli-Hammersley shape constant. Do not promote P0219 before coordinator-grade admission.
  repository_delta:
    base: "7ae7748e178c3e3cbb96fe4fbf0fcea0a0e2ea37"
    prewrite_head: "cfa50b7200aeffed3f76362e0a92e9512607db70"
    ahead_by: 108
    behind_by: 0
    too_large: false
    added_canonical_claims:
      - "P0169 / R7-02 / CLOSABLE OUTSIDE / already owned"
    canonical_p0219_claim: ABSENT_404
    free_ready_closable: "0 -> 0"
  validation:
    new_checker_created: false
    reason: "new theorem is analytic; reused existing executed P13 exact checker for the finite witness rather than duplicating validation"
    audits_requested: []
  remaining_r06_state: >-
    Remain PENDING_ADMISSION. Do not reopen I0056 or the rotated Nielsen successor.
    Preserve frozen H_{5,5} width zero and wait for/produce a lawful source-current ownership-clear CLOSABLE admission.
```
