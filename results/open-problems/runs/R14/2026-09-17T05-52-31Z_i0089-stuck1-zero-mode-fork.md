Model actually run: GPT-5.6 Sol. Reasoning level: UNVERIFIED — GPT-6 / maximum was requested, but this runtime exposes no authenticated model-family selector or reasoning-effort selector, so I do not claim otherwise. **NO FIXED-METRIC MOVEMENT: `S_1: 1 -> 1`; unchanged count `2 -> 3`; STUCK-RECOVERY-1. Methods tried: #1 CHANGE THE CATEGORY, #13 FIND WHAT ONLY INCREASES, #27 SWAP THE QUANTIFIERS.**

# R14 / I0089 — first stuck recovery: the missing zero mode

Status: **PARTIAL / source Conjecture 38 OPEN.** This is deliberately a thinking/stuck report. It makes **no new theorem-sized claim** and creates no checker merely to document stagnation.

## 0. Continuity and non-reopening rule

The original R14 negative-margin spherical-perceptron target was already handed off after both permitted hard-target recoveries. Its final supported bracket remains

\[
6.30297437506\le \alpha_c(-1)\le 12.78437096216,
\qquad \alpha_U-\alpha_L=6.48139658710.
\]

This run does **not** reopen that target. The canonical R14 successor remains I0089, Mathieu Lewin, *Coulomb and Riesz gases: The known and the unknown*, J. Math. Phys. 63 (2022), arXiv:2202.09240, Conjecture 38.

The frozen successor metric is

\[
S_1=\inf\{s_0\ge 1:\ \forall s>s_0\text{ and admissible }\mu>0,\text{ every }d=1\text{ short-range equilibrium configuration is a scaled translate of }\mathbb Z\}.
\]

R14-C190 already put `S_1=1`. R14-C191 then proved on the page the structural long-range statement `X=a Z+tau` for `d=1, 0<s<1`; R14-C192 proved existence of at least one Theorem-28 thermodynamic extraction at the correct long-range scale `a=rho_b^{-1}`. Those remain self-check/on-page results with `0/2` external audits. The fixed metric was already saturated, so the latest two successor runs were unchanged; this run is the third and therefore triggers Section I.

Repository continuity checked this invocation: campaign INDEX/RANKING, POSTED, RESULTS, QUEUE, NEW_METHODS policy, the I0089 claim, newest own R14 report, and the latest neighboring R15 handoff were read. The large intake JSONL remains access-limited through the connector, so I used the targeted I0089 intake record rather than pretending to have rendered every row.

## 1. Current primary-source check

Primary source rechecked against arXiv:2202.09240v2.

Theorem 28 starts from **any finite-volume grand-canonical minimizer** at fixed background `rho_b>0` and, after a subsequence plus translation/relabeling, constructs an infinite configuration and a locally convergent renormalized potential. In `d=1, 0<s<1`, the source's simpler move-function representation (83) applies. The theorem gives the finite-replacement equilibrium inequality (82).

The source itself identifies the exact missing density issue in the proof of Theorem 28: it says that it cannot prove absence of large holes and only proves that **almost all** recentering points have local density close to `rho_b` in an averaged sense, whereas the expected statement is equidistribution around any point.

Immediately before Conjecture 38, the source says that for `s<d` one can introduce an equilibrium-configuration definition using Theorem 28 with `mu in R` and `rho_b>0`, and then conjectures that all such configurations have scale `r=rho_b^{-1/d}`. In `d=1` this is exactly the scale obligation `a=rho_b^{-1}`.

Fresh dated literature checks through 2026-09-17 found no primary source closing this exact all-equilibrium-configuration statement. The closest 2026 one-dimensional results I found remain periodic/screened: De Luca--Goldman--Ponsiglione, *Dynamics of screened particles towards equi-spaced ground states* (Adv. Calc. Var. 19 (2026), 399--422), and De Luca--Pini--Ponsiglione--Santilli, arXiv:2607.29663, *Periodic ground states for a one-parameter family of nonlocal energies on the real line* (submitted 2026-07-31). Both build neutrality/periodicity into the setup. This is bounded negative evidence only, not a novelty certificate.

## 2. Required stuck item (a): exact blocker

After C191, the long-range `d=1` source obligation has collapsed to the following zero-mode statement:

\[
\boxed{
X=a\mathbb Z+\tau\text{ arises as a source-admissible Theorem-28 equilibrium at background }\rho_b
\quad\Longrightarrow\quad
a^{-1}=\rho_b.
}
\tag{BLOCK-I0089}
\]

Equivalently, for every admissible thermodynamic recentering one needs

\[
\lim_{R\to\infty}\frac{\#(X\cap[-R,R])}{2R}=\rho_b.
\]

C192 proves this for a specially chosen countably-good extraction. It does not prove it for every admissible extraction/equilibrium configuration.

## 3. Required stuck item (b): routes tried and the precise failure of each

### Route A — local DLR / finite replacement

This route produced X44. Once the renormalized potential `Phi` is fixed, the explicit `rho_b` terms in the local finite-replacement functional (82) cancel. Therefore the local DLR algebra sees the configuration and the potential, but not the background zero mode. Replaying (82) cannot determine `a^{-1}-rho_b`.

**Failure:** the scale is a global charge/density datum erased by local finite differences.

### Route B — countably-good thermodynamic centers

Theorem-28 Step 1 gives an averaged discrepancy estimate for most centers. C192 diagonalized over a sequence of tolerances and obtained one extraction with the correct density. 

**Failure:** `there exists a good center/extraction` is not `every admissible center/extraction`. A sparse set of bad recentering sequences is not excluded by an averaged estimate.

### Route C — direct analytic continuation of the periodic lattice

Source Lemma 29 shows that the pole residue of a periodic/discrepancy-controlled configuration records its density; Lemma 31 gives the periodic analytic-continuation potential. Once C191 says `X=aZ+tau`, its canonical periodic potential therefore knows the density `1/a`.

**Failure:** Theorem 28 does not identify its hard-wall thermodynamic-limit potential with the canonical periodic/background potential at the prescribed `rho_b` in a way that controls the zero Fourier mode. The source itself says that different background growth can change the potential by a constant and that the equivalence for minimizers is not generally proved. Potential differences/forces are insufficient because constants are precisely where the zero mode hides.

### Route D — global net-charge penalty

Source Lemma 48 gives, at `d=1`, `0<s<1`, `beta=infinity`, a finite-volume missing-charge penalty of order

\[
\frac{Q^2}{N^s}.
\]

Thus a **global** density error `Q\asymp delta N` costs order `N^{2-s}`, superlinear because `2-s>1`. Lemma 49/Corollary 50 supply the complementary net-charge control. This is exactly the right convexity scale.

**Failure:** those estimates are for the entire finite box. A wrong-density *local* window is coupled to the exterior through a long-range field; naively applying the global charge estimate to an embedded subinterval double-counts the exterior compensation. No current argument converts the global `Q^2/N^s` cost into a uniform-in-center mesoscopic local charge bound.

### Route E — source periodic ground-state theorems / later periodic papers

The source proves one-dimensional lattice optimality for the energy problem (Theorem 36) and the 2026 papers prove equispacing in periodic screened models.

**Failure:** those problems impose a global period/neutrality condition. I0089 asks for every infinite source equilibrium configuration produced/allowed by the hard-wall thermodynamic setup. The missing step is deriving neutrality rather than assuming it.

## 4. Method #1 — CHANGE THE CATEGORY: from DLR to a fractional Poisson zero mode

For `d=1, 0<s<1`, set

\[
\alpha=\frac{1-s}{2}\in(0,1/2).
\]

Formally the finite-volume Theorem-28 potential satisfies a fractional Poisson equation

\[
(-\Delta)^\alpha\Phi_\ell
= c_s\left(\sum_j\delta_{x_{j,\ell}}-\rho_b\mathbf 1_{\Omega_\ell}\right),
\]

because `|x|^{-s}` is the Riesz kernel whose Fourier multiplier is proportional to `|xi|^{s-1}`.

This language retains exactly the datum lost by DLR. If one could pass this identity through the thermodynamic recentering and then use C191 (`Phi` is periodic up to an additive constant once `X=aZ+tau`), the zero Fourier mode would force

\[
1/a-\rho_b=0.
\]

A useful quantitative version is to test against a cutoff `chi_R(x)=chi(x/R)`. The fractional Laplacian scales like

\[
\|(-\Delta)^\alpha\chi_R\|_{L^1}\asymp R^{1-2\alpha}=R^s,
\]

whereas a nonzero mean charge produces an `O(R)` left side. Since `s<1`, an `O(R^s)` right-side bound would rule out an `O(R)` density mismatch.

**What happened:** this is the strongest new route of the run. It isolates the missing datum as a zero-frequency conservation law and explains why the force/move-function proof cannot see it. I am **not** claiming the passage to the limit: `(-Delta)^alpha` is nonlocal, while Theorem 28 gives local `L^1` convergence of `Phi_ell`; controlling the tail pairing is exactly the unresolved technical step.

## 5. Method #13 — FIND WHAT ONLY INCREASES: net-charge energy as the candidate monovariant

At `d=1`, the source's Lemma 48 penalty has the scaling

\[
Q^2/N^s.
\]

For a macroscopic density defect `Q\asymp \delta N`, this becomes `c delta^2 N^{2-s}`, which dominates the `O(N)` bulk/chemical-potential scale for every `0<s<1`.

**What happened:** this strongly suggests that persistent wrong-density regions cannot occupy a macroscopic fraction of a minimizing box and explains the source's almost-everywhere Step-1 estimate. But it does not yet control a rare recentering whose anomalous window grows submacroscopically. The missing monotonicity/localization statement is: a mesoscopic charged interval should retain a definite fraction of this superlinear penalty after optimizing the exterior. No such source-valid inequality has been established here.

## 6. Method #27 — SWAP THE QUANTIFIERS: expose the exact logical gap

The source obtains, schematically,

\[
\text{for most }\tau,\quad \text{local averaged discrepancy at }\tau\text{ is small}.
\]

Conjecture 38 needs, after C191,

\[
\text{for every admissible recentering sequence }\tau_\ell,\quad a(\tau_\ell)^{-1}=\rho_b.
\]

Those quantifiers are not interchangeable. A set of bad centers whose relative measure tends to zero can still contain one center at every volume and hence generate a subsequential local limit.

**What happened:** this confirms that improving the existing average estimate by constants cannot close the problem. The proof must either (i) obtain a genuinely uniform discrepancy estimate, or (ii) show that bad centers cannot be nested into a valid thermodynamic recentering, or (iii) recover the zero mode from the limiting potential as in Method #1.

## 7. Required stuck item (c): what a successful proof must contain that all previous routes lack

A proof now needs **one global zero-mode principle that survives recentering**. Any one of the following would be sufficient:

1. a justified thermodynamic-limit fractional Poisson identity for `Phi`, with enough tail control to test approximate constants;
2. a uniform-in-center mesoscopic charge inequality converting the finite-box `Q^2/N^s` penalty into local discrepancy control;
3. a theorem that the Theorem-28 hard-wall potential for a periodic limiting configuration equals the canonical periodic/background potential with the **prescribed** `rho_b`, not merely up to the background-blind local DLR relation.

No previous R14 route contains this zero-frequency information.

## 8. Required stuck item (d): simplest still-unproved special case

Do not attack arbitrary configurations anymore. C191 already removed that complexity. The simplest remaining statement is exactly:

\[
\boxed{
0<s<1,\quad X=a\mathbb Z+\tau\text{ is an actual Theorem-28 thermodynamic limit at background }\rho_b
\quad\Longrightarrow\quad a=\rho_b^{-1}.
}
\]

This is the first special case a future proof should close.

There is also a useful **refutation test**: distinguish carefully whether the source's phrase “introduce a similar definition using Theorem 28” means (A) actual hard-wall thermodynamic limits, or only (B) abstract pairs `(X,Phi)` satisfying the separation/potential/DLR properties. Under interpretation (B), X44 makes the prescribed `rho_b` suspiciously invisible and a wrong-density periodic lattice may become a counterexample after finite-replacement stability is checked. Under interpretation (A), the missing theorem is the zero-mode passage above. This semantic fork must be resolved before publication claims.

## 9. Required stuck item (e): nearest solved problem and the missing ingredient

The nearest solved models are the **periodic screened** one-dimensional problems:

- De Luca--Goldman--Ponsiglione (2026), *Dynamics of screened particles towards equi-spaced ground states*;
- De Luca--Pini--Ponsiglione--Santilli, arXiv:2607.29663 (2026), *Periodic ground states for a one-parameter family of nonlocal energies on the real line*.

They prove equispacing in settings where the screened charge has zero average / periodic neutrality is built into the state space. Lewin's own periodic construction likewise says neutrality is automatically imposed in the periodic model.

**What those solved problems have that I0089 lacks:** an explicit global zero-mode constraint. The hard-wall Theorem-28 recentering only gives a local limit plus averaged control for most centers; it does not hand us neutrality for every recentering.

## 10. Recovery choice — exactly one

**Chosen recovery: PORT THE TECHNIQUE FROM THE NEAREST SOLVED PROBLEM.**

The next attack should port periodic neutrality into the hard-wall thermodynamic limit through the fractional Poisson formulation, rather than derive another local DLR lemma. Concretely:

1. write the exact finite-volume fractional Poisson identity for `Phi_ell`;
2. choose a scaled cutoff whose fractional Laplacian has `L^1=O(R^s)`;
3. prove the tail pairing is uniform along the Theorem-28 minimizing sequence using the source's global net-charge bounds and potential lower/local-upper estimates;
4. pass `ell -> infinity` first at fixed `R`, then `R -> infinity`;
5. insert C191 periodicity to conclude the charge average is zero and hence `a^{-1}=rho_b`.

This is hard-target recovery `1/2` for the successor I0089. If it fails without changing the frozen metric/remaining obligation, one final stuck recovery is allowed; a later third stuck episode must hand off/rotate.

## 11. Next section-B moves

The next invocation, if it remains on I0089, should not repeat #1/#13/#27. The planned triple is:

- **#7 TAKE THE LIMIT** — make the two-scale `ell -> infinity`, then `R -> infinity` fractional-test argument source-valid;
- **#12 FIND WHAT IS CONSERVED** — identify the total zero Fourier mode / neutral charge as the invariant carried by finite minimizers;
- **#29 ADD THE POINTS AT INFINITY** — compactify the one-dimensional line to separate the constant mode from the periodic oscillatory potential and control boundary charge explicitly.

## 12. Neighbor / ownership / exclusions

The newest visible R15 I0076 report is already a six-run handoff/rotation report; it leaves Burdzy--Scheutzow Problem 7.2 OPEN/PARTIAL and does not supply a closure package needing a new R14 audit. I therefore did not invent an audit verdict.

POSTED/INDEX exclusions were respected. I0089 remains owned by R14. No peer files, shared roots, email, Drive, public posting, purchases, permission changes, workflow execution, or scheduler state were modified.

## 13. Model / scheduler boundary

The exposed task interface still has prompt/title/schedule/enablement/timing controls but no model-family selector, no reasoning-effort selector, and no authenticated completed-run model telemetry. GPT-6 / maximum remains prompt text only here. The current repository ledger also records that P26 was eventually editable from an authorized P/C context while all R-series edits were denied in that context; therefore `You cannot modify this task` is an ownership/context issue, not evidence that the prompt itself is malformed. The legitimate workaround is the authorized owning account/workspace surface or platform support, never task duplication or permission bypass.

## ledger_delta

```yaml
track: R14
target: I0089 / Lewin Conjecture 38
source_status: OPEN
status: PARTIAL
fixed_metric: S_1
before: 1
after: 1
movement: false
unchanged_count_before: 2
unchanged_count_after: 3
stuck_recovery: 1/2
new_theorem_claims: none
methods_tried: [1, 13, 27]
recovery_choice: port_technique_from_nearest_solved_problem
exact_blocker: "For an actual d=1, 0<s<1 Theorem-28 thermodynamic limit X=aZ+tau at background rho_b, prove a^{-1}=rho_b."
next_methods: [7, 12, 29]
perceptron_reopened: false
external_audits_C190_C191_C192: 0/2
```
