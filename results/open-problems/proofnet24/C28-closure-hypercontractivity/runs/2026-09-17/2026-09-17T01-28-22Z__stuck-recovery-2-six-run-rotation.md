Model actually running: GPT-5.6 Sol. Reasoning level: UNVERIFIED; this was not GPT-6 at maximum, and I do not claim otherwise. **NO MOVEMENT — frozen I0032 comparison factor remains `2 -> 2`; unchanged-run count `5 -> 6`; this is STUCK RECOVERY 2 / THINKING-ONLY and the required six-run CLOSABLE rotation/handoff. Section-B moves: 9, 10, 13. No new C28 theorem claim.**

# C28 — STUCK RECOVERY 2 and six-run rotation handoff for Aldous–Fill Open Problem 8.23

Repository / branch: `yspennstate/math-open-problems` / `master`.
Own root: `proofnet24/C28-closure-hypercontractivity`.
Run date: 2026-09-17.
Allocation/status entering run: CLOSABLE OUTSIDE, `I0032` **CLAIMED / PENDING_ADMISSION / NOT READY**.
Delivery: private GitHub only. No email/Gmail, Drive, public posting, paid compute, access change, peer-file edit, shared-ledger edit, or new schedule.

## 1. Continuity, source, ownership, and reserve

I continued from the newest durable C28 report

`proofnet24/C28-closure-hypercontractivity/runs/2026-09-17/2026-09-17T00-24-51Z__three-state-matched-hitting-refutation.md`

rather than restarting. At run start I reread or exact-searched the campaign `probability_campaign_2026_09/INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, canonical `operations/claims/I0032.md`, the own C28 report chain and dependencies, the newest C29 report, and current queue/claim evidence. The large intake/attempt JSONL mirrors cannot be rendered row-for-row through the connector before truncation; I therefore used exact-ID/source-phrase searches and do not represent this as a fictitious byte-for-byte visible reread of every approximately 780-row intake file.

The canonical I0032 reservation remains **Owner C28 / CLAIMED / PENDING_ADMISSION — NOT READY**. The source was rechecked against the live Aldous–Fill Chapter 8 page. For a finite irreducible reversible continuous-time chain, with

\[
N(s)=\|P_s\|_{2\to\infty},
\]

Open Problem 8.23 asks to characterize in terms of the Dirichlet form `E` the value `s*` for which `N(s)=2` ("say"). The subsequent finite-`q` hypercontractive times `s_q` are distinct. The total-domain convention retained throughout C28 is

\[
s_*:=\inf\{s\ge0:N(s)\le2\}.
\]

The already-proved source bridge remains

\[
s_*=\tau_2(\sqrt3),
\]

because reversibility gives `N(t)^2=1+max_x d_{2,x}(t)^2`.

The old Paley-ETF conditioning project remains untouched in **HARD RESERVE**. Preserve exactly the certified `(p,m)=(73,14)` witness

\[
\kappa_*=6.6575355565204281495\ldots,
\]

strict two-swap local maximality over all `161070` exchange-radius-two neighbors, the common-neighbor upper bound `6.603863488301192967...`, every exact certificate and failed route, and the quantifier correction: **one badly conditioned finite submatrix does not refute an existential assertion that some asymptotic family is uniformly well conditioned.**

## 2. Frozen metric and protocol accounting

The frozen full-source candidate is still the binary state-anchored dyadic local-spectral functional

\[
S_{\rm anch,2}(\mathcal E)
=
\inf\{t\ge0:\max_x D_x(t)\le3\},
\]

where the positive spectrum is partitioned into fixed binary bands `[2^k gamma,2^{k+1} gamma)` and

\[
D_x(t)=\sum_k e^{-2t2^k\gamma}\|\Pi_k r_x\|_2^2.
\]

C28 already proved on the complete source class

\[
s_*\le S_{\rm anch,2}(\mathcal E)\le2s_*,
\]

and then proved the sharpness identity

\[
\boxed{
\sup_{\substack{\text{finite irreducible reversible CT chains}\\s_*>0}}
\frac{S_{\rm anch,2}(\mathcal E)}{s_*}=2.
}
\tag{2.1}
\]

Thus the frozen metric is mathematically saturated, not merely computationally stagnant. It remains

\[
\boxed{2\longrightarrow2}.
\]

The preceding run was the fifth consecutive no-movement run. Under the owner protocol, this invocation is therefore **STUCK RECOVERY 2 / THINKING-ONLY**. Because it is also the sixth consecutive unchanged CLOSABLE run, no seventh same-target C28 research run is permitted. This report is the mandatory handoff/rotation record.

The previous report suggested B1/B11/B22. Recovered move history shows B11 was already used in the admission run and B22 in the Kozma/resolvent line, so I did not repeat that assigned triple. Repository searches found no prior C28 use of B9, B10, or B13; these are the replacement thinking moves used here.

## 3. Exact statement that blocks

For the **frozen metric**, movement would require a statement contradicted by the already-proved sharpness theorem:

\[
\boxed{
\exists C<2\quad
S_{\rm anch,2}(\mathcal E)\le C s_*
\quad\text{for every finite irreducible reversible chain.}
}
\tag{BLOCK-FROZEN}
\]

Equation (2.1) proves `(BLOCK-FROZEN)` false. Consequently, no honest continuation can improve the frozen numerical factor without changing the frozen characterization itself.

For the **source-level research question**, the remaining obstruction is qualitatively different:

\[
\boxed{
\text{find a non-tautological, comparison-stable Dirichlet-form functional }F(\mathcal E)
\text{ that captures }s_*\text{ more sharply than the frozen hard-band surrogate.}
}
\tag{BLOCK-SOURCE}
\]

Changing the candidate and reporting its constant as though it were movement of the already-frozen metric would violate the metric rule. This is the central reason rotation is mandatory rather than cosmetic.

## 4. Complete current-target route inventory and precise failure modes

### 4.1 Ordinary spectral-profile integral

The initial comparison-friendly static object was the ordinary spectral-profile integral. Kozma-type sharpness shows that it can add costs from incompatible worst sets across scales, and the reverse ratio to `s_*` is unbounded.

**Failure:** cross-scale quantifiers are wrong: a different extremal set can be chosen at every scale.

### 4.2 State-anchored dyadic local spectrum

Fixing one starting state across all spectral scales repairs that incompatibility. It gives the full-source theorem

\[
s_*\le S_{\rm anch,2}\le2s_*.
\]

**Failure for further movement:** factor `2` is exactly sharp, already on transitive uniform-stationary product chains. Hard band boundaries are also comparison-unstable: arbitrarily small form perturbations moving mass across a dyadic edge can change the surrogate by almost factor two while `s_*` changes only slightly.

### 4.3 Finer deterministic bands

Replacing binary bands by ratio `rho>1` gives formally `s_*<=S_anch,rho<=rho s_*`.

**Failure:** this is a different candidate and therefore cannot be used to game the frozen metric. As `rho` approaches one it also approaches exact spectral diagonalization, while retaining hard-boundary instability.

### 4.4 Finite resolvent / implicit-Euler filters

Finite-depth resolvent cascades are variational and comparison-friendly, but the exact refresh-chain calculation gives an unbounded ratio to `s_*` for every fixed depth.

**Failure:** polynomial high-frequency decay cannot reproduce the heat kernel's exponential localization.

### 4.5 Infinite resolvent depth

Taking the depth to infinity recovers the exponential semigroup.

**Failure:** exactness is bought by rebuilding `e^{-tL}` itself, which is tautological relative to the source's comparison-oriented motivation.

### 4.6 Conventional Hermon–Peres hitting profile

Hermon–Peres characterize the conventional `tau_2(1/2)` up to constants by hitting-time distributions.

**Failure:** the Aldous–Fill threshold is `tau_2(sqrt3)`. Near the source singular boundary `pi_*=1/4`, standard-threshold quantities remain macroscopic while `s_*` can collapse, so the conventional theorem cannot simply be transplanted.

### 4.7 Threshold-matched hitting profile

C28 matched the threshold exactly and proved `rho^(sqrt3)<=s_*`, exact zero-set agreement, and a two-state asymptotic match from below.

**Failure:** claim `C28-I0032-MATCHED-HITTING-NO-REVERSE-09` gives an explicit three-state reversible family for which `rho^(sqrt3)` stays bounded while `s_*` diverges like `(1/4)log(1/(4p-1))`. Sets with stationary mass just above `1/4` become invisible to the survival constraint while residual spectral mass still controls the source threshold.

### 4.8 Hard-band smoothing tension

The accumulated evidence is now structural rather than a missing estimate: hard spectral localization has the right exponential tail but is perturbation-unstable; positive resolvent-type soft filters are comparison-friendly but have tails that are too slow; exact heat flow has both the right tail and the right answer but is the semigroup itself.

**Failure:** no route so far simultaneously supplies exponential localization, static variational comparison stability, and a non-tautological source characterization.

## 5. What a successful proof would have to contain

A genuinely new source-level characterization would need, in one object, all of the following features that no tested route currently combines:

1. **one-anchor cross-scale compatibility**, so unrelated extremizers cannot be summed as in the ordinary spectral profile;
2. **near-critical mass sensitivity on both sides of `1/4`**, so the three-state threshold-switch obstruction cannot hide a slow cluster;
3. **residual-mass information**, not only exit time or relaxation scale;
4. **exponential high-energy localization**, strong enough to avoid the finite-resolvent tail obstruction;
5. **stability under comparison of Dirichlet forms**, unlike hard spectral projectors;
6. a genuinely static/variational formulation that does not simply reconstruct `e^{-tL}`.

The missing ingredient is therefore not another lemma about the already-frozen binary bins. It is a new object with incompatible-looking analytic properties.

## 6. Simplest special case still unproved

The three-state family that killed the matched-hitting reverse inequality is now solved as a counterexample, so it is no longer the simplest unresolved obligation.

A clean smallest remaining laboratory is the following restricted design problem:

> On arbitrary **three-state reversible chains**, can one construct a positive static variational functional from Dirichlet-form data—without exponentiating the generator and without hard spectral cutoffs—that is monotone/stable under form comparison and approximates the source threshold `s_*` with a universal factor strictly below `2`?

This is deliberately a restricted special case and is **UNPROVED**. A positive answer would still be PARTIAL relative to Open Problem 8.23; a negative answer could explain why comparison-stable exact characterizations are structurally impossible. No result on this special case is claimed in this thinking run.

## 7. Section-B move 9 — RANDOMIZE the dyadic phase

The hard-band sharpness family exploits the phase of an eigenvalue relative to a fixed dyadic boundary. A natural escape is to randomize the logarithmic offset of the binary grid before aggregating local spectral mass.

For one scalar eigenvalue, a uniform logarithmic shift makes its lower-endpoint rounding ratio log-uniform on `[1,2)`. A scratch calculation gives mean rounding ratio

\[
\int_0^1 2^u\,du=\frac1{\log2},
\]

well below `2`. More importantly, averaging over the phase smooths the discontinuity at any single dyadic boundary.

**Why this did not produce movement:** the threshold functional is nonlinear in the whole spectral measure and includes a maximum over states. An average scalar rounding factor does not imply a uniform threshold comparison. At large `t lambda`, even a small set of shifts placing `lambda` near the top of a binary band contributes on the slow `lambda/2` clock; positive phase averaging therefore retains a worst-tail obstruction. Turning this into a source theorem would require a uniform spectral-measure inequality, not the scalar average above.

This route is worth preserving because it addresses the instability mechanism directly, but it does not alter `(2.1)` and no theorem claim is made.

## 8. Section-B move 10 — DERANDOMIZE with shifted grids

The next thought is to use finitely many shifted dyadic grids and select one deterministically. For a **single eigenvalue**, `K` evenly shifted grids ensure that one grid rounds that eigenvalue by at most a factor `2^(1/K)`.

The obstruction is simultaneity. A chain can carry important local spectral mass at several logarithmic phases and at several starting states. The shift that is favorable for one cluster of eigenvalues need not be favorable for the others. Taking a different shift separately for each band merely refines the spectral partition and returns to a different hard-band candidate; taking a single global shift leaves an adversarial multi-phase problem.

**Outcome:** derandomization identifies a precise missing minimax statement—one phase must work simultaneously for every relevant anchor and scale—but no such minimax theorem was found. Because the frozen candidate is binary and already sharp, even proving it would define a replacement object rather than move the present metric.

No new finite checker was appropriate: there is no finite claim to certify in this thinking run.

## 9. Section-B move 13 — FIND WHAT ONLY INCREASES under comparison

The source motivation asks for an object useful with the comparison technique, so I looked for quantities monotone under strengthening of the Dirichlet form.

Resolvent quadratic forms such as

\[
R_x(a)=\langle r_x,(I+aL)^{-1}r_x\rangle_\pi
=
\sup_g\{2\langle r_x,g\rangle_\pi-\|g\|_2^2-a\mathcal E(g,g)\}
\]

have exactly the desired variational comparison monotonicity. The earlier finite-resolvent obstruction, however, shows the cost of that monotonicity: finite positive combinations inherit polynomial rather than exponential high-frequency tails.

The diagnostic is sharper when viewed through scalar functional calculus. The heat multiplier `e^{-t lambda}` has the needed exponential decay, while the most natural positive comparison-monotone soft filters are resolvent/Stieltjes-type kernels. This suggests that the conflict between **Loewner/form monotonicity** and **exponential spectral localization** may be structural, not merely a poor choice of finite approximation.

**Outcome:** this is the most promising future obstruction theorem to formalize if I0032 is ever reassigned. One would try to prove that a sufficiently broad positive comparison-monotone filter class necessarily has slow tails, which would explain the refresh-chain failure abstractly. I do not claim that theorem here.

## 10. Nearest solved literature and current-status refresh

Fresh bounded searches dated **2026-09-17** included:

- `"Open Problem 8.23" Aldous Fill N(s) Dirichlet form hypercontractivity`;
- `"Open Problem 8.23" Aldous Fill reversible Markov chain 2025 2026 hypercontractivity`;
- `"A characterization of L2 mixing and hypercontractivity via hitting times and maximal inequalities" Hermon Peres`;
- `"Open Problem 8.23" Hermon Kozma sensitivity mixing times`.

The live Aldous–Fill page still states Open Problem 8.23. Hermon–Peres (PTRF 170 (2018), 769–800) give a constant-factor probabilistic characterization of conventional reversible `L_2` mixing and an extremal log-Sobolev characterization. Hermon–Kozma, *Sensitivity of mixing times of Cayley graphs* (published online 18 July 2023; Canadian J. Math. 76(4), 2024), explicitly cite Aldous–Fill Open Problem 8.23 in the robustness/comparison discussion. I found no later source explicitly claiming to resolve the exact `N(s*)=2` characterization.

That is a **bounded negative search only**. It is not proof of worldwide openness and not a novelty certificate.

The nearest solved technique remains Hermon–Peres. What it has that the exact source threshold lacks is a uniform margin in its conventional threshold regime that permits hitting-time estimates plus relaxation corrections. At the Aldous–Fill `sqrt3` threshold, the `pi=1/4` switch destroys that uniform margin, exactly as the three-state counterexample demonstrates.

## 11. Section-I action and successor screen

I choose exactly one Section-I action:

\[
\boxed{\textbf{MOVE TO THE NEXT PROBLEM IN QUEUE.md AND RECORD THE SWITCH.}}
\]

The current queue/claim screen does not expose a lawful READY unassigned CLOSABLE successor for C28, so the operational result is a **rotation hold**, not a fabricated claim.

The front of the current queue was checked as follows:

- `I0006` remains `HOLD_SOURCE / PENDING`, with no exact remaining open source locator recovered. A fresh read of Bou-Rabee–Panagiotis, arXiv:2609.02820, shows the paper itself says it answers the cited earlier parking-model questions and proves the advertised tail/growth asymptotics; this makes invention of an unspecified “remaining odometer-tail problem” especially unsafe.
- `I0011` has a current canonical claim and is not unassigned.
- `I0028` remains `HOLD_SCOPE` / HARD rather than an admitted CLOSABLE dispatch.
- `I0035` is canonically reserved to C31.
- `I0054` is canonically reserved to R11.
- `I0055` is not a live reserve item: the current Lyons–Peres text records Pengfei Tang's positive answer to the modified Question 5.16, and repository admission evidence likewise treats it as resolved for queue purposes.
- `I0070` is reserved to R10.
- `I0068` is READY but already claimed by P19.
- `I0066` is already claimed by P15.
- `I0077` remains owned by R07.

Thus C28 does **not** create a replacement claim. Its state after this report is

**ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED**.

I0032 remains preserved as a handoff/reserve research record with all proved partial results and failed routes. A future return requires a fresh route/admission decision; the present C28 slot is not authorized to run a seventh unchanged I0032 attack.

## 12. Directed second-audit duty — C29

C29's actual newest report is

`proofnet24/C29-closure-brownian-shapes/runs/2026-09-16/2026-09-16T23-36-35Z__six-run-rotation-handoff.md`.

It is explicitly a six-run thinking/handoff report with **no new C29 theorem claim**. Therefore there is no legitimate fresh claim for C28 to audit in this run. I do not manufacture a receipt-only or duplicate audit.

Preserve the latest valid C28 verdict

`C28-AUDIT-C29-DC34-CENTERED-TWO-DEFECT-10 = PASS (claim-scoped)`.

That PASS covers only C29's centered two-defect semialgebraic/finitely-laminated hull theorem; it does not settle Directional Convexity Conjecture 34 or certify a successor admission.

## 13. Handoff summary

Preserve all of the following if I0032 is later reassigned:

- exact source parameter `s_*=inf{s>=0:||P_s||_{2->infinity}<=2}=tau_2(sqrt3)`;
- full source class: finite irreducible reversible continuous-time chains;
- `C28-I0032-ANCHORED-DYADIC-04`: `s_*<=S_anch,2<=2s_*`;
- `C28-I0032-ANCHORED-DYADIC-SHARP-05`: factor `2` is exact optimal for the frozen binary candidate, even on transitive uniform chains;
- `C28-I0032-HARD-BAND-INSTABILITY-06`: hard binary bands are comparison-unstable under arbitrarily small form perturbations;
- finite-resolvent fixed-depth tail obstruction;
- exact identity `s_*=tau_2(sqrt3)` and threshold-matched one-sided hitting bridge;
- `C28-I0032-MATCHED-HITTING-NO-REVERSE-09`: no universal reverse factor for the matched hitting profile, with the exact three-state source-normalized family and symbolic certificate;
- the candidate restricted margin class `Delta(pi)>=delta` is only a future PARTIAL direction, not a theorem;
- all bounded prior-art searches remain negative evidence only;
- Paley-ETF reserve remains independent and untouched.

The research diagnosis at handoff is: **comparison stability, exponential localization, and non-tautological static representation have not yet been achieved simultaneously.**

## 14. Model / scheduler control

Actual runtime metadata available to this report identifies **GPT-5.6 Sol**. Reasoning effort is **UNVERIFIED**. This is not GPT-6 at maximum.

The exposed task-control interface still supports prompt/title, schedule/timing, and enabled state; it exposes no model-family selector and no reasoning-effort selector and supplies no authenticated applied-runtime telemetry. Therefore `GPT-6 / maximum` remains prompt-only. Enforcing it requires scheduler/backend or authorized enclosing-runtime support that exposes, persists, binds, and reports those fields.

The historical P26 response `You cannot modify this task` is a permission/ownership-context boundary. The legitimate workaround remains modification from the authorized owner/admin/coordinator context or platform support. Do not bypass permissions and do not create a duplicate task as a workaround.

## 15. ledger_delta for P26

```text
track=C28
target=I0032 / Aldous-Fill Open Problem 8.23
source_parameter=s_*:=inf{s>=0: ||P_s||_{2->infinity}<=2}=tau_2(sqrt3)
source_class=finite irreducible reversible continuous-time chains
frozen_candidate=S_anch,2(E) / binary state-anchored dyadic local-spectral threshold
metric_before=2
metric_after=2
movement=no movement
unchanged_run_count_before=5
unchanged_run_count_after=6
protocol=STUCK RECOVERY 2 / THINKING-ONLY; six-run CLOSABLE rotation/handoff
new_C28_theorem_claim=none
moves_used=9,10,13
assigned_suggested_moves_replaced=yes; B11 and B22 already occurred in recovered I0032 move history, so three untried moves were used
selected_section_I_action=move to next problem in QUEUE.md and record the switch
successor=none claimed; ROTATION HOLD — SUCCESSOR ADMISSION REQUIRED
status=PARTIAL / I0032 handoff preserved / no seventh same-target run authorized
paley_etf_reserve=unchanged; kappa_*=6.6575355565204281495... at (73,14), exact radius-two certificate and existential-quantifier correction preserved
second_audit=no new C29 theorem; preserve C28-AUDIT-C29-DC34-CENTERED-TWO-DEFECT-10=PASS claim-scoped
shared_ledger_edit=none
peer_file_edit=none
```
