Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT: frozen I0024 remains `C=1`; R01 successor metric remains `UNMEASURED -> UNMEASURED`; status `PENDING_ADMISSION`; methods #6, #20, #29.**

# R01 — post-rotation P0219 prior-art/bridge screen

Repository: private `yspennstate/math-open-problems`, branch `master`.

## 1. Controlling continuity: I0024 remains frozen at equality

I recovered the newest R01 state before doing anything else. The original source is David Aldous and James Fill, *Reversible Markov Chains and Random Walks on Graphs*, Open Problem 3.44 / intake I0024. The maintained Chapter 3 page still asks:

> Does there exist a characterization of the relaxation time as exactly an inf over flows?

and Chapter 4 still contrasts that question with the non-exact path/flow upper bound of Theorem 4.32.

R01's frozen result remains the exact stationary-weighted right-inverse characterization

\[
\tau_2=
\inf_{R:\,BR=I_{H_0}}
\sup_{0\ne b\in H_0}
\frac{(Rb)^T C^{-1}(Rb)}{b^T\Pi^{-1}b},
\qquad
R_*=CB^TL^+,
\]

with source metric `C=1`. The existing R20 and P26 independent PASS audits remain the closure evidence. I did not reopen I0024, rerun a checker, or manufacture another audit.

Fresh bounded literature queries on 2026-09-19 for `"relaxation time" "infimum over flows"`, `right inverse incidence relaxation time Markov chain`, `Thomson principle relaxation time flow exact`, and close variants recovered the Aldous--Fill source and standard/nonreversible spectral-gap literature but no checked later source explicitly publishing the retained R01 formula. This is bounded negative evidence, not a worldwide priority certificate.

The former R01 FEI assignment remains retired; P03 owns FEI. The six-run-terminal KPS/Nielsen successor remains handed off and was not reopened.

## 2. Repository-wide delta and admission state

The controlling predecessor is

`runs/R01/20260919T0103Z_post_rotation_p0219_replenishment_lead_1_10_17_6d2f8a41.md`

at commit `83b699e1cc063fdd57e9c7af9bce7765cd8829db`.

I reread/recovered campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest operations implementation manifest, the newest own report, neighboring successor-admission reports, and the relevant P0219 intake/prior-attempt records. A commit comparison from the R01 predecessor to the fresh prewrite master snapshot `da28736a5b97a8bb69b97e68e033ca9808435a71` is **95 commits ahead / 0 behind**. In that interval the only new canonical claim file is `operations/claims/H0008.md`, owned by R14 in the **HARD OUTSIDE** lane. No root `QUEUE.md`, `RESULTS.md`, `POSTED.md`, campaign `INDEX.md`/`RANKING.md`, or intake source-ledger mutation appears in the compared file set, and no canonical claim release/deletion appears.

The newest coordinator/admission screens still report `E_READY_CLOSABLE: 0 -> 0`. `operations/claims/P0219.md` is still absent (404). P0219 therefore remains an unclaimed **PENDING_NOT_READY** replenishment lead, not a target R01 may promote by fiat. No claim was created this run and no successor metric was initialized.

## 3. Fresh prior-art finding for P0219: a discrete exact Hammersley model is much closer than the previous screen recorded

The current lead is David Aldous, *A discrete Hammersley process as an extreme case of oriented percolation flows*. Write `q=1-p`. The source defines `V(n,p)/(2n) -> v(p)` and conjectures

\[
\boxed{1-v(p)\sim\sqrt{2q}}\qquad(q\downarrow0).
\]

The source rewrites the deficiency through `U(n,p)`, the minimum number of boundary-to-boundary oriented paths covering all closed edges, and explains the conjecture by replacing the rare closed edges with a planar Poisson process. The stated difficulty is interchange of the infinite-volume and rare-defect limits.

A new prior-art route not found in the previous R01/R06/P13 text search is Timo Seppäläinen, *Increasing sequences of independent points on the planar lattice*, Ann. Appl. Probab. **7** (1997), 886--898, DOI `10.1214/aoap/1043862416`. Seppäläinen solves the independent Bernoulli **lattice** Hammersley problem exactly. If lattice sites are independently marked with probability `r`, his Theorem 1 gives an exact shape function; on the diagonal its interior formula reduces to

\[
\Psi_r(1,1)
 =\frac{2\sqrt r-2r}{1-r}
 =\frac{2\sqrt r}{1+\sqrt r}
 =2\sqrt r+O(r).
\]

The same paper explicitly recovers the planar Poisson Hammersley shape by the low-density lattice scaling `r -> 0`. It also remarks that the **nondecreasing** variant is genuinely different and that the stationary-process step used for the strict model did not directly identify its steady state. Later Bernoulli last-passage work (for example Georgiou 2010 and Georgiou--Ortmann 2018) develops closely related strict/weak Bernoulli LPP models.

This does **not** resolve P0219. It materially changes the best route and the admission prior-art obligation: before treating P0219 as a fresh two-scale de-Poissonization problem, we must determine whether Aldous's closed-edge cover is exactly, or sparsely equivalent to, one of these known discrete Bernoulli Hammersley/LPP models.

## 4. Method #6 — deform to the exact Bernoulli Hammersley model

The useful deformation is no longer lattice `->` continuum Poisson. It is

\[
\text{closed directed edges}
\quad\longrightarrow\quad
\text{Bernoulli marked points on an edge-midpoint lattice}
\quad\longrightarrow\quad
\text{strict/weak Bernoulli Hammersley width}.
\]

There are two possible directed edge orientations per unit lattice cell, so the rare-defect point intensity is `2q` per unit physical area. The universal low-density Hammersley first-order term `2 sqrt(lambda)` therefore predicts

\[
U(n,1-q)\sim 2n\sqrt{2q},
\]

which after division by `2n` is exactly Aldous's coefficient `sqrt(2)`.

The important improvement is conceptual: the constant can potentially be obtained from a **discrete exact shape theorem before taking `q -> 0`**, avoiding Poissonization altogether. Seppäläinen's diagonal formula supplies the correct `2 sqrt(r)` low-density law for an independent lattice model.

But the models are not yet identified. Edge midpoints occupy a two-orientation periodic/checkerboard set rather than all sites of one standard square lattice, and the reachability relation between directed edges allows borderline same-row/same-column behavior depending on edge orientation. Consequently I do not substitute `r=2q` into Seppäläinen's theorem as if this were already a proof.

Outcome of #6: **promising new route, no source metric movement.**

## 5. Method #20 — identify exactly why the obvious chain-cover algorithm is not yet a proof

Let `C_n(q)` be the random set of closed directed edges. Put a finite partial order on those edges by

\[
e\preceq f
\quad\Longleftrightarrow\quad
\text{there is an oriented north/east lattice path that traverses `e` before `f`}.
\]

Define

\[
W(n,q):=\operatorname{width}(C_n(q),\preceq),
\]

so by Dilworth this is also the minimum number of abstract chains needed to cover all closed edges.

Every admissible path in Aldous's definition of `U(n,1-q)` intersects the closed-edge set in one chain. Therefore every actual edge-disjoint path cover induces a chain cover, and the deterministic inequality

\[
\boxed{W(n,q)\le U(n,1-q)}
\]

is immediate.

This isolates two distinct obligations rather than one vague interchange of limits:

**Bernoulli-width obligation**
\[
\lim_{q\downarrow0}\lim_{n\to\infty}
\frac{W(n,q)}{n\sqrt q}=2\sqrt2,
\]

with the relevant mode of convergence/expectation made source-compatible; and

**routing-tax obligation**
\[
\lim_{q\downarrow0}\limsup_{n\to\infty}
\frac{U(n,1-q)-W(n,q)}{n\sqrt q}=0.
\]

If both hold, the source conjecture follows immediately.

The first obligation is where Seppäläinen/modern Bernoulli LPP can plausibly enter. The second is the precise reason the naive `apply Dilworth + cite Hammersley` algorithm fails: an abstract chain decomposition does not automatically give a **simultaneously edge-disjoint routing** of all chains through the original directed grid. Connector conflicts between different chains are invisible to the poset width.

A second mismatch is strict versus weak order. Seppäläinen's exactly solved model uses paths strictly increasing in both coordinates; his paper itself flags the nondecreasing version as requiring different stationary analysis. Aldous's two edge orientations naturally create half-lattice and borderline comparability effects. These effects are expected to be lower order at sparse density, but that expectation is exactly what must be proved at the `o(n sqrt(q))` scale.

Outcome of #20: **the hard step is reduced to a named routing-tax lemma plus a periodic/weak Bernoulli-width lemma; neither is proved here.**

## 6. Method #29 — add the points at infinity / stationarize before taking the rare-defect limit

The finite square may be the wrong category for the missing uniformity. Seppäläinen's exact Hammersley shape comes from an interacting-particle/stationary construction. A more direct route for P0219 is therefore to add infinite entrance/exit boundaries and seek a translation-invariant stationary cut/path-cover process for the closed-edge model.

At heuristic level, if `rho` denotes stationary interface/path-line density, the rare-defect balance suggested by the two independent edge orientations has the form

\[
F_q(\rho)\approx \rho+\frac{2q}{\rho}.
\]

Its optimizer is `rho=sqrt(2q)` and

\[
\inf_{\rho>0}F_q(\rho)=2\sqrt{2q},
\]

which is exactly the unnormalized first-order coefficient required for `U(n,1-q)/n`. This is only a route heuristic. The real task is to derive the stationary current/flux identity from the edge model, not assume the displayed balance.

If such a stationary law exists, a shape theorem/Busemann argument could separate the bulk coefficient from finite-square boundary effects and avoid proving a direct total-variation Poisson approximation uniform in `n`. This is now a cleaner #29 route than adding another finite-grid checker.

Outcome of #29: **new infinite-volume attack identified; no theorem claim yet.**

## 7. Current assessment and next obligation

P0219 remains a good replenishment lead but is **not yet READY**. The fresh Seppäläinen connection makes it simultaneously more promising and more delicate:

- more promising, because the needed `sqrt(q)` law and its exact low-density coefficient already occur in a solved discrete Bernoulli Hammersley model;
- more delicate, because a prior-art-complete admission must now distinguish Aldous's two-orientation edge-disjoint cover from strict/weak Bernoulli LPP and must not claim novelty for a bridge that may already be known under another formulation.

The highest-value next mathematical check is therefore not another Poisson approximation. It is to derive the exact max-flow/min-cut or path-cover representation of `U` in a dual lattice and determine whether that representation is one of the known Bernoulli LPP models. If exact identification fails, prove a deterministic/probabilistic bound on the routing tax `U-W` at the `o(n sqrt(q))` scale.

No checker was created because there is no new finite claim to certify. No audit was requested because no complete neighboring package is ready. No shared root, other track file, email, Drive item, public post, permission, or scheduler was modified.

## 8. Model/scheduler control status

The exposed task-control surface still provides prompt/title, schedule or relative-start timing, timing mode, and enable/disable state. It does **not** expose a binding model-family selector, a reasoning-effort selector, an authenticated receipt of the applied model/effort, or a guaranteed one-hour execution field. GPT-6/maximum therefore remains prompt text only on this surface.

The historical P26 `You cannot modify this task` response was authorization-context-specific; repository history records that a later authorized context succeeded. The lawful workaround is the owning/authorized product/workspace/API/admin context or platform support, not duplication or permission bypass.

## 9. Structured ledger_delta

```yaml
ledger_delta:
  track: R01
  category: CLOSABLE_OUTSIDE
  frozen_source:
    id: I0024
    source: "Aldous--Fill Open Problem 3.44"
    metric_name: "uniform multiplicative distortion C"
    metric_before: 1
    metric_after: 1
    status: PROVED_FROZEN
    audits: [R20_PASS, P26_PASS]
  active_successor:
    claim: null
    state_before: PENDING_ADMISSION
    state_after: PENDING_ADMISSION
    metric_name: UNMEASURED
    metric_before: UNMEASURED
    metric_after: UNMEASURED
    movement: false
    unchanged_runs: NOT_STARTED
  tried_moves: [6, 20, 29]
  method_scope: ADMISSION_AND_ROUTE_SCREEN
  repository_delta:
    base: 83b699e1cc063fdd57e9c7af9bce7765cd8829db
    prewrite_head: da28736a5b97a8bb69b97e68e033ca9808435a71
    ahead_by: 95
    behind_by: 0
    new_canonical_claims: [H0008_HARD_OWNED_R14]
    free_ready_closable_delta: "0 -> 0"
  replenishment_lead:
    id: P0219
    title: "High-density oriented percolation flow asymptotics"
    same_id_claim: ABSENT_AT_SCREEN
    lifecycle: PENDING_NOT_READY
    source_endpoint: "1-v(p) ~ sqrt(2(1-p)) as p -> 1"
    new_prior_art:
      - "Seppalainen 1997 exact Bernoulli lattice Hammersley shape, DOI 10.1214/aoap/1043862416"
      - "Georgiou 2010 strict Bernoulli soft-edge work"
      - "Georgiou--Ortmann 2018 Bernoulli last-passage models"
    new_reduction:
      - "define closed-edge reachability width W(n,q)"
      - "deterministic W(n,q) <= U(n,1-q)"
      - "separate Bernoulli-width asymptotic from routing-tax U-W"
    remaining_obligation: >-
      Before admission or source research, identify the exact dual/LPP model or
      prove sparse-density equivalence to a known Bernoulli Hammersley model;
      in particular control U-W=o(n sqrt(q)) in the sequential limit and finish
      coordinator-grade current-literature/ownership admission. Do not promote
      PENDING_NOT_READY by fiat.
  evidence:
    original_source_checked_utc: 2026-09-19
    current_literature_checked_utc: 2026-09-19
    p0219_claim_404: true
    audits_requested: []
    checker_created: false
```
