Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum.** Primary metric **no movement**: `L_6 >= 0 -> L_6 >= 0`; this is the required **STUCK2** thinking run, so it makes no new theorem-sized claim and adds no checker; methods tried: **B8 / B17 / B27**.

# HARD7-06 run 7 — STUCK2: replace local scalar surrogates by a source-compatible channel/cluster enclosure

Status: **PARTIAL / Chang--Kolhe--Sohn k=3 sharpness conjecture remains OPEN under a bounded current-literature review.**

Repository / branch: `yspennstate/math-open-problems` / `master`.

Canonical ownership remains `operations/claims/CKS-2024-RREG-HYPER2COL-K3.md`, owner `HARD7-06`. This report is the second Section-I thinking/recovery report. It deliberately does not manufacture another auxiliary lemma after the frozen source metric failed to move through the first recovery cycle.

## 1. Continuity, source status, ownership, and current literature

Before choosing the second recovery I reread the controlling HARD7 files, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, the canonical claim, the full HARD7-06 run history through `2026-09-19T01-50-00Z__soft_tilt_no_go.md`, and the neighboring F0097/random-3-SAT ownership history. I also checked the relevant intake record in `probability_1000_intake_F_20260908/batches/b07_kalai_frieze.json`. The initial random 3-SAT candidate is still not available to this track merely by alias: its canonical history is F0097/R03, so I do not duplicate it or infer release from an old handoff.

The source target remains Evan Chang, Neel Kolhe, Youngtak Sohn, *Upper Bounds on the 2-Colorability Threshold of Random d-Regular k-Uniform Hypergraphs for k >= 3*, APPROX/RANDOM 2024, LIPIcs 317, Article 47, DOI `10.4230/LIPIcs.APPROX/RANDOM.2024.47`, full version arXiv:2308.02075. Their explicit upper bound is conjectured sharp; Table 1 has `ceil(d_*(3))=7`, while the source locates `d_*(3)` above 6. Thus the admitted lower-side boundary remains the uniformly random **simple** 6-regular 3-uniform hypergraph.

A fresh bounded literature screen on 2026-09-19 checked the exact CKS title/arXiv identifier, `random regular NAE-SAT k=3 d=6`, `random regular 3-uniform hypergraph 2-colorability d=6`, and recent reconstruction/scaling-window work. It recovered the source and no later theorem proving the exact simple-uniform `H_{n,6,3}` lower side. This is bounded negative evidence, not proof of worldwide openness.

Three recent/nearest items materially affect method choice without closing the source:

1. **Yuzhou Gu, arXiv:2606.21699, 19 June 2026, _Exact reconstruction thresholds on hypertrees over a symmetric binary alphabet_.** The abstract gives exact reconstruction thresholds for a class of symmetric-binary hypertree broadcasts and, as a consequence, identifies condensation with the Kesten--Stigum threshold for random NAE-SAT and random hypergraph bicoloring of arity at most four at any temperature. The proof uses robust non-reconstruction, binary-memoryless-symmetric (BMS) channel comparison, and rigorous computer-assisted population dynamics. This is a reconstruction/condensation result, not a proof that the source's simple random 6-regular 3-uniform hypergraph is 2-colorable w.h.p.
2. **Ding--Sly--Sun, _Satisfiability Threshold for Random Regular NAE-SAT_**, gives the exact satisfiability threshold for sufficiently large `k`, not for `k=3`.
3. **Nam--Sly--Sohn I/II and Sly--Sohn's local-geometry work** supply the cluster/frozen-configuration, 1RSB, small-subgraph-conditioning, and unbounded-state-space architecture used in the solved large-`k` regime. Their large-`k` hypotheses are exactly what is missing here.

I also found Gaia Carenini's August 2026 scaling-window work, which gives `O(n/log n)` windows for fixed-`k` random k-SAT and related non-two-colourability models. That is a sharpness-width result in a different ensemble/parameterization; it does not locate the present random-regular `k=3,d=6` threshold and therefore does not change this target's status.

No POSTED/INDEX/claim collision or source-matching external resolution was found.

## 2. Frozen source metric

The metric remains the admission metric

\[
L_6:=\sup\left\{L\in[0,1]:\liminf_{n\to\infty}
\Pr(H_{n,6,3}\text{ is 2-colorable})\ge L\right\},
\]

along the source-admissible `n` in the uniformly random **simple** 6-regular 3-uniform model.

Nothing in this thinking run gives a positive source-model probability. Hence

\[
\boxed{L_6\ge0\quad\longrightarrow\quad L_6\ge0.}
\]

This is **no movement**. In particular, reconstruction, a nontrivial tree fixed point, a finite channel computation, or a positive physics complexity by itself is not promoted to a lower bound on `L_6`.

## 3. Section I(a): exact blocker

The first recovery established that the object must be richer than raw solutions, minority profiles, three-state warnings, or a factor-local size tilt. The source-facing obstruction can now be stated more sharply.

A successful proof must construct a genuine nonnegative cluster-weighted random variable `Y_n` for the **random regular configuration model**, with the implication that a counted object yields an actual proper 2-coloring, and must establish enough moment/conditioning control that

\[
\boxed{
\begin{gathered}
Y_n>0\ \Longrightarrow\ H_{n,6,3}\text{ has a proper 2-coloring},\\
\liminf_{n\to\infty}\frac1n\log\mathbb E Y_n>0,\\
\sup_n\frac{\mathbb E Y_n^2}{(\mathbb E Y_n)^2}<\infty
\quad\text{after the required short-cycle correction},\\
\text{and the conclusion survives conditioning on simplicity.}
\end{gathered}}
\tag{I.2}
\]

Any comparable quenched argument replacing the displayed second-moment line would also suffice, but some bridge of this strength is necessary. What blocks the source is therefore not merely "find a tree fixed point"; it is

\[
\boxed{
\text{turn a source-compatible nontrivial cluster/channel recursion at }(k,d)=(3,6)
\text{ into (I.2), hence }L_6>0.
}
\tag{I.3}
\]

No route tried so far contains this bridge.

## 4. Section I(b): every route tried and the precise failure

### Route 1 — raw balanced-solution second moment (run 1; B2/B11/B24)

The exact overlap curvature at independence is

\[
S_d''(0)=\frac{2d-11}{11},\qquad S_6''(0)=\frac1{11}>0.
\]

**Failure:** the independent overlap is not even a local maximum at `d=6`. A Paley--Zygmund proof for the ordinary solution count is structurally miscentered.

### Route 2 — global raw-overlap analysis (run 2; B1/B6/B20)

The full symmetric raw-count problem has a nonzero correlated saddle/global maximizer; the instability is born in a pitchfork at `d_c=11/2`.

**Failure:** the run-1 sign is not a missing estimate. The raw count is genuinely dominated by correlated solutions.

### Route 3 — linear minority-incidence tilt (run 3; B12)

For every proper coloring, the minority-incidence statistic satisfies the exact conservation law

\[
\sum_v R_v=2n.
\]

**Failure:** `exp(lambda sum_v R_v)` is constant on proper colorings, so this tilt cannot alter the overlap landscape.

### Route 4 — nonlinear profile-conditioned count (run 3; B15/B3)

The deformation `p_alpha=(1-alpha)q+alpha delta_2` produced a positive one-replica annealed exponent and, at a clean rational `alpha`, a negative-definite local feasible two-replica Hessian.

**Failure:** this is only local stability. The global pair variational inequality, type prefactors, cycle fluctuations, and configuration-to-simple transfer remained open. `L_6` did not move.

### Route 5 — cluster/frozen hard-field port (runs 4--5; first Section-I recovery)

The large-`k` cluster architecture was specialized first to a finite `{0,1,f}` warning alphabet. The exact unweighted hard-field surrogate bifurcates only after the source boundary (`d<=6` has no nonzero hard-field fixed point, while `d=7` does). More importantly, arbitrarily long free trees already produce infinitely many distinct likelihood ratios/Fibonacci-type size data.

**Failure:** the three-state alphabet cannot preserve exact cluster sizes, so it is too small for a source-valid cluster count at `k=3`.

### Route 6 — exact soft likelihoods with factor-local `S^lambda` tilt (run 6; B5/B7/B21)

Keeping the full soft likelihood `X` but reweighting each factor locally by `S(X,Y)^lambda` still fails. On symmetric two-point perturbations the exact variance multiplier satisfies

\[
\Gamma_\lambda(t)>1\qquad(t>0,\ 0\le\lambda\le1),
\]

with infinitesimal limit `10/9`.

**Failure:** a factor-local scalar normalization is not the Nam--Sly--Sohn 1RSB measure and cannot stabilize the soft-message origin. It omits variable normalization correlations, free-tree structure, and global cluster weight.

The first recovery therefore succeeded as a diagnosis but not as source movement: it identified two classes of insufficient cluster surrogates without producing (I.2).

## 5. Section I(c): what a proof must contain that no route so far contains

A viable second-recovery route must contain **all** of the following, not merely one more local coefficient.

1. **A source-compatible cluster state.** It must retain the unbounded free-tree/soft-message information required by exact cluster sizes. A finite warning alphabet or independently tilted factor law is not enough.
2. **Rigorous distributional control.** The order parameter is now a probability law/channel, not one scalar. Any finite discretization must be an exhaustive enclosure in a certified order (for example BMS degradation/Blackwell order), not a sample of trajectories.
3. **The actual cluster weight/free-energy functional.** The weight must be derived from the finite-`k` NAE/hypergraph coarsening and node/factor normalizations used by the solved cluster theory. An invented `S^lambda` surrogate is no longer acceptable.
4. **Positive one-replica cluster complexity in the correct ensemble.** A nontrivial broadcast fixed point alone says nothing about satisfiability probability.
5. **Global pair or quenched control.** The construction must survive correlated pairs/clusters; local linear stability is insufficient.
6. **Cycle and simplicity transfer.** The random regular configuration model has short-cycle fluctuations, and the source is the uniform simple model. A genuine small-subgraph-conditioning or comparable argument must be included before source movement is claimed.
7. **A logical witness map.** Every counted cluster/frozen object used for the lower bound must be shown to contain/produce an actual proper coloring; coarsening need not be surjective in general.

The nearest solved proofs possess versions of items 1--7 for sufficiently large `k`; the present track has none of them simultaneously at `k=3`.

## 6. Section I(d): simplest special case still unproved

The simplest special case worth proving now is not another scalar warning recursion. It is a **certified regular-tree channel/cluster enclosure** for the exact finite-`k` cluster transform.

For orientation only, rewrite run 6's unweighted soft BP map in magnetization coordinates

\[
m=\tanh(X/2),\qquad n=\tanh(Y/2).
\]

The same algebraic map becomes

\[
\widehat m=-\frac{m+n}{3-mn},
\tag{6.1}
\]

and a degree-six cavity variable combines five factor messages by

\[
m'=\tanh\!\left(\sum_{i=1}^{5}\operatorname{artanh}\widehat m_i\right).
\tag{6.2}
\]

Equations (6.1)--(6.2) are only a coordinate rewrite of the already-recorded unweighted recursion, **not** a new theorem and **not** the desired 1RSB transform. Linearization reproduces the already-known `10/9` Kesten--Stigum-shaped multiplier; this reinforces the conclusion that forcing contraction to the paramagnetic origin is the wrong goal.

The bridge subproblem for the next recovery is therefore:

> Recover from the actual finite-`k` Nam--Sly--Sohn frozen/cluster definitions the exact cluster-weighted channel transform `T_lambda` and its Bethe/complexity functional at `(k,d)=(3,6)`. If it admits a BMS-channel representation, find explicit finite atomic lower/upper channels `W_-`, `W_+` and a certified channel order such that a nontrivial invariant interval is trapped,
> \[
> W_-\preceq T_\lambda(W_-),\qquad
> T_\lambda(W_+)\preceq W_+,
> \tag{6.3}
> \]
> while rigorously certifying a strictly positive lower bound for the **same** cluster complexity/free-energy functional on the trapped set.

Here `\preceq` is intended as an information/degradation order only if the exact transform preserves it; this monotonicity itself must be proved before using (6.3). Finite BSC mixtures would be an enclosure basis, not Monte Carlo evidence. Success on (6.3) would still be **PARTIAL** and would not move `L_6` until the global random-regular bridge (I.2) is supplied.

This is the smallest special case that simultaneously respects the run-5 infinite-state obstruction and the run-6 local-tilt no-go.

## 7. Section I(e): nearest solved problems and the missing ingredient

There are two complementary nearest solved pieces.

### Source-level analogue: sufficiently-large-k random regular NAE-SAT

Ding--Sly--Sun establish the satisfiability threshold in the sufficiently-large-`k` regular model. Nam--Sly--Sohn's 1RSB work exposes the architecture useful here: cluster/frozen configurations, a genuinely cluster-weighted partition function, tree recursions on an unbounded state space, moment analysis, and then small-subgraph conditioning / Doob-Fourier variance decomposition to convert moments to high-probability statements.

**What it has that this problem lacks:** quantitative control whose error terms close only in their large-`k` regime. At `k=3`, the local instability and infinite family of soft free-tree messages cannot be discarded as small errors.

### Local information-theoretic analogue: Gu 2026

Gu's hypertree theorem uses BMS channel comparison and rigorous population dynamics to certify reconstruction behavior in a symmetric-binary setting, including NAE-SAT/hypergraph bicoloring consequences at low arity.

**What it has that this problem lacks:** a rigorous order/comparison framework for an infinite-dimensional distributional recursion. **What it does not supply for us:** the source's finite-simple random-regular satisfiability lower bound, the exact cluster-count witness `Y_n`, or the cycle/simplicity transfer in (I.2).

The useful synthesis is therefore not "reconstruction implies colorability." It is: use Gu's channel-order technology to control the **local distributional part** of the actual NSS cluster transform, then use the random-regular cluster/SSC architecture for the **global probability part**. Both modules are required.

## 8. Three new Section-B moves

### B8 — go the other way and discretize

**Promising, but only after deriving the correct transform.** The infinite-dimensional BMS/channel law can in principle be bracketed by finite mixtures of binary symmetric channels with outward-rounded rational/interval parameters. If the transform is monotone in a degradation order, each step can produce rigorous upper/lower channel bounds instead of empirical population dynamics. This would turn a continuum search into a finite certificate without confusing finite sampling with proof.

The crucial discipline is order: first derive `T_lambda` from the genuine cluster measure; second prove the order it preserves; only then discretize. Discretizing the run-6 surrogate would merely certify the wrong object more precisely.

### B17 — look for the number somewhere else

**Changed the interpretation of the run-6 obstruction.** The exact infinitesimal multiplier `10/9` has the Kesten--Stigum form for `(k,d)=(3,6)`. Gu's 2026 theorem puts Kesten--Stigum/channel comparison at the center of low-arity NAE/bicoloring reconstruction. This does not establish equivalence with satisfiability; it says the number should be read as evidence that the paramagnetic contraction strategy is misposed, not as evidence that colorability fails.

The method lesson is to seek/control the nontrivial distributional channel rather than force the origin to be stable.

### B27 — swap the quantifiers

The failed routes effectively sought a statement of the form

\[
\text{for every small perturbation / every local message, the symmetric state contracts.}
\]

Run 6 proves that this universal contraction statement is false in a natural soft family. The second recovery asks a different question:

\[
\text{does there exist a nontrivial, source-compatible trapped channel/cluster region with positive certified complexity?}
\]

This is a meaningful quantifier swap because the source only needs existence of enough proper-coloring clusters, not contraction of every boundary condition to the unbiased state. The price is that existence must then be coupled to the global random-regular probability bridge (I.2); otherwise it remains tree physics rather than source progress.

## 9. Exactly one Section-I recovery choice

**Chosen second and final recovery: REDUCE THE OBSTRUCTION TO A FINITE CERTIFIED COMPUTATION.**

This is not permission to run another heuristic population-dynamics script. The next substantive HARD7-06 run has one concrete checkpoint:

1. recover the exact finite-`k` cluster/frozen recursion and cluster weight from the Nam--Sly--Sohn definitions, specialized to unsigned hypergraph bicoloring at `(k,d)=(3,6)`;
2. determine whether that exact transform has a BMS/degradation-order representation suitable for Gu-style comparison;
3. if yes, construct a rigorously outward-rounded finite atomic channel enclosure for a nontrivial invariant region and interval-evaluate the **actual** cluster complexity functional; if no, record the precise order/representation obstruction rather than replacing the transform by another surrogate;
4. only a successful positive enclosure earns a next-stage attempt at the global pair/SSC/simple-model bridge (I.2).

This is recovery cycle #2. If this route cannot produce a source-compatible positive cluster certificate, or if the frozen source obligation is unchanged at the next Section-I trigger, CONTROL.md requires a handoff and rotation to a fresh eligible CSP target. No third recovery on this target is authorized.

## 10. Capability honesty

The exposed scheduler interface still provides title, prompt, schedule/timing mode, and enabled state, but no model selector, reasoning-effort selector, or guaranteed execution duration. GPT-6 maximum therefore remains requested in prompt text only. This report actually ran under **GPT-5.6 Sol**; reasoning telemetry is **UNVERIFIED**. Changing that requires an authorized product/scheduler surface that exposes model/reasoning controls or platform support; repository text cannot change runtime selection.

The historical `You cannot modify this task` result for one P26 context is not a universal current denial: repository deployment records say P26 later updated successfully in a different authorized context. I did not probe or alter P26 or any other schedule. If such a denial recurs, the permitted remedy is the authorized account/workspace ownership context or platform support, not bypassing the restriction or creating a duplicate task.

## 11. Persistence / ledger delta

No new code or checker is warranted in this thinking run. The mathematical value of the run is the route decision and the exact source-facing blocker, not another certificate for an unchanged metric.

```yaml
ledger_delta:
  worker: HARD7-06
  category: HARD_OUTSIDE
  target: CKS-2024-RREG-HYPER2COL-K3
  status: PARTIAL
  metric: L_6
  before: ">= 0"
  after: ">= 0"
  movement: "no movement"
  protocol_state: STUCK2
  methods: [B8, B17, B27]
  exact_blocker: "source-compatible cluster/channel construction plus random-regular moment/SSC/simple-model bridge yielding L_6>0"
  chosen_recovery: "REDUCE_OBSTRUCTION_TO_FINITE_CERTIFIED_COMPUTATION"
  recovery_detail: "derive exact finite-k NSS cluster transform, then Gu-style BMS channel enclosure and certified actual cluster complexity"
  checker: none
  next_stuck_policy: "third stuck episode hands off and rotates to a fresh CSP target"
  shared_root_write_requested: false
```
