Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO FIXED-METRIC MOVEMENT on H0008: `I_mf = a_hi-a_lo -> same`. STUCK-RECOVERY-2/2, THINKING-ONLY; no new theorem claims. Methods actually used: #10 DERANDOMIZE, #13 FIND WHAT ONLY INCREASES, #24 FIND THE EXTREMAL OBJECT.**

# R14 HARD OUTSIDE — H0008 stuck recovery 2/2: multitype regeneration as a Markov-renewal suspension

## 0. Continuity, ownership, and mandatory second recovery

This run continues the mandatory Section-I recovery state from

`runs/R14/2026-09-19T08-50-01Z_h0008_stuck_recovery1_rousselin_port_5e2c.md`

(created at commit `7740e422a0927ee19179c2b7794316a424d8f9d8`). I do **not** reopen the original negative-margin spherical-perceptron target, H0017, D0036, D0039, or D0034: those R14 targets were already terminally handed off in the immutable track history. The active exclusive R14 HARD OUTSIDE claim remains `operations/claims/H0008.md`.

The canonical source remains Achyut Kumar (2026), *Threshold cascades of interacting diffusions on unimodular random trees: a conditional branching-process universality theorem, the annealed pressure, and the dimension of the failed boundary*, arXiv:2608.15987v1 (17 Aug 2026), Section 12.3 open problem (6), **Boundary fluctuations**. The source asks for the multifractal spectrum of transmission-weighted flows and the harmonic measure of the failed cluster, with dimension drop expected in the latter problem. The companion Kumar--Duddala paper arXiv:2608.21125 (21 Aug 2026) treats front propagation/Bramson correction and continuous-type limit theory; it does not advertise a solution of this finite-type harmonic-measure problem.

The frozen metric was already saturated on the finite-type multifractal clause:

\[
I_{\rm mf}=a_{\rm hi}-a_{\rm lo}.
\]

No legal improvement of that metric is produced here. Status therefore remains **PARTIAL / SOURCE OPEN**. This is the **second and final permitted stuck recovery** on H0008. The next R14 invocation must terminally hand off H0008 and rotate to a lawful ownership-clear HARD OUTSIDE successor; a third H0008 recovery is not authorized.

No new theorem, lemma, finite certificate, or numerical endpoint is claimed in this report. The purpose of this recovery is to sharpen the handoff route until the missing statement is as small and explicit as possible.

## 1. Repository and current-literature read

Before research I recovered/scoped the current required repository state:

- `probability_campaign_2026_09/INDEX.md` and `RANKING.md`;
- root `POSTED.md`, `RESULTS.md`, and `QUEUE.md`;
- `operations/new_methods_2026-09-16/OWNER_DIRECTIVE.md`;
- `operations/claims/H0008.md`;
- the newest R14 H0008 recovery report quoted above;
- neighboring ownership/source checks, including the latest R19 record confirming that H0008 is HARD and exclusively owned by R14;
- the H-intake/source material identifying Kumar Section 12.3 open problem (6).

A fresh bounded literature check on **19 September 2026** recovered:

1. Kumar, arXiv:2608.15987v1, dated 17 Aug 2026, still as the source paper;
2. Kumar--Duddala, arXiv:2608.21125, dated 21 Aug 2026, still as the companion on front propagation and continuous-type limits;
3. Pierre Rousselin, arXiv:1708.06965 / EJP 2018, *Invariant Measures, Hausdorff Dimension and Dimension Drop of some Harmonic Measures on Galton-Watson Trees*;
4. Pierre Rousselin, arXiv:1711.07920, *Dimension Drop for Transient Random Walks on Galton-Watson Trees in Random Environments*;
5. the established one-type Lyons--Pemantle--Peres exit-ray/ergodic framework;
6. finite-type neighboring machinery such as Altok's multitype unimodularity and Dembo--Sun's multitype reversing-measure construction.

Searches included exact-title/arXiv queries and combinations of `multitype Galton-Watson`, `harmonic measure`, `exit environment`, `regeneration`, `invariant measure`, and `dimension drop`. No current primary source surfaced that simply supplies the exact finite-type harmonic-exit invariant law needed here. This is bounded negative search evidence only, not a worldwide novelty certificate.

Rousselin's random-environment paper explicitly says its one-type invariant forward environment is constructed at exit times using **regeneration times and ergodic theory** and is absolutely continuous with respect to the joint tree/path law. That remains the nearest solved mechanism.

## 2. (a) Exact blocking statement

The previous R14 reduction is retained unchanged. For source root-type laws `P_i`, escape conductance `B`, size-biased potential offspring count `\widehat\nu`, and sibling-conductance sum `R_i`, the candidate Radon--Nikodym densities must solve

\[
\boxed{
(\mathcal Lh)_j(b)
=
 m_*q_j b\sum_i p_{ij}\,
 \mathbb E\!\left[
 \frac{
 h_i\!\left(\dfrac{b+R_i}{1+b+R_i}\right)
 }{b+R_i}
 \right],
\qquad b>0,
}
\tag{2.1}
\]

with

\[
\boxed{
\mathcal Lh=h,
\qquad
h_i(b)>0\quad P_i\text{-a.e. on }\{b>0\},
\qquad
\sum_i\mathbb E_i[h_i(B)]=1,
}
\tag{2.2}
\]

plus the logarithmic integrability required by the already-established PF--KL reduction.

The sole-infinite-child channel `R_i=0` has already been isolated in earlier R14 work and its extinction Jacobian shown spectrally subcritical. The unresolved channel is therefore still

\[
\boxed{R_i>0,}
\tag{2.3}
\]

meaning the genuine branch point at which another infinite sibling competes with the harmonic descendant.

## 3. (b) Every route tried and the precise failure

The consolidated failure map from recovery 1 remains valid, with one important refinement from this run.

1. **Shifted pressure / branching-random-walk route.** It solves the finite-type multifractal clause under the recorded hypotheses. It does not encode the random sibling normalization of harmonic flow.

2. **Pressure-only harmonic formula.** Explicit one-type examples with the same pressure curve and different harmonic dimensions show that even the full pressure function is insufficient.

3. **Electrical recursion.** The recursion `B=S/(1+S)` and harmonic weights `B_u/S` are exact, but local recursion does not itself furnish a stationary environment along the harmonic ray.

4. **One-type, Bethe, lumpable, and symmetric slices.** These reduce to ordinary Galton--Watson and are solved by classical dimension-drop theory. Generic source matrices do not lump.

5. **PF--KL identity.** Once an equivalent stationary ergodic harmonic-descendant environment exists, dimension drop reduces to a KL divergence. The identity does not construct that environment.

6. **Equality rigidity.** The zero-KL source equality case is the deterministic regular no-thinning model. Strictness outside that case is still conditional on stationarity/equivalence/integrability.

7. **Scalar Palm transfer operator.** Equations (2.1)--(2.2) are exact, but positivity and mass preservation alone do not prevent Cesaro mass from concentrating at conductance `b=0`.

8. **Pipe decomposition.** The `R_i=0` extinction-Jacobian channel is subcritical, so arbitrarily long sole-infinite-child pipes are not the main source of noncompactness. This does not control genuine branch points.

9. **Naive finite-state type chain.** A first tempting port says that regeneration should reset the tree using only the type. That statement is **false if one works directly with the harmonic child selected among siblings**: the selection probability contains a denominator `sum B_u`, so after integrating siblings the selected subtree is generally not merely `B(T)P_j(dT)/E_j B`. The sibling denominator is precisely the bias that produced (2.1). Thus a direct `type-only harmonic child chain` does not close the problem.

10. **Regeneration of the underlying walk instead of direct harmonic-child selection.** This is the new route refinement. At a *fresh-edge regeneration event* one first conditions on the actual random walk entering a previously unseen child and then never returning across that edge. Before the no-return conditioning, the forward subtree is fresh by the branching property; the no-return event depends only on that fresh subtree. This is the place where a type-indexed regeneration law may genuinely reset. The missing work is to turn that observation into the exact exit-ray stationary measure without accidentally reintroducing the sibling denominator.

The last item is a route, not a theorem claim. It is the strongest surviving handoff.

## 4. (c) What a successful proof must contain

The previous vague requirement "prove positive recurrence of `\mathcal L`" can now be replaced by a more concrete six-step programme. A complete proof must contain all of the following.

### C1. A source-matching regeneration event

Define a first fresh-edge regeneration for the simple random walk on a surviving multitype failed tree: the walk traverses an edge to a previously unseen child and thereafter never crosses that edge back toward the parent. The definition must be coupled to the same simple-random-walk/harmonic measure used in H0008, not to a different biased walk.

### C2. Exact reset law at a regeneration vertex

For every type `j`, identify the law `Q_j` of the forward subtree at a type-`j` regeneration vertex. The candidate Bayes form to verify is a type-specific no-return tilt of the original `P_j`. The proof must condition on the actual fresh-edge event, not on the already-integrated harmonic-child rule, so that sibling normalization is not silently imported into the reset law.

### C3. Finite-type regeneration kernel

From a regeneration root of type `i` with forward law `Q_i`, define

\[
K_{ij}=\mathbb P(\text{next regeneration vertex has type }j\mid\text{current regeneration type }i).
\tag{4.1}
\]

The branching/strong-Markov argument must show that, conditional on the next regeneration type `j`, the new forward subtree has exactly law `Q_j` and is independent of the pre-regeneration past. Only then are successive regeneration blocks Markov by the finite type state.

### C4. A finite-mean roof in *exit-ray levels*

Let `H` be the increase in exit-ray generation between successive regeneration vertices. One needs

\[
\max_i \mathbb E_{Q_i}H<\infty.
\tag{4.2}
\]

Physical walk time is not the relevant roof for Hausdorff dimension; the shift is by one boundary generation. This distinction may avoid trap-induced infinite physical holding times.

The candidate estimate to verify is based on the minimal annealed no-return probability over types. If

\[
b_i:=\mathbb E_{P_i}[B(T)]>0,
\qquad b_*:=\min_i b_i>0,
\tag{4.3}
\]

then each newly exposed edge, conditional on its child type and the past, has a fresh no-return chance at least `b_*` after averaging its independent forward subtree. The hoped-for consequence is a geometric domination for the maximum nested fresh depth before a successful regeneration. **This inequality has not been promoted to a theorem in this thinking-only run; the nesting/conditioning must be written without a hidden dependence error.**

### C5. Markov-renewal / Rokhlin suspension

If `K` is irreducible on the surviving types, let `pi` be its stationary distribution. The candidate invariant environment law for the one-level harmonic shift is then the occupation measure of a stationary regeneration block,

\[
\boxed{
\mu(A)
=
\frac{
\displaystyle\sum_i\pi_i\,
\mathbb E_{Q_i}\!\left[
\sum_{r=0}^{H-1}{\bf 1}\{\mathcal E_r\in A\}
\right]
}{
\displaystyle\sum_i\pi_i\,\mathbb E_{Q_i}H
},
}
\tag{4.4}
\]

where `\mathcal E_r` is the forward rooted environment at the `r`-th exit-ray level inside the regeneration block. Formula (4.4) is the exact object that the next proof attempt should verify by telescoping/Kakutani-tower invariance.

This is the main gain of the second recovery: **the stationary law should be constructed probabilistically first and only afterward identified as a fixed point of (2.1)**. Solving `\mathcal Lh=h` directly is no longer the preferred route.

### C6. Equivalence and PF--KL integrability

One must finally prove that `mu` is mutually absolutely continuous with the survival-conditioned source MGW law and that the logarithmic quantities entering the PF--KL identity are integrable. A potentially useful feature of the regeneration construction is that every block begins at a no-return-biased fresh subtree, so the block-start measure should already be positive on every surviving source tree. The occupation measure then contains the block-start term. This suggests a clean route to one direction of equivalence, but the exact density and the reverse absolute continuity still have to be checked.

A further useful observation for the eventual proof is that `x|log x|` is bounded on `(0,1]`; if the regeneration tilt really contains a factor comparable to the no-return probability, logarithmic conductance integrability at block starts may be much easier than under the original law. Again, this is a route note, not a claimed theorem.

## 5. (d) Simplest special case still unproved

The recovery keeps exactly the same non-lumpable two-type test case:

\[
\nu\equiv2,
\qquad q=(1/2,1/2),
\qquad
P=\begin{pmatrix}
3/4&3/4\\
1/2&1/4
\end{pmatrix}.
\tag{5.1}
\]

The type-weighted transmission row averages are unequal (`3/4` and `3/8`), so the one-block lumpability reduction is unavailable. The mean matrix is irreducible and supercritical; however, no claim about an explicit harmonic stationary density is made.

For this special case the next proof attempt should derive, in this order:

1. the two regeneration-reset laws `Q_1,Q_2`;
2. the `2 x 2` regeneration-type kernel `K`;
3. a bound for the two mean exit-level roofs `E_{Q_i}H`;
4. the tower law (4.4);
5. the induced density and a direct check that it satisfies (2.1).

If this cannot be done even for (5.1), the exact failure should be visible as either (i) the reset law retaining more than type information, (ii) an infinite mean roof, or (iii) failure of the tower projection to be equivalent to the source survival law.

## 6. (e) Nearest solved problem and the exact missing ingredient

The nearest solved problem remains Rousselin's one-type work.

- arXiv:1711.07920 constructs an absolutely continuous invariant **forward environment at exit times** for a transient random walk in random environment on a one-type Galton--Watson tree using regeneration times and ergodic theory.
- arXiv:1708.06965 / EJP 23 (2018), no. 46 constructs explicit invariant measures for a class of flow rules on marked one-type Galton--Watson trees and applies them to harmonic-measure dimensions.

The one-type proof has a reset feature that is automatic because every fresh descendant subtree has the same underlying Galton--Watson law. In the present problem, fresh subtrees are type-dependent. The missing ingredient is therefore not "regeneration exists" in the abstract; it is the finite-state **Markov-renewal bookkeeping of regeneration types together with an exit-level roof and the proof that the projected tower law is the stationary law for the harmonic descendant shift**.

Altok and Dembo--Sun show that useful stationary/reversing constructions are possible in finite-type Galton--Watson settings, but for different rerooting/walk kernels. They do not remove C1--C6 above.

## 7. The three actual Section-B moves

### #10 DERANDOMIZE

The previous formulation asked for an abstract invariant probability measure on an infinite-dimensional tree space or an abstract positive fixed point of `\mathcal L`. I replaced that existence slogan by the deterministic data of a regeneration scheme:

\[
(Q_i)_{i\in D},\qquad K=(K_{ij}),\qquad (\mathbb E_{Q_i}H)_{i\in D},\qquad \pi K=\pi,
\]

followed by the explicit occupation formula (4.4). This does not yet prove those objects satisfy all needed properties, but it turns "find an invariant measure" into a finite list of checkable identities/estimates.

Outcome: **route sharpened; metric unchanged; no theorem claim.**

### #13 FIND WHAT ONLY INCREASES

The monotone quantity is the number of newly exposed descendant edges / fresh depth since the last regeneration. Every time the walk first crosses a fresh edge there is another independent forward subtree behind it. If the type-wise annealed no-return probabilities admit a positive finite-type minimum `b_*`, then a run of nested fresh edges with no successful regeneration should pay a factor at most `1-b_*` per level. The exact conditional argument is the next proof obligation.

Outcome: the candidate positive-recurrence mechanism is now a **geometric fresh-depth tail**, not another spectral bound on `\mathcal L`.

### #24 FIND THE EXTREMAL OBJECT

The infinite tree is probably not the right extremal object. The handoff reduces the worst case to the **worst regeneration type**:

\[
b_* = \min_i \mathbb E_{P_i}B(T),
\qquad
h^* = \max_i \mathbb E_{Q_i}H.
\]

If the fresh-depth domination closes, finite type converts the entire recurrence problem into showing `b_*>0`; irreducible supercritical multitype survival/transience should be the literature input to check. If it does not close, the counterexample must exploit conditioning that defeats this worst-type reduction.

Outcome: a precise extremal test is identified; no bound is claimed as proved here.

## 8. Final recovery decision and handoff state

This is **STUCK-RECOVERY-2/2**. I choose the same permitted Section-I action as recovery 1, but now in its final form:

\[
\boxed{\textbf{PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.}}
\]

The port is no longer "generalize Rousselin somehow". It is the concrete C1--C6 Markov-renewal suspension above, with the two-type model (5.1) as the first test.

The H0008 handoff should preserve the following frontier:

- finite-type multifractal spectrum: already certified through the full closed exponent interval under the recorded source-reduction hypotheses, including zero-temperature endpoints;
- harmonic clause: source-open;
- PF--KL reduction and equality rigidity: preserved as PARTIAL progress;
- direct pressure-only route: certified insufficient;
- direct scalar transfer fixed-point route: exact but missing positive recurrence;
- sole-infinite-child pipes: already controlled through the subcritical extinction Jacobian;
- **best next route:** construct the stationary harmonic environment by fresh-edge regeneration, finite regeneration-type kernel, finite mean exit-level roof, and the tower occupation law (4.4), then derive `\mathcal Lh=h` as a consequence rather than as the starting point.

Because two stuck recoveries are now consumed, the **next R14 run must terminally hand off H0008 and rotate to an eligible ownership-clear HARD OUTSIDE target**. It must not do a third H0008 recovery even if this regeneration route looks promising. The unused H0008 Section-B triple that a future reassigned worker could try is exactly **#15 BREAK THE SYMMETRY, #19 MAKE IT AN ALGORITHM, #26 HUNT THE SPORADIC CASE**; every other numbered move has already been exercised on this target.

## 9. Model/scheduler capability statement

The currently exposed task-control interface still has fields for title/prompt, schedule or relative start, timing mode, enabled state, timezone/notification settings and run metadata. It exposes **no binding model-family selector and no reasoning-effort selector**, and it does not provide authenticated completed-run model telemetry. Therefore `GPT-6 / maximum` remains prompt text only and cannot be enforced from this surface. This run actually reports GPT-5.6 Sol with reasoning level UNVERIFIED.

An earlier task that returned `You cannot modify this task` represents an ownership/authorization-context boundary. The lawful workaround is the owning/admin-authorized context or platform support, not duplication or a permission bypass. No scheduler, permission, email, Drive, public-posting, purchase, or workflow state was changed in this run.

## 10. Structured ledger delta

```yaml
ledger_delta:
  worker: R14
  source: "Kumar 2026 arXiv:2608.15987v1, Section 12.3 open problem (6), Boundary fluctuations"
  canonical_claim: "operations/claims/H0008.md"
  target_status: "PARTIAL / SOURCE OPEN"
  metric: "I_mf = a_hi - a_lo"
  metric_before: "a_hi - a_lo (exact finite-type multifractal interval already certified)"
  metric_after: "same"
  movement: "NO MOVEMENT"
  unchanged_count: "UNKNOWN; policy stuck trigger already reached before recovery 1"
  stuck_recovery: "2/2 FINAL"
  thinking_only: true
  methods_used: [10, 13, 24]
  exact_blocker: "Construct an equivalent stationary ergodic harmonic-descendant environment, or equivalently a positive normalized fixed density for the conductance transfer operator, with PF-KL log-integrability; genuine branch-point channel R_i>0 remains the issue."
  best_route: "Fresh-edge regeneration -> type-indexed reset laws Q_i -> finite regeneration-type kernel K -> finite mean exit-level roof H -> Markov-renewal/Rokhlin occupation law -> equivalence/integrability -> transfer fixed point as corollary."
  simplest_unproved_test: "nu=2, q=(1/2,1/2), P=[[3/4,3/4],[1/2,1/4]]"
  remaining_obligation: "C1-C6 in this report; especially verify the reset law without a sibling-normalization error and prove a finite mean exit-level roof."
  next_action: "TERMINAL HANDOFF H0008 on next R14 invocation; rotate to lawful ownership-clear HARD OUTSIDE successor. No third H0008 recovery."
  prior_report_commit: "7740e422a0927ee19179c2b7794316a424d8f9d8"
  audits: "No source-level closure audits requested because H0008 remains PARTIAL/OPEN."
```
