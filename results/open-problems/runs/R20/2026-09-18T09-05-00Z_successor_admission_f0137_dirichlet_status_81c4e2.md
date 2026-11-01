Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — not GPT-6 maximum. NO ADMISSION MOVEMENT: `E_ready: 0 -> 0`; retired I0100 remains frozen at `p_max=1213`, retirement count `6`; methods #6 DEFORM TO A POINT YOU CAN SOLVE, #17 LOOK FOR YOUR NUMBERS SOMEWHERE ELSE, #30 DO ONE PRIME / ONE SCALE / ONE DIRECTION AT A TIME.**

# R20 CLOSABLE OUTSIDE — successor admission: F0137 Dirichlet `(T)_gamma` status reconciliation

Date checked: 2026-09-18 UTC.  
Repository / branch: private `yspennstate/math-open-problems` / `master`.

## 1. Continuity and source guard

I continued from the newest immutable R20 report

`runs/R20/2026-09-18T07-52-02Z_successor_admission_f0111_tropical_handoff_a6e91c.md`.

I reread the campaign `INDEX.md` and `RANKING.md`, root `POSTED.md`, `RESULTS.md`, `QUEUE.md`, the current implementation manifest, current task-health/coordinator surfaces, the relevant intake ledgers, and recent neighbouring reports. In particular, I read the newer R15 F0111 screening report before doing new work and did not duplicate R15's Schur/tropical work.

The retired source remains Afonso S. Bandeira et al., *Randomstrasse101: Open Problems of 2025*, Conjecture 26 / intake I0100, asking whether

`theta(complement G_{p,1}) ~ sqrt(p/2)`

for primes `p = 1 mod 4`. A fresh 2026-09-18 source check of the public Jig/Randomstrasse root still labels this asymptotic **Open** and explicitly distinguishes it from the failed stronger pointwise inequality. I therefore do **not** reopen I0100. The frozen exact-certified frontier remains

`p_max = 1213`,

with retained exact-certified prime set

`{5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213}`.

No new Paley prime, primal/dual certificate, or asymptotic theorem is claimed in this report.

## 2. Admission metric and ownership screen

The successor metric remains

`E_ready = number of newly verified source-clean, current-open, ownership-clear, genuinely CLOSABLE OUTSIDE successors found in this run`.

Before: `0`. After: `0`.

Several superficially finite/closable rows are unavailable and were not duplicated:

- `H0024` has `operations/claims/H0024.md` and a later six-run handoff; the claim has not been explicitly released.
- `G0002` has `operations/claims/G0002.md` owned by R09 and a later handoff; again there is no explicit release.
- `D0067` has a current canonical claim and active campaign reports.
- `F0057` has a current R19 canonical claim; `F0056` is already answered in the campaign record.

The current coordinator/peer admission surfaces still report no newly certified free `READY + CLOSABLE OUTSIDE + UNASSIGNED` successor. I therefore create no ownership claim merely to keep the lane busy.

A bounded repository search found no canonical `operations/claims/F0137.md`, but absence of a claim is not enough for admission: current-open scope and CLOSABLE shape still have to pass.

## 3. Candidate screened this run: F0137

### Exact source question

`F0137` comes from Sabot--Tournier's Dirichlet-environment survey. The source asks for the missing general ballisticity/transience mechanism: in the directionally transient Dirichlet setting, establish an appropriate Sznitman condition `(T)_gamma` (the survey discussion frames a complete parameter characterization as open). The intake's existing attempt had already isolated the tension: time reversal and the parameter `kappa` give sharp finite-trap/invariant-measure information, but they do not themselves produce the regeneration-tail control encoded by `(T)_gamma`.

This run did not try to manufacture a theorem before checking whether later work had already changed the status.

### 2026-09-18 primary/later-literature check

Dated bounded searches used combinations of

- `Sabot Tournier Dirichlet environment condition (T)_gamma directional transience`,
- `Dirichlet environment condition (T) ballistic stable limit Perrel`,
- `2D Dirichlet environment condition (T') Perrel Sabot`,
- exact later-paper titles and author names.

The relevant later primary evidence is:

1. **Adrien Perrel, 2024**, *Limit theorem for subdiffusive random walk in Dirichlet random environment in dimension d >= 3*, arXiv:2404.06502. The abstract explicitly says that, unlike the sub-ballistic result it extends, the paper **has to assume Sznitman's condition (T)** in the ballistic subdiffusive regime `kappa in (1,2)` to obtain the needed regeneration-time control. Thus `(T)` is still an input, not a theorem extracted from directional transience/Dirichlet parameters.

2. **Adrien Perrel--Christophe Sabot, 2025**, *Invariant measure for the process viewed from the particle for 2D random walks in Dirichlet environment*, arXiv:2501.06767. The abstract treats **directional transience and condition (T') as separate assumptions** when constructing the invariant measure in the transient regime. It also still describes recurrence for symmetric weights as strongly conjectural. Again, later Dirichlet-specific work does not collapse directional transience into `(T')`.

3. The Sabot--Tournier overview records that directional transience itself is completely understood in terms of the mean drift `d_alpha`, so the unresolved content is not identifying a transient direction. The hard missing bridge is precisely the stronger quantitative slab/regeneration control.

This is bounded negative evidence, not a worldwide novelty/open-status certificate. But it is sufficient to reject the stale-resolved interpretation: the exact stronger `(T)`/`(T')` mechanism is still being assumed in 2024--2025 work.

## 4. Section-B attacks

### #6 — DEFORM TO A POINT YOU CAN SOLVE

I deformed the proposed implication to the regimes where later papers can already run regeneration arguments. Under stronger ballisticity hypotheses, including an assumed `(T)` or `(T')`, Dirichlet-specific limit/invariant-measure theorems are available. This identifies the solved endpoint of the deformation.

The deformation does **not** glue back: the very hypothesis that has to be removed is `(T)` itself. So this move gives a clean obstruction rather than a new theorem: current techniques solve the problem only after assuming the missing conclusion-level quantitative input.

### #17 — LOOK FOR YOUR NUMBERS SOMEWHERE ELSE

The Dirichlet trapping parameter `kappa` reappears throughout later work, and it sharply governs moment/ballistic versus sub-ballistic regimes. However, the 2024 stable-limit theorem still adds `(T)` on top of the `kappa` regime. Therefore the natural candidate numerical criterion (`kappa`, drift nonsymmetry, or their combination) has not been converted by the later literature into the source-required general `(T)_gamma` theorem.

This is informative because it rules out the tempting inference “the trap exponent was identified, therefore the source condition is now automatic.” It is not automatic in the later papers checked.

### #30 — ONE DIRECTION / ONE DIMENSION AT A TIME

I localized separately to the two most natural pieces.

- In `d >= 3`, Perrel 2024 still assumes `(T)` in the directionally transient/ballistic subdiffusive analysis.
- In `d = 2`, Perrel--Sabot 2025 still assumes directional transience **and** `(T')` separately; the symmetric zero-drift recurrence side remains conjectural.

Thus neither the higher-dimensional nor the two-dimensional slice supplies a source-matching short closure. The failure to glue is not a sporadic dimension issue; it is the same regeneration-tail gap in both slices.

## 5. Disposition

`F0137` is now better classified for this lane as

`CURRENT-OPEN-LOOKING / HARD / NOT CLOSABLE / NOT CLAIMED`.

The fresh contribution of this run is the dated status reconciliation: later Dirichlet-specific work through 2025 continues to **assume** `(T)`/`(T')`, so F0137 should not be discarded as literature-resolved. But its full quantifier is a global RWRE/regeneration theorem, not a bounded finite certificate, one-witness counterexample, or one-constant closure. It therefore fails R20's CLOSABLE admission gate.

No exact finite claim moved, so no checker was created. No shared root, peer claim, or peer run file was edited.

## 6. Next route

R20 remains `SUCCESSOR_ADMISSION_REQUIRED`. The next pass should move to a different source rather than spend another run on F0137. Planned Section-B moves for the next admitted/screened source are:

- #3 PROVE SOMETHING STRONGER,
- #18 SAY IT IN ANOTHER LANGUAGE,
- #26 HUNT THE SPORADIC CASE.

These are deliberately different from this run's #6/#17/#30 triple.

## 7. Model/scheduler control status

The currently exposed task-management surface still provides prompt/title, schedule/timing mode, enablement, and related task controls, but **no binding model-family selector, no reasoning-effort selector, no authenticated applied-run model receipt, and no guaranteed hour-long execution control**. Accordingly GPT-6/maximum cannot be truthfully certified from this worker surface. The historical P26 `You cannot modify this task` case is an authorization-context issue; the lawful workaround is the owning/admin-authorized product surface, supported ownership transfer, or platform support, not duplication or permission bypass. No scheduler changes were attempted in this run.

## 8. Structured ledger delta

```yaml
ledger_delta:
  worker: R20
  repository: yspennstate/math-open-problems
  branch: master
  retired_source:
    id: I0100
    source: Randomstrasse_2025_Conjecture_26
    target: theta(complement_G_p_1)_asymptotic_sqrt_p_over_2
    frozen_metric:
      name: largest_admissible_prime_with_matching_exact_primal_dual_certificates
      value: 1213
      retirement_unchanged_count: 6
      retained_primes: [5,13,17,29,41,181,241,317,421,541,601,661,1009,1021,1033,1049,1061,1093,1201,1213]
  successor_metric:
    name: E_ready
    before: 0
    after: 0
    movement: no_movement
    unchanged_count: UNKNOWN
  section_b_methods: [6,17,30]
  candidate_screen:
    problem_id: F0137
    source: Sabot_Tournier_Dirichlet_environment_overview
    ownership: no_canonical_claim_found_in_bounded_repo_search
    current_status: CURRENT_OPEN_LOOKING
    closable_gate: FAIL_HARD_GLOBAL_REGENERATION_THEOREM
    disposition: NOT_CLAIMED
  evidence:
    - Randomstrasse/Jig source rechecked 2026-09-18: Conjecture 26 root asymptotic still marked Open
    - Perrel arXiv:2404.06502 (2024): condition (T) explicitly assumed
    - Perrel-Sabot arXiv:2501.06767 (2025): directional transience and (T') explicitly separate assumptions
    - current coordinator/peer surfaces: no newly certified free READY+CLOSABLE+UNASSIGNED successor recovered
    - ownership collisions preserved for H0024, G0002, D0067, F0057
  status: SUCCESSOR_ADMISSION_REQUIRED
  remaining_obligation: find_and_create_only_claim_next_source_clean_current_open_unowned_genuinely_CLOSABLE_OUTSIDE_target
  audit_ids: []
  next_methods: [3,18,26]
```

**NO I0100 CLOSURE CLAIM. NO F0137 CLAIM. NO SUCCESSOR CLAIM THIS RUN.**