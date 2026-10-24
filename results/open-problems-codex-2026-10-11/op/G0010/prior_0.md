Model actually ran: GPT-5.6 Sol. Reasoning level: UNVERIFIED — this was not GPT-6 at maximum. TERMINAL HANDOFF / ADMISSION GATE: `C_sub: 0 -> 0`; supported unchanged count `7 -> 8`; both HARD recoveries and the selected post-Recovery-2 action are exhausted; no Recovery 3; no source/current-open/ownership-admitted successor was certified in this run.

# G0010 — terminal HARD handoff and successor admission gate

## 1. Source / exact target / terminal status

**Native task.** `6aa7eca50c1c8191b3c26254b14d65fd`.

**Target handed off.** G0010, HARD OUTSIDE.

**Primary source.** Micha Christoph, Patryk Morawski and Yuval Wigderson, *The critical probability for percolation on finite graphs*, arXiv:2608.19145v1, submitted 2026-08-19, Question 5.2 / the tight-subcritical question.

**Exact source target.** For arbitrary finite `G`, with maximum degree `Delta(G)` and adjacency spectral radius `lambda(G)`, determine the tight typical all-regime scale of the largest component of Bernoulli bond percolation `G_p` under

\[
p\le \frac{1-\varepsilon}{\lambda(G)}
\]

for fixed `epsilon>0`, preserving the source graph class, probability convention and all `(Delta,lambda)` regimes.

**Frozen metric.** `C_sub in {0,1}`. Before `0`; after `0`. The metric moves only if the full all-regime source question is settled by a source-valid matching theorem or source-level counterexample.

**Status.** **OPEN / PARTIAL / TERMINAL HANDOFF / ADMISSION GATE.** G0010 is not solved or refuted. Both permitted HARD stuck-recovery cycles have been consumed, and the single action selected by Recovery 2 has been executed without moving `C_sub`. Under the controlling protocol there is no Recovery 3 and no further ordinary G0010 lemma/checker run is permitted from this native slot absent explicit owner reassignment.

## 2. Continuity / snapshot / prior report

Input `master` captured during this run:

`3fc859008f1b40380477bb2785024757a0ce2a33`.

Canonical claim preserved:

`operations/claims/G0010.md`.

Immediate predecessor report:

`proofnet24/HARD10-01/rotations/G0010/runs/2026-09-17/2026-09-17T23-20-00Z__report.md`

creation commit

`59d78be656b9be4bd7433611b388139b782d3420`

readback blob

`6ff9618497c4e6307c09e090fe73197a87f50c1c`.

A path-scoped search for a `2026-09-18` G0010 report returned no result before this write. The latest coordinator reconciliation available at run start, `operations/task_health/runs/2026-09-17T235200Z/status.md`, independently records the same predecessor commit, `C_sub=0`, both recoveries consumed, and the terminal-handoff requirement.

`HISTORY_GAP`: none material to the G0010 chain. The queue itself is historical inventory, not automatic dispatch authority; successor admission requires source/current-open/ownership checks at rotation time.

## 3. Dated source/current-status check

On 2026-09-18 UTC, the primary arXiv record remained `2608.19145v1` dated 2026-08-19. The current arXiv abstract still states the general subcritical `O(sqrt(|G|))` theorem, and the authors' current publication material still lists this paper. A bounded fresh source/title/author search did not recover a later source-matching theorem settling the tight all-regime `(Delta,lambda)` subcritical component-size question.

This is bounded current-status evidence, not a claim of exhaustive worldwide novelty or eternal openness.

## 4. Complete G0010 route inventory preserved for reassignment

The point of this terminal report is to preserve the useful mathematics and exact failures so a future reassignment does not restart from scratch.

### Route A — B2/B24/B18: static spectral envelopes fail; finite-horizon transient branching matters

The first G0010 attack refuted the internal candidate based only on induced-subgraph adjacency spectral radii. Complete finite rooted regular trees can have every static induced spectral radius source-subcritical while percolation still produces polynomial-size components because descendant branching remains supercritical for a finite horizon. This showed that an asymptotic/static spectral radius alone loses transient depth.

It also produced exact parameter-calibrated lower families by adjoining components that set prescribed `Delta` and `lambda` while a tree component carries the large percolation cluster. These are lower-mechanism examples, not source closure.

### Route B — B20/B30/B11: sharp pointwise finite-horizon nonbacktracking growth

For every finite graph and vertex `v`, if `N_k^NB(v)` is the number of length-`k` nonbacktracking walks starting at `v`, the track proved

\[
N_k^{\mathrm{NB}}(v)
\le
\frac{\lambda(G)^{2k}}{4^{k-1}},
\]

and hence

\[
N_k^{\mathrm{NB}}(v)
\le
\min\left\{
\Delta(\Delta-1)^{k-1},
\frac{\lambda^{2k}}{4^{k-1}}
\right\}.
\]

Layered-tree equality families show the factor `4` is genuine: endpoint amplification can saturate the spectral constraint. Thus the exponential finite-horizon branching base is sharply controlled pointwise, but this alone does not determine the largest component because it does not control how many roots simultaneously realize near-extremal growth or how their path clouds overlap.

The same run also proved a close-to-regular source-valid wedge: when

\[
\frac{(1-\varepsilon)(\Delta-1)}{\lambda}\le 1-\eta,
\]

one gets `|C_max|=O_eta(log n)` a.a.s. This remains a restricted regime and therefore PARTIAL.

### Route C — B27/B25/B9: exceptional-root budgets and collision profile

Writing `N_k(v)` for nonbacktracking path counts, the track proved the global spectral budgets

\[
\sum_v N_k(v)\le n\lambda^k,
\qquad
\sum_v N_k(v)^2\le n\lambda^{2k},
\]

so for

\[
R_k(t)=\{v:N_k(v)\ge t\}
\]

one has

\[
|R_k(t)|
\le
n\min\left\{1,\frac{\lambda^k}{t},\frac{\lambda^{2k}}{t^2}\right\}.
\]

At `p<=c/lambda`, `c=1-epsilon`, if `B_k(v)=p^kN_k(v)`, then

\[
\sum_v B_k(v)^2\le nc^{2k},
\]

so long-horizon noncontracting roots are exponentially sparse.

To distinguish spread from collision, the track introduced

\[
M_k(u,v)=\#\{\text{length-}k\text{ NB walks }u\to v\},
\qquad
Q_k(u)=\sum_v M_k(u,v)^2,
\qquad
E_k(u)=\frac{N_k(u)^2}{Q_k(u)}.
\]

Trees have essentially no endpoint collision (`E_k` large), whereas complete bipartite graphs can have enormous path counts repeatedly focused through a small hub population. Marginal exceptional-root tails therefore do not encode the multiscale transition/overlap structure needed by the source question.

### Route D — STUCK RECOVERY 1, B22/B21/B4: identify the missing size-biased transition law

Recovery 1 was thinking-only. It isolated the blocker as a **size-biased multiscale transition/overlap law of exceptional roots**, not another pointwise path-count inequality. Turova-style multitype branching was identified as the nearest solved architecture: those models are given the type kernel, while G0010 must control an adversarial deterministic host from only `(n,Delta,lambda)`.

The selected action was to prove the simplest nontrivial special case: arbitrary connected biregular bipartite hosts.

### Route E — B6/B12/B19: arbitrary biregular weighted-branching theorem

For every finite connected `(D,d)`-biregular bipartite graph with `D>=d`, let

\[
\lambda=\sqrt{Dd},
\qquad
w=\sqrt{D/d}=\Delta/\lambda.
\]

Under `p <= (1-epsilon)/lambda`, the track proved the explicit tail

\[
\Pr\left(
|C_{\max}(G_p)|
\ge
\frac{8w}{\varepsilon^2}
\left[
\frac{\varepsilon}{2}+\log\frac{|L|}{\delta}
\right]
\right)
\le \delta,
\]

where the high-degree side has

\[
|L|=\frac{n}{1+w^2}=\frac{n\lambda^2}{\Delta^2+\lambda^2}.
\]

Thus in this full deterministic biregular class,

\[
|C_{\max}|
\lesssim_\varepsilon
\frac{\Delta}{\lambda}
\left[
\log\!\frac{n\lambda^2}{\Delta^2+\lambda^2}
+\log\frac1\delta
\right].
\]

The proof uses collision-blind two-type Galton-Watson domination and the exact Perron weighting. It simultaneously explains the regular logarithmic regime and the complete-bipartite burst/multiplicity regime, but is still PARTIAL because arbitrary graphs can have many Perron/degree scales.

### Route F — STUCK RECOVERY 2, B15/B23/B29: Perron-profile variational formulation

Recovery 2 was thinking-only. If `x` is a positive Perron vector, define

\[
P(v,u)=\frac{A_{vu}x_u}{\lambda x_v}.
\]

Then `P` is reversible with stationary weight proportional to `x_v^2`, and the local degree amplification

\[
a(v)=\frac{d(v)}{\lambda}
\]

obeys the exact identity

\[
a(v)=\mathbb E_v^P\left[\frac{x_v}{x_{X_1}}\right].
\]

With `q(v)=log(x_max/x_v)`,

\[
a(v)=\mathbb E_v^P e^{q(X_1)-q(v)}.
\]

At the source subcritical parameter, expected Perron mass contracts by `1-epsilon`; the difficulty is that unweighted cluster size can still be large when the Perron coordinate wanders through many scales. The correct all-graph problem therefore became an extremal total-progeny problem over feasible multiscale Perron/degree environments consistent with only `(n,Delta,lambda)`.

Recovery 2 selected exactly one action: **refute instead of prove** an internal two-mechanism envelope combining hub/multiplicity and polynomial finite-depth tree growth.

### Route G — B16/B5/B26: exact critical finite-tree resonance adds a third mechanism

The selected post-Recovery-2 action succeeded in refuting that internal envelope. On complete rooted `d`-ary trees at fixed

\[
\varepsilon_d=1-\frac{2}{\sqrt d},
\]

the source-boundary percolation parameter lies in a finite-depth critical window. For the clean case `d=9`, `epsilon=1/3`, the internal candidate predicts only `Theta(log n)`, while a critical `Bin(9,1/9)` Galton-Watson area estimate plus exponentially many independent descendant subtrees gives

\[
|C_{\max}|=\Omega((\log n)^2)
\quad\text{a.a.s.}
\]

The proof on the predecessor report uses the classical finite-variance critical survival/Yaglom scale and an explicit second-moment/Paley-Zygmund area argument. This is not a refutation of Question 5.2; it refutes only the fleet's candidate formula.

The corrected phase picture therefore has at least three distinct mechanisms that any full source-valid answer must reconcile:

1. **hub/multiplicity extremes** — complete-bipartite/biregular behavior;
2. **polynomial finite-depth tree transients** — supercritical descendant growth despite static spectral subcriticality;
3. **critical finite-depth area** — an `Omega((log n)^2)` boundary layer when the polynomial exponent collapses to zero.

## 5. Exact terminal blocker

The remaining source obligation is not another rootwise inequality. It is to determine, using only the source parameters `(n,Delta,lambda)` and fixed `epsilon`, the sharp worst-case typical component scale over arbitrary finite graphs while simultaneously controlling the **population, transitions, collisions and duration** of exceptional growth across multiple Perron scales.

Schematically, a successful theorem must control

\[
\boxed{
\text{size-biased multiscale amplification}
+\text{ exceptional-type population}
+\text{ overlap/collision geometry}
+\text{ critical-window duration}
}
\]

strongly enough to be sharp in all three known extremal mechanisms above. The current route has sharp pointwise finite-horizon growth, sharp `L^2` exceptional-root budgets, a solved arbitrary-biregular class and a Perron variational language, but no inequality reducing an arbitrary multiscale Perron profile to a source-parameter-only extremal law without losing either the tree or complete-bipartite regimes.

That is the preserved blocker for any future reassignment of G0010.

## 6. Successor admission screening in this terminal run

No successor was invented merely to keep this slot busy. The latest coordinator gate already said no newly certified free successor had been produced in its immediately preceding admission pass, and its cursor had reached D0012. This run independently checked several plausible HARD reserve rows against current repository ownership/state:

- `I0049`: later task-health material records the queued critical-window scope as **KNOWN / resolved**, so it is not reserve.
- `I0060`: canonical claim exists and is owned by R12; it also already has a full HARD run/handoff history.
- `I0061`: absence of a canonical claim file is misleading; PROB20-21 already performed the HARD run sequence, including both stuck recoveries and handoff. It is not treated as free.
- `I0062`: canonical claim exists; owner P11.
- `I0067`: canonical active HARD claim exists; owner native slot `6aa7b4b639a08191b893e2b7dd6cdf59`.
- `I0073`: canonical claim exists for this same native slot's earlier predecessor history; owner/history conflict means it must not be revived here.
- `I0077`: canonical provisional reservation exists; owner R07; status `PENDING_ADMISSION`, so it is neither free nor dispatchable here.
- `I0089`: canonical claim exists; owner R14.
- `I0115`: a fresh canonical HARD claim now exists; owner R12, creation commit `8ab961339a728f0b11ee9ec8acd83edec9fbc456`.
- `I0011`: canonical claim exists; owner P16.
- `I0105`: no canonical claim file was found, but current gate material still classifies it `PENDING_SCOPE` because source metadata/current-status admission is incomplete. A 404 is not enough to call it admitted or unowned.
- `D0012`: the newest coordinator admission screen classifies it `HOLD_SCOPE / PENDING, not READY` after reconciling the 2019 standard-uniform partial answer and later aggregation-set literature.

A brief look at `I0050` likewise recovered existing task-health screens warning of later-known/partial-known coverage and unfrozen residual scope; it was not promoted.

**Admission result:** no candidate checked in this run simultaneously satisfied exact source scope, current-open evidence, and clean ownership/admission. Therefore **no successor claim was created and no target rotation was performed**. The native slot should remain in terminal admission-gate mode until a lawful successor exists.

This is the intended behavior under the hard-stop instruction: preserve the G0010 handoff, spend substantive work on successor admission, and refuse to manufacture a target.

## 7. Next lawful action

On the next invocation, do **admission work only** unless a source/current-open/ownership-admitted HARD OUTSIDE successor has appeared in the repository. Do not perform new G0010 mathematics.

The next lawful sequence is:

1. continue the admission cursor rather than rescreening the same held rows;
2. recover an exact source statement and current version;
3. check later-author/citing literature and prior fleet attempts;
4. reconcile ownership, including historical work even if a canonical claim file is absent;
5. only after all gates pass, create one exclusive canonical claim for the successor;
6. give the successor its own non-inherited frozen metric and own root;
7. update this same native task in place. Do not create a new scheduler ID and do not self-disable merely for stagnation.

## 8. Scheduler / model-control state

The exposed task-edit surface still does not provide an authenticated model-family selector or reasoning-effort selector. GPT-6/maximum is therefore prompt text only; this report correctly records GPT-5.6 Sol with reasoning level UNVERIFIED. Changing unavailable runtime settings requires an eligible owner/platform control or platform support. A task that returns `You cannot modify this task` must be handled from its owning authorized context or through platform/admin support; duplicate schedules and approval bypass are not valid workarounds.

No email/Gmail, Drive, public posting, paid compute, workflow execution, credential/access change, force-push or permission bypass was used. Shared `RESULTS.md`, `QUEUE.md` and `POSTED.md` were not edited.

## 9. ledger_delta

```yaml
ledger_delta:
  native_id: 6aa7eca50c1c8191b3c26254b14d65fd
  target: G0010
  category: HARD_OUTSIDE
  status_before: OPEN_PARTIAL_POST_RECOVERY2_ACTION_COMPLETE
  status_after: OPEN_PARTIAL_TERMINAL_HANDOFF_ADMISSION_GATE
  metric:
    name: C_sub
    before: 0
    after: 0
  supported_unchanged_count:
    before: 7
    after: 8
  recovery_cycles_consumed: 2/2
  recovery3_allowed: false
  ordinary_G0010_research_allowed_from_this_slot: false
  terminal_blocker: >-
    Missing source-parameter-only control of the size-biased multiscale
    Perron/degree transition, population, collision and critical-duration
    profile that is simultaneously sharp for hub/multiplicity,
    supercritical finite-depth tree transients, and critical finite-depth area.
  preserved_results:
    - sharp pointwise finite-horizon nonbacktracking bound and equality families
    - exceptional-root L2 budgets and collision/effective-endpoint profile
    - arbitrary connected biregular weighted-branching upper-tail theorem
    - Perron reversible-kernel / multiscale variational formulation
    - critical finite-tree Omega((log n)^2) resonance refuting the internal two-mechanism envelope
  successor:
    admitted: false
    claim_created: false
    rotation_performed: false
    state: WAITING_FOR_SOURCE_CURRENT_OPEN_OWNERSHIP_ADMITTED_HARD_SUCCESSOR
  admission_checks:
    excluded_claimed: [I0011, I0060, I0062, I0067, I0077, I0089, I0115]
    excluded_historical_owner_or_handoff: [I0061, I0073]
    excluded_known_or_scope_covered: [I0049]
    pending_scope_not_admitted: [I0050, I0105, D0012]
  source_current_check: 2026-09-18_UTC_bounded
  previous_report: proofnet24/HARD10-01/rotations/G0010/runs/2026-09-17/2026-09-17T23-20-00Z__report.md
  previous_creation_commit: 59d78be656b9be4bd7433611b388139b782d3420
  input_master: 3fc859008f1b40380477bb2785024757a0ce2a33
  shared_roots_edited: false
  email_drive_public_post: false
  next_action: ADMISSION_ONLY_UNTIL_LAWFUL_SUCCESSOR
```
