# F0136 work log

Task received: 2026-11-13 08:25 +04 (Asia/Tbilisi), “Open problem F0136.”

## 08:26 — literature first

Read startup memory index, brain navigation and mesh protocol; checked compute state
(status ok, owner_away_open). The current instruction restricts all work and writes
to this directory, so global brain/checklist/mesh databases will not be mutated.
No subagents. All computation will use nice 10, one worker and limited BLAS threads.
Source PDFs will only be streamed through memory to pdftotext; only text is saved.

Initial searches located Perrel–Sabot, arXiv:2501.06767 (2025): a conditional
two-dimensional invariant-measure result under (T'). This is not yet evidence of
the full conjecture. Also found recent claims for uniformly elliptic environments;
Dirichlet environments are not uniformly elliptic, so those claims do not by
themselves settle this task.

## 08:29 — source reading and search

Saved the 2016 overview v1, Sabot 2013, Bouchet's arXiv preprint, BRS 2016,
Campos–Ramírez, Fribergh–Kious, Guerra–Ramírez, Bouchet–Sabot–dos Santos,
Tournier 2009, Enriquez–Sabot, and Berger–Drewitz–Ramírez as text with source
and text hashes. Read the overview Sections 2–5 and relevant Sections 6–7;
read Sabot's torus proof, especially Lemmas 1–3 and the ergodic argument.
The dimension restriction is the finite-energy flow estimate, not the algebraic
time-reversal identity. The associated reference network has bounded symmetric
conductances and is recurrent in two dimensions.

Perrel–Sabot arXiv:2501.06767, Theorem 2.3, PDF p. 8, gives the invariant
probability under (T') and kappa > 1, with density in L^p for p < kappa.
Conjecture 1, PDF p. 9, still asks for removal of (T'). Targeted searches for
2016–2026 work found no unconditional resolution; this is a bounded search,
not a proof that no such paper exists. Follow-up: Ramírez–Ribeiro 2021 criteria,
Poudevigne-Auboiron and Perrel limit theorems, and the 2026 uniformly elliptic claim.

The shell already inherits niceness 10. A redundant `nice -n 10` printed a
setpriority warning, but the source fetch completed. Direct Python confirmed
os.getpriority(PRIO_PROCESS, 0) == 10; subsequent Python commands retain it.

Planned complete derivations: exact two-site trap tail; logarithmic lower
bound for the flow energy on the two-dimensional torus; a sufficient uniform
integrability reduction from torus stationary densities to ballisticity, including
an elementary stationary-increment argument for nonzero speed. These do not
establish the missing uniform integrability estimate.

## 08:41 — derivations and computations complete; final audit

REPORT.md now contains the full torus uniform-integrability reduction, including
equivalence/ergodicity and an elementary future-minimum proof that stationary
increments escaping in a coordinate have positive mean. It also contains the
explicit harmonic-series lower bound for torus flow energy, the exact two-site
holding-time and Green-function tails, and the conditional regeneration-moment
argument using BRS and Campos–Ramírez. No new unconditional ballisticity region
is claimed. The statement status is PARTIAL.

Ran nine configurations, 24 independent replicas each, 2,000,000 steps per
replica: 432 million walk steps. Separately sampled nine million fresh two-site
holding times. One C++ worker, inherited nice 10, observed peak RSS 158.59375 MiB.
Compiled without diagnostics using -O2 -Wall -Wextra -pedantic.

The exact Beta/Gamma trap probabilities agree with counts; largest absolute
z-score where both expected cell counts >=10 is 3.2133. Finite-product and
log-Gamma evaluations agree independently. Near kappa=1 there is pronounced
finite-time slowing; even kappa<=1 has positive displacement at the last
checkpoint, so no inference of positive limiting speed is made from this.

Read Perrel–Sabot Section 6: (T') enters the return-moment estimate in Lemma
6.1, then a killed-torus construction and product-ratio identity produce
approximately invariant measures, with error vanishing as killing goes to zero.

Checked exact statement locations again. Corrected a preliminary citation of
Perrel 2024 from its background Green-function Theorem 2 to its actual limit
Theorem 6, PDF p. 8; corrected BDR theorem location to PDF p. 4. The published
Tournier text independently verifies the strong-drift and zero-speed results.

The first figure review found mismatched colors between tail points and their
exact-law lines. Fixed the plot to assign one color per parameter set and
regenerated summaries/figure from the saved raw data. No trajectory rerun.

## Final artifact audit

The independent audit passed: 18 primary source texts have verified saved-text
hashes and page counts; 216 trajectories, 1,080 checkpoint rows, and 153 fresh-trap
tail rows are present. Rational arithmetic reproduces all speed means and SEs
from raw integer displacements. Both the extension scan and file-magic scan
find no saved PDF. Sources contain plain text only. The only retained image
is data/evidence.png, generated from this experiment.

Completed the requested literature review, proof-gap analysis, complete sufficient
reduction and local-tail derivations, and numerical evidence. Full conjecture
unresolved in this work. No publication, pushes, subagents, or global-state writes.
