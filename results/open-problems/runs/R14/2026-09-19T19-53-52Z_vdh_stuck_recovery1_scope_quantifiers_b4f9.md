Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise. NO MOVEMENT in the frozen metric `lim Delta_dual,n`: `0 -> 0`; this is mandatory STUCK-RECOVERY-1/2, THINKING-ONLY. Methods actually used: B3 PROVE SOMETHING STRONGER, B12 FIND WHAT IS CONSERVED, B27 SWAP THE QUANTIFIERS.**

# R14 bounded research iteration — VDH-8.3-DUALITY STUCK-RECOVERY-1: separate quenched duality from deterministic-profile replacement

Repository / branch: private `yspennstate/math-open-problems` / `master`.

Status: **PARTIAL / source OPEN / STUCK-RECOVERY-1/2 / THINKING-ONLY**.

## 1. Continuity and ownership

I resumed the current canonical R14 assignment `VDH-8.3-DUALITY`; I did **not** reopen the stale scheduler-title negative-margin perceptron, H0008, or P0157. The canonical claim `operations/claims/VDH-8.3-DUALITY.md` still lists R14 as exclusive owner after the HARD7-04 handoff.

Before route selection I reread/recovered the controlling campaign surfaces `probability_campaign_2026_09/INDEX.md`, `probability_campaign_2026_09/RANKING.md`, root `POSTED.md`, root `RESULTS.md`, `QUEUE.md`, `operations/NEW_METHODS_2026-09-16.md`, the canonical claim, the newest R14 VDH report `runs/R14/2026-09-19T18-53-58Z_vdh_truncated_susceptibility_duality_v2d7.md`, and the principal HARD7-04 VDH handoff/recovery reports including the collared lower-bound and quantitative-histogram checkpoints. I used indexed intake/source searches for the large `probability_1000_intake_*/problems.jsonl` collections rather than pretending a connector preview was a literal full-file dump.

The newest R14 checkpoint records `closure: false` and the remaining obligation as source-scope reconciliation: the random-residual-sequence quenched duality plus sharp `C_2` proof candidate may already match the source's intended question; only a stronger interpretation would require point-process/profile-replacement stability. That same report records that this VDH assignment had already accumulated two consecutive R14 `0 -> 0` metric runs. Hence this third unchanged run is, by Section I, a thinking-only stuck recovery. I do not manufacture another lemma, checker, or certificate here.

## 2. Source and current-status refresh

Primary source: Remco van der Hofstad, *Stochastic processes on random graphs*, preliminary monograph dated **4 August 2026**, Notes on Section 8.3, printed p. 245 / PDF p. 255:

`https://rhofstad.win.tue.nl/Saint_Flour_SPoRG_Grundlehre.pdf`

The source still says that the 2019 barely-supercritical configuration-model work does not investigate the second-largest component in the supercritical regime, notes that the high-degree vertices should lie in the unique giant, and asks:

> “Does the discrete duality principle still hold?”

A bounded current-literature refresh on 19 September 2026 again found no paper closing this exact shrinking-window deterministic-degree CM question. The closest structural references remain:

- van der Hofstad–Janson–Łuczak (2019), barely-supercritical giant/component structure;
- Coulson–Perarnau (EJP 2023), sharp subcritical CM upper-bound technology under additional hypotheses, with tightness for certain sequences rather than a general duality theorem;
- Janson–Riordan (2010/2011), a genuine full duality theorem for independent-edge inhomogeneous random graphs, but not for the fixed-degree pairing model.

This is bounded negative evidence only, not a worldwide novelty certificate.

## 3. Frozen metric and trigger

The inherited source-relevant admission metric is

\[
\Delta_{\rm dual,n}
=\left|\frac{1-\nu_n^{\rm dual}}{\varepsilon_n}-1\right|.
\]

HARD7-04 already reached the supported floor

\[
\Delta_{\rm dual,n}\to0.
\]

Therefore this run honestly records

`lim Delta_dual,n: 0 -> 0` — **NO MOVEMENT**.

This is R14's third consecutive unchanged VDH metric run and therefore **STUCK-RECOVERY-1/2**. The Section-I action selected below is **prove the simplest unproved special case**, but that proof is deferred to the next proof-capable invocation; this report is thinking-only.

---

# Section-I stuck report

## 4(a). Exact blocking statement

For the **narrow source interpretation**—the second-largest-component scale after giant deletion—the repository already contains a complete-looking proof candidate, conditional on the stated earlier reductions:

\[
|C_{2,n}|=(1+o_p(1))\frac{2R_*}{\varepsilon_n^2}
\log(n\varepsilon_n^3),
\]

together with literal quenched pairing-law duality of the complement: conditional on its realized residual degree sequence, deleting the unique giant leaves asymptotically the law of a fresh configuration model on that realized degree sequence.

Thus the only mathematical blocker that remains **if one reads “duality principle” more strongly than the leading `C_2` asymptotic** is to define and prove an ideal-dual observable-level comparison that legitimately replaces the random residual degree profile by a canonical extinction-tilted proxy. A safe formulation is:

\[
\boxed{
\text{Find a canonical ideal dual law }\mathsf D_n
\text{ and a source-meaningful observable class }\mathcal F_n
\text{ such that }
\sup_{F\in\mathcal F_n}
\left|
\mathbb E F(G_n[V\setminus C_{1,n}])
-
\mathbb E_{\mathsf D_n}F
\right|\to0.
}
\tag{4.1}
\]

Here `F` should at least see the extreme residual components if this is to strengthen the existing `C_2` theorem candidate.

A crucial route correction is that **whole-graph total variation against a fixed deterministic rounded extinction-tilted degree sequence is not the right target**. The degree sequence itself is a graph-measurable observable. Two configuration-model laws supported on different deterministic degree multisets are mutually singular as measures on labelled graphs. Hence full graph-TV can tend to zero only if the degree profiles agree with probability tending to one, which the natural residual fluctuations do not provide. This is a diagnosis of an over-strong target, not a new theorem about the source problem.

## 4(b). Routes tried and the precise reason each does or does not reach (4.1)

### Route 1 — reflected branching-process parameter

Succeeded:

\[
1-\nu_n^{\rm dual}=\varepsilon_n(1+o(1)).
\]

**Why insufficient for strong duality:** it controls the one-particle exploration drift, not the joint law of rare extreme components.

### Route 2 — exact post-giant stopping/remainder reduction

Succeeded in turning the complement after a lawful completed-component stopping boundary into an exact configuration model on a random residual sequence.

**Why insufficient alone:** it transfers every remaining component-law question to that random sequence rather than replacing the sequence by a canonical ideal dual law.

### Route 3 — Cramér collar and sharp upper bound

Succeeded in giving the correct leading upper scale for the post-giant largest residual component.

**Why insufficient:** one-root/exponential-tail control is one-sided and does not identify a full residual component process.

### Route 4 — bounded-support tree census

Succeeded for a concrete bounded three-point law.

**Why insufficient originally:** fixed support hides triangular-array tails and small degree-class multiplicities. The later collared deterministic theorem repairs this for the leading largest-component scale, but not for an entire point process.

### Route 5 — collared deterministic lower theorem + source `C_2` proof candidate

Succeeded at the leading source-size obligation. The global coefficient saddle, lattice smoothing, and two-color second moment give the matching lower leading constant on a deterministic high-probability class inherited from giant deletion.

**Why it does not automatically imply (4.1):** a leading `L_1` asymptotic is much weaker than stability of all large components or any whole-graph law.

### Route 6 — simultaneous weighted extinction-tilted degree histogram

Succeeded:

\[
\sum_d(1+d)|N^{out}_{n,d}-n_d\xi_n^d|
=o_p(n\varepsilon_n).
\]

**Why insufficient for a strong distributional replacement:** weighted `ell^1` proximity of profiles does not by itself imply continuity of extreme component statistics at the `\varepsilon_n^{-2}\log(n\varepsilon_n^3)` scale.

### Route 7 — exact fixed-set conditional pairing identity + giant-scale susceptibility bound

Succeeded at the strongest literal pairing statement obtained so far. Given a candidate giant set, the complement pairing is uniform; the only extra bias from requiring it to be the unique largest set is conditioning a fresh residual CM to have `L_1<|S|`. The R14 truncated-susceptibility theorem makes that conditioning asymptotically negligible. Thus the actual complement is asymptotically a **fresh CM on its realized random residual degree sequence**.

**Why insufficient for the strongest reading of (4.1):** the residual degree sequence is still random and correlated with the original giant-deletion exploration.

### Route 8 — deterministic-profile global total variation

**Fails as a target, not just as a proof technique.** The labelled degree multiset is observable, so laws with different deterministic degree sequences live on disjoint profile events. Attempting to prove graph-level TV to one deterministic rounded proxy asks for more than the model can naturally supply.

### Route 9 — extreme-component point-process/profile replacement

This is the surviving stronger route.

**Why still open here:** no completed argument upgrades the weighted profile estimate to a stable limit law for the whole collection of extreme subcritical components under the residual-profile fluctuations allowed by the source.

## 4(c). What a stronger proof must contain that the completed routes do not

If the source is interpreted as asking for more than the already obtained leading `C_2` asymptotic plus quenched fresh-pairing law, a proof must add all of the following:

1. a **canonical randomized ideal dual profile**, rather than a single deterministic graph-TV proxy;
2. a topology or observable class that is insensitive to unavoidable degree-profile fluctuations but still sees the extreme components;
3. stability of the extreme-component law under random perturbations of the residual degree histogram at the source's natural scale;
4. preservation of the reflected drift, `R_*`, parity/lattice structure, and the exponential collar on the same high-probability event;
5. a multicomponent local-limit/second-moment or Poisson-point-process mechanism, not merely the one-largest-component coefficient saddle;
6. conditionalization on the random post-giant sequence without losing uniformity.

The present repository work contains the ingredients for item 4 and the one-component version of item 5, but not the multicomponent stability theorem.

## 4(d). Simplest useful special case still unproved

Take a **fixed bounded degree support** satisfying the source's critical limiting assumptions, and construct an ideal randomized extinction-thinned profile by independent classwise thinning

\[
\widehat N_{n,d}\sim\operatorname{Bin}(n_d,\xi_n^d),
\]

with the unavoidable even-half-edge conditioning, then sample a fresh configuration model on that randomized profile.

The first useful stronger target is not whole-graph TV. It is a fixed-threshold extreme-component comparison. For fixed `a>0`, let `\mathcal P_n^{(a)}` record the normalized sizes (and, if needed, degree masses) of all residual components above the threshold

\[
a\varepsilon_n^{-2}.
\]

Prove that a bounded-support version of the actual post-giant complement and the independently extinction-thinned ideal dual have asymptotically the same Laplace functionals for `\mathcal P_n^{(a)}`. This special case removes the triangular-array high-degree problem, keeps the genuinely new dependence/profile-replacement issue, and is strictly stronger than the already obtained leading `C_2` scale.

This is the **single Section-I action selected**: on the next proof-capable run, **prove the simplest unproved special case above**. No claim that it is true is made in this thinking report.

## 4(e). Nearest solved problem and the ingredient it has that this problem lacks

The nearest genuine “full duality” theorem is Janson–Riordan's duality for very general **independent-edge inhomogeneous random graphs**. There, deleting the giant leaves (after the appropriate parameter transformation) another graph in essentially the same independent-edge family.

The ingredient the configuration model lacks is exactly **edge independence after the macroscopic deletion**. Degree constraints transmit global dependence through the random residual degree profile. R14 has now shown that the *pairing conditional on that profile* is asymptotically fresh; the unsolved stronger step is therefore not pairing dependence but replacing the random profile by an ideal randomized extinction-thinned proxy for extreme-component observables.

For the narrower size-only problem, the nearest solved machinery is instead Riordan's bounded-degree barely-subcritical CM theorem / the bounded-support mechanism cited by Coulson–Perarnau. The R14/HARD7 collared coefficient-saddle route is already designed to port that size mechanism to the source profile.

---

## 5. The three route-finding moves used in this thinking run

### B3 — PROVE SOMETHING STRONGER

I stress-tested the strongest natural interpretation: full graph-level TV after replacing the random residual profile by a deterministic extinction-tilted sequence. That formulation is structurally over-strong because the degree profile is observable. The useful strengthening must therefore live at the level of randomized ideal profiles and extreme-component observables, not deterministic whole-graph TV.

**Outcome:** productive failure of the naive strongest target; it sharply identifies the right state space.

### B12 — FIND WHAT IS CONSERVED

The conserved/sufficient state under giant deletion is the **realized residual degree multiset**. Conditional on it, the pairing law is uniform; after the R14 susceptibility estimate, even the unique-largest conditioning vanishes asymptotically. Thus the only remaining strong-duality information is in the law of the residual profile and the stability of extreme observables under perturbing it.

**Outcome:** the pairing-law problem is separated from the profile-replacement problem.

### B27 — SWAP THE QUANTIFIERS

For the concrete `C_2` source statement, do not prove one universal continuity theorem for all profile perturbations. Instead prove a deterministic subcritical theorem **uniformly for every degree sequence in a high-probability good class**, then show the random post-giant sequence lies in that class. HARD7-04's collared deterministic lower theorem already implements this quantifier swap for the leading largest-component scale.

**Outcome:** strong evidence that the narrow source-size obligation is already mathematically reduced to audit/source-interpretation, while only a broader point-process reading remains mathematically unproved.

## 6. Next route

This run consumes **STUCK-RECOVERY-1/2** on `VDH-8.3-DUALITY`.

Selected Section-I action: **prove the simplest unproved special case** in §4(d) on the next proof-capable invocation.

Fresh next method triple, chosen to avoid every indexed VDH move already used by HARD7-04 or R14:

- **B7 TAKE THE LIMIT** — formulate the extreme-component point-process/Laplace-functional target first and derive the finite-`n` obligations from it;
- **B15 BREAK THE SYMMETRY ON PURPOSE** — expose one candidate extreme component and then the remainder sequentially instead of demanding simultaneous exchangeable profile replacement;
- **B26 HUNT THE SPORADIC CASE** — track parity/lattice residues and degree-class sparsity explicitly so that the randomized ideal profile does not silently erase the exceptional subsequences that could break convergence.

If a subsequent three-run stagnation triggers a second stuck episode, only one more recovery is permitted. A third stuck episode on VDH must terminally hand it off and rotate.

## 7. Capability / scheduler-control honesty

The exposed scheduler surface still provides task identity/title/prompt, schedule/timing mode, enabled state, and update fields. It exposes **no binding model-family selector and no reasoning-effort selector**. Therefore `GPT-6 / maximum` remains prompt text only; this run actually identifies as GPT-5.6 Sol and exposes no reasoning-effort telemetry, hence `UNVERIFIED`.

Changing this requires an authorized product/workspace/API/admin execution surface that actually exposes and persists model/reasoning controls; no repository edit can create them. Historical `You cannot modify this task` responses such as the P26 case are authorization-context restrictions. The compliant workaround is the owning/admin-authorized context or platform support, never a permission bypass and never a duplicate schedule.

No scheduler, permission, workflow, email, Drive, public-posting, or peer-file change was made.

## 8. Structured ledger delta

```yaml
ledger_delta:
  source: VDH-8.3-DUALITY
  metric: "Delta_dual,n = |(1-nu_dual,n)/epsilon_n - 1|"
  before: "0 (supported floor, inherited)"
  after: "0"
  movement: "NO MOVEMENT"
  r14_vdh_consecutive_unchanged_runs: 3
  status: "PARTIAL / SOURCE OPEN / STUCK-RECOVERY-1/2 / THINKING-ONLY"
  tried_moves: [3, 12, 27]
  selected_section_I_action: "prove the simplest unproved special case"
  remaining_obligation: "If source means only leading C2 plus quenched fresh pairing, reconcile scope and obtain two independent other-track audits. If a stronger duality interpretation is required, prove randomized-profile extreme-component stability; deterministic-profile whole-graph TV is not the right target."
  next_moves: [7, 15, 26]
  independent_audits: []
  closure: false
```
