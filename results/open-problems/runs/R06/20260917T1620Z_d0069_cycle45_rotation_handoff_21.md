Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO MOVEMENT in the frozen metric: `C5: 5/5 -> 5/5`, unchanged count `5 -> 6`; Section-B moves tried: #3 PROVE SOMETHING STRONGER, #16 COMPUTE EVERY SMALL CASE, #30 DO ONE SCALE / ONE DIRECTION AT A TIME.**

# R06 CLOSABLE OUTSIDE — D0069 finite-cycle strengthening and six-run rotation handoff

Run date: 2026-09-17 UTC.  
Repository / branch: `yspennstate/math-open-problems` / `master`.  
Delivery: private GitHub only. No email/Gmail, Drive, public posting, purchases, permission changes, workflow execution, or scheduler mutation.

## 1. Continuity, predecessor, ownership, and the frozen metric

I continued from current repository state rather than restarting the historical scheduler title. I reread/recovered the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current implementation/deployment receipt, `operations/claims/D0069.md`, the R06 report chain through

`runs/R06/20260917T1520Z_d0069_triangle_factor_local_transform_20.md`,

and the newest visible neighboring R07 report

`runs/R07/20260917T1423Z_i0077_branch_swapping_exterior_22.md`.

The native title still names Russell Lyons and Yuval Peres, *Probability on Trees and Networks*, Question 6.20 / intake I0056. That predecessor is not reopened. Its exact retained source scope asks for `Phi_V(G)` for regular co-regular plane graphs and `Phi_E(G), Phi_V(G)` for more general transitive plane graphs. R06's frozen regular/co-regular regime was `H_{5,5}={5,5}` with outer vertex-boundary normalization

\[
\Phi_V(G)=\inf_{\varnothing\ne K\subset V(G),\ |K|<\infty}
\frac{|\partial_VK|}{|K|},
\]

and the preserved handoff has

\[
\Phi_V(H_{5,5})=\sqrt5,\qquad [L,U]=[\sqrt5,\sqrt5],\qquad U-L=0.
\]

The full Lyons--Peres question remains PARTIAL. The triangular and quadrangular co-degree cases of Haslegrave--Panagiotis, DOI `10.1002/rsa.20946`, remain excluded prior art. I0056 already hit its six-unchanged CLOSABLE threshold and rotated.

The current canonical R06 ownership is `operations/claims/D0069.md`, Geoffrey R. Grimmett and Zhongyang Li's question whether

\[
\mu(G)\ge\sqrt{\Delta-1}
\]

extends from simple infinite connected vertex-transitive regular graphs, and from nonsimple vertex-transitive regular multigraphs for `Delta<=4`, to nonsimple vertex-transitive regular multigraphs of larger degree. The original theorem/question is in *Bounds on connective constants of regular graphs*, Theorem 4.1 and the sentence immediately following it; the survey restatement is Question 2.2.

The frozen first unresolved degree is `Delta=5`. The official R06 metric is

\[
C_5=\#\{\text{the five nonsimple degree-5 multiplicity partitions proved uniformly}\}.
\]

Run 15 saturated it at

\[
\boxed{C_5=5/5}.
\]

Runs 16--20 left that frozen number unchanged while producing additional degree-six structure. This invocation is the sixth consecutive unchanged run, so the operational CLOSABLE rule requires rotation after this report. I do not replace `C5` by a more convenient degree-six metric.

## 2. Source and current-literature check — 2026-09-17

Primary source checked again: Geoffrey R. Grimmett and Zhongyang Li, *Bounds on connective constants of regular graphs*, arXiv:1210.6277 / Combinatorica 35 (2015), 279--294. Theorem 4.1 gives `mu(G)>=sqrt(Delta-1)` for simple vertex-transitive regular graphs and, in the nonsimple case, for `Delta<=4`, then asks whether the nonsimple conclusion extends to larger degree. Its SAW convention distinguishes parallel edge copies and the relevant multigraphs are loopless.

Fresh dated searches included:

- `Grimmett Li nonsimple multigraph connective constant sqrt(Delta-1) larger degree`;
- `"[4,1,1]" connective constant multigraph self-avoiding walk`;
- `"Self-avoiding walks on cubic graphs and local transformations" Grant Li`;
- `degree six vertex-transitive multigraph connective constant parallel edges`.

The nearest current paper found remains Benjamin Grant and Zhongyang Li, *Self-avoiding walks on cubic graphs and local transformations*, arXiv:2601.12571 (v1 18 January 2026, v2 16 February 2026), which develops exact scalar two-port substitution identities for symmetric three-port finite gadgets. I found no source-matching later theorem resolving Grimmett--Li's full nonsimple larger-degree question or the finite-cycle `[4,1,1]` subclasses below. This is **bounded negative search evidence only; novelty remains UNVERIFIED**. Grant--Li's local-transformation viewpoint is prior machinery/inspiration, not relabelled as new.

A current repository search for `D0069` plus `AUDIT/PASS` still finds no independent P26 plus second OTHER-track closure pair for D0069. Hence even the saturated degree-five package is not called protocol-closed.

## 3. Recovered residual degree-six problem

Run 18 covered eight of the nine local nonsimple degree-six multiplicity partitions and left only

\[
\boxed{[4,1,1]}.
\]

For such a graph `G`, let `H` be its simple cubic skeleton. The multiplicity-four classes form an automorphism-invariant perfect matching `M`, while the singleton classes form an automorphism-invariant spanning 2-factor `S`.

Run 19 diagnosed why a multiplicity-only scalar blue-count certificate fails here. Run 20 then proved the `[4,1,1]` subclass in which every component of `S` is a triangle, using an exact critical transfer through triangle blocks.

This run follows the prescribed fresh triple `#3,#16,#30` and asks for the next finite scales: singleton cycles of lengths `L=4` and `L=5`.

## 4. Method #3 — prove the finite-cycle reduction in a stronger common form

Assume every component of `S` is a finite cycle of common length `L`. Vertex transitivity forces the common length.

### 4.1 Every heavy matching edge joins different `S`-cycles

The property

> the `M`-mate of a vertex lies in the same `S`-component

is invariant under the vertex-transitive automorphism group because `M` and `S` are determined by edge multiplicity. Therefore it holds either at every vertex or at no vertex.

If it held everywhere, every heavy matching edge would stay inside an `S`-cycle. Since all singleton edges also stay inside that cycle by definition, distinct `S`-cycles would have no edges between them. This contradicts connectedness and infinitude of `G` (a single finite `S`-cycle cannot contain all vertices). Hence every heavy matching class joins two distinct `S`-cycles.

### 4.2 Contract the singleton cycles

Contract each `S`-cycle to one macrovertex and retain each heavy matching class as one quotient edge. The resulting quotient `Q` is infinite, connected, loopless, locally finite and vertex-transitive. It is `L`-regular as a multigraph, because the `L` ports of a singleton cycle each support exactly one heavy matching class. Parallel quotient edges are allowed.

A vertex-self-avoiding quotient walk never revisits a macrocycle. If it enters an intermediate cycle through port `u` and leaves through port `v`, then `u!=v` because `M` is a matching. There are exactly two internally vertex-simple singleton arcs between the ports, of lengths

\[
r\quad\text{and}\quad L-r,
\qquad 1\le r\le L-1.
\]

The outgoing heavy class has four parallel edge-copy choices in `G`.

Set the source-critical value

\[
z=\frac1{\sqrt5}.
\]

The exact critical transfer through an intermediate cycle is therefore

\[
\boxed{T_{L,r}(z)=4z\bigl(z^r+z^{L-r}\bigr).}
\tag{4.1}
\]

Let

\[
T_L^{\min}=\min_{1\le r<L}T_{L,r}(1/\sqrt5).
\]

For each `n`-step quotient SAW, independently selecting one of the two internal arcs at every intermediate macrocycle and one of the four physical copies of each outgoing heavy edge gives genuine edge-copy-distinct SAWs in `G`: no macrocycle is revisited, and each chosen internal arc is vertex-simple. A fixed starting vertex in the initial cycle costs only a positive `L`-dependent endpoint factor `c_L>0`, independent of `n`.

Thus if `sigma_n(Q)` is the number of quotient SAWs from a fixed macrovertex,

\[
W_n(z)\ge c_L\,\sigma_n(Q)\,(T_L^{\min})^{n-1}
\tag{4.2}
\]

for the total `z^{length}`-mass of this lifted family. Consequently,

\[
\boxed{\mu(Q)T_L^{\min}>1\quad\Longrightarrow\quad
\sum_m\sigma_m(G)5^{-m/2}=\infty
\quad\Longrightarrow\quad \mu(G)\ge\sqrt5.}
\tag{4.3}
\]

This is the common finite-cycle compiler. It strengthens run 20's one-off triangle argument and identifies exactly what quotient information is needed.

## 5. Method #16 — compute every next small port-distance case exactly

### 5.1 Singleton 4-cycles

For `L=4`, the quotient `Q` is a loopless vertex-transitive `4`-regular multigraph. Grimmett--Li Theorem 4.1(b) applies directly because the source already proves the nonsimple bound through degree four:

\[
\mu(Q)\ge\sqrt3.
\tag{5.1}
\]

The exact transfers are

\[
T_{4,1}=T_{4,3}=4(z^2+z^4)=\frac{24}{25},
\]

and

\[
T_{4,2}=8z^3=\frac{8}{5\sqrt5}.
\]

Hence

\[
T_4^{\min}=\frac{8}{5\sqrt5}.
\]

The product criterion is strictly satisfied:

\[
\sqrt3\,\frac{8}{5\sqrt5}>1
\iff
\frac{192}{125}>1
\iff
192>125.
\tag{5.2}
\]

Therefore every source-admissible `[4,1,1]` graph whose singleton 2-factor consists of 4-cycles satisfies

\[
\boxed{\mu(G)\ge\sqrt5.}
\tag{T7a}
\]

### 5.2 Singleton 5-cycles

For `L=5`, the quotient `Q` is a loopless vertex-transitive `5`-regular multigraph. If it is simple, Grimmett--Li's source theorem gives `mu(Q)>=2`. If it is nonsimple, the complete degree-five theorem proved on page in R06 run 15 gives the same bound for every one of the five nonsimple local multiplicity partitions:

\[
\mu(Q)\ge2.
\tag{5.3}
\]

Thus this `L=5` result inherits the internal proof/audit status of the run-15 degree-five theorem; it is not presented as an independently published fact.

The exact transfers are

\[
T_{5,1}=T_{5,4}=\frac45+\frac{4}{25\sqrt5},
\]

and

\[
T_{5,2}=T_{5,3}=\frac4{25}+\frac4{5\sqrt5}.
\]

Therefore

\[
T_5^{\min}=\frac4{25}+\frac4{5\sqrt5}.
\]

Using `mu(Q)>=2`,

\[
2T_5^{\min}>1
\iff
\frac8{25}+\frac8{5\sqrt5}>1
\iff
8\sqrt5>17
\iff
320>289.
\tag{5.4}
\]

Hence every source-admissible `[4,1,1]` graph whose singleton 2-factor consists of 5-cycles also satisfies

\[
\boxed{\mu(G)\ge\sqrt5.}
\tag{T7b}
\]

Combining run 20 with this run gives the stronger finite-cycle statement:

> **Theorem R06-D0069-T7.** If `G` is an infinite connected loopless vertex-transitive 6-regular multigraph of local type `[4,1,1]`, and its singleton 2-factor has finite components of common length `L in {3,4,5}`, then `mu(G)>=sqrt5`.

The `L=3` case is run 20; `L=4,5` are proved above. This remains PARTIAL for the full `[4,1,1]` class and for D0069.

## 6. Method #30 — one scale at a time exposes the exact next obstruction

The small-scale computation is informative because it shows where the scalar worst-port transfer stops being competitive.

At `L=6`, the worst distance is `r=3`, giving

\[
T_{6,3}=8z^4=\frac8{25}.
\]

Even the conjectural/source-shaped degree-six quotient lower bound `mu(Q)>=sqrt5` would give only

\[
\sqrt5\,\frac8{25}<1.
\]

Therefore the minimum-over-port-distances compiler (4.3) cannot simply be iterated to all cycle lengths, even if the degree-six Grimmett--Li bound were already known. The remaining proof has to retain the sequence of port-distance states, exploit their frequency/correlation, or return to the entropy/matching-density flow from run 19. This is a method obstruction, not a counterexample to the source inequality.

The residual `[4,1,1]` regimes left in the handoff are:

1. finite singleton cycles of common length `L>=6`, where a matrix/state transfer is needed rather than the scalar minimum;
2. singleton 2-factor components that are bi-infinite double rays, where the run-19 Gibbs/entropy formulation remains the best current route.

All other degree-six local multiplicity partitions were covered by run 18. Degrees `Delta>=7` remain part of the full Grimmett--Li question.

## 7. Exact finite self-check

Only after the proof route was fixed, I executed an exact arithmetic checker and archived it:

- `artifacts/R06/d0069_run21_cycle45_selfcheck.py` @ creation commit `d4662df72a99f8424262cd6eab0e9c0288960b0f`;
- `artifacts/R06/d0069_run21_cycle45_selfcheck.out` @ creation commit `e6424f50f1cde180f42bad56897fd7cafe944aa5`.

The checker represents `Q(sqrt(5))` exactly as pairs `a+b/sqrt(5)` with rational coefficients. It verifies every port-distance transfer for `L=4,5`, the minima, and the two integer comparison certificates

\[
192>125,
\qquad
320>289.
\]

The archived output ends

`ALL_EXACT_FINITE_CHECKS_PASS`.

This is explicitly a SELF-CHECK of the finite algebra. The infinite lifting theorem is proved on the page above.

## 8. Six-unchanged CLOSABLE rotation handoff

The frozen metric history since saturation is now:

- run 15: `C5` moved to `5/5`;
- run 16: unchanged 1;
- run 17: unchanged 2;
- run 18: unchanged 3;
- run 19: unchanged 4 (mandatory stuck/thinking run);
- run 20: unchanged 5;
- **this run 21: unchanged 6**.

Under the current owner rule, R06 therefore **rotates away from D0069 now**, notwithstanding real auxiliary degree-six progress. No subsequent R06 invocation should manufacture a seventh unchanged `C5` run. D0069 is left with a complete handoff rather than labelled solved.

### Handoff state

- Source: Grimmett--Li nonsimple extension question.
- Frozen degree-five theorem: all five nonsimple local partitions covered, `C5=5/5`; full source still PARTIAL.
- Degree six: eight of nine local multiplicity partitions covered in run 18.
- Ninth type `[4,1,1]`: finite singleton-cycle lengths `L=3,4,5` now covered; `L>=6` and the double-ray singleton-factor regime remain.
- Best remaining finite-cycle identity: `T_{L,r}(z)=4z(z^r+z^{L-r})` at `z=1/sqrt5`; scalar worst-distance transfer fails already at `L=6`.
- Best double-ray route: run-19 entropy/Gibbs lower bound coupling SAW entropy and heavy-matching frequency.
- Exact evidence: run-15 degree-five self-checks, run-18 degree-six partition checks, run-20 triangle check, and the run-21 `L=4,5` checker above.
- Closure: no independent P26 + distinct OTHER-track D0069 audit pair recovered; novelty UNVERIFIED.

Status after handoff:

\[
\boxed{\text{D0069 = PARTIAL / R06 ROTATED AFTER SIX UNCHANGED FROZEN-METRIC RUNS}.}
\]

## 9. Successor-admission screen

I did not create a speculative successor claim merely to fill the slot. The current front of `QUEUE.md` was checked against current ownership/status:

- `I0006`: still `HOLD_SOURCE`; the exact alleged remaining odometer-tail statement is not source-cleared.
- `I0011`: already canonically claimed by P16; not available.
- `I0028`: still `HOLD_SCOPE`; not an admitted CLOSABLE dispatch.
- `I0035`: current repository state records a C31 reservation/claim; not available to R06.
- `I0054`: current repository state records an R11 claim with an active report chain; not available to R06.
- `I0055` / Lyons--Peres Question 5.16: not open. The current *Probability on Trees and Networks* text says Pengfei Tang gave a positive answer to Kahn's modified question, and Tang's 2020 arXiv:2012.01135, *A note on some critical thresholds of Bernoulli percolation*, explicitly states that positive answer.

Thus no create-only successor was legitimately available in this bounded front-of-queue screen. The next R06 invocation should continue **SUCCESSOR_ADMISSION_REQUIRED** from the next unoccupied, source-cleared CLOSABLE queue candidate; it must not resume D0069 or steal a claimed row.

## 10. Neighbor continuity

The newest visible neighboring R07 report read this run is `runs/R07/20260917T1423Z_i0077_branch_swapping_exterior_22.md`. It advances its own shape-family metric and keeps Burdzy--Scheutzow Problem 7.8 PARTIAL. I did not spend this run manufacturing a new outgoing audit: the validation budget went to the exact `L=4,5` finite core, current literature/ownership checks, and the required rotation handoff.

## 11. Model/scheduler control status

The requested GPT-6/maximum configuration is still not enforceable or authenticated from the exposed task-control schema. The current deployment receipt records controls for title/prompt, schedule or relative start, enabled state and timing mode, but **no model-family selector, no reasoning-effort selector, no authenticated completed-run routing telemetry and no guaranteed one-hour execution field**. GPT-6/maximum therefore remains prompt text only in this environment.

The historical P26 `You cannot modify this task` error was context-dependent: `operations/new_methods_2026-09-16/NATIVE_PC_DEPLOYMENT.md` records a later successful P26 update from a different authorized context. The legitimate workaround for a protected task is the owning/admin context or platform support. Enforcing model/reasoning would require product/backend support for persistent `model` and `reasoning_effort` fields plus trustworthy per-run telemetry. No scheduler change or permission bypass was attempted here, as required by the operational addendum.

## 12. Structured ledger_delta

```yaml
ledger_delta:
  track: R06
  allocation: CLOSABLE_OUTSIDE
  predecessor_source_retained: "Russell Lyons and Yuval Peres, Probability on Trees and Networks, Question 6.20 / I0056"
  predecessor_status: "PARTIAL / rotated earlier; H_{5,5} interval [sqrt(5),sqrt(5)] width 0"
  active_source: "Geoffrey R. Grimmett and Zhongyang Li, Bounds on connective constants of regular graphs / survey Question 2.2; claim D0069"
  source_question: "Does mu(G) >= sqrt(Delta-1) extend to nonsimple vertex-transitive regular multigraphs of degree Delta>4?"
  frozen_metric: C5
  metric_before: "5/5"
  metric_after: "5/5"
  movement: "NO MOVEMENT"
  unchanged_count_before: 5
  unchanged_count_after: 6
  tried_moves: [3, 16, 30]
  status: "PARTIAL / ROTATED_AFTER_SIX_UNCHANGED"
  new_claims:
    - id: R06-D0069-T7a
      statement: "degree-6 [4,1,1] with singleton 2-factor of 4-cycles has mu(G)>=sqrt(5)"
      label: "PROVED-ON-PAGE / SELF-CHECK-PASS / SUBCLASS-PARTIAL / NOVELTY-UNVERIFIED"
    - id: R06-D0069-T7b
      statement: "degree-6 [4,1,1] with singleton 2-factor of 5-cycles has mu(G)>=sqrt(5), using the run-15 degree-5 quotient theorem"
      label: "PROVED-ON-PAGE-IN-R06-CHAIN / SELF-CHECK-PASS / SUBCLASS-PARTIAL / NOVELTY-UNVERIFIED"
    - id: R06-D0069-T7
      statement: "degree-6 [4,1,1] with finite singleton cycles of common length L in {3,4,5} has mu(G)>=sqrt(5)"
      label: "COMBINED SUBCLASS THEOREM; L=3 from run20, L=4,5 here"
  exact_evidence:
    - "artifacts/R06/d0069_run21_cycle45_selfcheck.py @ d4662df72a99f8424262cd6eab0e9c0288960b0f"
    - "artifacts/R06/d0069_run21_cycle45_selfcheck.out @ e6424f50f1cde180f42bad56897fd7cafe944aa5"
  self_check_status: PASS
  independent_d0069_audits: PENDING
  novelty: UNVERIFIED
  remaining_obligation: "D0069 handed off: residual degree-6 [4,1,1] has finite cycles L>=6 and double-ray singleton factors; full source also has Delta>=7. R06 must rotate."
  successor_status: SUCCESSOR_ADMISSION_REQUIRED
  successor_screen:
    I0006: HOLD_SOURCE
    I0011: CLAIMED_P16
    I0028: HOLD_SCOPE
    I0035: CLAIMED_C31
    I0054: CLAIMED_R11
    I0055: KNOWN_RESOLVED_BY_TANG_2020
  model_actual: "GPT-5.6 Sol"
  reasoning_actual: UNVERIFIED
  requested_but_not_authenticated: "GPT-6 maximum"
  delivery: "private GitHub only"
```
