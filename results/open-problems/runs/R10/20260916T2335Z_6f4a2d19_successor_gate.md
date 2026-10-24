Model actually running: GPT-5.6 Sol. Reasoning: UNVERIFIED — NO MOVEMENT in the retired I0070 frozen metric (`theta_* = 1/2` as a supremum before and after; endpoint `theta=1/2` not claimed). This is a successor-gate run, not a seventh I0070 research attack. Section-B moves actually used: **#20 FIND WHY THE ALGORITHM FAILS, #22 READ THE FAILURES / LATER LITERATURE, #26 HUNT THE SPORADIC CASE**.

Problem/source handed off: Antonio Agresti and Mark Veraar (2025), *Nonlinear SPDEs and Maximal Regularity: An Extended Survey*, Problem 6 / intake I0070. The source asks for the critical Hilbert `p=2` extension of Theorem 5.7 under the source critical equality. R10's retained author-side candidate is `R10-I0070-C006`; campaign status remains **PARTIAL / RETIRED-HANDOFF**, not closure.

# R10 successor-gate report after I0070 six-run retirement

Repository/branch: `yspennstate/math-open-problems` / `master`.
Dated check: 2026-09-16 UTC / 2026-09-17 Asia/Jerusalem.

## 1. Continuity: I0070 stays retired in this slot

I continued from the immutable handoff

`runs/R10/20260916T2236Z_i0070_sixrun_handoff_gate.md`.

That report reached the owner-defined six-unchanged-run CLOSABLE retirement threshold. I therefore did **not** restart Agresti--Veraar Problem 6, did not manufacture a seventh endpoint lemma, and did not increment the retired streak beyond 6.

Retained mathematical state:

- fixed metric: `theta_* = 1/2` as a supremum;
- endpoint `theta=1/2`: not claimed (and not required by Theorem 5.7);
- strongest retained source-level candidate: `R10-I0070-C006 — AUTHOR-SIDE PROVED / EXTERNAL AUDIT REQUIRED` in `runs/R10/20260916T2138Z_i0070_progressive_representative.md`;
- campaign status: **PARTIAL**;
- required independent audits of C006 located in the current repository search: **0/2**;
- canonical `operations/claims/I0070.md` still literally says `PENDING_ADMISSION, not READY`; I did not edit that coordinator-owned claim file.

The Cardy route previously occupying R10 remains separately preserved in earlier R10 reports and stays retired from this slot; nothing here relabels or deletes it.

## 2. Required repository/control read

Before successor screening I read/recovered the current campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the newest own R10 handoff, the newest available R11 package, and current canonical claims around the CLOSABLE queue front. Large intake JSONL files are connector-truncated when rendered wholesale; I used exact-ID/source searches across the intake ledgers and do **not** falsely claim a literal byte-for-byte visual reread of all roughly 780 rows.

The current shared ledger is known to lag some R-series reports; I therefore use own immutable reports plus current claims/status screens rather than resetting any value from a stale shared row.

## 3. Move #20 — why successor dispatch fails right now

The successor algorithm is: take the highest eligible CLOSABLE outside queue item, verify exact source/current status/prior history/no owner, then create a canonical claim create-only. It currently fails at the **admission/ownership gate**, not at GitHub access.

The most recent repository-wide rotation screens already show the high-ranked CLOSABLE front as occupied, resolved/held, metadata-incomplete, or otherwise not READY. In particular, D0007--D0010 have acquired distinct owners; I0077, I0079, I0082, I0095, I0110, I0113, I0004 and I0075 are owned; I0098 is on a resolution hold; I0105/I0106 still lack sufficient source metadata for clean dispatch; and the recent coordinator queue screen had no newly certified READY/unassigned successor.

I did not treat an old intake `admitted=true` flag as current verification, did not overwrite another track's claim, and did not assign a successor metric a fake zero baseline.

## 4. Moves #22 and #26 — I0087 is not a lawful fresh-open successor

I specifically hunted the apparently unclaimed queue item `I0087`, because it looked like a concrete finite-geometry CLOSABLE candidate rather than another broad classification problem.

The original source is Matteo D'Achille, Nicolas Curien, Nathanael Enriquez, Russell Lyons and Meltem Unel, *Ideal Poisson--Voronoi tessellations on hyperbolic spaces*, arXiv:2303.16831, Question 7.1 (Other manifolds). The current source asks:

> For which homogeneous Riemannian manifolds does the low-intensity Poisson--Voronoi limit exist? For example, does it exist on the Riemannian product `H_2 x R`?

Primary locator checked:
`https://arxiv.org/html/2303.16831`, Question 7.1, lines in the current HTML around the Future Directions section.

A later primary source makes the queue item's highlighted `H^2 x R` scope unsafe to dispatch as an open problem:

Matteo D'Achille and Ali Khezeli, *Convergence towards Ideal Poisson--Voronoi tessellations with a focus on Diestel--Leader graphs*, arXiv:2606.30517 (29 June 2026).

Its Theorem 1.2 gives necessary and sufficient conditions for full convergence toward a unique IPVT on proper pointed measured metric spaces, and the introduction states that the product machinery applies to examples including

`H^2 x H^2`, **`H^2 x R`**, regular trees, products of regular trees, and Diestel--Leader graphs, with those cases discussed in Section 5. Section 5.4 then develops convergence for products.

Primary locator checked:
`https://arxiv.org/html/2606.30517`, especially introduction around Theorem 1.2 and Section 5.4.

**Verdict for R10 dispatch:** `I0087 = NOT READY AS A FRESH OPEN CLOSABLE SUCCESSOR`. At minimum, the source-highlighted `H^2 x R` example is later covered by a general convergence theorem/product treatment. I do not claim the later paper completely classifies every homogeneous Riemannian manifold in the broad first sentence of Question 7.1; the narrower queue scope is enough to reject dispatch. No I0087 claim was created.

This is a real successor-screen update relative to the prior R10 handoff: the apparent unclaimed candidate is now excluded by dated later-literature evidence rather than merely left metadata-incomplete.

## 5. No lawful successor admitted in this bounded run

After current ownership and the I0087 current-status adjudication, I did not find a target satisfying all of:

1. exact outside source recovered;
2. current primary/later/citing status checked;
3. prior attempt/history recovered;
4. no current owner;
5. not POSTED/settled in the selected scope;
6. genuinely CLOSABLE with a defensible frozen metric.

Therefore R10 remains **ROTATION HOLD / SUCCESSOR ADMISSION REQUIRED**. This is preferable to reviving retired I0070, stealing another track's target, or calling a pending/known item READY.

No new finite mathematical claim was made for R10, so no checker-only artifact was manufactured.

## 6. Independent R10 audit of newest R11 package

Newest R11 theorem package located and read:

`runs/R11/2026-09-16T22-40-00Z_i0054-cayley-universality-3f2a.md`.

It introduces the universality statement `R11-I0054-U001` for exchangeably labelled weighted random trees and the concrete Cayley specialization `R11-I0054-C007`.

### Audit ID

`R10-AUDIT-R11-I0054-U001-CAYLEY-20260916`

### Verdict

**PASS for the universality generator/coupling core and the C007 Cayley weight-profile specialization only.** This is not a source-intent/novelty audit and not an end-to-end closure certification for Aldous--Janson Open Problem 18.

### Independent check of U001 core

Suppose an exchangeably labelled weighted tree on `[m]` satisfies the oriented profile

`E[ sum_{(e,S): |S|=s} w_m(e) ] = m/[s(m-s)]`.

By exchangeability, for any fixed `s`-subset `S`, its expected oriented-side weight is

`[m/(s(m-s))]/C(m,s) = B(s,m-s)`.

Fix `b` sampled labels and a particular visible split `A | A^c`, `|A|=i`. Summing over hidden side sizes gives

`sum_s C(m-b,s-i) B(s,m-s) = B(i,b-i)`.

The identity follows directly from the beta integral and the binomial theorem and is independent of the hidden block size `m`. Hence the first-order visible split generator is exactly the CTCS generator.

If `W(T_m)<=A_N`, independent rare edge marks at rate scale `delta_N` produce two-or-more-mark error `O(delta_N^2 A_N^2)` per raw step. Over `O(1/delta_N)` steps on a fixed physical-time interval, maximal coupling therefore fails with probability `O(delta_N A_N^2) -> 0`, which validates the fixed-finite-restriction Euler-generator argument. Projective convergence then follows by controlling one finite label restriction and the deterministic tail of the projective metric.

### Independent check of Cayley specialization

For a uniform Cayley tree, the expected number of oriented edge sides of size `s` is

`Z_{m,s} = C(m,s) s^(s-1) (m-s)^(m-s-1) / m^(m-2)`.

The proposed symmetric physical-edge weight

`w_m(s)=m^(m-1)/[C(m,s) s^s (m-s)^(m-s)]`

satisfies exactly

`Z_{m,s} w_m(s)=m/[s(m-s)]`,

so U001 applies once the total-weight bound is supplied. R11 proves `W(T_m)<3m/2`; with `delta_N=N^-3`, taking `A_N=3N/2` gives

`delta_N A_N^2 <= 9/(4N) -> 0`.

The package's exact checker independently archives the beta identity, profile cancellation, the `m=4` failure of uniform unweighted Cayley cutting, the finite weight checks, and the error-scale condition. I found no defect in these audited components.

## 7. Model/runtime and permission boundary

Actual runtime is GPT-5.6 Sol with reasoning level UNVERIFIED. The exposed scheduler surface still has no model-family selector, reasoning-effort selector, authenticated runtime telemetry, or guaranteed hour-long duration. GPT-6/maximum is therefore only a prompt request here. A real change requires an eligible owner-side product/workspace control that exposes those fields, or platform support.

Likewise, a native `You cannot modify this task` response (including the historical P26 ownership-boundary case) is resolved only from the owning/authorized control context or by platform support. Creating a duplicate or bypassing permissions is not a valid workaround.

## 8. ledger_delta

```yaml
ledger_delta:
  worker: R10
  source: "Agresti--Veraar (2025), Nonlinear SPDEs and Maximal Regularity: An Extended Survey, Problem 6 / I0070"
  target: "critical Hilbert p=2 extension of Theorem 5.7 under the source critical equality, with all source norms/weights/parameter restrictions"
  metric: "largest rigorously established time-regularity exponent theta; endpoint 1/2 not claimed"
  before: "theta_* = 1/2 as a supremum"
  after: "theta_* = 1/2 as a supremum"
  movement: "none; target already retired after six unchanged runs"
  unchanged_count: 6
  status: "PARTIAL / RETIRED-HANDOFF / ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED"
  own_claim: "R10-I0070-C006 author-side proved; independent closure audits still 0/2 located"
  exact_evidence:
    - "runs/R10/20260916T2138Z_i0070_progressive_representative.md"
    - "runs/R10/20260916T2236Z_i0070_sixrun_handoff_gate.md"
  successor_screen:
    I0087: "NOT READY AS FRESH OPEN: later arXiv:2606.30517 explicitly treats product convergence including H^2 x R"
    claimed_or_unavailable_front: true
    ready_unassigned_successor_found: false
  outgoing_audit_ids:
    - "R10-AUDIT-R11-I0054-U001-CAYLEY-20260916"
```

No email, Gmail, Google Drive, public posting, purchase, paid compute, credential access, workflow execution, permission change, force-push, peer-file edit, or shared-root edit was performed.

END OF IMMUTABLE R10 REPORT
