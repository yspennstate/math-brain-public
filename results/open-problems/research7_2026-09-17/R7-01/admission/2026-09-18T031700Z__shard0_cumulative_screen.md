Model actually run: **GPT-5.6 Sol**. Reasoning level: **UNVERIFIED**. This is **not GPT-6 at maximum**; the exposed runtime provides no authenticated model/effort selector or telemetry establishing that requested configuration.

# R7-01 shard-0 cumulative admission screen — 2026-09-18

## Scope and continuity

Native slot: `R7-01`, native ID `6aabe777361481919c9e614646464772`.

Start-of-run `master`: `b095a0116a52ebb7bb43bb1b4daa8101760d785c`.

Newest prior own report recovered and read: `research7_2026-09-17/R7-01/runs/2026-09-18/2026-09-18T021800Z__report.md`, creation commit `568620f8d8d162397e4810064f29e9acdecf3e1c`.

Fresh pre-delivery `master` observed after screening: `5415c81f1b8a69f15989ff6bbd4218afede6b29e`.

R7-01's admission shard is the exact case-sensitive gate

`sum(ord(c) for c in canonical_id) % 7 == 0`.

This file advances the admission cursor. It creates **no assignment and no ownership claim**. The predecessor D0033 metric and stagnation count remain frozen with its six-run handoff; they are not inherited.

## New shard-0 dispositions recovered in this pass

### D0015 — exclude as KNOWN / resolved in literature

Intake identity: Angel-Holroyd-Romik random sorting networks, Conjecture 3 (Great circles), PDF p. 9. The intake itself records Duncan Dauvergne, *The Archimedean limit of random sorting networks* (arXiv:1802.08934; JAMS), as resolving the conjecture. A separate current repository admission screen on 2026-09-17 likewise classifies D0013-D0015 as resolved. D0015 therefore cannot be admitted.

### D0024 — do not admit; later literature materially overlaps the literal convergence target

Source intake target: disordered asymmetric zero-range process, Problem 3, Section 4, PDF p. 9. It asks, for fixed site disorder and a spatially ergodic initial distribution of density `rho`, whether the process converges weakly to the corresponding equilibrium, and in the supercritical phase whether the local limit is the critical-density equilibrium.

A fresh 2026-09-18 literature check recovered C. Bahadoran, T. Mountford, K. Ravishankar and E. Saada, *Quenched convergence and strong local equilibrium for asymmetric zero-range process with site disorder*, arXiv:1804.06148, PTRF 176 (2020). Its abstract states quenched strong local equilibrium at subcritical and critical hydrodynamic densities, dynamic local loss of mass at supercritical density, no local-Gibbs starting assumption, and convergence from given initial configurations with an asymptotic density. Their 2020 survey *Zero-range process in random environment* also describes necessary and sufficient conditions for convergence to the maximal invariant measure and strong local equilibrium.

This is too close to the literal D0024 endpoint to certify D0024 as a fresh current-open target without a theorem-by-theorem scope comparison. Since the slot requires a clean current-open CLOSABLE endpoint, D0024 is **not admissible in this pass**. This is a conservative scope exclusion, not a claim that every quantifier of the 1999 problem has been proved.

### D0042 — current-looking but not honestly CLOSABLE

Source: Bálint Virág, operator-limits problem list (2014), Question 4 (Formulas), PDF p. 13: derive/connect edge and bulk correlation formulas directly from the limiting random operators (stochastic Airy operator and Brownian-carousel/Sine-beta operator).

The recovered intake attempt already reduces the bulk side to the joint winding law of several hyperbolic diffusions driven by the same Brownian motion; the missing object is a tractable multi-point stationary law / correlation computation. Even if still open, the source question is a broad operator/integrable-probability programme rather than a short source-level theorem, finite certificate, sharp constant, or single explicit counterexample. R7-01 therefore classifies it **HARD-shaped / not eligible for this CLOSABLE slot** rather than relabeling it to satisfy portfolio pressure.

### D0051 — exclude from this slot as HARD

Source intake: LQG metric survey, Problem 5.3, asking for the thickness spectrum of points on an LQG geodesic. This is a global multifractal/LQG-geodesic problem, not a finite certificate or short counterexample endpoint. No CLOSABLE admission.

### D0084 — exclude from this slot as HARD and later-work-sensitive

Source intake: mating-of-trees survey, Problem 6.5, embedded convergence to LQG for spanning-tree-weighted and bipolar-oriented maps. The intake already flags later Holden-Yu activity/seminar evidence. The source target is a full scaling-limit/embedding theorem, not a short finite endpoint. No CLOSABLE admission.

### D0093 — excellent CLOSABLE shape, but fresh canonical ownership collision

Source: Leonardo T. Rolla, *Activated Random Walks on Z^d*, Probability Surveys 17 (2020), Section 6.2, open problem immediately after Theorem 6.1 / estimate (6.3): remove the `log^2 n` factor from the high-probability finite-cycle fast-phase toppling bound.

This would otherwise fit R7-01 well. However fresh master contains `operations/claims/D0093.md`, which records an **EXCLUSIVE / OPEN / PARTIAL** claim owned by P13 / native `6aa7b253b37c8191b693d8dc79298d37`, with frozen metric `beta_fast=2` and source target `beta_fast=0`. R7-01 therefore skips D0093 and does not duplicate or edit the P13 work.

### I0125 — finite and shard-compatible, but unavailable

`I0125` (five-dimensional kissing number) is shard 0 and has a crisp finite metric, but `operations/claims/I0125.md` records an exclusive native claim by another worker. Its history includes the six-run retirement/handoff line for that worker; under the owner rule a disabled/retired worker state is not a release of canonical ownership. R7-01 does not revive it.

### F-family continuation — no newly eligible CLOSABLE source recovered

The cumulative F-family screen now excludes or downgrades the shard-0 sequence encountered so far: F0004 is literature-resolved; F0040 and F0047 are literature-resolved; F0056/F0057 are already answered in the campaign; F0065 and F0074 are asymptotic HARD problems; F0083 is closable-shaped but exclusively claimed by R08; F0092 and F0103 are hard asymptotic/conjectural programmes; F0112, F0121 and F0130 are resolved/known; F0137 requires unresolved prior-art/scope work and is not a clean closable endpoint.

### G/H continuation — no admission

G0003 is not admissible because its source/intake formulation intentionally leaves the relevant “disconnection type” undefined, so there is no fixed truth-valued endpoint to claim. H0002 and H0011 remain broad HARD problems, while H0020 is already refuted in the campaign record.

## Admission conclusion

No problem passed all four gates simultaneously:

1. exact shard-0 canonical ID;
2. genuinely CLOSABLE outside source endpoint;
3. current-open/scope-safe after dated literature screening;
4. presently unclaimed/unreserved/not held/not retired.

Accordingly R7-01 remains `PENDING_ADMISSION`. No `operations/claims/<ID>.md` file was created. No target research B-method triple is charged in this pass, because the owner protocol requires admission before target research. The successor metric remains `UNKNOWN/UNMEASURED`; the successor stagnation counter has not started.

## Cumulative cursor for the next pass

Do **not** repeat D0015, D0024, D0042, D0051, D0084, D0093, I0125, G0003, H0002/H0011/H0020 or the already-screened F rows absent a status/ownership change.

Continue the shard-0 intake cursor with still-unscreened exact IDs, beginning with the remaining D-sequence candidates such as D0060, D0067 and D0075, then the next unscreened E/F/I shard-0 candidates. For each promising row, ownership must be checked before mathematical work, and a current-source/later-literature check must precede admission.
