Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — GPT-6 / maximum was requested in prompt text, but the exposed runtime provides no authenticated applied-model or reasoning-effort receipt, so I do not claim GPT-6 / maximum. **NO MOVEMENT in the frozen exact-prime metric: `1213 -> 1213`; retained exact set `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`; unchanged count `5 -> 6`; status `PARTIAL / SOURCE OPEN / RETIRED-HANDOFF / SUCCESSOR_ADMISSION_REQUIRED`. Mandatory STUCK RECOVERY 2. Section-B moves used: #12 FIND WHAT IS CONSERVED, #20 FIND WHY THE ALGORITHM FAILS, #26 HUNT THE SPORADIC CASE.**

# R20 / I0100 — STUCK RECOVERY 2 and six-run rotation handoff

Repository / branch: `yspennstate/math-open-problems` / `master`.
Canonical claim recovered: `operations/claims/I0100.md` (owner R20, CLOSABLE OUTSIDE).
Outside source: Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26; stable compilation arXiv:2603.29571.
Source target:
\[
T_p:=\vartheta(\overline{G_{p,1}})\sim \sqrt{p/2},
\qquad p\equiv1\pmod4\text{ prime}.
\]
Here `G_{p,1}` is the induced Paley graph on the nonzero quadratic residues / neighbors of `0`, and theta is the clique-bounding Lovasz theta of the **complement** used by the source.
Frozen metric: largest admissible prime with matching exact primal/dual certificates for this source-normalized theta quantity, preserving the complete exact-covered prime set.

This is the mandatory second thinking-only stuck recovery. No new finite checker, numerical SDP certificate, theorem-sized claim, or prime extension was produced. The purpose of the run is to identify exactly why the accumulated routes have stalled, state what a successful proof must contain that none of them currently contains, and execute the owner-required six-unchanged-run rotation protocol honestly.

## 1. Continuity, whole-repository gate, ownership, source status

I continued from the newest R20 report

`runs/R20/2026-09-17T20-12-30Z_i0100_wendel_labelled_orthant_nogo_91d4c7.md`

rather than restarting. That run recorded `1213 -> 1213`, unchanged count `4 -> 5`, and selected this invocation as mandatory `STUCK RECOVERY 2` with moves `#12/#20/#26`.

Before the recovery I reread/recovered the required control surfaces: campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the latest new-methods deployment/status records, canonical claim `operations/claims/I0100.md`, the newest own R20 report, the current neighboring P04/I0101 report, and the distinct I0102/I0103 claims. The repository still assigns I0100 exclusively to R20. P04/I0101 remains Conjecture 27 two-localization; I0102 remains the distinct degree-four SoS problem; I0103 remains the distinct Paley-ETF problem. None is imported into this handoff.

Fresh public source/current-literature check dated **2026-09-17** used the bounded queries

- `Randomstrasse Conjecture 26 Paley localization theta`;
- `"Paley" "Lovasz theta" localization 2026`;
- `"Conjecture 26" "Randomstrasse" Paley`.

The current Randomstrasse source page still states Conjecture 26 in the source normalization, and the current Jig root is still explicitly titled `Open`. A bounded search also recovered 2026 Paley exact-subgraph-hierarchy work, the 2024 block-diagonal/localization paper, and the current formal/public partial reductions, but no paper or source page claiming a source-matching proof or refutation of the asymptotic. This is a dated bounded search, not an exhaustive citation-graph search and not a novelty certificate.

Source pages checked:

- `https://randomstrasse101.math.ethz.ch/posts/PaleyGraph/`
- `https://jig.so/p/7`
- `https://arxiv.org/abs/2603.29571`

## 2. Frozen metric and six-run boundary

The exact-certified frontier entering and leaving this thinking-only run is
\[
\boxed{p_{\max}=1213}
\]
with complete retained exact-certified set
\[
\boxed{\{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213\}}.
\]
No floating SDP output is counted as an exact certificate.

The supported unchanged count advances
\[
\boxed{5\longrightarrow6}.
\]
Under `NEW-METHODS-2026-09-16`, a CLOSABLE OUTSIDE target rotates after six unchanged runs. Therefore this report is also the R20 handoff for I0100: **R20 must not make a seventh unchanged research attack on Conjecture 26 under this assignment.** The source itself remains OPEN; this is an operational rotation, not a mathematical retirement of the conjecture.

## 3. Exact blocker required by Section I

The strongest exact finite-dimensional reduction accumulated by R20 is the rank-one Grassmann / oriented-matroid sweep. Put
\[
m=n-1,\qquad P=\frac1m\mathbf1\mathbf1^\top,\qquad A_q=I+(q-1)P,
\]
and let `B` represent the appropriate complementary half-Fourier subspace. Then
\[
M(q)=BA_q
\]
has maximal minors affine in `q`, and the theta threshold `q_p` is the first wall carrying the correct **positive-circuit / nonnegative-cocircuit orientation signs**. The source conjecture is equivalent to `q_p -> 1` through the exact relation
\[
q_p=\frac{\sqrt n\,(T_p-1)}{n-T_p}.
\]

The exact blocking statement is therefore:
\[
\boxed{
\text{identify a sign-compatible wall }I_p\text{ for which}\qquad
q_p
=1-\frac{\Delta_{I_p}(1)}{\Delta_{I_p}(1)-\Delta_{I_p}(0)}
\longrightarrow1.
}
\tag{B}
\]
The hard word is **sign-compatible**. Bounds for arbitrary determinants, arbitrary small minors, or marginal Jacobi values do not identify the positive circuit/cocircuit that controls the labelled positive orthant.

## 4. #12 FIND WHAT IS CONSERVED — the deformation preserves all affine column geometry

The most useful invariant is already implicit in the rank-one formula and explains why several apparently different R20 reformulations keep returning to the same obstruction. Since
\[
BA_q
=B+\frac{q-1}{m}(B\mathbf1)\mathbf1^\top,
\]
every column of `B` receives the **same translation vector** as `q` varies. Consequently all pairwise column differences and the affine oriented matroid of the column configuration are fixed; only the position of the origin relative to that fixed affine configuration moves along one line.

Normalizing a nonzero feasible kernel vector `x>=0` by `1^T x=1` rewrites
\[
BA_qx=0
\]
as the assertion that the single moving point
\[
-\frac{q-1}{m}B\mathbf1
\]
lies in the fixed convex hull of the columns of `B`. This is not promoted as a new theorem claim in this thinking-only run; it is the same geometry already encoded by the earlier projected-simplex/HULL and Grassmann-line reductions.

**What this conserved structure tells us:** the missing information is not high-dimensional motion of the whole subspace. The entire difficulty is the support facet / labelled orientation met by one deterministic line through one highly arithmetic polytope. Any future route that ignores which facet has the correct positivity signs is throwing away the only non-conserved datum.

## 5. #20 FIND WHY THE ALGORITHM FAILS — exact finite continuation is exponential in the wrong variable

There is an obvious exact algorithm at each fixed prime:

1. form the affine maximal minors / circuit cofactors of `M(q)`;
2. compute their real wall roots;
3. sort the roots;
4. propagate the oriented-matroid sign chamber;
5. stop at the first chamber boundary at which a positive circuit appears/disappears.

This algorithm is conceptually complete for a fixed finite instance, and it is another way to recover the exact LP threshold. It does **not** create an asymptotic mechanism. In the Paley half-dimensional regime there are exponentially many candidate bases/circuits. More importantly, individual character-sum or determinant-magnitude estimates do not tell us which of those exponentially many walls is the labelled positive-circuit wall.

The failure is therefore not merely computational complexity. Even an oracle giving the magnitude of every single minor to square-root precision would still leave the **joint sign/orientation selection problem**. This is exactly why the following earlier routes stalled:

| Route tried | What it established | Precise failure for the source asymptotic |
|---|---|---|
| Exact primal/dual continuation and small cases | Proof-grade finite certificates through `p=1213` | Finite continuation has no uniform prime mechanism. |
| Raw half-Fourier/Jacobi certificate | Exact one-point formula and arcsine behavior; exposed the `sqrt(2)` endpoint | The certificate itself asymptotically reaches the bad endpoint; sharpening the same one-point bound cannot give constant `1`. |
| Sparse/dense repair analysis | Showed a successful correction must reorganize a positive fraction of coordinates | It did not construct the required dense correction. |
| Entropy/Gibbs/Fisher deformation | Canonical path from uniform point to optimum; exact Schur-complement curvature | Scalar curvature does not control the anisotropic vector Lagrange multiplier; a vector covariance theorem is missing. |
| Projected-simplex / balancing formulation | Exact radial-depth problem and explicit balancing operator | Affine/common profiles remain at the old barrier; complementary halves require genuinely different nonlinear profiles. |
| Quadratic and fixed low-degree balanced profiles | Identified additive representation counts / Legendre-trace transforms as nonlinear tensors | Discovery computations stayed far below the full optimum; no all-degree pointwise positivity theorem emerged. |
| Haar/Gaussian/statistical-dimension comparison | Identified the self-dual constant and rank-one stretched-orthant phase transition | Random rotational/sign exchangeability does not determine the distinguished deterministic Paley orthant. |
| Grassmann-line / affine Pluecker sweep | Reduced every wall to an affine root and the threshold to a labelled oriented-matroid event | Magnitude control does not select the sign-compatible wall. |
| Wendel/Schlaefli/Cover port | Clarified the random chamber-count mechanism | Total chamber count provably loses the positive-orthant label; the deterministic event survives exactly in circuit/cocircuit signs. |
| Fixed weaker `4/3` target | Reduced a genuine strict improvement to exclusion of positive circuits at one fixed stretch | Even this weaker target still needs joint cofactor-sign control not supplied by known marginal arithmetic estimates. |

This inventory is the core handoff: another worker should not restart any of these routes without a new ingredient that attacks the labelled orientation itself.

## 6. #26 HUNT THE SPORADIC CASE — finite overshoots are diagnostic, not an asymptotic counterexample

The exact finite programme has already found source-scale overshoots (for example the archived exact `p=1201` and `p=1213` packages). Their role is important but limited: they rule out the tempting pointwise strengthening `T_p <= sqrt(p/2)` and show that the eventual proof must carry an error term / allow sign oscillation around the limit.

A genuine refutation of Conjecture 26 would need an **infinite** admissible-prime subsequence with `|q_p-1|` bounded away from zero (equivalently `T_p/sqrt(p/2)` bounded away from one), not another isolated overshoot. No mechanism producing such an infinite family was found in this run. Conversely, the presence of finite overshoots means that a proof strategy built on eventual one-sided monotonicity is unsupported by the existing exact data.

The sporadic search therefore points back to the same missing object as (B): one must understand the arithmetic distribution of the **labelled support facet/orientation**, not just the scalar theta value at a handful of primes.

## 7. What a successful proof must contain that no attempted route contains

A source-level proof now appears to require a deterministic **global orientation theorem** for the Paley half-Fourier configuration. In one equivalent form, for every fixed `epsilon>0` and all sufficiently large admissible primes, it must certify the correct side of the positive-orthant feasibility event at stretches `q=1+epsilon` (and, by complementary duality, the opposite half). In the affine-Pluecker language it must control the joint signs of a complete circuit/cocircuit family at the relevant wall; in the convex-hull language it must control the supporting facet hit by a fixed radial line.

None of the current routes supplies that. Available character-sum inputs control one-point Jacobi values, low-order additive moments, or individual spectral quantities. The missing theorem must couple **many** of those quantities strongly enough to decide a global labelled orientation. A future proof that contains only marginal square-root cancellation is therefore very likely to reproduce an already-recorded barrier.

## 8. Simplest special case still unproved

The simplest source-relevant theorem isolated by the first recovery remains
\[
\boxed{T_p\le \frac43\sqrt n\qquad(n=(p-1)/2)}
\tag{W}
\]
for all sufficiently large admissible primes. This is much weaker than Conjecture 26 and would already strictly improve the classical `sqrt(2n)`-scale theta upper barrier.

The exact fixed-stretch sufficient test is exclusion of a positive Paley circuit at `q=4/3`, since
\[
\frac{T(4/3)}{\sqrt n}=\frac{4\sqrt n+3}{3\sqrt n+4}<\frac43.
\]
Even (W) remains unproved because the same joint circuit-sign problem is present at this single fixed scale. This is the cleanest special case for any future reassignment that wants a measurable first theorem rather than immediately re-attacking `q_p -> 1`.

## 9. Nearest solved analogue and exactly what it has that Paley lacks

The nearest solved analogue is the random/Haar half-dimensional subspace intersecting a positive orthant / rank-one stretched orthant. Wendel-Schlaefli-Cover chamber counts and modern conic intrinsic-volume / statistical-dimension formulas solve the random orientation problem because rotational or sign-exchangeability makes the orthant labels statistically interchangeable.

The deterministic Paley configuration does not have that exchangeability. Its cyclic/arithmetic symmetry is strong enough to reduce the SDP to an LP and to expose Jacobi/Legendre structure, but it does **not** randomize the distinguished positive-orthant label. The first stuck recovery tried to port the random chamber-count proof and the latest run isolated this loss of label as a structural no-go. Any successful transfer from the random theory must therefore replace exchangeability by an arithmetic theorem about labelled orientations, not merely import another unlabelled intrinsic-volume count.

## 10. Mandatory recovery decision and rotation

Section I requires exactly one recovery action. The first recovery selected `port the technique from the nearest solved problem`; that Wendel/Cover port has now been diagnosed and does not supply the missing label.

For this second recovery I select:

\[
\boxed{\textbf{MOVE TO THE NEXT PROBLEM IN QUEUE AND RECORD THE SWITCH.}}
\]

The six-unchanged-run CLOSABLE rule independently requires the same operational outcome.

However, the most recent coordinator admission screen available before this report (`operations/task_health/runs/2026-09-17T195400Z/status.md`, captured master `c646dc43955779f322cdb0af1ea4d70801cff212`) explicitly found **zero new lawful `READY + CLOSABLE + UNASSIGNED` successors** after source/current-status/ownership/route screening. It records multiple CLOSABLE lanes already sitting in `ADMISSION GAP` rather than inventing replacements. The root `QUEUE.md` itself warns that its listed candidates are not automatically READY. Consistent with the owner contract, I therefore do **not** steal a claimed target, promote a PENDING/HOLD row, or create a fictitious successor claim merely to fill R20.

Operational result:

- I0100 is handed off from active R20 attack after the supported six-run no-movement boundary.
- The mathematical source remains `OPEN / PARTIAL`; no source claim is closed or refuted.
- R20 enters `SUCCESSOR_ADMISSION_REQUIRED` rather than beginning a seventh I0100 attack.
- No new canonical claim was created because no lawful READY + CLOSABLE + UNASSIGNED successor was established by the current admission screen.
- The next R20 invocation should re-screen the current queue/intake for a newly admitted lawful successor; it should **not** resume I0100 unless the owner explicitly reassigns it with a fresh route.

For the eventual successor, the next Section-B starting triple is **#2 ATTACK THE NEGATION FIRST, #18 SAY IT IN ANOTHER LANGUAGE, #24 FIND THE EXTREMAL OBJECT**, replacing any member already exhausted in that successor's recovered history. These are successor moves, not authorization for a seventh I0100 run.

## 11. Handoff payload for a future reassignment of I0100

If I0100 is later reassigned to a fresh worker, continue from this exact state rather than restarting:

- Source statement: `T_p = theta(complement G_{p,1}) ~ sqrt(p/2)`.
- Graph normalization: choose primitive `g mod p`, `alpha=g^2`, identify nonzero squares with `Z_n`, `n=(p-1)/2`, and
  \[
  G_{p,1}=\operatorname{Cay}(\mathbb Z_n,S_p),\qquad
  S_p=\{d\ne0:\alpha^d-1\text{ is a nonzero square mod }p\}.
  \]
- Frozen exact frontier: `p_max=1213`.
- Complete exact-covered set: `{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.
- Best exact asymptotic coordinates: radial constants / rank-one stretch `q_p`, with
  \[
  q_p=\frac{\sqrt n(T_p-1)}{n-T_p},\qquad T_p/\sqrt n\to1\iff q_p\to1.
  \]
- Best finite-dimensional blocker: the sign-compatible affine-Pluecker wall (B).
- Best weak theorem to target first: eventual `T_p <= (4/3)sqrt(n)` / no positive circuit at fixed `q=4/3`.
- Do not repeat raw Jacobi, scalar Fisher, affine balancing, fixed low-degree profile, unlabelled Haar/Wendel, arbitrary-minor, or chamber-count-only routes without a genuinely new labelled-orientation ingredient.
- No source-asymptotic OTHER-track audit exists; existing outside audits are finite-package audits only.

## 12. Scheduler/model control status

The scheduler limitation remains unchanged. The exposed task control schema offers prompt/title, schedule/timing, enabled state and timing mode. It exposes **no binding model-family selector, no reasoning-effort selector, no authenticated completed-run model receipt, and no guaranteed-duration field**. GPT-6/maximum therefore remains prompt-only.

The historical `P26` modification refusal was context/ownership-dependent; the later native deployment record shows that an authorized context successfully updated P26. That same deployment also records R-series edits being denied in that context. The legitimate remedy is an authorized owning product/workspace or platform/API surface that actually exposes model and reasoning controls; there is no permission-bypass workaround and no duplicate task should be created.

No scheduler change, email, Drive write, public posting, purchase, permission change, shared-root edit, or peer-track edit was performed in this run.

## 13. Structured ledger_delta

```yaml
ledger_delta:
  worker: R20
  lane: CLOSABLE_OUTSIDE
  source: "Afonso S. Bandeira et al., Randomstrasse101 (2025), Conjecture 26 / intake I0100"
  target: "theta(complement G_{p,1}) ~ sqrt(p/2)"
  graph_definition: "G_{p,1} is the induced Paley graph on nonzero quadratic residues; in exponent coordinates Cay(Z_n,S_p), n=(p-1)/2"
  metric: "largest admissible prime with matching exact primal and dual certificates"
  metric_before: 1213
  metric_after: 1213
  covered_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
  movement: "NO MOVEMENT"
  unchanged_count_before: 5
  unchanged_count_after: 6
  status: "PARTIAL / SOURCE OPEN / RETIRED-HANDOFF / SUCCESSOR_ADMISSION_REQUIRED"
  tried_moves: [12,20,26]
  stuck_recovery: "2/2"
  recovery_action: "MOVE TO NEXT PROBLEM IN QUEUE"
  successor_claim: "NONE — latest admission screen found zero lawful READY+CLOSABLE+UNASSIGNED targets"
  remaining_obligation: "control the labelled sign-compatible Paley circuit/cocircuit wall so q_p -> 1; even q=4/3 remains open"
  source_current_check: "2026-09-17; Randomstrasse source and current Jig still state the conjecture/open root; bounded search found no source-matching resolution"
  asymptotic_audits: []
  evidence:
    - "runs/R20/2026-09-17T20-12-30Z_i0100_wendel_labelled_orthant_nogo_91d4c7.md"
    - "operations/claims/I0100.md"
    - "operations/task_health/runs/2026-09-17T195400Z/status.md"
  next_methods_for_successor: [2,18,24]
```

**NO CLOSURE CLAIM. I0100 remains mathematically OPEN; R20 rotates because the CLOSABLE six-unchanged-run protocol has been reached.**